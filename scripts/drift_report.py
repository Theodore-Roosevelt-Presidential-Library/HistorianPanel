#!/usr/bin/env python3
"""Weekly drift report: are the panel's scores and skills holding up?

Reads aggregate scores in results/history/*.json (no case text), the roster,
and git history, and prints a Markdown report:

- score trend (catch rate, red-team catch rate, false alarms, unverifiable)
- skills added or changed in the last 7 days, and agent-authored share
- skills not touched in 180 days (their source pointers may have rotted)
- roster progress (active vs planned)

Usage: python scripts/drift_report.py > report.md
"""
from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
PLUGIN = REPO / "plugins" / "historian-panel"
HISTORY = REPO / "results" / "history"
STALE_DAYS = 180


def git(*args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def last_touched(path: Path) -> dt.date | None:
    out = git("log", "-1", "--format=%cs", "--", str(path.relative_to(REPO))).strip()
    return dt.date.fromisoformat(out) if out else None


def fmt(v: float | None) -> str:
    return "n/a" if v is None else f"{v:.1%}"


def main() -> int:
    today = dt.date.today()
    lines = [f"# HistorianPanel drift report, week of {today.isoformat()}", ""]

    runs = sorted(HISTORY.glob("*.json"))
    lines.append("## Scores")
    if not runs:
        lines.append("No recorded regression runs yet.")
    else:
        lines.append("| Date | Cases | Catch rate | Red-team catch | False alarms | Unverifiable |")
        lines.append("|------|-------|-----------|----------------|--------------|--------------|")
        for p in runs[-8:]:
            s = json.loads(p.read_text())
            lines.append(f"| {s.get('date', p.stem)} | {s.get('cases')} | {fmt(s.get('catch_rate'))} | "
                         f"{fmt(s.get('redteam_catch_rate'))} | {fmt(s.get('false_alarm_rate'))} | "
                         f"{fmt(s.get('unverifiable_rate'))} |")
        if len(runs) >= 2:
            a, b = (json.loads(p.read_text()) for p in runs[-2:])
            for key, label in (("catch_rate", "Catch rate"), ("false_alarm_rate", "False alarms")):
                if a.get(key) is not None and b.get(key) is not None:
                    delta = b[key] - a[key]
                    lines.append(f"\n{label} moved {delta:+.1%} since the previous run.")
    lines.append("")

    since = (today - dt.timedelta(days=7)).isoformat()
    log = git("log", f"--since={since}", "--name-only", "--format=--%an|%s", "--", "plugins/historian-panel/skills",
              "plugins/historian-panel/agents")
    changed: set[str] = set()
    agent_commits = commits = 0
    for line in log.splitlines():
        if line.startswith("--"):
            commits += 1
            if "agent" in line.lower():
                agent_commits += 1
        elif line.strip():
            parts = Path(line).parts
            if "skills" in parts:
                changed.add(parts[parts.index("skills") + 1])
            elif "agents" in parts:
                changed.add("agent:" + Path(line).stem)
    lines.append("## Changes in the last 7 days")
    lines.append(f"{commits} commit(s) touching skills or agents, {agent_commits} mentioning an agent author.")
    if changed:
        lines.append("Changed: " + ", ".join(sorted(changed)))
    lines.append("")

    roster = yaml.safe_load((PLUGIN / "roster.yaml").read_text())["specialists"]
    active = [e for e in roster if e["status"] == "active"]
    planned = [e for e in roster if e["status"] == "planned"]
    stale = []
    for e in active:
        touched = last_touched(PLUGIN / "skills" / e["name"])
        if touched and (today - touched).days > STALE_DAYS:
            stale.append(f"{e['name']} (last changed {touched})")
    lines.append("## Roster")
    lines.append(f"{len(active)} active, {len(planned)} planned.")
    if stale:
        lines.append(f"Not changed in {STALE_DAYS}+ days; check their source links: " + ", ".join(stale))
    lines.append("")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
