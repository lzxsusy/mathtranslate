# 形式 Hitchin 联络

> `grassmann/concept/formal-hitchin-connection` · 轨道 1 · Hitchin 联络与 TQFT · 状态 draft

> **先自测**：为什么存在唯一的形式联络，使每个 Toeplitz 族都成为它的渐近协变常截面？

## 一句话

Teichmüller 空间上取值于形式微分算子环的联络，由 Toeplitz 族的渐近协变常性唯一确定。

## 定义

设 $\mathcal{D}(M)$ 为 $M$ 上光滑微分算子空间，$\mathcal{D}_h(M)=\mathcal{D}(M)[[h]]$，$C_h^\infty(M)=C^\infty(M)[[h]]$。$\mathcal{T}$ 上 $C_h$ 中的**形式联络**是映射 $D$，对 $f\in C_h^\infty(M)$ 与向量场 $V$ 给出 $$D_Vf=V[f]+\tilde D(V)(f),$$ 其中 $\tilde D$ 是 $\mathcal{T}$ 上取值于 $\mathcal{D}_h(M)$ 的光滑 1-形式，$\tilde D(V)=\sum_{l\ge0}\tilde D^{(l)}(V)h^l$。

**记号约定**：$\tilde D$ 不是张量（它取值在微分算子中），故 $D$ 不是通常意义的联络；$h$ 是形式参数。

## 要点（为什么需要它）

- $\tilde D$ 取值于微分算子，这使 $D$ 能作用于任意 $f$ 而不只是截面，故称「形式」联络。
- 定理 6 断言存在唯一 $D$ 使 Toeplitz 族渐近协变常；它由 Hitchin 联络在 $\operatorname{End}(\mathcal{H}^{(k)})$ 中的诱导联络唯一决定。
- 规范条件 $\tilde D=0\bmod h$ 只固定零阶项，高阶项 $\tilde D^{(l)}$ 一般非零。
- 展开参数是 $(k+n/2)^{-1}$ 而非 $k^{-1}$，故 $D$ 的 $h$ 与 Toeplitz 展开的 $h$ 差一个标号平移。

## 关键公式

$$
D_Vf=V[f]+\tilde D(V)(f)
$$

$$
\tilde D(V)=\sum_{l\ge0}\tilde D^{(l)}(V)h^l
$$

## 定理与证明（或缺口）

### 定理 6（Andersen）

存在唯一的形式联络 $D$，使对所有 $f$ 与 $V$ 有 $\hat\nabla_V^eT_f^{(k)}\sim T_{D_Vf}^{(k)}$（按 $(k+n/2)^{-1}$ 展开），且 $\tilde D=0\bmod h$。

**证明状态：只引出处，原书不重证**


出处：中译 p.12（§1 定理 6，证明在 [A6]）

## 易错点

- 把 $\tilde D=0\bmod h$ 误读成 $D$ 平凡：零阶项确为 $V[f]$，但高阶项正是 Hitchin 联络曲率的编码。
- 把定理 6 的 $h$ 当 $k^{-1}$ 直接与定理 10 的 $c^{(l)}$ 相乘：两套展开的标号差 $\phi(h)=2h/(2+nh)$，混用会错位一阶系数。

## 相关卡

- [形式平凡化](../concepts/formal-trivialization.md)
- [Hitchin 联络](../concepts/hitchin-connection.md)
- [抛物丛与抛物次数](../concepts/parabolic-bundle.md)

## 出处

- ch1 §1 形式联络的定义；中译 p.12（英文 PDF p.15），源码 `chapters/ch01.tex:175`
