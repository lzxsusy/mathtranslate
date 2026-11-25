# Bridgeland 稳定性条件

> `grassmann/concept/bridgeland-stability-condition` · 轨道 3 · Reider 与 Thaddeus 再探 · 状态 draft

> **先自测**：为什么 Bridgeland 稳定性条件必须定义在倾斜心 $\mathcal A_s$ 上，而不能直接定义在凝聚层范畴上？

## 一句话

Bridgeland 稳定性条件是在倾斜心 $\mathcal A_s$ 上由中心荷 $Z_{s+it}$ 的相位与斜率定义的稳定性，Reider 论证因此被改写为斜率不等式的推论。

## 定义

固定 $0<s<1$，设 $\mathcal A_s$ 是挠对 $(\mathcal F_s,\mathcal T_s)$ 的倾斜心。**中心荷** $Z_{s+it}=-d_{(s,t)}+it\,r_s$ 把 $\mathcal A_s$ 的非零对象送到上半平面，相位 $\arg Z_{s+it}\in(0,1]$；**斜率**为 $\mu_{s+it}=\frac{d_{(s,t)}}{t\,r_s}=-\frac{\Re Z_{s+it}}{\Im Z_{s+it}}$。对象 $E^\bullet$ 称为 $\mu_{s+it}$-**稳定的**，若对每个真子对象 $K^\bullet\subset E^\bullet$（商具有非零中心荷）都有 $\mu_{s+it}(K^\bullet)<\mu_{s+it}(E^\bullet)$；完整的 Bridgeland 定义还要求每个对象都有有限长度的 Harder–Narasimhan 滤过。

**记号约定**：$r_s([E^\bullet])=c_1(E^\bullet)\cdot H^{n-1}-s\,r(E^\bullet)H^n$；$d_{(s,t)}([E^\bullet])=\operatorname{ch}_2(E^\bullet)\cdot H^{n-2}-s\,c_1(E^\bullet)\cdot H^{n-1}+\frac{s^2-t^2}{2}r(E^\bullet)H^n$；$t>0$。

## 要点（为什么需要它）

- 与 Mumford 稳定性不同，这里的对象是二项复形：$\mathcal O_X[1]$ 与 $L\otimes\mathcal I_Z$ 只有在同一个心 $\mathcal A_s$ 内才可比。
- 中心荷取上半平面值是关键：它保证相位有界、两条斜率可以比较，从而 $\mu$ 具有斜率函数的单调性。
- Harder–Narasimhan 滤过的存在性是无理 $(s,t)$ 时最微妙的部分，原文承认自己对稳定性概念「使用略显宽松」。
- 它比「$\Hom$ 消没」强：后者只是斜率不等式的推论，因此重访版需要更强的数值条件 $(2d+1)^2$ 而不是 $4d$。

## 关键公式

$$
Z_{s+it}(E^\bullet)=-d_{(s,t)}(E^\bullet)+it\,r_s(E^\bullet)
$$

$$
\mu_{s+it}=\frac{d_{(s,t)}}{t\,r_s}=-\frac{\Re Z_{s+it}}{\Im Z_{s+it}}
$$

$$
0<\arg Z_{s+it}(E^\bullet)\le1
$$

## 定理与证明（或缺口）

### 命题 3.6（$\mathcal O_X[1]$ 与 $L$ 的稳定性）

对所有 $s\ge0$ 与 $t>0$，$\mathcal O_X[1]$ 是 $\mathcal A_s$ 的 $\mu_{s+it}$-稳定对象；对所有 $s<1$ 与 $t>0$，$L$ 是 $\mathcal A_s$ 的 $\mu_{s+it}$-稳定对象。

**证明状态：完整**

1. 设 $K^\bullet\subset\mathcal O_X[1]$ 是去稳定化子对象，$Q^\bullet=\mathcal O_X[1]/K^\bullet$，取 $Q$ 的 Harder–Narasimhan 分次中的稳定层 $E$，则 $0<\mu_H(E)\le s$。
   - *为什么*：$\mathcal O_X[1]$ 在 $\mathcal A_s$ 中的子对象分类（情形 (iii)）给出该斜率范围。
2. 把两条斜率公式代入 $\mu_{s+it}(\mathcal O_X[1])<\mu_{s+it}(E[1])$，等价于 $(s^2+t^2)c_1(E)\cdot H^{n-1}>2s\,\operatorname{ch}_2(E)\cdot H^{n-2}$。
   - *为什么*：通分并消去 $(s^2-t^2)$ 项。
3. 由 Bogomolov 不等式与 Hodge 指标定理该不等式成立，故任何子对象的斜率都小于 $\mathcal O_X[1]$。
   - *为什么*：Bogomolov 给 $(2s)\operatorname{ch}_2\le s c_1^2/r$，Hodge 给 $s c_1^2/r\le s^2 c_1\cdot H$，再用 $t>0$。
4. $L$ 的情形类似：$L$ 的子对象 $K'$ 满足 $s<\mu_H(E')<1$，同样由 Bogomolov 与 Hodge 得 $\mu_{s+it}(E')<\mu_{s+it}(L)$。
   - *为什么*：与 (a) 相同的两手，只是斜率区间换成 $s<\\mu_H<1$。


出处：中译 p.64（§3 命题 3.6）

## 易错点

- $\mathcal A_s$ 的对象不都是凝聚层：$\mathcal O_X[1]$ 是平移对象，讨论子对象必须在倾斜心里进行，回到凝聚层范畴会漏掉移位部分。
- 稳定性定义要求商具有非零中心荷；忽略这一条会把支在余维 $\ge3$ 的挠层当作合法的去稳定化子对象。
- $(s,t)$ 为无理数时 Harder–Narasimhan 滤过的存在性并非自动，原文只对有理值给出完整论证，并明确把一般情形留给 [Bri08]。

## 相关卡

- [挠对与倾斜](../concepts/torsion-pair-and-tilt.md)
- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)
- [Jordan–Hölder 滤过与 S-等价](../concepts/jordan-holder-filtration.md)

## 出处

- ch3 §1 引言（Bridgeland 稳定性条件）；中译 p.55（英文 PDF p.60），源码 `chapters/ch03.tex:34`
