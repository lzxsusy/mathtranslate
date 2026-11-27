# 2026-11-27 修卡案例集（11 例 / 12 条 issue / 23 处改动）

本目录是 `11_card_audit/daily_verify/2026-11-27/` 当日核验的**修卡归档**，独立于
`11_card_audit/casebook/` 的 32 例（后者的 `index.json` 被 `check_casebook.py` 硬编码为 32 条，
按既有约定不再追加，参见 `11_card_audit/glc_full/` 的先例）。

卡片本身已在 `datasets/` 原位置修好；这里保留错误版 / 正确版对照，用于追溯与防回归。

| 案例 | 卡片 | 严重度 | 失效模式 | 改动处 |
|---|---|---|---|---|
| D27-01 | [`siebert/correction/prop-3-12-lci`](siebert__correction__prop-3-12-lci.md) | minor | 出处定位漂移 | 1 |
| D27-02 | [`gtgl15/concept/eigenbranes`](gtgl15__concept__eigenbranes.md) | minor | 定理 / 猜想层级混淆 | 1 |
| D27-03 | [`kw/concept/n4-sym-theory`](kw06__concept__n4-sym-theory.md) | minor | 出处定位漂移 | 1 |
| D27-04 | [`functoriality/concept/strip-shrinking`](functoriality__concept__strip-shrinking.md) | minor | 出处定位漂移 | 3 |
| D27-05 | [`ggl09/deriv/descent-to-xi`](ggl09__deriv__descent-to-xi.md) | major | 逻辑方向反转 | 1 |
| D27-06 | [`siebert/concept/gromov-witten-invariant`](siebert__concept__gromov-witten-invariant.md) | major | 适用范围遗漏 / 条件替换 | 1 |
| D27-07 | [`lbook04/concept/ch9-langlands-spectral`](lbook04__concept__ch9-langlands-spectral.md) | minor | 内部不一致 / 证据归属错误 | 1 |
| D27-08 | [`lbook04/concept/ch3-three-motives`](lbook04__concept__ch3-three-motives.md) | minor | 页覆盖不足 / 出处定位漂移 | 2 |
| D27-09 | [`bzg/concept/categorical-fourier`](benzvi_glc__concept__categorical-fourier.md) | major | 出处无法定位 / 证据强度夸大 | 7 |
| D27-10 | [`gw06/concept/two-dimensional-defect`](gw06__concept__two-dimensional-defect.md) | minor | 页覆盖不足 / 出处定位漂移 | 3 |
| D27-11 | [`glc/concept/fundamental-local-equivalence`](glc__concept__fundamental-local-equivalence.md) | minor | 页覆盖不足 | 2 |

## 与 11-26 批次的关系

- `kw/concept/n4-sym-theory` 是**第二次修改**（11-26 曾把 source 从 `B p.6` 改为 `B p.7–11（…p.11）`；
  本批按页脚修正为 p.10）。按 WORKFLOW §9 在此追加，不改 11-26 的历史 fix_log。
- 其余 10 张卡 11-26 均未改过。
