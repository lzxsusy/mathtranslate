# 译文修订 section-16-hi.tex:65

> `seidel/correction/a09-section-16-hi-65` ｜ 原书 p.234 ｜ draft

**一句话**：初版 $S^{n+1}\subset\CC^{n+2}$ 改为 $S^n\subset\CC^{n+1}$：原书 p234 页图作 $\sqrt{1-s}\,S^n\subset\CC^{n+1}$；消失圈在 $2n$ 维全空间中是 $n$ 维球面。

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
$V_{\gamma\vert[s,1]}=\sqrt{1-s}\,S^{n+1}\subset\CC^{n+2}$
```

## 改后

```
$V_{\gamma\vert[s,1]}=\sqrt{1-s}\,S^n\subset\CC^{n+1}$
```

## 为什么改

原书 p234 放大确认为 $S^n\subset\CC^{n+1}$；消失圈在 $2n$ 维全空间中是 $n$ 维球面，维数写错会破坏引理 16.15 的整个论证。

## 补注

见分章报告 A09；修订总表第 26 条（section-16-hi.tex:65，印刷页 234）。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.234–234（原书 p.234）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据修订总表、分章报告与原书印刷页图逐条核对（PDF 页 = 印刷页 + 8）；页码已回页确认。
