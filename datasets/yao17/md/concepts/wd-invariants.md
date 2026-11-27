# Weil–Deligne 表示的导子 c(ρ)、L 因子与 ε 因子

> `yao17/concept/wd-invariants` · 轨道 Weil–Deligne 侧 · 状态 dev

> **先自测**：N 怎样进入导子、L 因子与 ε 因子的定义？为什么 ε 的显式因子只依赖 (ker N)^{I_K} 与 V^{I_K}/(ker N)^{I_K}？

## 一句话

c(ρ)=c(ρ')+dim V^{I_K}−dim(ker N)^{I_K}；L 与 ε 只用 (ker N)^{I_K} 与 V^{I_K}/(ker N)^{I_K} 上的 Frobenius 作用。

## 定义

设 $\rho=(\rho',N)$ 是 $W_K$ 的 Weil–Deligne 表示，$q=\#k$。(1) 导子 $c(\rho):=c(\rho')+\dim V^{I_K}-\dim(\ker N)^{I_K}$，其中 $c(\rho')$ 是 Artin 导子 $c(\chi_{\rho'})=\sum_i\frac{1}{[G_0:G_i]}(\dim V-\dim V^{G_i})$；(2) 取几何 Frobenius $\Phi$，$L(\rho,s):=\det\big(1-q^{-s}\Phi|_{(\ker N)^{I_K}}\big)^{-1}$；(3) $\epsilon(\rho,s,\psi):=q^{-(c(\rho)+n(\psi)\dim V)s}\cdot\det\big(-\Phi|_{V^{I_K}/(\ker N)^{I_K}}\big)\cdot\epsilon(\rho',\psi,dx)$。

**记号**：$G_i$ 是 $I_K$ 的第 $i$ 个分歧子群；$n(\psi)$ 是 $\psi$ 的导子指数；$\epsilon(\rho',\psi,dx)$ 是定理 1.3 对 $W_K$ 表示给的因子。

## 要点（为什么需要它）

1. N 的作用被「夹在 $I_K$-不变量与 $\ker N$ 之间」：导子只数 $V^{I_K}$ 比 $(\ker N)^{I_K}$ 多出的部分，L 因子只看 $(\ker N)^{I_K}$，$\epsilon$ 的显式行列式因子只在商 $V^{I_K}/(\ker N)^{I_K}$ 上。
2. 推论 1.4 把这个定义压成一行：$\epsilon(\rho,s,\psi)=q^{-(c(\rho)+n(\psi)\dim V)s}\epsilon(\rho,0,\psi)$，即 $\epsilon$ 关于 $s$ 是纯指数——这正是 §3.6 里 JPPS 公式的来源。
3. 对 $\rho'$ 用 Artin 导子公式时，$\dim V-\dim V^{G_i}$ 的权 $1/[G_0:G_i]$ 是 Artin 的原始归一化；底本在 Remark 里把它和 $\epsilon$ 的指数因子并排写出，正是为了说明两者指数相同。
4. 当 $(\rho,N)$ 来自 $\ell$ 进表示时，这套 $c,L,\epsilon$ 与定理 1.3 给 $\rho'$ 的因子相容——所以 LLC 的性质 (2) 可以直接在这套量上陈述。

## 核心公式

$$
$c(\rho)=c(\rho')+\dim V^{I_K}-\dim(\ker N)^{I_K}$$L(\rho,s)=\det\big(1-q^{-s}\Phi|_{(\ker N)^{I_K}}\big)^{-1}$$\epsilon(\rho,s,\psi)=q^{-(c(\rho)+n(\psi)\dim V)s}\det\big(-\Phi|_{V^{I_K}/(\ker N)^{I_K}}\big)\epsilon(\rho',\psi,dx)$$\epsilon(\rho,s,\psi)=q^{-(c(\rho)+n(\psi)\dim V)s}\epsilon(\rho,0,\psi)$
$$

$$
$L(\rho,s)=\det\big(1-q^{-s}\Phi|_{(\ker N)^{I_K}}\big)^{-1}$
$$

$$
$\epsilon(\rho,s,\psi)=q^{-(c(\rho)+n(\psi)\dim V)s}\det\big(-\Phi|_{V^{I_K}/(\ker N)^{I_K}}\big)\epsilon(\rho',\psi,dx)$
$$

$$
$\epsilon(\rho,s,\psi)=q^{-(c(\rho)+n(\psi)\dim V)s}\epsilon(\rho,0,\psi)$
$$

## 定理与证明（或缺口）

### 推论 1.4

$\epsilon(\rho,s,\psi)=q^{-(c(\rho)+n(\psi)\dim V)s}\epsilon(\rho,0,\psi)$。

1. 把 $\epsilon(\rho,s,\psi)$ 的定义代入，只需认出显式因子 $q^{-(c(\rho)+n(\psi)\dim V)s}$ 之外的部分正是 $s=0$ 时的表达式。
   - *为什么*：定义里只有指数因子带 $s$；$\det(-\Phi|_{\cdot})$ 与 $\epsilon(\rho',\psi,dx)$ 都与 $s$ 无关。
2. 故 $\epsilon(\rho,s,\psi)=q^{-(c(\rho)+n(\psi)\dim V)s}\cdot\epsilon(\rho,0,\psi)$。
   - *为什么*：底本称其为「从定义直接读出的平凡推论」（Corollary）。

出处：`A §1.1.11 p.7`

## 常见误解

- 这里用的是「几何 Frobenius」$\Phi$；若换成算术 Frobenius，$L$ 因子里的 $q^{-s}$ 要改成 $q^{s}$，符号会翻转。
- $c(\rho)$ 里第二项是 $\dim V^{I_K}-\dim(\ker N)^{I_K}$，不是 $\dim V-\dim\ker N$；$I_K$-不变子空间这一限制不能省，否则与 $\ell$ 进侧不兼容。

## 相关卡

[Tate 的局部 L 因子与 ε 因子、定理 1.3 的存在唯一性](../concepts/tate-epsilon.md) · [Weil–Deligne 表示 (ρ, N) 及其基本性质](../concepts/wd-representation.md) · [导子 c(π)、深度、JPPS 的 ε 公式与深度 0 对照图](../concepts/conductor-depth.md) · [局部 Langlands 对应：定理 2.13 的五条性质](../concepts/llc-statement.md)

## 出处（印刷页）

- A p.7（A p.7）

> 说明：(1)–(3) 与推论 1.4 逐条照 p.7；Artin 导子公式见 p.6 Remark；key_points 中「N 的作用被夹在…之间」是我们的概括。
