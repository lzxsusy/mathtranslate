# 几何半经典定态

> `geoq/concept/geometric-semiclassical-state` · 轨道 B · 几何半经典量子化 · 状态 draft

> **先自测**：几何半经典定态的两个部件各自承担什么信息，为什么这个定义在焦散处依然有意义？

## 一句话

定态的半经典信息浓缩为一对 (L,Ω)：拉格朗日子流形落在能量面上、半密度在哈密顿流下不变；这个定义不依赖投影坐标，因此能跨过焦散描述态。

## 定义

所谓几何半经典定态，指的是给拉格朗日子流形配上半密度的一份数据 $(L,\Omega)$，并满足两条约束。第一，$L\subset T^*X$ 必须整块位于 $\mathcal H$ 的同一等能面 $\mathcal H^{-1}(E)$ 中；第二，$\Omega$ 在 $L$ 上处处非零，且沿 $V_{\mathcal H}$ 的李导数为零。前一条保证了 $V_{\mathcal H}$ 切于 $L$，于是后一条中的李导数无需求解 $L$ 外的流，不变性提法才说得通。

**记号约定**：$X=\mathbb R^n$ 为位形空间，$\mathcal H$ 为经典哈密顿函数；$\Omega\in\Gamma(L,\mathrm{Dens}_L^{1/2})$ 且处处非零；可投影情形记 $s:X\to L,\ \mathbf x\mapsto(\mathbf x,\nabla S(\mathbf x))$，并写 $s^*\Omega=a_0|d^nx|^{1/2}$。

## 要点

- 分工很清楚：$L$ 承载相位（$S=\int\lambda$，只定到常数）与能量（$\mathcal H|_L\equiv E$），$\Omega$ 承载振幅（$|\Omega|^2$ 是概率密度）。
- 条件 ① 有两种等价读法：$\mathcal H$ 在 $L$ 上是常数；$V_{\mathcal H}$ 处处切于 $L$。后者才是「定态」的几何内容——流不会把 $L$ 推离自身。
- 条件 ② 就是 WKB 输运方程的几何版：$\mathcal L_{V_{\mathcal H}}\Omega=0\iff\nabla\cdot(a_0^2\nabla S)=0$，即概率沿流守恒。
- $L$ 只要求拉格朗日、不要求可投影：焦散处投影退化、$a_0$ 在位形表示下发散，但 $(L,\Omega)$ 本身光滑，所以几何语言能跨过焦散。
- 把 $(L,\Omega)$ 变成真正的量子态还差两步：单值性条件（玻尔–索末菲加马斯洛夫，即 EBK）与极化（第 5.4 节）。在此之前它只是 WKB 首阶的几何化身。
- 对谐振子，$L$ 是 $T^*\mathbb R\cong\mathbb R^2$ 中的椭圆，$V_{\mathcal H}$ 沿它循环流动；$V_{\mathcal H}$-不变的半密度就是按流参数写出的 $|dt|^{1/2}$ 的常数倍。

## 关键公式

$$
$\mathcal H|_L\equiv E$
$$

$$
$\left.\iota_{V_{\mathcal H}}\omega\right|_L=0\iff V_{\mathcal H}(z)\in T_zL$
$$

$$
$\mathcal L_{V_{\mathcal H}}\Omega=0$
$$

$$
$s^*\Omega=a_0(\mathbf x)\,|d^n\mathbf x|^{1/2}$
$$

$$
$\psi=e^{\frac{i}{\hbar}S(\mathbf x)}a_0(\mathbf x)$
$$

## 定理与证明

### 命题（几何半经典数据在哈密顿流下不变）

设 $(L,\Omega)$ 是几何半经典定态，$\varphi_t$ 为 $\mathcal H$ 的哈密顿流。则在其定义范围内 $\varphi_t(L)=L$ 且 $\varphi_t^*\Omega=\Omega$。

**完整证明**

1. 由条件 ① 得 $d\mathcal H|_L=0$；又 $\iota_{V_{\mathcal H}}\omega=d\mathcal H$，故 $\omega(V_{\mathcal H},T_zL)=0$，即 $V_{\mathcal H}(z)\in(T_zL)^{\omega}$。$L$ 拉格朗日给出 $(T_zL)^{\omega}=T_zL$，于是 $V_{\mathcal H}(z)\in T_zL$。
   - *为什么*：这一步把「$\mathcal H$ 沿 $L$ 取常值」翻译成「$V_{\mathcal H}$ 与 $L$ 相切」，是定义 ② 有意义的前提。
2. 向量场与子流形相切时，从 $L$ 上出发的积分曲线永不离开 $L$，故 $\varphi_t(L)\subset L$；又 $\varphi_t$ 是微分同胚，故 $\varphi_t(L)=L$。
   - *为什么*：相切就是「初值在 $L$ 内则解族留在 $L$ 内」；可逆性把单侧包含升成等式。
3. 条件 ② 说 $\mathcal L_{V_{\mathcal H}}\Omega=0$。由于 $\varphi_t$ 是单参数群，$\frac{d}{dt}\varphi_t^*\Omega=\varphi_t^*\mathcal L_{V_{\mathcal H}}\Omega=0$ 对一切 $t$ 成立，故 $\varphi_t^*\Omega$ 与 $t$ 无关，等于 $t=0$ 时的 $\Omega$。
   - *为什么*：李导数沿流与拉回可交换，所以在 $t=0$ 验证一次就够；这也给出了「不变」的严格含义。

来源：ch05a.tex:1062-1068（原书 p.268）

### 命题（可投影情形下 $(L,\Omega)$ 还原 WKB 解）

设 $L=L_{dS}$ 恰当可投影，$\pi:L\to\mathbb R^n$ 为微分同胚，$s=\pi^{-1}$，$s^*\Omega=a_0|d^nx|^{1/2}$，且 $(L,\Omega)$ 满足几何半经典定态的定义。则 $\psi=e^{\frac{i}{\hbar}S}a_0$ 满足 WKB 的两个首阶方程（哈密顿–雅可比方程与齐次输运方程）。

**完整证明**

1. 由 $L=L_{dS}$ 得 $\lambda|_L=dS$，故在 $L$ 上 $p_i=\partial_iS$；把 $\mathbf p=\nabla S$ 代入条件 ① 得 $\mathcal H(\mathbf x,\nabla S)=E$，正是哈密顿–雅可比方程。
   - *为什么*：只需把 $L_{dS}$ 的参数化代回 $\mathcal H|_L\equiv E$，不需要额外计算。
2. 由前一定理，$\mathcal L_{V_{\mathcal H}}\Omega=0$ 沿 $\pi$ 推前为 $\nabla\cdot(a_0^2\nabla S)=0$（差一个非零因子 $-\frac1m$ 不影响零点），正是齐次输运方程。
   - *为什么*：推前只把向量场乘上非零函数，「李导数为零」在这种乘性变化下不变。
3. 两条首阶方程同时成立，故 $\psi=e^{\frac{i}{\hbar}S}a_0$ 是半经典解；这说明定义 5.2.3 不是空话，而是 WKB 解析拟设的几何重写。
   - *为什么*：把结论接回 WKB 卡的命题，整个链条才闭合；也解释了为什么需要 $\Omega$ 而不只是一个函数 $a_0$。

来源：ch05a.tex:1000-1018（原书 p.267）

## 易错点

- $(L,\Omega)$ 不是希尔伯特空间中的向量：它只承载 WKB 首阶信息，还要过 EBK 单值性条件、选定极化，才对应到真正的量子态。「定态」在这里指几何数据不随流变，而不是本征态已经构造完毕。
- 半密度可以乘任意正常数，定义本身不固定归一化；把 $|\Omega|^2$ 解释成概率密度时必须另给归一化条件，否则振幅没有物理含义。
- $V_{\mathcal H}$ 在 $L$ 上必须非零，否则「沿流不变」退化，$L$ 也无法由一条轨道扫出；谐振子在 $E>0$ 时 $V_{\mathcal H}$ 于椭圆上无零点，而 $E=0$ 时轨道塌成一点，正好落在定义失效的边界上。

## 相关卡

- [WKB 半经典解与哈密顿–雅可比方程](../concepts/wkb-approximation.md)
- [密度、半密度与刘维尔测度](../concepts/half-density.md)
- [玻尔–索末菲量子化条件](../concepts/bohr-sommerfeld.md)
- [马斯洛夫修正与 EBK 条件](../concepts/maslov-correction.md)
- [拉格朗日子流形、可投影与相函数](../concepts/lagrangian-submanifold.md)
- [哈密顿向量场与泊松括号](../concepts/hamiltonian-vector-field.md)
- [极化：实极化与凯勒极化](../concepts/polarization.md)
- [一维谐振子的水平集与焦散](../examples/harmonic-oscillator-level-set.md)

## 出处

- §5.2.2 半经典解的几何数据，p.267（PDF p.268），源码 `ch05a.tex:1000-1021`
- §5.2.3 定义 5.2.3（几何半经典定态），p.268（PDF p.269），源码 `ch05a.tex:1062-1068`
- §5.2.3 用 $\int\lambda$ 造相位，p.269（PDF p.270），源码 `ch05a.tex:1072-1098`
