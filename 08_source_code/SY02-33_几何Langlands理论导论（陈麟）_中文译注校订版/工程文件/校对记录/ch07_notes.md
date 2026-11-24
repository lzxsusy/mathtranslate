# ch07（Laumon 因子化）审读：待加译注之处

6 条。选取标准：作者以 standard／Recall／一句带过的方式给出的构造与定理，读者在记号与命题适用范围上一定会卡住之处。

## 待注 ch07.tex:58（原 PDF p42）

- 原文：For any local system E for which the Laumon complexes are defined, in particular for the geometrically irreducible E used in the cleanness argument, one has on Tor × Tor (s,q)_!m^*L_E ≃ L_E ⊠ L_E.
- 概念：Laumon 复形 L_E 的构造（沿 Hecke 对应把 E 拉回、再推前所得的复形），以及“几何不可约”这个前提在定义 L_E 时的作用。
- 读者缺什么：本章直接使用 L_E，却没有交代它由什么构造得到；“Laumon 复形能够定义”和“几何不可约”各自保证什么，读者无从判断命题的适用范围。
- 建议来源：原书文献 [KL85]；nLab "geometric Langlands correspondence"

## 待注 ch07.tex:69（原 PDF p42）

- 原文：Recall the regular semisimple locus Tor^{d,rss} = {⊕_{i=1}^d k(x_i) | x_i ≠ x_j for i ≠ j} ⊂ Tor^d, which is a gerbe over X^{(d),rss} = X^{(d)} − Δ whose stabilizer at a geometric point is (G_m)^d.
- 概念：胚叠（gerbe）、几何点处的稳定子，以及 Tor^{d,rss} 为什么是 (G_m)^d-胚叠。
- 读者缺什么：作者用“Recall”一句带过；读者未必记得胚叠是局部同构于 BG 的叠，也未必看出 (G_m)^d 来自每个 k(x_i) 的标量自同构——而这正是后文可以用 S_d 作对称下降的依据。
- 建议来源：nLab "gerbe"；原书第 4 章（标量自同构胚叠）

## 待注 ch07.tex:71（原 PDF p42）

- 原文：E^{(d)} := (r_{rss,*}E^{⊠d})^{S_d}, L^d_E ≃ j_{rss,!*}(s^*_{rss}E^{(d)}[d]).
- 概念：记号 $j_{!*}$（中间延拓／IC 延拓）、$S_d$-不变子层（对称下降），以及移位 $[d]$ 的归一化约定。
- 读者缺什么：没有解释 $j_{!*}$ 与 $j_!$、$j_*$ 的关系（$j$ 非开、闭嵌入时它才是中间延拓），也没说明 $(r_{\mathrm{rss},*}E^{\boxtimes d})^{S_d}$ 为何是下降到 $X^{(d),\mathrm{rss}}$ 上的局部系统，读者会卡在这两处记号。
- 建议来源：nLab "intermediate extension"；原书第 4 章（Laumon 延拓定理，含 $[d]$ 与 $S_d$ 的约定）

## 待注 ch07.tex:86（原 PDF p43）

- 原文：For X = A^1, a length-d torsion sheaf is a d-dimensional vector space with an endomorphism, hence Tor^d ≃ gl_d/GL_d.
- 概念：$\mathbb A^1$ 上长度 $d$ 挠层的分类（$k[x]$-模 ↔ 带幂零自同态的 $d$ 维向量空间，同构 ↔ $\GL_d$ 共轭），以及商叠 $\mathfrak{gl}_d/\GL_d$。
- 读者缺什么：原文说“带一个自同态的向量空间”就直接给出 $\mathfrak{gl}_d/\GL_d$，读者会问自同态为什么自动幂零、为什么模掉的是 $\GL_d$ 而不是别的群（第 4 章只在局部形式下点明“幂零”）。
- 建议来源：nLab "quotient stack"；nLab "coherent sheaf"

## 待注 ch07.tex:90（原 PDF p43）

- 原文：The required geometric input is the standard parabolic-restriction theorem for the Grothendieck–Springer sheaf [AHJR14, GPR20]: the complex (p/P → m/M)_!(p/P → g/G)^*Spr_g is the IC-extension from the locus in m/M where the two characteristic polynomials are regular and disjoint, with the Weyl local system obtained by restricting the S_d-monodromy to S_{d1} × S_{d2}.
- 概念：Grothendieck–Springer 层 $\operatorname{Spr}_{\mathfrak g}$、抛物限制（parabolic restriction）定理、Weyl 局部系统与 $S_d$-单值作用。
- 读者缺什么：只报“标准定理”和两条文献，没有陈述动机；读者不知道 $\operatorname{Spr}_{\mathfrak g}$ 是什么、为什么沿抛物对应作 $!$-推前会得到 $\mathfrak m/M$ 上的 IC 延拓，也不清楚“把 $S_d$-单值作用限制到 $S_{d_1}\times S_{d_2}$”具体指哪个局部系统。
- 建议来源：原书文献 [AHJR14]、[GPR20]；nLab "Grothendieck–Springer resolution"

## 待注 ch07.tex:95（原 PDF p43）

- 原文：For reference, a Bruhat proof stratifies p̃ := {(x, gB) | x ∈ p ∩ Ad_g b} by the double-coset pieces PwB/B, with w ∈ W_M \ W_G.
- 概念：Bruhat 分解、双陪集 $W_M\backslash W_G$、最小陪集代表，以及其纤维 $\mathfrak u_w$ 的仿射纤维化。
- 读者缺什么：没有说明 $\widetilde{\mathfrak p}$ 是什么（Grothendieck–Springer 解消的抛物版本）、为何按 $PwB/B$ 分层，也没说“最小陪集代表”这一选取在证明中起什么作用（纤维维数随 $w$ 变化，要单独估计）。
- 建议来源：nLab "Bruhat decomposition"；原书文献 [AHJR14]
