#!/usr/bin/env python3
"""Check that every [ref: ID] trap tag in a skill points to a qualifying ledger ID.

Public check: the ID must be listed in provenance/claim-ids.txt with status
confirmed, closed or audit.

Private check (optional): if HP_LEDGER points at the private ledger (a JSONL
file whose records carry "claim_id" and "status"), the ID must also be
confirmed or closed there. CI runs the public check; staff with ledger access
can run both.

Also reports IDs listed in claim-ids.txt that no skill cites (a warning only).

Usage: python scripts/check_provenance.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_skills import DEFAULT_PLUGIN, REPO, collect_refs  # noqa: E402

QUALIFYING = {"confirmed", "closed", "audit"}


def load_public_ids(path: Path) -> dict[str, str]:
    ids: dict[str, str] = {}
    for line in path.read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            raise SystemExit(f"{path}: malformed line {line!r}")
        ids[parts[0].strip()] = parts[1].strip()
    return ids


def load_private_ledger(path: Path) -> dict[str, str]:
    statuses: dict[str, str] = {}
    with path.open() as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if "claim_id" in rec and "status" in rec:
                statuses[rec["claim_id"]] = rec["status"]
    return statuses


def main() -> int:
    public = load_public_ids(REPO / "provenance" / "claim-ids.txt")
    refs = collect_refs(DEFAULT_PLUGIN)
    errors: list[str] = []

    for ref, files in sorted(refs.items()):
        where = ", ".join(str(f.relative_to(REPO)) for f in files)
        status = public.get(ref)
        if status is None:
            errors.append(f"{ref} (cited in {where}) is not in provenance/claim-ids.txt")
        elif status not in QUALIFYING:
            errors.append(f"{ref} (cited in {where}) has status {status!r}; needs one of {sorted(QUALIFYING)}")

    ledger_env = os.environ.get("HP_LEDGER")
    if ledger_env:
        private = load_private_ledger(Path(ledger_env))
        for ref in sorted(refs):
            if ref.startswith("audit-"):
                continue
            if private.get(ref) not in {"confirmed", "closed"}:
                errors.append(f"{ref} is not confirmed or closed in the private ledger ({private.get(ref)!r})")
        print(f"checked {len(refs)} refs against the private ledger")

    unused = sorted(set(public) - set(refs))
    for ref in unused:
        print(f"warning: {ref} is listed but no skill cites it")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(refs)} cited ref(s), {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
