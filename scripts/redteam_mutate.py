#!/usr/bin/env python3
"""Make deliberately wrong versions of known-true claims, for the red-team test.

Deterministic, not AI: given a seed, the same input always gives the same
mutations. Each mutation changes one checkable detail of a true claim:

- year:    shift a year between 1800 and 1999 by 1 to 3
- number:  change a standalone number (not a year) by a small amount
- month:   swap a month name for a neighboring month
- ordinal: swap an ordinal word (first <-> second, second <-> third ...)

Mutated cases are expected to come back contradicted. A mutation can, rarely,
produce another true statement; the report lists every mutation so a person can
spot those.

Usage: python scripts/redteam_mutate.py cases.yaml [--seed 1] [--per-case 1]
"""
from __future__ import annotations

import argparse
import random
import re
import sys
from pathlib import Path

import yaml

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
ORDINALS = ["first", "second", "third", "fourth", "fifth", "sixth"]

YEAR = re.compile(r"\b(18\d\d|19\d\d)\b")
NUMBER = re.compile(r"(?<![\d.,-])(\d{1,3}(?:,\d{3})*|\d+)(?![\d,])")
MONTH = re.compile(r"\b(" + "|".join(MONTHS) + r")\b")
ORDINAL = re.compile(r"\b(" + "|".join(ORDINALS) + r")\b", re.I)


def _mut_year(text: str, rng: random.Random) -> tuple[str, str] | None:
    hits = list(YEAR.finditer(text))
    if not hits:
        return None
    m = rng.choice(hits)
    old = int(m.group(1))
    new = old + rng.choice([-3, -2, -1, 1, 2, 3])
    return text[: m.start()] + str(new) + text[m.end():], f"year {old} -> {new}"


def _mut_number(text: str, rng: random.Random) -> tuple[str, str] | None:
    hits = [m for m in NUMBER.finditer(text) if not YEAR.fullmatch(m.group(1))]
    if not hits:
        return None
    m = rng.choice(hits)
    raw = m.group(1)
    old = int(raw.replace(",", ""))
    delta = max(1, round(old * rng.choice([0.1, 0.2]))) if old > 10 else 1
    new = old + rng.choice([-delta, delta])
    if new <= 0:
        new = old + delta
    formatted = f"{new:,}" if "," in raw else str(new)
    return text[: m.start()] + formatted + text[m.end():], f"number {raw} -> {formatted}"


def _mut_month(text: str, rng: random.Random) -> tuple[str, str] | None:
    hits = list(MONTH.finditer(text))
    if not hits:
        return None
    m = rng.choice(hits)
    i = MONTHS.index(m.group(1))
    new = MONTHS[(i + rng.choice([-1, 1])) % 12]
    return text[: m.start()] + new + text[m.end():], f"month {m.group(1)} -> {new}"


def _mut_ordinal(text: str, rng: random.Random) -> tuple[str, str] | None:
    hits = list(ORDINAL.finditer(text))
    if not hits:
        return None
    m = rng.choice(hits)
    word = m.group(1)
    i = ORDINALS.index(word.lower())
    j = i + 1 if i + 1 < len(ORDINALS) else i - 1
    new = ORDINALS[j]
    if word[0].isupper():
        new = new.capitalize()
    return text[: m.start()] + new + text[m.end():], f"ordinal {word} -> {new}"


MUTATORS = [_mut_year, _mut_number, _mut_month, _mut_ordinal]


def mutate_cases(cases: list[dict], seed: int = 1, per_case: int = 1) -> list[dict]:
    rng = random.Random(seed)
    out: list[dict] = []
    for case in cases:
        if case.get("expected") != "supported" or case.get("type") == "quote":
            continue  # quotes are mutated by wording, which needs a person
        made = 0
        for mutator in rng.sample(MUTATORS, len(MUTATORS)):
            if made >= per_case:
                break
            result = mutator(case["claim"], rng)
            if result is None:
                continue
            text, how = result
            out.append({
                "id": f"{case['id']}-rt{made + 1}",
                "claim": text,
                "type": case.get("type", "other"),
                "context": text,
                "expected": "contradicted",
                "origin": f"mutation of {case['id']}: {how}",
            })
            made += 1
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cases", type=Path)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--per-case", type=int, default=1)
    args = ap.parse_args(argv)
    cases = yaml.safe_load(args.cases.read_text())
    yaml.safe_dump(mutate_cases(cases, args.seed, args.per_case), sys.stdout, sort_keys=False, allow_unicode=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
