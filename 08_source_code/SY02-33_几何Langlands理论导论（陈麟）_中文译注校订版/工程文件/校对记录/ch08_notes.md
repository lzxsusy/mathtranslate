# ch08（Aut_E 的构造）审读：待加译注之处

6 条。选取标准：作者明说“黑箱”的输入（Deligne 真推前不变性、FGKV 比较、Drinfeld 紧化）与只报名字的构造（[dk](dk/2) 归一化、微小 Hecke 关系、尖点性判据）。

## 待注 ch08.tex:38（原 PDF p45）

- 原文：The black-box input is Deligne's proper-pushforward invariance: if f : Y1 → Y2 is proper and K1, K2 ∈ D(Y1) are étale-locally isomorphic, then the Euler characteristic functions of f!K1 and f!K2 agree.
- 概念：Deligne 的真推前不变性；Euler 示性数函数（构造函数）与 étale 局部同构。
- 读者缺什么：作者明说这是“黑箱”，但没说明为什么只需 étale 局部同构就能让推前层的 Euler 示性数函数相等（$\chi$ 可加、可按分层局部计算，真性保证推前仍是构造性的），读者无法判断这一不变性的适用范围。
- 建议来源：nLab "six operations"；原书第 3 章的六函子约定

## 待注 ch08.tex:44（原 PDF p45）

- 原文：The map is not literally proper, but the compactified Whittaker construction admits a Drinfeld compactification, so the same argument applies after replacing the correspondence by its compactified version.
- 概念：Drinfeld 紧化，以及紧化后映射成为真态射。
- 读者缺什么：读者不知道“Drinfeld 紧化”是什么、原来的映射为何不真、换成紧化版本后为什么 Deligne 定理可以直接套用（需要说明紧化边界不贡献 Euler 示性数）。
- 建议来源：nLab "Drinfeld compactification"；原书第 9 章的紧化 Whittaker 构造

## 待注 ch08.tex:46（原 PDF p45）

- 原文：By the comparison theorem of Frenkel–Gaitsgory–Kazhdan–Vilonen, its restriction to Bun′n(Fq) is the trace function M′ ↦ Tr(FrobM′, Aut′E′).
- 概念：FGKV 的层–函数比较定理（Hecke 特征层的迹函数恰是自守特征函数）。
- 读者缺什么：只报名字，没说明比较的两边是什么、为何限制到 $\Bun'_n$ 上恰好是迹函数，而且文献号 [FGKV98] 要到章末才出现，此处读者无法定位。
- 建议来源：原书文献 [FGKV98]

## 待注 ch08.tex:55（原 PDF p45）

- 原文：HL^d_k(K) := h→_! h←^* K[dk](dk/2), K ∈ D(Coh_k).
- 概念：Hecke–Laumon 函子中的移位 $[dk]$ 与 Tate 扭转 $(dk/2)$ 归一化。
- 读者缺什么：两个归一化因子直接出现、未解释来历，读者无法判断它们与第 7 章因子化命题里的“移位与 Tate 扭转”如何对应，也容易把 $(dk/2)$ 当成笔误。
- 建议来源：原书第 5–6 章的归一化约定；nLab "Tate twist"

## 待注 ch08.tex:100（原 PDF p47）

- 原文：The higher minuscule Hecke relations follow from the compatibility of the first Hecke correspondence under convolution, with eigenvalues ∧^iE.
- 概念：微小（minuscule）Hecke 关系、Hecke 对应的卷积，以及特征值 $\bigwedge^iE$。
- 读者缺什么：没有说明“第一 Hecke 关系”如何经卷积生成所有微小关系，也没解释 $\bigwedge^iE$ 作为特征值从何而来（外幂局部系统），读者只能接受结论。
- 建议来源：nLab "Hecke algebra"；原书第 2 章的 Hecke 对应约定

## 待注 ch08.tex:114（原 PDF p47）

- 原文：Finally, AutE is cuspidal. The reason is the same vanishing theorem used in the clean-extension argument: every proper constant-term functor for GLn factors through an averaging operation on some Bunk with k < n, and the averaging theorem for the geometrically irreducible rank-n local system E forces that contribution to vanish.
- 概念：尖点性（cuspidality）、常数项函子、平均函子与平均消失定理。
- 读者缺什么：尖点层的定义在第 3 章，此处直接用“所有真抛物常数项消失”作判据；读者不熟悉常数项函子为何能“因子化”到某个 $\Bun_k$，也不清楚平均定理的陈述（其证明在第 9 章）。
- 建议来源：原书文献 [Gai04]、[Gai16b]；nLab "Eisenstein series"
