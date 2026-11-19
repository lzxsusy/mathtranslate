# 稳定丛模空间与余切丛

> `gtgl15/concept/stable-locus` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：$\MH$ 里 $\varphi=0$ 的希格斯丛组成的子空间为什么是 Lagrangian 的，余切丛又为什么只是“开”嵌入？

## 一句话

$\varphi=0$ 把稳定全纯丛模空间 $\mathcal M$ 嵌入 $\MH$，成为 $I$-全纯 Lagrangian 子流形；其余切丛 $T^*\mathcal M$ 在 $\mathcal M$ 附近开嵌入 $\MH$。

## 定义

$\mathcal M\subset\MH$ 是 $\varphi=0$ 的稳定 $G_\mathbb{C}$-丛模空间。遗忘 $\varphi$ 的映射 $\MH\to\mathcal M$ 在 $\mathcal M$ 附近有截面；Hitchin 的局部模型给出 $T^*\mathcal M\hookrightarrow\MH$ 的开嵌入。$\mathcal M$ 的复维数是 $(g-1)\dim G=\frac12\dim_\mathbb{C}\MH$（middle-dimensional）。固定 $E$ 的全纯型（固定 $\bar\partial$ 轨道）的叶也是 $I$-全纯中维子流形，对 $\Omega_I$ Lagrangian。

**记号**：$\mathcal M$；$T^*\mathcal M$；$\Omega_I|_{\mathcal M}=0$。

## 要点（为什么需要它）

1. $\mathcal M\hookrightarrow\MH$ 是 $I$-全纯嵌入，且 $\Omega_I$ 在 $\mathcal M$ 上恒为零（Lagrangian）。
2. $T^*\mathcal M$ 在 $\mathcal M$ 的一个邻域内开嵌入 $\MH$：$\varphi$ 是余切方向的线性化坐标。
3. $\mathcal M$ 的复维数是 $(g-1)\dim G=\frac12\dim_\mathbb{C}\MH$：它是 middle-dimensional 的复 Lagrangian，实余维恰为实维数的一半（这正是复 Lagrangian 的定义）。
4. 叶状结构（固定全纯型）给出另一族 Lagrangian，与 Hecke 作用、't Hooft 算符的边界条件关系密切。
5. $\mathcal M$ 是电中性点集：在 $\mathcal M$ 上只有 Wilson 算符作用，没有 't Hooft 算符的拓扑荷。

## 核心公式

$$
$$\mathcal M\hookrightarrow\MH,\qquad \Omega_I|_{\mathcal M}=0,\qquad T^*\mathcal M\subset\MH\ \text{(开)}$$$$\dim_\mathbb{C}\mathcal M=(g-1)\dim G=\tfrac12\dim_\mathbb{C}\MH$$
$$

$$
$$\dim_\mathbb{C}\mathcal M=(g-1)\dim G=\tfrac12\dim_\mathbb{C}\MH$$
$$

## 定理与证明（或缺口）

### $T^*\mathcal M$ 开嵌入

遗忘 $\varphi$ 的映射给出 $T^*\mathcal M\hookrightarrow\MH$ 的开嵌入；$\Omega_I$ 限制到 $T^*\mathcal M$ 上就是它作为全纯余切丛的自然辛形式。像是开的但不等于 $\MH$（存在底层丛 $E$ 不稳定的稳定希钦对）。

> 证明状态：**gap**。原文 §2.3 一句话引用 Hitchin 的局部模型 [13]，未复述证明。

出处：`A p.7`

## 常见误解

- $T^*\mathcal M\subset\MH$ 是开嵌入，不是整体同构；$\MH$ 的整体拓扑远大于余切丛。
- $\mathcal M$ 是复 Lagrangian，复维数只有 $\MH$ 的一半：别写成“与 $\MH$ 同维”；实余维 $=\frac12\dim_\mathbb{R}\MH$ 正是 Lagrangian 的定义。
- $\mathcal M$ 嵌入依赖 $\varphi=0$ 这一特殊截面，换复结构（例如换成 $J$）就没有同样的嵌入。

## 相关卡

[希格斯丛与希钦对](../concepts/higgs-bundle.md) · [希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [超凯勒商与复结构 I、J、K](../concepts/hyperkahler-quotient.md) · [线算符](../concepts/line-operators.md) · [电本征膜](../concepts/electric-eigenbranes.md)

## 出处（印刷页）

- A p.7（A p.7）
- A p.6（A p.6 eq (2.4)）

> 说明：A=原文 §2.3 关于 $\mathcal M$、$T^*\mathcal M$ 与 Lagrangian 叶的陈述，以及 §2.4 eq (2.6) 的维数；B=把 $\Omega_I|_{\mathcal M}=0$ 显式写出并整理维数；C=“电中性点集”的解释是我们的判断。最没把握处：开嵌入的精确邻域大小原文未界定。
