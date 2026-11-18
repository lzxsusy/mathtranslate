# 译文修订 section-19-c.tex:33

> `seidel/correction/a12-section-19-c-33` ｜ 原书 p.300 ｜ draft

**一句话**：初版此处误译：英文 p300 作 "unique up to isotopy and orientation-reversal"

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
"……满足 $(\mu_j^{k+1})^{-1}(C^{k+1})=\{-1,1\}$，在同痕及**反转定向**…
```

## 改后

```
"……在**同痕及反向**意义下唯一。"
```

## 为什么改

英文 p300 作 "unique up to isotopy and orientation-reversal"。这里被反向的是匹配路径 $\mu_j^{k+1}:[-1,1]\to\CC$ 的**参数方向**（即 $\mu(t)\mapsto\mu(-t)$），不是流形的定向。本书 "orientation" 一词专用于流形/膜的定向（§12 的 Pin 结构、$\Z/2$ 定向反转），原译"反转定向"会把这些概念混在一起，读者会误以为要反转 $\CC$ 或膜的定向。

## 补注

见分章报告 A12；修订总表第 28 条。 引文截取至 60 字以内。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.300–300（原书 p.300）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据 A12 分章报告与修订总表；原文页码由 reason 或 page_map 推出。
