# ch04（Laumon 层）审读：待加译注之处

6 条。选取标准：作者一句带过、但读者在公式/记号层面一定会卡住的地方。

## 待注 ch04.tex:8（原 PDF p26）
- 原文：One should think of the desired Whittaker object as W_E ≃ δ_E ∗ W_0, where W0 is the vacuum Whittaker sheaf.
- 概念：Whittaker 范畴上的卷积（沿 Hecke 对应的 $!$-卷积）、局部系统处的摩天层 $\delta_E$、真空 Whittaker 层 $W_0$。
- 读者缺什么：$*$ 没有定义（在哪个范畴、沿哪个对应卷），$W_0$ 也没有定义；读者无法理解"$\delta_E$ 卷积真空层"为什么就是所希望的 Whittaker 对象，也接不上第 3 章 $\Av_!$ 的图景。
- 建议来源：原书文献 [Gai18]、[FGKV98]。

## 待注 ch04.tex:22（原 PDF p27）
- 原文：The one-dimensional model is the Artin–Schreier sheaf: for j : A1 ↩→ P1 and i∞ : {∞} ↩→ P1, i∗∞j∗Lψ = 0, hence j!Lψ ≃ j∗Lψ.
- 概念：Artin–Schreier 层 $\cL_\psi$（$x\mapsto x^p-x$ 的伽罗瓦覆盖所给的局部系统）、洁净延拓（clean extension）、$j_!\simeq j_*$ 的判别。
- 读者缺什么：$\cL_\psi$ 的定义没给；也没解释为什么 $\infty$ 处茎消失就推出 $j_!\simeq j_*$（$j_!$ 与 $j_*$ 只差边界茎），于是"clean"只是被当作形容词用过去。
- 建议来源：原书文献 [KL85]、[Gai18]。

## 待注 ch04.tex:66（原 PDF p28）
- 原文：On the regular semisimple locus Tord,rss of multiplicity-free support, sd exhibits Tord,rss as the scalar-automorphism gerbe over X(d),rss, and T̃ord,rss is the ordered scalar-automorphism gerbe over Xd,rss. After rigidifying these scalar automorphisms, π becomes the usual ordered Sd-cover.
- 概念：标量自同构胚叠（band 为 $\Gm$ 的胚叠）、胚叠的刚性化、刚性化后得到的 $S_d$-覆盖。
- 读者缺什么："scalar-automorphism gerbe" 与 "rigidify" 都当作已知；读者不知道这个胚叠记录的是"支撑点上的标量自同构"这一多余自由度，也不知道刚性化是把 $\Gm$-胚叠压成 $S_d$-torsor，因此看不出 $\pi$ 与通常的 $X^{d}\to X^{(d)}$ 覆盖之间的关系。
- 建议来源：nLab "gerbe"；原书文献 [GPR20]、[AHJR14]。

## 待注 ch04.tex:73（原 PDF p29）
- 原文：The shift [d] is the normalization used here for the equivariant-perverse convention. The Sd-action is the Springer monodromy action [AHJR14].
- 概念：等变反常（equivariant perverse）归一化中的 $[d]$ 移位；Springer 单值作用；与 Hecke 函子所用 $[d(n-d)]$ 移位的区别。
- 读者缺什么：没有说明这是哪一个约定（相对维数 $d$ 的 IC 归一化），也没说 $S_d$ 作用为什么只能是单值作用、不能字面置换旗；读者会疑惑移位为什么取 $[d]$ 而不是 $[d^2]$ 或 $[d(n-d)]$。
- 建议来源：原书文献 [AHJR14]；nLab "Springer correspondence"。

## 待注 ch04.tex:122（原 PDF p30）
- 原文：The stack Tordx has dimension −d; under the nilpotent-cone model below, its strata are quotient stacks of nilpotent orbits.
- 概念：商叠的维数（$\dim\Tor_x^d=\dim\cN_d-\dim\GL_d=d^2-d-d^2=-d$）；分层 $\Tor_x^\lambda=\cO_\lambda/\GL_d$。
- 读者缺什么：作者直接抛出"维数为 $-d$"，计算一步没给；也不知道"its strata are quotient stacks of nilpotent orbits"里哪个分片对应哪个幂零轨道（要等第 155 行的 $\Tor_x^d\simeq\cN_d/\GL_d$ 才补上）。
- 建议来源：nLab "algebraic stack"；原书文献 [GPR20]。

## 待注 ch04.tex:137（原 PDF p31）
- 原文：put n(λ) := Σi≥1(i − 1)λi. Via the usual Casselman–Shalika normalization view n(λ) = ⟨λ, (0, 1, . . . , n − 1)⟩.
- 概念：$n(\lambda)=\langle\lambda,\rho\rangle$ 中的 $\rho=(0,1,\dots,n-1)$（$\GL_n$ 的半和正根在余权坐标下的像）；Tate 因子 $(-n(\lambda))$ 的来源。
- 读者缺什么：只说 "usual normalization"，没解释 $\rho$ 为什么取 $(0,1,\dots,n-1)$（而不是 $(1,\dots,1)$ 或 $(n-1,\dots,0)$），也没把它与第 3 章 $\gamma_x$ 的归一化和 Casselman–Shalika 公式里的 $q_x^{-\sum_i(i-1)\lambda_i}$ 联系起来——两处其实是同一个指数。
- 建议来源：原书文献 [KL85]、[FGKV98]。
