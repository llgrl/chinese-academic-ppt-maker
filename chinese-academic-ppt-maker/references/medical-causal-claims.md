# Medical, Clinical, And Causal Claims

## Required Distinctions

Always distinguish:

- original trial treatment randomization vs ML train/test split;
- internal validation vs held-out center validation vs independent external validation;
- observed factual outcome vs unobserved counterfactual outcome;
- average treatment effect vs subgroup/conditional treatment effect;
- prediction model vs causal treatment effect estimator;
- retrospective secondary analysis vs prospective clinical deployment.

## Validation Language

- `患者级随机切分`: weak for multicenter clinical ML because center leakage may occur.
- `中心留出验证`: test centers did not participate in training.
- `内部中心留出验证`: held-out centers are still from the same parent trial/cohort.
- `独立外部验证`: validation cohort comes from another independent trial, institution system, time period, or dataset.
- `前瞻性验证`: model is evaluated prospectively after development.

Suggested phrase:

`本研究采用 RICAMIS 内部的中心留出验证。测试中心未参与模型训练，因此可减少中心层面的信息泄漏；但由于测试集仍来自同一 RCT，不能等同于独立外部验证。`

## Causal Inference Wording

Use:

- `估计条件平均治疗效应（CATE）`
- `模型预测的获益分层`
- `治疗-推荐交互提示治疗效应异质性`
- `RCT 随机化降低了治疗分配混杂`
- `仍需独立外部验证和前瞻性验证`

Avoid:

- `模型知道每个患者的反事实结果`
- `模型证明某个患者一定会获益`
- `不推荐组受到伤害`
- `可以直接用于临床决策`
- `测试集是外部验证` when it is from the same parent RCT.

## Absolute Risk Difference And NNT

When reporting ARD/NNT:

- define favorable or unfavorable outcome;
- define treatment direction;
- report subgroup denominator;
- avoid interpreting negative NNT casually;
- explain that NNT is a population-level summary, not a deterministic individual prediction.

## Medical Safety

For clinical decks:

- Keep conclusions hypothesis-generating unless prospectively validated.
- Do not recommend treatment changes for real patients.
- Make clear when the analysis is secondary/post hoc.
- Include limitations about population, geography, sample size, missing variables, and external validation.

## Similar Study Comparison

When comparing with benchmark papers:

- identify whether data are RCT or observational;
- identify derivation and validation cohorts;
- identify whether validation is same-trial, held-out center, independent cohort, or independent RCT;
- state feature harmonization issues when external data differ.
