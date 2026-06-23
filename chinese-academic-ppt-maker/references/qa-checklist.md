# QA Checklist

## Text QA

- No prompt-like visible text:
  - `汇报时建议`
  - `这里可以讲`
  - `不要说`
  - `提示词`
  - `口径如下`
- No unsupported overclaims:
  - `证明`
  - `临床部署`
  - `完全一致`
  - `外部验证完成`
- Technical terms are consistent.
- Numbers match their data split and denominator.
- Unverified claims are marked as open or removed.

## Visual QA

- No text overlap.
- No clipped title/body/table text.
- Every figure has enough resolution.
- Color meaning is consistent.
- Tables are readable at presentation size.
- Slide titles are not too long.
- Dense slides have notes or backup slides.

## Scientific QA

- Data source is named accurately.
- Randomization and train/test split are not confused.
- Validation level is stated correctly.
- Causal claims do not imply observed individual counterfactuals.
- Limitations include missing external/prospective validation when relevant.

## Delivery QA

- Final answer includes the absolute PPTX path.
- Final answer says what was checked.
- Final answer says what was not checked.
- If the user has an upcoming oral report, provide a short safe口径.
