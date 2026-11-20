---
id: MS-22
zh: 极端跃迁与锥形奇点跃迁
en: extremal and conifold transitions
aliases: [极端跃迁, 锥形奇点跃迁, 锥形跃迁, extremal transition, conifold transition]
layer: L2
prereqs: [MS-09, MS-21, MS-14, MS-03]
sources:
  - "A 级：Cox–Katz 1999, p.166–171（PDF p.166–171，印刷 p.143–148）§6.2.4「Kähler 模空间的边界」：定义 6.2.9、例 6.2.4.1–6.2.4.3、镜像映射≠恒等段落"
  - "A 级：Cox–Katz 1999, p.155–157（PDF p.155–157，印刷 p.132–134）§6.2.2：定义（本原收缩）、命题（Wilson）、I/II/III 型、I 型翻越、III 型反射"
  - "A 级：Cox–Katz 1999, p.428–429（PDF p.428–429，印刷 p.405–406）第 12 章：锥形奇点跃迁、Reid 幻想的 Kähler 版本、旗流形完全交构造"
  - "A 级：Greene–Morrison–Strominger 1995, Nucl. Phys. B451, 109（hep-th/9504145；书内 [GMS]）；Morrison 1997, Through the Looking Glass（alg-geom/9705028；书内 [Morrison9]）；Reid 1987, Math. Ann. 278, 329–334（书内 [Reid5]）"
  - "B 级：nLab「conifold transition」条目（2026-08-04 修订）；SY01-24 术语表第 15、18 条"
status: draft
review:
  drafter: agent-238
  reviewer: lead
  blindtest: pending
glossary_refs: ["SY01-24 术语表 #15 消失循环／#18 单值变换（冲突 T2／T1）", "_冲突表 T1、T2"]
symbols_refs: ['$V$', '$\overline V$', '$\widetilde V$', '$\phi$', '$K(V)$', '$W^*$', '$h^{1,1}$', '$h^{2,1}$', '$b_3$', '$q_j$', '$z_j$']
updated: 2026-11-20
---

# MS-22 极端跃迁与锥形奇点跃迁

## 1. 一句话

先爆缩到奇异簇、再光滑化，由一个 Calabi–Yau 三维簇得到另一个的两步变形。

## 2. 为什么需要它

- **它是本书「所有 Calabi–Yau 三维簇连成一张网」的唯一机制。** 第 12 章把锥形奇点跃迁作为 Reid 幻想的 Kähler 版本来陈述：若把所有 $V,\widetilde V$ 的复模空间沿所有 $\overline V$ 的模空间粘起来后连通，则任意两个 Calabi–Yau 三维簇都能经跃迁相连（PDF p.428–429；原猜想见 p.166 与 [Reid5]）。
- **它是镜像对称的一条硬检验。** 例 6.2.4.3 末尾（PDF p.171）指出：若镜像映射是恒等，对偶跃迁应在 $|z_2|=1$ 处粘接；实际粘接轨迹是判别式 $1-4z_2=0$（即 $z_2=1/4$），而代入镜像映射恰好得 $q_2=1$。没有极端跃迁，第 6.3 节的镜像映射就缺这条一致性检验。
- **它把抽象猜想变成可算构造。** 例 6.2.4.2（PDF p.168–169）用自反多胞形嵌套 $\Delta\subset\widetilde\Delta$ 造出环面极端跃迁，使 7555 个加权射影空间超曲面经此类跃迁落在同一连通分支（p.168，[ACJM,CGGK]）；这也让「跃迁前后 Hodge 数如何变」成为可核算的算术（本卡 §4）。

## 3. 定义（全假设）

**3.1 背景。** 基域 $\mathbb C$。$V$ 为光滑 Calabi–Yau 三维簇（本书约定：光滑射影三维簇、$K_V\cong\mathcal O_V$，从而 $h^{1,1}(V),h^{2,1}(V)$ 确定 $b_3=2+2h^{2,1}$ 与 $\chi=2(h^{1,1}-h^{2,1})$；约定见 MS-03）。$\overline V$ 记 $V$ 的双有理像。

**3.2 收缩与本原收缩**（§6.2.2 定义，PDF p.155，label `def:primitive-contraction`）。双有理态射 $\phi:V\to\overline V$ 称为**收缩**，若 $\overline V$ 为射影正规三维簇且 $\rho(\overline V)<\rho(V)$（$\rho$ 为 Picard 数）；若 $\phi$ 不能分解为正规簇之间的非平凡双有理态射之复合，则称**本原**。本原收缩收缩的 1-圈数值类 $C$ 至倍数唯一，超平面 $\mathcal H=\{D\in H^2(V,\mathbb R):D\cdot C=0\}$ 支撑 $\overline{K(V)}$ 的一个余维一面，称此面**对应于**该本原收缩（PDF p.155）。

**3.3 三型与翻越**（PDF p.156）。本原收缩 $\phi$ 分为：**I 型**：存在曲线 $C\subset V$，$\phi$ 在 $V-C$ 上为同构、$\phi(C)$ 为一点；**II 型**：存在曲面 $S$，$\phi$ 在 $V-S$ 上为同构、$\phi(S)$ 为一点；**III 型**：存在曲面 $S$，$\phi$ 在 $V-S$ 上为同构、$\phi(S)$ 为曲线。I 型收缩可**翻越**：存在另一个 Calabi–Yau 三维簇 $V'$ 与 $\phi':V'\to\overline V$ 收缩 $C'\subset V'$，$V,V'$ 的 Kähler 锥沿各自的面相接，且 $H^2(V)\cong H^2(V')$（PDF p.156，[Reid2,Kollar]）。

**3.4 极端跃迁**（定义 6.2.9，PDF p.166，引自 [Morrison9]）。设 $V$ 为 Calabi–Yau 三维簇，$\phi:V\to\overline V$ 为双有理收缩。若 $\overline V$ 可光滑化为 Calabi–Yau 三维簇 $\widetilde V$，则从 $V$ 到 $\widetilde V$ 的这个过程称为**极端跃迁**（extremal transition）。若 $\phi$ 本原，称**本原极端跃迁**；$\phi$ 属 I/II/III 型时，说该跃迁属 I/II/III 型。**锥形奇点跃迁**（conifold transition）= I 型极端跃迁，因为物理学家常把三维结点叫作锥形奇点（conifold，PDF p.166）。

**3.5 本书用法。** Cox–Katz 在 p.166 采用 [Morrison9] 的宽松版本：只要求「双有理收缩 + $\overline V$ 可光滑化为 Calabi–Yau 三维簇」，既未在定义中要求 $\phi$ 本原，也未要求 $\overline V$ 射影正规、$\rho$ 下降（比 p.155 的收缩定义少这两条）；正文随后用「本原」「I 型」等附加词补足。形式化时必须补上，否则「收缩」与 §6.2.2 不同义（§11 C3）。

## 4. 最小例子（能算出）

**4.1 例 6.2.4.1 的几何（PDF p.167–168，取自 [GMS]）。** 设 $\overline V\subset\mathbb P^4$ 由 $x_3g+x_4h=0$ 定义，$g,h$ 为一般四次多项式。其奇点集是 $\{x_3=x_4=0\}\cong\mathbb P^2$ 上两条四次曲线 $g|_{\mathbb P^2}=h|_{\mathbb P^2}=0$ 之交，故恰有 $4\cdot4=16$ 个结点（一般位置横截）。令 $V\subset\mathbb P^4\times\mathbb P^1$ 为
$$y_0x_4-y_1x_3=0\quad(1,1),\qquad y_0g+y_1h=0\quad(4,1)$$
定义的光滑完全交；因 $1+4=5=4+1$，$K_V$ 平凡，$V$ 为 Calabi–Yau 三维簇。每个结点上方的纤维 $\mathbb P^1\subset V$ 被投影 $\mathbb P^4\times\mathbb P^1\to\mathbb P^4$ 压成一点，故限制 $\phi:V\to\overline V$ 恰收缩这 16 条曲线；书内用「$H$ 张成 Kähler 锥的一个面且 $H^3=5\ne0$」（p.167）说明它是本原收缩。

**4.2 手算 Hodge 数（不依赖任何跃迁公式）。** 记 $H,F$ 为 $\mathbb P^4,\mathbb P^1$ 的超平面类。环 $\mathbb P^4\times\mathbb P^1$ 中 $H^5=F^2=0$、$\int H^4F=1$，且 $[V]=(H+F)(4H+F)=4H^2+5HF$，于是 $\int_VH^3=5$、$\int_VH^2F=4$、$\int_VHF^2=\int_VF^3=0$。由伴随公式
$$c(T_V)=\frac{(1+H)^5(1+F)^2}{(1+H+F)(1+4H+F)},\qquad c_3(T_V)=-20H^3-17H^2F,$$
得 $\chi(V)=\int_Vc_3=-20\cdot5-17\cdot4=-168$。又 $V$ 在 $\mathbb P^4\times\mathbb P^1$ 中丰沛，由 Lefschetz 定理 $H^2(V)\cong H^2(\mathbb P^4\times\mathbb P^1)$，即 $h^{1,1}(V)=2$（与书内「$V$ 的 Kähler 锥同构于 $\mathbb P^4\times\mathbb P^1$ 的」一致，p.167）。由 $\chi=2(h^{1,1}-h^{2,1})$ 得 $h^{2,1}(V)=2+84=86$，$b_3(V)=2+2\cdot86=174$。

**4.3 光滑化端的数字。** 五次三维簇 $\widetilde V\subset\mathbb P^4$：5 变量 5 次单项式共 $\binom94=126$ 个，扣除 $\dim GL_5=25$，故 $h^{2,1}(\widetilde V)=101$、$h^{1,1}(\widetilde V)=1$、$b_3=204$、$\chi=-200$。

**4.4 对账。** 16 个结点给出 16 个消失 3-圈，但它们满足 1 条关系（16 条例外曲线同属一个纤维类，只有 1 条极值射线，Kähler 模只损失 1 维），独立圈数 $n-r=16-1=15$。于是
$$h^{2,1}:86+15=101,\quad h^{1,1}:2-1=1,\quad b_3:174+2\cdot15=204,\quad \chi:-168\to-200,$$
四项全部对上。反过来，已知 $b_3(\widetilde V)=204$ 与 $n=16$ 时，$b_3(V)=174$ 逼迫 $r=1$。

**4.5 同法核第二个例子（例 6.2.4.3，PDF p.169–170）。** $V\in|4D_3|\subset X_\Sigma$ 有 $(h^{1,1},h^{2,1})=(2,86)$、$b_3=174$（书内给出），其 III 型本原收缩把直纹面收缩到亏格 3 的平面四次曲线；一般复结构形变下有 $2g-2=4$ 条纤维可全纯形变、可同时翻越且满足 1 条关系，故 $n-r=3$：$h^{2,1}:86+3=89$、$h^{1,1}:2-1=1$、$b_3:174+6=180$、$\chi:-168\to-176$，与书内 $h^{1,1}(\widetilde V)=1$、$h^{2,1}(\widetilde V)=89$ 一致。记账规则（本卡从两例归纳，书中无一般公式，待核 Q3）：$\Delta h^{1,1}=-k$、$\Delta h^{2,1}=n-r$、$\Delta b_3=2(n-r)$、$\Delta\chi=2(-k-(n-r))$。

**4.6 与队列提示的差异。** 队列写「$b_3:204\to202$」。本书此例是 $174\to204$；$202$ 需要 $(h^{1,1},h^{2,1})=(2,100)$ 的伙伴（$n=1,r=0$），书中未出现 → §11 Q2 待核，勿引作书内结论。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | 定义只需「双有理收缩 + 奇异簇可光滑化」，不预设收缩类型 | 定义 6.2.9，PDF p.166 | 宽松版本；见 §3.5、§11 C3 |
| 2 | I 型 ⇔ 锥形奇点跃迁；II/III 型也可构成极端跃迁 | PDF p.156、p.166 | 例 6.2.4.3 是 III 型（p.169） |
| 3 | SCFT 模空间中看是两步：固定复结构走 Kähler 边界，再固定 Kähler 作复结构光滑化 | PDF p.167 | 「同时粘合复与 Kähler 模空间比只粘合复模空间更自然」 |
| 4 | 镜像对称预言：跃迁的镜像是 $V^\circ$ 中反向的极端跃迁（[Morrison9]） | PDF p.167 | 书中只在例与第 12 章检验 |
| 5 | Hodge 记账：$\Delta h^{1,1}=-k$、$\Delta h^{2,1}=n-r$、$\Delta b_3=2(n-r)$、$\Delta\chi=2(-k-(n-r))$ | PDF p.167–170 两例 + 本卡 §4 计算 | 书中无一般定理；本卡归纳，待核 Q3 |
| 6 | 环面实现：自反多胞形嵌套 $\Delta\subset\widetilde\Delta$ 给出跃迁，镜像侧方向反转 | 例 6.2.4.2，PDF p.168–169 | 依赖 Batyrev 构造（§4.3，MS-23） |

## 6. 推导流程（D1…Dn）

- **D1.** 取本原收缩 $\phi:V\to\overline V$；其丰沛类拉回给出 $\overline{K(V)}$ 的面 $F$。（依据：PDF p.155 的命题与 p.167 的叙述）
- **D2.** $F$ 的类型由例外集决定：曲线→I 型，曲面映点→II 型，曲面映曲线→III 型。（依据：PDF p.156）
- **D3.** 跨过 $F$ 走出 Kähler 锥：I 型可翻越（得 $V'$，$H^2$ 自然同构）；III 型（$g\ge2$）沿 $2g-2$ 条纤维翻越，$H^2$ 上作用为 $D\mapsto D+(D\cdot f)E$、$E\cdot f=-2$ 的反射。（依据：PDF p.156–157，[Reid2,Kollar]、[Wilson2]）
- **D4.** 固定 Kähler、形变复结构：$\overline V$ 的复模空间是 $\widetilde V$ 复模空间边界的子集，沿 $\overline V$ 光滑化得 $\widetilde V$。（依据：PDF p.167）
- **D5.** 两步在 SCFT 模空间中合成单一跃迁；镜像侧给出 $V^\circ\to\widetilde V^\circ$ 的反向极端跃迁。（依据：PDF p.167，[Morrison9]）
- **D6.** 五次族实例：$\phi$ 是 16 条曲线上的 I 型本原收缩（$H^3=5\ne0$），$\overline V$ 光滑化为五次簇，即锥形奇点跃迁。（依据：例 6.2.4.1，PDF p.167–168；数字见本卡 §4）
- **D7.** 环面实例：$\Delta\subset\widetilde\Delta$ ⇒ 细分 $\pi:X_\Sigma\to X_{\widetilde\Sigma}$ ⇒ $\phi=\pi|_V$；放开被置零的系数 $\lambda_i$ 得 $\widetilde V$；镜像侧因 $\widetilde\Delta^\circ\subset\Delta^\circ$ 而反向。（依据：例 6.2.4.2，PDF p.168–169）
- **D8.** 镜像映射校验：对偶跃迁粘接轨迹 $1-4z_2=0$ 给 $z_2=1/4$，代入镜像映射得 $q_2=1$，即 $t_2\in\mathbb Z$、$\operatorname{Im}t_2=0$，$\omega$ 落在原跃迁的 Kähler 锥面。（依据：PDF p.171 与 §6.3.3 例 2，PDF p.181–182）
- **D9.** 宏观陈述：Reid 幻想的 Kähler 版本与镜像极端跃迁猜想，已在完全交、环面超曲面与旗流形等处部分检验。（依据：第 12 章，PDF p.428–429；[ACJM,CGGK,BCFKvS1,BCFKvS2]）

## 7. 常见误解与反例（≥2）

- **误解 1：极端跃迁就是一次双有理收缩。** 错。定义 6.2.9（p.166）含两个环节：收缩到 $\overline V$，**再**把 $\overline V$ 光滑化。只有收缩没有光滑化时拓扑不变，不构成跃迁。反例：同一 $V$ 的两个翻越模型之间只差一次翻越，$b_3$ 不变（p.156），而跃迁改变 $b_3$（§4：$174\to204$）。
- **误解 2：锥形奇点跃迁是极端跃迁的通名。** 错。只有 I 型才叫锥形奇点跃迁（p.166）。反例：例 6.2.4.3 的 III 型本原收缩把直纹面爆缩到亏格 3 曲线，随后光滑化为 $\mathbb P^5$ 中的 $(2,4)$ 完全交（p.169–170）；它是极端跃迁，但不是锥形奇点跃迁。
- **误解 3：跃迁是拓扑不变的变形，两边 Hodge 数相同。** 错。例 6.2.4.1 中 $h^{1,1}:2\to1$、$h^{2,1}:86\to101$、$b_3:174\to204$、$\chi:-168\to-200$（本卡 §4 手算，与书内光滑化端 $(1,101)$ 及 $H^3=5$ 相容）。
- **误解 4：既然镜像映射把 Kähler 模空间等同于复模空间，对偶跃迁应沿 $|z_2|=1$ 粘接。** 错。p.171 指出：恒等映射会给出 $|z_2|=1$；实际判别式轨迹是 $1-4z_2=0$，即 $z_2=1/4$，代入镜像映射后 $q_2=1$，才与「$\operatorname{Im}t_2=0$ ⇔ $|q_2|=1$ ⇔ $\omega$ 落在 Kähler 锥面」相容。
- **误解 5：Reid 幻想已被证明。** 目前只是猜想（p.166、p.428–429）：已验证的只是若干类（完全交、环面超曲面 7555 例 [ACJM,CGGK]、旗流形 [BCFKvS1,BCFKvS2]），书中把它当动机而非定理。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999（本书） | PDF p.166（印刷 143），§6.2.4 | 定义 6.2.9（引自 [Morrison9]）、I 型 = 锥形奇点跃迁、Reid 幻想 |
| Cox–Katz 1999（本书） | PDF p.167–171（印刷 144–148），§6.2.4 | 例 6.2.4.1（五次族，p.167–168）、例 6.2.4.2（环面，p.168–169）、例 6.2.4.3（III 型，$(2,86)\to(1,89)$，p.169–171）、镜像映射≠恒等（p.171） |
| Cox–Katz 1999（本书） | PDF p.155–157（印刷 132–134），§6.2.2 | 本原收缩定义、Wilson 命题、I/II/III 型、翻越、III 型反射；**注意**：队列所写「§6.4」无此内容（§6 只有 §6.1–§6.3，见 §11 Q1） |
| Cox–Katz 1999（本书） | PDF p.428–429（印刷 405–406），第 12 章「锥形奇点跃迁」 | 收尾重述、镜像极端跃迁猜想的检验清单、旗流形完全交构造 |
| SY01-24（Siebert 讲义中译本，术语表 70 条） | 无 conifold／极端跃迁／跃迁条目（关键词 0 命中）；第 15 条「消失循环」p.18、第 18 条「单值变换」p.21 | **冲突**：本卡按 _冲突表 T2 用「消失圈」、T1 用「单值性」；SY01-24 作「消失循环」「单值变换」并声明全书统一「单值变换」→ §11 C1/C2，不判定 |
| SY01-25 资料卡（04-术语文献勘误） | §一 25 条术语、§二 34 条文献（[Se]「消没圈」与变异）；无跃迁条目 | **冲突**：其侧用「消没圈」；本卡用「消失圈」（_冲突表 T2）→ §11 C2 |
| Greene–Morrison–Strominger 1995（[GMS]） | Nucl. Phys. B451 (1995) 109；hep-th/9504145 | 例 6.2.4.1 的原始出处：16 结点五次簇的锥形奇点跃迁与黑洞凝聚（p.167 引用） |
| Morrison 1997（[Morrison9]） | Through the Looking Glass，alg-geom/9705028 | 定义 6.2.9 的来源与「镜像跃迁 = 反向跃迁」猜想（p.166–167 引用） |
| Reid 1987（[Reid5]） | Math. Ann. 278 (1987) 329–334 | Reid 幻想：Calabi–Yau 三维簇复模空间经跃迁连通（p.166 引用） |
| CdFKM 1994（[CdFKM]） | Nucl. Phys. B416 (1994) 481–538；hep-th/9308083 | 双参数模型；例 6.2.4.3 的判别式 $1-4z_2=0$ 与镜像映射来源（p.169–171 引用） |
| BCFKvS 1998（[BCFKvS1]） | Nucl. Phys. B514 (1998) 640–666；alg-geom/9710022 | 检验镜像极端跃迁的例子：Grassmann 流形中的完全交（p.428–429 引用） |
| B 级：nLab「conifold transition」 | https://ncatlab.org/nlab/show/conifold+transition（2026-08-04 修订） | 索引条目：Reid 1987、Green–Hübsch、Avram–Kreuzer–Skarke 的 Calabi–Yau 网络；相邻条目 flop transition / conical singularity |

## 9. 前置与后继

- **前置**：**MS-09** 自反多胞形——例 6.2.4.2 的 $\Delta\subset\widetilde\Delta$ 与 Batyrev 构造（PDF p.168–169）；**MS-14** 消失圈——I 型跃迁中「结点 → 消失 3-圈」的语言（PDF p.166、p.428）；**MS-03** 五次三维簇——例 6.2.4.1 的光滑化端 $(1,101)$ 与 $h^{2,1}=126-25$；**MS-21** GLSM 与相（队列所列前置，§6.2.4 开头 PDF p.166 的 GLSM 语境要用，该卡**尚未建**）。
- **补充隐含前置**：例 6.2.4.2/6.2.4.3 使用 Batyrev 镜像构造与 nef 分拆（§4.3，PDF p.076–087；MS-23），队列未列 MS-23。
- **后继**：**MS-01** 镜像对称（反向跃迁是镜像预言的检验场景，PDF p.171）；第 12 章旗流形完全交构造与 Reid 幻想的 Kähler 版本（PDF p.428–429，队列无独立卡）。

## 10. 形式化接口（Lean 可 sorry）

```lean
-- 只给签名与关键假设，允许 sorry
structure CY3 where
  h11 : ℕ
  h21 : ℕ

namespace CY3
def b3 (V : CY3) : ℕ := 2 + 2 * V.h21
def euler (V : CY3) : ℤ := 2 * ((V.h11 : ℤ) - (V.h21 : ℤ))
end CY3

/-- §6.2.2（PDF p.156）：本原收缩的三型 -/
inductive ContractionType | I | II | III

/-- 定义 6.2.9（PDF p.166）：双有理收缩 φ : V → V̄，且 V̄ 可光滑化为 Calabi–Yau 三维簇 Ṽ -/
structure ExtremalTransition (V V' : CY3) where
  type : ContractionType
  primitive : Prop
  smooths : Prop

/-- I 型极端跃迁 = 锥形奇点跃迁（PDF p.166） -/
def IsConifoldTransition {V V' : CY3} (T : ExtremalTransition V V') : Prop :=
  T.type = ContractionType.I

/-- 记账（本卡 §4 归纳，书中无一般公式，待核 Q3）：
    k = 收缩的独立曲线类数，n = 结点数，r = 消失圈的关系数 -/
theorem hodge_shift {V V' : CY3} (T : ExtremalTransition V V') (k n r : ℕ)
    (h1 : V'.h11 + k = V.h11) (h2 : V'.h21 + (n - r) = V.h21) :
    V'.euler = V.euler - 2 * ((k : ℤ) + ((n - r : ℕ) : ℤ)) := by sorry

/-- 例 6.2.4.1（PDF p.167–168）：16 结点、1 条关系，174 + 2·15 = 204 -/
theorem quintic_conifold_example :
    (174 : ℤ) + 2 * ((16 - 1 : ℕ) : ℤ) = 204 := by sorry
```

## 11. 待核清单

- [ ] **C1 术语冲突（单值性）**：SY01-24 术语表第 18 条作「单值变换」并在「本轮的术语改动」声明全书统一；本项目 _冲突表 T1 裁定「单值性」。本卡正文从 T1，不判定两处孰是，提交 lead 终裁并同步 _冲突表。
- [ ] **C2 术语冲突（消失圈）**：SY01-24 第 15 条作「消失循环」，SY01-25 资料卡用「消没圈」；本卡从 _冲突表 T2「消失圈」。同上待终裁。
- [ ] **C3 定义宽严**：定义 6.2.9（p.166）未要求 $\phi$ 本原、$\overline V$ 射影正规、$\rho$ 下降，而 §6.2.2 的收缩定义（p.155）要求后两者；两处是否等价于通行的「双有理收缩」，待核。
- [ ] **Q1 队列定位**：队列记「第 3 章 §3.5；第 6 章 §6.4」。实际第 6 章无 §6.4，内容在 §6.2.4（PDF p.166–171）；第 3 章 §3.5 是「Fano 簇与自反多胞形」（PDF p.069–070，MS-09 主位）。建议改队列（本人不改既有文件）。
- [ ] **Q2 队列例子**：队列写「$b_3:204\to202$」。书中例 6.2.4.1 是 $174\to204$；$202$ 需 $(2,100)$ 伙伴（$n=1,r=0$），本书未出现，单结点情形的小消解是否 Kähler 亦未讨论 → 待核。
- [ ] **Q3 记账规则**：$\Delta h^{1,1}=-k$、$\Delta h^{2,1}=n-r$、$\Delta b_3=2(n-r)$ 由例 6.2.4.1、6.2.4.3 归纳，书中无一般公式；待与专论 III 型收缩 Hodge 数公式的文献核对。
- [ ] **Q4 例 6.2.4.3 的关系数**：书中只说 $2g-2=4$ 条纤维形变、可同时翻越，未明写关系数；$r=1$ 由 $\Delta b_3=6$ 反推，待核。
- [ ] **Q5 [Morrison9] 出版信息**：书中仅给 arXiv alg-geom/9705028，正式出版信息待核。
- 非空则 status ≠ frozen（本卡 status: draft）。

> 书内页码一律 PDF 物理页（=\SourcePage{N}，印刷页 +23）；外部文献用原书页码或定理号。
