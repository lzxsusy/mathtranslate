# 导子 c(π)、深度、JPPS 的 ε 公式与深度 0 对照图

> `yao17/concept/conductor-depth` · 轨道 分类与不变量 · 状态 dev

> **先自测**：§3.5 的对照图用五条 ⇔ 把自守侧与 Galois 侧的「分歧程度」逐级对应，各条的依据分别是什么？

## 一句话

ε(π,s,ψ)=q^{−(c(π)+n·n(ψ))s}ε(π,0,ψ)；深度 0 的 π 对应驯分歧的 r_n(π)，非分歧对应 ρ|I_K=0 且 N=0。

## 定义

对光滑不可约 $\pi$，令 $L(\pi,s)$、$\epsilon(\pi,s,\psi)$ 为 $\pi'$ 取平凡特征标时的因子。JPPS 定理（及其修正）：$\epsilon(\pi,s,\psi)=q^{-(c(\pi)+n\cdot n(\psi))s}\epsilon(\pi,0,\psi)$，其中 $c(\pi)$ 是 §3.4 定义的导子；底本指出文献中两种导子定义（§3.4 的与由 $L(\pi,s)$ 函数方程定义的）一致。引理 3.8：在 LLC 下 $c(\pi)=c(\rec_n(\pi))$。§3.5 对照图：$\pi$ 非分歧 $\iff\pi^K\neq0$；$r_n(\pi)$ 非分歧 $\iff\rho|_{I_K}=0$ 且 $N=0$；$\pi$ Iwahori-球面 $\iff\pi^{\Iw}\neq0$；$\rec_n(\pi)$ 为 $I_K$-球面 $\iff\rho|_{I_K}=0$；$\pi$ 深度 0 $\iff$ $r_n(\pi)$ 驯分歧。

**记号**：$K=\GL_n(\mathcal O_K)$，$\Iw=B_0$ 是 Iwahori 子群（约化模 $\Bbbk$ 的标准 Borel 的原像）；$r_n=\WD^{-1}\circ\rec_n$ 是 $\ell$ 进表示；$n=n$ 表示 $\dim\pi$。

## 要点（为什么需要它）

1. 引理 3.8 的证明是「比较指数」：由 $\epsilon$ 相容性 $\epsilon(\pi,\psi,s)=\epsilon(\rec_n(\pi),\psi,s)$，再用推论 1.4 把两侧都写成 $q^{-(\cdot)s}$，比较指数即得 $c(\pi)=c(\rec_n(\pi))$。
2. 对照图的三级结构很值得记：非分歧（$K$-固定）对应 $\rho|_{I_K}=0$ 且 $N=0$；Iwahori-球面对应「$I_K$ 上平凡但 $N$ 可非零」（$I_K$-球面）；深度 0 对应驯分歧（$\rho|_{P_K}$ 的像落在更小群，且 $N$ 无约束）。
3. 深度概念由 Moy–Prasad 引入，底本在 §2.3.1 的 Remark 里就把它与导子并列为 LLC 保持的两大量；§3.4「导子与新向量」与 §3.5.1「导子与深度」在底本里都只留标题，正文空缺。
4. JPPS 公式的形式与推论 1.4 完全同构：一侧是 $c(\rho)+n(\psi)\dim V$，一侧是 $c(\pi)+n\cdot n(\psi)$——所以「导子守恒」几乎是这个形式对应的直接推论。

## 核心公式

$$
$\epsilon(\pi,s,\psi)=q^{-(c(\pi)+n\,n(\psi))s}\,\epsilon(\pi,0,\psi)$$c(\pi)=c(\rec_n(\pi))\quad(\text{LLC 下})$$\pi\ \text{非分歧}\iff\pi^K\neq0,\qquad r_n(\pi)\ \text{非分歧}\iff\rho|_{I_K}=0\ \&\ N=0$$\pi\ \text{深度}\ 0\iff r_n(\pi)\ \text{驯分歧}$
$$

$$
$c(\pi)=c(\rec_n(\pi))\quad(\text{LLC 下})$
$$

$$
$\pi\ \text{非分歧}\iff\pi^K\neq0,\qquad r_n(\pi)\ \text{非分歧}\iff\rho|_{I_K}=0\ \&\ N=0$
$$

$$
$\pi\ \text{深度}\ 0\iff r_n(\pi)\ \text{驯分歧}$
$$

## 定理与证明（或缺口）

### 引理 3.8（导子被 LLC 保持）

在 LLC 下 $c(\pi)=c(\rec_n(\pi))$。

1. 取 $\pi'$ 为平凡特征标，由 LLC 性质 (2) 的 $\epsilon$ 相容性得 $\epsilon(\pi,\psi,s)=\epsilon(\rec_n(\pi),\psi,s)$。
   - *为什么*：这是定理 2.13(2) 在 $n_2=0$（平凡特征标）时的特例。
2. 两侧分别用 JPPS 公式与推论 1.4 写成 $q^{-(c(\pi)+n n(\psi))s}\epsilon(\pi,0,\psi)$ 与 $q^{-(c(\rec_n\pi)+n n(\psi))s}\epsilon(\rec_n\pi,0,\psi)$。
   - *为什么*：两个公式的指数结构相同，故可直接比较。
3. 比较 $s$ 的系数得 $c(\pi)=c(\rec_n(\pi))$。
   - *为什么*：$q\neq1$，指数相等即系数相等。

出处：`A §3.6.4 p.31`

## 常见误解

- $n(\psi)$（加性特征标的导子指数）与 $n=\dim\pi$ 在 JPPS 公式里并排出现，容易把 $n\,n(\psi)$ 误读成向量；它是标量乘积。
- 「$\pi$ 深度 0 $\iff$ $r_n(\pi)$ 驯分歧」这一条里 $r_n$ 是 $\ell$ 进表示（$\rho$ 的半单化），不是 $\rec_n(\pi)$ 本身；对 $\rec_n(\pi)$ 说「驯分歧」需要先取 $\WD^{-1}$。

## 相关卡

[Weil–Deligne 表示的导子 c(ρ)、L 因子与 ε 因子](../concepts/wd-invariants.md) · [局部 Langlands 对应：定理 2.13 的五条性质](../concepts/llc-statement.md) · [深度 0 的五条等价链：从 π^K ≠ 0 一路推到 N = 0](../derivations/depth-zero-chain.md) · [球面 Hecke 代数与 Satake 同构、非分歧表示](../concepts/satake.md)

## 出处（印刷页）

- A p.30–31（A p.30）

> 说明：深度 0 对照图五条取自 p.30 的 §3.5；JPPS 公式与「两种导子定义一致」见 p.30 §3.6.3；引理 3.8 与其证明见 p.31。§3.4/§3.5.1/§3.6 的正文在底本中空缺（只留标题），已在译本照实标注。
