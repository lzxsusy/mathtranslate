# 中心荷与相位

> `grassmann/concept/central-charge-and-phase` · 轨道 3 · Reider 与 Thaddeus 再探 · 状态 draft

> **先自测**：中心荷取上半平面值这一条，为什么足以保证斜率函数具有通常的单调性？

## 一句话

中心荷 $Z_{s+it}=-d_{(s,t)}+it\,r_s$ 把倾斜心的对象送到上半平面，其相位与斜率 $\mu=-\Re Z/\Im Z$ 共同给出 Bridgeland 稳定性的数值判据。

## 定义

对 $n$ 维光滑射影簇 $X$ 与 $t>0$，**中心荷**定义为 $Z_{s+it}(E^\bullet)=-d_{(s,t)}(E^\bullet)+it\,r_s(E^\bullet)=-\int_X e^{-(s+it)H}\operatorname{ch}(E^\bullet)H^{n-2}$。对 $\mathcal A_s$ 的非零对象有 $Z_{s+it}\ne0$ 且 $0<\arg Z_{s+it}\le1$（其中 $\arg(re^{i\pi\rho})=\rho$），这个角称为**相位**；斜率 $\mu_{s+it}=\frac{d_{(s,t)}}{t\,r_s}=-\frac{\Re Z_{s+it}}{\Im Z_{s+it}}$。

**记号约定**：$r_s$、$d_{(s,t)}$ 同 Bridgeland 稳定性条件卡；$\Re Z=-d_{(s,t)}$，$\Im Z=t\,r_s$。

## 要点（为什么需要它）

- 实部是负次数、虚部是 $t$ 倍秩，因此上半平面性等价于「$r_s>0$，或 $r_s=0$ 且 $d_{(s,t)}\ge0$」。
- 相位把斜率变成角：$\mu=-\cot(\pi\cdot\text{相位})$，于是斜率的单调性可以直接从 $\arg$ 读出。
- 积分写法只在曲面时与 $-d+it\,r_s$ 逐项一致；一般 $n$ 必须保留 $H^{n-2}$ 配对，否则实部虚部都对不上。
- 中心荷为零的对象（支在余维 $\ge3$ 的挠层）不参与稳定性比较，这正是「商具有非零中心荷」这一条件的来源。

## 关键公式

$$
Z_{s+it}(E^\bullet)=-d_{(s,t)}(E^\bullet)+it\,r_s(E^\bullet)
$$

$$
Z_{s+it}(E)=-\int_X e^{-(s+it)H}\operatorname{ch}(E)H^{n-2}
$$

$$
0<\arg Z_{s+it}(E^\bullet)\le1
$$

## 定理与证明（或缺口）

### 推论 3.4（中心荷取上半平面值）

若 $X=S$ 是曲面，则复线性函数 $Z_{s+it}=-d_{(s,t)}+it\,r_s$ 对 $\mathcal A_s$ 的所有非零对象满足 $Z_{s+it}(E^\bullet)\ne0$ 与 $0<\arg Z_{s+it}(E^\bullet)\le1$。

**证明状态：提纲（有缺口）**


> **缺口**：原文只写「由命题 3.3」：把 $E^\bullet$ 拆成挠层与半稳定层的平移两种情形，分别用 $r_s\ge0$ 与 $d_{(s,t)}\ge0$ 验证；$r_s>0$ 与 $r_s=0$ 的边界、以及相位落在 $(0,1]$ 而非 $[0,1]$ 的逐项核对没有展开。


出处：中译 p.63（§3 推论 3.4）

### 推论 3.7（Kodaira 消没定理的特例）

若 $\dim X=n>1$，则 $\operatorname H^{n-1}(X,K_X+L)=0$。

**证明状态：完整**

1. 在半圆 $t^2+(s-\frac12)^2<\frac14$（$t>0$）内，$\mu_{s+it}(L)>\mu_{s+it}(\mathcal O_X[1])$。
   - *为什么*：代入两条斜率公式直接比较，见半圆比较例。
2. 由命题 3.6，$L$ 与 $\mathcal O_X[1]$ 都是 $\mu_{s+it}$-稳定的，故 $\Hom_{\mathcal A_s}(L,\mathcal O_X[1])=0$。
   - *为什么*：斜率严格大的稳定对象之间没有非零态射。
3. 倾斜心内的 $\Hom$ 与层上 $\Ext^1$ 一致，再用 Serre 对偶得 $\operatorname H^{n-1}(X,K_X+L)^\vee=0$。
   - *为什么*：$\Hom_{\mathcal A_s}(L,\mathcal O_X[1])\cong\Ext^1_{\mathcal O_X}(L,\mathcal O_X)$，而后者对偶于 $H^{n-1}(X,K_X+L)$。


出处：中译 p.64（§3 推论 3.7）

## 易错点

- 原书把中心荷的积分域写成曲面 $S$ 却保留 $H^{n-2}$，只在 $n=2$ 时自洽；一般 $n$ 应写 $\int_X$（译注 10）。
- $Z_{s+it}(E^\bullet)=0$ 的对象（支在余维 $\ge3$ 的挠层）不参与稳定性比较，把它当作稳定的去稳定化子对象会得到错误结论。
- 相位约定是 $\arg(re^{i\pi\rho})=\rho$，取值 $(0,1]$，不是通常的 $\arg\in(-\pi,\pi]$；差一个 $\pi$ 会把斜率符号弄反。

## 相关卡

- [Bridgeland 稳定性条件](../concepts/bridgeland-stability-condition.md)
- [墙与穿墙](../concepts/wall-and-wall-crossing.md)
- [有效除子的斜率](../concepts/slope-of-effective-divisor.md)

## 出处

- ch3 §3 中心荷与相位；中译 p.63（英文 PDF p.68），源码 `chapters/ch03.tex:432`
