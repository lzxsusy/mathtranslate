# M_H 上的 sigma 模型数据与维数公式

> `kw/deriv/mh-sigma-data` · 轨道 C · 舞台：曲线与模空间 · 状态 dev · 4 步

> **要回答的问题**：紧化得到的 sigma 模型在 $M_H$ 上的度规与 $B$-场是什么，维数如何确定？

## 一句话

从二维有效理论出发，确定 $M_H$ 上的度规与 $B$-场：物理度规是 $\mathrm{Im}\,\tau$ 倍的自然度规 eq (4.15)，$B$-场是 $-\mathrm{Re}\,\tau\,\omega_I$ eq (4.19)；并得到复维 $(2g-2)\dim G$ 与 Hitchin 纤维化的半维数公式。

## 目标

定出 $M_H$ 上的 sigma 模型数据与维数。

## 前提

- 二维有效理论以 $M_H$ 为靶空间，见 `B p.38`。
- $M_H$ 复维 $(2g-2)\dim G$，见 `B p.39`。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 把四维规范理论的动能项按 $(1,1)$ 型拆分，得到 sigma 模型动能；与 eq (4.2) 的自然度规比较得诱导度规 eq (4.15)：$\mathrm{d}s^2_g=(4\pi/e^2)\mathrm{d}s^2=(\mathrm{Im}\,\tau)\mathrm{d}s^2$。 | 不比较 $(4.2)$ 与一般 sigma 模型动能，就无法定出度规的整体因子 $\mathrm{Im}\,\tau$；这个因子是后面 T-对偶的耦合常数。 | `B p.47 eq (4.15)` | A·原文明确写了 |
| 2 | $\theta$ 项经拓扑不变性变形为 $-\frac{i\theta}{8\pi^2}\int_\Sigma\int_C\mathrm{Tr}\,\delta A_C\wedge\delta A_C=\frac{i\theta}{2\pi}\int_\Sigma\Phi^*(\omega_I)$，故 $B=-\frac{\theta}{2\pi}\omega_I=-(\mathrm{Re}\,\tau)\omega_I$，即 eq (4.19)。 | $B$-场只能从 $\theta$ 项读出；只写度规会漏掉复化 Kähler 类的实部。 | `B p.48 eq (4.19)` | A·原文明确写了 |
| 3 | $\omega_I/2\pi$ 是 $H^2(M_H,\mathbb Z)$ 的生成元，故 $\int_\Sigma\Phi^*(\omega_I/2\pi)$ 就是二维瞬子数；二维与四维的 $\theta$ 角相同，因为它们是同一批瞬子。 | 这一步把 $B$-场的周期归一化钉死；若忘了 $2\pi$ 因子，瞬子数会差整数倍，$\theta$ 角对不上。 | `B p.48` | A·原文明确写了 |
| 4 | 在复结构 $I$ 中，$\varphi$ 的 Casimir 多项式给出 Hitchin 纤维化 $\pi:M_H\to B$，$\dim B=(g-1)\dim G=\frac12\dim M_H$，即 eq (4.25)；故一般纤维与底同维，都是 $\frac12\dim M_H$。 | 度规与 $B$-场之外还需知道纤维结构；$\dim B=\frac12\dim M_H$ 是后面完全可积性与纤维 $T$-对偶的维数前提。 | `B p.54 eq (4.25)` | A·原文明确写了 |

## 结论

有效 sigma 模型的数据由 $\tau$ 统一给出：度规是 $\mathrm{Im}\,\tau$ 乘 $M_H$ 的自然超凯勒度规，$B$-场是 $-\mathrm{Re}\,\tau\,\omega_I$，故复化 Kähler 类只依赖 $\tau$。这个 $(g,B)$ 的显式形式是后续 T-对偶与镜像对称论证的出发点；维数公式则保证 Hitchin 纤维化的纤维是环面。

## 缺口

- 度规与 $B$-场的推导只到 sigma 模型极限的领头阶，原文未讨论 $\alpha'$ 修正。

## 最容易讲错的地方

- 把 $B$-场写成 $-\mathrm{Im}\,\tau\,\omega_I$：$\theta$ 项给的是 $\mathrm{Re}\,\tau$，度规才是 $\mathrm{Im}\,\tau$。
- 忽略 $\omega_I$ 的周期归一化：$\omega_I/2\pi$ 才是整系数上同调类，否则瞬子数差 $2\pi$。

## 相关卡

[紧化到 Hitchin 方程：M = Σ×C](../derivations/compactify-to-hitchin.md) · [Hitchin 模空间](../concepts/hitchin-moduli.md) · [矩映射](../concepts/moment-map.md) · [超凯勒商与三个复结构 I, J, K](../derivations/hyperkahler-quotient.md)

## 出处（印刷页）

- B p.46–54（B p.48 eq (4.19)）

> 说明：A4：eq (4.15)、eq (4.19)、$\omega_I$ 的整性归一化与 eq (4.25) 均在 `B p.47–54` 明写；最没把握处是第 3 步把「同一批瞬子」的说法接到 $B$-场周期上的表述。
