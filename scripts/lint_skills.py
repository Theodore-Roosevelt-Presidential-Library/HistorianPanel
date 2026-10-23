#!/usr/bin/env python3
"""Lint HistorianPanel skills and agents against reference/skill-standard.md.

No AI involved: these are mechanical checks that run on every pull request.

Exit code 0 when clean, 1 when any error is found. Warnings never fail the run.

Usage: python scripts/lint_skills.py [--plugin plugins/historian-panel]
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
DEFAULT_PLUGIN = REPO / "plugins" / "historian-panel"

SPECIALIST_SECTIONS = [
    "Scope",
    "Out of scope",
    "Where to look first",
    "Known traps",
    "Procedure",
    "Output",
]
MAX_SKILL_CHARS = 16_000
MAX_DESCRIPTION_CHARS = 1_000
MAX_QUOTE_WORDS = 25

TRAP_TAG = re.compile(r"\[(ref:\s*[A-Za-z0-9-]+(\s*,\s*[A-Za-z0-9-]+)*|method|house-rule)\]\s*$")

# Patterns that must never appear in a public repository.
SECRET_PATTERNS = {
    "Anthropic key": re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    "AWS key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "private IP": re.compile(r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b"),
    "home path": re.compile(r"(?:/Users/[A-Za-z]|/home/[a-z]+/|C:\\Users\\)"),
}

QUOTED = re.compile(r"[\"“]([^\"”\n]{20,})[\"”]")


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, path: Path, msg: str) -> None:
        self.errors.append(f"{_rel(path)}: {msg}")

    def warn(self, path: Path, msg: str) -> None:
        self.warnings.append(f"{_rel(path)}: {msg}")


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def load_denylist() -> list[str]:
    """Generic public terms, plus private terms that must not be published.

    Private terms (internal hostnames and the like) would leak if listed in this
    public repo, so they come from the environment: a file named by
    HP_DENYLIST, or newline-separated terms in HP_DENYLIST_TERMS (a CI secret).
    """
    import os

    lines: list[str] = []
    public = REPO / "scripts" / "denylist.txt"
    if public.exists():
        lines += public.read_text().splitlines()
    private_file = os.environ.get("HP_DENYLIST")
    if private_file and Path(private_file).exists():
        lines += Path(private_file).read_text().splitlines()
    lines += os.environ.get("HP_DENYLIST_TERMS", "").splitlines()
    return sorted({ln.strip().lower() for ln in lines if ln.strip() and not ln.strip().startswith("#")})


def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    try:
        meta = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return None, text
    return meta, text[end + 4 :]


def sections(body: str) -> list[tuple[str, str]]:
    """Return (heading, content) for each '## ' heading, in order."""
    parts = re.split(r"^## +(.+?)\s*$", body, flags=re.M)
    out = []
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1]))
    return out


def check_public_safety(path: Path, text: str, report: Report, denylist: list[str]) -> None:
    for label, pattern in SECRET_PATTERNS.items():
        for m in pattern.finditer(text):
            report.error(path, f"possible {label}: {m.group(0)[:40]!r}")
    lowered = text.lower()
    for term in denylist:
        if term in lowered:
            report.error(path, f"denylisted term present: {term!r}")
    _, body = parse_frontmatter(text)
    for m in QUOTED.finditer(body):
        words = len(m.group(1).split())
        if words > MAX_QUOTE_WORDS:
            report.error(path, f"quotation of {words} words (limit {MAX_QUOTE_WORDS}); cite instead of quoting")


def check_traps(path: Path, content: str, report: Report) -> list[str]:
    refs: list[str] = []
    bullets = re.split(r"^- ", content, flags=re.M)[1:]
    if not bullets:
        report.error(path, "## Known traps has no bullets")
    for b in bullets:
        flat = " ".join(b.split())
        m = TRAP_TAG.search(flat)
        if not m:
            report.error(path, f"trap missing [ref: ID], [method] or [house-rule] tag at end: {flat[:70]!r}")
            continue
        tag = m.group(1)
        if tag.startswith("ref:"):
            refs.extend(x.strip() for x in tag[4:].split(","))
    return refs


def lint(plugin: Path) -> Report:
    report = Report()
    denylist = load_denylist()

    roster_path = plugin / "roster.yaml"
    roster = yaml.safe_load(roster_path.read_text())
    entries = {e["name"]: e for e in roster.get("specialists", [])}
    if len(entries) != len(roster.get("specialists", [])):
        report.error(roster_path, "duplicate names in roster")
    groups = set(roster.get("groups", {}))

    skills_dir = plugin / "skills"
    skill_dirs = {p.name: p for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.exists() else {}

    for name, entry in entries.items():
        if entry.get("group") not in groups:
            report.error(roster_path, f"{name}: unknown group {entry.get('group')!r}")
        status = entry.get("status")
        if status not in {"active", "planned"}:
            report.error(roster_path, f"{name}: status must be active or planned")
        if status == "active" and name not in skill_dirs:
            report.error(roster_path, f"{name}: active but skills/{name}/ is missing")
        if status == "planned" and name in skill_dirs:
            report.error(roster_path, f"{name}: has a skill folder but is still marked planned")
        if not entry.get("blurb"):
            report.error(roster_path, f"{name}: needs a plain-language blurb for ROSTER.md")
        if status == "active" and name.startswith("sp-") and not entry.get("routes"):
            report.error(roster_path, f"{name}: active specialist needs routes")

    for name, d in sorted(skill_dirs.items()):
        skill_md = d / "SKILL.md"
        if name not in entries:
            report.error(d, "skill folder not listed in roster.yaml")
        if not skill_md.exists():
            report.error(d, "missing SKILL.md")
            continue
        text = skill_md.read_text()
        meta, body = parse_frontmatter(text)
        if meta is None:
            report.error(skill_md, "missing or invalid frontmatter")
            continue
        if meta.get("name") != name:
            report.error(skill_md, f"frontmatter name {meta.get('name')!r} must equal folder name {name!r}")
        desc = str(meta.get("description") or "")
        if not desc:
            report.error(skill_md, "missing description")
        elif len(desc) > MAX_DESCRIPTION_CHARS:
            report.error(skill_md, f"description is {len(desc)} chars (limit {MAX_DESCRIPTION_CHARS})")
        if len(text) > MAX_SKILL_CHARS:
            report.error(skill_md, f"SKILL.md is {len(text)} chars (limit {MAX_SKILL_CHARS}); move detail to references/")
        if "panel-rules.md" not in body:
            report.error(skill_md, "must tell the reader to read reference/panel-rules.md")
        check_public_safety(skill_md, text, report, denylist)

        for extra in d.rglob("*"):
            if extra.is_file() and extra != skill_md and extra.suffix in {".md", ".txt", ".yaml", ".json"}:
                check_public_safety(extra, extra.read_text(errors="replace"), report, denylist)

        if name.startswith("sp-"):
            found = sections(body)
            headings = [h for h, _ in found]
            expected = [h for h in headings if h in SPECIALIST_SECTIONS]
            if expected != SPECIALIST_SECTIONS:
                report.error(skill_md, f"specialist sections must be, in order: {SPECIALIST_SECTIONS}; found {expected}")
            content = dict(found)
            if "Known traps" in content:
                check_traps(skill_md, content["Known traps"], report)
            if "Output" in content and "panel-rules.md section 11" not in content["Output"]:
                report.error(skill_md, "## Output must point to reference/panel-rules.md section 11")

    agents_dir = plugin / "agents"
    for agent in sorted(agents_dir.glob("*.md")) if agents_dir.exists() else []:
        text = agent.read_text()
        meta, _ = parse_frontmatter(text)
        if meta is None:
            report.error(agent, "missing or invalid frontmatter")
            continue
        if meta.get("name") != agent.stem:
            report.error(agent, "frontmatter name must equal file name")
        if not meta.get("description"):
            report.error(agent, "missing description")
        if ":" in str(meta.get("name", "")):
            report.error(agent, "agent name may not contain ':'")
        check_public_safety(agent, text, report, denylist)

    for ref_file in (plugin / "reference").glob("*.md"):
        check_public_safety(ref_file, ref_file.read_text(), report, denylist)

    return report


def collect_refs(plugin: Path) -> dict[str, list[Path]]:
    """All [ref: ...] IDs cited by specialist skills, mapped to the files citing them."""
    refs: dict[str, list[Path]] = {}
    for skill_md in sorted((plugin / "skills").glob("sp-*/SKILL.md")):
        _, body = parse_frontmatter(skill_md.read_text())
        content = dict(sections(body))
        if "Known traps" not in content:
            continue
        scratch = Report()
        for ref in check_traps(skill_md, content["Known traps"], scratch):
            refs.setdefault(ref, []).append(skill_md)
    return refs


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plugin", type=Path, default=DEFAULT_PLUGIN)
    args = ap.parse_args(argv)
    report = lint(args.plugin)
    for w in report.warnings:
        print(f"warning: {w}")
    for e in report.errors:
        print(f"error: {e}")
    print(f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
