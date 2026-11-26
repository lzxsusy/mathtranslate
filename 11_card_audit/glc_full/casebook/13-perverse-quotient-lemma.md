# 13 引理 8.5.2：向量丛经 $\mathbb G_m$-商的推前仍反常

- 卡片：`glc/concept/perverse-quotient-lemma`
- 失效模式：summary 漏前提
- 严重度：minor
- 确认链：A(A4)+arbiter-t1a
- 修复字段：`summary`

## 错误版

- `summary`：若 $\mathcal K$ 是 $\mathbb G_m$-等变、$\pi_*\mathcal K$ 反常，则下降到 $\mathbb P(\mathcal E)$ 后沿 $\bar\pi$ 的 $!$ 推前仍反常。

## 正确版

- `summary`：若 $\mathcal K$ 是 $\mathbb G_m$-等变、$\pi_!\mathcal K$ 与 $\pi_*\mathcal K$ 均反常，则下降到 $\mathbb P(\mathcal E)$ 后沿 $\bar\pi$ 的 $!$ 推前仍反常。

## 为什么错

summary 只写 `π_*K` 反常，漏掉 `π_!K` 反常；同卡 definition/theorem/pitfalls[1] 都要求两者同时成立（p.47：`π! K, π∗ K ∈ Perv(B)`）。

## 证据

- E1 glc.pdf p.47: `Suppose K ∈ Perv(E) is Gm-equivariant and that π! K, π∗ K ∈ Perv(B).`
- 同卡 def/theorem/pitfalls[1] 均要求 π_!K 与 π_*K 同时反常

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 1 处，JSON 变更 2 行；md 镜像同步 1 处

## 形式化提示

形式化时引理前提是合取 `π_!K ∈ Perv(B) ∧ π_*K ∈ Perv(B)`；summary 必须写成合取。

## 防再犯

summary 与 theorem.statement 的前提集合必须逐项对齐。
