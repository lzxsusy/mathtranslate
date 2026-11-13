# B · 极化与全纯截面（T1）

> 依据：李思《量子力学与几何》中译 5.4.4（印刷 p.304–309；PDF = 印刷 + 12）、Witten §3–3.2（p.366–371）、§2.2（p.359）、§4.3（p.382）。
> 页锚一律印刷页。**标 [补] 者为本报告自写、教材与原文均无对应**（S2 判分要求）。

**一句话**：§3 的答案是"H_Σ = H⁰(M_J, L^{⊗k})"，但这不是"量子态空间"，而是"某个极化下的量子态空间"；"与 J 无关"只到**射影**平坦，所以 H_Σ 只在射影层面典范。

## 一、五问

### 1. 紧相空间为什么不能选 q,p 分离的极化 [src p.368]

原文给的理由是体积：[p.368] "Such a scheme definitely requires a noncompact phase space of infinite volume, since — though the q^i may take values in a compact space — the p_j are definitely unbounded. Accordingly, the space ℋ is infinite dimensional." 反面紧接着一句：[p.368] "since in quantum mechanics there is one quantum state per unit volume in classical phase space, the finiteness of the volume of M means that the quantum Hilbert spaces will be finite dimensional."

教材侧的对照正好是"可行的那个极端"：李思例 5.4.8 [李思 p.306] 在 $M=\mathbb R^{2n}$ 取 $P=\mathrm{span}\{\partial/\partial p_i\}$，$P$-极化截面恰为 $f=f(x)$——这就是 q,p 分离，但它依赖 $M=T^*X$ 的**非紧**结构。

**[补]（教材与原文本句未展开）** 几何上还有一层：紧 $M$ 上不存在 $TM=P\oplus\bar P$ 的全局实分解（那是余切丛的结构）；实极化的叶是 Lagrangian，紧流形上叶空间一般非 Hausdorff（$T^2$ 的无理斜叶层就是反例），"沿叶常值"的截面要么退化、要么不构成好的 Hilbert 空间。所以对 $M_\Sigma$ 来说真正的障碍不是"没有极化"，而是**没有自然的**极化：$M_\Sigma$ 上唯一典范的结构是复结构，任何实极化都得人为选，会破坏映射类群对称性。

### 2. Kähler 极化与"全纯 = 只依赖一半" [李思 p.305–307]

定义 5.4.6 [李思 p.305]：极化是复子丛 $P\subset T^{\mathbb C}M$，满足 ① 每点 $P_z$ 是 Lagrangian（$\dim_{\mathbb C}P=n$、$\omega|_P=0$）；② 可积：$X,Y\in\Gamma(P)\Rightarrow[X,Y]\in\Gamma(P)$；③ $\dim(P_z\cap\bar P_z)$ 为常数。两类：实极化 $P=\bar P$；Kähler 极化 $P\cap\bar P=\{0\}$。截面条件 [李思 p.305]：$\nabla_X s=0,\ \forall X\in P$，即 $P$-极化截面。

Kähler 情形取相容三元组 $(M,J,\omega)$ 与 $P=T^{0,1}M$：李思例 5.4.9 [李思 p.306–307] 在 $\mathbb C^n$ 上取 $P=\mathrm{span}\{\partial/\partial\bar z_i\}$，$P$-极化 $\iff f$ 全纯；$K=|z|^2$ 恰得 Segal–Bargmann 空间。原文 [p.368–369] 同一件事的场论版：$M$ Kähler、辛形式是全纯线丛 $L$ 的第一陈类曲率形式时，"one carries out quantization not by separating the variables ... into 'coordinates' and 'momenta', q's and p's, but by separating them into holomorphic and anti-holomorphic degrees of freedom, essentially $z\sim q+ip$ and $\bar z\sim q-ip$. The quantum Hilbert space is then ... the space of holomorphic sections of the line bundle $L$"，紧则有限维 [p.369]。

**可检验的直观**：$\bar\partial$-方程是 $n$ 个复（$=2n$ 个实）一阶方程，解由半维实切片上的数据唯一决定——自由度砍一半。检验：$\mathbb{CP}^1$ 上 $\mathcal O(k)$ 给 $\dim H^0=k+1$（李思例 5.4.10 [李思 p.308]），与"每单位体积一个态"的 $k^n\mathrm{vol}$ 计数一致（李思例 5.4.11 [李思 p.308–309]）；而**不**极化的 $L^2(M,L)$ 无限维（李思 [p.304] 明说"太大"）。

### 3. "与 J 无关"到底是什么意思 [src p.369–371]

原文自己先承认依赖：[p.370] "our description of ℋ_Σ depends on the choice of J, and what we have called ℋ_Σ might perhaps be better called ℋ_Σ(J). As J varies, the ℋ_Σ(J) vary holomorphically with J"，构成复曲面模空间上的全纯向量丛。想"只依赖 Σ"就需要典范平坦联络；[p.370] 点出这正是 BPZ 微分方程里隐含、Friedan–Shenker 明确提出的"flat vector bundles on moduli space"。

但**不是平坦，是射影平坦**：[p.370] "Because of the conformal anomaly, this bundle has only a projectively flat connection, with the projective factor being canonically odd under reversal of orientation." 单值性也不添麻烦：[p.371] "these monodromies just correspond to an action of the purely topological mapping class group, so that the formal properties of ℋ_Σ are just like those of $H^1(\Sigma,\mathbb R)$."

所以正确读法是：**射影化后的 $\mathbb P\mathcal H_\Sigma$ 才典范**；"与 J 无关"= 射影平坦 + 单值性 = 映射类群作用。教材侧只有一句相关的：不同极化的量子空间由 BKS 核相联系 [李思 p.310]，没有射影平坦丛——这一问主要靠原文 [p.370–371]。[补]

### 4. 半形式 $K^{1/2}$ 与 $k\to k+h^\vee$；本文哪里略去 [src p.359, p.369, p.382]

**[补]（教材无，原文不用此语言）** 严格几何量子化取 $L\otimes K^{1/2}$（$K$ = 极化对应的典范丛/垂直丛），"半形式"保证量子化在 metaplectic 修正下自洽、并给马斯洛夫指标的相位。李思只在 5.2 讲半密度与马斯洛夫修正（据核查表 [李思 p.279–288]），5.4.4 不涉及半形式，故这一段无教材支持。

它的净效果是能级平移 $k\to k+h^\vee$。**本文哪里略去**：§3.1 [p.369] 直接取 $H^0(M_J,L^{\otimes k})$，没有 $K^{1/2}$。但修正以别的形式出现三处：
1. §2 (2.16)–(2.17) [p.359]：$\eta$ 不变量的 APS 公式给 $(\eta(A)-\eta(0))=\frac{1}{2\pi}c_2(G)I(A)$，原文紧接着 "The effect of this factor is to replace $k$ in (2.8) by $k+c_2(G)/2$"；并说这是 1+1 维流代数中 $k\to k+c_2(G)/2$ 的解释的开端 [p.359–360]。$c_2(SU(N))=2N$（原文同页给出归一化）⇒ 平移量 $=N=h^\vee$。
2. §4.3 标架反常修正 (4.20) [p.382]：$\alpha,\beta,\gamma$ 需分别乘 $\exp(-2\pi i h_R)$、$\exp(-4\pi i h_R)$。
3. 最终变量 [eq 4.21, p.382]：$q=\exp(2\pi i/(N+k))$。

**所以 SU(2) 的 $q$ 是 $e^{2\pi i/(k+2)}$，不是 $e^{2\pi i/k}$**——分母的 2 就是 $h^\vee$，与 (2.17) 的 $c_2/2=2$ 对得上 [p.359][p.382]。

### 5. Narasimhan–Seshadri 给了什么 [src p.369]

[p.369]："Once one picks a complex structure $J$ on $\Sigma$, the moduli space $\mathcal M$ of flat connections can be given a new interpretation — it is the moduli space of stable holomorphic $G_{\mathbb C}$ bundles on $\Sigma$ which are topologically trivial ... $\mathcal M_J$ is naturally a complex Kähler (and in fact projective algebraic) variety." $G=SU(N)$ 时即稳定、秩 $N$、$c_1=0$ 的全纯向量丛模空间。

给的三样东西：① **复结构**（依赖 $\Sigma$ 上的 $J$），使"全纯截面"有意义；② **Kähler 且射影代数**，紧性 + 凝聚上同调有限性 ⇒ $\dim H^0<\infty$；③ 平坦联络的辛形式 = **行列式线丛**（Quillen 度规）第一陈类，$k=1$；一般 $k$ 取 $L^{\otimes k}$ [p.369]。

教材对应：李思例 5.4.10 [李思 p.307]——紧复流形 + 厄米全纯线丛、$\omega=i\hbar F_\nabla$、$P=T^{0,1}M$ ⇒ $\mathcal H=H^0(M,L)$ 有限维。**[补]** NS 这个定理名两边都没点（Witten 只引 Atiyah–Bott [33]），是数学侧的名字。

## 二、桥接段（**我们自写，教材无对应**）：$\hbar\leftrightarrow k$

- 李思例 5.4.11 [李思 p.308]：$L=L_0^{\otimes k}$，$F_\nabla=kF_{\nabla_0}=-i(2\pi k)\omega$，**认同 $\hbar=1/(2\pi k)$** 即得预量子化线丛；半经典极限 $\hbar\to0$ 对应 $k\to\infty$。
- 原文 [p.369]：辛形式代表 $c_1(L^{\otimes k})$；$k=1$ 即行列式线丛，一般 $k$ 是 $k$ 次张量幂。
- 故 $2\pi\hbar=1/k$；整性条件 $\frac{1}{2\pi\hbar}\oint\omega\in\mathbb Z$ 就化为 $c_1(L^{\otimes k})$ 整 $\iff k\in\mathbb Z$（S1 的结论）。但注意：原文的 $k$ 同时是 WZW 能级，量子修正后是 $k+h^\vee$；李思的 $k$ 只是张量幂次——两者差一个平移，正是 Q4 的落点。

## 三、最没把握的三点

1. Q1 里"紧 $M$ 上无自然的实极化"：原文只给体积论证 [p.368]，叶空间非 Hausdorff 那半句是我补的 [补]；$T^2$ 有实极化说明命题不能绝对化，措辞已限定为"无自然极化"。
2. Q4 的"半形式 $\Rightarrow k+h^\vee$"我只把原文 p.359 的 $k+c_2/2$ 与 (4.21) 的 $N+k$ 对上，**没有独立推导**；若被追问"为什么恰好 $c_2/2$"，只能答"已知结果，本场未证"。
3. 李思 [p.310] 关于 BKS 核只有一句话，跨极化的空间识别我没细读，Q3 的教材侧因此很薄。

## 四、锚点速查

| 内容 | 锚点 |
|---|---|
| q,p 分离需无限体积、单位体积一态 | [src p.368] |
| Kähler 量化 = 全纯截面、紧⇒有限维 | [src p.368–369] |
| 依赖 $J$、记作 $\mathcal H_\Sigma(J)$、射影平坦、映射类群单值性 | [src p.370]、[src p.371] |
| $k\to k+c_2(G)/2$、$c_2(SU(N))=2N$ | [src p.359] |
| 标架反常修正 (4.20)、$q=e^{2\pi i/(N+k)}$ (4.21) | [src p.382] |
| 极化定义、$P$-极化、相容性 | [李思 p.305] |
| $\mathbb R^{2n}$ 例（$f=f(x)$）、$\mathbb C^n$ 例（全纯、Segal–Bargmann） | [李思 p.306–307] |
| $\mathbb{CP}^1$、$\mathcal O(k)$、$\dim=k+1$、$\hbar=1/(2\pi k)$ | [李思 p.308–309] |
