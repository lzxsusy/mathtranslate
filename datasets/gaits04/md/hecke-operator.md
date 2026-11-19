# Hecke 算子等于 $T_x^i$

> `gaits04/concept/hecke-operator` · 轨 C 向量丛与 Hecke · 状态 reviewed · 核验 source-only

**问题：** 为什么「拉回再推前」定义的几何算子会等于函数的 Hecke 算子？

**一句话：** 算子 $f\mapsto(h^{\rightarrow})_!((h^{\leftarrow})^*f)$ 从 $\operatorname{Funct}(\mathrm{Bun}_n)$ 到自身，等于 Hecke 算子 $T_x^i$。

**别名：** `Hecke operator`、`T_x^i`、`Proposition 2.6`

## 定义

注意 $k_x$ 是有限域，故 $h^\leftarrow$ 与 $h^\rightarrow$ 的纤维都是有限集。考虑从 $\operatorname{Funct}(\mathrm{Bun}_n)$ 到自身的算子，由 $f\mapsto(h^{\rightarrow})_!((h^{\leftarrow})^*(f))$ 给出（上标 $*$ 表示沿指定态射的函数拉回，下标 $!$ 表示沿纤维求和）。命题 2.6：上述算子等于 $T_x^i(f)$。

**记号：** $(h^{\leftarrow})^*$：沿 $h^\leftarrow$ 拉回函数；$(h^{\rightarrow})_!$：沿纤维求和；$T_x^i$：§1.6 的双陪集特征函数在球向量上的作用。

## 要点

- 有限性来自 $k_x$ 有限：纤维是 Grassmann 簇的 $k_x$-点集，故求和是有限和。
- 几何算子在「同构类」层面计数：$h^\leftarrow$ 拉回把 $f$ 拉成三元组上的函数，$h^\rightarrow$ 推前沿 $M'$ 求和。
- 命题的证明就是把两侧逐点展开：一侧是双陪集特征函数的卷积，另一侧是 Grassmann 纤维的计数。

## 公式

$$
f\mapsto(h^{\rightarrow})_!((h^{\leftarrow})^*(f))
$$

## 定理与证明

**命题 2.6**　算子 $f\mapsto(h^{\rightarrow})_!((h^{\leftarrow})^*(f))$ 等于 $T_x^i(f)$。

> 跳步说明：原书未展开证明，只说与 §1.6 的定义直接对照。

*出处：§2.6，原书 p.275*

## 易错点

- 把 $!$ 与 $*$ 写反：$*$ 在 $h^\leftarrow$ 上（拉回到三元组），$!$ 在 $h^\rightarrow$ 上（沿 $M'$ 求和）。写反得到的是另一个算子。

## 批注

**〔背景直觉〕为什么这很重要**　这一步把「表示论里的 Hecke 算子」翻译成「向量丛上的对应」，几何 Langlands 才有立足点：一旦算子是几何的，就可以把它抬到层上（§3.2），再问它的本征对象是什么。

## 相关

[[hecke-correspondence]]、[[hecke-functor]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§2.5–2.6，原书 pp. 275（PDF pp. 277）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec2.tex:51-66（§2.5–§2.6）`
