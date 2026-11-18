# 译文修订 section-3.tex:51

> `seidel/correction/a02-section-3-51` ｜ 原书 p.33 ｜ draft

**一句话**：初版此处误译：全书仅此一处用 `\mathcal X`，`src\settings.tex` 也未定义 `\X`；英文原书对应式（合订本 L619）作 `Hom_{H(Q)}(X, Z⊗Y)`，且该同构链其余各项都用 `X`

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
\Hom_{H(\Q)}(\mathcal X,Z\otimes\Y)
```

## 改后

```
\Hom_{H(\Q)}(X,Z\otimes\Y)
```

## 为什么改

全书仅此一处用 `\mathcal X`，`src\settings.tex` 也未定义 `\X`；英文原书对应式（合订本 L619）作 `Hom_{H(Q)}(X, Z⊗Y)`，且该同构链其余各项都用 `X`。属排版/转写残留。

## 补注

见分章报告 A02；修订总表第 4 条（section-3.tex:51，印刷页 33）。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.33–33（原书 p.33）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据修订总表、分章报告与原书印刷页图逐条核对（PDF 页 = 印刷页 + 8）；页码已回页确认。
