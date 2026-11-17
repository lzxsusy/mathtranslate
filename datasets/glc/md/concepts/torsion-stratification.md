---
id: glc/concept/torsion-stratification
type: concept
track: C
---

# 挠层叠的按分拆分层（整体与局部）

> $\operatorname{Tor}^d$ 按分拆分成局部闭子叠，循环层 $\operatorname{Tor}^{(d)}$ 是开的；局部地 $\operatorname{Tor}_x^\lambda$ 对应阶梯挠层。

**问题**：$\operatorname{Tor}^d$ 的按分拆分层如何由对称幂的图册描述，$x$ 处的局部层 $\operatorname{Tor}_x^\lambda$ 对应什么挠层？

## 定义

令 $\operatorname{Part}^d=\{(d_1\ge d_2\ge\cdots\ge d_s>0)\mid d_1+\cdots+d_s=d\}$，置 $d_{s+1}=0$。叠 $\operatorname{Tor}^d$ 按局部闭子叠 $\operatorname{Tor}^{(d_1,\ldots,d_s)}$ 分层：由 $(d_1,\ldots,d_s)$ 标记的层是 $X^{(d_1-d_2)}\times X^{(d_2-d_3)}\times\cdots\times X^{(d_s)}\to\operatorname{Tor}^d$ 的像，其中 $(D_1,\ldots,D_s)\mapsto\mathcal{O}_{D_1+\cdots+D_s}\oplus\mathcal{O}_{D_2+\cdots+D_s}\oplus\cdots\oplus\mathcal{O}_{D_s}$。分层 $\operatorname{Tor}^{(d)}$ 是开的，它是 $X^{(d)}\to\operatorname{Tor}^d$、$D\mapsto\mathcal{O}_D$ 的像。局部地，$x$ 处的层是剩余部分 $\operatorname{Tor}_x^\lambda\subset\operatorname{Tor}_x^d$，对应于挠层 $T_{\lambda,x}:=\bigoplus_{i=1}^s\mathcal{O}_X/\mathcal{O}_X(-\lambda_i x)$；等价地，过渡到完备局部环并选取素元 $t$ 后它是 $k[[t]]$-模 $\bigoplus_{i=1}^s k[[t]]/(t^{\lambda_i})$。

*记号*：$X^{(m)}$ 为 $X$ 的 $m$ 次对称幂；$X^{(d)}-\Delta$ 为去掉对角线的开部分；对有效除子 $D$ 记 $\mathcal{O}_D:=\mathcal{O}_X/\mathcal{O}_X(-D)$；$\lambda=(\lambda_1\ge\cdots\ge\lambda_s>0)\vdash d$，$|\lambda|=d$，$\ell(\lambda)=s$。

## 要点

- 分拆 $(d_1,\ldots,d_s)$ 记录挠层各层支撑的厚度：第 $i$ 个因子 $\mathcal{O}_{D_i+\cdots+D_s}$ 在 $D_1+\cdots+D_{i-1}$ 之上又叠了一层，所以图册是各个对称幂的乘积，$d_{s+1}=0$ 只是为了写统一公式。
- $\operatorname{Tor}^{(d)}$ 是开的：它由循环挠层 $\mathcal{O}_D$ 组成。对 $X=\mathbb{A}^1$ 这给出 $\operatorname{Tor}^{(d)}\simeq\mathfrak{gl}_d^{\mathrm{reg}}/\operatorname{GL}_d$、$\operatorname{Tor}^{(d)}|_{X^{(d)}-\Delta}\simeq\mathfrak{gl}_d^{\mathrm{rss}}/\operatorname{GL}_d$、$X^{(d)}\simeq\mathfrak{t}_d/W$，因此挠层叠是曲线情形下对 $\mathfrak{gl}_d$ 的伴随商图景的类比。
- 局部分层只保留支撑在 $x$ 的剩余部分：$\operatorname{Tor}_x^\lambda$ 对应 $T_{\lambda,x}=\bigoplus_i\mathcal{O}_X/\mathcal{O}_X(-\lambda_i x)$，即把 $d$ 的每一块 $\lambda_i$ 在 $x$ 处堆成阶梯。
- 讲义指出叠 $\operatorname{Tor}_x^d$ 的维数为 $-d$；在幂零锥模型下各分层是幂零轨道的商叠，负维数按「维数减群维数」计（译注 §4.8 给出该算法）。

## 关键公式

- $\operatorname{Part}^d=\{(d_1\ge d_2\ge\cdots\ge d_s>0)\mid d_1+\cdots+d_s=d\}$
- $X^{(d_1-d_2)}\times X^{(d_2-d_3)}\times\cdots\times X^{(d_s)}\longrightarrow\operatorname{Tor}^d$
- $(D_1,\ldots,D_s)\longmapsto\mathcal{O}_{D_1+\cdots+D_s}\oplus\mathcal{O}_{D_2+\cdots+D_s}\oplus\cdots\oplus\mathcal{O}_{D_s}$
- $\operatorname{Tor}^{(d)}\simeq\mathfrak{gl}_d^{\mathrm{reg}}/\operatorname{GL}_d,\qquad\operatorname{Tor}^{(d)}|_{X^{(d)}-\Delta}\simeq\mathfrak{gl}_d^{\mathrm{rss}}/\operatorname{GL}_d,\qquad X^{(d)}\simeq\mathfrak{t}_d/W$
- $T_{\lambda,x}=\bigoplus_{i=1}^s\mathcal{O}_X/\mathcal{O}_X(-\lambda_i x)\ \simeq\ \bigoplus_{i=1}^s k[[t]]/(t^{\lambda_i})$
- $\dim\operatorname{Tor}_x^d=-d$

## 定理与证明

### 按分拆分层与 $\mathbb{A}^1$ 对照（要点（有缺口））

叠 $\operatorname{Tor}^d$ 按局部闭子叠 $\operatorname{Tor}^{(d_1,\ldots,d_s)}$ 分层，其中 $\operatorname{Tor}^{(d)}$ 是开的、由 $D\mapsto\mathcal{O}_D$ 的像给出；当 $X=\mathbb{A}^1$ 时三个等同 $\operatorname{Tor}^{(d)}\simeq\mathfrak{gl}_d^{\mathrm{reg}}/\operatorname{GL}_d$、$\operatorname{Tor}^{(d)}|_{X^{(d)}-\Delta}\simeq\mathfrak{gl}_d^{\mathrm{rss}}/\operatorname{GL}_d$、$X^{(d)}\simeq\mathfrak{t}_d/W$ 成立。

1. 把分拆 $(d_1,\ldots,d_s)$ 对应到对称幂乘积的图册，取其在 $\operatorname{Tor}^d$ 中的像。  
   *为什么*：讲义直接以该像作为分层 $\operatorname{Tor}^{(d_1,\ldots,d_s)}$ 的定义。
2. 对 $s=1$ 的情形取出 $X^{(d)}\to\operatorname{Tor}^d$、$D\mapsto\mathcal{O}_D$，说明它给出开分层 $\operatorname{Tor}^{(d)}$。  
   *为什么*：循环挠层在 $\operatorname{Tor}^d$ 中是开的，讲义断言而未展开。
3. 对 $X=\mathbb{A}^1$ 用「长度 $d$ 挠层＝带自同态的 $d$ 维向量空间」把三个叠换成 $\mathfrak{gl}_d$ 的伴随商。  
   *为什么*：这是 §4.3 例子的直接翻译，讲义以「这意味着」带过。

> 缺口：讲义只陈述分层由这些图册给出、$\operatorname{Tor}^{(d)}$ 开，以及 $\mathbb{A}^1$ 时的三个等同，未给局部闭性与开性的证明；这些都属于「曲线类比伴随商」的断言。

*出处*：§4.4（原书 p.28）、§4.8（原书 p.30）


## 易错点

- $X^{(d_1-d_2)}\times\cdots\times X^{(d_s)}$ 的维数按 $d_1+\cdots+d_s=d$ 配平，但每个因子是「差」$d_i-d_{i+1}$；漏掉 $d_{s+1}=0$ 会把最后一块写错。
- $\operatorname{Tor}^{d,\mathrm{rss}}$（无重数支撑）与 $\operatorname{Tor}^{(d)}$（循环层）不是一回事：前者是开的稠密部分，后者是更大的循环轨迹；§4.5 的 Springer 解消在两者上分别给出胚叠与覆盖两种描述。
- 局部层 $\operatorname{Tor}_x^\lambda$ 只在支撑固定为 $x$ 的纤维里取，别把它与整体分层 $\operatorname{Tor}^\lambda$ 混同：后者还记录其它支撑点。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§4.4 按分拆的整体分层；§4.8 按分拆的局部分层，p.28-30（PDF p.28-30），`源码/chapters/ch04.tex:59-70,126-137（§4.4、§4.8）`

## 核验

状态：`source-only`（2026-11-18）
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 卡里『局部分层 Tor_x^λ 对应 T_{λ,x} = ⊕_{i=1}^s O_X/O_X(−λ_i x)，等价地 k[[t]]-模 ⊕ k[[t]]/(t^{λ_i})』对应原文『the stratum Coh^λ_{n,m}(x) parametrizes T = O_X/O_X(−λ_1 x) ⊕ … ⊕ O_X/O_X(−λ_n x)』；卡里『叠 Tor_x^d 维数 −d』对应原文『the stack Coh_{n,m}(x) has dimension −m』。
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 卡里『Tor^{(d)} 是开的，是 X^{(d)} → Tor^d, D ↦ O_D 的像』的开性与无重数部分，对应原文开子叠 Coh^{rss}_{n,m}（regular semi-simple，T = ⊕ O_X/O_X(−x_i)）及其与 X^{(m),rss} 的关系。

## 关联

- `glc/concept/torsion-sheaf-stack`
- `glc/concept/springer-resolution`
- `glc/concept/b-lambda-ic`
