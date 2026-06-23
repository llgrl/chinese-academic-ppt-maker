# Reproduction Reporting

## Reproduction Scope Slide

Report in layers:

- environment created;
- dependencies installed;
- data preparation reproduced;
- model training reproduced;
- ensemble/optimization reproduced;
- report tables/figures generated;
- supplementary analyses not yet rerun.

Use cautious wording:

`主实验结果已在本地环境下复现对齐。`

Do not say:

`全部完全一致`

unless every table, figure, seed, image metadata, supplementary output, and timestamp-independent artifact was checked.

## Result Comparison

Use a table:

| 项目 | 原结果 | 当前复现 | 状态 |
|---|---:|---:|---|
| train N | 1301 | 1301 | 对齐 |
| test N | 475 | 475 | 对齐 |
| main metric | ... | ... | 对齐 |
| supplementary bootstrap | 未查 | 未跑 | 待完成 |

## Known Difference Types

Separate meaningful differences from harmless differences:

- `Meaningful`: sample count, feature list, split file, model hyperparameter, metric value.
- `Probably harmless`: timestamp, log order, byte-level PNG metadata, warning text.
- `Needs checking`: library version mismatch, old slide claims, manuscript numbers from old runs.

## Train/Test Split Explanation

Explain:

- whether split is fixed or generated;
- whether split is patient-level, center-level, time-based, or external cohort;
- whether test data participated in feature selection, tuning, or ensemble weight optimization;
- if center-level, whether one large center dominates the test set.

## Oral Summary Template

`目前我完成的是主流程复现，不是所有补充分析的完整复核。主结果表和关键指标已经与原项目对齐；同时我也注意到当前验证属于 RICAMIS 内部中心留出验证，不应表述为独立外部验证。下一步需要继续核对补充分析、变量定义和外部验证可能性。`
