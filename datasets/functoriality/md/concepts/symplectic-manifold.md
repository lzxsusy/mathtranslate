# 辛流形

> `functoriality/concept/symplectic-manifold` ｜ track A ｜ draft

**一句话**：辛流形是带闭且非退化 2-形式的偶维光滑流形；余切丛与射影代数簇给出基本例子，Darboux 定理说明它没有局部不变量。

**自测**：为什么辛流形要求 $\omega$ 既闭又非退化，这两个条件各自锁定什么结构？

## 定义

辛流形 $(M^{2n},\omega)$ 是光滑偶维流形，$\omega\in\Omega^2(M;\R)$ 是闭 2-形式（$d\omega=0$）且逐点非退化：其最高次外幂 $\omega^{\wedge n}$ 处处非零，从而是 $M$ 的体积形式。非退化等价于 $\omega$ 在每点切空间上给出非退化双线性型，于是 $X\mapsto\omega(X,\cdot)$ 是 $TM\to T^*M$ 的丛同构，这也迫使 $\dim M=2n$。辛同胚是满足 $\varphi^*\omega_N=\omega_M$ 的微分同胚 $\varphi:M\to N$。

记号：$M^{2n}$ 强调维数偶数；$\omega_0$ 记 Darboux 形式，$\omega_{\mathrm{can}}$ 记余切丛的典范形式，$\omega_{\mathrm{FS}}$ 记 Fubini–Study 形式。

## 要点

- 非退化性把 $TM$ 与 $T^*M$ 等同，因此辛流形自动带相容殆复结构与定向；这是 §2.1 用殆复结构定义条带的先决条件。
- 闭性 $d\omega=0$ 使 Cartan 公式成立，哈密顿向量场与哈密顿微分同胚才有定义，Floer 定理里的「$\varphi$ 为哈密顿微分同胚」正是靠它。
- 基本例子有三类：$\R^{2n}$ 的 $\omega_0$、余切丛 $T^*Q$ 上的 $\omega_{\mathrm{can}}$、射影空间的 Fubini–Study 形式；Kähler 性限制到复子流形仍保持，所以射影代数簇都是紧辛流形。
- Darboux 定理说明任意点附近都辛同胚于 $\C^n$ 原点附近，辛几何没有局部不变量；刚性只能来自伪全纯曲线，而不是曲率之类的局部量。

## 公式

$$\left(\R^{2n},\omega_0\coloneqq\sum_{i=1}^n dp_i\wedge dq_i\right),$$
$$\left(T^*Q,\omega_{\mathrm{can}}\coloneqq\sum_{i=1}^n dp_i\wedge dq_i\right).$$
$$\omega_0\coloneqq\frac{i}{2}\partial\overline\partial\bigl(|z|^2\bigr),$$

## 定理与证明

### Darboux 定理与 Weinstein 邻域定理

辛流形中任意一点都有邻域辛同胚于复欧氏空间中原点的某个邻域。类似地，闭流形 L 在 (M,ω) 中的任意拉格朗日嵌入，都可延拓为 T*L 零截面的某邻域与 M 中 L 的某邻域之间的辛同胚。

（none；来源：原书 p.3 §1.1）


缺口：原文只陈述定理（定理 thm:1.3）并引 [Dar82]、[Wei71]，未给证明；证明属经典结果。

### Kähler 情形给出紧辛流形

射影空间上的 Fubini–Study 形式是辛形式；由于 Kähler 性在限制到复子流形时保持，射影代数簇都带诱导的紧辛结构。

（none；来源：原书 p.2–3 §1.1）


缺口：原文只作陈述（例 thm:1.1 末），未给证明；属复几何标准事实。

## 易错点

- 「非退化」不是「$\omega$ 逐点非零」：要求的是每点切空间上的双线性型非退化，等价说法才是 $\omega^{\wedge n}\ne0$。
- 闭性不能省略：若 $d\omega\ne0$，$\omega(X,\cdot)$ 闭合这一条件不再定义辛向量场，哈密顿力学与 Floer 理论的整套构造失效。
- 辛流形一定偶维、可定向，但不必是 Kähler 流形；Gromov 的伪全纯技术正是为摆脱 Kähler 假设而设。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§1.1，p.2–3（原书 p.2–3 §1.1）

关联：`functoriality/concept/lagrangian-submanifold`、`functoriality/concept/almost-complex-structure`、`functoriality/concept/pseudoholomorphic-curve`

来源说明：原书 p.2–3 §1.1（辛流形定义、例 thm:1.1）；公式逐字取自中译本 chapter1.tex 的 eq:1–eq:3。
