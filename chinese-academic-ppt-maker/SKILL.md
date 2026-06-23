---
name: chinese-academic-ppt-maker
description: Create, revise, audit, and rehearse cautious, polished Chinese academic PowerPoint decks for lab meetings, oral reports, project handoffs, paper reproduction updates, proposal defenses, manuscript progress presentations, clinical/medical AI talks, causal inference talks, and research-to-paper updates. Use when Codex needs to turn research materials, PDFs, transcripts, analysis outputs, figures, code results, existing PPTX files, or old meeting slides into a Chinese PPT/PPTX with clear scientific口径, conservative claims, readable slide structure, speaker notes, visual QA, and text linting.
---

# Chinese Academic PPT Maker

## Routing

Use the minimal reference set needed:

- For every deck: read `references/intake-and-claim-ledger.md` and `references/design-system.md`.
- For medical, clinical, causal inference, RCT, ML, or manuscript decks: also read `references/medical-causal-claims.md`.
- For project handoff or reproduction progress: also read `references/reproduction-reporting.md`.
- For slide ordering and narrative choices: read `references/deck-structures.md`.
- For oral delivery or speaker notes: read `references/oral-script.md`.
- Before final delivery or after editing an existing PPTX: read `references/qa-checklist.md` and run `scripts/lint_pptx_text.py` when possible.

## Operating Modes

### Create

Create a new PPTX from research materials.

1. Build the claim ledger first.
2. Choose a deck structure from `references/deck-structures.md`.
3. Draft slide titles as claims, not topic labels.
4. Create the deck with the Presentations skill or available PPTX tooling.
5. Add speaker notes when the user is preparing to present orally.
6. Run text linting and visual QA.

### Revise

Improve an existing PPTX.

1. Inspect slide text and structure before editing.
2. Preserve user intent and existing data unless asked to redesign.
3. Remove prompt-like phrases, overclaims, and unsupported claims.
4. Improve hierarchy, figure captions, and oral notes.
5. Re-render or inspect after editing.

### Audit

Review a PPTX without changing it.

1. Extract text using `scripts/inspect_pptx_text.py`.
2. Run `scripts/lint_pptx_text.py`.
3. Report findings by severity: wrong claim, unsupported claim, confusing wording, layout risk, missing explanation.
4. Do not edit unless the user explicitly asks.

### Rehearse

Prepare the user to speak.

1. Convert slides into a short oral script.
2. Mark sensitive口径 and what not to overstate.
3. Provide likely questions and compact answers.
4. Keep rehearsal language natural, not manuscript-like.

## Non-Negotiables

- Use 简体中文 by default.
- Never mix original RCT randomization with machine-learning train/test splitting.
- Never call same-parent-trial held-out centers independent external validation.
- Never imply individual counterfactual outcomes are observed.
- Never expose private raw data in a shareable deck unless the user explicitly approves.
- Never leave prompt-like text on slides: `汇报时建议`, `这里可以讲`, `不要说`, `提示词`, `口径如下`.
- Never produce final PPTX without text QA; visual QA is required when tooling permits.

## Scripts

Use the scripts from the skill folder:

```bash
python scripts/inspect_pptx_text.py deck.pptx --json-out deck_text.json
python scripts/lint_pptx_text.py deck.pptx
python scripts/make_claim_ledger.py --topic "项目复现进展" --out claim_ledger.md
```

The scripts use only Python standard library modules and can run without PowerPoint.

## Final Response

When work is complete, report:

- absolute PPTX path;
- sources and result files used;
- QA checks performed;
- unresolved claims or analyses not verified;
- a concise oral口径 if the user will present soon.
