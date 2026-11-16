# WKB 半经典解与哈密顿–雅可比方程

> `geoq/concept/wkb-approximation` · 轨道 B · 几何半经典量子化 · 状态 draft

> **先自测**：WKB 拟设代入定态薛定谔方程后，ℏ 的零阶与一阶分别给出什么方程，它们各自的几何含义又是什么？

## 一句话

把定态波函数写成相位因子乘 ℏ 的幂级数，逐阶代入薛定谔方程：首阶给出哈密顿–雅可比方程，次阶给出输运方程，几何上等于在能量面上选定一张拉格朗日子流形。

## 定义

WKB 法处理定态方程 $\hat H\psi=E\psi$（$\hat H=-\frac{\hbar^2}{2m}\nabla^2+V$）：尝试 $\psi=e^{\frac{i}{\hbar}S(\mathbf x)}a(\mathbf x,\hbar)$ 形式的解，$S$ 与 $a$ 分别叫相函数、振幅，并要求 $a$ 能展成 $\hbar$ 的渐近级数、首项 $a_0$ 不恒为零。代回方程、按 $\hbar$ 的幂次比较系数，会得到一列递推方程。若只保留领头项 $e^{\frac{i}{\hbar}S}a_0$，所得近似称为半经典近似；其中 $\hbar^0$ 阶方程即 Hamilton–Jacobi 方程，下一阶则是齐次输运方程。

**记号约定**：$m$ 为粒子质量，$V$ 为势能，$E$ 为本征能量，$\hbar$ 为普朗克常数除以 $2\pi$；$\nabla$ 是对位形变量 $\mathbf x\in\mathbb R^n$ 求梯度；$|d^nx|$ 是 $\mathbb R^n$ 的典范体积密度；$\mathcal H(\mathbf x,\mathbf p)=\frac{\mathbf p^2}{2m}+V(\mathbf x)$ 为经典哈密顿函数，$\omega=\sum_i dp_i\wedge dx^i$ 为 $T^*\mathbb R^n$ 的辛形式。

## 要点

- 拟设把解劈成两块：$S$ 管相位、$a$ 管振幅。相位被 $1/\hbar$ 放大，所以 $\hbar\to0$ 时波函数振荡得越来越快，振幅只剩下输运方程这一个约束。
- 零阶方程 $\frac{(\nabla S)^2}{2m}+V=E$ 只含 $S$、不含 $a$：经典力学正是在这一阶进入量子问题的。
- 几何翻译：$\mathbf x\mapsto(\mathbf x,\nabla S(\mathbf x))$ 把位形空间映成 $T^*\mathbb R^n$ 中的拉格朗日子流形 $L_{dS}$；哈密顿–雅可比方程等价于 $\mathcal H$ 在 $L_{dS}$ 上取常值 $E$，也等价于哈密顿向量场 $V_{\mathcal H}$ 在 $L_{dS}$ 上处处相切。
- 一阶方程 $a_0\nabla^2S+2\nabla S\cdot\nabla a_0=0$ 可写成散度形式 $\nabla\cdot(a_0^2\nabla S)=0$：沿 $\nabla S$ 的流，密度 $a_0^2|d^nx|$ 守恒，概率不会丢失。
- 振幅在焦散（投影 $\pi$ 的临界点）处发散，一阶 WKB 表示在那里失效；要跨过焦散拼接，必须补上马斯洛夫相位。
- WKB 级数一般是 $\hbar\to0$ 的发散渐近级数，截断到有限阶才有意义。它对至多二次的势（谐振子）给出精确谱是特例，不能当作普适的精确方法。

## 关键公式

$$
$\psi(\mathbf x)=e^{\frac{i}{\hbar}S(\mathbf x)}\left(a_0(\mathbf x)+a_1(\mathbf x)\hbar+\cdots\right)$
$$

$$
$\frac{(\nabla S)^2}{2m}+V(\mathbf x)=E$
$$

$$
$a_0\nabla^2S+2\nabla S\cdot\nabla a_0=0$
$$

$$
$\nabla\cdot\left(a_0^2\nabla S\right)=0$
$$

$$
$\left(-\frac{\hbar^2}{2m}\nabla^2+V-E\right)\left(ae^{\frac{i}{\hbar}S}\right)=\left[a\left(\frac{(\nabla S)^2}{2m}+V-E\right)-\frac{\hbar^2}{2m}\nabla^2a-\frac{i\hbar}{2m}\left(a\nabla^2S+2\nabla S\cdot\nabla a\right)\right]e^{\frac{i}{\hbar}S}$
$$

## 定理与证明

### 命题（WKB 展开的零阶与一阶方程）

设 $\psi=e^{\frac{i}{\hbar}S}\sum_{k\ge0}a_k\hbar^k$，$a_0\ne0$，代入 $\hat H\psi=E\psi$。则 $\hbar^0$ 阶给出哈密顿–雅可比方程 $\frac{(\nabla S)^2}{2m}+V=E$，$\hbar^1$ 阶给出齐次输运方程 $a_0\nabla^2S+2\nabla S\cdot\nabla a_0=0$；后者又等价于 $a_0^2|d^nx|$ 沿向量场 $\nabla S=\sum_i\partial_iS\,\partial_{x^i}$ 不变。

**完整证明**

1. 先把算符作用在 $ae^{\frac{i}{\hbar}S}$ 上的结果算出来：两个导数分别打在指数因子与振幅上，二阶导数给出 $-\frac{1}{\hbar^2}(\nabla S)^2+\frac{i}{\hbar}\nabla^2S$，归并后即得 formulas 第 5 条的三项式，整体再乘 $e^{\frac{i}{\hbar}S}$。
   - *为什么*：这是纯粹的 Leibniz 法则加链式法则，是后面逐阶比较的唯一依据；不先把它算清楚，幂次一定会数错。
2. 取 $\hbar^0$ 阶：三项中只有 $a\big(\frac{(\nabla S)^2}{2m}+V-E\big)$ 这一项不带正幂 $\hbar$，代入 $a=a_0+O(\hbar)$ 后它给出 $a_0\big(\frac{(\nabla S)^2}{2m}+V-E\big)$；因 $a_0\ne0$ 可以除掉，得 $\frac{(\nabla S)^2}{2m}+V=E$。
   - *为什么*：$a_0\ne0$ 这条要求就是为这一步准备的：它保证首阶方程不是恒等式，而是一个真正约束 $S$ 的方程。
3. 取 $\hbar^1$ 阶：$-\frac{i\hbar}{2m}(a\nabla^2S+2\nabla S\cdot\nabla a)$ 取 $a=a_0$ 恰是 $\hbar^1$ 阶，而 $-\frac{\hbar^2}{2m}\nabla^2a_0$ 已属 $\hbar^2$ 阶；于是 $a_0\nabla^2S+2\nabla S\cdot\nabla a_0=0$。
   - *为什么*：$\nabla^2a_0$ 那一项比当前阶高一阶，属于下一条递推式；把它算进来就会平白多出一个不可能的方程。
4. 在输运方程两边乘 $a_0$：$a_0^2\nabla^2S+2a_0\nabla S\cdot\nabla a_0=\nabla\cdot(a_0^2\nabla S)=0$；再对向量场 $X=\nabla S$ 用 $\mathcal L_X(\rho|d^nx|)=\nabla\cdot(\rho X)|d^nx|$，得 $\mathcal L_{\nabla S}(a_0^2|d^nx|)=0$。
   - *为什么*：乘 $a_0$ 是为了把两项凑成全散度，从而读成密度守恒；这也说明守恒律的主语是 $a_0^2$ 而不是 $a_0$。

来源：ch05a.tex:843-918（原书 p.264–265）

### 命题（哈密顿–雅可比方程的拉格朗日几何刻画）

设 $S\in C^\infty(\mathbb R^n)$，$L_{dS}=\{(\mathbf x,\mathbf p)\mid\mathbf p=\nabla S(\mathbf x)\}\subset T^*\mathbb R^n$。则下列三条等价：(i) $S$ 满足 $\mathcal H(\mathbf x,\nabla S(\mathbf x))=E$；(ii) $\mathcal H|_{L_{dS}}\equiv E$；(iii) $V_{\mathcal H}$ 在 $L_{dS}$ 上处处与 $L_{dS}$ 相切。

**完整证明**

1. $\mathbf x\mapsto(\mathbf x,\nabla S(\mathbf x))$ 是 $n$ 维子流形 $L_{dS}$ 的参数化，且 $\lambda|_{L_{dS}}=\sum_i\partial_iS\,dx^i=dS$。
   - *为什么*：刘维尔形式 $\lambda=\sum_ip_idx^i$ 在 $\mathbf p=\nabla S$ 上正好退化为 $dS$，这说明 $L_{dS}$ 是恰当可投影的。
2. 于是 $\omega|_{L_{dS}}=d\lambda|_{L_{dS}}=d(dS)=0$，即 $L_{dS}$ 各向同性；又 $\dim L_{dS}=n=\frac12\dim T^*\mathbb R^n$，故它是拉格朗日子流形。
   - *为什么*：各向同性加最大维数就是拉格朗日性的定义，无需再验证别的东西。
3. 把 $\mathbf p=\nabla S$ 代进哈密顿函数，得到 $\mathcal H|_{L_{dS}}(\mathbf x)=\mathcal H(\mathbf x,\nabla S(\mathbf x))$；所以 (i) 与 (ii) 是同一句话的两种写法，而 (ii) 又等价于 $d\mathcal H|_{L_{dS}}=0$。
   - *为什么*：常值函数的微分是零；反之 $L_{dS}$ 连通，$d\mathcal H$ 在它上面为零就意味着 $\mathcal H$ 取常值。
4. 哈密顿方程 $\iota_{V_{\mathcal H}}\omega=d\mathcal H$ 说明 $d\mathcal H|_{L_{dS}}=0$ 等价于 $\omega(V_{\mathcal H},T_zL_{dS})=0$ 对每个 $z\in L_{dS}$ 成立，即 $V_{\mathcal H}(z)\in(T_zL_{dS})^{\omega}$。
   - *为什么*：这只是把 $d\mathcal H$ 换成它对切向量的取值，用的是哈密顿向量场的定义式。
5. 对拉格朗日 $L$ 有 $(T_zL)^{\omega}=T_zL$：包含 $T_zL\subset(T_zL)^{\omega}$ 来自 $\omega|_{L}=0$，而两边维数都是 $n$。故 $\omega(V_{\mathcal H},T_zL)=0\iff V_{\mathcal H}(z)\in T_zL$，即 (ii) 与 (iii) 等价。
   - *为什么*：没有拉格朗日性，$V_{\mathcal H}$ 只能落在辛正交补里，未必真的相切；这是本命题的关键一步。

来源：ch05a.tex:869-905（原书 p.265）

## 易错点

- 输运方程是 $a_0$ 的一阶方程，但守恒律的主语是 $a_0^2$：写成 $\nabla\cdot(a_0^2\nabla S)=0$ 才对，误写成 $\nabla\cdot(a_0\nabla S)=0$ 会多出 $\frac12a_0\nabla^2S$ 一项。
- 相位的符号决定动量的指向：拟设取 $e^{+\frac{i}{\hbar}S}$ 时 $\mathbf p=\nabla S$，取 $e^{-\frac{i}{\hbar}S}$ 时 $\mathbf p=-\nabla S$，输运方程与焦散判据随之变号；两种约定混用会把 $V_{\mathcal H}$ 的切向算反。
- 高阶递推式的指标要按级数约定对齐：在 $a\sim\sum_ka_k\hbar^k$、$\psi=e^{iS/\hbar}a$ 下，比较 $\hbar^{k+1}$ 阶得到 $a_k\nabla^2S+2\nabla S\cdot\nabla a_k=i\nabla^2a_{k-1}$（$k\ge1$），其中没有额外的 $\hbar$；若把 $k$ 的起点或 $\hbar$ 的幂次记错，整阶修正会错位。

## 相关卡

- [密度、半密度与刘维尔测度](../concepts/half-density.md)
- [玻尔–索末菲量子化条件](../concepts/bohr-sommerfeld.md)
- [几何半经典定态](../concepts/geometric-semiclassical-state.md)
- [拉格朗日子流形、可投影与相函数](../concepts/lagrangian-submanifold.md)
- [哈密顿向量场与泊松括号](../concepts/hamiltonian-vector-field.md)
- [余切丛的典范辛结构与刘维尔形式](../concepts/cotangent-bundle.md)
- [一维谐振子的水平集与焦散](../examples/harmonic-oscillator-level-set.md)

## 出处

- §5.2.1 半经典解，p.263–265（PDF p.264–266），源码 `ch05a.tex:813-919`
- §5.2.1 输运方程的几何改写，p.266（PDF p.267），源码 `ch05a.tex:920-949`
