#!/usr/bin/env python3
"""Build ROSTER.md, the friendly guide to the panel, from roster.yaml.

ROSTER.md is generated so it can never drift from the roster. Edit roster.yaml
(title, blurb, routes), then run this script. CI runs it with --check and fails
if ROSTER.md is out of date.

Usage:
  python scripts/build_roster_md.py          # rewrite ROSTER.md
  python scripts/build_roster_md.py --check  # exit 1 if ROSTER.md is stale
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
PLUGIN = REPO / "plugins" / "historian-panel"
OUT = REPO / "ROSTER.md"

GROUP_ORDER = ["workflow", "period", "family", "theme", "collection", "scholarship", "era", "media"]
GROUP_INTROS = {
    "workflow": "They run the review itself. You rarely call them by name; the coordinator does.",
    "period": "Each one knows a stretch of T.R.'s life, and where the records for those years live.",
    "family": "The people closest to T.R., and how they were related.",
    "theme": "Subjects that run through his whole life, plus a few cross-cutting checks.",
    "collection": "Archives and libraries. They know how a collection is organized, what is digitized, and how to cite it.",
    "scholarship": "What has been written about T.R., how reliable it is, and how views have changed.",
    "era": "The world around T.R.: the places, politics and everyday life of his times.",
    "media": "Pictures, film, maps and things.",
}


def build() -> str:
    roster = yaml.safe_load((PLUGIN / "roster.yaml").read_text())
    groups = roster["groups"]
    entries = roster["specialists"]
    active = sum(e["status"] == "active" for e in entries)

    lines = [
        "# Meet the panel",
        "",
        "<!-- Generated from plugins/historian-panel/roster.yaml by scripts/build_roster_md.py. Do not edit by hand. -->",
        "",
        f"HistorianPanel has **{len(entries)} members**: {active} at work and "
        f"{len(entries) - active} planned. Each one is a specialist in one slice of "
        "Theodore Roosevelt's world. None of them answers from memory. They know "
        "*where to look* and *what usually goes wrong*, and they bring back sources.",
        "",
        "You don't need to pick a specialist. Ask Claude to check something "
        "(\"Is this caption right?\", \"Review this page\") and the coordinator "
        "sends each claim to the right two or three members. Every claim gets a "
        "second, blind check from a different member before it is closed.",
        "",
        "To call one directly, name it: *\"Ask the quote specialist whether this "
        "is real.\"*",
        "",
    ]
    for g in GROUP_ORDER:
        members = [e for e in entries if e["group"] == g]
        if not members:
            continue
        lines += [f"## {groups[g]}", "", GROUP_INTROS.get(g, ""), ""]
        lines += ["| Specialist | Ask them about | Status |", "|---|---|---|"]
        for e in members:
            name = e["name"]
            skill = PLUGIN / "skills" / name / "SKILL.md"
            label = f"[{e['title']}](plugins/historian-panel/skills/{name}/SKILL.md)" if skill.exists() else e["title"]
            blurb = e.get("blurb", "").replace("|", "\\|")
            status = "Active" if e["status"] == "active" else "Planned"
            lines.append(f"| {label}<br>`{name}` | {blurb} | {status} |")
        lines.append("")
    lines += [
        "## Want another specialist?",
        "",
        "Ask Claude: *\"Propose a new HistorianPanel specialist for ...\"*. It drafts "
        "the skill as a pull request, the quality checks score it, and a person "
        "merges it. Everyone gets it on the next update.",
        "",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    text = build()
    if args.check:
        if not OUT.exists() or OUT.read_text() != text:
            print("ROSTER.md is out of date: run python scripts/build_roster_md.py")
            return 1
        print("ROSTER.md is current")
        return 0
    OUT.write_text(text)
    print(f"wrote {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
