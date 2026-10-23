"""Unit tests for the quality-layer scripts. Run: python -m unittest discover -s tests"""
from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import lint_skills  # noqa: E402
import redteam_mutate  # noqa: E402
import run_regression  # noqa: E402


class RepoIsClean(unittest.TestCase):
    def test_lint_passes(self):
        report = lint_skills.lint(lint_skills.DEFAULT_PLUGIN)
        self.assertEqual(report.errors, [])

    def test_every_ref_is_listed(self):
        listed = {ln.split("\t")[0] for ln in (REPO / "provenance" / "claim-ids.txt").read_text().splitlines()
                  if ln and not ln.startswith("#")}
        cited = set(lint_skills.collect_refs(lint_skills.DEFAULT_PLUGIN))
        self.assertTrue(cited)
        self.assertEqual(cited - listed, set())


class LinterCatchesProblems(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.plugin = self.tmp / "plugin"
        shutil.copytree(lint_skills.DEFAULT_PLUGIN, self.plugin)
        self.skill = self.plugin / "skills" / "sp-badlands" / "SKILL.md"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def errors_after(self, old: str, new: str) -> list[str]:
        text = self.skill.read_text()
        self.assertIn(old, text)
        self.skill.write_text(text.replace(old, new, 1))
        return lint_skills.lint(self.plugin).errors

    def test_untagged_trap(self):
        errs = self.errors_after("[ref: D-25]", "")
        self.assertTrue(any("trap missing" in e for e in errs))

    def test_private_ip(self):
        errs = self.errors_after("## Procedure", "Corpus at 192.168.4.20.\n\n## Procedure")
        self.assertTrue(any("private IP" in e for e in errs))

    def test_long_quotation(self):
        long_quote = '"' + " ".join(["word"] * 30) + '"'
        errs = self.errors_after("## Procedure", long_quote + "\n\n## Procedure")
        self.assertTrue(any("quotation of 30 words" in e for e in errs))

    def test_missing_section(self):
        errs = self.errors_after("## Out of scope", "## Not in scope")
        self.assertTrue(any("specialist sections" in e for e in errs))

    def test_unlisted_skill(self):
        (self.plugin / "skills" / "sp-rogue").mkdir()
        (self.plugin / "skills" / "sp-rogue" / "SKILL.md").write_text("---\nname: sp-rogue\ndescription: x\n---\n")
        errs = lint_skills.lint(self.plugin).errors
        self.assertTrue(any("not listed in roster" in e for e in errs))


class RedTeam(unittest.TestCase):
    CASES = [
        {"id": "a", "claim": "He sailed on May 12, 1869, with his family.", "type": "date", "expected": "supported"},
        {"id": "b", "claim": "It created 51 federal bird reservations.", "type": "number", "expected": "supported"},
        {"id": "c", "claim": "Already wrong in 1900.", "type": "date", "expected": "contradicted"},
    ]

    def test_deterministic(self):
        self.assertEqual(redteam_mutate.mutate_cases(self.CASES, seed=7),
                         redteam_mutate.mutate_cases(self.CASES, seed=7))

    def test_mutates_only_true_cases_and_changes_text(self):
        out = redteam_mutate.mutate_cases(self.CASES, seed=3)
        self.assertEqual({o["origin"].split(":")[0] for o in out}, {"mutation of a", "mutation of b"})
        originals = {c["id"]: c["claim"] for c in self.CASES}
        for o in out:
            self.assertEqual(o["expected"], "contradicted")
            self.assertNotEqual(o["claim"], originals[o["id"].split("-rt")[0]])


class Scoring(unittest.TestCase):
    def test_score_and_compare(self):
        cases = [
            {"id": "e1", "expected": "contradicted"}, {"id": "e2", "expected": "contradicted"},
            {"id": "t1", "expected": "supported"}, {"id": "t2", "expected": "supported"},
        ]
        finals = [{"claim_id": "e1", "result": "contradicted"}, {"claim_id": "e2", "result": "supported"},
                  {"claim_id": "t1", "result": "supported"}, {"claim_id": "t2", "result": "partly_supported"}]
        s = run_regression.score(cases, finals)
        self.assertEqual(s["catch_rate"], 0.5)
        self.assertEqual(s["false_alarm_rate"], 0.5)
        problems = run_regression.compare(s, {"catch_rate": 0.9, "false_alarm_rate": 0.0, "tolerance": 0.05})
        self.assertEqual(len(problems), 2)

    def test_panel_never_sees_expected(self):
        claims = run_regression.to_claims([{"id": "x", "claim": "c", "expected": "supported", "origin": "o"}])
        self.assertNotIn("expected", claims[0])
        self.assertNotIn("origin", claims[0])


if __name__ == "__main__":
    unittest.main()
