# 形式平凡化

> `grassmann/concept/formal-trivialization` · 轨道 1 · Hitchin 联络与 TQFT · 状态 draft

> **先自测**：形式联络平坦时，为什么可以把它的平行移动写成算子值形式幂级数 P，并让它逐阶满足 D_V(P(f))=0？

## 一句话

把形式联络的平坦性积分成算子值映射 P：模 h 为恒等，且沿任意方向作用在 P(f) 上为零。

## 定义

**形式平凡化**是从 $\mathcal{T}$ 到 $\mathcal{D}_h(M)$ 的光滑映射 $P$，满足 $P\equiv\operatorname{Id}\pmod h$，且对所有向量场 $V$ 与 $f\in C_h^\infty(M)$ 有 $$D_V\bigl(P(f)\bigr)=0.$$ 若还有 $P(\varphi(\sigma))=\varphi^*P(\sigma)$（$\varphi\in\Gamma$），称 $P$ 为 $\Gamma$-等变的。

**记号约定**：$\Gamma$ 是 $\Sigma$ 的映射类群；$\varphi^*$ 表示 $\varphi$ 在微分算子上的拉回作用。

## 要点（为什么需要它）

- $P$ 是算子值映射而非 $M$ 上的函数：它把每个 $f$ 送成一个形式微分算子 $P(f)$。
- 命题 1：$D$ 平坦且 $\tilde D=0\bmod h$ 时局部存在；$H^1(\mathcal{T},\mathbb{R})=0$ 时整体存在；$H^1_\Gamma(\mathcal{T},\mathcal{D}(M))=0$ 时可取 $\Gamma$-等变。
- 等变形式平凡化在相差形式常数的意义下唯一（$M$ 的映射类群不变函数只有常数）。
- 定理 7 给出一阶项 $P_\sigma^{(1)}(f)=\frac14\Delta_\sigma(f)+i\nabla_{X_F''}(f)$，但 §4 命题 3 的推导给出相反符号（译注 872）。

## 关键公式

$$
D_V\bigl(P(f)\bigr)=0,\qquad P\equiv\operatorname{Id}\pmod h
$$

$$
P_\sigma^{(1)}(f)=\tfrac14\Delta_\sigma(f)+i\nabla_{X_F''}(f)
$$

## 定理与证明（或缺口）

### 定理 7（一阶形式平凡化）

映射类群等变形式平凡化在一阶存在，且 $P_\sigma^{(1)}(f)=\frac14\Delta_\sigma(f)+i\nabla_{X_F''}(f)$，其中 $X_F''$ 是 Ricci 势的 Hamilton 向量场的 $(0,1)$ 部分。

**证明状态：提纲（有缺口）**


> **缺口**：§4 命题 3 只推出 $P=\operatorname{Id}-h(\frac14\Delta+i\nabla_{X_F''})+O(h^2)$，与定理 7 印刷的加号相反，译注 872 认为按推导应带负号。缺口是把两处符号统一，并补出 $P^{(2)}$ 以上各阶的存在性。


出处：中译 p.13（§1 定理 7）与 p.26（§4 命题 3）

## 易错点

- 把 $P$ 当成 $M$ 上的函数 $P(f)=f+\cdots$：它是算子值形式幂级数，$P^{(1)}$ 是二阶算子 $\frac14\Delta+i\nabla_{X_F''}$。
- 忽略定理 7 与命题 3 的符号冲突而直接引用 $+\frac14\Delta$：按 §4 推导应是 $-\frac14\Delta-i\nabla_{X_F''}$，符号用反会使一阶星积项整体反号。

## 相关卡

- [形式 Hitchin 联络](../concepts/formal-hitchin-connection.md)
- [Hitchin 联络](../concepts/hitchin-connection.md)
- [等平凡族 / 簇的形式](../concepts/isotrivial-family.md)

## 出处

- ch1 §1 形式平凡化的定义；中译 p.12（英文 PDF p.15），源码 `chapters/ch01.tex:213`
