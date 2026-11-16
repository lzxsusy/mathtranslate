# 玻尔–索末菲量子化条件

> `geoq/concept/bohr-sommerfeld` · 轨道 B · 几何半经典量子化 · 状态 draft

> **先自测**：为什么拉格朗日子流形上刘维尔形式的限制一定闭？玻尔–索末菲条件在什么情形下自动满足、什么情形下又必须打补丁？

## 一句话

拉格朗日子流形上刘维尔形式的限制自动闭，却未必恰当；要求相位因子沿每个闭链单值，就得到 ∮λ 落在 2πℏ 整数倍上的玻尔–索末菲条件。

## 定义

仍取 $L\subset T^*X$ 为拉格朗日子流形，$\lambda=\sum_ip_i\,dx^i$。玻尔–索末菲条件要求：$L$ 的每个闭 1-链 $\gamma$ 都满足 $\frac{1}{2\pi\hbar}\oint_{\gamma}\lambda\in\mathbb Z$。它的等价说法是，积分 $e^{\frac{i}{\hbar}\int_{z_0}^{z}\lambda}$ 只与端点有关，因而可以在整个 $L$ 上无歧义地定义相位。

**记号约定**：$z_0\in L$ 是取定的参考点，$\int_{z_0}^{z}\lambda$ 沿 $L$ 内路径积分；$Z_1(L)$、$H_1(L)$ 分别记闭 1-链群与一维同调群；$\pi:L\to X$ 是余切丛投影，$\pi$ 的临界点集称焦散（caustics）。

## 要点

- $d(\lambda|_L)=(d\lambda)|_L=\omega|_L=0$：$L$ 各向同性使 $\lambda$ 的限制自动闭，这是整套构造能启动的原因。
- 闭而不恰当：$\oint_{\gamma}\lambda$ 是闭形式 $\lambda|_L$ 的周期，只依赖 $\gamma$ 的同调类，给出同态 $H_1(L)\to\mathbb R$。
- 量子化条件正是要求这些周期都落在 $2\pi\hbar\mathbb Z$ 里，也就是要求相位因子在 $L$ 上单值；否则只能说 $L$ 给出一个「差一个相位的截面」。
- 可投影情形 $L=L_{dS}$ 时 $\lambda|_L=dS$ 恰当，所有周期为零，条件自动成立，一个能级也定不出来；有界运动的离散谱要靠 $L$ 非单连通（典型情形 $L\cong S^1$）。
- 焦散是 $\pi$ 的临界点，不是 $L$ 的奇点；跨过焦散时半密度还要补马斯洛夫相位，条件升级为凯勒–马斯洛夫（EBK）条件。

## 关键公式

$$
$\lambda=\sum_ip_i\,dx^i$
$$

$$
$d(\lambda|_L)=\omega|_L=0$
$$

$$
$\frac{1}{2\pi\hbar}\oint_{\gamma}\lambda\in\mathbb Z,\qquad\forall\gamma\in Z_1(L)$
$$

$$
$\oint_{\gamma}\lambda=\int_{\Sigma}\omega,\qquad\partial\Sigma=\gamma$
$$

$$
$\frac{1}{2\pi\hbar}\oint_{\gamma}\lambda-\frac{1}{4}m(\gamma)\in\mathbb Z$
$$

## 定理与证明

### 命题（拉格朗日子流形上刘维尔形式的限制是闭的）

设 $L\subset(T^*X,\omega)$ 是拉格朗日子流形，$\lambda=\sum_ip_idx^i$（$d\lambda=\omega$）。则 $\lambda|_L$ 是闭 1-形式，其沿闭链的积分只依赖同调类；当 $L$ 单连通时 $\lambda|_L$ 恰当。

**完整证明**

1. 外微分与拉回可交换：$d(\lambda|_L)=(d\lambda)|_L=\omega|_L$。
   - *为什么*：这是 $d$ 的自然性，与 $\lambda$ 的具体取法无关；它把流形上的闭性判据直接搬到子流形上。
2. 由 $L$ 拉格朗日（$\dim L=n$ 且 $\omega$ 在 $TL$ 上为零）得 $\omega|_L=0$，于是 $d(\lambda|_L)=0$。
   - *为什么*：各向同性正是「辛形式在切空间上恒为零」；没有这一条，$\lambda|_L$ 一般并不闭。
3. 若 $\gamma=\partial\Sigma$ 是 $L$ 中的一条边界，则由 Stokes 公式 $\oint_{\gamma}\lambda=\int_{\Sigma}d\lambda=0$；故闭链上的积分在同调类上良定义。
   - *为什么*：闭形式沿边界的积分为零，于是两条同调路径的积分相等，多值性完全由 $H_1$ 决定。
4. $L$ 单连通时 $H_1(L)=0$，所有周期为零；由 de Rham 定理存在 $S\in C^\infty(L)$ 使 $\lambda|_L=dS$。
   - *为什么*：周期全为零等价于上同调类为零，这正是恰当性的判据。

来源：ch05a.tex:1086-1098（原书 p.269）

### 命题（玻尔–索末菲条件 = 相位因子单值）

设 $\lambda|_L$ 闭，$z_0\in L$。则 $e^{\frac{i}{\hbar}\int_{z_0}^{z}\lambda}$ 是 $L$ 上良定义的光滑函数，当且仅当对每条闭 1-链 $\gamma$ 有 $\frac{1}{2\pi\hbar}\oint_{\gamma}\lambda\in\mathbb Z$。

**完整证明**

1. 两条从 $z_0$ 到 $z$ 的路径 $\gamma_1,\gamma_2$ 拼成闭链 $\gamma=\gamma_1-\gamma_2$，故两次积分之差为 $\oint_{\gamma}\lambda$。
   - *为什么*：把路径差写成闭链，多值性就被完全归结为周期，这是唯一需要观察的一点。
2. 相位因子单值，当且仅当对每条这样的 $\gamma$ 都有 $e^{\frac{i}{\hbar}\oint_{\gamma}\lambda}=1$。
   - *为什么*：指数函数的核是 $2\pi i\mathbb Z$，所以「相位不变」就是一个整性条件。
3. 取对数得 $\frac{1}{\hbar}\oint_{\gamma}\lambda\in2\pi\mathbb Z$，除以 $2\pi$ 即 $\frac{1}{2\pi\hbar}\oint_{\gamma}\lambda\in\mathbb Z$。
   - *为什么*：除以 $2\pi$ 只是把条件写成整数，好与绕数、陈数对照。
4. 由定理一，$\lambda|_L$ 闭，所以只须在 $H_1(L)$ 的一组生成元上验证，不必检验每一条闭链。
   - *为什么*：周期是同态，验证生成元即可；实用上这也是唯一可行的查验方式。

来源：ch05a.tex:1090-1109（原书 p.269）

## 易错点

- 别漏 $2\pi$：条件是 $\oint_{\gamma}\lambda\in2\pi\hbar\mathbb Z$，不是 $\hbar\mathbb Z$；一维时即 $\oint p\,dx=2\pi\hbar n$，写错会让能级整体差一个 $2\pi$。
- 整性只对闭链成立。对开链（从 $z_0$ 到 $z$ 的路径）谈整数没有意义；$L$ 非紧时也只能对紧支闭链提条件。
- 别指望可投影情形由这个条件给出离散谱：$\lambda|_{L_{dS}}=dS$ 恰当时周期全为零，条件恒真。要得到离散谱，必须让 $L$ 有非平凡 $H_1$（如 $S^1$），并叠加马斯洛夫修正。

## 相关卡

- [马斯洛夫修正与 EBK 条件](../concepts/maslov-correction.md)
- [几何半经典定态](../concepts/geometric-semiclassical-state.md)
- [WKB 半经典解与哈密顿–雅可比方程](../concepts/wkb-approximation.md)
- [拉格朗日子流形、可投影与相函数](../concepts/lagrangian-submanifold.md)
- [余切丛的典范辛结构与刘维尔形式](../concepts/cotangent-bundle.md)
- [马斯洛夫指标与 $\mathcal L(V)$ 的基本群](../concepts/maslov-index.md)
- [谐振子的凯勒–马斯洛夫条件给出精确谱](../examples/oscillator-ebk-spectrum.md)

## 出处

- §5.2.3 焦散与玻尔–索末菲条件，p.268–269（PDF p.269–270），源码 `ch05a.tex:1024-1109`
