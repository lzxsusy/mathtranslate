# Pass A / Pass B 对照

A 记录 154 行，B 记录 52 行。

| 分类 | 卡数 |
|---|---|
| a_issue_only | 12 |
| b_not_sampled | 102 |
| both_issue | 15 |
| both_pass | 25 |

## both_issue（可进入确认）

| id | A group | A sev | B group | B sev | 字段重叠 |
|---|---|---|---|---|---|
| glc/concept/aut-sigma-module | A7 | minor | B1 | minor | sources[0].pages |
| glc/concept/base-whittaker-sheaf | A3 | minor | B2 | minor | summary |
| glc/concept/drinfeld-sokolov-gauge | A7 | minor | B2 | minor | — |
| glc/concept/eisenstein-compatibility | A8 | minor | B3 | minor | theorems[0].source |
| glc/concept/gl1-trace-character | A1 | minor | B1 | minor | — |
| glc/concept/global-langlands-functor | A8 | minor | B3 | minor | theorems[0].source |
| glc/concept/hecke-laumon-eigensheaf | A4 | minor | B2 | minor | sources[0].pages |
| glc/concept/hitchin-base | A7 | minor | B2 | minor | sources[0].pages |
| glc/concept/quantum-local-langlands | A8 | minor | B1 | minor | theorems[0].source |
| glc/concept/restricted-local-systems | A5 | minor | B2 | minor | verification.checks[1].asserts |
| glc/concept/scheme-of-singularities | A5 | minor | B2 | minor | theorems[0].source |
| glc/concept/torsion-stack-local-model | A4 | minor | B1 | minor | theorems[0].source |
| glc/concept/unramified-oper | A8 | minor | B1 | minor | sources[0].pages |
| glc/concept/vanishing-theorem | A3 | major | B2 | major | key_points[1] |
| glc/concept/whittaker-coefficient | A7 | minor | B2 | minor | theorems[0].source |

## a_issue_only（需 arbiter 盲审）

| id | A verdict | B verdict | A sev | B sev |
|---|---|---|---|---|
| glc/concept/affine-grassmannian | issue | pass | minor | None |
| glc/concept/b-lambda-ic | issue | pass | minor | None |
| glc/concept/deligne-gl1-existence | issue | pass | minor | None |
| glc/concept/euler-characteristic-trace-test | issue | pass | minor | None |
| glc/concept/fourier-deligne-transform | issue | pass | minor | None |
| glc/concept/frobenius-twisted-trace | issue | pass | minor | None |
| glc/concept/hecke-laumon-stack | issue | pass | minor | None |
| glc/concept/local-laumon-formula | issue | pass | minor | None |
| glc/concept/local-whittaker-eigenfunction | issue | pass | minor | None |
| glc/concept/perverse-quotient-lemma | issue | pass | minor | None |
| glc/concept/restricted-categorical-langlands | issue | pass | minor | None |
| glc/concept/shv-nilpotent-support | issue | pass | minor | None |

## 第三名盲审仲裁（arbiter）


单方判 issue 的卡（12 张）交第三名 arbiter 盲审；arbiter 同字段判 issue 才确认，判 pass 或只发现其它字段问题的保留为单方发现。

| id | arbiter | 结论 | arbiter 认定字段 | A/B 认定字段 | 处理 |
|---|---|---|---|---|---|
| `affine-grassmannian` | arbiter-t1b | pass | — | sources[0].pages | 单方未修 |
| `b-lambda-ic` | arbiter-t1a | issue | key_points[3]＋pitfalls[0]（Whittaker 归一化名称） | key_points[3] | 确认并修复 |
| `deligne-gl1-existence` | arbiter-t1b | pass | — | definition.notation | 单方未修 |
| `euler-characteristic-trace-test` | arbiter-t1b | pass | — | sources[0].pages | 单方未修 |
| `fourier-deligne-transform` | arbiter-t1b | issue | theorems[0].proof.steps[2].why | theorems[0].proof.steps[2].why | 确认并修复 |
| `frobenius-twisted-trace` | arbiter-t1a | issue | theorems[0].source＋sources.pages | sources[0].pages | 确认并修复 |
| `hecke-laumon-stack` | arbiter-t1a | pass | — | key_points[0] | 单方未修 |
| `local-laumon-formula` | arbiter-t1a | issue | definition.text＋key_points[3]＋theorems[0].proof.steps[7].why＋theorems[0].proof.gap_note | definition.text | 确认并修复 |
| `local-whittaker-eigenfunction` | arbiter-t1b | issue | verification.checks[2] | key_points[4] | 单方未修（arbiter 发现的是另一字段，A 的断言未被第二人认可） |
| `perverse-quotient-lemma` | arbiter-t1a | issue | summary | summary | 确认并修复 |
| `restricted-categorical-langlands` | arbiter-t1b | issue | sources[0].pages / sources[0].anchor / theorems[0].source | sources[0].pages | 确认并修复 |
| `shv-nilpotent-support` | arbiter-t1a | issue | theorems[0].source＋theorems[0].proof.gap_note＋sources.pages | sources[0].pages | 确认并修复 |

## 最终确认

| 状态 | 卡数 | 说明 |
|---|---|---|
| confirmed_fixed | 22 | A+B 或 单方+arbiter 同字段确认，已按 fix_log 修复 |
| single_sided | 5 | 仅一方判 issue，另一判断未认可，不修 |
| unverifiable | 0 | 未能对 E1 来源核验 |
