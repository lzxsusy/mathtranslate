# 译文修订 section-12-gh.tex:8

> `seidel/correction/a07-section-12-gh-8` ｜ 原书 p.184 ｜ draft

**一句话**：初版此处误译：原书印刷页 183 作 `(z3,…,zd) ∈ (∂D)^{d−2}`：这是一个 $d-2$ 元组，属于该乘积空间，不是它的子集

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
$(z_3,\allowbreak \ldots,\allowbreak z_d)\subset(\partial…
```

## 改后

```
改为 `\in(\partial D)^{d-2}
```

## 为什么改

原书印刷页 183 作 `(z3,…,zd) ∈ (∂D)^{d−2}`：这是一个 $d-2$ 元组，属于该乘积空间，不是它的子集。$\subset$ 会让读者误以为在讨论某个子集族，属记号笔误。

## 补注

见分章报告 A07；修订总表第 14 条。 引文截取至 60 字以内。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.184–184（原书 p.184）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据 A07 分章报告与修订总表；原文页码由 reason 或 page_map 推出。
