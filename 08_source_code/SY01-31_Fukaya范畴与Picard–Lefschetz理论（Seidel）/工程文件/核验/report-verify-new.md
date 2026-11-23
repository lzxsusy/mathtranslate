# 新增概念卡核验报告（16 张）

- 核验日期：2026-11-19
- 范围：`cards/concepts/` 下 16 张新增概念卡（operad … a-m-singularity），status 一律保持 `draft`，各卡新增 `"verified_at": "2026-11-19"`。
- 方法：每卡按 `sources.pages` 与 `theorem.source` 的页码，回 PDF 页图（印刷页 + 8 = PDF 页，150 dpi，`work/pages/new-<PDF页>.png`）逐条对照 `definition / key_points / formulas / theorems / pitfalls / sources`；每张至少实读 1 张页图，公式卡核到对应公式页。文本层（`pdftotext -layout`）只用于定位，不作为判定依据。
- 外部依据：卡内出现的 nLab / arXiv 条目全部 `web_fetch` 实际打开（HTTP 200），逐条比对卡内转述；见各卡 evidence。
- 收尾自检：`python tools/lint_cards.py --strict` → `卡片 70 张（概念 32，推导 8，勘误 30）`、`OK：0 error，0 warn`。

## 分类小结

| 类别 | 张数 | 卡 |
| --- | --- | --- |
| 改错（内容确有错） | 6 | operad、homological-perturbation-lemma、yoneda-embedding、quasi-isomorphism、dehn-twist、picard-lefschetz-formula |
| 只改页码/出处（内容无误） | 6 | mapping-cone、directed-a-infinity-category、maslov-class、spectral-flow、pin-structure、lefschetz-fibration-fukaya-category |
| 原样通过（仅加 verified_at） | 4 | kadeishvili-theorem、exceptional-object、serre-functor、a-m-singularity |

---

## 1. operad

核了 p.7（PDF 15，"we do not use operads"）、p.8（PDF 16，式 (1.2)）、p.17（PDF 25，命题 1.12 与式 (1.18)）、p.19（PDF 27，注 1.15 的 "cofibrant property of the operad governing A∞-structures, see [99]"）；实读页图 `new-016.png`、`new-025.png`。外部打开 nLab `operad` 与 `A-infinity-algebra`：合成映射 γ、O-代数定义、A∞-操作子分辨的表述均与卡一致。
改动：`formulas[2]` 的 A∞ 关系符号原写作 `$(-1)^{r+st}$`，与原书 (1.2) 的 `$(-1)^{\star_n}$`（`\star_n=|a_1|+\cdots+|a_n|-n`，见 p.8 页图）不符，改为 `$(-1)^{\star_r}$` 并补上 `\star_r` 的定义，与同目录 `a-infinity-algebra.json` 的约定一致。
存疑：卡内 `$\mathcal A_\infty(n)=C_*(K_n)$` 的 `$K_n$` 是译者对胞腔模型的简化记号，原书未用；定义与 key_points 不受影响，未改。

## 2. homological-perturbation-lemma

核了 p.17（命题 1.12、式 (1.18)）与 p.18（注 1.13、推论 1.14）；实读 `new-025.png`、`new-026.png`。外部打开 nLab `homological+perturbation+theory`（`f∇=1`、`∇f=1+dΦ+Φd`、`Φ^τ=Σ_{r≥0}Φ(1+d^τΦ)^r`）。
改动（本批最大的一处）：原卡把经典形变收缩的假设 `$G^1F^1=\mathrm{id}$` 塞进了命题 1.12 的假设，并断言 `$F,G$` 是拟同构。原书命题 1.12 只假设 `$\mu^1_BT^1+T^1\mu^1_B=F^1G^1-\mathrm{id}$`，结论只到 `$F\circ G\simeq\mathrm{Id}_{\mathcal B}$`；只有注 1.13（p.18）的分裂情形（`$F^1$` 含入、`$G^1$` 投影）才有 `$G\circ F\simeq\mathrm{Id}_{\mathcal A}$`，此时 `$F,G$` 才是拟同构。据此改了 `definition`（加一段区分经典版本与命题 1.12）、`theorems[0].statement`、`key_points[3]`、`pitfalls[1]`，并补 `proof.gap_note`。式 (1.18) 两条分拆求和本来正确，未动。
存疑：卡内经典 HPL 部分（收敛性、`$\Phi^\tau$` 级数）依据是 nLab 条目而非原书，已在 `provenance_note` 标明。

## 3. kadeishvili-theorem

核了 p.17（命题 1.12）、p.18（注 1.13 的分裂构造、推论 1.14 "Any quasi-isomorphism between non-unital A∞-categories has an inverse up to homotopy"）、p.19（注 1.15 历史）；实读 `new-025.png`、`new-026.png`。外部打开 nLab `A-infinity-algebra`（Kadeishvili 1980 / Merkulov 1999 的极小模型定理）。
结论：逐条一致，未发现错误，未改内容（仅加 `verified_at`）。

## 4. yoneda-embedding

核了 p.21（§1l、(1.23)、(1.24)、(1.25)：(1.25) 即 `$\lambda_{\mathcal M}(c)^d(b,a_{d-1},\ldots,a_1)=\mu^{d+1}_{\mathcal M}(c,b,a_{d-1},\ldots,a_1)$`）、p.22（注 1.17 的线性化函子 `$L$`）、p.30（引理 2.12：`$\mathcal M$` c-unital 时 `$\lambda$` 是拟同构）、p.31（推论 2.13：`$\mathcal I$` 同调全忠实）；实读 `new-029.png`。外部打开 nLab `Yoneda+embedding`（仅作背景）。
改动：① 定理假设由「`$\mathcal A$` 是 c-unital」改为「`$\mathcal M$` 是 c-unital 模」（原书引理 2.12 的真实条件），并补 p.30–31 出处；② 删除「每个线性 A∞ 范畴都 A∞ 等价于某个 dg 范畴」——注 1.17 只说 `$L$` 的像中模同态只有一阶项；③ `key_points[3]` 原写「`$D(\mathcal A)=H^0(\mathrm{mod}\,\mathcal A)$` 再取 Karoubi 包络，这是 §10 用模范畴代替 `$\mathcal A$` 的依据」，p.19–22 无此内容（Karoubi 全书出现于 p.275 附近），改为 (1.23) 的拉回相容性；④ `key_points[0]`「全忠实」改为「同调全忠实」；⑤ `pitfalls[3]` 相应改写；⑥ `sources` 增补 §2g p.30–31。
存疑：卡内「`$\mathcal Y$` 叫自由模」是译者措辞（原书用 Yoneda module / representable），未改。

## 5. mapping-cone

核了 p.35（§3e：`$\mathcal C(X)=\hom_{\mathcal A}(X,Y_0)[1]\oplus\hom_{\mathcal A}(X,Y_1)$`、(3.6)、(3.7) 的 `$t^1,t^d$`、注 3.5）与 p.36（§3f、引理 3.6）；实读 `new-043.png`。卡文与 (3.6)、(3.7) 逐字符一致，含 `$t^1=((-1)^{|b_0|-1}b_0,(-1)^{|b_1|}b_1+\mu^2_{\mathcal A}(h,b_0))$` 与同构由 Lemma 1.16 给出的说明。
改动：`sources` 补 `pdf_pages` `[43,43]`、`[44,44]`（原卡缺该字段）。
存疑：无。

## 6. quasi-isomorphism

核了 p.9（§1b：拟同构 = `$H(F)$` 为范畴同构，另定义同调全忠实；注 1.1(iii) 说明非含幺情形「等价」无意义）、p.28（§2e 拟等价定义）、p.29（定理 2.9 与引理 2.5）；实读 `new-037.png`。
改动：① `definition` 中「若 `$\A,\B$` 带严格单位元，`$c$`-含幺函子 `$F$` 的 `$H(F)$` 只可能是范畴同构或不是（全忠实加本质满射），此时「拟同构」与「`$H(F)$` 是等价」重合」一句自造且含糊，按 p.9 注 1.1(iii) 与 p.28 §2e 重写，并点明范畴同构强于等价；② `key_points[0]` 相应改为「拟同构是拟等价的特例」；③ 定理 2（拟同构一般无严格逆）的 source 原挂「原书 p.17 §1、p.29 §2e」，属误挂，改为 p.9 §1b 并注明该反例（如 `$\Z\xrightarrow{\cdot2}\Z\to\Z/2$`）原书未给；④ `sources` 改为 §1b `[9,9]` 与 §2e `[28,29]`（原卡缺 p.9 与 p.28，却挂 p.17）。
存疑：定理 2 的反例是标准链复形例子，书中未作为命题给出，已在 source 中明示。

## 7. exceptional-object

核了 p.75（§5i：例外对象 `$\mathrm{Hom}_{H(\mathcal A)}(Y_k,Y_k)=\mathbb K[e_{Y_k}]$`、`$k>l$` 时为零、full collection 按 §3j 生成；引理 5.13 `$T_{Y_1}\cdots T_{Y_m}(X)\cong0$`）与 p.76（证明：`$X_m=X$`、`$X_{k-1}=T_{Y_k}(X_k)$`、(5.4)、`$\mathrm{Cone}(e_{Y_l})\cong0$`、推论 3.9 保正合三角、(5.23) Postnikov 梯）；实读 `new-083.png`。
结论：逐条一致，未发现错误，未改内容（仅加 `verified_at`）。

## 8. directed-a-infinity-category

核了 p.80（§5m 定义：严格含幺、m 个有序对象、`$i>j$` 时 0、`$i=j$` 时 `$\mathbb K e_{Y_i}$`、`$i<j$` 有限维）、p.81（(5.30)–(5.32)）、p.86（推论 5.26 `$P$` 是 `$\mathcal A^\to$` 的三角包络）、p.87（推论 5.27 "Any directed A∞-category is quasi-isomorphic to another one which is also directed, and which is actually a dg category"）；实读 `new-088.png`。
改动：`sources` 的 §5p 由 `[87,87]` 改为 `[86,87]`（推论 5.26 在 p.86），anchor 改「原书 p.86–87 §5p」。
存疑：无。

## 9. maslov-class

核了 p.157（§11e："the Maslov class `$\mu\in H^1(Gr(V))$`"、"`$w_1$` is the mod 2 reduction of `$\mu$`"、"The pairing with `$\mu$` is an isomorphism `$\pi_1(Gr(V))\to\Z$`"、(11.15)）、p.158（引理 11.7 与 (11.16)）、p.159–160（§11f 的路径 Maslov 指标、交叉型 `$q_{\Lambda_0,\Lambda_1}$`）；实读 `new-165.png`。外部打开 nLab `Maslov+index`（`$H^1(LGrass,\Z)\cong\Z$` 的生成元、拉回 `$i^*u$`）。
改动：`sources` 的 §11e 由 `[157,158]` 扩为 `[157,160]`，anchor 改「原书 p.157–160 §11e–§11f」（卡内定理 1 本就引到 p.160）。
存疑：nLab 条目讲的是路径的 Maslov 指数，与卡内 `$H^1(Gr(V))$` 类只是同一对象的不同面向，卡内措辞已按原书，未混用。

## 10. spectral-flow

核了 p.151（§11b：`$I:\mathcal P\to\Z$`、线丛）、p.152（引理 11.2："`$I(\alpha)=\mathrm{index}(d_\alpha)$`; moreover, `$\delta$` is canonically isomorphic to the determinant line bundle of the family `$\{d_\alpha\}$`"）、p.153（证明：扩域、`$\ker\cong\Theta_\alpha(0)$`、(11.7)、穿零点累加）、p.159–160（§11f）；实读 `new-160.png`。外部打开 nLab `spectral+flow`（自伴 Fredholm 算子谱的正负穿越计数）。
改动：定理 2（谱流 = Maslov 指标）的 source 由「原书 p.152 §11b；Robbin–Salamon（转引）」补为「p.152 §11b；p.159–160 §11f（路径的 Maslov 指标）；见 Robbin–Salamon（转引）」；`sources` 增 §11f `[159,160]` 条目。
存疑：「谱流 = Maslov 指标」的证明不在 §11b，靠 Robbin–Salamon（原书书目 [112] Topology 32 (1993) 827–844、[113] Bull. LMS 27 (1995) 1–33），卡内已标「转引」。

## 11. pin-structure

核了 p.166（§11i：`$\mathrm{Pin}_n$` 是 `$O_n$` 的 `$\Z/2$` 中心扩张、取 `$w_2$` 分类者、Clifford 构造 `$v^2=\|v\|^2e$`、扭曲共轭 `$w\mapsto -vwv$`、引理 11.14 与 (11.29) `$(-1)^{\frac12\mathrm{rank}F^{\mathrm{anti}}(\mathrm{rank}F^{\mathrm{anti}}-1)}e$`、注 11.15：本书 `$\mathrm{Pin}_n=\mathrm{Pin}_{0,n}=\mathrm{Pin}^+_n$`，另一版 `$\mathrm{Pin}_{n,0}=\mathrm{Pin}^-_n$` 障碍 `$w_2+w_1^2$`、反射原像阶 4）、p.167（障碍 `$w_2$`、`$H^1(B;\Z/2)$` 仿射空间、`$P^\#\otimes\beta$`、(11.30) `$\mathrm{Aut}(P^\#)\cong\mathrm{Pin}(F\otimes\Lambda^{top}F)$`、注 11.16 扭曲版障碍 `$w_2(F)+w$`）；实读 `new-174.png`（p.166 整页与文本层逐句一致）。外部打开 nLab `pin+group` 与 `twisted+spin+structure`。
改动：仅把 `sources` 的 anchor 精确为「原书 p.167–168 §11i」。
存疑：无（两版本 Pin 群、障碍类、torsor 结构、自同构群全部对得上）。

## 12. serre-functor

核了 p.180（(12.15) `$\int_{L^\#}:HF^n(L^\#,L^\#\otimes\Lambda^{top}TL)\cong H^n(L;|\Lambda^{top}TL|_K)\cong H_0(L;\mathbb K)\to\mathbb K$`、配对非退化且分次对称）、p.181（"not in general a Frobenius category, except if `$\xi_M$` is trivial"）、p.189（§12j：抽象 Serre 函子 `$D:\mathcal A\to\hat{\mathcal Q}\mathrm{mod}(\mathcal A)$`、`$Y^-(X)=\hom_{\mathcal A}(Y,X)^-$`、弱 CY 条件）、p.190（用 pointed discs 加单个内部标记点、Lemma 1.6 与 Floer Poincaré 对偶构造同构）；实读 `new-188.png`。外部打开 nLab `Serre+functor`。
结论：逐条一致，未发现错误，未改内容（仅加 `verified_at`）。

## 13. dehn-twist

核了 p.223（§16c：framed exact Lagrangian 球面、`$b(r)=0\ (r\ge s)$`、`$b(r)-b(-r)=-r$` (16.5)）、p.224（`$H(x)=b(|\xi^{-1}(x)|)$`、时间 `$2\pi$` 流、exact、`$[\tau_V]$` 不依赖定向、(16.6) `$h_\gamma\simeq\tau_{V_\gamma}$`、"We will not give the proof here"）、p.232（§16h 引理 16.13 与 (16.10) `$\Sigma_{\tau,I}\simeq\tau_{\Sigma_{\tau_1,I_1}}(\Sigma_{\tau_0,I_0})$`）、p.261（推论 17.17）、p.283–284（§18g）、p.289（§18l：`$\delta^{1/2}\in\mathrm{Br}_m$` 几何上是沿边界平行圆的负 Dehn 扭转的平方根）；实读 `new-231.png`、`new-232.png`。外部打开 nLab `Dehn+twist`。
改动：① 定理 2 的 statement「在纤维中有同痕」改为「存在 framed Lagrangian 球面在总空间 `$E$` 中的同痕」，并补式 (16.10) 的精确形式；② 其 source 由「原书 p.232 §16」精确为「p.232 §16h Lemma 16.13」；③ `key_points[4]` 的 §18l 归属核对后改写为 `$\delta^{1/2}$` 与「负 Dehn 扭转的平方根」；④ 定理 1 的 `gap_note` 改为原书明确不给证明（p.224）；⑤ `sources` 重排为 §16c `[223,224]`、§16h `[232,232]`、§16c 注 16.6 + §17 推论 17.17 `[224,261]`、§18g–§18l `[283,289]`，删去原「§18g 原书 p.284」这条与本章内容对不上的出处。
存疑：公式 `$\tau_L(S)=S+\langle S,L\rangle L$` 只在实二维纤维（`$n=2$`）下用这个符号，卡内 `pitfalls[0]` 已声明；原书 §16c 只给几何版，同调版属经典表述。

## 14. picard-lefschetz-formula

核了 p.223–224（§16c：(16.5)、(16.6) 与「不给证明」）、p.225–226（§16d：Hurwitz 移动、辫群 `$\mathrm{Br}_m$` 作用）、p.283–284（§18g：复合单值 = monodromy）；实读 `new-232.png`。外部打开 nLab `Picard-Lefschetz+theory`（"starting point is the Picard-Lefschetz formula describing monodromy at a critical point"，并列出本书为参考）。
改动：① `definition` 的维数自相矛盾：原文写「`$\dim_\R F=n$`，故 `$\delta\cong S^{n-1}$`」并让公式作用在 `$H_{n-1}(F)$`——`$n-1$` 维球面在 `$n$` 维流形里不是中间维，相交形式退化。按 `$\dim_\C F=n-1$`（即 `$\dim_\R F=2(n-1)$`）修正后 `$\delta\cong S^{n-1}$` 是中间维，`$n=2$` 正好是曲面纤维、`$\delta$` 为简单闭曲线，与卡内其他说法自洽；② 定理 1 的 source 改为「p.224 式 (16.6)（几何版本）；同调公式为经典 PL 公式，原书未给证明」，`gap_note` 与 `pitfalls[0]` 相应改写；③ 定理 2 的 source 补 §16d p.225–226（原只挂 §18g）。
存疑：同调版公式本身原书未证，`$\varepsilon$` 的精确符号书中未显式给出，卡内已提示需与 §16d 定向约定对齐。

## 15. lefschetz-fibration-fukaya-category

核了 p.281（§18f：`$\mathrm{char}\,\mathbb K\ne2$`）、p.282（定义 18.12 `$F(\pi)=\tilde{\mathcal A}^{\mathrm{inv}}$`、命题 18.13 的同调全忠实嵌入 `$F(E)\to F(\pi)$` 与 `$L^\#\subset E^{\mathrm{shrink}}\mapsto\tilde L^\#$`、证明用定理 2.9 与 (18.20)、命题 18.14 例外收集）、p.286（命题 18.23）、p.287（(18.29)、定理 18.24 "Tw `$F^\to(V^\#_\beta)$` is quasi-equivalent to Tw `$F(\pi)$`"）、p.288（推论 18.25 嵌入、`$\mathrm{char}\,\mathbb K\ne2$` 的唯一代价）；实读 `new-290.png`。
改动：`sources` 的 §18j 由 `[287,288]` 改为 `[286,288]`（§18j 起于 p.286），anchor 改「原书 p.286–288 §18j」。
存疑：无。

## 16. a-m-singularity

核了 p.304（§20a：`$\Psi=p(x_0)+x_1^2+\cdots+x_n^2$`、`$X^n_m=\Psi^{-1}(w)$`、典范丛平凡、(20.1)）、p.305（(20.2) 箭图、路径代数次数 = n × 下降步数、三条关系、`$A^n_m\cong H(F^n_m)$`、`$\tau=\tau_{V_1}\cdots\tau_{V_m}$` 是单值、`$\tau^{2m+2}(L^\#)\simeq S^{(4-2n)(m+1)-4}L^\#$`、位移非零、Prop 19.7 论证 split-generate、(20.3)）、p.306（(20.4) `$\mu^2(e,e)=e,\ \mu^2(e,f)=(-1)^{n-1}f,\ \mu^2(f,e)=f$`、(20.5) m+1 份、(20.6) `$C_j=\mathrm{Cone}(e_{j,j-1})$`）、p.307（命题 18.21、length grading、`$e$` 长 0 / `$f$` 长 2、(20.7)、命题 1.12 消 `$\mu^1$` 且保双分次、"Inspection shows ... `$\mu^d_A, d>2$` trivial"、§20c 的 `$\mathrm{char}\,\mathbb K=0$`）；实读 `new-314.png`。外部打开 arXiv `math/0010032`（Seidel, *More about vanishing cycles and mutation*）。
结论：逐条一致，未发现错误，未改内容（仅加 `verified_at`）。
存疑：卡内「注 A12-08 – A12-11」是译者注编号，不是原书编号，保留但不应被当作原书出处引用。

---

## 外部依据核查汇总（全部 HTTP 200，实际打开）

| URL | 用于 | 结论 |
| --- | --- | --- |
| https://ncatlab.org/nlab/show/operad | operad | 一致（γ 与 O-代数定义） |
| https://ncatlab.org/nlab/show/A-infinity-algebra | operad、kadeishvili-theorem | 一致（A∞-操作子的代数、极小模型定理） |
| https://ncatlab.org/nlab/show/homological+perturbation+theory | homological-perturbation-lemma | 一致（经典形变收缩与 `$\Phi^\tau$` 级数） |
| https://ncatlab.org/nlab/show/Yoneda+embedding | yoneda-embedding | 一致（仅作背景，A∞ 版以原书为准） |
| https://ncatlab.org/nlab/show/Maslov+index | maslov-class | 一致（万有 Maslov 指数与拉回） |
| https://ncatlab.org/nlab/show/spectral+flow | spectral-flow | 一致（谱流 = 谱的正负穿越计数） |
| https://ncatlab.org/nlab/show/pin+group | pin-structure | 一致（Pin 为 O(n) 双覆盖、含反射） |
| https://ncatlab.org/nlab/show/twisted+spin+structure | pin-structure | 一致（`$\alpha$`-twisted spin 结构的 `$w_2$` 障碍） |
| https://ncatlab.org/nlab/show/Serre+functor | serre-functor | 一致（`$\hom(A,B)\cong\hom(B,S(A))^*$`、Bondal–Kapranov） |
| https://ncatlab.org/nlab/show/Dehn+twist | dehn-twist | 一致（环带上的扭转定义、Lickorish） |
| https://ncatlab.org/nlab/show/Picard-Lefschetz+theory | picard-lefschetz-formula | 一致（单值公式的定位，且列出本书） |
| https://arxiv.org/abs/math/0001043 | dehn-twist（provenance） | 存在：Seidel–Thomas, *Braid group actions on derived categories of coherent sheaves* |
| https://arxiv.org/abs/math/0010032 | a-m-singularity（provenance） | 存在：Seidel, *More about vanishing cycles and mutation* |
| https://arxiv.org/abs/math/0007115 | dehn-twist（provenance） | 存在：Seidel, *Vanishing cycles and mutation* |

未发现打不开或与卡内说法冲突的链接，故未删除任何外部依据。

## 仍需留意

1. `operad` 的 `$K_n$` 记号、`yoneda-embedding` 的「自由模」措辞、`a-m-singularity` 的注 A12-xx 编号，都属译者层表述而非原书用语，未改，但不应被当作原书原文引用。
2. `picard-lefschetz-formula` 与 `dehn-twist` 的同调版公式在原书中没有证明（§16c 只给几何版并明说不证），卡内已把 source 与 `gap_note` 改成「原书未给」而不是假托页码。
3. 「谱流 = Maslov 指标」只能经 Robbin–Salamon 转引，原书 §11b 未给证明。
