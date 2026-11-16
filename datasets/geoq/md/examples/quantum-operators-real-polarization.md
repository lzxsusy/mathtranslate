# 实极化下 P-保持函数的量子化

> `geoq/example/quantum-operators-real-polarization` · 轨道 D · 几何量子化机器 · 状态 draft

> **这张卡练什么**：为什么位置表象里只剩「位置乘法 + 动量方向的导数」这两类算子？

## 一句话

在 R^{2n} 的竖直极化下，保持极化的函数恰为 a(x)+Σb_i(x)p_i；把它们代入 Q(f) 后动量项与刘维尔形式项相消，只剩 -iℏΣb_i∂_{x^i}+a(x)。

## 设定

相空间取 $\mathbb{R}^{2n}$，$\omega=\sum_idp_i\wedge dx^i$；预量子化线丛取平凡丛，$\theta=\sum_ip_idx^i$，$\nabla=d-\frac{i}{\hbar}\theta$（由 $d\theta=\omega$ 知曲率为 $-\frac{i}{\hbar}\omega$）；极化取 $P=\operatorname{Span}{\partial_{p_i}\}$，量子态是 $P$-极化截面 $\psi=\psi(\mathbf x)$。要算两件事：哪些 $f$ 保持 $P$，以及这些 $f$ 的 $Q(f)$ 在 $\psi(\mathbf x)$ 上的显式形式。

## 计算

**第 1 步**：写出哈密顿场 $V_f=\sum_i(\partial_{x^i}f\frac{\partial}{\partial p_i}-\partial_{p_i}f\frac{\partial}{\partial x^i})$，再与 $\partial_{p_k}$ 作李括号：$[\partial_{p_k},V_f]=\sum_i(\partial_{p_k}\partial_{x^i}f)\frac{\partial}{\partial p_i}-\sum_i(\partial_{p_k}\partial_{p_i}f)\frac{\partial}{\partial x^i}$。

> 为什么：第一项仍落在 $P$ 内（$P$ 由 $\partial_{p_i}$ 张成），只有含 $\partial_{x^i}$ 的第二项可能跑出 $P$，所以只需盯住它。

**第 2 步**：要求 $[\partial_{p_k},V_f]\in P$，等价于第二项的所有系数为零：$\partial_{p_k}\partial_{p_i}f=0$ 对一切 $i,k$ 成立；积分两次得 $f=a(\mathbf x)+\sum_ib_i(\mathbf x)p_i$。

> 为什么：$P$ 在每点只含 $p$ 方向，故 $x$ 方向的系数必须消失；「关于 $p$ 的二阶导为零」正是「关于 $p$ 至多一次」的解析说法。

**第 3 步**：算出 $\theta(V_f)=\sum_ip_idx^i(V_f)=-\sum_ip_ib_i(\mathbf x)$：因为 $V_f$ 的 $x$ 分量为 $-\partial_{p_i}f=-b_i$，而 $dx^i$ 只配对 $x$ 方向。

> 为什么：这一步决定 $Q(f)$ 里那个看似麻烦的 $\theta(V_f)$ 项；它恰好是一个动量的一次式，后面会与 $f$ 的动量项抵消。

**第 4 步**：对 $P$-极化 $\psi=\psi(\mathbf x)$ 有 $V_f\psi=-\sum_ib_i(\mathbf x)\partial_{x^i}\psi$（$\partial_{p_i}$ 方向作用在 $\psi$ 上为零），代入 $Q(f)=i\hbar(V_f-\frac{i}{\hbar}\theta(V_f))+f$ 得 $Q(f)\psi=i\hbar\cdot(-\sum_ib_i\partial_{x^i}\psi)+(\theta(V_f)+f)\psi$。

> 为什么：$i\hbar\cdot(-\frac{i}{\hbar}\theta(V_f))=+\theta(V_f)$；把两项拆开是为了让抵消看得清楚。

**第 5 步**：合并：$\theta(V_f)+f=-\sum_ip_ib_i+a+\sum_ib_ip_i=a(\mathbf x)$，动量一次式整体消去，最终 $Q(f)\psi=-i\hbar\sum_ib_i(\mathbf x)\frac{\partial\psi}{\partial x^i}+a(\mathbf x)\psi$。

> 为什么：抵消是必然的：$Q(f)\psi$ 必须仍是 $P$-极化截面，不能含 $p$；这也从另一个角度验证了命题 5.4.13。

## 结果

$Q(f)=-i\hbar\sum_{i=1}^nb_i(\mathbf x)\frac{\partial}{\partial x^i}+a(\mathbf x)$，其中 $f=a(\mathbf x)+\sum_ib_i(\mathbf x)p_i$。特例：$f=p_k$ 给 $-i\hbar\partial_{x^k}$，$f=x^k$ 给乘以 $x^k$，$f=1$ 给恒等算子。

## 复核

取 $f=p_1$ 与 $\psi=e^{ikx^1}$：$Q(f)\psi=-i\hbar(ik)\psi=\hbar k\psi$，与动量本征值相符。再验括号关系：$[Q(x^1),Q(p_1)]\psi=x^1(-i\hbar\partial_{x^1}\psi)-\big(-i\hbar\partial_{x^1}(x^1\psi)\big)=i\hbar\psi=i\hbar Q(\{x^1,p_1\})\psi$，与预量子化的 Q4 一致。最后换到水平极化 $P'$ 重算同一 $f$，得 $i\hbar c_i(\mathbf p)\partial_{p_i}+a(\mathbf p)$ 型的算子，经傅里叶变换与上式对应（$x$ 表象与 $p$ 表象的等价性）。

## 易错点

- $\theta(\partial_{p_i})=0$ 是整段计算能化简的关键：$\theta=\sum p_idx^i$ 只与 $x$ 方向配对。若把刘维尔形式误写成 $\sum x^idp_i$，竖直极化的解会变成动量函数，表象整体错位。
- $b_i(\mathbf x)p_i$ 的哈密顿场含 $x$ 方向分量，却仍然保持 $P$：P-保持的条件是 $[V_f,\Gamma(P)]\subset\Gamma(P)$，不是 $V_f\in\Gamma(P)$。
- 限制之后的算子未必自伴：$Q(b(\mathbf x)p_1)=-i\hbar b\partial_{x^1}$ 关于 $dx$ 的伴随多出 $-i\hbar b'$。自伴性要在 $L^2(M,\mathcal{L})_P$ 的内积下另行检查，不能从预量子化的自伴性直接继承。

## 用到哪些概念

- [量子算子与 P-保持条件](../concepts/quantum-operator.md)
- [极化：实极化与凯勒极化](../concepts/polarization.md)
- [量子希尔伯特空间与半形式修正](../concepts/quantum-hilbert-space.md)

## 相关卡

- [$\mathbb{R}^{2n}$ 的实极化与位置波函数](../examples/real-polarization-r2n.md)
- [凯勒极化、半形式与 $(n+\frac12)\hbar$ 谱](../examples/oscillator-half-form-spectrum.md)

## 出处

- §5.4.5 例 5.4.14，p.293–294（PDF p.294–295），源码 `ch05b.tex:1323-1361`
