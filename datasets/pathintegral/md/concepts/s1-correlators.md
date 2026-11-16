# $S^1$ 上的传播子与关联函数

> `pi/concept/s1-correlators` · 轨道 E · 微扰与代数结构 · 状态 draft

> **先自测**：为什么 $S^1$ 上的传播子要先删掉零模，而关联函数前的 $m!$ 又恰好与循环序区域的体积相消？

## 一句话

把相空间路径放到圆周上：$\partial_\theta$ 的零模必须剔除，格林函数由命题 2.8.11 给出分段形式，定义 2.8.12 再用威克定理与循环序积分把 $m+1$ 个多项式收缩成一个 $A[\hbar]$ 中的元素。

## 定义

把量子力学模型的相空间路径改成定义在圆周上的周期映射 $\gamma(\theta)=(\mathbb{X}^i(\theta),\mathbb{P}_i(\theta))$，$\theta\sim\theta+1$，自由作用量取 $S_0=\int_{S^1}\mathbb{P}_i\dot{\mathbb{X}}^i\,d\theta$。两点收缩由 $d/d\theta$ 的积分核 $G$ 给出，而常数函数不能被 $d/d\theta$ 求逆，因此求逆只在去掉 $n=0$ 分量之后进行，此时 $\delta$ 要换成 $\hat\delta=\delta-1$。对 $f_0,\dots,f_m\in A=\mathbb{R}[x,p]$，先把每个 $f$ 沿同一点的量子涨落平移成 $\mathcal{O}_f(\theta)=f(\mathbf{x}+\mathbb{X}(\theta),\mathbf{p}+\mathbb{P}(\theta))$，用威克定理把涨落两两收缩掉，再在循环序构型空间 $\mathrm{Cyc}_{m+1}(S^1)$ 上积分并乘 $m!$；所得 $A[\hbar]$ 中的元素称为这组多项式的 $S^1$ 关联。

**记号约定**：$A=\mathbb{R}[x,p]$（或 $\mathbb{R}[x^i,p_i]$）；$\theta\in S^1=\mathbb{R}/\mathbb{Z}$；$G(\theta_1,\theta_2)=g(\theta_2-\theta_1)$；$\mathrm{Cyc}_{m+1}(S^1)$ 是循环顺序互不相同的 $m+1$ 元组；$\langle-\rangle_\gamma^{S^1}$ 是沿 $\gamma$ 的涨落期望。

## 要点

- $S^1$ 上的常函数不能被 $d/d\theta$ 求逆，这就是零模；剔除它的代价是把 $\delta$ 换成 $\hat\delta=\delta-1$，$G$ 只解 $\partial_{\theta_1}G=\hat\delta$。
- $g$ 在 $(0,1)$ 上等于 $\theta-\tfrac12$、在 $0$ 处取 $0$，于是它是周期为 $1$ 的奇函数；这是命题 2.8.11 的内容。
- 两点函数在两点重合时出现跳跃：从一侧趋近得 $-\mathrm{i}\hbar/2$、从另一侧得 $+\mathrm{i}\hbar/2$，与 $\mathbb{R}$ 上的传播子一致，因为圆周的局部几何就是直线。
- 循环序区域 $\mathrm{Cyc}_{m+1}(S^1)$ 的体积是 $1/m!$，定义里的前置 $m!$ 正是为消掉它，使 $\hbar\to0$ 时回到普通乘法。
- 因此 $S^1$ 关联给出 $A$ 的一个形变量子化：零阶是交换乘法，高阶项全部来自 $G$ 的重合奇性。

## 关键公式

$$
G(\theta_1,\theta_2)=g(\theta_2-\theta_1)=\sum_{n\in\mathbb{Z}\setminus\{0\}}\frac{\mathrm{i}}{2\pi n}e^{2\pi\mathrm{i}n(\theta_2-\theta_1)}
$$

$$
\frac{\partial}{\partial\theta_1}G(\theta_1,\theta_2)=\hat\delta(\theta_1,\theta_2)=\delta(\theta_1,\theta_2)-1
$$

$$
\langle\mathbb{X}^k(\theta_1)\mathbb{P}_j(\theta_2)\rangle_\gamma^{S^1}=\mathrm{i}\hbar\,g(\theta_2-\theta_1)\,\delta^k_j
$$

$$
\langle f_0\otimes\cdots\otimes f_m\rangle_{S^1}=m!\int_{\mathrm{Cyc}_{m+1}(S^1)}d\theta_0\cdots d\theta_m\left\langle\mathcal{O}_{f_0}(\theta_0)\cdots\mathcal{O}_{f_m}(\theta_m)\right\rangle_\gamma^{S^1}
$$

$$
\lim_{\hbar\to0}\langle f_0\otimes\cdots\otimes f_m\rangle_{S^1}=f_0\cdots f_m
$$

## 定理与证明

### 命题 2.8.11（$S^1$ 格林函数的分段形式）

把 $g$ 延拓成 $\mathbb{R}$ 上周期为 $1$ 的函数，则在 $[0,1)$ 上有 $g(0)=0$ 与 $g(\theta)=\theta-\tfrac12$（$0<\theta<1$）；这样延拓的 $g$ 满足 $g(-\theta)=-g(\theta)$。

**完整证明**

1. 对 $n\neq0$ 计算 $\theta-\tfrac12$ 的傅里叶系数：$\int_0^1e^{-2\pi\mathrm{i}n\theta}(\theta-\tfrac12)d\theta$ 用分部积分，边界项因 $e^{-2\pi\mathrm{i}n}=1$ 化为 $\frac{1}{-2\pi\mathrm{i}n}\left(\tfrac12+\tfrac12\right)=\frac{\mathrm{i}}{2\pi n}$。
   - *为什么*：级数 $\sum_{n\neq0}\frac{\mathrm{i}}{2\pi n}e^{2\pi\mathrm{i}n\theta}$ 的系数必须与它逐项相同，才能断言两边是同一个函数。
2. 分部积分留下的第二项是 $\frac{1}{2\pi\mathrm{i}n}\int_0^1e^{-2\pi\mathrm{i}n\theta}d\theta=0$（$n\neq0$ 时一个完整周期的积分为零），所以系数确实只有 $\frac{\mathrm{i}}{2\pi n}$。
   - *为什么*：书中这一步漏印了因子 $\mathrm{i}/(2\pi n)$，但该项本身为零，结论不受影响；这里补全以免误以为还有别的贡献。
3. 常数项即 $n=0$ 的系数是 $\int_0^1(\theta-\tfrac12)d\theta=0$，展开中没有零模分量。
   - *为什么*：这与 $G$ 只在 $\hat\delta$ 上求逆相容：$g$ 的平均值为零，正是零模被剔除的印记。
4. 于是 $0<\theta<1$ 时级数与 $\theta-\tfrac12$ 的傅里叶级数逐项一致；$\theta=0$ 处 $n$ 与 $-n$ 的项相消给出 $0$，故 $g(0)=0$，且系数关于 $n$ 的奇对称给出 $g(-\theta)=-g(\theta)$。
   - *为什么*：周期函数由傅里叶系数唯一确定；奇性则说明端点取值无法任意指定，只能取级数的对称和。

来源：ch02c.tex:850-883（原书 p.152）

### 两点函数的重合极限

当 $\theta_1\to\theta_2$ 时 $S^1$ 上的两点函数回到 $\mathbb{R}$ 上的值：$\lim_{\theta_1\to\theta_2^-}\langle\mathbb{X}^k(\theta_1)\mathbb{P}_j(\theta_2)\rangle_\gamma^{S^1}=-\frac{\mathrm{i}\hbar}{2}\delta^k_j$，而从另一侧趋近得 $+\frac{\mathrm{i}\hbar}{2}\delta^k_j$。

**完整证明**

1. 令 $u=\theta_2-\theta_1$，把命题 2.8.11 的周期延拓用到负自变量：$g(u)=u-\tfrac12$（$0<u<1$），$g(u)=u+\tfrac12$（$-1<u<0$）。
   - *为什么*：$u$ 的符号决定用哪一段线性表达式，这正是两个单侧极限相差 $1$ 的原因。
2. $\theta_1\to\theta_2^-$ 时 $u\to0^+$，故 $g(u)\to-\tfrac12$；$\theta_1\to\theta_2^+$ 时 $u\to0^-$，故 $g(u)\to+\tfrac12$。
   - *为什么*：跳跃量恰好是 $1$，与 $\partial_\theta G=\delta-1$ 的首项系数一致。
3. 乘上 $\mathrm{i}\hbar\delta^k_j$ 即得两个单侧极限；当两点分离时 $g$ 平滑，故远离重合处看不出圆周与直线的差别。
   - *为什么*：这一步把周期格林函数翻译成可测的量：只有重合点携带拓扑信息。

来源：ch02c.tex:905-918（原书 p.153）

## 易错点

- 零模不能随手丢掉：$\hat\delta=\delta-1$，若把 $G$ 当成 $\delta$ 的原函数会多出常数项，周期性被破坏。
- 定义 2.8.12 的 $m!$ 与测度不能重复计入：$\int_{\mathrm{Cyc}_{m+1}}=1/m!$，若写成 $(m!)^2$，$\hbar\to0$ 的极限会放大成 $m!\,f_0\cdots f_m$。
- 命题 2.8.11 的证明第二项要带 $\mathrm{i}/(2\pi n)$（书上漏印，tutornote 已指出）；照抄会以为该项系数为 $1$。
- $g(0)=0$ 不是人为约定：级数在 $\theta=0$ 的对称求和本来就是 $0$，书里说「取 $g(0)=0$ 以保证奇性」因果说反了。

## 相关卡

- [外尔量子化与 Moyal 乘积](../concepts/weyl-quantization-moyal.md)
- [量子 HKR 映射](../concepts/quantum-hkr.md)
- [霍赫希尔德同调](../concepts/hochschild-homology.md)

## 出处

- §2.8.4 $S^1$ 关联，p.151–155（PDF p.152–156），源码 `ch02c.tex:786-1045`
