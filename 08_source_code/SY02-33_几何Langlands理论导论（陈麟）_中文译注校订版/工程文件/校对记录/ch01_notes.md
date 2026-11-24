# ch01（导论）审读：待加译注之处

5 条。行号按当前 `src/chapters/ch01.tex`（312 行，含审读期间他人插入的 4 处 `transnote`）。选取标准：作者一句带过、而读者在公式或记号层面一定会卡住的地方。

## 待注 ch01.tex:114（原 PDF p7）
- 原文：For every rank-one local system σ on X, there exists an essentially unique Hecke eigensheaf Aut_σ on Pic_{X/k} with eigenvalue σ; moreover Aut_σ is a local system. Here "essentially unique" means unique up to tensoring by an object of Shv(Spec k), which preserves the eigenvalue.
- 概念：本质唯一（essentially unique）；按 $\Shv(\Spec k)$ 的对象作张量；$\Aut_\sigma$ 是局部系统。
- 读者缺什么：“按 $\Shv(\Spec k)$ 的对象作张量”是什么意思（这类对象就是带 $\Gal_{\bar k/k}$ 作用的分次向量空间/复形，张量后相当于整体平移与直和分解），为什么这种张量不改变特征值 $\sigma$，以及为何因此唯一性只能谈到“相差一个这样的张量”为止。
- 建议来源：nLab "Hecke eigensheaf"；原书文献 [FGKV98]。

## 待注 ch01.tex:175（原 PDF p8）
- 原文：Here geometrically irreducible means that, after base change to k̄, the associated Ǧ-local system has no flat reduction to a proper parabolic subgroup of Ǧ; for G = GLn this is the usual irreducibility of the rank-n local system.
- 概念：几何不可约的 $\check G$-局部系统（geometrically irreducible）。
- 读者缺什么：“到真抛物子群的平坦约化”为什么正是“不可约”的几何形式（约化指子 $P$-丛且与联络相容，即局部系统落在真 Levi/抛物里），以及为什么必须基变换到 $\bar k$ 之后才判；对 $G=\GL_n$ 它退化为通常不可约性这一点也没有展开。
- 建议来源：nLab "geometric Langlands correspondence"；原书文献 [GR24a]。

## 待注 ch01.tex:222（原 PDF p9）
- 原文：Another important object is the Whittaker model Whit(LG) ∈ LG-Mod, obtained by taking right LN-invariants against a generic character χ, where N is the unipotent radical of a Borel subgroup B.
- 概念：Whittaker 模型 $\Whit(LG)$；“相对于一般特征标取右 $LN$-不变量”。
- 读者缺什么：“一般特征标”的具体含义（$N(K_v)$ 的加性特征标，在每条单根上非平凡），为什么对 $\chi$ 取右 $LN$-不变量能从 $LG$-模造出新的 $LG$-模（不变量被左作用保持），以及 $\Whit(LG)$ 与下一行 $\mathrm{KM}_{\mathfrak g}$ 在 Feigin–Frenkel 型结论中的作用。
- 建议来源：nLab "Whittaker model"；原书文献 [FGKV98]。

## 待注 ch01.tex:232（原 PDF p10）
- 原文：For a reductive group H, one has LocSys_H(D) ≃ pt/H and LocSys_H^nilp(D°) ≃ N/H, where N ⊂ h is the nilpotent cone.
- 概念：圆盘/穿孔圆盘上局部系统的模叠；“幂零奇点”；幂零锥的商 $\cN/H$。
- 读者缺什么：为什么 $D=\Spec\cO_v$ 上任何 $H$-局部系统都可平凡化、于是只剩“平凡化”的模（$\mathrm{pt}/H$）；$D^\circ$ 上“幂零奇点”指留数落在幂零锥，所以模叠是 $\cN/H$（按共轭作用商），而这里 $\cN$ 是 $\mathfrak h$ 的幂零锥。
- 建议来源：nLab "local system"；原书文献 [FG05]。

## 待注 ch01.tex:233（原 PDF p10）
- 原文：One also considers LocSys_Ǧ(D°) itself and the space of opers Op_Ǧ(D°).
- 概念：oper（$\check G$-oper）与 oper 空间 $\Op_{\check G}(D^\circ)$。
- 读者缺什么：oper 没有定义：它是带完全旗的平坦 $\check G$-联络，且联络相对该旗的形状固定（逐级把旗“拧”到标准形）；$\Op_{\check G}(D^\circ)$ 是这种联络的模空间。书中只在 (7)(8) 两条 Hom 公式里用到它，读者不知道它为什么能替代谱一侧的 $\LocSys_{\check G}(D^\circ)$。
- 建议来源：nLab "oper"；原书文献 [Fre02]。
