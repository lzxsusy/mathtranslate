# 原文 p.24：右模映射的指标 $r_k$ 应为 $r_a$

> `functoriality/correction/d08-right-module-index` ｜ 原书 p.24 ｜ draft

**一句话**：图 11 中右模映射右端的指标 $k$ 与左端因子个数 $a$ 不符，应为 $r_1+\cdots+r_a$。

**自测**：右模映射定义里左端有 $a$ 个 $K$ 因子，右端为何写成 $r_1+\cdots+r_k$？

## 初版

```
$J_a \times K_{r_1} \times \cdots \times K_{r_a} \to J_{r_1+\cdots+r_k}$
```

## 改后

```
$\to J_{r_1+\cdots+r_a}$
```

## 为什么改

左端恰有 $a$ 个 $K$ 因子（$K_{r_1},\dots,K_{r_a}$），右端应把它们全数相加；$k$ 在式中无定义。

## 补注

中译本照录原文并加译注。

## 易错点

- $k$ 在式内没有定义，不要照抄成通用指标。
- 左模与右模的不对称正体现在这里：右模多一个 $J_a$ 因子，末项随 $a$ 走。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§3.4，p.24–24（原书 p.24）

关联：`functoriality/concept/composite-polytope`、`functoriality/concept/guillemin-sternberg`

来源说明：英文底本 functors.tex 图 11 的定义项（A 级）；对照同页左模定义。
