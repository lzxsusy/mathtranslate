# 极限 $\psi^{\infty}(\beta)$ 存在（$t\to+\infty$）

`kshms/concept/prp-13-psi-infinity-limit` · track F（同调镜像猜想） · 原文 命题 13

**问题**　沿梯度流把紧支集截面推 $t\to+\infty$，为什么极限一定存在而不会跑掉？

**摘要**　紧支集截面经 $\psi^t$ 推动后，当 $t\to+\infty$ 有极限 $\psi^{\infty}(\beta)$，落在分布值 Dolbeault 形式空间中，其像由不稳定流形对应的分布张成。

**别名**　Proposition 13；limit of $\psi^t$ as $t\to+\infty$；$\psi^{\infty}$ 落在分布值形式空间

## 陈述

对任意 $\beta\in\Gamma_c(P(L_1,L_2),\underline{\mathrm{Hom}}^{alg}(E_1,E_2))$，极限
$$\psi^{\infty}(\beta)=\lim_{t\to+\infty}\psi^t(\beta)\in\Gamma\bigl(P(L_1,L_2),\mathcal{C}^{tw}_{\varepsilon}\otimes(\widehat{\rho}^{*}_1\otimes\widehat{\rho}_2)\otimes\underline{D}'_{P(L_1,L_2)}\bigr)$$
存在。

## 记号

$\Gamma_c$：紧支集截面函子；$\underline{D}'_{P(L_1,L_2)}$：$P(L_1,L_2)$ 上的分布值微分形式层，其截面带 adic 拓扑（与任一检验微分形式配对后在 adic 意义下收敛）；$U_x\subset P(L_1,L_2)$（$x\in L_1\cap L_2$）：不稳定流形。

## 要点

- 极限在更大的空间中取：$\underline{\mathrm{Hom}}^{alg}(E_1,E_2)$ 是 $\mathcal{C}^{tw}_{\varepsilon}\otimes(\widehat{\rho}^{*}_1\otimes\widehat{\rho}_2)\otimes\underline{D}'_{P(L_1,L_2)}$ 的子层，极限落在后者。
- 机制是 $\psi^t$ 把谱移到 $-\infty$：指数项随 $t$ 增大而衰减，级数在 adic 意义下收敛到分布值形式。
- 极限的像由 $x\in L_1\cap L_2$ 的不稳定流形 $U_x$ 对应的分布张成，是有限维 $\mathbb{C}_{\varepsilon}$-向量空间，这是通往 $\mathrm{Hom}_{FO(X^{\vee})}$ 的通道。
- $\beta\mapsto\psi^{\infty}(\beta)$ 延拓到滤过的完备化上并下降为 $\alpha\mapsto\phi^{\infty}(\alpha)$，其像落在同构于 $\mathrm{Hom}_{FO(X^{\vee})}((L_1,\rho_1),(L_2,\rho_2))$ 的空间中。

## 公式

$$\psi^{\infty}(\beta)=\lim_{t\to+\infty}\psi^t(\beta)$$

$$\psi^{\infty}(\beta)\in\Gamma\bigl(P(L_1,L_2),\mathcal{C}^{tw}_{\varepsilon}\otimes(\widehat{\rho}^{*}_1\otimes\widehat{\rho}_2)\otimes\underline{D}'_{P(L_1,L_2)}\bigr)$$

## 证明（sketch）

1. $\underline{\mathrm{Hom}}^{alg}(E_1,E_2)$ 是 $\mathcal{C}^{tw}_{\varepsilon}\otimes(\widehat{\rho}^{*}_1\otimes\widehat{\rho}_2)\otimes\underline{D}'$ 的子层，后者的截面带 adic 拓扑。

   *为什么*：极限要在完备的对象里取，这一步确定取值空间与拓扑。

2. $\psi^t$ 把 $\beta$ 的谱逐项移到 $-\infty$，故每个指数项随 $t\to+\infty$ 衰减，与检验形式配对后在 adic 意义下收敛。

   *为什么*：这就是原文「利用 $\psi^t$ 把态射的谱移到 $-\infty$」一句的内容，衰减保证收敛到分布。

3. 与 §6.5 的 Morse 理论论证平行，极限落在 $U_x$（$x\in L_1\cap L_2$）对应的分布张成的有限维空间，并可延拓到滤过的完备化、下降为 $\phi^{\infty}$。

   *为什么*：原文说明这一步「与 §6.5 类似可以证明」，并据此描述 $\phi^{\infty}$ 的像。

> 缺口：原文写「与 Morse 理论的情形（§6.5）类似，可以证明」，未给证明。缺口有两处：其一，adic 拓扑下逐项收敛到分布值形式需要 §6.5 的估计（配对后的收敛速率）；其二，$\psi^{\infty}$ 的像恰由不稳定流形 $U_x$ 的分布张成（含有限维性）也只是转述 §6.5，细节须回查该节。

## 易错点

- 极限不是逐点收敛的普通函数极限，而是在分布值形式空间里按 adic 拓扑取的极限；用 $C^{\infty}$ 收敛去理解会得出错误结论。
- $\psi^{\infty}$ 不是恒等或满射：它把一般截面压到不稳定流形张成的有限维空间中，信息有损失，这正是它像「投影」的原因。
- 命题 13 只断言极限存在，没有断言 $\psi^{\infty}$ 幂等；把它当投影算子 $\Pi$ 使用是 §8.3 后续的步骤，其性质不在本命题内。

## 相关卡

- `kshms/concept/prp-11-spectrum-semigroup`
- `kshms/concept/prp-14-mk-formulas-agree`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §8.3（原文 p.57）；锚点 `源码/chunks/ch09.tex:230-239（命题 13）`

> 原文 p57 §8.3；译本 ch09.tex 第 217–239 行（第 217–228 行给出层与分布值形式的包含关系与 adic 拓扑，第 230–239 行为命题）；命题之后第 241 行起描述极限与 $\phi^{\infty}$ 的像。
