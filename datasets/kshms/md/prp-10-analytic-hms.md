# 解析侧收尾：$C(Y)$ 与 $D^b_{\mathcal{A}_\infty}(\mathcal{Y})$ 的 $\mathcal{A}_\infty$-等价

`kshms/concept/prp-10-analytic-hms` · track E（刚性解析与凝聚层） · 原文 命题 10

**问题**　$C(Y)$ 是用解析侧层的消解定义的 $\mathcal{A}_\infty$-范畴，它凭什么等于代数侧 $\mathcal{Y}$ 的导出范畴？

**摘要**　把 $\mathcal{O}_Y$ 换成解析侧的消解不改变 $\mathcal{A}_\infty$-结构：$C(Y)$ 与射影代数簇 $\mathcal{Y}$ 的 $\mathcal{A}_\infty$-增强导出范畴等价，这是 GAGA 在 $\mathcal{A}_\infty$ 层面的体现。

**别名**　Proposition 10；analytic GAGA for $C(Y)$；凝聚层导出范畴的 $\mathcal{A}_\infty$-结构（解析版）

## 陈述

范畴 $C(Y)$ 与 $D^b_{\mathcal{A}_\infty}(\mathcal{Y})$ 是 $\mathcal{A}_\infty$-等价的，其中 $\mathcal{Y}$ 是对应于指派给 $Y$ 的解析空间 $Y^{an}$ 的射影代数簇。

## 记号

$C(Y)$：对象为有限秩局部自由 $\mathcal{O}_Y$-模的有限复形、态射空间为 $\Gamma\bigl(Y,\underline{\mathrm{Hom}}_{\mathcal{O}_Y}(E_1,E_2)\widehat{\otimes}_{\mathcal{O}_Y}\widehat{\Omega}^{*}_Y\bigr)$ 的 dg-范畴，除 $m_1,m_2$ 外无高阶复合；$D^b_{\mathcal{A}_\infty}(\mathcal{Y})$：$\mathcal{Y}$ 上凝聚层有界导出范畴的 $\mathcal{A}_\infty$-增强（按 $\mathcal{A}_\infty$-等价取类）；$\widehat{\Omega}^{*}_Y$：$\mathcal{O}_Y$ 的软 dg-代数层消解。

## 要点

- $C(Y)$ 的态射空间按定义就是 $\mathcal{O}_Y$-模层空间张量 $\widehat{\Omega}^{*}_Y$ 的整体截面，即相应层空间的消解；因此解析侧与代数侧的差别只剩 GAGA。
- $\mathcal{A}_\infty$-等价的对象是等价类 $D^b_{\mathcal{A}_\infty}(V)$：不同消解选取给出 $\mathcal{A}_\infty$-等价的范畴，故命题的结论不依赖消解的选法。
- 命题依赖前置假设「$[g]$ 是整的」：由此 $\exp([g])$ 是 $Y^{an}$ 上某线丛的第一 Chern 类，才能调用 [Be] 命题 3.14 的 GAGA 把解析凝聚层范畴换成 $\mathcal{Y}$ 上的代数凝聚层范畴。
- 它是 §7 的收尾：解析侧的对象已被认成 $\mathcal{Y}$ 的导出范畴，§8 才能在这两个范畴之间构造镜像对称函子。

## 公式

$$C(Y)\simeq_{\mathcal{A}_\infty}D^b_{\mathcal{A}_\infty}(\mathcal{Y})$$

## 证明（sketch）

1. $C(Y)$ 的态射空间是 $\underline{\mathrm{Hom}}_{\mathcal{O}_Y}(E_1,E_2)\widehat{\otimes}\widehat{\Omega}^{*}_Y$ 的整体截面，即相应 $\mathcal{O}_Y$-模层空间的消解。

   *为什么*：这是 $C(Y)$ 的定义（§7.2）：把态射空间化归为层的问题，才谈得上用 GAGA。

2. 把消解解析化到 $Y^{an}$ 上，再由 [Be] 的 GAGA 定理把 $\mathrm{Coh}(Y^{an})$ 与 $\mathrm{Coh}(\mathcal{Y})$ 等同，得到代数侧的消解。

   *为什么*：$\mathcal{Y}$ 射影，故 GAGA 给出解析凝聚层与代数凝聚层范畴的等价，消解层面随之对应。

3. 不同消解之间的比较同构给出 $\mathcal{A}_\infty$-等价的范畴，于是 $C(Y)$ 与 $D^b_{\mathcal{A}_\infty}(\mathcal{Y})$ 在 $\mathcal{A}_\infty$-等价类意义下相同。

   *为什么*：原文明确「不同消解的选取导致 $\mathcal{A}_\infty$-等价的范畴」，故第 2 步的选取不影响结论。

> 缺口：原文只写「由 [Be] 中的 GAGA 定理，下述结果成立」，未展开。缺口在 $\mathcal{A}_\infty$ 层面：$\widehat{\Omega}^{*}_Y$ 的软消解解析化后与 Godement 消解的相容性、以及 $m_k$ 在等价下的逐项对应都没有写出；GAGA 的依据是 [Be] 命题 3.14。

## 易错点

- $\mathcal{Y}$ 不是 $Y$：$\mathcal{Y}$ 是 $Y^{an}$ 所对应的射影代数簇，$Y$ 是实环面；命题说的是 $C(Y)$ 与 $\mathcal{Y}$ 的导出范畴等价。
- 「$\mathcal{A}_\infty$-等价」不能弱化为「导出等价」或「三角等价」：$D^b_{\mathcal{A}_\infty}$ 带的是增强后的高阶复合数据，等价须保 $m_k$。
- 整性假设 $[g]\in H^1(Y,Af_Y)/\mathrm{torsion}$ 写在本段之前（「今后我们假定 $[g]$ 是整的」），命题本身不再重复，漏读会以为 GAGA 无条件可用。

## 相关卡

- `kshms/concept/prp-09-mumford-construction`
- `kshms/remark/rmk-19-oy-tilde`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §7.2（原文 p.52）；锚点 `源码/chunks/ch08.tex:192-195（命题 10）`

> 原文 p52 §7.2 末；译本 ch08.tex 第 189–195 行（第 189–191 行为由消解与 GAGA 得结论的说明，第 192–195 行为命题）；整性假设 $[g]$ 见第 157–158 行。
