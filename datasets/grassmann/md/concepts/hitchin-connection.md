# Hitchin 联络

> `grassmann/concept/hitchin-connection` · 轨道 1 · Hitchin 联络与 TQFT · 状态 draft

> **先自测**：Hitchin 联络为什么能保持全纯截面子丛 H^{(k)}，它的显式公式又是怎样从投影的变分算出来的？

## 一句话

保持全纯子丛的联络，由 Kähler 形式变分与预量子化数据显式给出，是 Verlinde 丛射影平坦性的来源。

## 定义

设 $\mathcal{H}^{(k)}=\mathcal{T}\times C^\infty(M,\mathcal{L}^k)$，$H^{(k)}\subset\mathcal{H}^{(k)}$ 是以 $H^0(M_\sigma,\mathcal{L}_\sigma^k)$ 为纤维的子丛。**Hitchin 联络**是 $\mathcal{H}^{(k)}$ 上的联络 $\hat\nabla$，满足 $$\hat\nabla_V=\hat\nabla_V^t+\frac{1}{4k+2n}\bigl\{\Delta_{G(V)}+2\nabla_{G(V)dF}+4kV'[F]\bigr\},$$ 其中 $\hat\nabla^t$ 是 $L^2$ 联络，$G(V)$ 由 $V'[I]=G(V)\omega$ 定义，$F$ 是 Ricci 势。

**记号约定**：$\Delta_{G(V)}$ 是 $G(V)$ 的 Laplace 算子；$\nabla_{G(V)dF}$ 是沿 $1$-形式 $G(V)dF$ 的协变导数。

## 要点（为什么需要它）

- 定理 5 的内容是 $\hat\nabla$ 保持 $H^{(k)}$；等价于式 (8) 的解 $u(V)$ 给出 $\hat\nabla=\hat\nabla^t-u(V)$。
- 显式公式的 $4k$ 项来自把 $\frac{1}{k+n/2}o(V)-V'[F]$ 通分，两个负号相消后才得到定理 5 的加号。
- 当 $M$ 是平坦联络模空间时 $\hat\nabla$ 射影平坦（ADW/Hitchin），这正是 Verlinde 丛射影平坦性的来源。
- 条件 $H^1(M,\mathbb{R})=0$ 用于把「恰当且 $(0,1)$ 型」的 1-形式判为零，这一步用到 $M$ 紧致。

## 关键公式

$$
\hat\nabla_V=\hat\nabla_V^t+\frac{1}{4k+2n}\bigl\{\Delta_{G(V)}+2\nabla_{G(V)dF}+4kV'[F]\bigr\}
$$

$$
\hat\nabla_V=\hat\nabla_V^t-u(V)
$$

## 定理与证明（或缺口）

### 定理 5（Andersen）

设 $I$ 是紧可预量子化辛流形 $(M,\omega)$ 上的刚性 Kähler 族，$c_1(M,\omega)=n[\omega/2\pi]\in H^2(M,\mathbb{Z})$ 且 $H^1(M,\mathbb{R})=0$。则上述 $\hat\nabla$ 保持子丛 $H^{(k)}\subset\mathcal{H}^{(k)}$。

**证明状态：提纲（有缺口）**


> **缺口**：证明归结为验证式 (8)；文中由引理 2、3、4 推出，但引理 2 与引理 4 的证明在 [A6]，本章只引用。缺口是这两个引理的逐项计算。


出处：中译 p.11（§1 定理 5），证明在 §2 p.17–18

## 易错点

- 漏掉 $\hat\nabla=\hat\nabla^t-u(V)$ 的负号：$u=-\frac{1}{4k+2n}\{\cdots\}$，写成 $+u$ 会使 $4kV'[F]$ 项反号。
- 把定理 5 的条件当成纯技术假设：没有刚性，$\Delta_{G(V)}$ 与 $\nabla_{G(V)dF}$ 的型分解不成立，式 (8) 无法逐项匹配。

## 相关卡

- [形式 Hitchin 联络](../concepts/formal-hitchin-connection.md)
- [刚性 Kähler 族](../concepts/rigid-kahler-family.md)
- [抛物丛与抛物次数](../concepts/parabolic-bundle.md)

## 出处

- ch1 §1 定理 5（一般框架）；中译 p.11（英文 PDF p.14），源码 `chapters/ch01.tex:165`
