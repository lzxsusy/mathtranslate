# 斯托克斯现象与艾里函数

> `pi/concept/stokes-phenomenon` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **先自测**：为什么艾里积分的渐近式是两项之和，而跨过斯托克斯射线时系数会跳变？

## 一句话

有多个鞍点时渐近式是各项之和；参数跨过某些射线时某一项的系数会离散跳变。艾里积分的两个鞍点 $\pm1$ 给出 $e^{\pm\frac{2}{3}\mathrm{i}\lambda}$ 两项。

## 定义

当一个含大参数的积分有多个非退化鞍点时，固定射线的首阶渐近是各鞍点贡献之和，每一项的系数由围道如何分解成最速下降曲线决定。让参数 $\lambda$ 在复平面上连续转动，只要不穿过某些特殊射线，这些系数保持不变；一旦穿过，两条最速下降曲线会接成同一条、围道的分解随之改变，系数发生整数跳变。这就是斯托克斯现象，那些射线称为斯托克斯射线（或斯托克斯线）。艾里积分是最简单的演示：两个鞍点 $z=\pm1$ 各给一项，指数因子为 $e^{\pm\frac{2}{3}\mathrm{i}\lambda}$。

**记号约定**：$f(z)=\mathrm{i}\lambda\left(\frac{z^3}{3}-z\right)$（$\lambda$ 已含在 $f$ 内，故局部高斯因子是 $\sqrt{2\pi/(-f'')}$）；$p_\pm=\pm1$；$C_\pm$ 为过 $p_\pm$ 的最速下降围道；$n_\pm\in\mathbb{Z}$。

## 要点

- 艾里积分 $I(\lambda)=\int_{\mathbb{R}}e^{\mathrm{i}\lambda(z^3/3-z)}\mathrm{d}z$ 可化为 $2\pi\lambda^{-1/3}\operatorname{Ai}(-\lambda^{2/3})$，是研究斯托克斯现象的标准模型。
- 相位 $z^3/3-z$ 的驻点 $z=\pm1$ 给出两个鞍点，$f(p_\pm)=\mp\frac{2}{3}\mathrm{i}\lambda$，两支贡献的指数因子互为复共轭。
- 每个鞍点对应一条最速下降围道 $C_\pm$；实轴围道在 $\lambda>0$ 时可分解为 $C_-+C_+$，故渐近式是两项之和。
- 两支的相对权重随 $\operatorname{Arg}\lambda$ 改变；在 $\operatorname{Re}\lambda=0$ 上 $\operatorname{Im}f(p_+)=\operatorname{Im}f(p_-)$，一条下降曲线连接两个鞍点，系数在此跳变。
- 斯托克斯射线与反斯托克斯射线不同：前者是 $\operatorname{Im}f$ 的等值条件（围道连通、系数跳变），后者是 $\operatorname{Re}f$ 的等值条件（哪一项占主导）。

## 关键公式

$$
I(\lambda)=\int_{-\infty}^{+\infty}e^{\mathrm{i}\lambda\left(\frac{z^3}{3}-z\right)}\mathrm{d}z=2\pi\lambda^{-1/3}\operatorname{Ai}\left(-\lambda^{2/3}\right)
$$

$$
f'(z)=0\iff z=p_\pm=\pm1,\qquad f(p_\pm)=\mp\dfrac{2}{3}\mathrm{i}\lambda,\qquad f''(p_\pm)=\pm2\mathrm{i}\lambda
$$

$$
I(\lambda)\simeq\sqrt{\dfrac{\pi}{\mathrm{i}\lambda}}\,e^{\frac{2}{3}\mathrm{i}\lambda}+\sqrt{\dfrac{\pi}{-\mathrm{i}\lambda}}\,e^{-\frac{2}{3}\mathrm{i}\lambda},\qquad \lambda\to+\infty
$$

$$
\operatorname{Ai}(-x)\sim\dfrac{1}{\sqrt{\pi}}\,x^{-1/4}\sin\left(\dfrac{2}{3}x^{3/2}+\dfrac{\pi}{4}\right),\qquad x\to+\infty
$$

## 定理与证明

### 艾里积分的双鞍点渐近

当 $\lambda\to+\infty$ 沿正实轴时，$I(\lambda)=\int_{\mathbb{R}}e^{\mathrm{i}\lambda(z^3/3-z)}\mathrm{d}z\simeq\sqrt{\pi/(\mathrm{i}\lambda)}\,e^{\frac{2}{3}\mathrm{i}\lambda}+\sqrt{\pi/(-\mathrm{i}\lambda)}\,e^{-\frac{2}{3}\mathrm{i}\lambda}$。

**完整证明**

1. 求鞍点：$f'(z)=\mathrm{i}\lambda(z^2-1)=0$ 给出 $p_\pm=\pm1$；$f''(p_\pm)=\pm2\mathrm{i}\lambda\ne0$，均为非退化。
   - *为什么*：最速下降的首阶只依赖非退化临界点。
2. 计算 $f(p_+)=-\frac{2}{3}\mathrm{i}\lambda$、$f(p_-)=+\frac{2}{3}\mathrm{i}\lambda$；两条最速下降围道 $C_\pm$ 满足 $\operatorname{Im}f=\operatorname{Im}f(p_\pm)$，两端 $\operatorname{Re}f\to-\infty$。
   - *为什么*：对 $\int e^{f}\mathrm{d}z$，衰减要求 $\operatorname{Re}f\to-\infty$，故每条围道只经过自己的鞍点。
3. 把实轴围道形变为 $C_-+C_+$（$\lambda>0$ 时两条曲线不相交），$I=\int_{C_-}e^f\mathrm{d}z+\int_{C_+}e^f\mathrm{d}z$。
   - *为什么*：被积函数整函数，两端贡献消失，柯西定理允许这种形变。
4. 在每个鞍点用高斯近似 $\int_{C_\pm}e^f\mathrm{d}z\simeq e^{f(p_\pm)}\sqrt{2\pi/(-f''(p_\pm))}$，得两项 $\sqrt{\pi/(\mathrm{i}\lambda)}\,e^{\frac{2}{3}\mathrm{i}\lambda}$ 与 $\sqrt{\pi/(-\mathrm{i}\lambda)}\,e^{-\frac{2}{3}\mathrm{i}\lambda}$。
   - *为什么*：$\sqrt{2\pi/(\mp2\mathrm{i}\lambda)}$ 分别化简为 $\sqrt{\pi/(\mp\mathrm{i}\lambda)}$；误差为 $O(1/\lambda)$。

来源：ch02a.tex:1218-1295（原书 p.102–104）

### 跨射线的系数跳变

当 $\lambda$ 跨过 $\operatorname{Re}\lambda=0$ 的射线时，$\operatorname{Im}f(p_+)=\operatorname{Im}f(p_-)$，$C_+$ 与 $C_-$ 接成一条经过两个鞍点的下降曲线；围道分解 $C=n_-C_-+n_+C_+$ 的整系数发生跳变 $n_-\mapsto n_-\pm n_+$（对称地也可改 $n_+$），而各项的解析形式不变。

**证明提纲**

1. 在 $\operatorname{Re}\lambda=0$ 上，$\operatorname{Im}f(p_\pm)=0$ 相等，故同一水平集同时经过 $p_+$ 与 $p_-$。
   - *为什么*：水平集由 $\operatorname{Im}f$ 的值标记，值相等时两条曲线接上。
2. 跨射线时 $C_\pm^\lambda$ 连续变形，但围道在鞍点附近的连通方式改变，分解系数只能取整数以保持 $C$ 的连续性。
   - *为什么*：整系数来自围道的拓扑分解，连续性只允许离散跳变。

> **缺口**：书中只以图形说明跨射线时 $C_\pm^\lambda$ 的变换与系数跳跃，未给出跳跃量的解析证明，也未引入斯托克斯乘子与连接公式；本卡只陈述规则，完整证明需 §2.7 的连接公式。


来源：ch02a.tex:1341-1357、1386-1409（原书 p.105–107）

## 易错点

- 只取指数大的那个鞍点：跨斯托克斯射线时次项虽指数小，却必须一并保留才能保持连续；两项模同阶（$\operatorname{Re}f$ 相等）的是反斯托克斯射线，那里丢掉次项会直接算错。
- 把斯托克斯射线与反斯托克斯射线混为一谈：前者判据是 $\operatorname{Im}f$ 相等（围道连通、系数跳变），后者是 $\operatorname{Re}f$ 相等（主导项交换）。
- 书中写 $f(p_\pm)=\pm\frac{2}{3}\mathrm{i}\lambda$，与 $p_\pm=\pm1$ 的下标约定相反；照抄会在配对指数与平方根时出错。
- 跨射线时变的是系数 $n_\pm$，不是每一项的解析表达式；不要把跳变误当成某项数值发散。
- $C_\pm$ 的选择依赖 $\lambda$ 的辐角；固定一条实轴围道而不随 $\lambda$ 变形，会在 $\operatorname{Re}\lambda<0$ 时得到发散的积分。

## 相关卡

- [最速下降法](../concepts/steepest-descent.md)
- [莫尔斯流与最速下降曲线](../concepts/morse-flow.md)
- [斯托克斯射线与渐近求和](../concepts/stokes-rays-asymptotic-summation.md)

## 出处

- §2.5.4 斯托克斯现象（艾里积分），p.102–104（PDF p.103–105），源码 `ch02a.tex:1212-1296`
- §2.5.4 斯托克斯射线（小节），p.105（PDF p.106），源码 `ch02a.tex:1341-1357`
- §2.5.4 跨射线的系数跳变，p.107（PDF p.108），源码 `ch02a.tex:1403-1409`
