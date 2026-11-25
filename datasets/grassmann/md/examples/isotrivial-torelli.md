# 等平凡 Torelli 定理

> `grassmann/example/isotrivial-torelli` · 轨道 6 · 曲线上层的算术 · 状态 draft

> **这张卡练什么**：粗模空间明明不刻画 gerbe（例 1.8），为什么叠结构一回来 Torelli 就成立了？

## 一句话

对几何纤维上平凡的 μ_r-gerbe，叠的 μ_r-线性同构与模叠的 μ_r-线性同构等价；证明靠 H² 的截面分裂与引理 1.7 杀类。

## 背景定义

设 $\\mathscr{X}\\to S$ 是 $S$ 上的叠，带包含 $\\boldsymbol{\\mu}_r\\hookrightarrow\\mathscr{I}(\\mathscr{X})$（$\\mathscr{I}$ 为惯性叠）。两个这样的叠 $\\mathscr{X},\\mathscr{Y}$ 之间的 **$\\boldsymbol{\\mu}_r$-线性同构**指同构 $\\iota: \\mathscr{X}\\to\\mathscr{Y}$，使合成
$$\\iota^*\\boldsymbol{\\mu}_r\\xrightarrow{\\sim}\\boldsymbol{\\mu}_r\\hookrightarrow\\mathscr{I}(\\mathscr{X})\\to\\iota^*\\mathscr{I}(\\mathscr{Y})$$
等于给定的 $\\boldsymbol{\\mu}_r\\hookrightarrow\\mathscr{I}(\\mathscr{Y})$；记作 $\\mathscr{X}\\cong_r\\mathscr{Y}$。$C$ 上的 $\\boldsymbol{\\mu}_r$-gerbe $\\mathscr{C}$ 称**在几何纤维上平凡**，若每个几何点 $\\bar s$ 处 $\\mathscr{C}_{\\bar s}\\cong\\mathsf{B}\\boldsymbol{\\mu}_r$。定理断言：两个几何纤维上平凡的 $\\boldsymbol{\\mu}_r$-gerbe 满足 $\\mathscr{C}_1\\cong_r\\mathscr{C}_2$，当且仅当它们在 $C$ 上的稳定模叠满足 $\\mathscr{M}_{\\mathscr{C}_1/S}(r,L)\\cong_r\\mathscr{M}_{\\mathscr{C}_2/S}(r,L)$。

## 设定

设 $f:C\to S$ 是亏格 $g\ge2$、带截面、几何一般纤维无非凡自同构的固有光滑相对曲线；$L$ 在每条几何纤维上次数为 $d$，$r$ 与 $d$ 互素且 $rd$ 为奇数。给定带包含 $\boldsymbol{\mu}_r\hookrightarrow\mathscr{I}(\mathscr{X})$、$\boldsymbol{\mu}_r\hookrightarrow\mathscr{I}(\mathscr{Y})$ 的叠 $\mathscr{X},\mathscr{Y}$，记 $\mathscr{X}\cong_r\mathscr{Y}$ 表示存在同构 $\iota: \mathscr{X}\to\mathscr{Y}$，使
$$\iota^*\boldsymbol{\mu}_r\xrightarrow{\sim}\boldsymbol{\mu}_r\to\mathscr{I}(\mathscr{X})\to\iota^*\mathscr{I}(\mathscr{Y})$$
等于给定的 $\boldsymbol{\mu}_r\to\mathscr{I}(\mathscr{Y})$ 在 $\iota$ 下的拉回；这样的同构称 $\boldsymbol{\mu}_r$-线性的。取 $\mathscr{C}_1,\mathscr{C}_2$ 为 $C$ 上在 $f$ 的几何纤维上均平凡的 $\boldsymbol{\mu}_r$-gerbe。

## 计算

结论（定理 1.9）：$\mathscr{C}_1\cong_r\mathscr{C}_2$ 当且仅当 $\mathscr{M}_{\mathscr{C}_1/S}(r,L)\cong_r\mathscr{M}_{\mathscr{C}_2/S}(r,L)$。

证明路线（四步记账）：
(1) $f$ 有截面，拉回给出自然分裂
$$\mathrm{H}^2(C,\boldsymbol{\mu}_r)=\mathrm{H}^2(S,\boldsymbol{\mu}_r)\oplus\mathrm{H}^1(S,\mathbf{R}^1f_*\boldsymbol{\mu}_r)\oplus\mathrm{H}^0(S,\mathbf{R}^2f_*\boldsymbol{\mu}_r),$$
前两项对应「在几何纤维上平凡」的类；$[\mathscr{C}_i]$ 在 $\mathrm{H}^1(S,\mathbf{R}^1f_*\boldsymbol{\mu}_r)$ 中的像就是与 $M_{\mathscr{C}_i/S}(r,L)$ 相伴的类。
(2) 若 $\mathscr{M}_{\mathscr{C}_1/S}\cong\mathscr{M}_{\mathscr{C}_2/S}$，粗模空间同构，故两个类在 $\mathrm{H}^1(S,\mathbf{R}^1f_*\boldsymbol{\mu}_r)$ 中像相同；于是在 $\mathrm{H}^2(C,\boldsymbol{\mu}_r)$ 中有 $[\mathscr{C}_1]-[\mathscr{C}_2]=[\mathscr{S}]|_C$，其中 $\mathscr{S}\to S$ 是某个 $\boldsymbol{\mu}_r$-gerbe。
(3) 由 Giraud 的理论可写 $\mathscr{C}_1=\mathscr{C}_2\wedge\mathscr{S}_C$，于是有典范同构 $b:M_{\mathscr{C}_1/S}\to M_{\mathscr{C}_2/S}$，并满足 $[\mathscr{M}_{\mathscr{C}_1/S}]-b^*[\mathscr{M}_{\mathscr{C}_2/S}]=[\mathscr{S}]_{M_{\mathscr{C}_1/S}}$。
(4) 由假设 1.3，$M_{\mathscr{C}_1/S}$ 的任意自同构都提升为模叠的 $\boldsymbol{\mu}_r$-线性自同构；把 $b\circ\overline\varphi^{-1}$ 提升，得 $\mathscr{S}_{M_{\mathscr{C}_1/S}}$ 平凡，再由引理 1.7（$\mathrm{Pic}_{X/S}=\mathbf{Z}$ 时 $\mathrm{H}^2(S,\boldsymbol{\mu}_r)\to\mathrm{H}^2(X,\boldsymbol{\mu}_r)$ 单射）得 $[\mathscr{S}]=0$，故 $\mathscr{C}_1\cong_r\mathscr{C}_2$。

## 要点

- 定理的实质是「粗模空间丢掉的信息恰好被 $\mathrm{H}^1(S,\mathbf{R}^1f_*\boldsymbol{\mu}_r)$ 完整记录」，而叠结构能把这个类读回来。
- 反面对照（例 1.8）：$\mathscr{C}=C\times\mathscr{S}$ 时粗模空间同构，但 $[\mathscr{M}_{\mathscr{C}/S}]-[\mathscr{M}_{C/S}]=[\mathscr{S}_{M_{C/S}}]$，除非 $\mathscr{S}\cong\mathsf{B}\boldsymbol{\mu}_{r,S}$，叠不同构。
- 截面假设不可省：分裂 $\mathrm{H}^2(C,\boldsymbol{\mu}_r)=\mathrm{H}^2(S)\oplus\mathrm{H}^1(S,\mathbf{R}^1f_*)\oplus\mathrm{H}^0(S,\mathbf{R}^2f_*)$ 就是靠截面的拉回给出的。
- 引理 1.7 是「杀掉 $\mathscr{S}$」的关键一步，其证明的核是 $\mathrm{H}^0(S,\mathbf{R}^1f_*\boldsymbol{\mu}_r)=\mathrm{H}^1(X,\mathrm{Pic}_{X/S}[r])=0$（原书此处下标有误，见译注）。

## 关键公式

$$
\mathscr{C}_1\cong_r\mathscr{C}_2\iff\mathscr{M}_{\mathscr{C}_1/S}(r,L)\cong_r\mathscr{M}_{\mathscr{C}_2/S}(r,L)
$$

$$
\mathrm{H}^2(C,\boldsymbol{\mu}_r)=\mathrm{H}^2(S,\boldsymbol{\mu}_r)\oplus\mathrm{H}^1(S,\mathbf{R}^1f_*\boldsymbol{\mu}_r)\oplus\mathrm{H}^0(S,\mathbf{R}^2f_*\boldsymbol{\mu}_r)
$$

$$
[\mathscr{C}_1]-[\mathscr{C}_2]=[\mathscr{S}]|_C\ \Longrightarrow\ \mathscr{C}_1=\mathscr{C}_2\wedge\mathscr{S}_C
$$

## 相关定理

- **等平凡 Torelli 定理（定理 1.9）**：在 $f:C\to S$ 带截面、几何一般纤维无非凡自同构、$r$ 与 $d$ 互素且 $rd$ 为奇数、$[\mathscr{C}_i]$ 在几何纤维上平凡的假设下，
$$\mathscr{C}_1\cong_r\mathscr{C}_2\quad\Longleftrightarrow\quad\mathscr{M}_{\mathscr{C}_1/S}(r,L)\cong_r\mathscr{M}_{\mathscr{C}_2/S}(r,L),$$
即「$\\boldsymbol{\\mu}_r$-线性的」叠同构与模叠的 $\\boldsymbol{\\mu}_r$-线性同构互相决定。

## 易错点

- 把结论读成「叠由粗模空间决定」：恰好相反，粗模空间不刻画 gerbe（例 1.8），必须带上 $\boldsymbol{\mu}_r$-线性的叠结构才有 Torelli。
- 漏掉「几何纤维上平凡」：$\mathrm{H}^0(S,\mathbf{R}^2f_*\boldsymbol{\mu}_r)$ 那一项对应沿纤维非平凡的类，不先杀掉它，分裂里前两项与 $M_{\mathscr{C}/S}$ 的对应就不成立。
- 把引理 1.7 的 $\mathrm{H}^1(X,\mathrm{Pic}_{X/S}[r])$ 照抄：原书此处应为 $\mathrm{H}^0(S,\mathrm{Pic}_{X/S}[r])=0$（译注已指出），照抄会得到一个维数不对的群。

## 用到哪些概念

- [等平凡族 / 簇的形式](../concepts/isotrivial-family.md)
- [μ_n-带化的 gerbe](../concepts/gerbe-banded-by-mu-n.md)
- [扭曲层](../concepts/twisted-sheaf.md)

## 相关卡

- [等平凡族 / 簇的形式](../concepts/isotrivial-family.md)
- [μ_n-带化的 gerbe](../concepts/gerbe-banded-by-mu-n.md)
- [扭曲层](../concepts/twisted-sheaf.md)
- [凝聚系](../concepts/coherent-system.md)

## 出处

- ch6 §1 定理 1.9；中译 p.100（英文 PDF p.110），源码 `chapters/ch06.tex:191`
