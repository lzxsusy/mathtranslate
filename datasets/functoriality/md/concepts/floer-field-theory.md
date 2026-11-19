# Floer 场论

> `functoriality/concept/floer-field-theory` ｜ track D ｜ draft

**一句话**：(2+1) 维连通范畴值场论：曲面 X 映到 Fuk#(M(X))，配边 Y 映到拉格朗日对应诱导的 A∞-函子；闭 3-流形不变量由拼接 Floer 上同调给出。

**自测**：Wehrheim–Woodward 的 Floer 场论如何在对象与态射上把三维配边变成 A∞-函子？

## 定义

在 Donaldson、Floer、Fukaya、Salamon–Wehrheim 等人工作的基础上，Wehrheim–Woodward 用拼接 Floer 理论构造了一个 $(2+1)$ 维连通范畴值场论：函子 $\Phi$ 从（紧致连通定向二维流形，三维配边）映到（$\Ainf$-范畴，$\Ainf$-函子的同伦类）。在对象上，曲面 $X$ 送到 $\Fuk^\#(M(X))$，其中 $M(X)$ 是具有固定行列式的中心曲率联络的表示簇，Hodge 配对给它一个单调辛形式；在态射上，初等配边 $Y$ 给出拉格朗日对应 $L(Y)\hookrightarrow M(X_-)^-\times M(X_+)$，再经 $\Phi^\#_{L(Y)}$ 得到 $\Ainf$-函子。

记号：$M(X)$：固定行列式中心曲率联络的表示簇；$L(Y)$：初等配边 $Y$ 对应的拉格朗日对应；$\overline{HF}(Y)$：闭定向三维流形的不变量。

## 要点

- 对象：紧致连通定向曲面 $X$ 映到 $\Fuk^\#(M(X))$，$M(X)$ 是固定行列式中心曲率联络的表示簇，Hodge 配对使它单调。
- 态射：初等配边 $Y$ 映到拉格朗日对应 $L(Y)\hookrightarrow M(X_-)^-\times M(X_+)$，再经 $\Phi^\#_{L(Y)}$ 得到 $\Ainf$-函子；一般配边取初等分解的复合。
- 良定义性：配边分解的无关性由带收缩分析与任意两个分解只差 Cerf 变换推出。
- 闭三维流形不变量：与环面圆柱作连通和后，$\overline{HF}(Y):=H(\hom(\Phi(\overline Y))(\pt),\pt)$，原文括号如此（译者注给出自然读法）。
- 这是转述 [WW20] 的构造，不是本文定理；它属于 Atiyah–Floer 猜想研究史的一部分。

## 公式

$L(Y)\hookrightarrow M(X_-)^-\times M(X_+)$
$\Phi(Y):=\Phi^\#_{L(Y)}:M(X_-)\longrightarrow M(X_+)$
$\overline{HF}(Y):=H\bigl(\hom\bigl(\Phi(\overline Y)\bigr)(\pt),\pt\bigr)$

## 定理与证明

### Floer 场论的存在性（转述 Wehrheim–Woodward [WW20]）

存在函子 $\Phi$，从（紧致连通定向二维流形，三维配边）映到（$\Ainf$-范畴，$\Ainf$-函子的同伦类）；它在曲面上取 $\Fuk^\#(M(X))$，在初等配边上取 $\Phi(Y):=\Phi^\#_{L(Y)}:M(X_-)\longrightarrow M(X_+)$。这是转述 [WW20] 的构造，不是本文证明的定理。

（none；来源：原书 p.56 §5.3（转述 [WW20]））


缺口：原文只概述 [WW20] 的构造，不重复其证明；本卡不把它当作本文定理。

## 易错点

- 把 $\Phi$ 当作严格函子：原文只在 $\Ainf$-函子的同伦类层面陈述，是连通范畴值场论。
- 忽略初等配边分解与 Cerf 变换：一般配边要先验证复合与分解无关。
- 把 $\overline{HF}(Y)$ 的括号按字面读：原文括号如此，按第 2 章的约定应读作 $H(\hom(\Phi(\overline Y)(\pt),\pt))$（译者注）。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§5.3，p.56–56（原书 p.56 §5.3）

关联：`functoriality/concept/quilted-floer`、`functoriality/concept/mww-functor`、`functoriality/concept/phi-sharp`

来源说明：据中译本 §5.3（p.56）与译者注（式 (120) 的括号）转述 [WW20] 的构造。
