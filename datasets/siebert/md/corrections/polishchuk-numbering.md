# Polishchuk 命题编号 3.1 → 3.7

> `siebert/correction/polishchuk-numbering` ｜ 原书 p.105 ｜ draft

**一句话**：译文把 bar 复形计算引作 Polishchuk 的命题 3.1，原文是 Proposition 3.7；引错号会让读者按号查找时找不到对应结论。

**自测**：引用编号差了六个号，为什么这不是小事、必须按原文改成 3.7？

## 初版

```
这就是此处使用的 Polishchuk 的命题 3.1。
```

## 改后

```
这就是此处使用的 Polishchuk 的命题 3.7。
```

## 为什么改

英文原文（原书 p.105，英文原文第 4888 行）写的是 “This is Proposition 3.7 in Polishchuk.”，译文误作 3.1。引用编号是读者定位文献的唯一线索：Polishchuk（arXiv:math/0302178）的命题 3.1 不是这条 bar 复形计算，按 3.1 去查会得到另一个结论，整段证明的依据就断了。据本轮校对记录（校对/ch06.jsonl 第 2 条，applied=true，p.103 line311），改动依据即原文该行；讲义 p.105 同时给出指向 arXiv:math/0302178 的超链接。

## 补注

位置在 §3.6 命题 6.5 的证明中：讲完广义 bar 复形 $K^\bullet_l=B^\bullet(k,M,\ldots,M,k)$ 与该 bar 复形计算可对 $n$ 归纳之后，用这句话把计算归给 Polishchuk。改动只涉及编号，正文其余不变。另附：原书目录与章标题把 rigidity 拼成 “rigidiy”（英文原文第 149、4687 行），译文拼写正确，不另立卡。

## 易错点

- 别按 3.1 去 Polishchuk 文中找：3.7 才是 $B^\bullet(M_1,\ldots,M_n)$ 的 bar 复形计算。
- 超链接只给到 arXiv 摘要页，没标版本号；若 Polishchuk 文改版，编号可能移动，引用时最好带上定理内容。
- 编号错误不影响数学，但会让读者无法复核，属于必须改的实质性引用错误。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，校订，p.105–105（原书 p.105）

关联：`siebert/deriv/rigidity-theorem`、`siebert/concept/hochschild-cohomology`

来源说明：原书 p.105（英文原文 4888 行 “This is Proposition 3.7 in Polishchuk”）；校对/ch06.jsonl 第 2 条（applied）。Polishchuk, arXiv:math/0302178 为讲义该处所引文献（p.105 超链接）。
