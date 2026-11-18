---
id: dmod/concept/relative-differential-operators
type: concept
track: C
---

# 相对微分算子的一阶部分

> $F_1\mathcal D_X=\mathcal O_X\oplus\mathcal T_X$ 属绝对情形；相对情形的一阶部分只在光滑时等于 $\mathcal O_X\oplus\Omega_{X/S}^{\vee}$。

**问题**：把 $F_1\mathcal D_X=\mathcal O_X\oplus\mathcal T_X$ 搬到相对情形时，为什么 $\Omega_{X/S}^{\vee}$ 只能取光滑情形，一般情形只剩包含关系？

## 定义

设 $k$ 是特征零代数闭域，$X$ 是 $k$ 上代数簇。绝对情形（$S=\operatorname{Spec}k$）下，对仿射开集 $U\subset X$ 有 $D_1(U)=R(U)\oplus\mathcal T_X(U)$，其中 $\mathcal T_X(U)=\operatorname{Der}_k(R(U))$；层化得 $F_1\mathcal D_X=\mathcal O_X\oplus\mathcal T_X$（命题 1.16）。对一般基概形 $S$，把向量场换成相对向量场即得相对微分算子层 $\mathcal D_{X/S}$；其一阶部分 $\mathcal D_{X/S,\le1}$ 在 $X$ 于 $S$ 上光滑时等于 $\mathcal O_X\oplus\Omega_{X/S}^{\vee}$，一般情形则是 $\mathcal O_X\oplus\mathcal T_{X/S}$ 的子层（译者注，chap2.tex:245-247）。

*记号*：$\Omega_{X/S}$：Kähler 微分模层；$\Omega_{X/S}^{\vee}=\mathcal{H}om_{\mathcal O_X}(\Omega_{X/S},\mathcal O_X)$；$\mathcal T_{X/S}$：相对向量场构成的层；$F_1\mathcal D_X$：阶数 $\le 1$ 的微分算子层。

## 要点

- 绝对情形：$D_1(U)=R(U)\oplus\mathcal T_X(U)$（$U$ 仿射），故 $F_1\mathcal D_X=\mathcal O_X\oplus\mathcal T_X$（命题 1.16(ii)）。
- 光滑情形：$\mathcal D_{X/S,\le1}=\mathcal O_X\oplus\Omega_{X/S}^{\vee}$，即一阶相对算子等同于「函数 $+$ 一次微分形式」。
- 非光滑情形：讲义只断言 $\mathcal D_{X/S,\le1}$ 是 $\mathcal O_X\oplus\mathcal T_{X/S}$ 的子层，不给等号（chap2.tex:245-247）。
- $\Omega_{S/R}$ 的记法按 Kähler 微分模的全称：由形式符号 $\mathrm ds$ 生成，满足 $\mathrm d(rs)=r\,\mathrm ds+s\,\mathrm dr$ 与加法性（Stacks 07BK）。
- 同一命题还断言切层 $\mathcal T_X$ 是凝聚 $\mathcal O_X$-模（命题 1.16(i)），这是后面把 $\mathcal D_X$ 的阶数片段当作凝聚层处理的前提。

## 关键公式

- $F_1\mathcal D_X=\mathcal O_X\oplus\mathcal T_X$
- $\mathcal D_{X/S,\le1}=\mathcal O_X\oplus\Omega_{X/S}^{\vee}\quad(X\ \text{于}\ S\ \text{上光滑})$
- $\mathcal D_{X/S,\le1}\subset\mathcal O_X\oplus\mathcal T_{X/S}$
- $D_1(U)=R(U)\oplus\operatorname{Der}_k(R(U))$

## 定理与证明

### 命题 1.16（切层与一阶微分算子层）（完整）

设 $X$ 是 $k$ 上的代数簇。则 (i) 切层 $\mathcal T_X$ 是凝聚 $\mathcal O_X$-模；(ii) $F_1\mathcal D_X=\mathcal O_X\oplus\mathcal T_X$。

1. 对仿射开集 $U\subset X$ 有 $D_1(U)=R(U)\oplus\mathcal T_X(U)$，且限制映射与该直和分解相容。  
   *为什么*：直和分解与限制相容，才能在仿射开集构成的基上把 $U\mapsto\mathcal T_X(U)$ 组织成预层。
2. 故 $U\mapsto\mathcal T_X(U)$ 是基上的预层，记其相应的层为 $\mathcal T_X$，称为 $X$ 的切层。  
   *为什么*：层由其在一组拓扑基上的值决定，基上的预层唯一确定一个层。
3. 由 $F_1\mathcal D_X=\mathcal O_X\oplus\mathcal T_X$，而 $F_1\mathcal D_X$ 与 $\mathcal O_X$ 都是层，得 $\mathcal T_X$ 是层，且该等式在 $X$ 上成立。  
   *为什么*：层对直和项封闭：两个直和项之一是层、和为层时，另一项必是层。
4. 由定理 1.15(iii)，$\operatorname{Gr}_1\mathcal D_X$ 是凝聚 $\mathcal O_X$-模；又 $\mathcal T_X\cong\operatorname{Gr}_1\mathcal D_X$，故 $\mathcal T_X$ 凝聚，得 (i)。  
   *为什么*：凝聚性沿 $\mathcal O_X$-模同构传递，(ii) 已给出同构 $\mathcal T_X\cong\operatorname{Gr}_1\mathcal D_X$。

*出处*：命题 1.16 / chap2.tex:236-242


## 易错点

- 光滑性不能省：只有 $X$ 于 $S$ 上光滑时才有 $\mathcal D_{X/S,\le1}=\mathcal O_X\oplus\Omega_{X/S}^{\vee}$，一般情形是包含而非等号。
- 不要与绝对情形的 $\mathcal O_X\oplus\mathcal T_X$ 混写：$\mathcal T_X$ 是导子层，$\Omega_{X/S}^{\vee}$ 是一次微分形式层的对偶；光滑时二者同构，非光滑时不能互换。
- 讲义正文只处理绝对情形（$S=\operatorname{Spec}k$），相对情形仅见于译者注，故本卡的相对陈述都按译者注的强度（子层，不宣称等号）理解。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 II 章 §1 代数簇上的微分算子（含译者注），p.55（PDF p.61），`源码/chapters/chap2.tex:234-247（命题 1.16 与译者注）`

## 核验

状态：`external-confirmed`（2026-11-19）
- Stacks Project：https://stacks.math.columbia.edu/tag/07BK — 该定义给出 $\Omega_{S/R}$ 为形式符号 $\mathrm ds$ 生成的 $S$-模模去 $\mathrm d(rs)=r\,\mathrm ds+s\,\mathrm dr$ 与加法性，并给出泛导子 $\mathrm d:R\to\Omega_{S/R}$；本卡所用 $\Omega_{X/S}$、$\Omega_{X/S}^{\vee}$ 的记法与之一致。卡中关于 $\mathcal D_{X/S,\le1}$ 的断言仍只见于讲义译者注。

## 关联

- `dmod/concept/dz-structure-sheaf`
- `dmod/concept/module-over-algebraic-variety`
