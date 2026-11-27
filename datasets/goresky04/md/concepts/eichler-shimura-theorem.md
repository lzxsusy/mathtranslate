# Eichler–Shimura：$n=2$ 情形猜想的证明

> `goresky04/concept/eichler-shimura-theorem` · 轨道 C · 对应与障碍 · 状态 dev

> **先自测**：为什么 $n=2$ 时猜想可以被证明，证明用的是哪条上同调？

## 一句话

模曲线 $X$ 的平展上同调 $H^1_{\et}(X,\Ql)$ 分解为 Eisenstein 部分与尖点部分，尖点部分正好给出与 Hecke 特征形式对应的 $2$ 维 Galois 表示——这就是 $n=2$ 的朗兰兹对应。

## 定义

取 $X=\GL(2,\bbQ)Z(\bbA)\backslash\GL(2,\bbA)/\sO(2)K_{\mathrm f}$（模曲线）。Eichler 与 Shimura 证明：$X$ 上存在局部系数系 $E_k$（由权 $k$ 决定），使得 $H^1_P(X,E_k;\bbQ)\otimes\bbC\cong S_k\oplus\overline{S_k}$。于是每个归一化 Hecke 特征形式 $f\in S_k$ 对应 $H^1_{\et}(X,\Ql)$ 中的一个 $2$ 维 Galois 表示 $\rho_f$，并且 $L(\rho_f,s)=L(f,s)$。

**记号**：$H^1_P$ 记抛物上同调（parabolic cohomology）；$E_k$ 是权 $k$ 的局部系数系；$\overline{S_k}$ 是复共轭。

## 要点（为什么需要它）

1. 关键的几何事实：模曲线是**代数曲线**，所以它有平展上同调，上同调上带 Galois 作用。$n\ge3$ 时缺的正是这个几何对象。
2. 上同调分解成 Eisenstein 部分与尖点部分，尖点部分才对应自守表示；Eisenstein 部分对应的是诱导表示，不属于「漂亮」的那一类。
3. 证明是「构造性」的：它不只说存在对应，而是把对应具体写成「取上同调中的一个成分」，所以能逐素数验证 $L$ 函数相等。

## 核心公式

$$
$H^1_P(X,E_k;\bbQ)\otimes_{\bbQ}\bbC\cong S_k\oplus\overline{S_k}$  (7.1.1)$L(\rho_f,s)=L(f,s)=\prod_p(1-\lambda_pp^{-s}+p^{k-1-2s})^{-1}$
$$

$$
$L(\rho_f,s)=L(f,s)=\prod_p(1-\lambda_pp^{-s}+p^{k-1-2s})^{-1}$
$$

## 定理与证明（或缺口）

### Eichler–Shimura（$n=2$）

对每个归一化 Hecke 特征形式 $f\in S_k$，存在 $2$ 维 Galois 表示 $\rho_f\colon\Gal(\Qbar/\bbQ)\to\GL(2,\Ql)$，使 $L(\rho_f,s)=L(f,s)$；反之 $H^1_{\et}$ 的每个尖点成分都这样来。

> 证明状态：**sketch**。原文只给出 (7.1.1) 与结论，不提证明细节；完整证明见 [Sh1][K][M]。

出处：`A p.14`

## 常见误解

- 不要把 $H^1_{\et}(X,\Ql)$ 直接等同于 $S_k$：中间要乘 $\overline{S_k}$（复共轭），且要取抛物上同调（去掉 Eisenstein 部分）。
- $n=2$ 的成功依赖「模曲线是一维的」：$H^1$ 的秩 $2$ 与群 $\GL(2)$ 的维数 $2$ 恰好对上；对 $\GL(n)$ 需要 $n-1$ 维的簇，那是 Shimura 簇，只在少数情形存在。

## 相关卡

[Shimura 簇：$n=2$ 的几何载体](../concepts/shimura-variety.md) · [$n=2$：上同调分解给出 Galois 表示（(7.1.1)）](../derivations/eichler-shimura-decomposition.md) · [$n\ge3$ 的障碍：Shimura 簇不存在](../concepts/obstruction-n-ge-3.md)

## 出处（印刷页）

- A p.14（A p.14）

> 说明：对应原文 §7.1 的 (7.1.1) 与文字说明；证明四步是译者按 [Sh1][K] 的通行证明概括，原文未展开。
