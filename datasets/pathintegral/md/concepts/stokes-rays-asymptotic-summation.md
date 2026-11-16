# 斯托克斯射线与渐近求和

> `pi/concept/stokes-rays-asymptotic-summation` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **先自测**：为什么艾里积分的渐近展开在 λ 平面某些射线上必须跳变，跳变又为何不改变首阶结果？

## 一句话

解析延拓艾里积分时，λ 平面虚轴上的两条射线让两条最速下降曲线相接；跨过射线时鞍点权重跳变，而首阶渐近保持不变。

## 定义

考虑含复参数 $\lambda$ 的艾里积分 $I(\lambda)=\int_C e^{i\lambda(z^3/3-z)}\,dz$，让 $\lambda\to+\infty\,e^{i\theta}$ 并同步形变围道 $C$。把 $C$ 拆成经过鞍点 $p_\pm=\pm1$ 的两条最速下降曲线：$C=n_-C_-^\lambda+n_+C_+^\lambda$。当 $\operatorname{Re}\lambda=0$ 时，两鞍点的 $\operatorname{Im}f$ 相等（$f=i\lambda(z^3/3-z)$），于是同一条下降曲线同时经过两个鞍点；$\lambda$ 平面中满足此条件的两条开射线称为斯托克斯射线（Stokes rays）。

**记号约定**：$z\in\mathbb{C}$；$p_\pm=\pm1$ 为 $f'(z)=0$ 的鞍点；$n_\pm$ 为围道分解系数；$\lambda$ 为渐近参数，$\theta=\arg\lambda$。

## 要点

- 斯托克斯射线由两鞍点的相位相等决定，即 $\operatorname{Im}f(p_-)=\operatorname{Im}f(p_+)$；对艾里积分这等价于 $\operatorname{Re}\lambda=0$。
- 在射线上，一条最速下降曲线把两个鞍点连起来，围道分解系数 $(n_-,n_+)$ 不再唯一；跨过射线时按 $n_-\mapsto n_-\pm n_+$ 跳变。
- 跳变只重新分配两条下降曲线的权重，主导项由指数大的那条给出，所以 $I(\lambda)$ 的首阶渐近连续。
- $\operatorname{Im}\lambda=0$（实轴）是反斯托克斯射线：两侧分别由 $C_+^\lambda$ 与 $C_-^\lambda$ 主导，主导项在此互换。
- 最速下降给出的是渐近级数而非收敛级数；书中所谓「渐近求和」是把各鞍点的贡献相加，并未使用 Borel 重求和。

## 关键公式

$$
I(\lambda)=\int_C e^{i\lambda\left(\frac{z^3}{3}-z\right)}\,dz
$$

$$
f(z)=i\lambda\left(\frac{z^3}{3}-z\right),\qquad f(p_+)=-\frac{2}{3}i\lambda,\quad f(p_-)=\frac{2}{3}i\lambda
$$

$$
\operatorname{Im}f(p_+)=-\frac{2}{3}\operatorname{Re}\lambda,\qquad \operatorname{Im}f(p_-)=\frac{2}{3}\operatorname{Re}\lambda
$$

$$
C=n_-C_-^\lambda+n_+C_+^\lambda,\qquad n_+\mapsto n_+,\quad n_-\mapsto n_-\pm n_+
$$

$$
I(\lambda)\simeq n_-\sqrt{\frac{\pi}{i\lambda}}\,e^{\frac{2}{3}i\lambda}+n_+\sqrt{\frac{\pi}{-i\lambda}}\,e^{-\frac{2}{3}i\lambda}
$$

## 定理与证明

### 斯托克斯射线是两鞍点的等相位线

对 $f(z)=i\lambda(z^3/3-z)$，两条最速下降曲线 $C_\pm^\lambda$ 的 $\operatorname{Im}f$ 相等当且仅当 $\operatorname{Re}\lambda=0$（$\lambda\ne0$）。因此斯托克斯射线是 $\lambda$ 平面虚轴的两条开射线。

**完整证明**

1. 代入 $z=\pm1$ 算出 $f(p_\pm)=\mp\frac{2}{3}i\lambda$。
   - *为什么*：鞍点由 $f'(z)=i\lambda(z^2-1)=0$ 定出，再合并同类项。
2. 取虚部得 $\operatorname{Im}f(p_\pm)=\mp\frac{2}{3}\operatorname{Re}\lambda$，故两者相等当且仅当 $\operatorname{Re}\lambda=0$。
   - *为什么*：$\operatorname{Im}(\pm i\lambda)=\pm\operatorname{Re}\lambda$，两支相差一个符号。
3. 最速下降曲线是 $\operatorname{Im}f$ 的等值线；等相位时过 $p_-$ 与 $p_+$ 的等值线重合，于是一条曲线连接两个鞍点。
   - *为什么*：这正是射线上围道拓扑改变、分解系数不再唯一的原因。

来源：ch02a.tex:1309-1357（原书 p.104–106）

### 跨射线的权重跳变不改变首阶

在 $\operatorname{Im}\lambda>0$ 的一侧 $C_+^\lambda$ 主导。跨过 $\lambda\in i\mathbb{R}_{>0}$ 时 $C_+^\lambda\mapsto C_+^\lambda\pm C_-^\lambda$，等价于 $n_-\mapsto n_-\pm n_+$；由于 $C_-$ 的贡献小一个指数因子，$I(\lambda)$ 的首阶不变。另一条射线情形对称。

**完整证明**

1. 跨射线时 $C_+^\lambda$ 连续形变为 $C_+^\lambda\pm C_-^\lambda$。
   - *为什么*：射线上两条曲线相接，可把 $C_-$ 的一段并入 $C_+$ 而不改变端点与下降性质。
2. 代入 $C=n_-C_-^\lambda+n_+C_+^\lambda$ 得 $C=(n_-\pm n_+)C_-^\lambda+n_+C_+^\lambda$，故 $n_-\mapsto n_-\pm n_+$。
   - *为什么*：要保持同一条 $C$ 的分解，系数必须吸收这个变化。
3. 两条贡献的模之比为 $e^{\operatorname{Re}f(p_-)-\operatorname{Re}f(p_+)}=e^{-\frac{4}{3}\operatorname{Im}\lambda}$，沿 $\lambda\to\infty\,e^{i\theta}$ 在射线上为指数小。
   - *为什么*：首阶只由指数大的项决定，改动小项的系数不影响首阶。

来源：ch02a.tex:1378-1409（原书 p.106–107）

### 反斯托克斯射线与主导项切换

当 $\operatorname{Im}\lambda>0$ 时 $C_+^\lambda$ 的贡献主导，当 $\operatorname{Im}\lambda<0$ 时 $C_-^\lambda$ 主导；实轴 $\operatorname{Im}\lambda=0$ 称为反斯托克斯射线（anti-Stokes ray），主导项在其两侧互换。

**完整证明**

1. 由 $f(p_+)=-\frac{2}{3}i\lambda$ 得 $\operatorname{Re}f(p_+)=\frac{2}{3}\operatorname{Im}\lambda$，而 $\operatorname{Re}f(p_-)=-\frac{2}{3}\operatorname{Im}\lambda$。
   - *为什么*：写 $\lambda=a+ib$，则 $i\lambda=-b+ia$，取实部即得。
2. 每条下降曲线的贡献随 $e^{\operatorname{Re}f(p_\pm)}$ 变化，故 $\operatorname{Im}\lambda>0$ 时 $C_+$ 的指数大，$\operatorname{Im}\lambda<0$ 时 $C_-$ 的指数大。
   - *为什么*：比较两个实部即可判断哪一项在 $|\lambda|\to\infty$ 时占优。
3. $\operatorname{Im}\lambda=0$ 时两实部相等，主导地位在此交换，这条线就是反斯托克斯射线。
   - *为什么*：主导项切换的 locus 正是反斯托克斯射线的定义。

来源：ch02a.tex:1432-1449（原书 p.107）

## 易错点

- 斯托克斯射线在 $\lambda$ 平面（虚轴）上，不是 $z$ 平面里的最速下降曲线；两者不要混。
- 在射线上分解系数不唯一；跨越时的跳变是 $(n_-,n_+)$ 的重新选取，不是 $I(\lambda)$ 本身不连续。
- 跳变方向依赖跨越方向：$n_-\mapsto n_-\pm n_+$ 的符号要由 $C_+^\lambda$ 的具体变形定，不能一律取加号。
- 本节只给首阶 $O(1/\lambda)$；把 $\simeq$ 当成收敛展开、或直接把 Borel 重求和搬来，都越出底本范围。
- 反斯托克斯射线（$\operatorname{Im}\lambda=0$）处是主导项互换，不是权重跳变；两条射线的角色不同。

## 相关卡

- [斯托克斯现象与艾里函数](../concepts/stokes-phenomenon.md)
- [最速下降法](../concepts/steepest-descent.md)
- [莫尔斯流与最速下降曲线](../concepts/morse-flow.md)
- [半经典费曼核](../concepts/semiclassical-kernel.md)

## 出处

- §2.5.6 斯托克斯射线、§2.5.7 渐近求和，p.104–107（PDF p.105–108），源码 `ch02a.tex:1297-1466`
