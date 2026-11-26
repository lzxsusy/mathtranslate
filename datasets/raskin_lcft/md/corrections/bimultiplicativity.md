# 双乘性的解释句把 ax²+bcy² 印成 ax²+by²

> `raskin_lcft/correction/bimultiplicativity` ｜ 原书 p.6 ｜ reviewed

**一句话**：原文解释双乘性时把两个方程印成同一个 ax²+by²=1；正确者第一式左边应为 ax²+bcy²=1，否则整句变成同义反复。

**自测**：为什么「(a,bc)=1 ⟺ (a,b)=1 且 (a,c)=1」这两个方程里，第一个必须是 ax²+bcy²=1？

## 初版

```
双乘性：$ax^2+by^2=1$ 可解 $\iff$「$ax^2+by^2=1$ 与 $ax^2+cy^2=1$ 分别可解」或「两者都不可解」。
```

## 改后

```
双乘性：$ax^2+bcy^2=1$ 可解 $\iff$「$ax^2+by^2=1$ 与 $ax^2+cy^2=1$ 分别可解」或「两者都不可解」。
```

## 为什么改

双乘性说的是 $(a,bc)_K=(a,b)_K(a,c)_K$，即「$b$、$c$ 都是范数 $\iff$ $bc$ 是范数」。若首个方程也印成 $ax^2+by^2=1$，句子退化为「$P\iff(P\wedge Q)\vee(\neg P\wedge\neg Q)$」，只在 $P\Rightarrow Q$ 时成立，双乘性本身反而丢了。按 $b\mapsto bc$ 复原即得正确表述。

## 补注

译文径改并加注；底本 p.6 两处均作 by²，属排印重复，不是译误。

## 易错点

- 把 $(a,bc)$ 误写成 $(ab,c)$（配对两个变元的角色不对称）。
- 在 $b$ 或 $c$ 为平方时仍拿这条去证非平凡结论（此时两侧都平凡）。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 2 讲 希尔伯特符号，p.6–8（原书 p.6）

关联：`raskin_lcft/concept/hilbert-symbol`、`raskin_lcft/concept/lcft-main-theorem`

来源说明：勘误来自本次校对（对照 MIT OCW 公开讲义 PDF 逐页核校）；译文用 % [原文疑误：…] 注释留痕，注释不进 PDF。
