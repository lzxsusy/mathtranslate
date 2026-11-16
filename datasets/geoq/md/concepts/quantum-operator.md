# 量子算子与 P-保持条件

> `geoq/concept/quantum-operator` · 轨道 D · 几何量子化机器 · 状态 draft

> **先自测**：为什么 Q(f) 不能对任意光滑函数都定义在量子希尔伯特空间上？P-保持条件在 R^{2n} 与 C^n 里各筛出哪些函数？

## 一句话

只有当哈密顿向量场把极化映回自身时，预量子化算子 Q(f)=iℏ∇_{V_f}+f 才把 P-极化截面送到 P-极化截面。实极化下这类函数是 a(x)+Σb_i(x)p_i，凯勒极化下是二次多项式。

## 定义

固定极化 $P$。若函数 $f$ 的哈密顿向量场 $V_f$ 保持 $P$ 的截面空间，即 $[V_f,\Gamma(P)]\subset\Gamma(P)$（等价地，任意 $X\in\Gamma(P)$ 都满足 $[V_f,X]\in\Gamma(P)$），则称 $f$ 为 $P$-保持函数，其全体记作 $C^\infty(M)_P$。对这类 $f$，量子算子定义为预量子化算子在极化态空间上的限制：$Q(f)=i\hbar\nabla_{V_f}+f$，定义域为 $L^2(M,\mathcal L)_P$。若 $f$ 不满足该条件，$Q(f)$ 会把一个极化态送出该极化，须另行处理。

**记号约定**：$V_f$ 由 $\iota_{V_f}\omega=df$ 确定（本书约定，与例 5.4.14 的显式公式一致）；$\nabla_f:=\nabla_{V_f}$；$Q$ 表示预量子化映射，限制到 $L^2(M,\mathcal{L})_P$ 后仍记作 $Q$。$C^\infty(M)_P$ 不是所有光滑函数，只是其中保持极化分布的一个子代数。

## 要点

- P-保持说的是「流把极化分布搬回自身」：条件里出现的是李括号 $[V_f,X]$，而不是要求 $V_f$ 本身落在 $P$ 里；两者差别很大，$b_i(\mathbf x)p_i$ 的哈密顿场就不在 $P$ 中。
- 命题 5.4.13 把这件事抬到算子层面：$f\in C^\infty(M)_P$ 时 $Q(f)$ 自动保持 $P$-极化性，因此可以无歧义地限制成量子希尔伯特空间上的算子。
- 实极化 $P=\operatorname{Span}{\partial_{p_i}\}$ 下，$C^\infty(\mathbb{R}^{2n})_P=\{a(\mathbf x)+\sum_ib_i(\mathbf x)p_i\}$：位置、动量的一次式都在内，$p_ip_j$ 与 $p_i^2$ 不在内。
- 凯勒极化、$K=|\mathbf z|^2$ 时，实值 P-保持函数是 $a+b_kz^k+\bar b_k\bar z^k+c_{k\bar j}z^k\bar z^j$，即关于 $z,\bar z$ 至多二次的多项式；谐振子 $\mathscr{H}=|z|^2$ 正落在这一类，所以全纯表示对二次哈密顿量特别好用。
- 对不保持 $P$ 的 $f$，哈密顿流会把 $P$ 搬到另一个极化 $P_t$；要比较两套量子希尔伯特空间，就得构造 BKS 核，这是几何量子化中真正困难的一半。

## 关键公式

$$
$[V_f,\Gamma(P)]\subset\Gamma(P)$
$$

$$
$C^\infty(M)_P=\{f\in C^\infty(M)\mid [V_f,P]\subset P\}$
$$

$$
$[\nabla_X,Q(f)]=i\hbar\nabla_{[X,V_f]},\qquad X\in\Gamma(P)$
$$

$$
$Q(f)=-i\hbar\sum_ib_i(\mathbf x)\frac{\partial}{\partial x^i}+a(\mathbf x),\qquad f=a+\sum_ib_ip_i$
$$

$$
$Q(f)=a+\sum_kb_kz^k+\hbar\sum_k(\bar b_k+c_{j\bar k}z^j)\frac{\partial}{\partial z^k}$
$$

## 定理与证明

### 命题 5.4.13：P-保持函数的量子化仍是 P-极化截面

设 $\psi\in\Gamma(M,\mathcal{L})$ 是 $P$-极化截面，$f\in C^\infty(M)_P$ 是 $P$-保持函数。则 $Q(f)\psi$ 仍是 $\mathcal{L}$ 的 $P$-极化截面，即 $\nabla_X(Q(f)\psi)=0$ 对一切 $X\in\Gamma(P)$ 成立。

**完整证明**

1. 先算交换子 $[\nabla_X,Q(f)]=[\nabla_X,i\hbar\nabla_{V_f}+f]=i\hbar[\nabla_X,\nabla_{V_f}]+X(f)$。
   - *为什么*：$f$ 是乘法算子，它与 $\nabla_X$ 的交换子作用在截面上等于 $X(f)$ 乘该截面；这一步把问题拆成「二阶项 + 一阶项」。
2. 用曲率恒等式 $[\nabla_X,\nabla_{V_f}]=\nabla_{[X,V_f]}+F_\nabla(X,V_f)$ 与 $F_\nabla=-\frac{i}{\hbar}\omega$，得 $i\hbar[\nabla_X,\nabla_{V_f}]=i\hbar\nabla_{[X,V_f]}+\omega(X,V_f)$。
   - *为什么*：系数 $i\hbar\cdot(-\frac{i}{\hbar})=1$，曲率项正好变成不帶 $\hbar$ 的 $\omega$ 值。
3. 由 $\iota_{V_f}\omega=df$ 得 $\omega(V_f,X)=X(f)$，故 $\omega(X,V_f)=-X(f)$，与第 1 步的 $X(f)$ 相消，于是 $[\nabla_X,Q(f)]=i\hbar\nabla_{[X,V_f]}$。
   - *为什么*：这一步是全部技巧所在：$f$ 的一阶导数既能看成乘法算子与导数的交换子，也能看成 $V_f$ 与 $X$ 的辛配对，二者必须相等，否则 $Q(f)$ 无法保持极化。
4. 对 $P$-极化 $\psi$ 用 Leibniz 法则：$\nabla_X(Q(f)\psi)=[\nabla_X,Q(f)]\psi+Q(f)\nabla_X\psi=i\hbar\nabla_{[X,V_f]}\psi$，因为 $\nabla_X\psi=0$。
   - *为什么*：这是「算子把定义域映回自身」的标准写法；第二项消失正是极化的定义。
5. $f$ 是 $P$-保持的，故 $[V_f,X]\in\Gamma(P)$，从而 $[X,V_f]=-[V_f,X]\in\Gamma(P)$；于是 $\nabla_{[X,V_f]}\psi=0$，即 $Q(f)\psi$ 仍 $P$-极化。
   - *为什么*：证明在此闭合：P-保持条件恰好补上最后一块，没有它第 4 步的结果是未知量。

来源：ch05b.tex:1282-1318（原书 p.290–293）

## 易错点

- P-保持不等于 $V_f\inP$：条件是 $[V_f,\Gamma(P)]\subset\Gamma(P)$。例 5.4.14 里 $f=b(\mathbf x)p_1$ 的哈密顿场含 $x$ 方向分量，却仍然保持竖直极化。
- 算子的定义域是 $L^2(M,\mathcal{L})_P$，只有 $f\in C^\infty(M)_P$ 时 $Q(f)$ 才把它映回自身；对一般 $f$ 硬套 $Q(f)$，结果是另一个极化下的截面，不是量子希尔伯特空间里的态。
- 自伴性不能想当然：$Q(b(x)p)=-i\hbar b(x)\partial_x$ 关于 $dx$ 的伴随是 $-i\hbar(b\partial_x+b')$，并不对称。预量子化在 $L^2(M,\mathcal{L})$ 上自伴，限制到极化截面后要重新验证；顺序歧义以这种形式重新出现。

## 相关卡

- [预量子化线丛](../concepts/prequantization.md)
- [极化：实极化与凯勒极化](../concepts/polarization.md)
- [量子希尔伯特空间与半形式修正](../concepts/quantum-hilbert-space.md)
- [哈密顿向量场与泊松括号](../concepts/hamiltonian-vector-field.md)
- [实极化下 P-保持函数的量子化](../examples/quantum-operators-real-polarization.md)
- [凯勒极化、半形式与 $(n+\frac12)\hbar$ 谱](../examples/oscillator-half-form-spectrum.md)

## 出处

- §5.4.5 定义 5.4.12 与命题 5.4.13，p.292–293（PDF p.293–294），源码 `ch05b.tex:1266-1321`
- §5.4.5 BKS 核与例 5.4.14–5.4.15，p.293–296（PDF p.294–297），源码 `ch05b.tex:1320-1465`
