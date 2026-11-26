# 引理 6.4（正合列的指标乘性）指标链自相矛盾

> `raskin_lcft/correction/exactness-index` ｜ 原书 p.25 ｜ reviewed

**一句话**：原文指标链把 #X_{n−1} 写了两次、两端差一个因子；正确归纳是拆成前段正合列与 0→ker d→X_{n−1}→X_n→0 两条。

**自测**：为什么「n 项交错乘积 = 1」必须用归纳证，而不能靠逐项约分？

## 初版

```
$\#X_0\cdots\#X_n=\#X_0\cdots\#X_{n-1}\cdot\#X_{n-1}/\#\mathrm{Im}(d_{n-1})$。
```

## 改后

```
$\#X_0\#X_2\cdots\#X_{n-2}=\#X_1\#X_3\cdots\#X_{n-3}\cdot\#\ker d_{n-1}$ 与 $\#X_{n-1}=\#\ker d_{n-1}\cdot\#X_n$ 相乘，得 $\#X_0\cdots\#X_n=\#X_1\cdots\#X_{n-1}$。
```

## 为什么改

原式右端已含 $\#X_0\cdots\#X_{n-1}$，再乘 $\#X_{n-1}$ 就把 $X_{n-1}$ 计了两次，且两端相差因子 $\#X_{n-1}/\#\mathrm{Im}(d_{n-1})$。正确做法是对 $n$ 归纳：$0\to X_0\to\cdots\to X_{n-2}\to\ker d_{n-1}\to0$ 与 $0\to\ker d_{n-1}\to X_{n-1}\to X_n\to0$ 分别用归纳假设与「阶相乘」，联立即得。

## 补注

译文整段重写并加注；这是全书唯一需要重写证明的地方（不是改一个符号）。

## 易错点

- 以为「交错乘积 = 1」可由逐项 $\#X_i/\#\mathrm{Im}$ 约分：约分需要预先知道正合性，正是归纳要证的。
- 把 $d_{n-1}$ 的定义域写成 $X_n$（应为 $X_{n-1}$）。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 6 讲 正合列与 Tate 上同调，p.24–26（原书 p.24）

关联：`raskin_lcft/concept/herbrand-quotient`、`raskin_lcft/concept/tate-cohomology`

来源说明：勘误来自本次校对（对照 MIT OCW 公开讲义 PDF 逐页核校）；译文用 % [原文疑误：…] 注释留痕，注释不进 PDF。
