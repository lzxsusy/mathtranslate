# 译文修订 section-16-ab.tex:9

> `seidel/correction/a09-section-16-ab-9` ｜ 原书 p.221 ｜ draft

**一句话**：初版「$n\leq3$ 时可缩」改为「$n<3$ 时可缩」：原书 p221 作 "contractible for $n<3$"，只断言 $n=1,2$；译文把范围放宽到 $n\leq3$，超出原书结论，故改回。

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
已知 $n\leq3$ 时 $\operatorname{Diff}(S^n)/O_{n+1}$ 可缩
```

## 改后

```
已知 $n<3$ 时……可缩
```

## 为什么改

原书 p221 的 Remark 16.1 明作 "contractible for $n<3$"，只断言 $n=1,2$；译文把范围放宽成 $n\leq3$，替作者扩大了断言，故改回 $n<3$。

## 补注

见分章报告 A09；修订总表第 20 条（section-16-ab.tex:9，印刷页 221）。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.221–221（原书 p.221）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据修订总表、分章报告与原书印刷页图逐条核对（PDF 页 = 印刷页 + 8）；页码已回页确认。
