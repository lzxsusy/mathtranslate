# Wilson 算子

> `kw/concept/wilson-operator` · 轨道 D · 二维、膜与算子 · 状态 dev

> **先自测**：Wilson 算子为什么只在 $\Psi=\infty$ 时拓扑不变，它作用在膜上的效果是什么？

## 一句话

规范理论的 order 算子 $\mathrm{Tr}_R P\exp(-\oint(A+\mathrm i\phi))$，在 $\Psi=\infty$ 处拓扑不变；作用在膜上即把 Chan–Paton 丛扭上 $E_q(R)$。

## 定义

Wilson 算子是沿曲面 $S$ 的 order 算子 $W(R,S)=\mathrm{Tr}_R P\exp(-\oint_S\mathcal A)$，在 $\Psi=\infty$（$t=\pm\mathrm i$）取 $\mathcal A=A+\mathrm i\phi$。此时 BPS 方程蕴含 $A$ 平坦，故 holonomy 与度规无关；它作用在膜上把 Chan–Paton 丛扭上 $E_q(R)$。

**记号**：$R$：$G$ 的表示；$S$：曲面（二维极限中是 $C$ 上的点）；$\mathcal A$：复化联络；$E_q(R)$：Wilson 线在点 $q$ 处决定的向量丛。

## 要点（为什么需要它）

1. 它是 order 算子，与 't Hooft 的 disorder 算子相对；S-对偶把两者互换。
2. 零膜是它的电特征膜，特征值取在一点纤维 $E_q(R)|_x$。
3. 所有 Wilson 算子的联合特征膜给出 $C$ 上的平坦丛，即局部系统。
4. $t=\pm\mathrm i$ 时 holonomy 与度规无关，这是它可以当作拓扑算子的原因。

## 核心公式

$$
$W(R,S)=\mathrm{Tr}_R\,P\exp\left(-\oint_S\mathcal A\right),\qquad \mathcal A=A+\mathrm i\phi\ \ (t=\mathrm i)$$W_q(R):\ \mathcal U\ \mapsto\ \mathcal U\otimes E_q(R)$
$$

$$
$W_q(R):\ \mathcal U\ \mapsto\ \mathcal U\otimes E_q(R)$
$$

## 定理与证明（或缺口）

### 零膜是电特征膜

在 $\Psi=\infty$ 的理论中，支撑在 $x\in M_H(G,C)$ 的零膜 $B_x$ 满足 $W_q(R)B_x\cong B_x\otimes E_q(R)|_x$，从而是所有 Wilson 算子的联合特征膜，特征值 $V=E_q(R)|_x$。

1. Wilson 算子作用在膜上把 Chan–Paton 丛 $U$ 换成 $U\otimes E_q(R)$。
   - *为什么*：这是 $W_q(R)$ 作为线算子对边界条件的定义。
2. 零膜的 Chan–Paton 丛是点 $x$ 处的摩天层 $U_x$。
   - *为什么*：零膜的支撑只是一个点。
3. 任何丛限制到点都平凡，故 $U_x\otimes E_q(R)\cong U_x\otimes E_q(R)|_x$。
   - *为什么*：张量积只依赖该点纤维，右端是固定向量空间，符合特征膜定义 $XB\simeq B\otimes V$。

出处：`B p.121 eq (8.10)`

## 常见误解

- 把 Wilson 算子当成固定 Hilbert 空间上的矩阵；它作用在膜上，特征值是向量空间或丛。
- 忽略 $\Psi=\infty$：一般 $\Psi$ 下 $A+\mathrm i\phi$ 的 holonomy 不是拓扑不变量。
- 把 order 与 disorder 弄反：Wilson 是 order，'t Hooft 是 disorder。

## 相关卡

['t Hooft 算子](../concepts/thooft-operator.md) · [特征膜（eigenbrane）](../concepts/eigenbrane.md) · [局部系统](../concepts/local-system.md) · [Wilson 与 't Hooft 线算子及其分类](../derivations/line-operators.md)

## 出处（印刷页）

- B p.79–80（B p.79 eq (6.1)）
- B p.121（B p.121 eq (8.10)）

> 说明：A=原文 p.79–80 的定义与 p.121 的零膜计算；B=$W_q(R)$ 作用即扭 $E_q(R)$ 的读出；C=把 (8.10) 读成“零膜是电特征膜”。
