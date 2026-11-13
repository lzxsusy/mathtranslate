# 前置页与书末独立复核（audit_backmatter）

状态：**已完成**（只读复核；未改动任何 tex 文件）。
范围：`src/frontmatter/`（titlepage、contact、preface、note）、`src/chunks/ch99_back.tex`、`src/appendix/terms.tex`、`src/main.pdf` 的目录。
方法：原文 `work/en/ch00_front.txt`、`work/en/ch99_back.txt`、`术语对照表.tsv` 逐一比对；页标回 `work/pages/p{原书页+1:03d}.png` 实测；`main.pdf` 用 pymupdf 抽 TOC 与页面文字实测；术语附录用脚本逐条比对 tsv。脚本留在 `work/review/`（audit_toc.py、audit_terms*.py、audit_bib*.py、audit_figs.py）。

---

## 一、前置页四件

### 1.1 `preface.tex` 与原书 p.8–9 逐段对读

结论：**6 段正文 + 署名全部译出，无漏段、无改写作者立场、无数字/年份/人名错误**。逐段对应如下（原文段落 → 译文行号）：

| 原文段落（p.8–9） | 译文位置 | 结论 |
|---|---|---|
| 讲义来源（两门课、清华、两部分目标） | `preface.tex:9` | 一致 |
| Part I / 第 1–2 章 | `preface.tex:11` | 一致 |
| Part II / 第 3–4 章 | `preface.tex:14` | 一致（有措辞问题，见下） |
| Part III / 第 5–6 章 | `preface.tex:16` | 一致（有措辞问题，见下） |
| 材料大体标准、§2.8.5 与 §6.4.3 例外、参考文献 | `preface.tex:18` | 一致 |
| 致谢（Notes Taker Program、杨鹏） | `preface.tex:20` | 一致 |
| 静斋 / December 2025 | `preface.tex:24–25` | 一致 |

三个问题（均为轻微，建议改）：

1. **术语前后不一致**：`preface.tex:14` 作「相位空间上以函数表示的经典可观测量」，`preface.tex:16` 作「量子力学的相空间表述」。同一概念两种译法，且 `术语对照表.tsv` 定为「相空间」。建议 :14 改为「相空间」。（证据：原书两处均作 phase space。）
2. **翻译腔两处**：`preface.tex:14`「这一理论对于诠释测量结果、对系统状态分类、分析动力学性质都是必要的」——「对于……都是必要的」；`preface.tex:16`「量子可观测量被当作其经典对应物的形式形变来处理」——「被当作……来处理」。建议改为「诠释测量结果、给系统状态分类、分析动力学性质，都离不开这一理论」与「把量子可观测量视为其经典对应物的形式形变」。
3. **译注句与自述略有张力**：`preface.tex:29` 末尾加了「［译注：以上前言据底本第 8–9 页译出，只作语言转换，未增删内容……］」。这句本身是译注本新增的文字，说「未增删内容」严格讲指正文；可保留，但若求严谨可写「译文未增删正文内容」。

### 1.2 `note.tex` 凡例七条与全书实际做法

结论：第 1、2、3、5 条成立；**第 4、6、7 条与实际做法不符**（第 6 条是当前状态问题，等 `notes_to_body` 跑完可消）。

| 凡例 | 行号 | 结论 | 证据 |
|---|---|---|---|
| ① 页码：`% [原文 p.N]`，底本 PDF 页 = N+1 | `note.tex:18` | **✓ 实测 5 处全对** | 见下表 |
| ② 陈述编号照抄底本 | `note.tex:19` | **✓ 抽 5 条全对** | `ch01a.tex:77` 例 1.1.2、`ch01a.tex:175` 定义 1.1.5、定义 6.3.3（原书 p.315）、定理 6.2.10（Fedosov，原书 p.313）、命题 4.7.8（`ch04c.tex:378`，原书 p.245） |
| ③ 公式不编号，保留作者手标 (*) | `note.tex:20` | ✓（措辞不全） | 全书 0 个 `equation` 环境、0 个 `\label`/`\ref`；`\tag` 共 11 处：(*) 8、(\*\*) 2、(†) 1。凡例只提 (*)，建议改为「(*)、(\*\*) 等」 |
| ④ 图：原位置、裁切、无题注无编号 | `note.tex:21` | **部分不符** | 无 `\caption` ✓；5 张抽查均紧跟所在段落 ✓；但**并非全部裁切**：109 张裁切 PNG 之外另有 29 个 `tikzpicture`，其中 ch01a 双缝三图、ch06b p330/331 交换图为按原图重绘（体例后经 Lead 允许），凡例未提 |
| ⑤ 「本节重点」框，可 `\showtakeawayfalse` 关 | `note.tex:22` | ✓ | `preamble.tex:103` `\newif\ifshowtakeaway`、`:120` `\takeaway` 条件包裹 |
| ⑥ 批注：灰底小框 `\tutornote{...}`，排在被注段之后 | `note.tex:23` | **不符（当前状态）** | 全书 15 处批注实际写成 `% [Tutor Note: ...]` 注释，**`\tutornote` 用量 0**；`preamble.tex:181` 的灰框样式已就绪但未被调用，故当前 `main.pdf` 里批注完全不显示。等 `notes_to_body` 把注释转成 `\tutornote` 后才与凡例一致 |
| ⑦ 术语首现以全角括号附原文 | `note.tex:24` | **大体不符** | 正文全角括注拉丁文仅 27 处，多为人名典故（Hugh Everett、David Mermin、Rieffel、EBK、HKR…）；普通术语首现不加英文（如「泊松括号」首现无 (Poisson bracket)）。要么全书补括注，要么把凡例改成「人名与少数术语首现括注」 |

第 1 条实测 5 处（均回页图核对页脚页码）：

| 源文件:行号 | 页标 | 该页内容 | 结论 |
|---|---|---|---|
| `preface.tex:8` | 原文 p.8 | 前言起（PDF 9，原书页 8） | ✓ |
| `ch01b.tex:105` | 原文 p.32 | 高斯波包 Ψ 链，页图 `p033.png` 页脚 32 | ✓ |
| `ch02c.tex:148` | 原文 p.140 | 威克定理 (*) 式，页图 `p141.png` 页脚 140 | ✓ |
| `ch06b.tex:1136` | 原文 p.331 | ρ_D^λ∘(D+b) 链，页图 `p332.png` 页脚 331 | ✓ |
| `ch05b.tex:247` | 原文 p.276 | Bergman 完备性估计，页图 `p277.png` 页脚 276 | ✓ |

批注 15 处位置（供 `notes_to_body` 用）：`ch01b.tex:781`、`ch02c.tex:321,595,877,1345`、`ch03a.tex:381`、`ch04a.tex:224,1770`、`ch04b.tex:270,633,747`、`ch04c.tex:416`、`ch05b.tex:271,552`、`ch06a.tex:488`。

关于「共 338 页」（`note.tex:11`）：✓ 底本 PDF 1–338，末页印刷页码 337。

### 1.3 `titlepage.tex`

| 项 | 底本（PDF p.1） | 译文 | 结论 |
|---|---|---|---|
| 书名 | Quantum Mechanics and Geometry | 量子力学与几何 + 英文 | ✓ |
| 作者 | 李思(Si Li) | Si Li（李思） | 次序对调（轻微，建议改回「李思（Si Li）」） |
| 单位 | Tsinghua University | 清华大学 丘成桐数学科学中心 | 增加了中心名（原封面无），信息真实但属增补 |
| 版本 | (preliminary draft updated December 2025) | preliminary draft, December 2025 | 基本一致，略去了 updated |
| 主页 URL | https://sili-math.github.io/ | 同 | ✓ |

渲染检查：`main.pdf` 第 1 页正常（`work/preview/fm_p1.png`），无页码、无溢出。

### 1.4 `contact.tex`

| 项 | 底本（PDF p.2） | 译文 | 结论 |
|---|---|---|---|
| email | [邮箱隐去] | 同（`contact.tex:11`） | ✓ |
| 主页 | https://sili-math.github.io/ | 同（`:12`） | ✓ |
| 首句 | Thank you for supporting this note! | 「感谢您对这份讲义的关注！」 | 语义偏移：supporting = 支持，不是「关注」。建议「感谢您支持这份讲义！」 |
| 页标记 | p.1 | `contact.tex:2` `% [原文 p.1]` | ✓（PDF 2） |

渲染检查：`main.pdf` 第 2 页正常（垂直居中、无页码）。

---

## 二、`ch99_back.tex`（参考文献）

### 2.1 重大：54 条 vs 底本 63 条，漏 9 条

`src/chunks/ch99_back.tex` 共 54 个 `\bibitem`（[1]–[54]，末尾为 `Susskind2014`），而 `work/en/ch99_back.txt` 明列 **[1]–[63]**。缺：

| 编号 | 条目（底本原文） |
|---|---|
| [55] | Takhtadzhian, Leon Armenovich. Quantum mechanics for mathematicians. Vol. 95. AMS, 2008. |
| [56] | Teschl, Gerald. Mathematical methods in quantum mechanics. Vol. 157. AMS, 2014. |
| [57] | Tsygan, Boris. Cyclic homology. Cyclic homology in non-commutative geometry. Vol. 121, 73–113. Springer, 2003. |
| [58] | Von Neumann, John. Mathematical foundations of quantum mechanics: New edition. Vol. 53. Princeton University Press, 2018. |
| [59] | Weinberg, Steven. Lectures on quantum mechanics. Cambridge University Press, 2015. |
| [60] | Witten, Edward. Analytic continuation of Chern-Simons theory. AMS/IP Stud. Adv. Math 50 (2011): 347. |
| [61] | Woodhouse, Nicholas Michael John. Geometric quantization. Oxford university press, 1992. |
| [62] | Zinn-Justin, Jean. Path integrals in quantum mechanics. OUP Oxford, 2004. |
| [63] | Zworski, Maciej. Semiclassical analysis. Vol. 138. AMS, 2012. |

**后果：正文引用悬空**（编号照底本、条目不存在）：
- `ch02a.tex:1140`「我们沿用文献 [60] 的讲法」（莫尔斯理论/最速下降，原文 `ch02a.txt` 亦作 [60]）；
- `ch06b.tex:579`「我们遵循 [57]」（微分分次代数，原文 `ch06b.txt` 亦作 [57]）。

建议：补 [55]–[63] 九条（照底本格式），接在 `[54] Susskind2014` 之后即可；页标无需改动——现有 `% [原文 p.334/p.335/p.336/p.337]` 四个页标与底本分页一致（[46]–[63] 均在原书 p.337）。

### 2.2 已有 54 条：逐条比对结论

- 程序比对（年份、词数、编号）**0 条异常**；逐条人工比对亦无作者名、年份、卷期页错误。
- 三处正字已落实：`[13] Sj\"ostrand`（原提取作 Sjostrand，底本实为 Sjöstrand）、`[16] Yakubovskii`（底本提取乱码 I￿A￿kubovskiĭ）、`[27] Griffiths`（底本提取为 ligature Griﬀiths）。
- 书名斜体：除 `[26] Ginzburg`（arXiv 预印本，无 `\emph`，可接受）外，其余条目书名/期刊名均有 `\emph`，未见斜体丢失。
- 细枝：`[1]` 底本用弯引号 Arnol’d，译文用直引号 Arnol'd（可统一）；`[47]` 底本有衍文「Functional analysis. . Gulf」，译文已删多余句点（属清理，非漏译）；`[3]` 底本作 Fronsdal 而 `ch06a.tex:9` 正文写 Frønsdal（前后不一致，建议统一为底本拼法或加注）；期刊名大小写译文统一为首字母大写（底本多为小写，属体例选择，可接受）。

---

## 三、`appendix/terms.tex`（英汉术语对照）

### 3.1 结构与计数

- 头部注释「共 9 组 / 591 条」（`terms.tex:3`）：**与实际一致**。
- 各组条数（`terms.tex` 行号 / tsv 行数）：

| 组 | 行号 | 附录条数 | tsv 行数 |
|---|---|---|---|
| 一、量子力学基本概念 | 14 | 102 | 102 |
| 二、希尔伯特空间与算子 | 126 | 63 | 63 |
| 三、路径积分 | 199 | 45 | 45 |
| 四、伪微分算子、象征与量子化 | 254 | 29 | 29 |
| 五、几何量子化 | 293 | 38 | 38 |
| 六、形变量子化 | 341 | 25 | 25 |
| 七、数学通用词 | 376 | **112** | **114** |
| 八、人名 | 498 | 46 | 46 |
| 九、各章译名增补（终审合并） | 554 | 131 | 131 |

### 3.2 两处缺条（原因：生成脚本按英文原词全局去重）

`tools/make_terms_appendix.py` 用 `seen` 集合按英文原词去重，同词第二个义项被静默丢弃。丢的正是两条：

| 丢失条目 | tsv 行 | 中文 | 已被谁「占位」 |
|---|---|---|---|
| `section` | 组七第 102 行 | 节（章节义） | 组七第 6 行 `section` → 截面（丛截面义） |
| `index` | 组七第 108 行 | 索引 | 组二 `index` → 指标（算子指标义） |

后果：① 附录里 `section` 只列「截面」，而正文 `\section` 一律译「节」，读者查「节」对不上；② 「索引」义没有条目（正文基本不用 index=索引，影响小）。
建议：脚本改为按「英文+中文」成对去重（或在 tsv 里把两个义项写成 `section (of a bundle)` / `section (of a chapter)`），再重跑生成。**这是全表唯一的缺条，不是串行。**

### 3.3 其余检查

- **无串行、无缺列、无乱码、无截断**：591 条与 tsv（组一至组九共 593 行）逐条程序比对，英文全等，中文除 `section` 一条外全等。
- 抽 20 条回查（序号:英文→中文）：0 quantum mechanics→量子力学、29 observation→观测、58 scattering state→散射态、87 Lie algebra→李代数、116 orthogonal projection→正交投影、145 one-parameter unitary group→单参数酉群、174 measure→测度、203 ladder operator→阶梯算子、232 Wigner transform→维格纳变换、261 integrality condition→整性条件、290 character→特征标、319 critical point→临界点、348 up to→相差、377 closed form→闭形式、406 appendix→附录、435 Fock→福克、464 closure (of an operator)→闭包、493 deep well limit→深阱极限、522 Weyl criterion→外尔判别法、551 Banach algebra→巴拿赫代数。**20 条全部与 tsv 一致。**
- 特殊行正常：`Dirac delta function` 的 `$\delta$` 在 PDF 中渲染为 δ（非字面 `$\delta$`）；处理列为「保留」的 5 行（WKB 近似、Moyal 乘积、Moyal、Levi-Civita 符号、Alice / Bob）均按原样列出。
- PDF 渲染（`main.pdf` 第 370–378 页）：9 组标题齐全（「九 各章译名增补（终审合并）」在排版中为「九 各章…」，文字抽取时空格丢失，无碍）；末条 EPR 正常收尾；双栏无溢出。

---

## 四、目录（`src/main.pdf`）

结论：**目录无缺项、无错页**。

- `main.pdf` 共 378 页；TOC 共 193 条：一级 5（前言、译注说明、三个 `\part`）、章 6、节 41、小节 139、书末 2。
- 与源文件对得上：`src/chunks/*.tex` 恰有 6 个 `\chapter`、41 个 `\section`、139 个 `\subsection`，标题与顺序**逐个相同**（章节标题只在 TOC 加了「第 1 章」前缀，属正常）。
- 页码实测：54 个 level ≤ 3 的条目，逐条到所标 PDF 页取文字，**全部能在该页找到标题，0 条失配**；印刷页码 = PDF 页 − 12（PDF 13 页脚为 1），TOC 显示的是印刷页码 ✓。
- 书末两项在目录中：参考文献 p.366（`\addcontentsline` 于 `ch99_back.tex:9`）、附录：英汉术语对照 p.370（`terms.tex:6`）✓。

---

## 五、建议清单（按优先级）

1. **补 `ch99_back.tex` 缺的 [55]–[63] 九条**（否则 [57]、[60] 两处正文引用悬空）。
2. **跑 `notes_to_body`**，把 15 处 `% [Tutor Note: ...]` 转成 `\tutornote{...}`；否则 `note.tex:23` 关于批注的说明在成品里不成立。
3. **改凡例措辞**：第 4 条补「少数示意图按原图重绘」；第 3 条补 `(\*\*)`、`(†)`；第 7 条按实际改为「人名与少数术语首现括注」；第 6 条在批注入库后再确认。
4. **术语附录**：修生成脚本的去重键（`section`、`index` 两条），或改 tsv 消除同词多义。
5. 小修：`preface.tex:14` 相位空间→相空间；`contact.tex:10` 关注→支持；`titlepage.tex:13` 作者次序按底本；`ch99_back.tex` 的 [1] 引号、[3] Fronsdal/Frønsdal 统一。
