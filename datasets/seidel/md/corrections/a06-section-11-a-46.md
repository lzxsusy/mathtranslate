# 译文修订 section-11-a.tex:46

> `seidel/correction/a06-section-11-a-46` ｜ 原书 p.151 ｜ draft

**一句话**：初版漏译「removing the sign」且保留符号因子；改为补出「（即去掉符号）」并删去 $(-1)^{\cdots}$ 因子：原书 p151 讲的是换用另一种约定，两处必须同时改。

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
提一下另一种可能的约定，也许有助于理解：将\eref{11.2}右侧换成<br>`\[(-1)^{\dim(\operatorname{coker}D_2)\cdot\operatorname{index}(D_1)}\bigwedge_iw_{1,i}^\vee\wedge\cdots\]`
```

## 改后

```
提一下另一种可能的约定，也许有助于理解：将\eref{11.2}右侧换成（即去掉符号）<br>`\[\bigwedge_iw_{1,i}^\vee\wedge\bigwedge_iw_{2,i}^\vee\otimes\bigwedge_iv_{1,i}\wedge\bigwedge_iv_{2,i}\]`
```

## 为什么改

原书 p151 此处说的是「改用另一约定（removing the sign）」，即把式 (11.2) 的符号因子去掉。旧译既保留 $(-1)^{\cdots}$ 因子，又未译出「去掉符号」，与「另一种约定」自相矛盾，读者无法判断到底改了哪里。补出「（即去掉符号）」并删去符号因子后，与下文「这样得到另一个线丛 $\underline{\det}'$」逻辑一致。

## 补注

见分章报告 A06；修订总表第 10 条（section-11-a.tex:46，印刷页 151）。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.151–151（原书 p.151）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据修订总表、分章报告与原书印刷页图逐条核对（PDF 页 = 印刷页 + 8）；页码已回页确认。
