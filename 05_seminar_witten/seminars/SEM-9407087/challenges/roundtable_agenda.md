# SEM-9407087 圆桌议程

**时间**：2026-11-09 21:45 起
**参与**：r01-physics、r02-math、r03-critique；Chair 主持并裁决
**规则**：
1. 第一轮各自独立作答，**先不读**别人的圆桌稿；每人写 `challenges/roundtable_rXX.md`，400–600 字/题，锚点用 `[src p.N]`/`[eq x.y]`。
2. 三份都交齐后，Chair 把三份发给所有人；每人再写 200–300 字 rebuttal（只挑一处同意、一处反对）。
3. Chair 写 `transcript.md` 的圆桌段与裁决；裁决只认证据，不认投票。

## Q1（证据地位）p42 的“实轴走廊”到底证明了什么？

原文：`sticking to the real u axis, one can come in from the semiclassical region of large u to the singularities at u = ±1 without crossing any jumping curves. Therefore, whatever particles become massless at u = ±1 must evolve continuously from the BPS-saturated states that can be seen semiclassically near infinity.` [src p.42]

请回答：
- 这是“必要性排除”（任何在 u=±1 变无质量的态都必须与半经典 BPS 态连续相连），还是只证明“存在一条不穿越跳跃曲线的路径”？
- 要把它变成严格论证，还缺哪一步？请具体到 (6.22)(6.23) 的渐近级数、§4 的跳跃判据、以及 |u|>1 到 u=±1 的连续性。
- 它是否足以把 §5.3 的“奇点来自磁单极/双荷子”从假设降为“有条件结论”？条件是什么？

## Q2（唯一性）§6 的“唯一解”缺口有多大？

原文：`It will then be clear that this is the unique choice that works.` [src p.38]

请回答：
- (6.16) 的 ansatz `dλ/du=f(u)λ₁`、`f` 为常数、`Im τ>0`、三个 cusp 的渐近，这四者各自是“推出”还是“选择”？
- 如果允许 `f` 在 u=1 有单极点（例如 `f=c+d/(u−1)`），会多出什么解？这些解是被物理排除、还是只是没被讨论？
- §6 的“存在性”是否达到定理级（modulo Clemens 的 Γ(2) 生成性）？“唯一性”应标 proof-gap 还是 open？

## Q3（独立检验）T² 的指数 2 是不是一个独立检验？

p30 说指数 2 来自半经典磁单极的电荷与多重数，因而“independent of the assumption of a Z2 symmetry”。但 r03 认为这只是把一环系数校准，不是独立检验；r01 认为 §5 已由半经典谱固定、§6 只是确认。

请回答：
- p30 的“independent of Z2”在什么意义上成立？它独立于哪些东西、不独立于哪些东西？
- 它能否作为“磁单极假设”的第二个独立证据？还是只是同一套一环输入的另一面？
- 如果要做真正的独立检验，应该拿什么去比什么？

## 裁决记录（Chair 填）

| 题 | 争点 | 裁决 | 依据 |
|---|---|---|---|
| Q1 |  |  |  |
| Q2 |  |  |  |
| Q3 |  |  |  |
