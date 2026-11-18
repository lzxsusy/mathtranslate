# 稳定曲线

> `siebert/concept/stable-curve` ｜ track B ｜ draft

**一句话**：稳定曲线是几何纤维连通、一维、至多结点、且每条光滑有理分支至少带 3 个特殊点的曲线；它与「自同构群有限」等价。

**自测**：稳定曲线条件里「每条有理分支至少 3 个特殊点」为什么恰好等价于自同构群有限？

## 定义

$S$ 上的 Deligne–Mumford 稳定曲线是固有平坦态射 $\pi:C\to S$，使每个几何纤维 $C_s$ 满足：(i) $C_s$ 是约化、连通的一维概形，奇点至多是结点（结点指平展局部同构于 $V(zw)\subset\mathbb{A}^2$ 的点）；(ii) 若 $E\subset C_s$ 是不可约分支而 $\nu:\widetilde E\to E$ 是其正规化，且 $\widetilde E\cong\mathbb{P}^1$，则 $E$ 的奇点在 $\widetilde E$ 中的原像至少 3 个点；此外不允许 $C_s$ 本身是亏格 $0$ 或亏格 $1$ 的光滑曲线。$C_s$ 的亏格取 $g=h^1(C_s,\mathcal{O}_{C_s})$。条件 (ii) 与「排除光滑 $g=0,1$」合起来，恰好等价于 $\operatorname{Aut}(C_s)$ 有限（注 2.9）。

记号：$\overline{\mathcal M}_g$：亏格 $g$ 稳定曲线的模叠；$\omega_{C/S}$：相对对偶化可逆层；$\nu:C_s'\to C_s$：几何纤维的正规化，$x_i,y_i\in C_s'$ 是第 $i$ 个结点的两个原像；「特殊点」= 结点原像与标记点。

## 要点

- 加结点的动机是紧化：光滑曲线的模空间 $\mathcal{M}_g$ 不紧，Deligne–Mumford 的做法是只补结点曲线而不再引入更坏的奇点，于是得到固有分离的 $\overline{\mathcal M}_g$，边界 $\overline{\mathcal M}_g\setminus\mathcal{M}_g$ 是正规交叉除子。
- 条件 (ii) 是稳定性判据的几何形式：一条光滑有理分支若只有 0、1、2 个特殊点，它上面就有连续多个自同构（$\mathbb{P}^1$ 的 $\mathrm{PGL}_2$ 保持至多 2 点仍有 1 维自由），自同构群因此不是有限群；3 个特殊点把 $\mathrm{PGL}_2$ 的自由度用完，自同构变成有限群。
- 「$\operatorname{Aut}(C_s)$ 有限」正是 $\overline{\mathcal M}_g$ 成为 Deligne–Mumford 叠的来源：对曲线族 $C/B$，同构函子 $\operatorname{Iso}_B(C,C)\to B$ 是有限非分歧的，于是对角态射 $\Delta_{\overline{\mathcal M}_g}$ 非分歧，这正是 DM 判据（定理 2.6）要的条件。
- 稳定曲线在平展局部是完全交（结点处 $V(zw)$），因此有相对对偶化可逆层 $\omega_{C/S}$；当 $n\ge3$ 时 $\omega_{C/S}^{\otimes n}$ 相对甚丰，可用来作 $n$-典范嵌入，这是把稳定曲线塞进 Hilbert 概形的全部技术基础。
- 结点处典范丛的表现是 $\nu^*\omega_{C_s}=\omega_{C_s'}(\sum x_i+\sum y_i)$（相当于在 $C_s'$ 上取 $\Omega^1(\sum x_i+\sum y_i)$），并且留数满足 $\operatorname{Res}_{x_i}+\operatorname{Res}_{y_i}=0$；这条「留数和为零」的约束正是结点不分走多余自由度、$n$-典范嵌入仍然有效的原因。
- $\overline{\mathcal M}_g$ 对 $g\ge2$ 是固有、分离、有限型的 DM 叠（推论 2.11 + 定理 2.13）；固有性需要稳定约化（定理 2.14），与「自同构有限」是两件独立的事。

## 公式

$$\nu^*\omega_{C_s}=\omega_{C_s'}\Big(\sum_i x_i+\sum_i y_i\Big),\qquad \operatorname{Res}_{x_i}(\nu^*\alpha)+\operatorname{Res}_{y_i}(\nu^*\alpha)=0$$
$$h^0\big(C_s,\omega_{C_s}^{\otimes n}\big)=(2n-1)(g-1)\qquad(n\ge3)$$
$$\#\operatorname{Aut}(C_s,\mathbf{x})<\infty\iff 2g-2+k>0\ \text{（每个有理分支至少 3 个特殊点）}$$

## 定理与证明

### 定理 2.8（$n$-典范丛的相对丰性）

设 $g\ge2$、$n\ge3$，$\pi:C\to S$ 是稳定曲线。则 $\omega_{C/S}^{\otimes n}$ 相对 $\pi$ 甚丰，且 $\pi_*\big(\omega_{C/S}^{\otimes n}\big)$ 是局部自由层，秩为 $(2n-1)(g-1)$。

（sketch；来源：原书 p.37 定理 2.8）

1. 先在光滑纤维上算：Riemann–Roch 给出 $h^0(\omega_C^{\otimes n})-h^1(\omega_C^{\otimes n})=(2n-1)(g-1)$，而 Serre 对偶把 $h^1$ 换成 $h^0(\omega_C^{\otimes(1-n)})$，$n\ge2$ 时它为零。  
   为什么：秩的公式必须先在光滑情形算出来，因为 $\pi_*\omega^{\otimes n}$ 局部自由意味着秩在纤维上取常值，光滑点给出这个常值。
2. 结点情形：用 $\nu^*\omega_{C_s}=\omega_{C_s'}(\sum x_i+\sum y_i)$ 与留数和为零，说明在结点处 $n$-典范形式的取值只受「留数配对」约束，最坏情形退化为 $\mathcal{O}_{\mathbb{P}^1}(1)$，仍分离点与切向量。  
   为什么：相对丰性的唯一障碍在结点：必须证明 $\omega^{\otimes n}$ 在结点局部仍能把相邻点分开，否则 $n$-典范映射会把这些点粘在一起。
3. 由逐纤维的丰性与上同调换基（cohomology and base change）得到相对甚丰与 $\pi_*$ 局部自由。  
   为什么：「相对甚丰」按定义要在每个几何纤维上检验，所以光滑情形与结点情形合起来就给出结论。

缺口：讲义自述这里只给出证明概要；基变换下的上同调相容性、$n$-典范映射的单射性（分离点与切向量）在结点邻域只作了最坏情形估计，未逐条验证。

## 易错点

- 「结点」是平展局部的条件，不是 Zariski 局部的：$V(zw)\subset\mathbb{A}^2$ 在 Zariski 局部看不到「两条线的交」，只有取平展覆盖（如 $z\mapsto$ 分支参数）才看出来。
- 条件 (ii) 与「排除光滑 $g=0,1$」缺一不可：光滑椭圆曲线没有结点、条件 (ii) 空洞成立，但 $\operatorname{Aut}$ 无限；光滑 $\mathbb{P}^1$ 同理。两条规则不能只取一条。
- 「稳定」不是「光滑」：$\overline{\mathcal M}_g\setminus\mathcal{M}_g$ 非空且是边界除子；把稳定曲线默认成光滑曲线会漏掉模叠的整个边界。
- 亏格是算术亏格 $h^1(\mathcal{O})$，不是各分支亏格之和：结点曲线的 $g=\sum g_i+\#\{\text{结点}\}$，逐分支算再加结点数才对。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 2 章 §3 稳定曲线，p.36–37（原书 p.37）

关联：`siebert/deriv/stable-curve-automorphism`、`siebert/concept/moduli-space`、`siebert/concept/deligne-mumford-stack`

来源说明：原书 p.36–37 §3（定义 2.10、注 2.9、定理 2.8 的陈述）。结点的平展局部模型与「3 个特殊点 ⇒ 自同构有限」按 Stacks Project tag 0E73（§109.22 Stable curves，定义 109.22.1）核对；稳定曲线作为 DM 叠的对象另见 nLab「moduli space of curves」（last revised 2026-03-02）。
