# 定理 3.3 证明里 #ker N 的不等号方向反了

> `raskin_lcft/correction/ker-n-direction` ｜ 原书 p.11 ｜ reviewed

**一句话**：原文写 #ker(N) ≤ (q²−1)/(q−1)，但范数像含于 F_q^×，故应 ≥；真正给出 ≤ 的是 x^{q+1}−1 的次数，两侧夹逼才得 q+1。

**自测**：只把不等号改过来，为什么就能得到 #ker N = q+1？

## 初版

```
$\#\ker(N)\le (q^2-1)/(q-1)$。
```

## 改后

```
$\#\ker(N)\ge (q^2-1)/(q-1)$，另由 $\#\ker(N)\le q+1$ 夹逼得 $\#\ker(N)=q+1$。
```

## 为什么改

$N:\mathbb F_{q^2}^\times\to\mathbb F_q^\times$ 的像含于 $\mathbb F_q^\times$，故核的大小至少是 $(q^2-1)/(q-1)=q+1$。另一侧：核中元素满足 $x^{q+1}=N(x)=1$，而 $x^{q+1}-1$ 是次数 $q+1$ 的多项式，至多 $q+1$ 个根。两侧相夹即得等号。原文的方向若成立，与「像含于 $\mathbb F_q^\times$」矛盾。

## 补注

译文径改并加注；原文 p.11 的 $\le$ 应为 $\ge$。

## 易错点

- 把 $x^{q+1}=N(x)$ 写成 $x^{q}=N(x)$，核的估计就会错一个 $q$。
- 只看不等号不看夹逼：单边不等式给不出 $q+1$，必须两侧都有。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 3 讲 带驯分歧的范数群，p.11–12（原书 p.11）

关联：`raskin_lcft/concept/tame-ramification`、`raskin_lcft/concept/norm-group`

来源说明：勘误来自本次校对（对照 MIT OCW 公开讲义 PDF 逐页核校）；译文用 % [原文疑误：…] 注释留痕，注释不进 PDF。
