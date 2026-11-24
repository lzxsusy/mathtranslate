# ch03（Whittaker）审读：待加译注之处

6 条。选取标准：作者一句带过、但读者在公式/记号层面一定会卡住的地方。

## 待注 ch03.tex:38（原 PDF p20）
- 原文：Equivalently, let γx be the normalized Satake parameter characterized by Tr(∧d γx) = qx^{d(n−1)/2} Tr(∧d σ(Frx)), 0 ≤ d ≤ n. In the Tate-twist convention this is denoted γx = σ((n−1)/2)(Frx).
- 概念：归一化 Satake 参数、Tate 扭转、$\rho=\Omega^{1/2}$；"上点"（$\dot G$）即 $\rho$-shift。
- 读者缺什么：作者没说明 $\gamma_x$ 与 $\sigma(\Fr_x)$ 差一个 $q_x^{(n-1)/2}$ 的标量扭转（就是 Tate 扭转 $\Omega^{(n-1)/2}$），也没说为什么用 $n-1$ 而非 $n$；更没解释 $\Tr(\bigwedge^d)$（$d=1,\dots,n$）何以唯一确定半单元素 $\gamma_x$。读者会卡在"两条特征值公式为什么是同一个"。
- 建议来源：nLab "Tate twist"；原书文献 [Laf18]。

## 待注 ch03.tex:74（原 PDF p21）
- 原文：The Casselman–Shalika formula gives the values explicitly; its geometric form is the Whittaker realization of Satake [FGKV98]. For a coweight λ = (λ1, . . . , λn), Wγ,x(tλx) = qx^{−Σi(i−1)λi} Tr(γ, V λ) for λ dominant, 0 otherwise.
- 概念：Casselman–Shalika 公式；$V^\lambda$ 为 $\check G$ 的最高权表示；Whittaker 形式的几何 Satake $\operatorname{Perv}^{\mathrm{Wh}}(\dot{\Gr}_{G,x})\simeq\Rep(\check G)$。
- 读者缺什么：只说"explicitly"，没给这个值的归一化来源——指数 $\sum_i(i-1)\lambda_i$ 就是第 4 章局部公式里的 $n(\lambda)$，两处用的是同一个 Tate 因子，书中没有点明；也没解释非优势 $\lambda$ 为什么取 0（对应 Whittaker 轨道上不存在所需的等变层，见 p027）。
- 建议来源：原书文献 [FGKV98]、[Gai18]；nLab "geometric Satake correspondence"。

## 待注 ch03.tex:125（原 PDF p23）
- 原文：A generic N-reduction of a B-bundle is equivalently a generic trivialization of its induced T-bundle, so BunB^{N-gen} = BunB ×_{BunT} BunT^{rat triv} ≃ BunB ×_{BunT} DivΛ, where DivΛ is the colored-divisor space for the coweight monoid.
- 概念：一般位置约化（generic reduction）；$\Bun_T^{\mathrm{rat\ triv}}$（带一般点平凡化的 $T$-丛）；余权标号的带色除子空间 $\operatorname{Div}_\Lambda$；缺陷除子。
- 读者缺什么：$\Bun_T^{\mathrm{rat\ triv}}$ 未定义，也没说它为什么同构于 $\operatorname{Div}_\Lambda$（一般点上的一个 $T$-丛平凡化，等价于给若干点标上余权，即 $\Lambda$-着色的除子）；"记录其缺陷除子"具体记录什么、有什么用，一句都没展开。
- 建议来源：原书文献 [Gai18]；nLab "divisor"。

## 待注 ch03.tex:156（原 PDF p24）
- 原文：Fourier transform on V (K)\\V (A) uses V (K)⊥ = Ch(V (A)/V (K)).
- 概念：阿代尔向量空间 $V(\A)/V(K)$ 上的 Fourier 变换；$\operatorname{Ch}(-)$ 是特征标群（Pontryagin 对偶），$V(K)^\perp$ 就是它的对偶。
- 读者缺什么：$\operatorname{Ch}$ 这个记号全书没有定义，读者不知道 $V(K)^\perp$ 是"对偶空间"，因此看不出下一段 $L_1(K)$ 的两个轨道为什么正好给出 Fourier 变换的分解（开轨道给 Whittaker 型空间，闭轨道给退化部分）。
- 建议来源：nLab "Pontryagin duality"；原书文献 [FGKV98]。

## 待注 ch03.tex:160（原 PDF p25）
- 原文：(1) the open orbit through a nonzero character ηn−1, whose stabilizer is the smaller mirabolic subgroup Q′1(K) ⊂ GLn−1(K); (2) the closed orbit {0}, whose stabilizer is L1(K).
- 概念：mirabolic 子群 $Q_1=L_1\ltimes V$ 与"较小的 mirabolic" $Q'_1\subset\GL_{n-1}$；$L_1(K)$ 在 $V(K)^\perp$ 上的轨道结构。
- 读者缺什么：$Q'_1$ 第一次出现且无定义（它是 $\GL_{n-1}$ 中稳定一个非零线性泛函的子群），"两个轨道"是典型的一步验算被跳过；不补这一步，第 170 行"迭代降秩、最后只剩一般位置 Whittaker 系数"就无从理解。
- 建议来源：原书文献 [FGKV98]。

## 待注 ch03.tex:189（原 PDF p25）
- 原文：The map Em → Cohm remembers the middle term with its tautological section; set ^{≠0}Em := Em ×_{Coh′m} ^{≠0}Coh′m.
- 概念：相对向量叠 $\mathcal E_m\to\Coh_{m-1}$、Serre 对偶给出的 $\mathcal E_m^\vee\simeq\Coh'_{m-1}$、Fourier–Deligne 变换的核。
- 读者缺什么：原文这里写 $\Coh_m$，紧接着的纤维积却取在 $\Coh'_m$ 上（带典范截面 $\Omega_X^{m-1}\to\cF$ 的中间项才在 $\Coh'_m$ 里），前后不一致，读者会卡在"$\mathcal E_m$ 到底映到哪个叠"。译稿已统一作 $\Coh'_m$，建议加一条译注点明原文此处应为 $\Coh'_m$，以免读者以为漏了上标。
- 建议来源：原书文献 [KL85]。
