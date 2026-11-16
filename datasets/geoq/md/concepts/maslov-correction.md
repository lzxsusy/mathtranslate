# 马斯洛夫修正与 EBK 条件

> `geoq/concept/maslov-correction` · 轨道 B · 几何半经典量子化 · 状态 draft

> **先自测**：马斯洛夫修正为什么恰好是 m/4 而不是 m/2？它究竟从半密度的哪一个指数上冒出来？

## 一句话

半密度只能取到四分相位，沿闭链绕一圈多出 e^{−iπm/2}；把这份马斯洛夫相位并入玻尔–索末菲条件，得到 (1/2πℏ)∮λ−m/4∈ℤ 的凯勒–马斯洛夫（EBK）规则。

## 定义

设 $L\subset T^*\mathbb R^n$ 可定向，$\mathcal L(\mathbb R^{2n})\cong U(n)/O(n)$ 是拉格朗日格拉斯曼流形。映射 $\det^2$ 从 $\mathcal L$ 打到 $S^1$，并给出 $\pi_1\cong\mathbb Z$。对环路 $\gamma:S^1\to\mathcal L(\mathbb R^{2n})$，$\det^2\circ\gamma$ 的绕数定义为马斯洛夫指标 $m(\gamma)$。把每个 $T_zL$ 视为 $\mathcal L$ 中的点，则 $L$ 上非零半密度的相位可写成 $\Theta^{1/4}$；绕 $\gamma$ 一周后相位乘以 $e^{-\frac{i}{4}2\pi m(\gamma)}$，这一额外因子就是马斯洛夫修正。把它吸收进量子化条件，得到凯勒–马斯洛夫（EBK）条件 $\frac{1}{2\pi\hbar}\oint_{\gamma}\lambda-\frac14m(\gamma)\in\mathbb Z$。

**记号约定**：$\Theta=\varphi/|\varphi|$，$\varphi:(\Lambda^nT^*L)^2-\{0\}\to\mathbb C^*$ 为 2-密度的比较映射；$\Omega^4$ 是 2-密度（半密度指数 $\frac12\times4=2$）；$m(\gamma)$ 为 $\det^2\circ\gamma$ 的绕数，约定使一维谐振子绕行一圈给 $m=2$。

## 要点

- 构造顺序：$T_zL$ 给格拉斯曼流形一个点，$\det^2$ 把它送到 $S^1$，绕数再给出整数 $m$。马斯洛夫指标是纯拓扑量，只依赖环路，与 $\Omega$、$S$ 的具体取法无关。
- 四分之一来自指数链：半密度 $\to$ 四次方得 2-密度 $\to$ 与参考 2-密度比较（$\varphi$ 含 $\det^2$，相位是 $2\theta$）$\to$ 再开四次方。每走一步都在分母上留下一个因子。
- 沿一圈的相位亏损是 $\frac{2\pi m}{4}=\frac{\pi m}{2}$：每穿过一个焦散（$m$ 增 $1$）相位少 $\frac\pi2$，这正是 WKB 在转折点的标准相移。
- 把相函数相位 $\frac1\hbar\oint\lambda$ 与马斯洛夫相位合起来要求总相位为 $2\pi$ 的整数倍，就得到 EBK 条件；$m\equiv0$（无焦散）时它退回玻尔–索末菲条件。
- 谐振子的一圈有左右两个焦散，$m=2$，修正项为 $\frac12$，条件变成 $\frac{E}{\hbar\omega}-\frac12\in\mathbb Z$，恰好给出 $E_n=\hbar\omega(n+\frac12)$。
- 马斯洛夫修正不是对经典力学的修正，而是半经典波在 $L$ 上整体拼接的拓扑条件：它不改变 $L$ 与 $\Omega$，只改变允许的量子化常数。

## 关键公式

$$
$\det{}^2(L_0)=\left[\frac{c_1\wedge_{\mathbb C}\cdots\wedge_{\mathbb C}c_n}{e_1\wedge_{\mathbb C}\cdots\wedge_{\mathbb C}e_n}\right]^2\in S^1$
$$

$$
$\varphi(\Omega^4)^{1/4}=\Theta^{1/4}\left|\varphi(\Omega^4)\right|^{1/4}$
$$

$$
$\Theta^{1/4}\longmapsto e^{-\frac{i}{4}\left(2\pi m(\gamma)\right)}\,\Theta^{1/4}$
$$

$$
$\frac{1}{2\pi\hbar}\oint_{\gamma}\lambda-\frac14m(\gamma)\in\mathbb Z$
$$

$$
$e^{\frac{i}{\hbar}\oint_{\gamma}\lambda-\frac{i}{4}2\pi m(\gamma)}=1$
$$

## 定理与证明

### 命题（半密度沿闭链的相位亏损为 $\pi m/2$）

设 $L$ 可定向，$\Omega$ 为 $L$ 上非零半密度，$\gamma$ 是 $L$ 中的闭路。把 $\Omega$ 参数化为 $\Theta^{1/4}|\varphi(\Omega^4)|^{1/4}$。则绕 $\gamma$ 一周后 $\Theta^{1/4}\mapsto e^{-\frac{i\pi}{2}m(\gamma)}\Theta^{1/4}$。

**完整证明**

1. 在每点取 $T_zL$ 的一组 $\mathbb C$-正交归一基 $c_1,\dots,c_n$，令 $e^{i\theta(z)}=\det^2(T_zL)$；换基只会改变各 $c_i$ 的相位，$\det^2$ 不变，故 $\theta$ 在 $L$ 上良定义到相差常数。
   - *为什么*：$\det^2$ 的构造正是为了消掉 $\mathrm U(n)$ 的相位自由度，只留下 $S^1$ 上的一个点。
2. $\varphi$ 把 2-密度 $(\alpha)^2$ 映成 $re^{-i\theta}$，其中 $r=(\alpha(c_1,\dots,c_n))^2>0$；于是 $\varphi(\Omega^4)=|\varphi(\Omega^4)|e^{-i\theta}$，即 $\Theta=e^{-i\theta}$。
   - *为什么*：映射的模由体积比较给出、相位由 $\det^2$ 给出；两件事分开看，才能读出半密度的四分相位。
3. 沿闭路 $\gamma$ 走一圈，$T_zL$ 回到自身，$\det^2\circ\gamma$ 的绕数为 $m(\gamma)$，故 $\theta$ 增加 $2\pi m(\gamma)$（符号由定向约定固定）。
   - *为什么*：绕数就是角度增量除以 $2\pi$；这一步把抽象的 $\pi_1$ 同构换成可计算的角度。
4. 于是 $\Theta^{1/4}=e^{-i\theta/4}$ 变成 $e^{-\frac{i}{4}(\theta+2\pi m(\gamma))}=e^{-\frac{i\pi}{2}m(\gamma)}\Theta^{1/4}$；模长因子 $|\varphi(\Omega^4)|^{1/4}$ 是正实数、单值，绕一圈不变。
   - *为什么*：四次方根把 $2\pi m$ 的增量除以 $4$，$m/4$ 因子正是从这里出来的。

来源：ch05a.tex:1145-1185（原书 p.270–271）

### 命题（凯勒–马斯洛夫 / EBK 量子化条件）

设 $(L,\Omega)$ 是几何半经典定态，$L$ 可定向。几何半经典波 $e^{\frac{i}{\hbar}\int^z\lambda}\Omega$ 在 $L$ 上单值，当且仅当对 $L$ 的每条闭 1-链 $\gamma$ 有 $\frac{1}{2\pi\hbar}\oint_{\gamma}\lambda-\frac14m(\gamma)\in\mathbb Z$。

**完整证明**

1. 沿 $\gamma$ 走一圈，相函数部分 $e^{\frac{i}{\hbar}\int^z\lambda}$ 变为 $e^{\frac{i}{\hbar}\oint_{\gamma}\lambda}$ 倍；由前一定理，半密度部分变为 $e^{-\frac{i\pi}{2}m(\gamma)}$ 倍。
   - *为什么*：两部分的多值性彼此独立：一份来自 $\lambda|_L$ 的周期，一份来自 $\det^2$ 的绕数，可以分开算再相乘。
2. 波在 $L$ 上整体定义，当且仅当总相位回到 $1$：$e^{\frac{i}{\hbar}\oint_{\gamma}\lambda-\frac{i\pi}{2}m(\gamma)}=1$。
   - *为什么*：波函数是两因子的乘积，绕一圈后必须逐点相等，而不只是相差一个与点无关的常数倍数。
3. 取对数得 $\frac{1}{\hbar}\oint_{\gamma}\lambda-\frac{\pi}{2}m(\gamma)\in2\pi\mathbb Z$，两边除以 $2\pi$ 即为 $\frac{1}{2\pi\hbar}\oint_{\gamma}\lambda-\frac14m(\gamma)\in\mathbb Z$。
   - *为什么*：这只是整理常数；当 $m\equiv0$ 时它逐字退回玻尔–索末菲条件，说明新条件确实是旧条件的加细。

来源：ch05a.tex:1187-1199（原书 p.271）

## 易错点

- 马斯洛夫指标存在相差 2 倍的约定：本书取 $m$ 为 $\det^2$ 的绕数（一维时无向直线绕一圈就给 $m=2$），所以修正项是 $m/4$。若改用按 $\det$ 计的约定，必须把因子换成 $m/2$ 或 $m$，否则谐振子谱会整体平移半个 $\hbar\omega$。
- $\frac14$ 不能约成 $\frac12$ 并塞进 $\frac{1}{2\pi\hbar}$：$m$ 与 $\oint\lambda$ 是两个独立的整型量，只有合成之后的总相位才要求是 $2\pi$ 的整数倍。
- 不要把马斯洛夫修正当成 $S$ 的修正。$S$ 仍满足哈密顿–雅可比方程；修正只出现在「波能否在 $L$ 上整体拼接」这一步，因此它是同伦不变量，与 $L$、$\Omega$ 的连续形变无关。

## 相关卡

- [玻尔–索末菲量子化条件](../concepts/bohr-sommerfeld.md)
- [几何半经典定态](../concepts/geometric-semiclassical-state.md)
- [密度、半密度与刘维尔测度](../concepts/half-density.md)
- [马斯洛夫指标与 $\mathcal L(V)$ 的基本群](../concepts/maslov-index.md)
- [拉格朗日子空间与格拉斯曼流形](../concepts/lagrangian-grassmannian.md)
- [谐振子的凯勒–马斯洛夫条件给出精确谱](../examples/oscillator-ebk-spectrum.md)

## 出处

- §5.2.4 马斯洛夫修正，p.270–271（PDF p.271–272），源码 `ch05a.tex:1111-1199`
- §5.2.4 凯勒–马斯洛夫条件，p.271（PDF p.272），源码 `ch05a.tex:1191-1199`
