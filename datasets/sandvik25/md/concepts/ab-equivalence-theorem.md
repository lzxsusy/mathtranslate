# 主定理：三向等价（定理 5.0.1 与推论 5.0.2）

> `sandvik25/concept/ab-equivalence-theorem` · 轨道 总览 · 状态 dev

> **先自测**：主定理说的是哪两个范畴等价，推论 5.0.2 的五个范畴又是怎么串起来的？

## 一句话

梗概：合成函子 $\mathrm{F}^{\mathrm{IW}}=\mathrm{Av}^{\mathrm{IW}}\circ\mathrm{F}$ 给出 $\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\simeq\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$；由此再得五个范畴两两等价。

## 定义

定理 5.0.1：函子 $\mathrm{F}^{\mathrm{IW}}\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$ 是范畴等价。推论 5.0.2：$\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})$、$\mathcal D^b\mathcal P_I^{\mathrm{asph}}$、$\mathcal D^b\mathcal P_{\mathrm{IW}}$、$\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$、$\mathcal D^b\mathcal P_I$ 五个范畴之间，原文画出的等价关系两两相连。

**记号**：$\mathrm{F}^{\mathrm{IW}}$ 是 $\mathrm{Av}^{\mathrm{IW}}\circ\mathrm{F}$；$\mathrm{F}$ 是 §3.4 从凝聚层到反球侧的全忠实嵌入的上升。

## 要点（为什么需要它）

1. 证明分两半：本质满射由对象对应表（式 (7)）加同调代数得到；全忠实由 $\mathrm{Hom}$ 计算（式 (8)）落到 $\mathcal O_{\widetilde{\mathcal N}}$ 与 $V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)[n]$ 这两种生成元上。
2. 全忠实那一步的关键是两边的 $\mathrm{Hom}$ 维数都等于 $\dim V_{-\lambda}$（$n=0$）或 $0$（$n\ne 0$），一边来自凝聚层的直和分解，一边来自定理 4.5.1 的倾斜层重数。
3. 推论 5.0.2 不是把定理重复五遍：它说明反球侧与 IW 侧由 $\mathrm{Av}^{\mathrm{IW}}$ 连接，而 $\mathrm{Av}^{\mathrm{IW}}$ 在反常层上经反球商分解、并且全忠实。
4. $\mathcal D^b\mathcal P_I$（非反球）也出现在推论里，但 $\mathrm{Fl}_G\to\mathrm{Gr}_G$ 的实现在这种情况下不是等价——原文在 §3.4 末尾特别提醒过。

## 核心公式

$$
$\mathrm{F}^{\mathrm{IW}}:=\mathrm{Av}^{\mathrm{IW}}\circ\mathrm{F}$$\dim\mathrm{Hom}(\mathcal O_{\widetilde{\mathcal N}},V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)[n])=\dim V_{-\lambda}\ (n=0),\quad 0\ (n\ne 0)$
$$

$$
$\dim\mathrm{Hom}(\mathcal O_{\widetilde{\mathcal N}},V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)[n])=\dim V_{-\lambda}\ (n=0),\quad 0\ (n\ne 0)$
$$

## 定理与证明（或缺口）

### 定理 5.0.1（Arkhipov–Bezrukavnikov）

$\mathrm{F}^{\mathrm{IW}}\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$ 是范畴等价。

> 证明状态：**sketch**。原文只给证明梗概；「本质满射」与 $5$-引理的具体同调代数推演未展开。

出处：`A p.12`

## 常见误解

- 定理 5.0.1 的 $\mathrm{F}^{\mathrm{IW}}$ 是**合成**（先 §3.4 的 $\mathrm{F}$，再 $\mathrm{Av}^{\mathrm{IW}}$），不是单个几何构造；把两步混为一谈会看不出反球商在哪里起作用。
- 推论 5.0.2 里的 $\sim$ 不是「都相等」：$\mathcal D^b\mathcal P_I$ 只在中间、且与反球侧的关系是 Serre 商，不是等价。

## 相关卡

[主函子 $F^{\mathrm{IW}}$ 与 Arkhipov–Bezrukavnikov 等价（定理 5.0.1）](../concepts/functor-fiw.md) · [主定理的全忠实：$\mathrm{Hom}$ 两边的显式计算](../derivations/fully-faithful-hom.md) · [反球模的三种描述与三种范畴化](../concepts/three-categorifications.md)

## 出处（印刷页）

- A p.11–12（A p.12）

> 说明：定理陈述与证明梗概出自 p.11–12；对象对应表与 $\mathrm{Hom}$ 计算在 p.11–12 的式 (7)(8)。
