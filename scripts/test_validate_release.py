#!/usr/bin/env python3
"""Regression tests for the release validator."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = Path("scripts/validate_release.py")


class ReleaseValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="interview-skill-validator-")
        self.skill_root = Path(self.temporary.name) / "data-ai-interview-coach"
        shutil.copytree(
            REPOSITORY_ROOT,
            self.skill_root,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_validator(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-X", "utf8", str(VALIDATOR), "."],
            cwd=self.skill_root,
            text=True,
            capture_output=True,
            check=False,
        )

    def assert_rejected(self, expected_message: str) -> None:
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(expected_message, result.stdout)

    def test_valid_release_passes(self) -> None:
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("RELEASE_VALIDATION_OK", result.stdout)

    def test_missing_skill_is_rejected(self) -> None:
        (self.skill_root / "SKILL.md").unlink()
        self.assert_rejected("缺少发布文件：SKILL.md")

    def test_broken_internal_link_is_rejected(self) -> None:
        readme = self.skill_root / "README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8") + "\n[失效链接](missing-file.md)\n",
            encoding="utf-8",
        )
        self.assert_rejected("失效的 Markdown 链接")

    def test_secret_like_value_is_rejected(self) -> None:
        fake_value = "sk-" + "a" * 24
        (self.skill_root / "synthetic-secret.txt").write_text(fake_value, encoding="utf-8")
        self.assert_rejected("发现疑似密钥或私钥")

    def test_real_state_file_is_rejected(self) -> None:
        (self.skill_root / "interview-prep-state.md").write_text(
            "synthetic test state\n", encoding="utf-8"
        )
        self.assert_rejected("公共仓库包含真实状态文件")

    def test_scenario_number_gap_is_rejected(self) -> None:
        path = self.skill_root / "evals/phase-2-scenarios.md"
        text = path.read_text(encoding="utf-8").replace("## 场景 14：", "## 场景 15：")
        path.write_text(text, encoding="utf-8")
        self.assert_rejected("场景编号不连续")


if __name__ == "__main__":
    unittest.main()
