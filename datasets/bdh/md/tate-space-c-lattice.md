# Tate 空间与 c-格：Lagrange 三元组的无穷维版

- **id**：`bdh/concept/tate-space-c-lattice`
- **类型**：concept
- **位置**：§4.2
- **问题**：为什么把 Lagrange 三元组里的有限维空间换成 Tate 空间、把两个 Lagrange 子空间换成一个 c-格与一个 d-格之后，Pfaffian 仍然良定义，并且恰好等于 $\operatorname{Pf}(\mathcal Q)$？

> Tate 空间是 $0$ 的邻域基由可公度子空间给出的完备拓扑向量空间；其中开有界的 c-格与离散的 d-格互为对偶，配成 Tate Lagrange 三元组后 Pfaffian 与行列式可推广到无穷维。

## 定义

\emph{Tate 空间}指完备拓扑向量空间，其 $0$ 的邻域基由一族\emph{可公度}的向量子空间构成，即对基中任意 $U_1,U_2$ 有 $\dim U_1/(U_1\cap U_2)<\infty$。向量子空间 $P\subset V$ 称为\emph{有界}的，若对每个开子空间 $U\subset V$ 存在有限集 $\{v_1,\dots,v_n\}\subset V$ 使 $P\subset U+\mathbb Cv_1+\dots+\mathbb Cv_n$；拓扑对偶 $V^*$ 是连续线性泛函空间，其拓扑使 $V$ 的有界子空间的正交补构成 $0$ 的邻域基，且典范态射 $V\to(V^*)^*$ 是同构。坐标模型：设 $\mathcal A$ 是 $I$ 的子集族的一个可公度等价类（元素称半无限子集），$\mathbb C((I,\mathcal A))$ 是形式和 $\sum c_ie_i$（$c_i=0$ 当 $i\notin A$，$A$ 半无限），拓扑由 $\mathbb C[[A]]$ 给出；每个 Tate 空间都同构于某个 $\mathbb C((I,\mathcal A))$。$V$ 中的 \emph{c-格}是开有界子空间；\emph{d-格}是离散子空间 $\Gamma\subset V$，使得对某个 c-格 $P\subset V$ 有 $\Gamma+P=V$（$c,d$ 分别是 compact 与 discrete 的首字母）。d-格（相应地 c-格）总有 c-格（相应地 d-格）补，且 $W^{\perp}\subset V^*$ 保持类型并满足 $(W^{\perp})^{\perp}=W$。$V$ 上的连续双线性型称为\emph{非退化}的，若它诱导拓扑同构 $V\to V^*$；此时 $L^{\perp}=L$ 的子空间称 \emph{Lagrange} 的。\emph{Tate Lagrange 三元组}由带非退化对称双线性型的 Tate 空间 $V$、Lagrange c-格 $L_+\subset V$ 与 Lagrange d-格 $L_-\subset V$ 构成。典型例子来自 $\omega$-正交丛 $\mathcal Q$：对非空有限 $S\subset X$ 置 $V:=\oplus_{x\in S}(\mathcal Q\otimes K_x)$、$L_+:=\oplus_{x\in S}(\mathcal Q\otimes\mathcal O_x)$、$L_-:=\Gamma(X\setminus S,\mathcal Q)$，双线性型取留数之和。此时对任意 c-格 $\Lambda\subset L_+$（$\Lambda\cap L_-=0$）可过渡到有限维三元组 $(\tilde V;\tilde L_+,\tilde L_-)$，而 $\operatorname{Pf}$ 与 $\det$ 不依赖 $\Lambda$，故可定义 $\operatorname{Pf}(V;L_+,L_-)$ 与 $\det(V;L_+,L_-)$；等价地 $\det$ 取复形 $0\to L_-\to V/L_+\to0$ 的行列式，$\operatorname{Pf}$ 用式 (166)/(167)（其中 $\operatorname{Cl}(V)$-模取\emph{离散}模）。于是对上述 $\mathcal Q$ 有 $\operatorname{Pf}(V;L_+,L_-)=\operatorname{Pf}(\mathcal Q)$、$\det(V;L_+,L_-)=\det R\Gamma(X,\mathcal Q)$。相关构造是\emph{费米 Fock 空间} $M=\varinjlim_U\bigwedge(V/U)\otimes\det(L_+/U)^*$（$U$ 遍历 $L_+$ 中的 c-格），即 $V$ 的半无限外幂。族版本（§4.2.14）：Tate $R$-模指同构于 $P\oplus Q^*$ 的拓扑 $R$-模（$P,Q$ 为有限生成投射 $R$-模的直和）；c-格是开有界子模 $P$ 使 $V/P$ 投射，d-格是子模 $\Gamma$ 使某个 c-格 $P$ 满足 $\Gamma\cap P=0$ 且 $V/(\Gamma+P)$ 有限型投射；需 $1/2\in R$（否则改用二次型）。

**记号**：$U_1,U_2$：$0$ 的邻域基中的开子空间；可公度指 $\dim U_1/(U_1\cap U_2)<\infty$、$V^*$：拓扑对偶，其 $0$ 的邻域基为 $V$ 的有界子空间的正交补、$c$-格：开有界子空间（compact 型）；$d$-格：离散 $\Gamma$ 且 $\Gamma+P=V$（discrete 型）、$L_+$：Tate Lagrange 三元组中的 Lagrange c-格；$L_-$：其中的 Lagrange d-格、$\mathcal Q\otimes K_x$、$\mathcal Q\otimes\mathcal O_x$：$\mathcal Q$ 拉回到 $\operatorname{Spec}K_x$、$\operatorname{Spec}\mathcal O_x$ 后的整体截面空间、$\Lambda$：$L_+$ 中的 c-格，用来过渡到有限维三元组；须满足 $\Lambda\cap L_-=0$

## 关键点

- Tate 空间的拓扑是「半无限」的：邻域基里的子空间两两可公度，$\dim U_1/(U_1\cap U_2)$ 有限，但 $U_i$ 本身可以无限维；这使得「开」「有界」「离散」都成为可操作的概念，而无需范数或 Fréchet 结构。
- c-格与 d-格是对偶的两类：c-格开且有界，d-格离散且与某个 c-格合成整个 $V$；正交补把 c-格送到 d-格、d-格送到 c-格，且 $(W^\perp)^\perp=W$。Lagrange 条件 $L^\perp=L$ 要求 $L$ 同时是自对偶的。
- Tate Lagrange 三元组只允许「一个 c-格 + 一个 d-格」：$L_+$ 是 c-格（紧型）、$L_-$ 是 d-格（离散型）。把两者都取成 c-格或都取成 d-格，就无法用有限维三元组逼近，$\operatorname{Pf}$ 的定义失效。
- Pf 与 det 的定义经 $\Lambda$ 中转但不依赖 $\Lambda$：对任意 c-格 $\Lambda\subset L_+$（$\Lambda\cap L_-=0$）取有限维三元组，4.2.11 的函子性保证 $\operatorname{Pf}$、$\det$ 与 $\Lambda$ 无关，于是 Tate 三元组的 Pf 与 det 良定义。
- 例 (181) 是全部讨论的来源：$V=\oplus(\mathcal Q\otimes K_x)$、$L_+=\oplus(\mathcal Q\otimes\mathcal O_x)$、$L_-=\Gamma(X\setminus S,\mathcal Q)$；在此例中 Tate 三元组的 Pf 与 det 恰好还原为 $\operatorname{Pf}(\mathcal Q)$ 与 $\det R\Gamma(X,\mathcal Q)$，把 §4.2.1–4.2.12 的有限维机器接到整体对象上。
- 族版本把「开有界」换成「$V/P$ 投射」、把「离散」换成「$\Gamma\cap P=0$ 且 $V/(\Gamma+P)$ 有限型投射」，并额外要求 $1/2\in R$；过渡用的 $\Lambda$ 还须使 $V/(\Lambda+L_-)$ 投射，等价于 $\Lambda^\perp+L_-=V$。

## 公式

```latex
\dim U_{1}/(U_{1}\cap U_{2})<\infty
```
```latex
V:=\oplus_{x\in S}(\mathcal{Q}\otimes K_{x}),\qquad L_{+}:=\oplus_{x\in S}(\mathcal{Q}\otimes\mathcal{O}_{x}),\qquad L_{-}:=\Gamma(X\setminus S,\mathcal{Q})
```
```latex
\operatorname{Pf}(V;L_{+},L_{-}):=\operatorname{Pf}(\tilde{V};\tilde{L}_{+},\tilde{L}_{-}),\qquad \det(V;L_{+},L_{-}):=\det(\tilde{V};\tilde{L}_{+},\tilde{L}_{-})
```
```latex
M=\varinjlim_{U}\bigwedge(V/U)\otimes\det(L_{+}/U)^{*}
```
```latex
\Lambda^{\perp}+L_{-}=V
```

## 常见错误

- 把 c-格与 d-格对调：$c$ 是 compact（开有界），$d$ 是 discrete。三元组要求 $L_+$ 是 c-格、$L_-$ 是 d-格；若把 $L_+$ 取成离散的，$\Lambda\subset L_+$ 就不可能是含于开有界子空间的 c-格，有限维近似 (178) 无从谈起。
- 把 Tate 空间当成 Banach 或 Fréchet 空间：它的邻域基由可公度子空间给出，坐标模型 $\mathbb C((I,\mathcal A))$ 里的 $\mathcal A$ 是半无限子集族，$\mathbb C[[A]]$ 一般无限余维；用范数直觉会误判「有界」与「开」。
- 忘记 $\Lambda\cap L_-=0$ 这个条件：没有它，$L_-$ 在 $\tilde V$ 中的像不离散，$(\tilde V;\tilde L_+,\tilde L_-)$ 不是有限维 Lagrange 三元组，$\operatorname{Pf}$ 的定义失效。源码在 4.2.11 与 4.2.13 都显式写出这个条件。
- 以为 $\operatorname{Pf}(V;L_+,L_-)$ 依赖所选的 $\Lambda$：源码说「如 4.2.11 所述，$\operatorname{Pf}$ 与 $\det$ 不依赖 $\Lambda$」，独立性来自子商复形的函子性（式 (179) 是同构），不是显然的；把它当成「任选一个 $\Lambda$ 的约定」会掩盖这一定理的实质。
- 在族的情形直接套用点上的定义：4.2.14 要求 $1/2\in R$、$V/P$ 与 $V/(\Gamma+P)$ 投射，以及 $\Lambda^\perp+L_-=V$；并且源码自注这个 Tate $R$-模定义「坏」（对 $\operatorname{Spec}R$ 不是局部的），只对同构于 $V_0\hat\otimes R$ 的情形够用。

## 批注

### 易错预警：c 与 d 的首字母就是定义

源码在 d-格的定义处加了脚注：「c 与 d 分别是「compact」与「discrete」的首字母」。所以 c-格 = 开有界（紧型、可以取商成有限维），d-格 = 离散（可以取交成有限维）。这决定了两条常用性质的方向：$V/W$ 对 c-格 $W$ 是离散的，$W\cap P$ 对 d-格 $W$ 与 c-格 $P$ 是有限维的。把 c 读成 closed 或 coherent，就会在 4.2.14 里把「$V/P$ 投射」误当成拓扑闭性条件。

### 含糊点拨：对偶为什么交换 c 与 d

$W\subset V$ 是开有界子空间时，$W^{\perp}\subset V^*$ 由所有在 $W$ 上消失的连续泛函组成；$W$ 越「大」（越开），$W^\perp$ 越「小」且越离散。源码把这条写成：若 $W$ 是 d-格（相应地 c-格），则 $W^{\perp}\subset V^*$ 也是 d-格（相应地 c-格），且 $(W^{\perp})^{\perp}=W$。这正是 Tate 对偶 $V\cong(V^*)^*$ 的实质内容，也是 $L^\perp=L$ 能同时容纳 c-格与 d-格的原因：Lagrange 自对偶把两类格配成一对。

### 背景直觉：半无限外幂是这套线性代数的目的地

式 (182) 的 $M=\varinjlim_U\bigwedge(V/U)\otimes\det(L_+/U)^*$ 把「越来越大的有限维商的外幂」用 $\det(L_+/U)^*$ 扭成相容系统，得到的直和就是费米 Fock 空间、$V$ 的半无限外幂。源码随后用交换李超代数 $\mathfrak a_{\mathcal O_x}\subset\mathfrak a_{K_x}$（奇部为 $\mathcal Q\otimes\mathcal O_x$、$\mathcal Q\otimes K_x$）解释它：$\operatorname{Cl}(\mathcal Q\otimes K_x)=\mathrm U'\mathfrak a_{K_x}$，$M_x$ 是真空模，而 $\operatorname{Pf}(\mathcal Q)^*$ 是 $\Gamma(X\setminus S,\mathcal Q)$ 在 $\otimes_x M_x$ 上作用的余不变量。也就是说，Tate 空间不是抽象玩具，它是把 $H^0$ 与 $H^1$ 同时装进一个 Clifford 模的容器。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §4.2.13–§4.2.14；印刷页 [142, 146] / PDF 页 [142, 146]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch04.tex:488-552`
- Tate 空间与有界/对偶在 p.142–143，c/d-格与 Tate 三元组在 p.143–144，式 (181) 与 Pf 的定义在 p.144，Fock 空间 (182) 与注在 p.144–145，族版本 4.2.14 与例在 p.145–146；本书 PDF 页 = 印刷页。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
