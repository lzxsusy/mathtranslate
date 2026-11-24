# ch02（Hecke 特征性质）审读：待加译注之处

6 条。行号按当前 `src/chapters/ch02.tex`（256 行）。选取标准：作者一句带过、而读者在公式或记号层面一定会卡住的地方。

## 待注 ch02.tex:94（原 PDF p14）
- 原文：To pass from this local model to global modifications, introduce the infinite-level bundle Bun^∞_G(S) = {(x, P, α) | x: S → X, P ∈ Bun_G(S), α: P|_{D_x} ≅ P^0|_{D_x}}. It is an L^+G_X-torsor over X × Bun_G.
- 概念：无限级丛 $\Bun_G^\infty$；$L^+G_X$-挠子；扭曲积 $\Bun_G^\infty\times^{L^+G_X}\Gr_{G,X}$。
- 读者缺什么：“无限级”指在形式圆盘 $D_x$ 上把 $G$-丛平凡化到全部阶数（$\alpha$ 是 $D_x$ 上的同构），作者没说明为何这样得到的恰好是 $X\times\Bun_G$ 上的 $L^+G_X$-挠子、为什么它只是 ind-对象，也没解释第 97 行 $\Hecke_{G,X}\simeq\Bun_G^\infty\times^{L^+G_X}\Gr_{G,X}$ 里这个扭曲积的含义。
- 建议来源：nLab "affine Grassmannian"；原书文献 [GR24a]。

## 待注 ch02.tex:105（原 PDF p14）
- 原文：Geometric Satake identifies the spherical sheaf category on the local Hecke stack with representations of the Langlands dual group: Perv_{L^+G_x}(Gr_{G,x}) ≃ Perv(Hecke^loc_{G,x}) ≃ Rep(Ǧ).
- 概念：几何 Satake 等价；球面层范畴；$\mathrm{IC}_{\Gr^\lambda}\leftrightarrow V^\lambda$。
- 读者缺什么：只说“identifies”，没给内容与条件：需要 $L^+G$-等变的反常层、$\lambda$ 取优势余权、$\mathrm{IC}_{\overline{\Gr^\lambda}}$ 对应最高权表示 $V^\lambda$；也没说清这里用的是 $\ell$-进还是 $D$ 模范畴。读者无法从这句话推出 $\Sat_V$ 是什么。
- 建议来源：nLab "geometric Satake correspondence"；原书文献 [FGKV98]。

## 待注 ch02.tex:138（原 PDF p15）
- 原文：An S-point is a modification of vector bundles at x: S → X whose local relative position is ω_i; locally this is equivalent to a quotient of length i supported on Γ_x. The local model is the ordinary Grassmannian Gr(i,n).
- 概念：相对位置（relative position）$\omega_i$；长度 $i$ 的商；“局部模型是通常的 Grassmann 簇 $\Gr(i,n)$”。
- 读者缺什么：相对位置与 $L^+G$-轨道 $t^{\omega_i}$ 的对应（Birkhoff 分解/矩阵对角化），为什么“支撑在 $\Gamma_x$ 上、长度为 $i$ 的商”的参数空间恰好是 $\Gr(i,n)$，以及 $\Hecke_n^i\simeq\Gr_{n,X}^i\widetilde\times\Bun_n$ 在一点上的纤维结构。
- 建议来源：nLab "affine Grassmannian"；原书文献 [FGKV98]。

## 待注 ch02.tex:163（原 PDF p16）
- 原文：Put d_i = i(n−i). This is the relative dimension of Hecke^i_{n,x} → Bun_n. The normalized Hecke functor is H^i_n(F) := (supp, h→)_! h←^*F[d_i](d_i/2).
- 概念：反常归一化（perverse normalization）里的移位 $[d_i]$ 与 Tate 扭转 $(d_i/2)$。
- 读者缺什么：为什么移位取相对维数 $d_i=i(n-i)$、Tate 扭转取半整数 $d_i/2$（$\ell$-进情形里对应 Weil 数），以及这正好使 (2.1) 的 $H_n^i(\cF)\simeq\bigwedge^iE\boxtimes\cF$ 两侧归一化一致；作者只说“the Satake/perverse normalization”，没有展开。
- 建议来源：nLab "perverse sheaf"、"Tate twist"；原书文献 [FGKV98]。

## 待注 ch02.tex:214（原 PDF p17）
- 原文：For G = GL_n there is a proper map from the positive global Schubert variety to the compactified modification stack: Gr^{+,≤(1,…,1)}_{G,X} ×~ Bun_n = Hecke^{+,≤(1,…,1)}_{n,X} → Mod^{−i}_n. Over X^i − Δ it factorizes as Gr^{+,≤(1,…,1)}_{G,X}|_{X^i−Δ} ≃ (Gr^1_{G,x_1} × ⋯ × Gr^1_{G,x_i})|_{X^i−Δ}.
- 概念：正的整体 Schubert 簇 $\Gr^{+,\le(1,\ldots,1)}_{G,X}$；Beilinson–Drinfeld Grassmann 簇 $\Gr^I_{G,X}$（$I=\{1,\dots,i\}$）；紧化修改叠 $\operatorname{Mod}^{-i}_n$。
- 读者缺什么：上标 $+,\le(1,\ldots,1)$ 与 $\Gr^I_{G,X}$ 都没定义（Beilinson–Drinfeld 的“沿 $I$ 中诸点同时修改”的族，$+$ 指正的部分），为什么它到 $\operatorname{Mod}^{-i}_n$ 的映射是 proper，以及为何只在互异点轨迹 $X^i-\Delta$ 上才分解成乘积。
- 建议来源：nLab "Beilinson-Drinfeld Grassmannian"；原书文献 [GR24a]。

## 待注 ch02.tex:228（原 PDF p18）
- 原文：The singularity-resolving maps to Bun_n are [...] and the support maps form the support square [...]. By projection formula, (supp, h→)_!(h←^*F ⊗ Spr_i) ≃ (sym × id_{Bun_n})_!((H^1_n)^i(F)).
- 概念：$\operatorname{Mod}^{-i}_n$ 的 Springer 型解消 $\varphi:\widetilde{\operatorname{Mod}}^{-i}_n\to\operatorname{Mod}^{-i}_n$；Springer 层 $\operatorname{Spr}_i=\varphi_!\mathrm{IC}$；符号等型 $\Hom_{S_i}(\mathrm{sgn},-)$。
- 读者缺什么：为什么“给初等商排序”的解消就是 Springer 解消、$\operatorname{Spr}_i$ 为什么是 Springer 层（作者只说“the same mechanism”），以及 $\Hom_{S_i}(\mathrm{sgn},\operatorname{Spr}_i)$ 提取 $\bigwedge^i$ 的符号等型机制；投影公式如何把整体的 $(H^1_n)^i$ 归约为 $\operatorname{sym}_!(E^{\boxtimes i})$ 这一步也整段跳过。
- 建议来源：nLab "Springer correspondence"；原书文献 [FGKV98]。
