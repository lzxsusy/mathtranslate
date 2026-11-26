# 定理 16.3 证明里的「膨胀」应为「余限制」

> `raskin_lcft/correction/corestriction` ｜ 原书 p.70 ｜ reviewed

**一句话**：定理 16.3 在非正规子群 H⊆G 上做范数，只有 res 与 cor 有定义且复合等于乘以指数；「膨胀」只对正规子群有定义。

**自测**：为什么这里不能写「膨胀」，只能写「余限制」？

## 初版

```
复合 $\mathrm{res}\circ\mathrm{inf}$ 等于乘以 $[G:H]$。
```

## 改后

```
复合 $\mathrm{res}\circ\mathrm{cor}$ 等于乘以 $[G:H]$（$\mathrm{cor}$ 为余限制）。
```

## 为什么改

$\mathrm{inf}:H^i(G/H,\cdot)\to H^i(G,\cdot)$ 只在 $H\trianglelefteq G$ 时有定义，而定理 16.3 的 $H$ 是任意子群；能对任意 $H$ 定义、且满足「$\mathrm{res}\circ\mathrm{cor}=[G:H]$」的是余限制 $\mathrm{cor}:H^i(H,\cdot)\to H^i(G,\cdot)$。证明正是用这条恒等式把上同调消没在 $G$ 与子群之间搬运。

## 补注

译文径改并加注；原文 p.70 的措辞在非正规情形下不成立。

## 易错点

- 把 $\mathrm{cor}$ 与「转移映射（transfer）」混为一谈：同调层面两者一致，上同调层面是余限制。
- 在 $H$ 正规时以为三者可互换：此时 $\mathrm{inf}$ 与 $\mathrm{cor}$ 仍是不同映射。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 16 讲 Tate 上同调群的消没，p.70–72（原书 p.70）

关联：`raskin_lcft/concept/vanishing-theorem`、`raskin_lcft/concept/brauer-group`

来源说明：勘误来自本次校对（对照 MIT OCW 公开讲义 PDF 逐页核校）；译文用 % [原文疑误：…] 注释留痕，注释不进 PDF。
