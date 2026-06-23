# Intake And Claim Ledger

## Intake Questions

Ask only what is missing and cannot be inferred from files:

- Who is the audience?
- How long is the talk?
- Is this a learning report, reproduction report, manuscript pitch, proposal defense, or update meeting?
- Which claims are safe to report now?
- Which files are authoritative?
- Should the deck be cautious, persuasive, tutorial, or discussion-oriented?

If the user is in a hurry, proceed with reasonable assumptions and state them briefly.

## Claim Ledger

Create a ledger before drafting slides:

| Claim | Status | Evidence | Slide Use | Wording |
|---|---|---|---|---|
| Main result reproduced | Verified | local run/table/path | main result slide | `主实验结果已在本地环境下复现对齐` |
| External validation absent | Verified/Open | meeting transcript/manuscript | limitation slide | `仍缺乏独立外部验证` |
| Clinical deployment | Open | requires prospective study | avoid | do not claim deployment |

Status values:

- `Verified`: supported by local results, source text, or cited paper.
- `Partially verified`: main number or table checked, but not all supplementary outputs.
- `Inferred`: interpretation from evidence, not directly stated.
- `Open`: requires supervisor/data dictionary/external data/rerun.
- `Do not report`: too uncertain, private, or not yet agreed.

## Slide Claim Rule

Every slide title should answer: `What should the audience remember?`

Prefer:

- `主实验结果已复现，验证层级仍需谨慎表述`
- `中心留出验证降低泄漏风险，但不是独立外部验证`

Avoid:

- `结果`
- `方法`
- `数据`
- `讨论`

## Evidence Granularity

For numeric claims, record:

- numerator and denominator;
- population;
- time point;
- whether train, validation, test, or external cohort;
- whether copied from paper, old slides, or reproduced locally.

## Sensitive Claim Handling

When a claim is important but not fully verified, present it as a question or next step:

- `需要确认 BG 的具体采集定义`
- `需要进一步评估测试集中心构成对结果的影响`
- `外部验证数据源仍待老师确认`
