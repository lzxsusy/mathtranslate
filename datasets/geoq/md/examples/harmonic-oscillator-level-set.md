# 一维谐振子的水平集与焦散

> `geoq/example/harmonic-oscillator-level-set` · 轨道 B · 几何半经典量子化 · 状态 draft

> **这张卡练什么**：为什么谐振子的能量面是拉格朗日子流形，而它的焦散却不在子流形的奇点集里？

## 一句话

把一维谐振子的能量面解成相平面里的椭圆，验证它是拉格朗日子流形；再找出投影的临界点，得到左右两个焦散。

## 设定

取位形空间 $X=\mathbb R$，余切丛 $T^*\mathbb R\cong\mathbb R^2$ 配辛形式 $\omega=dp\wedge dx$ 与刘维尔形式 $\lambda=p\,dx$。一维谐振子的哈密顿函数为 $\mathcal H(x,p)=\frac{p^2}{2m}+\frac{k}{2}x^2$（$m>0$，$k>0$），固有频率 $\omega_0=\sqrt{k/m}$。固定能量 $E>0$，考察水平集 $L=\{(x,p)\in T^*\mathbb R\mid \mathcal H(x,p)=E\}$，并研究余切丛投影 $\pi:L\to\mathbb R,\ (x,p)\mapsto x$ 的临界点（即焦散）。

## 计算

**第 1 步**：先看 $L$ 是不是子流形、是不是拉格朗日的。$d\mathcal H=kx\,dx+\frac{p}{m}\,dp$ 在 $\mathcal H=E>0$ 上不可能为零（若 $d\mathcal H=0$ 则 $x=0,p=0$，与 $E>0$ 矛盾），故 $L$ 是光滑的 $1$ 维子流形，且 $T_{(x,p)}L=\ker d\mathcal H$。又 $\iota_{V_{\mathcal H}}\omega=-d\mathcal H$，而 $\mathcal L(\mathbb R^2)$ 中任意 $1$ 维子空间都是各向同性的，故 $\omega|_{TL}\equiv0$；配合 $\dim L=1=\frac12\dim\mathbb R^2$ 得 $L$ 拉格朗日。

> 为什么：$d\mathcal H\ne0$ 保证水平集不会出奇点（$E>0$ 排除了原点），而 $n=1$ 时各向同性是自动的，真正要核对的是维数恰好为 $n$。

**第 2 步**：解出 $L$ 的方程。把 $\mathcal H=E$ 两边除以 $E$：$\frac{x^2}{2E/k}+\frac{p^2}{2mE}=1$，即相平面中的椭圆 $\frac{x^2}{a^2}+\frac{p^2}{b^2}=1$，半轴 $a=\sqrt{2E/k}$（沿 $x$ 方向）、$b=\sqrt{2mE}$（沿 $p$ 方向）。

> 为什么：这是把二次型配成标准形；半轴的具体长度后面算面积、定焦散位置都要用。

**第 3 步**：求焦散。$\pi|_L$ 在 $(x,p)$ 处是局部微分同胚，当且仅当 $dx$ 在 $T_{(x,p)}L$ 上不恒为零；由 $T_{(x,p)}L=\ker d\mathcal H$ 知这等价于 $\partial_p\mathcal H=p/m\ne0$，即 $p\ne0$。所以临界点恰是 $p=0$ 的两点：$u_\pm=\left(\pm\sqrt{2E/k},\,0\right)$，也就是两个经典转折点。

> 为什么：投影退化与否只看 $p$ 是否为 $0$：在 $u_\pm$ 处切线竖直，$x$ 不再是 $L$ 的局部坐标，半经典振幅 $a_0\propto(\partial H/\partial p)^{-1/2}$ 在那里发散。

**第 4 步**：补一句 $u_\pm$ 并非 $L$ 的奇点。$L$ 在 $u_\pm$ 处依旧光滑，把 $L$ 投影到 $p$ 轴上（映射 $(x,p)\mapsto p$）在 $u_\pm$ 的邻域内是局部微分同胚，因为在 $u_\pm$ 处 $\partial_x\mathcal H=kx=\pm\sqrt{2kE}\ne0$；把 $L$ 局部写成 $x=\pm\sqrt{\frac{2}{k}\left(E-\frac{p^2}{2m}\right)}$ 即可看出这一点。

> 为什么：这一条正是原书的要点：焦散是投影的临界点，而非子流形本身的奇点；换一个投影方向它就消失了。

## 结果

$L$ 是 $T^*\mathbb R\cong\mathbb R^2$ 中由 $\frac{x^2}{a^2}+\frac{p^2}{b^2}=1$（$a=\sqrt{2E/k}$，$b=\sqrt{2mE}$）给出的椭圆，是闭的拉格朗日子流形；椭圆面积为 $\pi ab=\pi\sqrt{2E/k}\cdot\sqrt{2mE}=2\pi E\sqrt{m/k}=\frac{2\pi E}{\omega_0}$。焦散为两点 $u_\pm=\left(\pm\sqrt{2E/k},0\right)$，是两个转折点；$L$ 本身处处光滑，$\pi$ 只在 $u_\pm$ 处退化。沿椭圆绕行一周，切方向随参数转过 $2\pi$，故马斯洛夫指标 $m(L)=2$——也可读成左右两个焦散各贡献 $1$。

## 复核

① 代回焦散：把 $u_\pm$ 代入 $\mathcal H$ 得 $\frac{k}{2}\cdot\frac{2E}{k}+0=E$，确实落在 $L$ 上。② 数值：取 $m=k=E=1$，则 $a=b=\sqrt2$，椭圆为 $x^2+p^2=2$，是半径 $\sqrt2$ 的圆，面积为 $2\pi$，与公式 $2\pi E/\omega_0=2\pi/1$ 一致；焦散为 $(\pm\sqrt2,0)$。③ 量纲：$[E/k]=ML^2T^{-2}/(MT^{-2})=L^2$，故 $a$ 是长度；$[mE]=M\cdot ML^2T^{-2}=M^2L^2T^{-2}$，故 $b$ 是动量；面积 $[ab]=\hbar$ 的量纲（作用量），与 $\oint p\,dx$ 相符。④ 极端情形：$E\to0^+$ 时 $a,b\to0$，椭圆缩成原点，投影处处退化，与「$p\ne0$ 才非临界」的判据一致。

## 易错点

- 只有 $n=1$ 时能量面本身才是拉格朗日的（$1$ 维自然各向同性）。$n\ge2$ 时 $\{\mathcal H=E\}$ 是 $2n-1$ 维超曲面，只能算余迷向，真正的半经典定态要被这个能量面含在内部的 $n$ 维刘维尔环面，别把超曲面当拉格朗日子流形。
- 焦散不是 $L$ 的奇点，也不是「轨道走不过去」的地方：$L$ 在 $u_\pm$ 处光滑，轨道照样穿过，只是 $x$ 坐标在该点不再是局部坐标；判据是 $\pi$ 的微分退化，不要用「$p=0$ 是分母零点」这种解析直觉代替几何判据。
- $E\le0$ 时上述构造退化：$E<0$ 时水平集为空（$\mathcal H\ge0$），$E=0$ 时退化为原点，$d\mathcal H$ 在该点为零，既不是子流形也谈不上拉格朗日性。

## 用到哪些概念

- [几何半经典定态](../concepts/geometric-semiclassical-state.md)
- [WKB 半经典解与哈密顿–雅可比方程](../concepts/wkb-approximation.md)
- [密度、半密度与刘维尔测度](../concepts/half-density.md)

## 相关卡

- [玻尔–索末菲量子化条件](../concepts/bohr-sommerfeld.md)
- [谐振子的凯勒–马斯洛夫条件给出精确谱](../examples/oscillator-ebk-spectrum.md)

## 出处

- §5.2.3 例 5.2.2（谐振子的水平集与焦散），p.268（PDF p.269），源码 `ch05a.tex:1032-1059`
