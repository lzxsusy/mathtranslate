# 面算符

- **id**：`gw06/concept/surface-operator`
- **类型**：concept
- **位置**：§2.1
- **问题**：面算符用什么数据定义，为什么它的参数是连续的而威尔逊算符的标签是离散的？

> 四维规范理论中沿余维二曲面支撑的算符，由希钦方程解在曲面附近的一类奇点定义，带连续参数，是分歧数据的载体。

## 定义

面算符是四维规范理论中支撑在一个二维子流形 $D$ 上的算符（四维中余维为 2）。它的定义方式是：取 $D$ 的法平面上的极坐标 $(r,\theta)$，要求希钦方程的解在 $D$ 附近取形式 $A=\alpha\,d\theta$、$\phi=\beta\,dr/r-\gamma\,d\theta$，其中 $(\alpha,\beta,\gamma)\in\mathbb{T}\times\mathfrak{t}\times\mathfrak{t}$，并模去外尔群的同时共轭作用。$\alpha$ 只在模去余特征格 $\Lambda_{\mathrm{cochar}}$ 的意义下有定义：绕 $D$ 一周的和乐为 $\exp(-2\pi\alpha)$，只有它才是规范不变的。在超对称的 GL 扭曲理论中，这类奇点保持一半超对称，因此是 BPS 算符。

**记号**：$D$：面算符的支撑曲面；$(r,\theta)$：$D$ 法平面上的极坐标；$\mathbb{T}$：极大环面；$\mathfrak{t}=\mathrm{Lie}(\mathbb{T})$；$\Lambda_{\mathrm{cochar}}$：余特征格；$\star$：霍奇星。

## 关键点

- 支撑维数：面算符在四维中余维 2（二维曲面），威尔逊算符与 't Hooft 算符余维 3（一维曲线）。
- 参数是连续三元组 $(\alpha,\beta,\gamma)$；$\alpha$ 取值于环面 $\mathbb{T}$ 并模去余特征格，$\beta$ 与 $\gamma$ 取值于 $\mathfrak{t}$，三者再一起模外尔群。
- $\alpha$ 的周期性与和乐：绕 $D$ 一周的和乐是 $\exp(-2\pi\alpha)$，所以 $\alpha$ 与 $\alpha+\lambda$（$\lambda\in\Lambda_{\mathrm{cochar}}$）给出同一个面算符。
- 奇点必须满足希钦方程（$F-\phi\wedge\phi=0$、$d_A\phi=0$、$d_A\star\phi=0$），这是它保持超对称、成为 BPS 算符的条件。

## 公式

```latex
A = \alpha\, d\theta
```
```latex
\phi = \beta\,\frac{dr}{r} - \gamma\, d\theta
```
```latex
(\alpha,\beta,\gamma) \in \mathbb{T} \times \mathfrak{t} \times \mathfrak{t}
```

## 常见错误

- 把 $\alpha$ 当成 $\mathfrak{t}$ 中的元素而忽略余特征格的周期性：$\alpha$ 与 $\alpha+\lambda_{\mathrm{cochar}}$ 是同一个面算符，忽略这一点会把参数空间算错。
- 忘记同时模去外尔群：$\alpha,\beta,\gamma$ 的共轭化必须一起做，只约化其中一个会得到不存在的“面算符”。
- 把 $\beta$ 与 $\gamma$ 的几何意义互换：$\beta$ 是 $\phi$ 在 $dr/r$ 方向的系数，$\gamma$ 是它在 $d\theta$ 方向的系数；二者在特征多项式的极点系数中扮演不同角色。
- 以为奇点类型唯一决定算符：还需要连续参数，这正是面算符能承载分歧数据的原因。

## 批注

### 易错预警：指数里为什么没有 $i$

本文约定路径有序指数为 $P\exp(-\int A)$，于是 $A=\alpha\,d\theta$ 绕一圈给出$\exp(-2\pi\alpha)$，指数上没有 $i$。若按 $\exp(i\oint A)$ 的约定去读，会把 $\alpha$ 与 $\theta$ 角的关系搞错 $2\pi$ 倍，进而把 $S$-对偶作用读错。

### 含糊点拨：三元组为什么模外尔群

规范群 $G$ 的外尔群来自 $\mathbb{T}$ 在 $G$ 中的共轭作用；把 $(\alpha,\beta,\gamma)$ 同时共轭化不改变奇点的物理内容（只是换了一组基），所以模空间要按 $\mathcal{W}$ 取商。这一步与第 3 节构造 $\MH(\alpha;p)$ 时的商是同一件事。

### 背景直觉：余维二的特殊性

四维中余维二的算符有个独有性质：它不破坏任何平移对称性，且法平面是复一维的，因此奇点可以用一个复坐标 $z=re^{i\theta}$ 上的单极点来描述，参数自然落在环面上。余维三的线算符没有这个自由度，标签只能取表示或余权的离散值。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §2.1；印刷页 [4, 5] / PDF 页 [5, 6]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s02a-definition.tex:34-64`
- 面算符定义与奇点模型 (2.2)；印刷页 4–5，原文 PDF 第 5–6 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
