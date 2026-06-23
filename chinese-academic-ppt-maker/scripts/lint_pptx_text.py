#!/usr/bin/env python
"""Lint PPTX visible text for Chinese academic reporting risks."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from inspect_pptx_text import extract_pptx


BANNED_PROMPTLIKE = [
    "汇报时建议",
    "这里可以讲",
    "不要说",
    "提示词",
    "口径如下",
    "怎么讲",
    "内部提示",
]

OVERCLAIM_PATTERNS = [
    ("证明", "Use `提示/支持/观察到` unless the study truly proves causality."),
    ("临床部署", "Avoid deployment claims without prospective validation."),
    ("完全一致", "Use only if every artifact was checked; otherwise say `主结果对齐`."),
    ("外部验证完成", "Check whether validation is independent external validation."),
    ("独立外部验证", "Check if the validation cohort is truly independent."),
]

LONG_LINE_LIMIT = 46


def lint_text(slide: int, text: str) -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    for phrase in BANNED_PROMPTLIKE:
        if phrase in text:
            findings.append(("prompt-like", f"Slide {slide}: contains `{phrase}`"))
    for phrase, advice in OVERCLAIM_PATTERNS:
        if phrase in text:
            findings.append(("overclaim-check", f"Slide {slide}: `{phrase}`. {advice}"))
    for line in text.splitlines():
        compact = line.strip()
        if len(compact) > LONG_LINE_LIMIT and not re.search(r"https?://|[A-Za-z]:\\", compact):
            findings.append(("long-line", f"Slide {slide}: long line ({len(compact)} chars): {compact[:80]}"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    args = parser.parse_args()

    rows = extract_pptx(args.pptx)
    all_findings: list[tuple[str, str]] = []
    for row in rows:
        all_findings.extend(lint_text(row["slide"], row["text"]))

    if not all_findings:
        print("PPTX text lint passed: no prompt-like phrases or obvious overclaim flags found.")
        return 0

    print("PPTX text lint findings:")
    for kind, message in all_findings:
        print(f"- [{kind}] {message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
