# 术语审计报告（U-audit）

> 审计对象：`tex/chapters/` 下**译文正文**（中文）中保留未译的英文专业词/短语。
> 快照时间：2026-10-28 16:19（此时 `ch06.tex`、`ch09-1.tex` 刚补入，`glossary.tex`/`preface.tex` 有更新）。
> 若其后各章再有改动，请以同一脚本重扫（见文末「方法」）。

---

## 0. 范围与方法

**纳入扫描（18 个文件）**：ch01-1, ch01-2, ch02, ch03-1, ch03-2, ch04, ch05-1, ch05-2, ch06, ch07, ch08, ch09-1, ch09-2, ch10-1, ch10-2, ch10-3, ch10-4, appendix。

**有意排除**：
- `bibliography.tex`：按项目规则文献题名不译，原样转写；
- `glossary.tex`：术语表本身即中英对照，属设计如此；
- `translator-note.tex`：译注说明，按设计保留大量英文；
- 源码中的 `%` 注释行（Tutor Note 属批注，不是译文）；
- 人名/模型名（Langlands、Drinfeld、Verma、Wakimoto、Hecke、Kac–Moody、Springer、Miura、Beilinson、Gaitsgory…）与文献引用 `[Frenkel and Ben-Zvi 2004]` 之类；
- LaTeX 命令、宏、环境名、`\label`/`\ref` 名、数学公式内的一切（`\operatorname{Conn}`、`\mathrm{nilp}`、`\begin{conjecture}` 等被清洗掉的“假英文”）。

**做法**：逐文件去除数学、环境、标签、引文、注释与宏后提取连续 ASCII 词串，按词频与上下文人工判定；再对每个候选词统计其在**译文正文**中的出现处数与行号示例，并对照 `GLOSSARY.md`（含最新 §7 补充裁定）核对收录情况。

---

## 1. 表 A：译文正文中保留未译的英文专业词（建议逐条处理）

| 英文词 / 短语 | 出现文件（处数；行号示例） | 建议处理 | 依据 |
|---|---|---|---|
| **Conjecture N**（指本书自己的猜想编号） | ch10-1（约 6 处：L50、L59、L160、L162、L260）；ch10-3（20 处：L26、L193、L217、L306、L327、L341、L353、L359、L416、L430、L457、L466、L495、L524、L575、L587、L632 等） | 译**「猜想 N」** | 同章正文其余处已用「猜想」（全书 106 处；ch10-3·L327 同句已经写作「Conjecture 10.4.4……该猜想」，属自相矛盾）；本译本环境名亦为「猜想」 |
| **Lemma N**（指本书自己的引理编号） | ch10-3（1 处：L153「Lemma 10.4.1 给出判据……Lemma 10.4.2 说明……」） | 译**「引理 10.4.1 / 引理 10.4.2」** | 环境名为「引理」；同句上下文其他引用均为中文 |
| **torsor / torsors** | ch04（8）、ch10-2（5）、ch08（4）、ch05-1（3）、ch05-2（3）、ch10-3（3）、ch06（2）、ch09-1（2）、ch03-2（1） | **保留 `torsor`**，首现括注「主齐性空间」，登记术语表 | GLOSSARY 未收；中文通行译名「主齐性空间」，但全书 31 处已惯用英文，统一改中文成本高且无必要（详见 §2 不一致第 7 条） |
| **Grothendieck alteration** | ch07（2：L72、L120）；ch10-3（5：L201、L244、L341） | **保留英文**，首现括注「Grothendieck 变更」 | Lead 于 U10 已裁定保留英文；GLOSSARY 未收，建议补录 |
| **DG**（DG 概形、DG 纤维、DG 化、DG 结构） | ch10-3（约 50 处 / 19 行：L14、L200、L201、L341、L343、L534…）；ch10-4（约 24 处 / 17 行：L12、L26、L35…）；全书「微分分次」**0 处** | **保留 `DG`**，首现括注「微分分次（differential graded）」 | 数学界通行写法「DG 概形」；但首次出现必须给中文，否则非专家读者无法解码 |
| **proper** | ch09-1（L482「由于旗簇是 proper 的」）；ch10-1（L236「涉及的态射不是 proper 的」） | 译**「真（proper）态射」**（「旗簇是真簇」） | 中文代数几何通行译名「真态射 / 真映射」；`proper morphism` 不宜保留英文 |
| **holonomic** | ch01-2（4 句：L346、L350、L352、L355） | 译**「完整（holonomic）D-模」** | 通行译名「完整 D-模」（holonomic system=完整系统）；GLOSSARY 未收 |
| **monodromic** | ch10-4（L263「$I_y$-monodromic 模范畴」；L308「无论是否 monodromic」） | 译**「单值（monodromic）」** | GLOSSARY 已收 monodromy=单值性，同词根宜统一；全书其余处（ch01-2、ch09-1、ch10-3 等）均用「单值」 |
| **parahoric** | ch01-2（1：L260「"parahoric"代数群 $P_i$」） | **保留 `parahoric`**，首现括注（建议「拟抛物子群」），提交 Lead 裁定 | 中文无统一通行译名（「拟抛物/准抛物」均有使用）；按项目规则「无通行译名则保留英文」 |
| **minuscule** | ch09-2（5 处：L896、L1108、L1112、L1114、L1116，均作「minuscule 权」） | 译**「极小（minuscule）权」** | `minuscule weight` 通行译名「极小权」；GLOSSARY 未收 |
| **Pfaffian** | ch04（1：L575） | 译**「Pfaff 行列式（Pfaffian）」** | 人名术语；中文常作 Pfaff 行列式，首现括注英文 |
| **Wronskian** | ch04（2：L73、L77） | 译**「朗斯基行列式（Wronskian）」** | 通行译名；glossary 未收 |
| **fonctions-faisceaux** | ch01-2（2：L243、L315「Grothendieck 的 fonctions-faisceaux 词典」） | **保留法文**，首现括注「函数-层词典」 | Grothendieck 本人的法文术语，无英译定名；保留原文最忠实 |
| **chiral algebra / factorization algebra** | ch02（各 1，L413：中文术语后括注「（chiral algebra, factorization algebra）」） | 补出中文：**「手性代数（chiral algebra）」「分解代数（factorization algebra）」** | `chiral` 在 ch05-2 已译「手性微分算子」；`factorization algebra` 中文通行「分解代数/因子化代数」 |
| **chiral differential operators** | ch05-2（1：L153，已译「手性微分算子（chiral differential operators）」） | 已处理，仅需登记术语表 | — |
| **blackboard 体** | ch09-2（2：L335、L582「书用 blackboard 体」） | 译**「黑板体（blackboard bold）」** | 字体名（$\mathbb{M}$ 这类字形），中文称黑板体 |
| **Cartesian 图表** | ch09-1（2：L603、L728「使下图成为 Cartesian 图表」） | 译**「笛卡尔（Cartesian）图表」**或直接用「拉回图表 / 纤维积图表」 | 通用数学术语，宜中文化 |
| **delta 函数** | ch02（6 处：L397、L438–440、L454、L471）；ch05-2（2：L20、L38） | 统一作**「δ-函数（delta 函数）」** | 数学记号应作 δ；「delta」是拉丁转写，不宜与中文混排 |
| **check（ˇ 记号）** | ch09-1（1：L21「带"check"的量（对偶侧）」） | 改「带 **ˇ（check）** 记号的量」 | `check` 在此指符号 ˇ（caron），宜用符号+英文名 |
| **BRST** | ch08（1：L908） | **保留缩写**（首现可注「BRST 上同调」） | 国际通用缩写，无需翻译 |
| **ind- / pro-**（前缀） | ch01-2（8）、ch03-2（4）、ch05-1（2）、ch10-1（3）、ch10-2（5） | **保留**（ind-概形、pro-幂幺群、pro-代数群），登记术语表 | 中文文献通行「ind-概形」「pro-幂幺」混写，硬译反而生造 |
| **Coind** | ch05-1（2）、ch05-2（7）、ch07（1） | **保留**（已有中文「余诱导」，Coind 作算子记号），登记 | `Coind` 是函子符号；正文「余诱导」已用中文 |

### 表 A′：外部文献的定位引用（**保留英文，不需改**）

| 英文定位 | 文件·行 | 说明 |
|---|---|---|
| `Theorem 4.4.1` | ch02·L1082 | 指向 [Frenkel and Ben-Zvi 2004] 的编号，保留英文便于查原文 |
| `Lemma 3.4.5` | ch03-1·L336 | 同上 |
| `Proposition 4.2.2` | ch03-1·L557 | 同上 |
| `Prop. 3.8.9` | ch09-1·L93（环境可选参数内） | 指向 [Drinfel'd and Sokolov 1985] |
| `Prop. 12.8` | ch09-2·L174（环境可选参数内） | 指向 [Frenkel 2005b] |
| `Prop. 1.8.1` | ch09-2·L1112（行内） | 指向 [Ginzburg 1995] |
| `Lemma 6.4` | ch10-3·L266（环境可选参数内） | 指向 [Frenkel and Gaitsgory 2006c] |

> 建议：这类定位可统一加「原文」二字（如「原文 Theorem 4.4.1」），但**不应**译成中文编号，否则读者无法在英文文献中定位。

---

## 2. 不一致术语（同一英文词在不同章/同章内译法不同）

> 下列均为**同一英文词**的不同中文/中英混合处理，需 Lead 裁定后统一。

| # | 英文词 | 现状（按译文正文统计） | 裁定建议 |
|---|---|---|---|
| 1 | **residue** | ch09-1 用**「残数」54 处**；其余 ch01-2、ch02、ch03-2、ch06、ch07、ch08、ch09-2、ch10-3、ch10-4 用**「留数」54 处** | 统一**「留数」**（GLOSSARY §5 明定 residue=留数）。ch09-1 全书 54 处需批量替换（含 keypoints、定理陈述） |
| 2 | **completed enveloping algebra** | **「完备包络代数」14 处**（ch01-2 1、ch02 2、ch03-1 5、ch03-2 2、ch08 2、ch09-2 2）vs **「完备泛包络代数」21 处**（8 文件） | 统一**「完备泛包络代数」**（GLOSSARY §1）。改 14 处 |
| 3 | **Weyl group** | **「Weyl 群」10 处**（ch05-1 2、ch08 3、ch09-2 5）vs **「外尔群」8 处**（ch04、ch05-2、ch07、ch09-1、ch10-3 ×3、ch10-4） | 统一**「外尔群」**（GLOSSARY §1）。改 10 处 |
| 4 | **screening operator** | **「筛选算子」3 处**（ch09-2：L580、L765 及 keypoints）vs **「屏蔽算子」58 处**（ch05-1、ch05-2、ch07 40、ch08 14） | 统一**「屏蔽算子」**（GLOSSARY §1）。改 3 处 |
| 5 | **twist / twisted** | 四种写法：**「扭变」15**（ch06 5、ch10-3 10）、**「扭曲」12**（ch10-2 6、ch10-4 6）、**「扭转」4**（ch05-2 2、ch09-1 2）、**「扭（twist）」3**（ch03-2、ch04、ch08 各 1） | 建议统一**「扭转」**（动词/名词）＋「扭转的」（形容词）。共约 25 处待改；ch03-2/04/08 的「扭（twist）」首现括注可保留 |
| 6 | **Conjecture N** | 英文 26 处（ch10-1 6、ch10-3 20）vs 中文「猜想」106 处 | 统一**「猜想 N」**，改 26 处（见 §1 表 A） |
| 7 | **torsor** | **`torsor` 31 处**（9 文件）vs **「主齐性空间」8 处**（ch03-2 7、ch09-2 1） | 建议统一保留 **`torsor`**（首现括注）；把 ch03-2、ch09-2 的「主齐性空间」改回 `torsor`。若 Lead 偏好全中文，则需改 31 处，成本更高 |
| 8 | **semi-infinite parabolic induction** | **「半无限抛物诱导」16 处**（ch06 6、ch07 7、ch08 1、ch09-2 2）vs **「半无限诱导」2 处**（ch06） | 统一**「半无限抛物诱导」**（GLOSSARY §1 全称）。改 2 处 |
| 9 | **Hecke eigensheaf vs Hecke eigenmodule** | 「Hecke 本征层」ch10-1 4、ch10-4 25；「Hecke 本征模」ch10-2 9、ch10-3 2、ch10-4 1 | 二者是**不同概念**（eigensheaf=本征层；eigenmodule=本征模），不应强行统一；但请核对 ch10-4·L161「可约模……都是 Hecke 本征模」指的是模还是层，若指层应改「本征层」 |
| 10 | **delta 函数** | 全书仅「delta 函数」8 处（ch02、ch05-2） | 统一**「δ-函数」**（符号化），非跨章矛盾但属规范问题 |

### 2′. 人名/排版一致性（非术语译名，但影响全书统一）

| 项 | 现状 | 建议 |
|---|---|---|
| Harish-Chandra 的连字符 | 单连字符 28 处（ch02、ch05-1、ch08、ch09-2、ch10-2、ch10-4）；**双连字符** 29 处（ch10-1 19、ch10-3 10，LaTeX 渲染为 en dash） | 人名本身用连字符，统一写 `Harish-Chandra`（单连字符）；改 ch10-1、ch10-3 共 29 处 |
| Drinfel'd / Drinfeld | `Drinfel'd` 10 处（ch01-1 4、ch04 3、ch08 1、ch09-1 1、ch10-4 1）与 `Drinfeld` 混用 | 正文人名统一 `Drinfeld`；**文献条目**（Bibliography）按原书拼写 `Drinfel'd` 保留 |
| Kac–Moody、Segal–Sugawara、Weil–Deligne 等 | 已统一用双连字符（en dash） | 保持 |

---

## 3. 表 C：术语表缺口（中文已统一，但 GLOSSARY 未收录）

> 这些**不是**未译英文，而是「译名已用、术语表缺失」，建议随本轮一并补入 GLOSSARY（可直接粘贴为 §7 补充裁定续行）。

| English | 现用中文 | 出现处 | 备注 |
|---|---|---|---|
| cocharacter | 余特征标 | ch04 4、ch09-1 2 | 与 coweight=余权配套 |
| unipotent / unipotent radical | 幂幺 / 幂幺根 | 全书多章 | 术语表仅有 nilpotent=幂零 |
| principal gradation | 主分次 | ch04 | |
| principal embedding | 主嵌入 | ch04 | |
| exponent（李代数的） | 指数 | ch04 | `E={d_1,…,d_ℓ}` |
| chiral algebra | 手性代数（chiral algebra） | ch02 | 见 §1 表 A |
| factorization algebra | 分解代数（factorization algebra） | ch02 | 见 §1 表 A |
| holonomic（D-module） | 完整（holonomic）D-模 | ch01-2 | 建议收录 |
| monodromic | 单值（monodromic） | ch10-4 | 与 monodromy=单值性配套 |
| proper（morphism） | 真（proper）态射 | ch09-1、ch10-1 | |
| parahoric | parahoric（保留英文） | ch01-2 | 待裁定 |
| minuscule | 极小（minuscule）权 | ch09-2 | |
| Pfaffian | Pfaff 行列式（Pfaffian） | ch04 | |
| Wronskian | 朗斯基行列式（Wronskian） | ch04 | |
| Schwarzian derivative | Schwarz 导数（Schwarzian derivative） | ch03-2 | 已在正文括注 |
| torsor | torsor（保留英文，首现括注主齐性空间） | 9 文件 | 见 §1 |
| Grothendieck alteration | Grothendieck alteration（保留英文） | ch07、ch10-3 | Lead 已裁定 |
| DG（differential graded） | DG（微分分次） | ch10-3、ch10-4 | |
| Coind | 余诱导（Coind） | ch05-1、ch05-2、ch07 | |
| BRST | BRST | ch08 | |
| ind- / pro-（前缀） | ind-概形 / pro-幂幺 | ch01-2 等 | |

---

## 4. 建议加入 GLOSSARY 的条目（可直接粘贴）

```markdown
| torsor | torsor（保留英文；首现括注“主齐性空间”） | |
| Grothendieck alteration | Grothendieck alteration（保留英文） | |
| DG（differential graded） | DG（微分分次） | 首现括注 |
| proper morphism | 真态射 | |
| holonomic D-module | 完整（holonomic）D-模 | |
| monodromic | 单值（monodromic） | |
| parahoric | parahoric（保留英文；待裁定中文） | |
| minuscule weight | 极小权 | |
| chiral algebra / factorization algebra | 手性代数 / 分解代数 | |
| Pfaffian | Pfaff 行列式（Pfaffian） | |
| Wronskian | 朗斯基行列式（Wronskian） | |
| Schwarzian derivative | Schwarz 导数 | |
| cocharacter | 余特征标 | |
| unipotent | 幂幺 | |
| principal gradation | 主分次 | |
| exponent（of a Lie algebra） | 指数 | |
| Coind | 余诱导（Coind） | |
| BRST | BRST | |
| ind- / pro- | ind-概形 / pro-幂幺 | |
```

---

## 5. 附：扫描与复现方法

1. 清洗：删 `%` 注释行、`\begin{…}…\end{…}`、`\[…\]`、`$…$`、`[...]` 引文、`\command`；
2. 抽取连续 `[A-Za-z'-]+` 词串，按词频排序；
3. 排除人名/模型名/文献定位/环境名/宏名（清单见 §0）；
4. 对候选词统计**非注释行**中的出现处数与行号；
5. 对照 `GLOSSARY.md`（含 §7 补充裁定）判定「已收录 / 未收录 / 译法不一」。

> 本次审计的统计口径均为「译文正文（非注释行）中的出现次数」，与批注中的英文无关。所有行号以快照时刻文件为准。
