# BRIEF —— SY02-40《Arkhipov–Bezrukavnikov 等价（Sandvik BunG 讲义）》

## 原文

| 项 | 内容 |
|---|---|
| 原题 | *The Arkhipov–Bezrukavnikov Equivalence* |
| 作者 | Colton Sandvik |
| 出处 | BunG 讨论班报告（2025-01-29）的 expository notes；无 arXiv 编号、无出版信息 |
| 规模 | 13 页（PDF 页 = 印刷页，偏移 0）；正文 p.1–12，参考文献 p.13 |
| 结构 | §1 引言（定理 1.0.1、提纲 1.0.2）；§2 中心层与 Wakimoto 层（2.1 $p$ 进动机、2.2 附近循环、2.3 仿射 Grassmann 簇与仿射旗簇、2.4 Gaitsgory 中心函子、2.5 Wakimoto 层、2.6 反球商）；§3 Springer 解消上的凝聚层（3.1 Springer 解消、3.2 函子 I、3.3 函子 II、3.4 函子 III）；§4 反球范畴与 Iwahori–Whittaker 层（4.1 Whittaker 层热身、4.2 IW 范畴、4.3 最高权结构、4.4 IW 平均、4.5 中心层与倾斜层）；§5 等价（定理 5.0.1、推论 5.0.2） |
| 编号条目 | 定理类共用按节计数器：1.0.1、命题 2.2.2、定义 2.2.1、定理 2.4.1、注 2.4.3、命题 2.5.1/2.5.2、定理 2.5.3、引理 2.5.4、引理 3.1.1、命题 3.1.2、引理 3.2.1、注 4.0.1、例 4.1.1、命题 4.3.1、推论 4.3.2、定理 4.4.1、定理 4.5.1、定理 5.0.1、推论 5.0.2；另有无编号的「旁注 2.4.2」 |
| 编号公式/交换图 | 8 条：(1) 反球模定义、(2) $K$ 群同构、(3) 附近循环的交换图、(4) Springer 侧三空间图、(5)(6) $\mathrm{Av}^{\mathrm{IW}}$ 作用、(7) 对象对应表、(8) $\mathrm{Hom}$ 比较映射 |
| 脚注 | 14 条，顺序与原文一致 |
| 文件 | 微信「文件」页签：`BunG_Seminar_2025-01-29_ArkhipovBezrukavnikov_Equivalence.pdf`（505.0K） |
| 底本 | `工程文件/work/原文/fulltext.txt`（逐页文本，带 `PDF p.n` 标记）；原 PDF 不入仓 |

**原文性质。** 讨论班讲稿的 expository notes，不是研究论文，也不是完整讲义。五个特点决定了译法：

1. **一句话一个论断，几乎不证**。全文除定理 2.4.1、定理 4.4.1、定理 4.5.1、定理 5.0.1 给了「证明/证明梗概」外，其余命题与引理只作陈述，把证明交给 [ArBe]、[Gai1]、[AcRi]。译文不补证明，只在译注里标出落点。
2. **两套语言来回切换**。§2–§3 在 Betti 层（复数域、$D^b_c$）里做，§4 起明确改到 étale 设置（注 4.0.1：$F=\overline{\mathbb F}_p$、$\ell\ne p$、$\mathbb Q_\ell$-层）。译文必须让这个切换显式可见，否则 §4 的 $\mathrm{Av}^{\mathrm{IW}}$ 会显得凭空出现。
3. **三层范畴，一层比一层弱**：$D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to D^b\mathcal P_I^{\mathrm{asph}}$（反球商）$\to D^b\mathcal P_{\mathrm{IW}}$；中间那层是 Serre 商，最后一层是最高权范畴。译文的节标题与「本节重点」要反复提醒读者现在站在哪一层。
4. **记号拥挤**：$G$ 在 §1–§3 与 $G^\vee$ 交替出现，$\widetilde{\mathcal N}$、$\widehat{\mathcal N}$、$\widehat{\mathcal N}_X$ 三个相近记号必须逐处核；$I$ 既是 Iwahori 子群也是 $L^+G$ 的 Iwahori，$I^+_u$ 是另一层。译文在首次出现处给译注，不擅自改记号。
5. **原文自认的缺口**：§3.4「This can be checked rather explicitly, and is omitted」、§2.4 旁注 2.4.2（中心比像大）、§4.5 拟极小情形「much more difficult」。这些是原文的诚实标记，译文照译并登记，不掩饰。

## 一句话主旨

反球模 $M^{\mathrm{asph}}$ 有三种等价描述（反球 Hecke 范畴的 $K$ 群、$G^\vee$-等变 Springer 解消上凝聚层的 $K$ 群、$q$-形变后的 Whittaker 模），Arkhipov–Bezrukavnikov 把它们**范畴化**成三向等价
$$D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\;\simeq\;D^b\mathcal P_I^{\mathrm{asph}}\;\simeq\;D^b\mathcal P_{\mathrm{IW}},$$
中介工具是 Gaitsgory 的中心函子（由中心仿射 Grassmann 簇上的附近循环给出）与 Wakimoto 层（其滤链的多重数就是权空间维数）。

## 五步逻辑链

1. **把三种描述摆出来**（§1）：$M^{\mathrm{asph}}=\mathbb Z\otimes_{\mathbb Z[W]}\mathbb Z[W_{\mathrm{ext}}]$（符号表示诱导），$K_0$ 上等于 $[D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})]$（式 (2)），又是 $q$-形变的 Whittaker 模；三条路各给一个候选范畴化。
2. **造中心层**（§2.1–2.4）：$p$ 进侧 Bernstein 同构 $\mathcal Z(C(I\backslash G_F/I))\cong C(G_{\mathcal O}\backslash G_F/G_{\mathcal O})$ 的逆需要几何化 → 用中心仿射 Grassmann 簇 $\mathrm{Gr}^{\mathrm{cen}}_G\to\mathbb C$ 上的附近循环定义 $Z$，定理 2.4.1 说它幺半、$t$-正合、像落在中心、$\pi_*Z(F)\cong F$。
3. **造 Wakimoto 层并给滤链**（§2.5）：$\mathbb W_\lambda:=\nabla_{\lambda_1}\star_I\Delta_{-\lambda_2}$ 与选择无关、支撑在 $\mathrm{Fl}_{G,\lambda}$、满足 $\mathbb W_\lambda\star\mathbb W_\mu\cong\mathbb W_{\lambda+\mu}$；定理 2.5.3 说 $Z(F)$ 有 Wakimoto 滤链，重数 $=\dim(\mathrm{Sat}^{-1}(F))_\lambda$。这一步把「几何侧的多重数」与「表示侧的权空间」接上。
4. **从凝聚层造到反球侧**（§3）：以 $\widetilde{\mathcal N}$ 上的线丛 $\mathcal O(\lambda)$ 与 $V\otimes\mathcal O$ 为生成元（引理 3.1.1），先用 $V\otimes k_{T^\vee}(\lambda)\mapsto Z(\mathrm{Sat}(V))\star\mathbb W_\lambda$ 造函子 I，再用 Tannakian 形式升级到 $\widehat{\mathcal N}_X$ 上的自由凝聚层（函子 II），最后用「$\partial X$ 上支撑的复形被打到零」下降成 $D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to D^b\mathcal P_I$（函子 III）。
5. **换到 Whittaker 侧并对撞**（§4–§5）：$\mathrm{Av}^{\mathrm{IW}}$ 把 $\mathrm{IC}_w$（$w\notin\widetilde W_{\mathrm{ext}}$）打零、把标准/余标准送到 $\Delta^{\mathrm{IW}}_\lambda/\nabla^{\mathrm{IW}}_\lambda$，因而是 $t$-正合且经反球商分解，且在 $\mathcal P_I^{\mathrm{asph}}\to\mathcal P_{\mathrm{IW}}$ 上全忠实；定理 4.5.1 说 $Z^{\mathrm{IW}}(V)$ 是倾斜层、重数 $=\dim V_\lambda$。合成 $\mathrm{F}^{\mathrm{IW}}$ 后，$\mathrm{Hom}$ 两边都用定理 4.5.1 算成 $\dim V_{-\lambda}$（$n=0$）或 $0$，主定理随之落地。

## 分块表

| 块 | 节 | PDF 页 | 编号条目 | 目标文件 | 状态 |
|---|---|---|---|---|---|
| 1 | §1 引言 | 1–2 | 定理 1.0.1、提纲 1.0.2、式 (1)(2) | `body1.tex` | ☑ |
| 2 | §2.1–2.3 | 2–3 | 定义 2.2.1、命题 2.2.2、式 (3) | `body1.tex` | ☑ |
| 3 | §2.4 | 3–4 | 定理 2.4.1、旁注 2.4.2、注 2.4.3 | `body1.tex` | ☑ |
| 4 | §2.5–2.6 | 5–6 | 命题 2.5.1、2.5.2、定理 2.5.3、引理 2.5.4 | `body1.tex` | ☑ |
| 5 | §3.1 | 6–7 | 引理 3.1.1、命题 3.1.2、式 (4) | `body2.tex` | ☑ |
| 6 | §3.2–3.4 | 7–8 | 引理 3.2.1 | `body2.tex` | ☑ |
| 7 | §4.0–4.3 | 8–10 | 注 4.0.1、例 4.1.1、命题 4.3.1、推论 4.3.2 | `body2.tex` | ☑ |
| 8 | §4.4–4.5 | 10–11 | 式 (5)(6)、定理 4.4.1、定理 4.5.1 | `body2.tex` | ☑ |
| 9 | §5 | 11–12 | 式 (7)(8)、定理 5.0.1、推论 5.0.2 | `body3.tex` | ☑ |
| 10 | 参考文献 | 13 | 5 条 | `body3.tex` | ☑ |

### 完稿对账

| 项 | 原文 | 译本 |
|---|---|---|
| 页数 | 13（正文 1–12 + 文献 13） | 21（含封面、目录、译注与「本节重点」） |
| 编号公式/图 | 8 | 8，逐条对齐 |
| 定理类条目 | 19（含旁注 2.4.2 与注 4.0.1） | 19，编号与原文一致 |
| 脚注 | 14 | 14 |
| 编译 | — | `xelatex` 三遍，0 error，0 缺字，0 undefined |
| 译注 | — | 橙框「译注」与蓝框「本节重点」为译者所加，正文明确标注 |

## 施工流程

1. 通读原文 13 页（`work/原文/fulltext.txt`）；2. 逐节译进 `源码/body1–3.tex`，每节译完即编译；3. 全稿三遍编译；4. `工程文件/work/glossary.tsv` 冻结术语；5. 资料卡五件套；6. 登记 `RELEASE_REGISTER.csv` 与 `03_translations_meta/SY02-40/`；7. `make_stats.py --write`；8. 推送 AtomGit。

## 质量标准

- 逐句译，不合并、不拆分段落；不增不删。
- 编号（定理 1.0.1、公式 (3)）一律照原文，不改号、不补号。
- 术语只取 `work/glossary.tsv`；新术语先入表再入正文。
- 译注只写读者自己推不出来的信息（论文落点、记号冲突、原始缺口），每条带依据。
- 明确区分「原文陈述」与「译者补充」：译者所加一律进橙框/蓝框，正文不混。
