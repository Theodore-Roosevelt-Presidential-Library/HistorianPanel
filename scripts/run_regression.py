#!/usr/bin/env python3
"""Score the panel against claims with known answers.

Cases come from tests/regression/examples.yaml (public, format examples) plus
the private file named by HP_CASES (built from the claim ledger; never commit
it). Red-team mutations of true cases are added unless --no-redteam.

Each case:
  id: unique ID
  claim: the claim text
  type: claim type from schemas/claim.schema.json
  context: optional surrounding sentence
  expected: contradicted | supported

The panel never sees `expected`. Claims are sent in batches to
`accuracy-review` in check mode through headless Claude Code.

Scores:
  catch_rate        share of expected-contradicted cases the panel flagged
                    (contradicted or partly_supported)
  false_alarm_rate  share of expected-supported cases the panel flagged
  unverifiable_rate share of all cases left unverifiable (neither right nor wrong)

The run fails if scores fall outside tests/regression/baseline.json.

By default only aggregate scores are printed, because CI logs on a public
repository are public and private case text must not appear in them. Use
--verbose locally to see per-case results.

Usage:
  python scripts/run_regression.py                 # run the panel
  python scripts/run_regression.py --runner fake   # plumbing test, no API calls
  python scripts/run_regression.py --update-baseline
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from redteam_mutate import mutate_cases  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
PLUGIN = REPO / "plugins" / "historian-panel"
EXAMPLES = REPO / "tests" / "regression" / "examples.yaml"
BASELINE = REPO / "tests" / "regression" / "baseline.json"
HISTORY = REPO / "results" / "history"

FLAGGED = {"contradicted", "partly_supported"}
ALLOWED_TOOLS = "Skill,Agent,Task,Read,Write,Glob,Grep,WebSearch,WebFetch"


def load_cases(include_private: bool = True, include_examples: bool = False) -> list[dict]:
    cases = [c for c in (yaml.safe_load(EXAMPLES.read_text()) or [])
             if include_examples or c.get("status") != "illustrative"]
    private = os.environ.get("HP_CASES")
    if include_private and private:
        path = Path(private)
        loaded = yaml.safe_load(path.read_text()) if path.suffix in {".yaml", ".yml"} else json.loads(path.read_text())
        cases += loaded
    seen: set[str] = set()
    for c in cases:
        if c["id"] in seen:
            raise SystemExit(f"duplicate case id {c['id']}")
        if c.get("expected") not in {"contradicted", "supported"}:
            raise SystemExit(f"case {c['id']}: expected must be contradicted or supported")
        seen.add(c["id"])
    return cases


def stratified_sample(cases: list[dict], n: int, seed: int) -> list[dict]:
    """Keep the error / true / red-team mix of the full set in a smaller sample."""
    import random

    rng = random.Random(seed)
    strata: dict[str, list[dict]] = {}
    for c in cases:
        key = "redteam" if "origin" in c else c["expected"]
        strata.setdefault(key, []).append(c)
    out: list[dict] = []
    for group in strata.values():
        k = max(1, round(n * len(group) / len(cases)))
        out += rng.sample(group, min(k, len(group)))
    return out


def to_claims(cases: list[dict]) -> list[dict]:
    """Strip everything the panel must not see."""
    return [{
        "claim_id": c["id"],
        "text": c["claim"],
        "type": c.get("type", "other"),
        "context": c.get("context", c["claim"]),
        "risk": "high",
    } for c in cases]


def run_claude(claims: list[dict], workdir: Path, budget_usd: float | None) -> list[dict]:
    if not shutil.which("claude"):
        raise SystemExit("claude CLI not found; install Claude Code or use --runner fake")
    inp = workdir / "claims.json"
    out = workdir / "verdicts.json"
    inp.write_text(json.dumps(claims, indent=2))
    prompt = (
        f"/historian-panel:accuracy-review check {inp} output={out}\n"
        "Run the full panel (Pass A, blind Pass B, independence audit, Pass C on splits). "
        "Write the final records as a JSON array to the output path. Do not write anything else."
    )
    cmd = ["claude", "--bare", "-p", prompt,
           "--plugin-dir", str(PLUGIN),
           "--output-format", "json",
           "--allowedTools", ALLOWED_TOOLS]
    if budget_usd:
        cmd += ["--max-budget-usd", str(budget_usd)]
    env = dict(os.environ, HP_CONFIG=str(workdir / "config.yaml"))
    (workdir / "config.yaml").write_text(f"ledger_dir: {workdir / 'ledger'}\npass_b_rate: 1.0\n")
    proc = subprocess.run(cmd, cwd=workdir, env=env, capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(f"claude exited {proc.returncode}: {proc.stderr[-2000:]}")
    if not out.exists():
        raise SystemExit("panel did not write the output file")
    return json.loads(out.read_text())


def run_fake(claims: list[dict], cases_by_id: dict[str, dict]) -> list[dict]:
    """Answers every case correctly except red-team cases, which it misses.

    Exercises batching, scoring and reporting without API calls.
    """
    out = []
    for c in claims:
        case = cases_by_id[c["claim_id"]]
        result = case["expected"] if "origin" not in case else "supported"
        out.append({"claim_id": c["claim_id"], "result": result})
    return out


def score(cases: list[dict], finals: list[dict]) -> dict:
    by_id = {f["claim_id"]: f for f in finals}
    errs = [c for c in cases if c["expected"] == "contradicted"]
    trues = [c for c in cases if c["expected"] == "supported"]
    rt = [c for c in errs if "origin" in c]

    def result(c: dict) -> str:
        return by_id.get(c["id"], {}).get("result", "missing")

    caught = sum(result(c) in FLAGGED for c in errs)
    false_alarms = sum(result(c) in FLAGGED for c in trues)
    unverifiable = sum(result(c) == "unverifiable" for c in cases)
    missing = sum(result(c) == "missing" for c in cases)
    rt_caught = sum(result(c) in FLAGGED for c in rt)
    pct = lambda a, b: round(a / b, 4) if b else None  # noqa: E731
    return {
        "cases": len(cases),
        "error_cases": len(errs),
        "true_cases": len(trues),
        "redteam_cases": len(rt),
        "catch_rate": pct(caught, len(errs)),
        "redteam_catch_rate": pct(rt_caught, len(rt)),
        "false_alarm_rate": pct(false_alarms, len(trues)),
        "unverifiable_rate": pct(unverifiable, len(cases)),
        "missing": missing,
    }


def compare(scores: dict, baseline: dict) -> list[str]:
    problems = []
    tol = baseline.get("tolerance", 0.05)
    if scores["missing"]:
        problems.append(f"{scores['missing']} case(s) got no verdict")
    for key, direction in (("catch_rate", "min"), ("redteam_catch_rate", "min"), ("false_alarm_rate", "max")):
        ref = baseline.get(key)
        val = scores.get(key)
        if ref is None or val is None:
            continue
        if direction == "min" and val < ref - tol:
            problems.append(f"{key} {val:.2%} is below baseline {ref:.2%} (tolerance {tol:.0%})")
        if direction == "max" and val > ref + tol:
            problems.append(f"{key} {val:.2%} is above baseline {ref:.2%} (tolerance {tol:.0%})")
    floor = baseline.get("floors", {})
    if scores.get("catch_rate") is not None and scores["catch_rate"] < floor.get("catch_rate", 0):
        problems.append(f"catch_rate below the absolute floor {floor['catch_rate']:.0%}")
    if scores.get("false_alarm_rate") is not None and scores["false_alarm_rate"] > floor.get("false_alarm_rate", 1):
        problems.append(f"false_alarm_rate above the absolute ceiling {floor['false_alarm_rate']:.0%}")
    return problems


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runner", choices=["claude", "fake"], default="claude")
    ap.add_argument("--batch", type=int, default=10)
    ap.add_argument("--no-redteam", action="store_true")
    ap.add_argument("--seed", type=int, default=int(dt.date.today().strftime("%Y%W")),
                    help="red-team seed; defaults to the year and week so mutations rotate weekly")
    ap.add_argument("--budget-usd", type=float, default=None, help="per-batch spending cap")
    ap.add_argument("--sample", type=int, default=0,
                    help="score a stratified random sample of this many cases (pull requests); 0 = all (weekly)")
    ap.add_argument("--update-baseline", action="store_true")
    ap.add_argument("--record", action="store_true", help="write scores to results/history/")
    ap.add_argument("--include-examples", action="store_true",
                    help="also run the illustrative format examples (plumbing tests)")
    ap.add_argument("--verbose", action="store_true", help="print per-case results (local use only)")
    args = ap.parse_args(argv)

    cases = load_cases(include_examples=args.include_examples)
    if not cases:
        print("no scored cases: set HP_CASES to the private case file (or use --include-examples)")
        return 0 if args.runner == "fake" else 1
    if not args.no_redteam:
        cases += mutate_cases(cases, seed=args.seed)
    if args.sample and args.sample < len(cases):
        cases = stratified_sample(cases, args.sample, args.seed)
    by_id = {c["id"]: c for c in cases}
    claims = to_claims(cases)

    finals: list[dict] = []
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(0, len(claims), args.batch):
            batch = claims[i: i + args.batch]
            if args.runner == "fake":
                finals += run_fake(batch, by_id)
            else:
                workdir = Path(tmp) / f"batch{i // args.batch:03d}"
                workdir.mkdir()
                finals += run_claude(batch, workdir, args.budget_usd)

    scores = score(cases, finals)
    scores["date"] = dt.date.today().isoformat()
    scores["runner"] = args.runner
    print(json.dumps(scores, indent=2))

    if args.verbose:
        res = {f["claim_id"]: f.get("result") for f in finals}
        for c in cases:
            mark = "ok " if (res.get(c["id"]) in FLAGGED) == (c["expected"] == "contradicted") else "BAD"
            print(f"{mark} {c['id']}: expected {c['expected']}, got {res.get(c['id'])}")

    if args.record and args.runner == "claude":
        HISTORY.mkdir(parents=True, exist_ok=True)
        (HISTORY / f"{scores['date']}.json").write_text(json.dumps(scores, indent=2) + "\n")

    if args.update_baseline:
        base = json.loads(BASELINE.read_text()) if BASELINE.exists() else {}
        for k in ("catch_rate", "redteam_catch_rate", "false_alarm_rate"):
            base[k] = scores[k]
        base["set_on"] = scores["date"]
        BASELINE.write_text(json.dumps(base, indent=2) + "\n")
        print("baseline updated")
        return 0

    if args.runner == "fake":
        return 0
    baseline = json.loads(BASELINE.read_text()) if BASELINE.exists() else {}
    problems = compare(scores, baseline)
    for p in problems:
        print(f"regression: {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
