# 译文修订 section-17-a.tex:45

> `seidel/correction/a09-section-17-a-45` ｜ 原书 p.237 ｜ draft

**一句话**：初版 (17.5) 左端漏写自变量，改为 $R(\partial_s,\partial_t)$：原书 p237 是曲率张量在 $(\partial_s,\partial_t)$ 上的取值，两边类型才相符。

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
$R=\bigl(\cdots\bigr)ds\wedge dt$
```

## 改后

```
$R(\partial_s,\partial_t)=\bigl(\cdots\bigr)ds\wedge dt$
```

## 为什么改

原书 p237 的 (17.5) 左端是曲率张量在 $(\partial_s,\partial_t)$ 上的取值，译文漏掉自变量，等式两边类型不符。

## 补注

见分章报告 A09；修订总表第 27 条（section-17-a.tex:45，印刷页 237）。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.237–237（原书 p.237）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据修订总表、分章报告与原书印刷页图逐条核对（PDF 页 = 印刷页 + 8）；页码已回页确认。
