# $\int_C e^{\mathrm{i}z^2}\,\mathrm{d}z$ 的围道计算

> `pi/example/fresnel-integral` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **这张卡练什么**：怎样用围道形变把 $\int_C e^{\mathrm{i}z^2}\mathrm{d}z$ 化成标准高斯积分？

## 一句话

把 $\int_{\mathbb{R}}e^{-\lambda x^2}\mathrm{d}x$ 解析延拓到 $\lambda=-\mathrm{i}$，用旋转 $45^\circ$ 的围道把振荡积分化为高斯积分，得 $e^{\mathrm{i}\pi/4}\sqrt{\pi}$。

## 设定

设 $I(\lambda)=\int_{C_\theta}e^{-\lambda z^2}\mathrm{d}z$，其中 $C_\theta$ 是过原点、与实轴成角 $\theta$ 的直线。已知 $\lambda>0$ 时 $I(\lambda)=\sqrt{\pi/\lambda}$。要把这个结果延拓到 $\lambda=-\mathrm{i}$，需选一条使积分收敛的 $C_\theta$，算出 $\int_C e^{\mathrm{i}z^2}\mathrm{d}z$，再与实轴上的菲涅耳积分对照。

## 计算

**第 1 步**：出发点：$\lambda>0$ 时沿实轴 $I(\lambda)=\int_{\mathbb{R}}e^{-\lambda x^2}\mathrm{d}x=\sqrt{\pi/\lambda}$。

> 为什么：这是标准高斯积分，后面的延拓都以它为基准。

**第 2 步**：沿 $z=re^{\mathrm{i}\theta}$ 有 $-\lambda z^2=-|\lambda|r^2e^{\mathrm{i}(\varphi+2\theta)}$（$\lambda=|\lambda|e^{\mathrm{i}\varphi}$）；先设 $\operatorname{Re}\lambda>0$，取 $\theta\in(0,\pi/4)$ 使 $\cos(\varphi+2\theta)>0$。

> 为什么：指数实部为负保证 $C_\theta$ 上的积分绝对收敛。

**第 3 步**：此时围道可自由转动：$e^{-\lambda z^2}$ 在扇形内解析，大弧上 $\cos(\varphi+2\alpha)$ 有一致正下界、弧贡献趋于零，故 $I(\lambda)$ 与 $\theta$ 无关，且对 $\operatorname{Re}\lambda>0$ 有 $I(\lambda)=\sqrt{\pi/\lambda}$。

> 为什么：柯西定理加大弧上的一致衰减，围道才能自由旋转。

**第 4 步**：两边都是 $\lambda$ 的解析函数，按解析延拓可取 $\lambda=-\mathrm{i}$：$I(-\mathrm{i})=\int_{C_{\pi/4}}e^{\mathrm{i}z^2}\mathrm{d}z$，沿该线 $|e^{\mathrm{i}z^2}|=e^{-t^2}$，积分绝对收敛。

> 为什么：解析延拓把 $\operatorname{Re}\lambda>0$ 的公式送到虚轴；$\lambda=-\mathrm{i}$ 时被积函数模为 $e^{-t^2}$。

**第 5 步**：令 $z=e^{\mathrm{i}\pi/4}u$（$u\in\mathbb{R}$），则 $z^2=\mathrm{i}u^2$、$\mathrm{i}z^2=-u^2$、$\mathrm{d}z=e^{\mathrm{i}\pi/4}\mathrm{d}u$。

> 为什么：旋转 $45^\circ$ 正是把 $\mathrm{i}z^2$ 变成 $-u^2$ 的那个变换。

**第 6 步**：代入得 $I(-\mathrm{i})=e^{\mathrm{i}\pi/4}\int_{\mathbb{R}}e^{-u^2}\mathrm{d}u=e^{\mathrm{i}\pi/4}\sqrt{\pi}$；反向旋转同理给出 $\int_{C_{-\pi/4}}e^{-\mathrm{i}z^2}\mathrm{d}z=e^{-\mathrm{i}\pi/4}\sqrt{\pi}$。

> 为什么：高斯积分 $\int_{\mathbb{R}}e^{-u^2}\mathrm{d}u=\sqrt{\pi}$，常数因子全部来自 $\mathrm{d}z$。

## 结果

$\int_{C_{\pi/4}}e^{\mathrm{i}z^2}\mathrm{d}z=e^{\mathrm{i}\pi/4}\sqrt{\pi}$，$\int_{C_{-\pi/4}}e^{-\mathrm{i}z^2}\mathrm{d}z=e^{-\mathrm{i}\pi/4}\sqrt{\pi}$；$C_{\pm\pi/4}$ 均取从 $-\infty$ 到 $+\infty$ 的定向。

## 复核

与实轴上的菲涅耳积分对照：$\int_{\mathbb{R}}\cos x^2\,\mathrm{d}x=\int_{\mathbb{R}}\sin x^2\,\mathrm{d}x=\sqrt{\pi/2}$，故 $\int_{\mathbb{R}}e^{\mathrm{i}x^2}\mathrm{d}x=(1+\mathrm{i})\sqrt{\pi/2}=e^{\mathrm{i}\pi/4}\sqrt{\pi}$；也可对 $I(\lambda)=\sqrt{\pi/\lambda}$ 求导验证 $I'=-I/(2\lambda)$，再代 $\lambda=-\mathrm{i}$。

## 易错点

- 旋转方向别弄反：算 $e^{\mathrm{i}z^2}$ 要用 $z=e^{\mathrm{i}\pi/4}u$；用 $e^{-\mathrm{i}\pi/4}$ 会把指数变成 $+u^2$ 而发散。
- 实轴上的 $\int e^{\mathrm{i}x^2}\mathrm{d}x$ 只是条件收敛，形变围道前必须说明两端大弧贡献消失。
- $\sqrt{\pi/(-\mathrm{i})}$ 的分支：$1/(-\mathrm{i})=\mathrm{i}$，故结果是 $e^{\mathrm{i}\pi/4}\sqrt{\pi}$；若写成 $\sqrt{\pi}\sqrt{-\mathrm{i}}$ 就取错了分支。
- 定向：$C_{\pi/4}$ 反向时结果整体变号，写答案时要交代定向。

## 用到哪些概念

- [最速下降法](../concepts/steepest-descent.md)

## 相关卡

- [高斯积分 $\int_C e^{\mathrm{i}\lambda z^2}\mathrm{d}z$ 的最速下降围道](../examples/steepest-descent-gaussian.md)

## 出处

- §2.5.2 最速下降法（例 2.5.2），p.98–99（PDF p.99–100），源码 `ch02a.tex:1029-1072`
