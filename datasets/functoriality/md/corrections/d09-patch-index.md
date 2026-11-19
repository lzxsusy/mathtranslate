# 原文 p.26：第 0 片的像应为 $M_0$

> `functoriality/correction/d09-patch-index` ｜ 原书 p.26 ｜ draft

**一句话**：局部椭圆估计中第 0 片映到 $M_j$，按分片编号应为 $M_0$。

**自测**：为什么第 0 片会映到 $M_j$，而不是 $M_0$？

## 初版

```
$\wt u_0\colon \bR\times[0,\delta_0] \to M_j$
```

## 改后

```
$\to M_0$
```

## 为什么改

上下文同段写 $\wt u_1\colon\bR\times[\delta_0,\delta_0+\delta_1]\to M_1$；按分片编号，下标 0 的片应落在 $M_0$。

## 补注

中译本照录原文并加译注。

## 易错点

- 拼接曲面的分片标号从 $0$ 开始，第 $j$ 片才映到 $M_j$。
- 此处只是标号笔误，不影响后续 Fredholm 论证。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§3.5，p.26–26（原书 p.26）

关联：`functoriality/concept/quilted-floer`、`functoriality/concept/seam-condition`

来源说明：英文底本 functors.tex 局部椭圆估计一段（A 级）；对照式 (59) 附近的分片标号。
