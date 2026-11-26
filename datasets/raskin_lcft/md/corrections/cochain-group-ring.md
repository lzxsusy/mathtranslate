# n-上闭链所在的项印成 Z[G]⊗M

> `raskin_lcft/correction/cochain-group-ring` ｜ 原书 p.56 ｜ reviewed

**一句话**：说「位于 Z[G]⊗M 的微分核中的元素叫 n-上闭链」时，该复形第 n 项其实是 Z[G^n]⊗M；Z[G]⊗M 只对应 n=1。

**自测**：为什么非齐次上链复形的第 n 项是 Z[G^n]⊗M，而不是 Z[G]⊗M？

## 初版

```
位于 $\mathbb Z[G]\otimes M$ 的微分核中的元素称为 $n$-上闭链。
```

## 改后

```
位于 $\mathbb Z[G^n]\otimes M$ 的微分核中的元素称为 $n$-上闭链。
```

## 为什么改

非齐次上链复形的第 $n$ 项由 $n$ 个 $G$ 因子给出：$\mathbb Z[G^n]\otimes M$（$n=0$ 时为 $M$）。原文在 $n=1$ 的例子处写对了 $\mathbb Z[G]$，随即用它定义一般的 $n$-上闭链，把下标留在了句子里。按定义域核对即知应为 $\mathbb Z[G^n]$（其中 $\mathbb Z[G\times G]=\mathbb Z[G^2]$）。

## 补注

译文径改并加注；原文 p.56 该句承接前文举例，修改不影响公式编号。

## 易错点

- 把 $\mathbb Z[G^n]$ 读成「$\mathbb Z[G]$ 的 n 次张量」：它是 $n$ 个 $G$ 因子的直积的群环。
- 在 $n=0$ 时套用 $\mathbb Z[G^n]$ 而不特判（$G^0$ 为单点，$\mathbb Z[G^0]=\mathbb Z$）。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 12 讲 导出函子与显式投射消解，p.52–56（原书 p.52）

关联：`raskin_lcft/concept/tate-cohomology`、`raskin_lcft/concept/hilbert-theorem-90`

来源说明：勘误来自本次校对（对照 MIT OCW 公开讲义 PDF 逐页核校）；译文用 % [原文疑误：…] 注释留痕，注释不进 PDF。
