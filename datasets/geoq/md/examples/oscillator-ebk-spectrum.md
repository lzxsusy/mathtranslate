# 谐振子的凯勒–马斯洛夫条件给出精确谱

> `geoq/example/oscillator-ebk-spectrum` · 轨道 B · 几何半经典量子化 · 状态 draft

> **这张卡练什么**：为什么把刘维尔积分与马斯洛夫指标一起代入条件，就能得到谐振子的精确能谱？

## 一句话

沿椭圆的刘维尔积分是 2πE/ω，马斯洛夫指标为 2；代入 EBK 条件即得 E=ℏω(n+1/2)，与谐振子的精确谱逐项吻合。

## 设定

沿用一维谐振子的数据：$\mathcal H=\frac{p^2}{2m}+\frac{k}{2}x^2$，$\omega=\sqrt{k/m}$，$E>0$。半经典定态取 $L=\{\mathcal H=E\}$（相平面中的椭圆）与 $V_{\mathcal H}$-不变的半密度 $\Omega$。$L$ 是可定向的闭曲线，取 $C$ 为 $L$ 上沿哈密顿流绕行一周的正向闭路。凯勒–马斯洛夫（EBK）量子化条件为 $\frac{1}{2\pi\hbar}\oint_C\lambda-\frac14m(C)\in\mathbb Z$；要算出 $\oint_C\lambda$ 与 $m(C)$，再把 $E$ 解出来。

## 计算

**第 1 步**：由 Stokes 公式，$\oint_C\lambda=\int_\Sigma d\lambda$，其中 $\Sigma$ 是椭圆围成的区域、$\partial\Sigma=C$。又 $\lambda=p\,dx$，$d\lambda=dp\wedge dx$，故该积分等于椭圆的面积：$\oint_Cp\,dx=\pi ab=\pi\sqrt{2E/k}\cdot\sqrt{2mE}=2\pi E\sqrt{m/k}=\frac{2\pi E}{\omega}$。

> 为什么：把一维环路积分换成二维面积分，可以完全避免用 $p(x)=\pm\sqrt{2m(E-kx^2/2)}$ 做带根号的积分；辛形式本身就是面积元。

**第 2 步**：独立复核：由 $\oint_Cp\,dx=\int_0^{T}p\dot x\,dt=\int_0^{T}\frac{p^2}{m}dt=2\langle T_{\mathrm{kin}}\rangle T$，其中 $T=\frac{2\pi}{\omega}$ 为周期；谐振子的维里定理给出 $\langle T_{\mathrm{kin}}\rangle=\frac{E}{2}$，于是 $\oint_Cp\,dx=2\cdot\frac{E}{2}\cdot\frac{2\pi}{\omega}=\frac{2\pi E}{\omega}$，与步骤 1 一致。

> 为什么：两条互不依赖的路线给出同一结果，才能排除「面积公式里漏了因子 $2$」这类错误——这是本例最容易出错的地方。

**第 3 步**：算马斯洛夫指标。椭圆上的切方向随绕行连续转动，作为无向直线它在 $\mathcal L(\mathbb R^2)=\mathrm U(1)/\mathrm O(1)\cong\mathbb{RP}^1$ 中绕了两圈；$\det^2$ 把 $\mathbb{RP}^1$ 同胚地送到 $S^1$，故复合环路在 $S^1$ 上绕两圈，$m(C)=2$。等价地数焦散：由例 5.2.2，椭圆上恰有两个焦散 $u_\pm$，每穿过一个使 $\arg\det^2$ 增加 $2\pi$（即 $m$ 增 $1$），一次往返共增 $4\pi$，仍得 $m(C)=2$。

> 为什么：$\det^2$ 的绕数与「穿越焦散计数」必须给同一个数，否则 EBK 条件的常数项就会错；书中一切关于 $1/4$ 的约定都锚定在这个 $2$ 上。

**第 4 步**：代入 EBK 条件：$\frac{1}{2\pi\hbar}\cdot\frac{2\pi E}{\omega}-\frac{2}{4}\in\mathbb Z$，即 $\frac{E}{\hbar\omega}-\frac12=n$（$n=0,1,2,\dots$），解得 $E_n=\hbar\omega\left(n+\frac12\right)$。

> 为什么：$n\ge0$ 的取法由 $E>0$ 与 $\frac{E}{\hbar\omega}-\frac12\ge0$ 共同限定；若允许 $n<0$ 会得到负能量，与椭圆水平集存在的前提矛盾。

## 结果

$E_n=\hbar\omega\left(n+\frac12\right)$，$n=0,1,2,\dots$，与谐振子的精确能谱逐项相同（基态 $\frac{\hbar\omega}{2}$，等间距 $\hbar\omega$）。这不是巧合：谐振子的势至多二次，WKB 级数在第三阶以后截断，半经典条件因而变成精确条件。

## 复核

① 代回：$n=0$ 给 $E_0=\frac{\hbar\omega}{2}$，$n=1$ 给 $E_1=\frac{3\hbar\omega}{2}$，间距 $E_{n+1}-E_n=\hbar\omega$，与算符代数的结果一致。② 若把马斯洛夫项漏掉（只用玻尔–索末菲条件），得 $E_n=\hbar\omega n$，基态为零、且与不确定关系矛盾；若把指标误取成 $m=4$，修正项变 $1$，得 $E_n=\hbar\omega(n+1)$，基态偏高 $\frac{\hbar\omega}{2}$——两个错误方向相反，正好说明 $m=2$ 不能动。③ 量纲：$[\oint p\,dx]=[\hbar]$，故 $\frac{1}{2\pi\hbar}\oint\lambda$ 无量纲，$m(C)/4$ 也无量纲，条件两侧同量纲。④ 量级：$E\sim\hbar\omega$ 与零点能同阶，符合半经典近似在低激发态也应给出正确标度的预期。

## 易错点

- 马斯洛夫指标 $m(C)=2$ 是按 $\det^2$ 的绕数计的，修正项才是 $\frac{2}{4}=\frac12$。若把 $m$ 理解成「绕 $S^1$ 一圈」而取 $1$，或按「穿过两个焦散、每次 $\frac\pi2$」直接写成 $m=4$，能谱就会整体平移半个或一个 $\hbar\omega$。
- 谐振子能谱的精确性是特例，不能外推：势的三阶以上导数不为零时，WKB 级数不截断，EBK 只给渐近谱，高阶修正一般不为零。
- 这里的 $m(C)=2$ 依赖于 $C$ 绕行一整圈且 $E>0$。若把 $C$ 取成半个周期（只从 $u_-$ 到 $u_+$），穿过一个焦散，$m=1$，条件退化为 $\frac{1}{2\pi\hbar}\int_{u_-}^{u_+}p\,dx-\frac14\in\mathbb Z$ 的「半经典」形式，与整圈的式子不能混用。

## 用到哪些概念

- [马斯洛夫修正与 EBK 条件](../concepts/maslov-correction.md)
- [玻尔–索末菲量子化条件](../concepts/bohr-sommerfeld.md)
- [几何半经典定态](../concepts/geometric-semiclassical-state.md)

## 相关卡

- [一维谐振子的水平集与焦散](../examples/harmonic-oscillator-level-set.md)

## 出处

- §5.2.4 例 5.2.4（谐振子的凯勒–马斯洛夫条件），p.271（PDF p.272），源码 `ch05a.tex:1201-1211`
- §5.2.4 例 5.2.4（续）与 §5.2 小结，p.272（PDF p.273），源码 `ch05b.tex:6-23`
