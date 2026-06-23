# Chinese Academic PPT Maker

A Codex skill for creating, revising, auditing, and rehearsing cautious Chinese academic PowerPoint presentations.

It is designed for:

- lab meeting slides;
- oral research updates;
- project handoff decks;
- reproduction progress reports;
- proposal or defense presentations;
- medical AI, causal inference, RCT, and manuscript-progress presentations.

## What It Includes

- `SKILL.md`: Codex skill entry point and workflow router.
- `references/`: detailed guidance for claim ledgers, deck structures, design, clinical/causal claims, reproduction reporting, oral scripts, and QA.
- `scripts/`: standard-library Python utilities for extracting and linting PPTX text.
- `agents/openai.yaml`: Codex UI metadata.

## Install

Copy the skill folder into your Codex skills directory:

```text
C:\Users\<your-user>\.codex\skills\chinese-academic-ppt-maker
```

On macOS/Linux:

```text
~/.codex/skills/chinese-academic-ppt-maker
```

Restart Codex if the skill list does not refresh automatically.

## Example Prompt

```text
使用 chinese-academic-ppt-maker，帮我做一份中文组会汇报PPT。
材料在 xxx 文件夹，目标是汇报项目复现进展，注意不要夸大外部验证和临床应用。
```

## Utilities

Extract visible text from a PPTX:

```bash
python chinese-academic-ppt-maker/scripts/inspect_pptx_text.py deck.pptx
```

Lint PPTX text for prompt-like phrases and risky scientific claims:

```bash
python chinese-academic-ppt-maker/scripts/lint_pptx_text.py deck.pptx
```

Create a claim-ledger template:

```bash
python chinese-academic-ppt-maker/scripts/make_claim_ledger.py --topic "项目复现进展" --out claim_ledger.md
```

## Notes

This repository does not include private research data, project-specific results, or unpublished manuscripts. It packages only reusable workflow instructions and lightweight QA scripts.
