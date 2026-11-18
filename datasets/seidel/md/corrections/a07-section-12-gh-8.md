# 译文修订 section-12-gh.tex:8

> `seidel/correction/a07-section-12-gh-8` ｜ 原书 p.183 ｜ draft

**一句话**：初版「$(z_3,\allowbreak \ldots,\allowbreak z_d)\subset(\partial D)^{d-2}$」改为「$\in(\partial D)^{d-2}$」：原书 p183 实印 $\subset$，但 $d-2$ 元组属于乘积空间而非其子集，系原书排印笔误（errata 未收，建议补录）。

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
$(z_3,\allowbreak \ldots,\allowbreak z_d)\subset(\partial D)^{d-2}$
```

## 改后

```
改为 `\in(\partial D)^{d-2}`
```

## 为什么改

原书 p183 页图作 "(z3,…,zd) ⊂ (∂D)^{d−2}"：这是一个 $d-2$ 元组，属于该乘积空间，不是它的子集；$\subset$ 系原书排印笔误，应为 $\in$。errata.md 尚未收录此条，建议补入。

## 补注

见分章报告 A07；修订总表第 16 条（section-12-gh.tex:8，印刷页 183）。分章报告已把此条列为「记号笔误」，但报告称原书作 $\in$，与页图不符（原书实印 $\subset$），本卡一并纠正。errata.md 尚未收录，建议补入。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.183–183（原书 p.183）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据修订总表、分章报告与原书印刷页图逐条核对（PDF 页 = 印刷页 + 8）；页码已回页确认。
