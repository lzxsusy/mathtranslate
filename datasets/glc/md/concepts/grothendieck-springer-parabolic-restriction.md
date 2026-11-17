---
id: glc/concept/grothendieck-springer-parabolic-restriction
type: concept
track: E
---

# Grothendieck–Springer 层的抛物限制

> 命题 7.4.1 证明所引的标准几何输入：$\operatorname{Spr}_{\mathfrak g}$ 沿抛物对应 $!$ 推前再拉回，得到从『两块特征多项式正则且互不相交』轨迹出发的 IC 延拓。

**问题**：复形 $(\mathfrak p/P\to\mathfrak m/M)_!(\mathfrak p/P\to\mathfrak g/G)^*\operatorname{Spr}_{\mathfrak g}$ 是从哪条轨迹出发的 IC 延拓，其 Weyl 局部系统是什么？

## 定义

设 $G=\operatorname{GL}_d$，$P=P_{d_1,d_2}=UM$，$M\simeq\operatorname{GL}_{d_1}\times\operatorname{GL}_{d_2}$，$\mathfrak p,\mathfrak m$ 为相应 Lie 代数，$\operatorname{Spr}_{\mathfrak g}$ 为 $\mathfrak g/G$ 上的 Grothendieck–Springer 层。所需的几何输入是 Grothendieck–Springer 层的标准抛物限制定理（讲义引 [AHJR14, GPR20]）：复形 $(\mathfrak p/P\to\mathfrak m/M)_!(\mathfrak p/P\to\mathfrak g/G)^*\operatorname{Spr}_{\mathfrak g}$ 是从 $\mathfrak m/M$ 中『两个特征多项式正则且互不相交』的轨迹作出的 IC 延拓，其 Weyl 局部系统由将 $S_d$ 单值作用限制到 $S_{d_1}\times S_{d_2}$ 得到。

*记号*：$\mathfrak g/G$ 是 $\mathfrak g$ 的伴随商叠；$\mathfrak p/P$、$\mathfrak m/M$ 是相应的商叠；$(\mathfrak p/P\to\mathfrak g/G)^*$ 与 $(\mathfrak p/P\to\mathfrak m/M)_!$ 分别是抛物对应 $\mathfrak g/G\leftarrow\mathfrak p/P\to\mathfrak m/M$ 的拉回与 $!$ 推前；$S_d$ 是 Weyl 群。

## 要点

- $\mathfrak m/M$ 上的『两个特征多项式』分别对应 $d_1$、$d_2$ 两块；『正则且互不相交』是开条件，正是 $\operatorname{Tor}$ 一侧两个支撑互不相交且各自正则半单的对应物。
- IC 延拓的 Weyl 局部系统是 $S_d$ 单值作用限制到 $S_{d_1}\times S_{d_2}$——与分支版本所需的对称群一致。
- Bruhat 证明：$\widetilde{\mathfrak p}:=\{(x,gB)\mid x\in\mathfrak p\cap\operatorname{Ad}_g\mathfrak b\}$ 按双陪集 $PwB/B$（$w\in W_M\backslash W_G$）分层；对极小陪集代表 $w$，到 $\mathfrak m$ 的 Grothendieck–Springer 解消的映射是仿射纤维化，纤维为 $\mathfrak u_w:=\mathfrak u\cap\operatorname{Ad}_w\mathfrak b$。
- 采用通常的反常归一化后这些分层拼成上述 IC 延拓，不会出现支撑在『正则且不交轨迹』补集上的直和项。

## 关键公式

- $(\mathfrak p/P\to\mathfrak m/M)_!(\mathfrak p/P\to\mathfrak g/G)^*\operatorname{Spr}_{\mathfrak g}$
- $\widetilde{\mathfrak p}:=\{(x,gB)\mid x\in\mathfrak p\cap\operatorname{Ad}_g\mathfrak b\}$
- $\mathfrak u_w:=\mathfrak u\cap\operatorname{Ad}_w\mathfrak b,\qquad w\in W_M\backslash W_G$

## 定理与证明

### Grothendieck–Springer 层的抛物限制（讲义引用）（要点（有缺口））

复形 $(\mathfrak p/P\to\mathfrak m/M)_!(\mathfrak p/P\to\mathfrak g/G)^*\operatorname{Spr}_{\mathfrak g}$ 是从 $\mathfrak m/M$ 中两个特征多项式正则且互不相交的轨迹作出的 IC 延拓，其 Weyl 局部系统由将 $S_d$ 单值作用限制到 $S_{d_1}\times S_{d_2}$ 得到。

1. 按双陪集 $PwB/B$（$w\in W_M\backslash W_G$）对 $\widetilde{\mathfrak p}$ 分层。  
   *为什么*：Bruhat 分解把 $\mathfrak p$ 中的点按『$x$ 落在哪个 $g\mathfrak b$ 中』分类，$P$-双陪集正是这一分类的标签。
2. 对极小陪集代表 $w$，到 $\mathfrak m$ 的 Grothendieck–Springer 解消的映射是仿射纤维化，纤维为 $\mathfrak u_w=\mathfrak u\cap\operatorname{Ad}_w\mathfrak b$，其维数依赖 $w$。  
   *为什么*：纤维不是整个 $\mathfrak u$：只有被 $\operatorname{Ad}_w\mathfrak b$ 截住的那部分留了下来。
3. 取通常的反常归一化，这些分层组合成抛物限制的 IC 延拓，且不出现支撑在正则不交轨迹补集上的直和项。  
   *为什么*：这是讲义所引 [AHJR14, GPR20] 的结论；反常归一化使各层的平移与维数一致，从而拼成一个 IC 层。

> 缺口：讲义只把它作为标准输入引用 [AHJR14, GPR20]，并给出 Bruhat 分层的思路，未在本书内证明；命题 7.4.1 的证明以此为前提。

*出处*：§7.4 证明 / 原书 p.43


## 易错点

- 纤维是 $\mathfrak u_w=\mathfrak u\cap\operatorname{Ad}_w\mathfrak b$ 而不是整个 $\mathfrak u$；维数随 $w$ 变化，所以这不是等维纤维化，不能逐层直接相加。
- 方向不能反：这是『引用』的标准输入，命题 7.4.1 用它，而不是由命题 7.4.1 推出它。
- 『正则且互不相交』是开轨迹条件；忘记『不相交』会让两块特征多项式重合，落到交叉对角线上，那里正是需要 IC 延拓（而非局部系统）的地方。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§7.4 Laumon 层通过短正合列的因子化（证明），p.43（PDF p.43），`源码/chapters/ch07.tex:101-109（抛物限制定理与 Bruhat 分层）`

## 核验

状态：`source-only`（2026-11-18）
- arXiv：https://arxiv.org/abs/1304.2642 — 下载 v2 全文（HTML→纯文本）检索："parabolic" 出现 0 次；唯一相关句是 "the functor S_ρ̇ commutes with restriction to Levi subgroups in an appropriate sense, by [AHR, §7]"，讲 Springer 函子与 Levi 限制的相容性，不是卡中 (p/P→m/M)_!(p/P→g/G)^*Spr_g 的 IC 描述。
- arXiv：https://arxiv.org/abs/2002.12480 — 全文检索 "parabolic" 3 处：分别讲 partial Springer resolution Ñ^P、cuspidal datum 的 Levi 分解、type A 的 L_d/P_d 构造；未见「从两个特征多项式正则且互不相交的轨迹作 IC 延拓」或该 pull-push 复形的陈述。
- nLab：https://ncatlab.org/nlab/show/Springer+correspondence — 快照为简短条目 + 文献表（Springer 1978、Kazhdan–Lusztig 1980、Lusztig–Spaltenstein 1985 等），正文无 parabolic / Levi restriction 的陈述，不支持卡中定理。

## 关联

- `glc/concept/laumon-factorization`
- `glc/concept/torsion-stack-local-model`
