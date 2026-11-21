# 仿射 Grassmannian $\Gr$

> `hausel22/concept/affine-grassmannian` · 轨道 E · 仿射 Grassmannian 与重数代数 · 状态 dev

> **先自测**：为什么 Hecke 修改要用仿射 Grassmannian 而不是普通 Grassmannian？

## 一句话

$\Gr=\GL_n((z))/\GL_n[[z]]$ 是按支配权分层的射影 ind 概形；极小权 $\omega_k$ 的层就是经典 Grassmann 簇。

## 定义

设 $\Gr:=\GL_n((z))/\GL_n[[z]]$，是射影 ind 概形。对支配权 $\mu$，轨道 $\Gr^\mu:=\GL_n[[z]]\cdot z^\mu$ 满足 $\Gr^\mu\to\GL_n[z^\mu]\cong\GL_n/P_\mu$，且闭包按支配序分层：$\overline{\Gr}^\mu=\coprod_{\mu\ge\lambda\in P^+}\Gr^\lambda$（式 (3.4)）。当 $\mu=\omega_k$ 是极小的第 $k$ 个基本权时 $\overline{\Gr}^{\omega_k}=\Gr^{\omega_k}\cong\Gr(k,n)$，即经典 Grassmann 簇。

**记号**：$\Gr$；$\Gr^\mu$；$\overline{\Gr}^\mu$；$\GL_n[[z]]$；支配序；$\omega_k$。

## 要点（为什么需要它）

1. $\Gr$ 是 ind 概形（可数并），不是有限型概形；每个 $\overline{\Gr}^\mu$ 才是射影簇。
2. 分层按支配序：$\mu\ge\lambda$ 指 $\mu-\lambda$ 是正根之和；闭包取「向下」的所有层。
3. 极小权给出经典的 $\Gr(k,n)$，这是一切计算能落到 Grassmann 上做的原因（式 (3.2) 与定理 3.10）。
4. Hecke 修改正是在 $\Gr^\mu$ 中选 $[g]$，把 $\Phi_a|_{\Delta_c}$ 的共轭条件写成仿射 Springer 纤维条件 $\gamma_a g^{-1}\in\gl_n[[z]]$（式 (3.6)）。

## 核心公式

$$
$$\Gr=\GL_n((z))/\GL_n[[z]],\qquad \overline{\Gr}^\mu=\coprod_{\mu\ge\lambda\in P^+}\Gr^\lambda$$$$\overline{\Gr}^{\omega_k}=\Gr^{\omega_k}\cong\Gr(k,n)$$
$$

$$
$$\overline{\Gr}^{\omega_k}=\Gr^{\omega_k}\cong\Gr(k,n)$$
$$

## 定理与证明（或缺口）

### 支配序分层（式 (3.4)）

$\overline{\Gr}^\mu=\coprod_{\mu\ge\lambda\in P^+}\Gr^\lambda$，其中 $\mu\ge\lambda$ 指 $\mu-\lambda$ 为若干正根之和（可带重数）。

> 证明状态：**sketch**。原文直接使用这个分层，未给证明。

出处：`A p.2242 eq (3.4)`

## 常见误解

- $\Gr$ 不是射影簇而是 ind 概形；说「$\Gr$ 同构于某个射影簇」是错的，只有 $\overline{\Gr}^\mu$ 是射影的。
- 支配序的方向：$\mu\ge\lambda$ 是 $\mu-\lambda$ 为正根之和，闭包取「小于等于 $\mu$」的层，不要反。
- $\Gr^{\omega_k}\cong\Gr(k,n)$ 只对极小权成立；一般 $\mu$ 的 $\Gr^\mu$ 是部分旗簇的仿射版本，不是 Grassmann。
- Hecke 修改用 $\GL_n((z))$（形式 Laurent 级数）而不是 $\GL_n[[z]]$；写成后者会让 $z^\mu$ 不可逆。

## 相关卡

[jet 概形 $J_d(X)$](../concepts/jet-scheme.md) · [局部重数代数 $Q_\calE$](../concepts/local-multiplicity-algebra.md) · [Hecke 修改把仿射 Grassmannian 嵌入上行流](../derivations/hecke-to-wobbly.md)

## 出处（印刷页）

- A p.2241–2242（A p.2242 eq (3.4)）
- A p.2242（A p.2242 eq (3.3)）

> 说明：A=原文 §3.3 的定义、式 (3.3)(3.4) 与极小权的例子；B=把「轨道 → 闭包 → Grassmann」的逻辑补出来；C=「ind 概形 vs 射影簇」的提醒是我们加的。最没把握处：$\Gr^\mu\to\GL_n[z^\mu]$ 的记号原文写作 $\GL_n[z^\mu]$，其确切含义（$\mu$ 决定的抛物子群）未展开。
