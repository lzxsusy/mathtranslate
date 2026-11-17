# Ψ ≠ 0：λ-连接与扭化 D-模

> `kw/deriv/psi-lambda` · 轨道 E · Langlands 与翻译器 · 状态 dev · 7 步

> **要回答的问题**：当 $\Psi\ne0$ 时 c.c. 膜如何修改，Hitchin 纤维上的 λ-连接为什么是自然的推广？

## 一句话

实 $\Psi$ 时 Hitchin 纤维不再是合法 A-膜；扭化后的 c.c. 膜把全纯结构旋转 $q$，纤维坐标变成 $\lambda=\ii\tan(q/2)$ 的 λ-连接，于是 D-模按 $\Psi$ 加权并写成 $D_{L^{\Psi-h}}$。

## 目标

从纤维非法性出发，解出扭化 c.c. 条件，识别 $\lambda=\ii\tan(q/2)$ 的 λ-连接，并把 D-模写成 $D_{L^{\Psi-h}}$。

## 前提

- B p.202 eq (11.29)：纤维是合法 A-膜的要求 $F+B|_Y=0$，即 $[B|_Y/2\pi]$ 为整数。
- B p.203 eq (11.30)：扭化 c.c. 条件 $(\omega^{-1}(F+B))^2=-1$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 实 $\Psi$ 时 $t=1$、$B=-\omega_I\mathrm{Re}\,\tau$；但 $B$ 沿 Hitchin 纤维并不平坦，故对一般 $\Psi$ 纤维不是合法的 A-膜——合法条件 (11.29) 要求 $[B\|_Y/2\pi]$ 为整数，$\theta\ne2\pi n$ 时不满足。 | 这说明 §11.2 的「支撑在纤维上的典范膜」并不能原样推广到 $\Psi\ne0$，必须修改膜的定义。 | `B p.202 eq (11.29)` | A·原文明确写了 |
| 2 | 扭化办法是把 $F$ 换成 $F+B$：条件变成 $(\omega^{-1}(F+B))^2=-1$，其解为 $F=\mathrm{Im}\,\tau\cos q\,\omega_J$、$\sin q=-\mathrm{Re}\,\tau/\mathrm{Im}\,\tau$。 | 加上 $B$ 后纤维的平坦性障碍被吸收进 $\cos q$ 的偏移，从而重新得到可解条件。 | `B p.203 eq (11.30)` | A·原文明确写了 |
| 3 | 全纯结构随之旋转：$I(\Psi)=\omega^{-1}(F+B)=I\cos q-J\sin q$（(11.32)），全纯坐标为 $A'_z=A_z-\ii\tan(q/2)\varphi_z$、$\varphi'_z=\varphi_z+\ii\tan(q/2)A_z$。 | 旋转是 $q$ 的线性作用，它把原来的复结构 $I$ 与 $J$ 混合，正是扭化膜的几何内容。 | `B p.203 eq (11.32)` | A·原文明确写了 |
| 4 | 纤维方向齐次变换的坐标是 $D''_z=\varphi_z+\ii\tan(q/2)D_z$（(11.36)），它（差一个因子 $\ii\tan(q/2)$ 后）是丛 $E$ 上的全纯 λ-连接，$\lambda=\ii\tan(q/2)$，满足 $\nabla(fs)=f\nabla s+\lambda\,\partial f\wedge s$（(11.37)）。 | 这解释了为什么 $\Psi\ne0$ 时必须用 λ-连接：普通联络只是 $\lambda=0$ 的特例。 | `B p.204 eq (11.37)` | A·原文明确写了 |
| 5 | Hitchin 方程保证 λ-连接可积，于是纤维是固定丛上 λ-连接的模空间，它同构于 $H^0(C,\mathrm{End}\,E'\otimes K_C)$ 的仿射空间，也就是 $T^*M_C$ 的仿射形变。 | 可积性是把「坐标」提升为「模空间」的前提，也让 D-模的构造可以用丛上同调表达。 | `B p.204` | A·原文明确写了 |
| 6 | 整数点：$\Psi=n$ 时 $B_n$ 支撑在 $\varphi=0$ 上、Chan-Paton 丛为 $L^n$，态空间是 $K_M^{1/2}\otimes L^n\otimes(\oplus_{j=0}^n\Omega^{0,j})$，即 $D_{K^{1/2}\otimes L^n}$ 的模。 | 整数点给出可完全写出的例子，为下面把一般 $\Psi$ 的答案插值出来提供边界条件。 | `B p.205` | A·原文明确写了 |
| 7 | 一般 $\Psi$：粘接修正对 $\Psi$ 线性（展开到 $1/(\mathrm{Im}\,\tau)^2$ 阶仍只线性），结合整数点得 $f(\Psi)=\Psi$；又 $K_M\cong L^{-2h}$（$h$ 为对偶 Coxeter 数），故代数层为 $D_{L^{\Psi-h}}$，$\Psi=h$ 时退化为普通 D-模（(11.39)）。 | 这一步把「整数点上的丛 $L^n$」与「一般 $\Psi$ 的代数层」统一为同一个函数 $f(\Psi)=\Psi$。 | `B p.206 eq (11.39)` | A·原文明确写了 |

## 结论

实 $\Psi$ 时 Hitchin 纤维不是合法 A-膜，因为 $B=-\omega_I\mathrm{Re}\,\tau$ 沿纤维不平坦。扭化后 $(\omega^{-1}(F+B))^2=-1$ 的解把全纯结构旋转 $q$（$\sin q=-\mathrm{Re}\,\tau/\mathrm{Im}\,\tau$），纤维坐标成为 $\lambda=\ii\tan(q/2)$ 的 λ-连接，可积性由 Hitchin 方程保证。整数点 $\Psi=n$ 给 $D_{K^{1/2}\otimes L^n}$ 模，插值得 $f(\Psi)=\Psi$，一般 $\Psi$ 的代数层为 $D_{L^{\Psi-h}}$。

## 缺口

- $f(\Psi)=\Psi$ 只论证到 $1/(\mathrm{Im}\,\tau)^2$ 阶的微扰线性，原文未给非微扰证明（B p.206）。
- 原文 p.198 把 type F 膜的类型标成 $(A,B,A)$，按 p.207 的清单应为 $(B,A,A)$，此处为原文笔误（B p.198、p.207）。

## 最容易讲错的地方

- (11.30) 里是 $F+B$ 而不是 $F$；$B=-\omega_I\mathrm{Re}\,\tau$，符号不要漏。
- λ-连接参数是 $\lambda=\ii\tan(q/2)$，漏掉 $\ii$ 会把实结构与复结构混淆。
- $\Psi=h$（$h$ 为对偶 Coxeter 数）时 $D_{L^{\Psi-h}}$ 退化为普通 D-模，这是检验公式的基准点。

## 相关卡

[c.c. A-膜、开弦代数与 A-膜→D-模](../derivations/a-to-dmod.md) · [三类膜回到四维：§12 检查表](../derivations/back-to-4d.md) · [D-模](../concepts/d-module.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md)

## 出处（印刷页）

- B p.202–206（B p.203 eq (11.30)）

> 说明：steps 的 provenance 分布：A×7（共 7 步）；gaps 2 条、pitfalls 3 条。
