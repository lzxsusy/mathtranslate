# 定义 9.9 的零伦公式指标整体位移一位

> `raskin_lcft/correction/homotopy-index` ｜ 原书 p.40 ｜ reviewed

**一句话**：原文写 d_i h_{i+1}+h_i d_{i+1}=f_{i+1}，按此式 f 的下标与两边不匹配；标准约定是 f_i=d_{i−1}h_i+h_{i+1}d_i。

**自测**：为什么 h 必须把 X_i 打到 Y_{i−1}，公式才可能成立？

## 初版

```
$d_i h_{i+1}+h_i d_{i+1}=f_{i+1}$。
```

## 改后

```
$f_i=d_{i-1}h_i+h_{i+1}d_i$，其中 $h_i:X_i\to Y_{i-1}$。
```

## 为什么改

零伦的意义是 $f=d h+h d$ 且两项都同型。若 $h_i:X_i\to Y_{i-1}$，则 $d_{i-1}h_i:X_i\to Y_{i-2}$ 与 $h_{i+1}d_i:X_i\to Y_{i-1}$ 都要落在 $f_i:X_i\to Y_{i-1}$ 的两侧才能相加（按符号约定亦可）。原文把 $i$ 写成 $i+1$，左边于是落在无意义的层，引理 9.10 的证明 $f(x)=d(h(x))$ 也随之不自洽。

## 补注

译文按标准约定改写并加注；引理 9.10 的证明同步改精确（取 $d_i x=0$）。

## 易错点

- 把 $h$ 的方向记成 $X_i\to Y_i$：那样 $h_{i+1}d_i$ 的复合根本接不上。
- 只改一处下标而不同时改引理 9.10 的证明，会留下新的不自洽。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 9 讲 希尔伯特定理 90 与上链复形，p.40–41（原书 p.40）

关联：`raskin_lcft/concept/tate-cohomology-unbounded`、`raskin_lcft/concept/tate-cohomology`

来源说明：勘误来自本次校对（对照 MIT OCW 公开讲义 PDF 逐页核校）；译文用 % [原文疑误：…] 注释留痕，注释不进 PDF。
