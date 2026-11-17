# GNO 对偶群

> `kw/concept/gno-dual-group` · 轨道 A · 四维物理与对偶 · 状态 dev

> **先自测**：GNO 对偶群是什么，它在整条论证链里起什么作用？

## 一句话

Goddard–Nuyts–Olive 对偶群：电核取 $G$ 的权格、磁核取对偶群 ${}^LG$ 的权格（即 $G$ 的余权格）；它把电磁对偶翻译成群论，也就是 Langlands 对偶群。

## 定义

GNO 对偶群 ${}^LG$ 指规范理论中承载磁荷的群：电核取值于 $G$ 的权格，磁核取值于 ${}^LG$ 的权格，等价地取值于 $G$ 的余权格。Goddard–Nuyts–Olive 1976 年的分析表明磁荷量子化自然给出这个对偶群。

**记号**：$\Lambda_{\rm w}(G)$ 权格、$\Lambda_{\rm cw}(G)$ 余权格；${}^LG$ 为 GNO 对偶群，与 Langlands 对偶群相同。

## 要点（为什么需要它）

1. 没有它，磁荷就没有群论归属，电磁对偶也无法写成 $G\leftrightarrow{}^LG$。
2. 它把『对偶群里承载磁荷』变成可计算的权格/余权格关系，Table 1 的逐项对应由此而来。
3. Atiyah 观察到 GNO 对偶群就是 Langlands 对偶群，这条观察第一次把数论与量子场论接上。
4. 它给出区分同李代数不同群（如 $\mathrm{SU}(N)$ 与 $\mathrm{PSU}(N)$）的物理判据。

## 核心公式

$$
$$\Lambda_{\rm w}({}^LG)=\Lambda_{\rm cw}(G),\qquad \Lambda_{\rm cw}({}^LG)=\Lambda_{\rm w}(G)$$$$\mathrm{SU}(N)\longleftrightarrow\mathrm{PSU}(N)=\mathrm{SU}(N)/\mathbb Z_N$$
$$

$$
$$\mathrm{SU}(N)\longleftrightarrow\mathrm{PSU}(N)=\mathrm{SU}(N)/\mathbb Z_N$$
$$

## 定理与证明（或缺口）

### GNO 电荷量子化

对紧致规范群 $G$，电核取值于权格 $\Lambda_{\rm w}(G)$，磁核取值于对偶群 ${}^LG$ 的权格，即 $\Lambda_{\rm cw}(G)$。

> 证明状态：**gap**。原文 p.2 只叙述 GNO 1976 的结论并引文，未给证明；p.14 再次用 'weight and coweight lattices' 陈述。

出处：`B p.2`

### GNO 对偶群等于 Langlands 对偶群

对每个紧致李群 $G$，其 GNO 对偶群与 Langlands 对偶群 ${}^LG$ 相同；对应由 Table 1 逐项给出，例如 $\mathrm{Sp}(n)\leftrightarrow\mathrm{SO}(2n+1)$。

> 证明状态：**gap**。原文 p.3 归功于 Atiyah 的观察，只列表举例，未给一般证明。

出处：`B p.3`

## 常见误解

- 把 GNO 对偶群当成同一李代数的另一实形式：它一般不同构于 $G$（如 $\mathrm{SU}(N)\leftrightarrow\mathrm{PSU}(N)$）。
- 以为磁荷属于 $G$ 的权格：磁荷在 ${}^LG$ 的权格，也就是 $G$ 的余权格。
- 忽略整体结构：$\mathrm{Spin}(2n)$ 与 $\mathrm{SO}(2n)$ 中心不同，对偶到的群也不同。

## 相关卡

[Langlands 对偶群](../concepts/langlands-dual-group.md) · [电磁对偶](../concepts/electromagnetic-duality.md) · [从 GNO 对偶群到 Langlands 对偶群](../derivations/gno-to-langlands.md) · [非单连通群的 n_g 修正与 Table 1](../derivations/table1-and-ng.md)

## 出处（印刷页）

- B p.2（B p.2）
- B p.3（B p.3）
- B p.14（B p.14）

> 说明：A=原文：GNO 结论、GNO=Langlands 对偶、权格/余权格陈述（B p.2–3、p.14）；C=整理：summary、key_points、pitfalls 与两条定理的 gap 标注。
