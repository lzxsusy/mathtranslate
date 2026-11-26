# Sandvik BunG 讲义（sandvik25）资料卡索引

共 27 张：概念卡 21 张、推导卡 6 张。


## 轨道 A · 中心层与 Wakimoto 层


**概念卡**

- [反球模 $M^{\mathrm{asph}}$](concepts/antispherical-module.md) —— 把 $\mathbb Z$ 沿 $W$ 的符号表示诱导到延长仿射 Weyl 群：$M^{\mathrm{asph}}=\mathbb Z\otimes_{\mathbb Z[W]}\mathbb Z[W_{\mathrm{ext}}]$。它是整篇文章的「靶子」。
- [中心仿射 Grassmann 簇 $\mathrm{Gr}^{\mathrm{cen}}_G$](concepts/central-affine-grassmannian.md) —— 一个带正则映射 $f\colon\mathrm{Gr}^{\mathrm{cen}}_G\to\mathbb C$ 的 ind-概形：一般纤维是 $\mathrm{Gr}_G$、特殊纤维是 $\mathrm{Fl}_G$，于是「仿射 Grassmann 簇形变到仿射旗簇」。
- [Gaitsgory 中心函子 $Z$](concepts/gaitsgory-central-functor.md) —— $Z(\mathcal F)=\Psi_f(\mathcal F\boxtimes k_{\mathbb C^\times}[1])$ 把 $L^+G$-等变层送到 $I$-等变层；定理 2.4.1 说它幺半、$t$-正合、像落在中心，且 $\pi_*Z(\mathcal F)\cong\mathcal F$。
- [附近循环函子 $\Psi_f$](concepts/nearby-cycles.md) —— 对 $f\colon X\to\mathbb C$，把 $X^\times=f^{-1}(\mathbb C^\times)$ 上的层拉回、经万有覆盖、再取特殊纤维：$\Psi_f\mathcal F=(i^*j_*\exp_{X*}\exp_X^*\mathcal F)[-1]$。
- [中心层的 Wakimoto 滤链（定理 2.5.3）](concepts/wakimoto-filtration.md) —— 每个中心层 $Z(\mathcal F)$ 都有滤链，各项商为 $\mathbb W_{\lambda_i}$；且 $\mathbb W_\lambda$ 的重数恰是 $\mathrm{Sat}^{-1}(\mathcal F)$ 的 $\lambda$-权空间维数。
- [Wakimoto 层 $\mathbb W_\lambda$](concepts/wakimoto-sheaves.md) —— 把 $\lambda=\lambda_1-\lambda_2$ 写成支配权之差，令 $\mathbb W_\lambda=\nabla_{\lambda_1}\star_I\Delta_{-\lambda_2}$：与选择无关、支撑在 $\mathrm{Fl}_{G,\lambda}$、且对加法幺半。

**推导卡**

- [从附近循环造出中心函子，并证明它 $t$-正合](derivations/nearby-cycles-to-central.md) —— 把 $Z(\mathcal F)=\Psi_f(\mathcal F\boxtimes k_{\mathbb C^\times}[1])$ 拆成「张量一个常层」与「附近循环」两步：前者显然 $t$-正合，后者由命题 2.2.2(2) 提供 $t$-正合性。

## 轨道 B · Springer 侧与三造函子


**概念卡**

- [函子 I：$F_1\colon\mathrm{Rep}(G^\vee\times T^\vee)\to\mathcal P_I^{\mathrm{Wak}}$](concepts/functor-f1.md) —— 在表示范畴上直接定义 $V\otimes k_{T^\vee}(\lambda)\mapsto Z(\mathrm{Sat}(V))\star_I\mathbb W_\lambda$；定理 2.5.3 保证值域落在有 Wakimoto 滤链的中心层里，且它是幺半的。
- [函子 II：经 Tannakian 重构把 $F_1$ 扩到 $\mathrm{Coh}_{\mathrm{free}}(\widehat{\mathcal N}_X)$](concepts/functor-f2.md) —— 把 $\mathcal P_I^{\mathrm{Wak}}$ 换成一个对称幺半的非全子范畴 $\mathcal C$，用 Tannakian 形式得 $H\colon\mathcal C\xrightarrow{\sim}A\text{-}\mathrm{mod}^{G^\vee\times T^\vee}_{\mathrm{free}}$，于是扩张 $F_1$ 等价于造一个等变代数映射 $\mathcal O(\widehat{\mathcal N}_X)\to A$。
- [函子 III：$F\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b\mathcal P_I$](concepts/functor-f3.md) —— 先验证 $K^bF_2$ 把 $\partial X$-支撑的复形打成零，于是 $F_2$ 下降为 $F$：$V\otimes\mathcal O_{\widetilde{\mathcal N}}\mapsto Z(\mathrm{Sat}(V))$、$\mathcal O_{\widetilde{\mathcal N}}(\lambda)\mapsto\mathbb W_\lambda$；复合实现函子后仍**不是**等价。
- [无穷小稳定化子 $\widehat{\mathcal N}$ 与 $\widehat{\mathcal N}_X$](concepts/hat-n-x.md) —— 把 $G^\vee/U^\vee$ 仿射完备化为 $X=\mathrm{Spec}\,\mathcal O(G^\vee/U^\vee)$，其无穷小万有稳定化子是 $\widehat{\mathcal N}_X$；$\widehat{\mathcal N}\subset\widehat{\mathcal N}_X$ 是开子簇，且 $\widehat{\mathcal N}$ 是 $\widetilde{\mathcal N}$ 上的 $T^\vee$-torsor。
- [Springer 解消 $\widetilde{\mathcal N}$ 与线丛 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$](concepts/springer-resolution.md) —— $\widetilde{\mathcal N}=G^\vee\times_{B^\vee}\mathfrak n^\vee$ 是 $G^\vee$-等变的 Springer 解消，其上的线丛 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$ 与 $V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)$ 生成 $\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})$。

**推导卡**

- [函子 I 为什么是幺半的](derivations/f1-monoidal.md) —— $F_1(V\otimes k_{T^\vee}(\lambda))=Z(\mathrm{Sat}(V))\star_I\mathbb W_\lambda$ 的两条乘法来源：中心的交换性（定理 2.4.1(3)）与 Wakimoto 层的加法性（命题 2.5.2(3)）。
- [Tannakian 重构里的代数 $A$ 与 $\mathcal O(\widehat{\mathcal N}_X)\to A$](derivations/tannakian-algebra.md) —— 先在对称幺半的非全子范畴 $\mathcal C\subset\mathcal P_I^{\mathrm{Wak}}$ 上取端环 $A$，得到 $H\colon\mathcal C\cong A\text{-}\mathrm{mod}_{\mathrm{free}}$；再把 $\mathcal O(\mathfrak g^\vee)\to A$（单值的对数）与 $\mathcal O(X)\to A$（Wakimoto 滤链）拼成 $\mathcal O(\widehat{\mathcal N}_X)\to A$。

## 轨道 C · Iwahori–Whittaker 侧


**概念卡**

- [反球商 $\mathcal P_I^{\mathrm{asph}}$](concepts/antispherical-quotient.md) —— 把 $\mathcal P_I=\mathrm{Perv}(I\backslash\mathrm{Fl}_G)$ 按那些 $w\notin\widetilde W_{\mathrm{ext}}$ 的单对象 $\mathrm{IC}_w$ 生成的 Serre 子范畴作商，得反球 Hecke 范畴，带商函子 $\mathcal P_I\to\mathcal P_I^{\mathrm{asph}}$。
- [中心层的 IW 像是倾斜层（定理 4.5.1）](concepts/central-tilting.md) —— 复合 $Z^{\mathrm{IW}}\colon\mathrm{Rep}(G^\vee)\xrightarrow{Z}\mathcal P_I\xrightarrow{\mathrm{Av}^{\mathrm{IW}}}\mathcal P_{\mathrm{IW}}$ 把每个 $V$ 送到倾斜层，且 $\Delta^{\mathrm{IW}}_\lambda$ 与 $\nabla^{\mathrm{IW}}_\lambda$ 的重数都等于 $\dim V_\lambda$。
- [IW 平均函子 $\mathrm{Av}^{\mathrm{IW}}$（定理 4.4.1）](concepts/iw-averaging.md) —— $\mathrm{Av}^{\mathrm{IW}}(\mathcal F)=\Delta^{\mathrm{IW}}_0\star_I\mathcal F$ 是反常 $t$-正合的，且在反常层上穿过反球商，给出全忠实函子 $\mathcal P_I^{\mathrm{asph}}\hookrightarrow\mathcal P_{\mathrm{IW}}$。
- [Iwahori–Whittaker 范畴 $\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$](concepts/iw-category.md) —— 取 $I_u^+$（$I^+$ 的幂幺根）经 $\chi\colon I_u^+\to\mathbb G_a$ 的 Whittaker 扭曲，定义 $\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$；反常 $t$-结构限制其上，且 $\mathcal D^b_c(I\backslash\mathrm{Fl}_G)$ 从右侧卷积作用于它。
- [IW 反常层的最高权结构（命题 4.3.1）](concepts/iw-highest-weight.md) —— $I_u^+$-轨道由 $W_{\mathrm{ext}}$ 参数化，其中只有 $\widetilde W_{\mathrm{ext}}$ 上的轨道承载非零 Whittaker 局部系统；据此定义 $\Delta^{\mathrm{IW}}_\lambda,\nabla^{\mathrm{IW}}_\lambda,\mathrm{IC}^{\mathrm{IW}}_\lambda$，得权偏序集为 $X^\vee$ 的最高权范畴，从而有不可分解倾斜层 $T^{\mathrm{IW}}_\lambda$。
- [Whittaker 层与 $(H,\chi^*\mathcal L_{\mathrm{AS}})$-等变范畴](concepts/whittaker-sheaves.md) —— 固定 $\chi\colon H\to\mathbb G_m$ 与 $\mathbb G_a$ 上的 Artin–Schreier 局部系统 $\mathcal L_{\mathrm{AS}}$，把 $\chi^*\mathcal L_{\mathrm{AS}}$ 当作 $H$ 的乘法局部系统，得等变导出范畴；其对象常被上同调消没死死约束。

**推导卡**

- [平均函子为什么 $t$-正合：式 (5)(6) 的用法](derivations/iw-averaging-t-exact.md) —— $\mathrm{Av}^{\mathrm{IW}}=\Delta^{\mathrm{IW}}_0\star_I(-)$ 把标准层送到标准层、余标准层送到余标准层（式 (6)），并把非极小胞腔的单层打成零（式 (5)）；由反常 $t$-结构的「标准–余标准判别法」即得 $t$-正合性。
- [Wakimoto 滤链的重数如何变成 $\dim V_\lambda$](derivations/wakimoto-multiplicity.md) —— 定理 2.5.3 说 $Z(\mathrm{Sat}(V))$ 的 Wakimoto 滤链里 $\mathbb W_\lambda$ 的重数是 $V$ 的 $\lambda$-权维数；定理 4.5.1 说平均之后 $\Delta^{\mathrm{IW}}_\lambda$ 与 $\nabla^{\mathrm{IW}}_\lambda$ 的重数也是 $\dim V_\lambda$——中间差一个 $\mathrm{Av}^{\mathrm{IW}}$ 保持重数的论证。

## 轨道 D · 主等价


**概念卡**

- [五个范畴的等价图（推论 5.0.2）](concepts/five-categories.md) —— 主定理连同 §4 的构造把五个范畴串成一个交换图：$\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\sim\mathcal D^b\mathcal P_I^{\mathrm{asph}}\sim\mathcal D^b\mathcal P_{\mathrm{IW}}\sim\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)\sim\mathcal D^b\mathcal P_I$。
- [主函子 $F^{\mathrm{IW}}$ 与 Arkhipov–Bezrukavnikov 等价（定理 5.0.1）](concepts/functor-fiw.md) —— $F^{\mathrm{IW}}=\mathrm{Av}^{\mathrm{IW}}\circ F\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$ 是等价：$V\otimes\mathcal O_{\widetilde{\mathcal N}}\mapsto Z^{\mathrm{IW}}(V)$、$\mathcal O_{\widetilde{\mathcal N}}(\lambda)\mapsto\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$。

**推导卡**

- [主定理的全忠实：$\mathrm{Hom}$ 两边的显式计算](derivations/fully-faithful-hom.md) —— 把 (8) 用五引理化到生成元后，两边都算成同一个数：$n=0$ 时为 $\dim V_{-\lambda}$，否则为 $0$。

## 轨道 总览


**概念卡**

- [主定理：三向等价（定理 5.0.1 与推论 5.0.2）](concepts/ab-equivalence-theorem.md) —— 梗概：合成函子 $\mathrm{F}^{\mathrm{IW}}=\mathrm{Av}^{\mathrm{IW}}\circ\mathrm{F}$ 给出 $\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\simeq\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$；由此再得五个范畴两两等价。
- [反球模的三种描述与三种范畴化](concepts/three-categorifications.md) —— 反球模 $M^{\mathrm{asph}}$ 有 $K$ 群、$q$-形变 Whittaker、Iwahori–Whittaker 函数三种描述，各给一个候选范畴化；主定理说三者其实是同一个三角范畴。
