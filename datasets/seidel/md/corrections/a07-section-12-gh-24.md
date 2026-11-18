# 译文修订 section-12-gh.tex:24

> `seidel/correction/a07-section-12-gh-24` ｜ 原书 p.184 ｜ draft

**一句话**：初版维数公式末项 $+d-2$ 改为 $+2-d$：原书 p184 作 $i(y_0)-\cdots-i(y_d)+2-d$，同段下一句与 $\mu^d$ 的次数要求都只能是 $+2-d$；颠倒次序会使维数公式与零维条件矛盾。

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
模空间 $\M^{d+1}(y_0,\ldots,y_d)$ 的维数为 $i(y_0)-i(y_1)-\cdots-i(y_d)+d-2$
```

## 改后

```
末项改为 $+2-d$
```

## 为什么改

原书印刷页 184 明确作 `i(y0) − i(y1) − ··· − i(yd) + 2 − d`；同段下一句「$i(y_0)=i(y_1)+\cdots+i(y_d)+2-d$」与 $\mu^d$ 要求的次数 $2-d$ 都只能是 $+2-d$。旧译把 $2$ 与 $d$ 的次序颠倒，使维数公式与紧随其后的零维条件互相矛盾。

## 补注

见分章报告 A07；修订总表第 15 条（section-12-gh.tex:24，印刷页 184）。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.184–184（原书 p.184）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据修订总表、分章报告与原书印刷页图逐条核对（PDF 页 = 印刷页 + 8）；页码已回页确认。
