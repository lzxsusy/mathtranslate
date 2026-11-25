# 丁组卡片交付报告（ch4 + ch6 + ch9）

- 交付张数：**24 张**（概念 20 + 例子 4），与任务书清单逐条对齐，id / type / track 未改。
  - ch4（track `4`）：7 张 = 概念 6 + 例子 1
  - ch6（track `6`）：10 张 = 概念 8 + 例子 2
  - ch9（track `9`）：7 张 = 概念 6 + 例子 1
- 落盘位置：`_cards_grassmann/cards/concepts/*.json`（20）与 `_cards_grassmann/cards/examples/*.json`（4）。
- 校验：`python tools/validate_cards.py` 全库 **90 张（概念 73 + 例子 17），0 error / 0 warn**，我的 24 张全在其中。
- 页码口径：`pages_zh` = 中文 PDF 页索引（页脚 = `pages_zh` − 6），`pages_en` = 英文 PDF 页索引（页脚 = `pages_en` − 9），不用书末印刷页码。章内关系：ch4 `zh = en − 6`，ch6 `zh = en − 10`，ch9 按 `ch09-批注.md` 逐条实测值（en 与 zh 的差在 18–20 之间漂移，不能线性换算）。anchor 全部回读 `Grassmannians-精读/source/chapters/chNN.tex`，确认是非空行且为定义 / 命题 / 定理 / 例的起始行。

## 一、每卡一句话

### ch4（7，Kiem《丛的奇异模空间中的相交配对》）

| # | id | 一句话 |
|---|---|---|
| 1 | `concept/balanced-action` | Kiem 的平衡判据：辛商上每点的稳定子单位分支都要在其辛切片上线性平衡；满足时相交上同调恰是等变上同调的一个截面 $V_M$，配对才能用杯积算。 |
| 2 | `concept/extended-moduli-space` | 把基本群表示的唯一关系 $\prod_j[a_j,b_j]=1$ 抬到李代数，得到带矩映射的光滑扩张模空间 $M^{\mathrm{ext}}$，其辛商就是奇异的 $M(n,d)$。 |
| 3 | `concept/intersection-pairing-via-vm` | 定理 5.5：互补次数的两个 $V_M$ 类之积 = 最高次类乘配对值，于是 $\tau\langle\sigma_1,\sigma_2\rangle$ 化归为等变上同调的杯积。 |
| 4 | `concept/kirwan-map-and-class-d` | Kirwan 映射把等变类送到商的上同调；正根之积类 $D$ 的像是 $K/T$ 的 Poincaré 对偶，故 $K$ 上积分等于 $\frac1{n!}$ 乘 $T$ 上积分（式 (9)）。 |
| 5 | `concept/partial-desingularization` | 按稳定子维数逆向归纳地沿最高维稳定子层爆破，得到轨形 $\widetilde M(n,d)$，使普通上同调仍带 Kirwan 映射、并能看见相交上同调；文中 A/B 两段说明确实写反（译注 1）。 |
| 6 | `concept/residue-formula-for-pairings` | 式 (10)：两个正则值处的配对之差 = 夹在中间的不动点分量上的留数之和，留数周期性地把求和压成 $1/(1-e^X)$。 |
| 7 | `example/wall-crossing-term-m20` | 沿 $\Delta=(S^1)^{2g}$ 爆破 $M(2,0)$，法丛三个直和项给权 $2,-2,-4$ 与 Euler 类，两次留数塌缩成一个系数：$W=-2^{-3g}\,\mathrm{Coeff}_{t^{g-1}}\big[(1-t/2)^{-g-1}(1-t/4)^{-g}\big]$，$g=2$ 给 $-1/32$。 |

### ch6（10，de Jong 等《曲线上层的模空间的算术方面》）

| # | id | 一句话 |
|---|---|---|
| 8 | `concept/isotrivial-family` | 等平凡族 = 所有忠实平坦拉回下都变成积的族；一个簇的形式就是它的等平凡族，因此形式由 $\mathrm{Aut}$ 的扭子（上同调类）分类。 |
| 9 | `example/isotrivial-torelli` | 定理 1.9：几何纤维上平凡的 $\mu_r$-gerbe，其叠的 $\mu_r$-线性同构与模叠的 $\mu_r$-线性同构一致；证明靠 $H^2$ 的截面分裂与引理 1.7 杀类。 |
| 10 | `concept/parabolic-bundle` | 在 $P^1$ 上给每个抛物点配权在 $\{0,\tfrac12\}$ 的子丛过滤，抛物次数 $\mathrm{pardeg}$ 把底层次数与各点秩跳按权加权，且等于根叠上对应层的次数。 |
| 11 | `concept/faddeev-index` | 把 Brauer 类沿 $\mathrm{Br}(K)$-平移后取最小指标：$\mathrm{ind}_F(\alpha)=\min_{\beta}\mathrm{ind}(\alpha+\beta_L)$；指标为 2 恰好等价于某个秩 2 扭曲模空间有有理点（命题 5.2.2）。 |
| 12 | `concept/gerbe-banded-by-mu-n` | 惯性叠同构于 $\mu_n$ 的 gerbe 给 $H^2(-,\mu_n)$ 中一个类，其到 $H^2(-,\mathbf G_m)$ 的像即 Brauer 类；其上的层按特征标劈成 $n$ 块，度数按 $1/n$ 计、稳定按 $\mu$ 判。 |
| 13 | `concept/twisted-sheaf` | 惯性 $\mu_n$ 的作用等于标量的 $\mathcal O$-模 = gerbe 叠上 étale 拓扑斯的 $\mathcal O$-模，于是 Illusie 形变理论照搬，Brauer 类由此变成可算的模空间。 |
| 14 | `concept/period-and-index` | $\mathrm{ind}$ = 凝聚扭曲层的最小非零秩，$\mathrm{per}$ = 一般点类在 $H^2(\eta,\mathbf G_m)$ 中的阶；$\mathrm{per}\mid\mathrm{ind}$、$\mathrm{ind}\mid\mathrm{per}^h$；猜想 2.3 成立时曲线上 $\mathrm{per}=\mathrm{ind}$（定理 3.4）。 |
| 15 | `concept/ramification-sequence` | 完备 DVR 上 $0\to\mathrm{Br}(R)'\to\mathrm{Br}(K)'\to H^1(\kappa,\mathbf Q/\mathbf Z)$；末端群可显式算，循环代数的分歧由 $(-1)^{v(a)v(b)}a^{v(b)}/b^{v(a)}$ 的 $n$ 次根给出。 |
| 16 | `concept/root-stack` | 沿 snc 除子取 $n$ 次根：$\mathscr R_n=[\operatorname{Spec}R[t^{1/n}]/\mu_n]$，在除子外是同构、在除子上留 $B\mu_n$ 剩余 gerbe，从而任何分歧类都能延拓上来（「铺平」）。 |
| 17 | `example/bicyclic-algebra-faddeev-4` | $A=(17,t)\otimes(13,(t-1)(t-11))$ 的 Faddeev 指标为 4，却在每个 $\mathbf Q_\nu$ 上指标为 2；真正的障碍是 $\mathbf Q_{17}$ 上方 $\mu_2\times\mu_2$ 惯性把秩 2 正则层杀掉。 |

### ch9（7，Teixidor i Bigas 等《可约曲线上的向量丛及应用》）

| # | id | 一句话 |
|---|---|---|
| 18 | `concept/slope-stable-torsion-free-sheaf` | 可约结点曲线上深度 1 无挠层配极化 $w$ 与 $w$-秩 $\sum w_ir_i$ 的 $\chi$-稳定性；$\chi(G)/\mathrm{rk}\,G=\mu(F)+(1-g)$ 说明它就是斜率稳定的替身（分支秩可不同）。 |
| 19 | `concept/reducible-nodal-curve-and-dual-graph` | 分支记顶点、结点记边得对偶图 $\Gamma$：$g=\sum g_i+b_1(\Gamma)$，紧型判据、多度等价 $d_i\mapsto d_i+ra_i$ 与秩 $r$ 模空间的分支数 $r^{M-1}$ 都由它读出。 |
| 20 | `concept/hilbert-compactification` | 把稳定丛变成曲线在 $\mathrm{Gr}(H^0(E),r)$ 中的嵌入点，取 Hilbert 概形的分支闭包再作 GIT 商；曲线不再固定，恰是退化所需，可约曲线上 Hilbert 稳定只是必要条件。 |
| 21 | `concept/limit-linear-series-higher-rank` | 每分支一个 $E_i$ 与 $k$ 维 $V_i$、结点处粘合、一个整数 $a$：条件 (a) $(\sum d_i)-r(M-1)a=d$、(b) 消没阶互补、(c) 截面由结点值决定。 |
| 22 | `concept/maximal-subbundle-and-langes-conjecture` | $s_{r'}(E)=r'd-r\max\deg E'$；稳定时 $s_{r'}\ge0$。Lange 猜想断言达界时一般丛就有秩 $r'$ 子丛，余维 $r'(r-r')(g-1)-(r'd-rd')$。 |
| 23 | `concept/brill-noether-locus-on-reducible-curves` | 可约/高秩情形的 BN 簇：$B^k_{r,d}=\{E:h^0\ge k\}$，预期维数 $\rho=r^2(g-1)+1-k(k-d+r(g-1))$，$B^{k+1}\subset\operatorname{Sing}$；用椭圆链作特殊纤维把维数夹到恰 $\rho$。$\beta$ 与经典 BN 数的定义见乙组 `concept/brill-noether-number`。 |
| 24 | `example/limit-linear-series-on-a-chain-of-five-elliptic-curves` | 五条椭圆曲线首尾粘成 $g=5$ 的链，$r=2,d=9,k=4$：$\sum d_i=9+8\cdot4=41\Rightarrow a=4$、$\rho=5$，逐分支丛与截面消没阶显式给出。 |

## 二、证明状态统计与 sketch 清单

24 张共 **42 条** theorems：**complete 16 / sketch 12 / reference 14**。原则：章内有可逐步复述的证明才写 complete（steps 每步带 `text` + `why`）；原文只给「类似地」「留给读者」「引某引理」的写 sketch 并在 `gap_note` 点明缺哪一步；只作文献定位的写 reference。

| 卡 | 定理 | 为什么只能 sketch / 缺什么 |
|---|---|---|
| `parabolic-bundle` | 命题 4.3 | 原文把「两方向互为逆」与「$\deg_{\mathscr P}V=\mathrm{pardeg}(V_*)$」都留给读者（§4–§5 是未定型的工作，批注 18），逆构造未写出。 |
| `faddeev-index` | 命题 5.2.2 | 反向最硬：局部模型只写「通过剩余域上的简单几何计算即推出」，缺 $\rho^{\oplus2}$ 在 $\mu_2$-特征分解下无秩 1 直和项的核对，以及各局部模型到整体扭曲层的粘合。 |
| `twisted-sheaf` | 命题 A.2.3 | 只给思路并引 [19] 的粘合引理；缺「等化子与 $\mu_n$-等变结构相容」与 $\mathrm{Ext}^1$-扭子无自然基点时粘 Azumaya 代数的细节。 |
| `ramification-sequence` | 推论 C.2 | Azumaya 代数与 $M_m(B)$ 的粘合推给 A.2.3 与 [22]；有限多个 $q$ 上取同一 $m$ 的一致性也未说明。 |
| `root-stack` | 命题 5.1.3 | 证明归给「分裂分歧」的计算与 A.2.3；且正文右端 $M^*_{\mathscr P/k}(n,L)$ 按证明首句应补 $\otimes\bar k$（译注 8 只对一半，批注 16）。 |
| `root-stack` | 命题 4.3 | 同 `parabolic-bundle`：范畴等价与次数保持被留作练习。 |
| `bicyclic-algebra-faddeev-4` | 推论 5.2.5 | 原文直接由引理 5.2.4 得结论；缺「任意 Faddeev 等价类可写成 $\alpha'+(u,t)$、$u\in\mathbf Z_{17}^{\times}$」的核对（命题 C.1(1)），本卡在正文里补了这一步。 |
| `hilbert-compactification` | 可约曲线上的必要条件 | 原文只说「类似于命题 2.1 证明中 $(∗)$ 的条件得以满足」「类似地……」，完整证明在 [G2a]/[Sc2]（批注 6）。 |
| `limit-linear-series-higher-rank` | 由一维族构造极限线性系 | 扭转符号与次数记账只说「于是容易验证 (a)」；按 $\mathscr O(-C'_i)\vert_{C_i}=\mathscr O(-P_i)$ 实算得 $-b$，与正文「乘 $\mathscr O(bP_i)$」相反，且逐结点累加给 $2(M-1)a$ 而 (a) 写 $r(M-1)a$（批注 9）。 |
| `maximal-subbundle-and-langes-conjecture` | 定理 5.1 | 只给要点与 $r=2,r'=1,d=1$ 的椭圆链勾勒；一般秩一般曲线分别归 [T7] 与 [RT]。 |
| `brill-noether-locus-on-reducible-curves` | 定理 6.1 | 只对 $g=5,k=4,d=9$ 做了一页勾勒，三组条件的一般推导与 $r>2$ 归 [T1]、[T9]。 |
| `limit-linear-series-on-a-chain-of-five-elliptic-curves` | 该点是 $\rho$ 维一般点 | 「不会延拓到这一形变上」未证；且维数等式实算 6 而非 $\rho=5$（笔记反例 1），这一步在本章内没有闭合。 |

reference（14 条，均为本章只引用、未证明）：ch4 七张卡的 Kiem / Kirwan / Guillemin–Kalkman / Martin 诸定理（定理 5.4、5.5、5.6、式 (9)(10) 的出处）；ch6 的定理 A.2.1（Illusie 形变理论）、命题 B.5（Galois 上同调练习，指 [20, Lemma 2.1.1.3]）、定理 3.2（de Jong，原文只勾勒）、命题 5.2.6（猜想 2.3 ⟹ per=ind，指 [20]/[15]）；ch9 的光滑曲线 Hilbert 稳定 ⟺ 斜率稳定（[GM]/[T4]/[T5]/[Sc1]）与分支数 $r^{M-1}$（[T2]/[T3]）。

## 三、id 与 related 冲突

- **id 无冲突**：24 个 id 全部按任务书，未新增清单外卡片，未改 type / track / 文件名。
- **主动分工（避免与兄弟组重复）**：
  - ch9 BN 卡只写**可约曲线 / 高秩**的 $B^k_{r,d}$、$\rho$ 与夹逼，不重抄 $\beta$ 与经典 BN 数；`related` 必链乙组 `grassmann/concept/brill-noether-number`。
  - ch6 `isotrivial-family`（簇 / 扭子的定义）与 `isotrivial-torelli`（Torelli 型定理的证明路线）分工，互链。
  - `root-stack`（构造与「铺平」性质）与 `ramification-sequence`（正合列与分歧公式）共享附录 C，但一个写几何对象、一个写代数正合列，无重叠。
- **跨组 related**：24 张每张 ≥1 条跨组链接（`isotrivial-torelli` 的 related 末尾补了 `grassmann/concept/coherent-system`）。validator 只认已落盘 id，写作过程中「无法解析」的临时告警在 24 张齐后全部消失。
- 未发现与他组重复的 id；`related` 全部取 `cards-ids.md` 中真实存在的 id。

## 四、存疑（5 条）

1. **页码**：ch9 的 en 与 zh 之差在 18–20 之间漂移（按 `ch09-批注.md` 逐条给值），ch4 / ch6 用 `zh = en − 6` / `zh = en − 10` 的线性关系。只有 5 张（isotrivial-family、parabolic-bundle、balanced-action、intersection-pairing-via-vm、brill-noether-locus）按 pymupdf 实测改过页码，其余按章内关系核算，未逐页 OCR；个别跨页条目（如命题 4.3 的「中译 105–106」）以断言句所在页为准。
2. **算例维数等式**：`ch09.tex:265` 的维数记账实算为 $6$，英文原式把被减项写成 $1+2+4+4+4+2$（算得 2），两边都不等于 $\rho=5$；$a=4$、$\rho=5$ 本身正确（批注 13、笔记反例 1）。卡片按「6」写并在 pitfall 里注明原文印错。
3. **极限线性系的扭转符号**：$\mathscr E_{j(i)}(-bC'_i)$ 限制到 $C_i$ 实算次数变化为 $-b$，与正文「乘以 $\mathscr O(bP_i)$」方向相反；逐结点累加给 $2(M-1)a$ 而条件 (a) 写 $r(M-1)a$。故这张只写 sketch，并建议 $M=2$ 时逐项核对（批注 9）。
4. **定理 6.1 的读法**：条件 (1) 中「$d_2\ge k_2\ne0$」应读作「$d_2\ge k_2$ 且 $k_2\ne0$」；「Hilbert 稳定 ⟹ $(∗)$ 型次数条件」与有理分支分裂型 $O^{\oplus j}\oplus O(1)^{\oplus r-j}$ 原文只说「类似地」，无证明（批注 6）。
5. **附录 C.3 只能 reference**：延拓定理原文证明略，仅作背景；命题 C.1 证明中的 $t^{1/u}$ 是原书误印（应为 $t^{1/n}$，译注 12），引用时已按 $t^{1/n}$ 写。
