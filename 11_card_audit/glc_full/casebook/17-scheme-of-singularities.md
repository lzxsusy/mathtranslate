# 17 奇异概形与支撑子范畴

- 卡片：`glc/concept/scheme-of-singularities`
- 失效模式：页码/出处定位漂移
- 严重度：minor
- 确认链：A(A5)+B(B2)
- 修复字段：`theorems[0].source`、`theorems[0].proof.gap_note`

## 错误版

- `theorems[0].source`：§10.1 / 原书 p.54
- `theorems[0].proof.gap_note`：讲义只陈述这两个等价（原书 p.54），未给证明；它属于 Arinkin–Gaitsgory 的奇异支撑形式体系（[AG15]）。

## 正确版

- `theorems[0].source`：§10.1 / 原书 p.53
- `theorems[0].proof.gap_note`：讲义只陈述这两个等价（原书 p.53），未给证明；它属于 Arinkin–Gaitsgory 的奇异支撑形式体系（[AG15]）。

## 为什么错

`Coh_0(Y)≃Perf(Y), IndCoh_0(Y)≃QCoh(Y)` 的等价陈述在 p.53 末段；`ch10.tex:42` 才`\srcpage{54}`，卡把 theorem.source 写成 p.54。

## 证据

- E1 glc.pdf p.53 L48-50: `The zero-support category recovers perfect objects: Coh0(Y) ≃ Perf(Y), IndCoh0(Y) ≃ QCoh(Y).`
- ch10.tex:42 才 \srcpage{54}

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 2 处，JSON 变更 4 行；md 镜像同步 2 处

## 形式化提示

pages [53,54] 本身没错（k-线性支撑横跨两页），只需把定理出处改成陈述所在 p.53。

## 防再犯

`theorems[].source` 的页码取陈述句所在页，不取 `\srcpage` 下一行。
