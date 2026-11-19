# 原文 p.52：方图的交叉引用应指向 §4.5.1

> `functoriality/correction/d13-crossref-co` ｜ 原书 p.52 ｜ draft

**一句话**：方图说明称所画拼接属于「§4.5.2 中复合双函子的特殊化」，但复合双函子定义在 §4.5.1。

**自测**：复合双函子究竟在 §4.5.1 还是 §4.5.2，为什么引用会错位？

## 初版

```
the specialization of the composition $A_\infty$-bifunctor in \S\ref{sss:CO}
```

## 改后

```
…in §4.5.1
```

## 为什么改

复合双函子定义于 §4.5.1 式 (104)；sss:CO 标签所在的 §4.5.2 讨论的是另一件事。

## 补注

中译本保留原书引用，加译注说明应参看 §4.5.1。

## 易错点

- §4.5.2 讲的是把 $2$-态射特殊化到点上，不是双函子的定义处。
- 式 (104) 是复合双函子的定义，引用它才自洽。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§4.5.2，p.52–52（原书 p.52）

关联：`functoriality/concept/a-infinity-bimodule`、`functoriality/concept/symp-category`

来源说明：英文底本 symp.tex §4.5.2 方图前（A 级）；对照 §4.5.1 式 (104)。
