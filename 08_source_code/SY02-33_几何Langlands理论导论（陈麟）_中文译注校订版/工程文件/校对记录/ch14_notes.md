# ch14 待注点（Hitchin 系统的量子化，原 PDF p67–p71）

## 待注 ch14.tex:20（原 PDF p68）
- 原文：Proposition 14.1.1. The prestack Op_Ǧ(X) is a torsor under the vector space Hitch_Ǧ(X). Consequently, if A := Γ(Op(X), O), A^cl := Γ(Hitch, O), then the natural filtration on A has associated graded gr A ≃ A^cl.
- 概念：Hitchin 底空间 Hitch_Ǧ(X) = Γ(X, c_{Ǧ,Ω})，其中 c_{Ǧ,Ω} ≅ ⊕_i Ω_X^{d_i+1}（直和，见 14 章开头）；oper 空间作为其挠子；以及 A 的过滤满足 gr A ≃ A^cl（PBW/Rees）。
- 读者缺什么：为什么底空间是仿射空间（指数 d_1,…,d_r 与分量次数 d_i+1 的来历）没有交代；“挠子”在此的含义（任取两个 oper 之差给出 Hitchin 场，但无典范 oper 可固定）也没解释；对 GL_n/SL_n，底空间的点正是谱曲线（特征多项式系数）给出的，Hitchin 纤维化／谱曲线这一图景整段缺席。
- 建议来源：nLab “Hitchin fibration”、“oper”；原书文献 [BD05]。

## 待注 ch14.tex:31（原 PDF p68）
- 原文：Let W be the right adjoint to the forgetful functor Sch/X_dR → Sch/X. For a vector bundle E on X, one may think of W(E) as the D_X-scheme of jets, so that W(E)(D_x) = Jets_x(E).
- 概念：de Rham 空间 X_dR、遗忘函子 Sch_{/X_dR} → Sch_{/X} 的右伴随 W，以及“射流 D_X-概形”。
- 读者缺什么：W 在全书仅此一见，既无构造也无例子；读者不知道它为何把 𝔠_{Ǧ,Ω} 变成参数化 opers 的 D_X-概形，只能从 14.2 的局部坐标 v(t) ∈ ǧ^e[[t]] 反推。
- 建议来源：nLab “de Rham space”、“jet bundle”；原书文献 [BD05]。

## 待注 ch14.tex:45（原 PDF p68）
- 原文：The Drinfeld–Sokolov gauge statement for opers [BD05, Fre02] is that each Ň((t))-gauge class has a unique representative ∇ = d + (f + v(t))dt, v(t) ∈ ǧ^e((t)), with v(t) ∈ ǧ^e[[t]] for regular opers. Here ǧ^e is the centralizer of e. This is Kostant's slice: the true parameters are the Kostant coordinates in ǧ^e, not all of b̌.
- 概念：Drinfeld–Sokolov 规范（DS reduction）与 Kostant 切片——Ň((t))-规范群的作用、过 f 的切片、中心化子 ǧ^e 作为“真正的参数”。
- 读者缺什么：未写出 Ň((t)) 如何作用、为何每个规范类有唯一代表（Kostant 的 sl_2 理论：ad f 的像给出横截切片），也没说清 e 与 f 的分工（f 定 oper 的最低次项，e 定切片方向）；“Kostant 切片”一词在此首次出现。
- 建议来源：nLab “Drinfeld-Sokolov reduction”、“Kostant slice”；原书文献 [BD05]、[Fre02]。

## 待注 ch14.tex:65（原 PDF p69）
- 原文：Theorem 14.3.1 (Feigin–Frenkel, see [Fre02]). There are canonical identifications Spf Z_crit,x ≃ Op_Ǧ(D_x^×), Spec z_crit(D_x) ≃ Op_Ǧ(D_x), and globally Spec z_crit ≃ Op^D_Ǧ as D_X-schemes. Under the PBW filtration, the classical limit is Spec gr z_crit ≃ W(c_{Ǧ,Ω}).
- 概念：Feigin–Frenkel 中心定理——临界水平仿射 Kac–Moody 的中心（及其真空模自同态环）同构于 oper 空间；PBW 分次给出 W(𝔠_{Ǧ,Ω})。
- 读者缺什么：Z_{crit,x} = Z(Û_{crit,x}) 与 z_crit(D_x) = End(V_{crit,x}) 是两个不同的环却都叫“中心”，讲义没有区分；Spf 与 Spec 的用法（形式谱 vs 通常谱）也未说明；Feigin–Frenkel 定理的内容（中心 ≅ 临界 W-代数）只报了名字。
- 建议来源：nLab “W-algebra”、“chiral algebra”；原书文献 [Fre02]。

## 待注 ch14.tex:82（原 PDF p69）
- 原文：For the irreducible Ǧ-representation V^λ̌, let IC_λ̌ = Sat(V^λ̌). If L_0 = −t∂_t ∈ Lie Aut_0(D), then the lowest L_0-eigenvalue of Γ(Gr_G, IC_λ̌)_crit is −〈λ̌, ρ〉; the corresponding eigenspace is one-dimensional and B̌-invariant. These lines satisfy the Plucker relations, hence give the desired B̌-reduction.
- 概念：临界水平的几何 Satake（Γ(Gr_G, Sat(V))_crit 作为 z_crit-模），以及用“最低旋转权”的一维直线构造 B̌-约化；L_0 的作用与 ρ-shift。
- 读者缺什么：L_0 从何而来（旋转/伸缩作用）、为何最低特征空间一维且 B̌-不变、为何这些直线满足 Plücker 关系就给出 B̌-约化，全部略过；−〈λ̌, ρ〉 中的 ρ 也没有说明（它正是临界扭转／ρ-shift 的来源）。
- 建议来源：nLab “geometric Satake correspondence”、“affine Grassmannian”；原书文献 [BD05]。

## 待注 ch14.tex:120（原 PDF p70）
- 原文：The proof uses Beilinson–Drinfeld localization Loc_x : ĝ_crit,x-Mod^{G[[t]]} → DMod_crit(Bun_G) with the property Loc_x(V_crit,x) ≃ D_crit.
- 概念：Beilinson–Drinfeld 局部化函子（Kac–Moody 表示 ↦ Bun_G 上的临界扭转 D 模）及其与 Hecke 作用的相容性。
- 读者缺什么：局部化的构造只字未提（在 Bun_G 上“沿 Hecke 作用取局部化”、取临界水平），读者无法理解为何 V_crit,x 落到 D_crit，也看不出 14.5 中 Sat_x(V) ⋆ D_crit 两步等式的第一步为何成立。
- 建议来源：nLab “D-module”、“affine Lie algebra”；原书文献 [BD91]、[FG05]。
