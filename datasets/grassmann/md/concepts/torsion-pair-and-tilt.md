# 挠对与倾斜

> `grassmann/concept/torsion-pair-and-tilt` · 轨道 3 · Reider 与 Thaddeus 再探 · 状态 draft

> **先自测**：为什么倾斜之后，凝聚层被平移层的扩张会变成二阶扩张？

## 一句话

挠对把凝聚层范畴分成低斜率无挠层与高斜率层（含挠层）两部分，其倾斜心 $\mathcal A_s$ 是 Bridgeland 稳定性的舞台，心的移位使 $\Ext^1$ 跳成 $\Ext^2$。

## 定义

阿贝尔范畴 $\mathcal A$ 的一对满子范畴 $(\mathcal F,\mathcal T)$ 称为**挠对**，若 (a) 对 $T\in\mathcal T$、$F\in\mathcal F$ 有 $\Hom(T,F)=0$；(b) 每个 $A$ 有唯一扩张 $0\to T\to A\to F\to0$。取 $\mathcal F_s$ 由斜率 $\mu\le s$ 的无挠稳定层生成、$\mathcal T_s$ 由 $\mu>s$ 的无挠稳定层与挠层生成，则 $(\mathcal F_s,\mathcal T_s)$ 是挠对；其**倾斜心**为 $\mathcal A_s=\{E^\bullet\mid \operatorname H^{-1}\in\mathcal F_s,\ \operatorname H^0\in\mathcal T_s,\ \text{其余}\ \operatorname H^i=0\}$，它自动是阿贝尔范畴。

**记号约定**：$\mathcal A_s$ 称为 $(\mathcal F_s,\mathcal T_s)$ 的倾斜（tilt）；在 $K(\mathcal D)$ 中 $[E^\bullet]=[\operatorname H^0(E^\bullet)]-[\operatorname H^{-1}(E^\bullet)]$。

## 要点（为什么需要它）

- 挠对定义中 $\Hom(T,F)=0$ 的方向不能反：是「高斜率到低斜率」与「挠到无挠」的态射消失。
- $\mathcal A_s$ 的对象是二项复形，包含 $F[1]$ 这种平移，所以它不是凝聚层范畴的子范畴。
- $\Ext^1_{\mathcal A_s}(T,F[1])=\Ext^2_{\mathcal O_X}(T,F)$：心内的一阶扩张被移位搬成层上的二阶扩张，这是全章的技术支点。
- 倾斜随 $s$ 变化：当 $s$ 穿过某个稳定层的斜率时心改变，这正是穿墙现象的来源。

## 关键公式

$$
\Hom(T,F)=0,\qquad 0\to T\to A\to F\to0
$$

$$
\Ext^1_{\mathcal A_s}(T,F[1])=\Ext^2_{\mathcal O_X}(T,F)
$$

## 定理与证明（或缺口）

### 应用 3.1（斜率挠对）

对每个实数 $s$，设 $\mathcal F_s$、$\mathcal T_s$ 分别由斜率 $\mu\le s$ 的无挠 $H$-稳定层、以及斜率 $\mu>s$ 的无挠稳定层与全部挠层生成。则 $(\mathcal F_s,\mathcal T_s)$ 是凝聚层范畴的挠对。

**证明状态：完整**

1. 验证 $\Hom(T,F)=0$：若 $T,F$ 稳定且 $\mu(T)>\mu(F)$ 则无非零态射；若 $T$ 挠而 $F$ 无挠，同样有 $\Hom(T,F)=0$。
   - *为什么*：稳定性与挠/无挠层的基本性质。
2. 对任意凝聚层 $E$，取 Harder–Narasimhan 滤过中满足 $\mu(E_i/E_{i-1})>s$ 的最大子层 $E(s)$，则 $0\to E(s)\to E\to E/E(s)\to0$ 给出所需扩张。
   - *为什么*：HN 滤过的定义保证 $E(s)\in\mathcal T_s$、商落在 $\mathcal F_s$。


出处：中译 p.59（§3 应用 3.1）

### 定理（Happel–Reiten–Smalø）

给定挠对 $(\mathcal F,\mathcal T)$，在 $\mathcal D(\mathcal A)$ 上存在 $t$-结构，其心为 $\mathcal A_{(\mathcal F,\mathcal T)}=\{E^\bullet\mid \operatorname H^{-1}\in\mathcal F,\ \operatorname H^0\in\mathcal T,\ \text{其余为零}\}$，且该心是阿贝尔范畴。

**证明状态：只引出处，原书不重证**


出处：中译 p.59（§3，引 [HRS96]）

## 易错点

- $\mathcal A_s$ 不是由层组成的范畴，比较子对象必须在心里做；把 $L\otimes\mathcal I_Z$ 的凝聚层子层直接拿来当心内子对象会数错。
- 挠对的写法 $\Hom(T,F)=0$ 若与 $\Hom(F,T)=0$ 混淆，整条斜率比较的方向都会反。
- $s$ 为有理数时倾斜的好性质容易验证，无理情形原文明确回避；不要假设任意实数 $s$ 都有同样结论。

## 相关卡

- [Bridgeland 稳定性条件](../concepts/bridgeland-stability-condition.md)
- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)
- [Jordan–Hölder 滤过与 S-等价](../concepts/jordan-holder-filtration.md)

## 出处

- ch3 §3 挠对与倾斜；中译 p.60（英文 PDF p.65），源码 `chapters/ch03.tex:247`
