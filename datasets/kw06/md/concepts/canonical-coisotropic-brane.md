# 典范余各向同性膜（c.c. 膜）

> `kw/concept/canonical-coisotropic-brane` · 轨道 E · Langlands 与翻译器 · 状态 dev

> **先自测**：典范余各向同性膜为什么叫“典范”，它凭什么把 A-膜翻译成 D-模？

## 一句话

空间充满的 rank-1 A-膜，曲率由几何唯一决定：$F=(\Im\tau)\omega_J$ 且 $(\omega^{-1}F)^2=-1$；开弦代数是微分算子，是 §11 的翻译器。

## 定义

典范余各向同性膜（c.c. 膜）是 $M_H(G,C)$ 上空间充满的 rank-1 A-膜，其 Chan–Paton 线丛曲率满足 $(\omega^{-1}F)^2=-1$。取 $\omega=(\Im\tau)\omega_K$ 时唯一解为 $F=(\Im\tau)\omega_J$，由 $I,J,K$ 唯一决定，故称典范。

**记号**：$\omega_I,\omega_J,\omega_K$：三个复结构对应的辛形式；$\tau$：$C$ 的模参数；$F$：Chan–Paton 线丛曲率。

## 要点（为什么需要它）

1. 它是 §11 的翻译器：开弦代数是 $K_M^{1/2}$ 上的微分算子，任意 A-膜借它得到 D-模。
2. “典范”指曲率没有连续自由度：一般组合 $a\omega_J+b\omega_I$ 因不恰当、周期非整被排除。
3. 它是 $(A,B,A)$-膜：$K,I$ 中是 A-膜，$J$ 中是 B-膜（曲率是 $(1,1)$ 型）。
4. 公式只在 $M_H$ 光滑部分定义，整体定义要靠规范理论边界条件（§12.4）。

## 核心公式

$$
$(\omega^{-1}F)^2=-1$$F=(\Im\tau)\omega_J,\qquad \alpha=\frac{\Im\tau}{2\pi}\int_C|\dd^2z|\,\mathrm{Tr}\left(\phi_z\delta A_{\bar z}+\phi_{\bar z}\delta A_z\right)$
$$

$$
$F=(\Im\tau)\omega_J,\qquad \alpha=\frac{\Im\tau}{2\pi}\int_C|\dd^2z|\,\mathrm{Tr}\left(\phi_z\delta A_{\bar z}+\phi_{\bar z}\delta A_z\right)$
$$

## 定理与证明（或缺口）

### c.c. 膜的曲率由几何唯一决定

满足 $(\omega^{-1}F)^2=-1$ 的空间充满 rank-1 A-膜在 $M_H$ 上只有 $F=\pm(\Im\tau)\omega_J$（相差定向）；一般解 $(\Im\tau)(a\omega_J+b\omega_I)$、$a^2+b^2=1$ 在 $b\ne0$ 时不恰当且周期非 $2\pi$ 整数倍，不能定义膜。

1. 条件 (11.1) 等价于 $\hat N=\omega^{-1}F$ 为近复结构，且 $\omega-\mathrm iF$ 全纯辛。
   - *为什么*：(11.1) 就是 $\hat N^2=-1$，配合 $F$ 闭得全纯性。
2. 故 $\omega$ 必须是某全纯辛形式的实部；在 $M_H$ 上取 $\omega=(\Im\tau)\omega_K$，则 $F=(\Im\tau)\omega_J$ 给出解。
   - *为什么*：该 $\omega$ 正是全纯辛形式的实部。
3. $\omega_J$ 在 $M_H$ 上恰当，故 $F=\dd\alpha$ 是平凡线丛上的曲率。
   - *为什么*：恰当形式的周期为零，可定义整体联络。
4. 一般解得 $b=0$：$b\ne0$ 时 $\omega-\mathrm iF$ 不恰当且周期非整。
   - *为什么*：否则线丛与联络不存在。

出处：`B p.185–186 eq (11.4)`

## 常见误解

- 把 c.c. 膜当成普通 Lagrange A-膜；它空间充满、rank 1，靠曲率满足 A-膜条件。
- 以为曲率可任选；恰当性与周期量子化把连续自由度排除，只剩符号与平坦扭。
- 把它在 $J$ 中说成 A-膜；c.c. 膜是 $(A,B,A)$。

## 相关卡

[A-膜](../concepts/a-brane.md) · [D-模](../concepts/d-module.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [典范参数 Ψ：定义、S 作用与消去 t](../derivations/canonical-parameter.md)

## 出处（印刷页）

- B p.185–187（B p.185 eq (11.1)）
- B p.191–195（B p.191–195）

> 说明：A=原文 p.185–187 的 (11.1)–(11.5) 与唯一性论证、p.191–195 的弦代数；B=把“典范”读成曲率无连续自由度；C=把四步整理成证明。
