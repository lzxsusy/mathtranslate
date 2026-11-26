# 21 Gaitsgory 消失定理

- 卡片：`glc/concept/vanishing-theorem`
- 失效模式：逻辑条件反转（放宽方向）
- 严重度：major
- 确认链：A(A3)+B(B2)
- 修复字段：`key_points[1]`

## 错误版

- `key_points[1]`：更一般的界把假设放宽为 $\operatorname{rank}(E)>k$（不再要求 $k<n$ 且 $E$ 几何不可约），界为 $d>(2g-2)k\cdot\operatorname{rank}(E)$；两式是同一增长率的不同写法，不是两个独立条件。

## 正确版

- `key_points[1]`：更一般的界把假设放宽为 $\operatorname{rank}(E)>k$，界为 $d>(2g-2)k\cdot\operatorname{rank}(E)$；两式是同一增长率的不同写法，不是两个独立条件。

## 为什么错

卡称一般形式「不再要求 k<n 且 E 几何不可约」，但讲义 p.36 的一般形式前提是 `rank(E)>k`——这正是 `k<n`（`n=rank(E)`），而且没有去掉 `E` 几何不可约。

## 证据

- E1 glc.pdf p.36 / ch05.tex:117-118: 「更一般地，当 rank(E)>k 时…界为 d>(2g−2)k·rank(E)」
- rank(E)>k 即 k<n（n=rank E），故「不再要求 k<n」为假；原文未去掉 E 几何不可约
- 同卡 theorems[0].statement 仍要求 E 几何不可约

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 1 处，JSON 变更 2 行；md 镜像同步 1 处

## 形式化提示

形式化：`rank(E)>k ↔ k<n`。所谓「放宽」只放宽了下界估计的常数形式（`nk(2g-2)` → `(2g-2)k·rank(E)`），不是放宽前提集合。

## 防再犯

凡写「更一般/放宽」，逐条对照前提列表，确认没有把原前提偷偷保留或删除。
