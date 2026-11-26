# 22 第一个 Whittaker 系数

- 卡片：`glc/concept/whittaker-coefficient`
- 失效模式：页码/出处定位漂移
- 严重度：minor
- 确认链：A(A7)+B(B2)
- 修复字段：`theorems[0].source`

## 错误版

- `theorems[0].source`：§13.1（讲义未编号的正文陈述）/ 原书 p.64

## 正确版

- `theorems[0].source`：§13.1（讲义未编号的正文陈述）/ 原书 p.65

## 为什么错

`coeff(F):=C_{dR,c}(Bun^Ω_N, p^!(F)⊗ψ^!(exp))` 的定义在 p.64，卡 pages [64] 正确；但「经由到温和商的投影分解」这一基本事实在 p.65，theorem.source 误写 p.64。

## 证据

- E1 glc.pdf p.64 L31 起 §13.1: `coeff(F) := … ∈ Vect`（定义在 p.64）
- E1 glc.pdf p.65 L8-9: `coeff : DMod(BunG) −→ Vect factors through the projection to the tempered quotient`

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 1 处，JSON 变更 2 行；md 镜像同步 1 处

## 形式化提示

定义与基本事实分居两页时，pages 覆盖定义页即可，但 theorem.source 必须指向陈述页。

## 防再犯

`theorems[].source` 指向的是定理/事实的陈述页，不是定义页。
