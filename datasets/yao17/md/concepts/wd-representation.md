# Weil–Deligne 表示 (ρ, N) 及其基本性质

> `yao17/concept/wd-representation` · 轨道 Weil–Deligne 侧 · 状态 dev

> **先自测**：Weil–Deligne 表示的定义里 N 的相容条件为什么会迫使 N 幂零？半单的 (ρ,N) 为什么一定是 Sp_m(r) 的直和？

## 一句话

(ρ,N) 中 ρ 是 I_K 上有限像的连续表示，N 满足 σNσ^{-1}=q^{-v_K(σ)}N；N 必幂零，半单情形下 (ρ,N)≅⊕Sp_m(r)。

## 定义

设 $L$ 特征 0，$V$ 是有限维 $L$-向量空间。$W_K$ 上的 Weil–Deligne 表示是一对 $(\rho,N)$：(1) $\rho$ 是 $W_K$ 的连续表示（$L$ 上离散拓扑，等价于 $\rho(I_K)$ 有限像）；(2) $N\in\End(V)$ 满足 $\sigma N\sigma^{-1}=q^{-v_K(\sigma)}N$，其中 $v_K$ 由 $\sigma\mapsto\operatorname{Frob}_K^{v_K(\sigma)}\in W_K/I_K\xrightarrow{\sim}\operatorname{Frob}^{\mathbb Z}$ 定义。态射是兼容 $N$ 的表示态射，由此得到范畴 $\wd=\wd_L(W_K)$。

**记号**：对 Frobenius 提升 $\phi\in W_K$，条件化为 $\phi N\phi^{-1}=q^{-1}N$；$V(-1)$ 记 $V$ 用非分歧特征标 $\epsilon\colon G_K\to L^\times$（$\phi\mapsto q$）的扭转。

## 要点（为什么需要它）

1. N 幂零是「算出来」的：特征多项式满足 $f(X)=\det(XI_n-N)=\det(XI_n-q^{-1}N)=q^{-n}f(qX)$，比较次数与首项迫使 $f(X)=X^n$。
2. N 不是 Galois 等变的，但它给出一个 Galois 等变的映射 $N(-1)\colon V\to V(-1)$——这是把「Frobenius 把 N 缩放 $q^{-1}$」翻译成「N 降低一个 Tate 扭转」的正确写法。
3. $\Sp_m(r)=r\oplus r(1)\oplus\dots\oplus r(m-1)$，$N$ 把 $r(i)$ 同构送到 $r(i+1)$、在 $r(m-1)$ 上为 0；等价地 $N(-1)$ 在 $r\oplus\dots\oplus r(m-2)$ 上是恒等、在 $r(m-1)$ 上是 0。
4. 对 $N$ 的幂零指数做归纳可得：$\rho$ 半单时 $(\rho,N)\cong\bigoplus_i\Sp_{m_i}(r_i)$，$r_i$ 是不可约表示且 $r_i(I_K)$ 有限。这是「$\wd$ 里的对象 = Steinberg 块的直和」的原型。
5. 张量积 $(\rho_1\otimes\rho_2,\ N_1\otimes\mathrm{id}+\mathrm{id}\otimes N_2)$；$\Hom(\rho_1,\rho_2)$ 上 $N\phi=N_2\phi-\phi N_1$，即 $\wd$ 是张量范畴。

## 核心公式

$$
$\sigma N\sigma^{-1}=q^{-v_K(\sigma)}N,\qquad \phi N\phi^{-1}=q^{-1}N$$\Sp_m(r)=r\oplus r(1)\oplus\dots\oplus r(m-1)$$(\rho,N)\ \text{半单}\ \Longrightarrow\ (\rho,N)\cong\bigoplus_i\Sp_{m_i}(r_i)$$(\rho_1\otimes\rho_2,\ N_1\otimes\mathrm{id}+\mathrm{id}\otimes N_2)$
$$

$$
$\Sp_m(r)=r\oplus r(1)\oplus\dots\oplus r(m-1)$
$$

$$
$(\rho,N)\ \text{半单}\ \Longrightarrow\ (\rho,N)\cong\bigoplus_i\Sp_{m_i}(r_i)$
$$

$$
$(\rho_1\otimes\rho_2,\ N_1\otimes\mathrm{id}+\mathrm{id}\otimes N_2)$
$$

## 常见误解

- 「$\rho$ 连续」在底本的约定里等价于「$\rho(I_K)$ 有限」，因为 $W_K$ 的拓扑不是子空间拓扑；若按一般拓扑群定义会把条件想放松。
- $\wd$ 的半单对象不是「$\rho$ 半单」的对象：$\wd$ 的半单对象是那些 $N=0$ 且 $\rho$ 半单的；$\rho$ 半单但 $N\neq 0$ 的 $\Sp_m(r)$ 是「$\phi$-半单但非半单」。

## 相关卡

[Weil 群 W_K、惯性群、野惯性群与驯特征标](../concepts/weil-group.md) · [φ-半单（Frobenius 半单）与引理 1.2](../concepts/frobenius-semisimple.md) · [Weil–Deligne 表示的导子 c(ρ)、L 因子与 ε 因子](../concepts/wd-invariants.md) · [Grothendieck 单值化定理、WD 函子与惯性类型](../concepts/wd-functor.md)

## 出处（印刷页）

- A p.3（A p.3）

> 说明：定义与基本性质 (1)–(4)、张量积与 Hom 取自 p.3 的 1.1.3–1.1.4 与 p.5 的 1.1.7；「N 幂零是算出来的」等解释是我们的判断。
