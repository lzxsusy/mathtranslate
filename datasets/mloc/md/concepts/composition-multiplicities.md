# 合成重数

> `mloc/concept/composition-multiplicities` · type=concept · track=G · status=draft · verification=source-only

**别名**：composition multiplicities、$[V:L(\lambda)]$、合成因子重数

## 摘要

最高权模有限长，故 Jordan–Hölder 滤过给出合成重数 $[V:L(\lambda)]$；标准模 $I(w,\lambda)$ 的滤过正合列与截面判别给出计算它的几何途径。

## 问题

合成重数 $[V:L(\lambda)]$ 能否只用 Verma 模的权空间维数算出，还是必须借助旗簇上的标准模？

## 定义

由命题 1.8，每个最高权模 $V$ 有有限滤过 $0=V_0\subset V_1\subset\cdots\subset V_n=V$，其各商 $V_i/V_{i-1}$ 不可约。由 Jordan–Hölder 定理，这些商的同构类与重数不依赖滤过的选取。对 $\lambda\in\mathfrak{h}_0^*$ 定义合成重数 $[V:L(\lambda)]=\#\{i\mid V_i/V_{i-1}\cong L(\lambda)\}$。它给出 $V$ 在 Grothendieck 群中的类 $[V]=\sum_\lambda[V:L(\lambda)][L(\lambda)]$。

记号：$[V:L(\lambda)]$：$V$ 中 $L(\lambda)$ 的合成重数；$I(w,\lambda)$：标准模（Bruhat 胞腔 $C(w)$ 上的标准层，$\lambda$ 反支配时也记其截面 $I(w\lambda)$）；$\Sigma_w^+=\Sigma^+\cap(-w^{-1}\Sigma^+)$；$\Sigma_\lambda=\{\alpha\in\Sigma\mid\alpha^\vee(\lambda)\in\mathbb{Z}\}$；$W(\lambda)$：$\lambda$ 的稳定化子。

## 要点

- 重数之所以良定义，全靠命题 1.8 的有限长度：在无限长的模范畴里没有 Jordan–Hölder 定理，$[V:L(\lambda)]$ 可以是无穷大或无定义。
- 权空间维数给出线性方程组：$\dim V^\mu=\sum_\lambda[V:L(\lambda)]\dim L(\lambda)^\mu$。这原则上确定重数，但 $\dim L(\lambda)^\mu$ 本身要先知道，故单靠 Verma 模的权结构不够。
- 几何途径：标准模 $I(w,\lambda)$ 有正合列（引理 1.22），且其合成因子是 $L(w',\lambda)$（同一 $\lambda$）；按 $\ell(w)$ 归纳可算出 $[I(w,\lambda):L(w',\lambda)]$。
- 截面判别（定理 1.19）把几何重数与代数重数对齐：$\lambda$ 反支配时，$\Gamma(X,L(w,\lambda))\neq0$ 当且仅当 $w$ 是左 $W(\lambda)$-陪集的最短元，此时截面恰为 $L(w\lambda)$。
- 不可约性判据是重数为 1 的特例：$I(w,\lambda)$ 不可约 $\iff\Sigma_w^+\cap\Sigma_\lambda=\emptyset$（定理 1.23）；$M(\lambda)$ 不可约 $\iff\lambda$ 反支配（定理 1.24）。
- 第 5 章的 §5.1 并未命名 Jantzen 滤过；与它最接近的是引理 1.22 中的 $U^0$（未命名），其内容是两个标准模之间的短正合列，而不是标准模的一个滤过。

## 公式

$$[V:L(\lambda)]=\#\{i\mid V_i/V_{i-1}\cong L(\lambda)\},\qquad [V]=\sum_\lambda[V:L(\lambda)][L(\lambda)]$$

$$\dim V^\mu=\sum_\lambda[V:L(\lambda)]\,\dim L(\lambda)^\mu$$

$$\Gamma(X,L(w,\lambda))\neq0\iff w\ \text{是左}\ W(\lambda)\text{-陪集的最短元}\quad(\lambda\ \text{反支配})$$

$$I(w,\lambda)\ \text{不可约}\iff\Sigma_w^+\cap\Sigma_\lambda=\emptyset$$

$$0\to U^0(I(w',s_\alpha\lambda))\to I(w,\lambda)\to I(w',\lambda)\to0\qquad(p=-\alpha^\vee(\lambda)\in\mathbb{Z})$$

## 相关定理

### 定理 1.19（§5.1：$L(w,\lambda)$ 的截面判别）

设 $\lambda$ 反支配。则：(i) 每个左 $W(\lambda)$-陪集含最短元；(ii) $\Gamma(X,L(w,\lambda))\neq0$ 当且仅当 $\Gamma(X,L(w,\lambda))=L(w\lambda)$，当且仅当 $w$ 是某个左 $W(\lambda)$-陪集的最短元。

证明状态：`sketch`

1. 由定理 1.14 的证明框架，$\Gamma(X,I(w,\lambda))=I(w\lambda)$；对 $I(w,\lambda)$ 的合成因子 $L(w',\lambda)$ 逐个考察，截面函子正合，故 $\Gamma(X,L(w,\lambda))$ 是 $I(w\lambda)$ 的合成因子层面的贡献。
   - 为什么：正合函子把滤过送到滤过，逐项取截面即可；$\Gamma$ 与合成列相容是因为截面不升高权。
2. 若 $w$ 不是左 $W(\lambda)$-陪集的最短元，则存在 $s_\alpha$（$\alpha\in\Sigma_\lambda^+$）使 $\ell(ws_\alpha)=\ell(w)-1$；用引理 1.22 型的正合列把 $L(w,\lambda)$ 写成某个 $I$ 的商，得 $\Gamma(X,L(w,\lambda))=0$。
   - 为什么：非最短元意味着可以沿 $W(\lambda)$ 下降，而下降一步对应的标准模正合列在截面层给出零。
3. 反之若 $w$ 最短，$C(w)$ 与 $W(\lambda)$-作用的关系（$\Sigma_w^+\cap\Sigma_\lambda$ 的结构）保证 $L(w,\lambda)$ 的截面非零，且由 $\Gamma(X,I(w,\lambda))=I(w\lambda)$ 与 $L(w\lambda)$ 的唯一性得 $\Gamma(X,L(w,\lambda))=L(w\lambda)$。
   - 为什么：截面不可约且非零，必是 $L(w\lambda)$；最高权由 $w\lambda-\rho$ 决定。
4. (i) 每个左 $W(\lambda)$-陪集含最短元，是 Coxeter 群的标准性质：陪集上的长度函数取到极小值，极小元即最短元。
   - 为什么：有限 Coxeter 群的任何陪集都含唯一的最短代表元。

> 缺口：第 2、3 步依赖第 5 章只引用未重证的结果：L.5.6（$I_{s_\alpha}$ 作用的标准模计算，判断 $I_{s_\alpha}(L)=0$ 的情形）与 L.3.12(ii)（$\Sigma_w^+\cap\Sigma_\lambda$ 的递推）；书中把 (ii) 归结为这些局部化理论的既有结论。

### 引理 1.22（§5.1：标准模的滤过正合列）

设 $p=-\alpha^\vee(\lambda)\in\mathbb{Z}$，$w=w's_\alpha$ 且 $\ell(w)=\ell(w')+1$。则有正合列 $0\to U^0(I(w',s_\alpha\lambda))\to I(w,\lambda)\to I(w',\lambda)\to0$，其中 $U^0\neq0$，且 $U^0$ 是形如 $p_\alpha^+(V)$ 的模的平移。

证明状态：`sketch`

1. 由引理 1.16 与 L.3.18 得 $I(w,\lambda)=I_{s_\alpha}(I(w',s_\alpha\lambda))$。
   - 为什么：标准模对 $w$ 的依赖可以沿单反射分解，这是交织函子的基本性质。
2. 由 L.5.3(ii)（抛物 $P_\alpha$ 的直接像的上同调）有正合列 $0\to U^0(I(w',s_\alpha\lambda))\to I(w,\lambda)\to I(w',s_\alpha\lambda)(-p_\alpha)\to U^1(\cdots)\to0$。
   - 为什么：$I_{s_\alpha}$ 对应抛物 $P_\alpha=B\cup Bs_\alpha B$ 的几何，$L.5.3$ 是其直接像的谱序列。
3. 用 $p_\alpha:X\to X_\alpha$ 与基变换，并由 $p_\alpha\circ i_{w'}$ 是仿射浸入，得 $U^1=0$。
   - 为什么：仿射浸入的相对上同调消没，谱序列退化。
4. 于是 $U^0$ 是该正合列的核，$U^0\neq0$ 且是 $p_\alpha^+(V)$ 型模的平移；由正合列的长度可归纳计算 $[I(w,\lambda):L(w'',\lambda)]$。
   - 为什么：$U^0$ 作为 $p_\alpha^+$ 的直接像，其合成因子可由 $V$ 的合成因子按 $\alpha$-链读出，从而把 $w$ 的重数递推到 $w'$。

> 缺口：证明完全落在局部化理论的既有结果上：L.3.18（交织函子与单反射分解）、L.5.3(ii)（抛物直接像的谱序列）、L.5.6（$p_\alpha^+$ 型模的平移结构）；第 5 章只给出引用与几何解释，未重证这些结论。

## 易错点

- 合成重数只在有限长范畴里有意义；对一般有限生成模（无最高权）合成列可能无限长，Jordan–Hölder 定理失效。
- **$\rho$ 平移**：$[V:L(\lambda)]$ 的指标 $\lambda$ 是 Verma 参数，$L(\lambda)$ 的最高权是 $\lambda-\rho$；用最高权当指标会把重数表整体平移 $\rho$，并与 $\mathcal{D}_\lambda=\mathcal{D}_{X,\lambda+\rho}$ 的约定对不上。
- 权空间维数方程组 $\dim V^\mu=\sum_\lambda[V:L(\lambda)]\dim L(\lambda)^\mu$ 不足以单独定出重数：$\dim L(\lambda)^\mu$ 本身是未知量；书中靠标准模的几何滤过（引理 1.22）而非权空间线性代数。
- 定理 1.19 的截面判别要求 $\lambda$ 反支配；一般 $\lambda$ 需先平移（用 1.16、推论 1.17 的 $w$ 作用）。
- 引理 1.22 的 $U^0$ 不是「标准模的 Jantzen 滤过」：它是两个标准模之间的短正合列，第 5 章没有命名 Jantzen 滤过，把 $U^0$ 当成 Jantzen 滤过的分次片是过度解读。
- $[I(w,\lambda):L(w',\lambda)]$ 的两个指标共用同一个 $\lambda$；不同 $\lambda$ 的块之间没有合成因子关系（对偶保持 $\theta$，不同块互不相干）。

## 相关卡

- `mloc/concept/unique-irreducible-quotient`
- `mloc/concept/standard-module-i-w-lambda`
- `mloc/concept/highest-weight-category`
- `mloc/concept/verma-module`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.1 命题 1.8（有限长度：合成重数的前提） · p.[95]（PDF [99]） · `源码/chapters/ch05a.tex:113-117（命题 1.8 及其证明）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.1 定理 1.19（$L(w,\lambda)$ 截面的非零判别） · p.[100, 101]（PDF [104, 105]） · `源码/chapters/ch05b.tex:63-93（定理 1.19 的陈述、证明与推论 1.20）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.1 引理 1.22（标准模的滤过正合列） · p.[101]（PDF [105]） · `源码/chapters/ch05b.tex:111-140（引理 1.22 的陈述与证明）`
