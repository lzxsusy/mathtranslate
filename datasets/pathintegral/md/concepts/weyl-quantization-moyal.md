# 外尔量子化与 Moyal 乘积

> `pi/concept/weyl-quantization-moyal` · 轨道 E · 微扰与代数结构 · 状态 draft

> **先自测**：Moyal 乘积为什么自然出现在相空间路径积分里，它的结合性又从何而来？

## 一句话

相空间路径积分的两点函数只依赖时间的先后，其收缩规则给出 Moyal 乘积；结合性源于时间位置的拓扑不变性，$\hbar$ 展开的首阶修正是泊松括号。

## 定义

取相空间 $\mathbb{R}^{2}$，坐标记 $(x,p)$。一条轨道是映射 $\gamma:\mathbb{R}\to\mathbb{R}^{2}$，$\gamma(t)=(\mathbb{X}(t),\mathbb{P}(t))$，记 $\mathcal{E}=\operatorname{Map}(\mathbb{R},\mathbb{R}^{2})$。零哈密顿量的作用量取 $S_{0}[\gamma]=\int\mathbb{P}\dot{\mathbb{X}}\,dt$，它对 $\gamma$ 是二次的。把相空间函数 $f,g$ 分别插在 $t_{2}>t_{1}$ 与 $t_{1}$，用背景 $(x,p)$ 作平移，取关联
$$\left\langle f(x+\mathbb{X}(t_{2}),p+\mathbb{P}(t_{2}))\,g(x+\mathbb{X}(t_{1}),p+\mathbb{P}(t_{1}))\right\rangle_{\gamma},$$
再令 $t_{1}\to t_{2}$，所得的相空间函数记作 $f*_{\hbar}g$，称为 Moyal 乘积（Moyal product）。它正是外尔量子化（Weyl quantization）$f\mapsto\hat{f}$ 之下算子乘积 $\hat{f}\hat{g}$ 的相空间对应物：先插哪个函数，对应先作用哪个算子。

**记号约定**：$(x,p)\in\mathbb{R}^{2}$ 既是相空间坐标又是背景平移量；$\mathbb{X},\mathbb{P}$ 为量子涨落；$*_{\hbar}$ 为 Moyal 乘积；$\{f,g\}=\partial_{x}f\,\partial_{p}g-\partial_{p}f\,\partial_{x}g$ 为泊松括号；$G$ 为 $\frac{d}{dt}$ 的格林函数。

## 要点

- 自由作用量的二次型矩阵含 $\frac{d}{dt}$，求逆要靠格林函数 $G(t_{1},t_{2})=\frac{1}{2}\operatorname{sgn}(t_{1}-t_{2})$，两点函数就是它的 $\pm\frac{i\hbar}{2}$ 倍。
- 两点函数只有 $\mathbb{X}$–$\mathbb{P}$ 的混合分量非零，并且只依赖谁先谁后：$t_{1}>t_{2}$ 给 $+\frac{i\hbar}{2}$，$t_{1}<t_{2}$ 给 $-\frac{i\hbar}{2}$。
- 同侧收缩 $\langle\mathbb{X}\mathbb{X}\rangle=\langle\mathbb{P}\mathbb{P}\rangle=0$，故每条边都连接两个不同函数的半边，这是指数里那个双线性型的来源。
- 把 $f$ 与 $g$ 的半边按全部双射配对的求和，等于对 $\frac{i\hbar}{2}(\overleftarrow{\partial_{x}}\overrightarrow{\partial_{p}}-\overleftarrow{\partial_{p}}\overrightarrow{\partial_{x}})$ 取指数。
- 结合性：三点关联只依赖插入顺序，与时刻落在哪里无关，两种括号方式因而给出同一个极限；$\hbar\to0$ 时 $f*_{\hbar}g=fg+\frac{i\hbar}{2}\{f,g\}+\cdots$。

## 关键公式

$$
S_{0}[\gamma]=\int\mathbb{P}\dot{\mathbb{X}}\,dt=\frac{1}{2}\int\left(\mathbb{P}\dot{\mathbb{X}}-\mathbb{X}\dot{\mathbb{P}}\right)dt
$$

$$
\langle\mathbb{X}(t_{1})\mathbb{P}(t_{2})\rangle_{\gamma}=\frac{i\hbar}{2}\operatorname{sgn}(t_{1}-t_{2})
$$

$$
f*_{\hbar}g=f\,\exp\left(\frac{i\hbar}{2}\left(\overleftarrow{\frac{\partial}{\partial x}}\overrightarrow{\frac{\partial}{\partial p}}-\overleftarrow{\frac{\partial}{\partial p}}\overrightarrow{\frac{\partial}{\partial x}}\right)\right)g
$$

$$
f*_{\hbar}g=fg+\frac{i\hbar}{2}\{f,g\}+O(\hbar^{2})
$$

$$
f*_{\hbar}g-g*_{\hbar}f=i\hbar\{f,g\}+O(\hbar^{3})
$$

## 定理与证明

### Moyal 乘积的显式公式

设 $f,g$ 是相空间上的多项式，$t_{2}>t_{1}$，则 $\left\langle f(x+\mathbb{X}(t_{2}),p+\mathbb{P}(t_{2}))\,g(x+\mathbb{X}(t_{1}),p+\mathbb{P}(t_{1}))\right\rangle_{\gamma}$ 在 $t_{1}\to t_{2}^{-}$ 下等于 $f*_{\hbar}g$，且 $f*_{\hbar}g=f\exp\left(\frac{i\hbar}{2}(\overleftarrow{\partial_{x}}\overrightarrow{\partial_{p}}-\overleftarrow{\partial_{p}}\overrightarrow{\partial_{x}})\right)g$。

**完整证明**

1. 把 $f,g$ 在背景 $(x,p)$ 处展开成 $\mathbb{X},\mathbb{P}$ 的多项式，用威克定理把所有因子两两收缩。
   - *为什么*：平移之后求的就是多项式在自由高斯测度下的矩，威克定理把它化成一串传播子之积。
2. 同侧收缩为零（$\langle\mathbb{X}\mathbb{X}\rangle=\langle\mathbb{P}\mathbb{P}\rangle=0$），所以每条边必须连接 $f$ 的一条半边与 $g$ 的一条半边。
   - *为什么*：两点函数只有混合分量，配对只能发生在 $\mathbb{X}$ 与 $\mathbb{P}$ 之间，同一函数内部无法成边。
3. 沿 $f\to g$ 方向把 $\mathbb{X}$ 与 $\mathbb{P}$ 配对给 $+\frac{i\hbar}{2}$（因 $t_{2}>t_{1}$），反向给 $-\frac{i\hbar}{2}$；这恰是算子 $\frac{i\hbar}{2}(\overleftarrow{\partial_{x}}\overrightarrow{\partial_{p}}-\overleftarrow{\partial_{p}}\overrightarrow{\partial_{x}})$ 的两项。
   - *为什么*：对 $f$ 求 $\partial_{x}$、对 $g$ 求 $\partial_{p}$ 并乘系数，与把 $f$ 的 $\mathbb{X}$ 半边接到 $g$ 的 $\mathbb{P}$ 半边是同一件事。
4. 对 $m$ 条边的全部配对求和并按 $m!$ 归一，得到 $\sum_{m}\frac{1}{m!}\left(\frac{i\hbar}{2}\Lambda\right)^{m}$，其中 $\Lambda=\overleftarrow{\partial_{x}}\overrightarrow{\partial_{p}}-\overleftarrow{\partial_{p}}\overrightarrow{\partial_{x}}$，即指数式。
   - *为什么*：$\Lambda^{m}$ 的展开自动枚举 $m$ 条交叉边的所有接法，指数把各阶 $m$ 打包，$m!$ 正是边次序的重复计数。

来源：ch02c.tex:697-744（原书 p.149–150）

### Moyal 乘积的结合性

对相空间上的多项式 $f,g,h$，有 $(f*_{\hbar}g)*_{\hbar}h=f*_{\hbar}(g*_{\hbar}h)$。

**证明提纲**

1. 把 $h,g,f$ 按时间顺序插入，得到三点关联；它只依赖三者的先后，不依赖时刻的绝对值。
   - *为什么*：两点函数只含 $\operatorname{sgn}(t_{i}-t_{j})$，整体平移或局部挪动时刻都不改变符号。
2. 两种括号化对应先合并其中一对、再与第三个收缩；两种取极限都落到同一个有序三点关联上。
   - *为什么*：先合并哪一对不改变最终的先后次序，极限值因此相同。
3. 故 $(f*_{\hbar}g)*_{\hbar}h=f*_{\hbar}(g*_{\hbar}h)$。
   - *为什么*：两边是同一极限的两种取法。

> **缺口**：书中只说这是结合性的「简单解释」：论证依据是关联函数的拓扑性，但没有证明它对时刻的局部形变真正不变（需要对路径积分测度或正规化给出估计），也没讨论两个极限交换的合法性。严格证明可在 Weyl 符号演算中把 $*_{\hbar}$ 写成 $e^{\frac{i\hbar}{2}\Lambda}$、利用 $\Lambda$ 是常系数双微分算子得到。


来源：ch02c.tex:753-784（原书 p.150–151）

## 易错点

- Moyal 乘积不交换：互换 $f,g$ 的插入时刻得到的是 $g*_{\hbar}f$，两者相差 $i\hbar\{f,g\}$ 起。
- $\langle\mathbb{X}\mathbb{X}\rangle=\langle\mathbb{P}\mathbb{P}\rangle=0$ 只对零哈密顿量的自由作用量成立，换成一般哈密顿量必须重算传播子。
- 对多项式 $f,g$，指数级数在有限阶后自动截断；对一般光滑函数它只是形式幂级数，不能当作收敛展开逐项换序。
- 对称化 $\frac{1}{2}(f*_{\hbar}g+g*_{\hbar}f)=fg+O(\hbar^{2})$ 的首阶就是普通乘积，别把 $O(\hbar)$ 的泊松括号项算进对称部分。

## 相关卡

- [费曼图的组合定义与展开公式](../concepts/feynman-diagrams.md)
- [威克定理与高斯矩的配对](../concepts/wick-theorem.md)
- [量子 HKR 映射](../concepts/quantum-hkr.md)
- [$S^1$ 上的传播子与关联函数](../concepts/s1-correlators.md)

## 出处

- §2.8.3 再论外尔量子化，p.146–151（PDF p.147–152），源码 `ch02c.tex:521-785`
