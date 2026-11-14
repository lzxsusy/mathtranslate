# EN49 施工总纲（BRIEF）—— Jeffs《超曲面的同调镜像对称：函子视角》中文译注

> 本文件是本工程**唯一**的施工总纲。开工前先读本文件、`README.md`、
> `<本地路径>`（下称《纪律》）、
> `<本地路径>`（下称《总纲》）§1.4 / §1.5 / §5.3 / §7.1 / §7.2。
> 四份文件冲突时，优先级：《纪律》＞本 BRIEF ＞《总纲》＞ README。

---

## §0 任务与交付

**任务**：把底本全文译成中文译注本，公式、编号、定理环境、图表、参考文献一律保留；
数学内容不得删改、不得补写、不得“顺带修正”原作者的错误（只能加【译者注】指出）。

**交付物**（七件套，全部放在 `deliverable\`）：
1. `EN49_Jeffs_超曲面HMS函子视角_中文译注本.pdf` —— 整书成品
2. `README.md` —— 底本信息、页映射、块表与进度、编译方式
3. `译注汇总.md` —— 全部【译者注】按块汇总（含所在页）
4. `阅读参考指南.md` —— 阅读路线、前置知识、章节依赖图
5. `工程总结.md` —— 工作量、难点、术语决策、遗留问题
6. `术语对照表.tsv` —— 冻结术语表（en / zh / 说明 / 状态）
7. `源码_LaTeX.zip` —— `src\` 全部源码（不含编译中间物）

**完成判据**（全部满足才算完成）：
- 14 个块全部译完，`reports\cNN.md` 14 份齐全；
- `python check.py` 输出 `VERDICT: PASS`；
- 整书 `build.ps1` 三遍编译 `errors=0 overfull=0 undefined=0 missing_char=0`；
- 七件套齐；`04_编号登记表.csv` 中 EN49 行状态改「已交付」并写入成品页数。

---

## §1 底本与页映射

- 底本：Maxim Jeffs, *A Functorial Perspective on Homological Mirror Symmetry for Hypersurfaces*,
  PhD dissertation, Harvard University, 2023（导师 Denis Auroux）。
- 原书 156 页 PDF（本地 `work\source\EN49_原文_Jeffs2023_156p.pdf`，794,892 B）；
  原书正文 145 页，前置页罗马数字 i–ix。
- **页映射：原书页 = PDF 页 − 11**；PDF 第 12 页 = 原书第 1 页。
  前置页对应：PDF 1 引用页 / 2 空白 / 3 标题页 / 4 版权 / 5–6 摘要 iii–iv /
  7–9 目录 v–vii / 10–11 致谢 viii–ix。
- 页图：`work\pages\p001.png … p156.png`（130dpi）。看 PDF 第 N 页的图 = `p<NNN>.png`，
  **编号就是 PDF 页号，不是原书页码**；换算：PDF 页 = 原书页 + 11。
- 文字层：`work\en\EN49_en_full.txt`（每页起首 `===== BOOK PAGE n (PDF m) =====`），
  以及按块切好的 `ch00_front_en.txt`、`ch01_en.txt` … `ch13_en.txt`。

**章节结构表**（原书页）：

| 位置 | 内容 | 原书页 |
|---|---|---|
| 前置 | 标题/版权/摘要/目录/致谢 | i–ix |
| Ch1 | Introduction 引言（1.1 概述；1.2 奇异超曲面；1.3 Knörrer 周期性〔1.3.1 证明概要〕；1.4 大复结构极限；1.5 环簇镜像对称〔1.5.1 函子式镜像对称〕；1.6 结果〔1.6.1 证明技巧〕；1.7 与已发表工作的关系） | 1–28 |
| Ch2 | Definitions and Conventions 定义与约定（2.1 正合 LG 模型；2.2 局部 Fukaya–Seidel 范畴；2.3 Cap 与 Cup 函子） | 29–47 |
| Ch3 | Complements of Fibers 纤维的补集（无小节） | 48–57 |
| Ch4 | Knörrer Periodicity for Hypersurfaces 超曲面的 Knörrer 周期性（4.1 AAK 等价；4.2 主定理的证明） | 58–75 |
| Ch5 | Applications to Mirror Symmetry 镜像对称的应用（5.1 裤子塔；5.2 对曲线的应用；5.3 推广） | 76–86 |
| Ch6 | Gradings 分次（6.1 矩阵分解范畴；6.2 双分次） | 87–97 |
| Ch7 | Gluing Diagrams 粘合图表（7.1 扇形粘合；7.2 镜像对称） | 98–111 |
| Ch8 | The Restriction Functor 限制函子（8.1 Knörrer 周期性；8.2 镜像对称；8.3 整分次增强） | 112–127 |
| Ch9 | The Lifting Functor 提升函子（9.1 一个例子） | 128–134 |
| 附录 A | Notation 记号 | 136–137 |
| 文献 | Bibliography | 138–145 |

---

## §2 目录与写作用域（防冲突）

```
EN49_Jeffs_超曲面HMS函子视角_中文译注\
├─ BRIEF.md                ← Lead 独占，译者只读
├─ README.md               ← 每人只改自己那一行的进度
├─ build.ps1 / check.py    ← Lead 独占
├─ src\
│  ├─ main.tex             ← Lead 独占（\input 清单、扉页、译本说明）
│  ├─ preamble.tex         ← Lead 独占（导言区、定理环境、记号宏）
│  ├─ chunks\cNN.tex       ← 译者写自己分配的块，其它块不动
│  ├─ figures\             ← 自己裁的图放这里，命名 fig_X_Y.png
│  └─ tools\               ← compile_chunk.py / zoom.py，只读
├─ work\                   ← 页图、文字层、临时；译者可写 work\zoom\
├─ reports\cNN.md          ← 每块报告
├─ review\                 ← 校对报告
└─ deliverable\            ← 七件套（Lead 最后生成）
```

**硬规则**：`preamble.tex`、`main.tex`、`BRIEF.md`、`build.ps1`、`check.py`、`chunks\` 里不属于
自己的块、`glossary` 的冻结项，**一律不改**。需要新宏、新环境、术语改名，写进 `reports\`
并报 Lead，由 Lead 统一改。

---

## §3 块划分与实施阶段

| 块 | 原书页 | 内容 | Phase |
|---|---|---|---|
| c00 | i–ix | 摘要、致谢 | P1 样板 |
| c01 | 1–11 | Ch1 §1.1–1.3（含 1.3.1） | P1 样板 |
| c02 | 12–21 | Ch1 §1.4–1.5（含 1.5.1） | P2 |
| c03 | 22–28 | Ch1 §1.6–1.7（含 1.6.1） | P2 |
| c04 | 29–47 | Ch2 §2.1–2.3 | P3 |
| c05 | 48–57 | Ch3 | P3 |
| c06 | 58–64 | Ch4 §4.1 | P3 |
| c07 | 65–75 | Ch4 §4.2 | P4 |
| c08 | 76–86 | Ch5 §5.1–5.3 | P4 |
| c09 | 87–97 | Ch6 §6.1–6.2 | P4 |
| c10 | 98–111 | Ch7 §7.1–7.2 | P5 |
| c11 | 112–127 | Ch8 §8.1–8.3 | P5 |
| c12 | 128–134 | Ch9 §9.1 | P5 |
| c13 | 135–145 | 附录 A + 参考文献 | P5 |

**Phase 1（样板）**：c00 + c01 由 Lead 亲自译完、编译、定体例；术语表冻结 v1 后，才允许
并行译其它块。**并行期术语只增不改**。
**Phase 2–5**：按表顺序推进，同一轮最多 3 块并行（《总纲》§5.3：同时“在译”≤4 项）。
**Phase 6**：整书编译 → `check.py` → 双校（对原文语义 / 对页图公式）→ 七件套 → 登记表。

**每块交付**：`chunks\cNN.tex`（能单独编译通过）+ `reports\cNN.md` + README 该行进度。

---

## §4 每块六步工作流

1. 读 `work\en\<chNN>_en.txt` 里本块那一段：只用来**定位句子和结构**，不要直接照抄词序。
2. 看页图：`work\pages\p{PDF页:03d}.png`（PDF 页 = 原书页 + 11），确认版面：
   交换图、脚注、公式编号、跨页定理。
3. 公式看不清就放大：`python src\tools\zoom.py <PDF页> 300 [x0 y0 x1 y1]`，
   PDF 坐标以 A4 点为单位（595×842，左上角为原点）。输出在 `work\zoom\`。
4. 写 `chunks\cNN.tex`：标题层级已在骨架里给好，**不要改标题文字**（要改先报 Lead）；
   正文每页起首加 `% ===== 原书 p.N =====` 注释行。
5. 单块自检：`python src\tools\compile_chunk.py cNN`，必须
   `errors=0 overfull=0 undefined=0 missing_char=0`。
6. 写 `reports\cNN.md`（模板见 §9），并在 `README.md` 进度表把本块改成「已完成」。

---

## §5 文本层的坑（Jeffs 这份底本特有）

- **行内公式被拍平**：`f_!`、`f^*`、上标下标常错位或丢失，`\mathcal{O}` 变成 `O`，
  `\mathbb{C}` 变成 `C`；一律以页图为准。
- **`≅`、`∘`、`⊗`、`⊂`、`⟶`** 在文字层常成问号或粘连，交换图箭头全部要在页图上核。
- **`Kn¨orrer`**：文字层把 ö 拆成 ¨+o；源文件里写作 `Kn{\"o}rrer`，不要写成 Knorrer。
- **编号**：原书公式 (1.1)、(1.2)…按章；定理类跨环境共用一个「章.节.序号」计数
  （如 注 1.2.1 之后可能是 定义 1.2.2、断言 1.2.4），因此 `preamble.tex` 用共享计数器
  `result`。**绝对不要手写编号**，用 `\begin{定理环境}\label{...}` + `\ref{...}`。
- **交叉引用**：`Section 1.3`、`Theorem 4.1`、`§` 一律用 `\ref`；参考文献用 `[AAK16]` 形式
  **原样保留**（原书是硬编码字面引用，不做 \cite），文献表条目不译。
- **脚注**：原书脚注排在页脚，译文用 `\footnote{}` 就地放，不要另设脚注章。
- **图**：原书 10 张图，从页图裁到 `src\figures\fig_X_Y.png`（X=章，Y=序号），
  `\includegraphics[width=0.7\textwidth]`，图注译为中文、编号自动。
- **交换图**：优先 `tikz-cd` 重画；极大或有弧线/装饰的图（第 7 章的扇形图）可裁页图。
- **跨页定理**：定理跨页时仍是一个环境，不要拆开；输出后核对页图里定理的完整边界。

---

## §6 LaTeX 规范

- 章标题用 `\section{}`（preamble 已让 `\thesection` 显示为「第 N 章」）；
  节 `\subsection{}`；三级 `\subsubsection{}`。**不写编号**，也不要在标题里加序号。
- 行内公式 `$...$`；展示公式 `\[ ... \]` 或 `equation`/`align` 环境（需要编号才用）。
- 定理类环境（都**不显示“章.节.序号”以外的手工数字**）：
  `definition` 定义、`theorem` 定理、`lemma` 引理、`proposition` 命题、`corollary` 推论、
  `claim` 断言、`example` 例、`remark` 注、`conjecture` 猜想、`problem` 问题。
- 每个环境后接 `\label{}`，引用写 `\ref{}` / `\eqref{}`。
- 译者注：`\transnote{一句话说明}`，独立成段；每块 8–15 条，三类：易错预警、含糊点拨、
  背景直觉。不写“我认为作者错了”这类主观判断，只陈述事实与理由。
- 不手动加汉字与公式之间的空格（ctex 已处理）；汉字用全角标点。
- 不引入新宏包。需要新命令先在 `reports\` 申请。

---

## §7 术语与记号

- 术语表：`work\glossary.tsv`（256 行，EN48 的 241 条冻结术语 + Jeffs 专有 15 条）。
  **表内已冻结的照抄，不得改写**；表外的新术语首次出现写「中文（English）」，并在
  `reports\cNN.md` 里列出来，由 Lead 决定是否入表。
- 人名保留英文：Auroux、Knörrer、Orlov、Seidel、Fukaya、Gammage、Kontsevich、AAK（Auroux–Abouzaid–Katzarkov）、
  Strominger–Yau–Zaslow。
- 禁止音译（Koszul / Morita / Novikov / Calabi–Yau 是《纪律》允许的例外）。
- 记号表见附录 A（原书 p.136–137），译文用 `preamble.tex` 里的宏：
  `\mathcal{}` 花体系（`\cA`…`\cZ`）、`\fA`…`\fZ` 哥特体、`\Vdual`（V^∨）。

**Jeffs 专有术语（v0，待冻结）**：

| English | 中文 | 说明 |
|---|---|---|
| matrix factorization | 矩阵分解范畴 | 第 6 章核心 |
| Knörrer periodicity | Knörrer 周期性 | 人名保留 |
| Liouville sector | Liouville 扇形 | sector 统一「扇形」 |
| sectorial gluing | 扇形粘合 | 待定 |
| gluing diagram | 粘合图表 | 待定 |
| partially wrapped Fukaya category | 部分缠绕深谷范畴 | 与 wrapped 区分 |
| very affine hypersurface | 极仿射超曲面 | 待定 |
| large complex structure limit | 大复结构极限 | |
| tower of pants | 裤子塔（tower of pants） | 专名，首次括注 |
| cap / cup functor | cap 函子 / cup 函子 | 保留英文 |
| derived scheme | 导出概型 | |
| local Fukaya–Seidel category | 局部 Fukaya–Seidel 范畴 | |
| stopped Fukaya category | 带停点的深谷范畴 | stop 不译 |

---

## §8 中文文风硬指标（`check.py` 会 grep，必须全 0）

- 禁用句式：「被……所」「进行……的讨论/计算/研究」「对于……而言」「关于……的讨论」
  「使得……得以」「起到了……的作用」「有着……的意义」「众所周知」「不难发现」
  「值得注意的是」。
- 一句一个逻辑重心，单句 ≤60–70 汉字（列举句 ≤90）。
- 不用「其/该/之」堆叠；指代明确。
- 英文术语、数字与汉字之间留半角空格；中文标点全角；行内公式的句末标点在公式之后。
- 不写“本文作者”“笔者认为”，译者只说该说的（【译者注】里用“译者按”或直接陈述）。

---

## §9 reports\cNN.md 模板

```markdown
# cNN 报告（原书 p.X–Y，PDF p.M–N）

## 完成情况
- 译完页数 / 公式数 / 定理环境数 / 图数
- 单块编译：errors=0 overfull=0 undefined=0 missing_char=0

## 术语与体例
- 新术语（en → zh，首次出现页）
- 与 glossary 冲突或需要改名的地方

## 疑点请示（不臆造，列出来给 Lead）
1. 原书 p.X 第 n 行：文字层为“……”，页图为“……”，疑为笔误/两种读法。
2. …

## 自检
- [ ] 每页有 `% ===== 原书 p.N =====`
- [ ] 无手写编号；`\ref` 全部解析（单块编译 undefined=0）
- [ ] `\transnote` 条数：n
```

---

## §10 关键提醒

1. **数学正确性最高**。读不懂、公式对不上、图看不清：写进报告，用最保守的译法，别猜。
2. **不臆造**。原文省略的证明步骤不补；原文写错的，译文照译并在【译者注】里说明。
3. 只改分配给自己的文件；改动别人文件 = 事故。
4. 每块结束必须单块编译通过；不要攒到最后一起调。
5. 页图是唯一的公式真相来源；文字层只用来定位句子。

---

## §11 初始冻结译名（节选，完整表见 `work\glossary.tsv`）

同调镜像对称（homological mirror symmetry）、深谷范畴（Fukaya category）、
导出范畴（derived category）、缠绕深谷范畴（wrapped Fukaya category）、
部分缠绕深谷范畴、弗洛尔上同调（Floer cohomology）、朗道–金兹堡模型（Landau–Ginzburg model）、
正合（exact）、环簇（toric variety）、丰富（ample）、极丰富（very ample）、
例外收集体（exceptional collection）、布里奇兰德稳定性（Bridgeland stability）、
微局部层（microlocal sheaf）、热带几何（tropical geometry）、轨形（orbifold）、
点层（skyscraper sheaf）、自同态（endomorphism）、带曲率（curved）、滤过（filtered）、
Euler 型（Euler form）、顶针（Lefschetz thimble / thimble）、
斯托明格–丘–扎斯洛夫纤维化（SYZ fibration）、矩阵分解范畴、Knörrer 周期性。

---

## §12 七件套交付清单（Phase 6）

- [ ] 整书 `build.ps1` 三遍：`errors=0 overfull=0 undefined=0 missing_char=0`
- [ ] `python check.py` → `VERDICT: PASS`
- [ ] `deliverable\` 七个文件齐（PDF、README、译注汇总、阅读参考指南、工程总结、术语表、源码 zip）
- [ ] `README.md` 写入成品页数与最终术语表版本
- [ ] `04_编号登记表.csv` 的 EN49 行：状态「已交付」、页数、日期
- [ ] 全书 `\transnote` 汇总进 `译注汇总.md`（按块、带原书页）
