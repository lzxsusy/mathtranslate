# 译文修订 section-11-ef.tex:123

> `seidel/correction/a06-section-11-ef-123` ｜ 原书 p.158 ｜ draft

**一句话**：初版此处误译：原文为 those $s$ where $\alpha(s)$ has a nonempty null space

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
更确切地说，来自 $\alpha(s)$ 的零空间非零的时刻 $s$。
```

## 改后

```
更确切地说，来自使 $\alpha(s)$ 的零空间非平凡的那些 $s$。
```

## 为什么改

原文为 those $s$ where $\alpha(s)$ has a nonempty null space。零空间是子空间，「非零」不适用于子空间（零空间永远含零向量），应为「非平凡（非零维）」；主语也应是 $s$ 而非「时刻」。

## 补注

见分章报告 A06；修订总表第 10 条。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.158–158（原书 p.158）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据 A06 分章报告与修订总表；原文页码由 reason 或 page_map 推出。
