# 有限维高斯积分

> `pi/concept/gaussian-integral` · 轨道 B · 高斯路径积分与谐振子 · 状态 draft

> **先自测**：为什么 $n$ 维高斯积分的值只依赖 $\det A$，带源项时又多出什么因子？

## 一句话

把 $n$ 维二次型高斯积分化为 $n$ 个一维积分之积，得到命题 2.3.1 的无源项与带源项公式；纯虚系数情形由解析延拓给出，整体相位由惯性指数决定。

## 定义

设 $A$ 是 $n$ 阶实对称正定矩阵，则 $\exp(-\mathbf{x}^{\mathrm{t}}A\mathbf{x})$ 在 $\mathbb{R}^n$ 上的积分等于 $\pi^{n/2}(\det A)^{-1/2}$。若指数中再加线性型 $\mathbf{J}^{\mathrm{t}}\cdot\mathbf{x}$，配方平移后只多出因子 $\exp(\mathbf{J}^{\mathrm{t}}A^{-1}\mathbf{J}/4)$。系数取纯虚数时同一等式按解析延拓理解，结果带上由正、负本征值个数之差决定的相位。

**记号约定**：$A$ 为 $n$ 阶实对称正定矩阵；$\Lambda$ 为实对称矩阵，$n_+$、$n_-$ 分别是它的正、负本征值个数；$\mathbf{J}\in\mathbb{R}^n$。

## 要点

- 证明的关键是对称矩阵的正交对角化：二次型化为平方和，积分随之拆成 $n$ 个一维高斯积分。
- 线性项靠配方吸收：平移 $\mathbf{x}\to\mathbf{x}-\frac12A^{-1}\mathbf{J}$ 不改变 $\mathbb{R}^n$ 上的测度，余下的常数即 $\frac14\mathbf{J}^{\mathrm{t}}A^{-1}\mathbf{J}$。
- 正定性是收敛的前提；$A$ 不正定时只能借 $i\epsilon$ 或复围道给积分一个定义。
- 纯虚系数情形由解析延拓得到，$\sqrt{\det(-i\Lambda)}$ 的分支决定整体相位 $e^{i\pi(n_+-n_-)/4}$。
- 这个有限维公式是路径积分的零件：每条时间切片都贡献一个同型的高斯因子，$N\to\infty$ 时再谈极限。

## 关键公式

$$
\int_{\mathbb{R}^n}\mathrm{d}^n\mathbf{x}\,e^{-\mathbf{x}^{\mathrm{t}}A\mathbf{x}}=\frac{\pi^{n/2}}{\sqrt{\det A}}
$$

$$
\int_{\mathbb{R}^n}\mathrm{d}^n\mathbf{x}\,e^{-\mathbf{x}^{\mathrm{t}}A\mathbf{x}+\mathbf{J}^{\mathrm{t}}\cdot\mathbf{x}}=\frac{\pi^{n/2}}{\sqrt{\det A}}\,e^{\frac14\mathbf{J}^{\mathrm{t}}A^{-1}\mathbf{J}}
$$

$$
\int_{\mathbb{R}}\mathrm{d}x\,e^{-ax^2}=\sqrt{\frac{\pi}{a}},\qquad a>0
$$

$$
\int_{\mathbb{R}}\mathrm{d}x\,e^{i\lambda x^2}=e^{\frac{i\pi}{4}\operatorname{sgn}\lambda}\,\sqrt{\frac{\pi}{|\lambda|}}
$$

$$
\int_{\mathbb{R}^n}\mathrm{d}^n\mathbf{x}\,e^{i\mathbf{x}^{\mathrm{t}}\Lambda\mathbf{x}}=e^{\frac{i\pi}{4}(n_+-n_-)}\,\frac{\pi^{n/2}}{\sqrt{|\det\Lambda|}}
$$

## 定理与证明

### 命题 2.3.1（无源项）

设 $A$ 为 $n$ 阶实对称正定矩阵，则 $\int_{\mathbb{R}^n}\mathrm{d}^n\mathbf{x}\,e^{-\mathbf{x}^{\mathrm{t}}A\mathbf{x}}=\dfrac{\pi^{n/2}}{\sqrt{\det A}}$。

**完整证明**

1. 写出正交对角化 $A=P\operatorname{diag}(\lambda_1,\dots,\lambda_n)P^{-1}$，其中 $P\in SO(n)$，$\lambda_i>0$。
   - *为什么*：实对称矩阵可由正交矩阵对角化；正定性等价于所有 $\lambda_i>0$，从而每个一维积分都收敛。
2. 作变量替换 $\mathbf{x}=P\mathbf{y}$。
   - *为什么*：正交变换的行列式为 $1$，故 $\mathrm{d}^n\mathbf{x}=\mathrm{d}^n\mathbf{y}$，测度不变。
3. 二次型化为 $\sum_{i=1}^n\lambda_iy_i^2$，积分拆成 $\prod_{i=1}^n\int_{\mathbb{R}}e^{-\lambda_iy_i^2}\mathrm{d}y_i$。
   - *为什么*：被积函数成为各分量函数的乘积，富比尼定理允许逐次积分。
4. 每个因子为 $\sqrt{\pi/\lambda_i}$，相乘得 $\pi^{n/2}/\sqrt{\lambda_1\cdots\lambda_n}=\pi^{n/2}/\sqrt{\det A}$。
   - *为什么*：$\det A=\prod_i\lambda_i$ 在正交相似下不变，故右端只依赖 $A$ 的行列式。

来源：ch02a.tex:501-542（原书 p.89）

### 命题 2.3.1（带源项）

在同样的 $A$ 下，$\int_{\mathbb{R}^n}\mathrm{d}^n\mathbf{x}\,e^{-\mathbf{x}^{\mathrm{t}}A\mathbf{x}+\mathbf{J}^{\mathrm{t}}\cdot\mathbf{x}}=\dfrac{\pi^{n/2}}{\sqrt{\det A}}\,e^{\frac14\mathbf{J}^{\mathrm{t}}A^{-1}\mathbf{J}}$。

**证明提纲**

1. 把指数配方成 $-\left(\mathbf{x}-\frac12A^{-1}\mathbf{J}\right)^{\mathrm{t}}A\left(\mathbf{x}-\frac12A^{-1}\mathbf{J}\right)+\frac14\mathbf{J}^{\mathrm{t}}A^{-1}\mathbf{J}$。
   - *为什么*：这样二次型部分仍是正定的，积分回到无源项的情形。
2. 平移 $\mathbf{y}=\mathbf{x}-\frac12A^{-1}\mathbf{J}$，把线性型消掉。
   - *为什么*：平移的雅可比为 $1$，全空间上的积分值不变，只剩一个与 $\mathbf{x}$ 无关的常数因子。

> **缺口**：书中只用「由配方可得」一句带过，没有写出配方时交叉项如何抵消、平移下测度为何不变，以及系数 $1/4$ 的来源；以上两步是按标准做法补的思路，原书未展开。


来源：ch02a.tex:508-514（原书 p.89）

### 注 2.3.2（虚相位与惯性指数）

取 $A=-i\Lambda$、$\Lambda$ 实对称，解析延拓给出 $\int_{\mathbb{R}^n}\mathrm{d}^n\mathbf{x}\,e^{i\mathbf{x}^{\mathrm{t}}\Lambda\mathbf{x}}=e^{\frac{i\pi}{4}(n_+-n_-)}\dfrac{\pi^{n/2}}{\sqrt{|\det\Lambda|}}$，其中 $n_+$、$n_-$ 是 $\Lambda$ 的正、负本征值个数。

**证明提纲**

1. 从 $a>0$ 的 $\sqrt{\pi/a}$ 出发，令 $a=-i\lambda$，沿下半平面把积分路径的端点转过去。
   - *为什么*：$e^{-az^2}$ 是整函数，只要在扇形边界上一致衰减，围道变形不改变积分值。
2. 多维情形按本征方向逐个作延拓，每个正本征值贡献 $e^{i\pi/4}$，每个负本征值贡献 $e^{-i\pi/4}$。
   - *为什么*：对角化后积分分解为各方向的乘积，相位因子相乘即按 $n_+-n_-$ 相加。

> **缺口**：书中直接写出延拓后的等式，没有说明 $\sqrt{\det(-i\Lambda)}$ 取哪一支，也没有给出围道旋转的合法性论证（扇形边界上的衰减估计）；这里只补了思路。


来源：ch02a.tex:544-553（原书 p.89）

## 易错点

- $\det A$ 位于分母的平方根内，写成 $\pi^{n/2}/\det A$ 会漏掉 $1/2$ 次幂。
- 源项的指数系数是 $1/4$：配方时平移量带 $\frac12$，平方后正好给出 $\frac14\mathbf{J}^{\mathrm{t}}A^{-1}\mathbf{J}$。
- $\lambda<0$ 时指数里的 $\operatorname{sgn}\lambda=-1$，相位是 $e^{-i\pi/4}$；不能把 $\operatorname{sgn}\lambda$ 提到指数外当整体符号。
- 缺少正定性时积分按普通意义发散，解析延拓给出的是正则化值，不能当作勒贝格积分使用。
- 只有对称部分进入二次型，讨论 $\det$ 前须先把矩阵对称化。

## 相关卡

- [zeta 函数正则化与泛函行列式](../concepts/zeta-regularization.md)
- [时间切片与复合律](../concepts/time-slicing.md)
- [谐振子传播子（Mehler 核）](../concepts/harmonic-oscillator-propagator.md)

## 出处

- §2.3.1 高斯积分，p.89–90（PDF p.90–91），源码 `ch02a.tex:485-555`
