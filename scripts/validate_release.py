#!/usr/bin/env python3
"""Validate the release structure and non-negotiable repository invariants."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "VERSION",
    "agents/openai.yaml",
    "assets/templates/project-deep-dive.md",
    "assets/templates/interview-prep-report.md",
    "assets/templates/interview-prep-state.md",
)

REQUIRED_STATE_FIELDS = (
    'schema_version: "1.2"',
    "checkpoint_type:",
    "checkpoint_reason:",
    "status:",
    "next_action:",
    "artifacts:",
    "migration_notes:",
)

PLACEHOLDER_PATTERN = re.compile(
    r"\b(?:" + "|".join(("TO" + "DO", "FIX" + "ME", "T" + "BD")) + r")\b",
    re.IGNORECASE,
)
SECRET_PATTERNS = (
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(
        r"(?i)(?:api[_-]?key|secret|password|access[_-]?token)\s*[:=]\s*"
        r"['\"][^'\"\r\n]{8,}['\"]"
    ),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)


def read_utf8(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"非 UTF-8 文件：{path} ({exc})")
        return ""


def parse_frontmatter(text: str, errors: list[str]) -> dict[str, str]:
    if not text.startswith("---\n"):
        errors.append("SKILL.md 缺少起始 YAML frontmatter")
        return {}
    try:
        block = text.split("---\n", 2)[1]
    except IndexError:
        errors.append("SKILL.md frontmatter 未闭合")
        return {}

    values: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("'\"")
    return values


def validate_frontmatter(root: Path, errors: list[str]) -> None:
    text = read_utf8(root / "SKILL.md", errors)
    metadata = parse_frontmatter(text, errors)
    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append("SKILL.md 的 name 必须是 1–64 位小写字母、数字或连字符")
    if name and name != root.name:
        errors.append(f"Skill 名称与目录不一致：{name!r} != {root.name!r}")
    if not description:
        errors.append("SKILL.md 缺少 description")
    if len(description) > 1024:
        errors.append("SKILL.md description 超过 1024 个字符")
    for boundary in ("中文", "校招", "不用于英文面试", "编程题"):
        if boundary not in description:
            errors.append(f"Skill description 缺少范围边界：{boundary}")


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = read_utf8(path, errors)
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"失效的 Markdown 链接：{path.relative_to(root)} -> {raw_target}")


def scenario_numbers(text: str) -> list[int]:
    patterns = (
        re.compile(r"^## 场景 (\d+)[:：]", re.MULTILINE),
        re.compile(r"^### (\d+)\. ", re.MULTILINE),
    )
    for pattern in patterns:
        values = [int(value) for value in pattern.findall(text)]
        if values:
            return values
    return []


def validate_evals(root: Path, errors: list[str]) -> int:
    total = 0
    files = sorted((root / "evals").glob("phase-*-scenarios.md"))
    if not files:
        errors.append("缺少阶段行为验收场景")
        return 0
    for path in files:
        text = read_utf8(path, errors)
        numbers = scenario_numbers(text)
        expected = list(range(1, len(numbers) + 1))
        if numbers != expected:
            errors.append(f"场景编号不连续：{path.relative_to(root)} -> {numbers}")
        expectation_count = len(re.findall(r"^期望：", text, re.MULTILINE))
        if expectation_count != len(numbers):
            errors.append(
                f"场景与期望数量不一致：{path.relative_to(root)} "
                f"({len(numbers)} 场景 / {expectation_count} 期望)"
            )
        total += len(numbers)
    if total < 90:
        errors.append(f"阶段验收场景少于发布基线 90：当前 {total}")
    return total


def validate_end_to_end(root: Path, errors: list[str]) -> int:
    path = root / "evals/end-to-end-scenarios.md"
    if not path.is_file():
        errors.append("缺少 V1 端到端验收矩阵")
        return 0
    text = read_utf8(path, errors)
    numbers = [int(value) for value in re.findall(r"^## (\d+)\. ", text, re.MULTILINE)]
    if numbers != list(range(1, 15)):
        errors.append(f"端到端场景必须连续编号 1–14：当前 {numbers}")
    pass_conditions = len(re.findall(r"^通过条件：", text, re.MULTILINE))
    if pass_conditions != len(numbers):
        errors.append(
            f"端到端场景与通过条件数量不一致：{len(numbers)} 场景 / "
            f"{pass_conditions} 通过条件"
        )
    return len(numbers)


def validate_state_template(root: Path, errors: list[str]) -> None:
    path = root / "assets/templates/interview-prep-state.md"
    text = read_utf8(path, errors)
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        errors.append("状态模板缺少完整 YAML frontmatter")
    for field in REQUIRED_STATE_FIELDS:
        if field not in text:
            errors.append(f"状态模板缺少字段：{field}")


def validate_openai_yaml(root: Path, errors: list[str]) -> None:
    text = read_utf8(root / "agents/openai.yaml", errors)
    for field in ("display_name:", "short_description:", "default_prompt:"):
        if field not in text:
            errors.append(f"agents/openai.yaml 缺少字段：{field}")
    if "allow_implicit_invocation: true" not in text:
        errors.append("Skill 应保持默认的隐式调用能力")
    if "$data-ai-interview-coach" not in text:
        errors.append("默认提示未引用正确的 Skill 名称")


def validate_repository_hygiene(root: Path, errors: list[str]) -> None:
    forbidden_suffixes = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".csv", ".key", ".pem"}
    allowed_state = Path("assets/templates/interview-prep-state.md")
    for path in root.rglob("*"):
        if not path.is_file() or any(
            part in {".git", "__pycache__", ".pytest_cache"} for part in path.parts
        ):
            continue
        relative = path.relative_to(root)
        if path.suffix.lower() in forbidden_suffixes:
            errors.append(f"公共仓库包含候选人材料或敏感文件类型：{relative}")
        if path.name == "interview-prep-state.md" and relative != allowed_state:
            errors.append(f"公共仓库包含真实状态文件：{relative}")
        if any(part in {"private", "user-data", "deep-dive"} for part in relative.parts):
            errors.append(f"公共仓库包含应忽略的用户目录：{relative}")

        if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif"}:
            text = read_utf8(path, errors)
            if PLACEHOLDER_PATTERN.search(text):
                errors.append(f"发现未完成占位符：{relative}")
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    errors.append(f"发现疑似密钥或私钥：{relative}")


def validate_required_files(root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"缺少发布文件：{relative}")
    license_text = read_utf8(root / "LICENSE", errors) if (root / "LICENSE").exists() else ""
    if "MIT License" not in license_text:
        errors.append("LICENSE 不是 MIT License")
    version_text = read_utf8(root / "VERSION", errors).strip() if (root / "VERSION").exists() else ""
    if not re.fullmatch(r"\d+\.\d+\.\d+", version_text):
        errors.append(f"VERSION 不是语义化版本：{version_text!r}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Skill 根目录")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []

    validate_required_files(root, errors)
    if (root / "SKILL.md").exists():
        validate_frontmatter(root, errors)
    validate_markdown_links(root, errors)
    scenario_count = validate_evals(root, errors)
    end_to_end_count = validate_end_to_end(root, errors)
    if (root / "assets/templates/interview-prep-state.md").exists():
        validate_state_template(root, errors)
    if (root / "agents/openai.yaml").exists():
        validate_openai_yaml(root, errors)
    validate_repository_hygiene(root, errors)

    if errors:
        print("RELEASE_VALIDATION_FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RELEASE_VALIDATION_OK")
    print(f"skill={root.name}")
    print(f"phase_scenarios={scenario_count}")
    print(f"end_to_end_scenarios={end_to_end_count}")
    print("license=MIT")
    print("state_schema=1.2")
    return 0


if __name__ == "__main__":
    sys.exit(main())
