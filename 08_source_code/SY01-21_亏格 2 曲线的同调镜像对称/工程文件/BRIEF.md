# EN48 施工总纲（BRIEF）— Cannizzo《亏格 2 曲线的同调镜像对称》中文译注本

> 本文件是本工程的唯一施工说明。开工前按顺序读完：本文件 → 工程根 `README.md`
> → `C:\Users\admin\Desktop\归档\00_归档说明\数学文献翻译纪律.md`（全文）
> → `C:\Users\admin\Desktop\学术翻译总纲\00_总纲.md`（§1.4、§1.5、§5.3、§7.1、§7.2 必读）。
> 三者冲突时，以《数学文献翻译纪律》为准；纪律未覆盖的，按本文件。

---

## §0 任务与交付

把 Catherine Kendall Asaro Cannizzo 的博士论文（145 页，英文）完整译成中文译注本，
按桌面工程体系交付：

- **文献号**：`EN48`（已核对 `04_编号登记表.csv`，EN01–EN47 已占用，EN48 空闲；已登记，状态「在译」）。
- **主题域**：`01_镜像对称与同调镜像对称`。
- **工程目录**：`C:\Users\admin\Desktop\归档\01_镜像对称与同调镜像对称\EN48_Cannizzo_亏格2曲线HMS_中文译注\`
- **成品**：`deliverable\EN48_Cannizzo_亏格2曲线HMS_中文译注本.pdf`，另按 §12 交付七件套。
- **状态机**：待搜集 → 已入库 → 待译 → **在译** → 已交付 → 已校订。每完成一阶段
  先更新登记表状态与路径（表是唯一真相源），再动别的。
- **产能红线**（总纲 §5.3）：本工程占用「在译」名额 1 个，全库同时「在译」不超过 4 项。

**本工程的完成判据**（缺一不可）：
1. `chunks/c00.tex … c11.tex` 全部译完，无 `TODO` 残留；
2. `python check.py` 输出 `VERDICT: PASS`（句式、术语、连字、整书编译 0 error / 0 overfull / 0 undefined / 0 missing char）；
3. 逐块 `reports/cNN.md` 齐全，`review/` 有双校记录（对原文语义 + 对页图公式）；
4. `deliverable\` 七件套齐全，成品 PDF 页数与 README 记录一致；
5. `04_编号登记表.csv` 中 EN48 状态更新为「已交付」，路径指向成品。

---

## §1 底本与页映射

- **底本**：Cannizzo, C. K. A., *Homological mirror symmetry for the genus 2 curve in an
  abelian variety and its generalized Strominger–Yau–Zaslow mirror*, PhD dissertation,
  University of California, Berkeley, Spring 2019. 导师 Denis Auroux；答辩委员会
  Denis Auroux（主席）、David Nadler、Marjorie Shapiro。
- **来源**：eScholarship `https://escholarship.org/uc/item/88g945z7`（开放获取）。
  原作无 arXiv 版本；本工程 PDF 为 eScholarship 官方版本，本地副本
  `work/source/EN48_原文_Cannizzo2019_145p.pdf`（1,569,233 B，145 页，PDF 文字层可抽取）。
- **页映射（铁律）**：**原书页 = PDF 页 − 9**。即 PDF p.10 = 原书 p.1。
  前置页用罗马数字 i–v：PDF p.5=i（献词）、p.6=ii（目录）、p.7–8=iii–iv（图目录）、p.9=v（致谢）。
  原书 p.1 开始正文页码；原书 p.136 是参考文献末页。PDF p.1–4 为 eScholarship 封面/扉页/
  版权页/摘要（摘要页未编页码）。
- **结构表**（已由 PDF 书签与文字层核对）：

| 块 | 原书页 | PDF 页 | 内容 | 小节 |
|---|---|---|---|---|
| c00 | i–v | 1–9 | 摘要、献词、致谢；封面/版权页信息并入扉页 | — |
| c01 | 1–12 | 10–21 | 第 1 章 引言、背景与设定 | 1.1 论文结果与方法的陈述（p.1）；1.2 B 侧流形（p.3） |
| c02 | 13–22 | 22–31 | 第 1 章（续） | 1.3 环簇的背景（p.13） |
| c03 | 23–43 | 32–52 | 第 1 章（续） | 1.4 A 侧流形（p.23）；1.5 辛形式的定义（p.38） |
| c04 | 44–69 | 53–78 | 第 2 章 辛形式 ω 的非退化性 | 2.1（p.44）、2.2（p.47）、2.3（p.49）、2.4（p.68） |
| c05 | 70–81 | 79–90 | 第 3 章 阿贝尔簇 V 与 V∨ 的 HMS | 无小节 |
| c06 | 82–90 | 91–99 | 第 4 章 深谷范畴 | 4.1 Y 的 Fukaya–Seidel 范畴：引言（p.82） |
| c07 | 91–109 | 100–118 | 第 4 章（续） | 4.2 背景（p.91）；4.3 模空间（p.94） |
| c08 | 110–113 | 119–122 | 第 4 章（续） | 4.4 定义与选择的无关性（p.110） |
| c09 | 114–130 | 123–139 | 第 5 章 主定理 | 5.1 HMS 计算（p.114）；5.2 证明（p.130） |
| c10 | 131 | 140 | 第 6 章 记号 | 无小节 |
| c11 | 132–136 | 141–145 | 参考文献 | — |

- 原书共有 21 张图（图 1.1–1.11、2.1–2.2、3.1、4.1–4.5、5.1–5.3），图目录在 PDF p.7–8。
- 原书全部定义/定理/引理/命题/推论/断言/注/例**共用同一编号计数器**，编号形式
  「章.节.该节内序号」（如 注 1.2.1、定义 1.2.2、断言 1.2.4 连续）。公式、图、表按章编号
  （式 (1.1)、图 1.1）。preamble 已按此设定，**不要手工写编号**，一律 `\label`/`\ref`。

---

## §2 目录与写作用域

工程根 `C:\Users\admin\Desktop\归档\01_镜像对称与同调镜像对称\EN48_Cannizzo_亏格2曲线HMS_中文译注\`：

```
BRIEF.md              本文件（施工总纲，先读）
README.md             工程状态：底本信息 / 进度表 / 术语冻结状态 / 变更日志 / 编译命令
build.ps1             整书三遍 xelatex 编译 + 质量统计 + 成品复制到 deliverable/
check.py              交付前审计（句式/连字/手工编号/整书编译指标）
src/
  preamble.tex        导言区（章节样式、共享定理计数器、编号、记号宏、\transnote）
  main.tex            扉页、译本说明、内容提要、目录、\input 12 个块
  chunks/c00..c11.tex 各块译文（标题行已给，正文待译；块内只写正文，不写 \documentclass）
  figures/            从原书页图裁出的插图（fig_1_1.png …）
  tools/compile_chunk.py   单块编译自检：python src/tools/compile_chunk.py c01
  tools/zoom.py            公式/插图局部放大：python src/tools/zoom.py 23 300 x0 y0 x1 y1
work/
  source/EN48_原文_Cannizzo2019_145p.pdf   底本 PDF
  en/EN48_en_full.txt       全文文字层（含 `===== BOOK PAGE N (PDF M) =====` 标记）
  en/chNN_en.txt            分章文字层（同上，按块粗分）
  en/ch00_front_en.txt      前置页文字层
  page_map.csv              PDF 页 ↔ 原书页 ↔ 首行 对照表
  pages/pNNN.png            全部 145 页的 130dpi 整页图（看版式用）
  zoom/                     zoom.py 输出的高清局部图
  tmp_cNN/                  单块编译产物（wrap.pdf 即单块成品）
  main_build/               整书编译产物
deliverable/            成品（PDF + 七件套）
reports/                每块报告 cNN.md
review/                 分章校对记录
```

**写作用域**：本工程只有一个译者会话，你对以上全部文件有写权限，但**只改本工程目录内**
的文件；登记表 `04_编号登记表.csv` 只允许改 EN48 那一行；`归档\00_归档说明\`、
`学术翻译总纲\`、其他 EN 工程一律只读。

---

## §3 块划分与建议顺序

12 块，每块 1–26 页。**顺序即建议施工顺序**，但每块必须一次译完、编译通过、写报告，
不允许半块交付：

| 块 | 页数 | 内容 | 备注 |
|---|---|---|---|
| c00 | 5 | 摘要、献词、致谢 | 短，先做，定文风 |
| c01 | 12 | 1.1–1.2 结果陈述 + B 侧流形 | **样板块**：术语、文风、评注体例在此定稿 |
| c02 | 10 | 1.3 环簇背景 | 术语密集（环簇/扇/矩多面体） |
| c03 | 21 | 1.4–1.5 A 侧流形 + 辛形式定义 | 公式与图多（图 1.2–1.11） |
| c04 | 26 | 第 2 章 非退化性 | 计算密集，逐页核对公式 |
| c05 | 12 | 第 3 章 HMS | 范畴论表述 |
| c06 | 9 | 4.1 Fukaya–Seidel 范畴引言 | 概念密集 |
| c07 | 19 | 4.2–4.3 背景 + 模空间 | 最长的一块，注意节奏 |
| c08 | 4 | 4.4 定义与无关性 | 短 |
| c09 | 17 | 第 5 章 主定理 | 核心结果 |
| c10 | 1 | 第 6 章 记号表 | 术语表定稿的依据，放最后译 |
| c11 | 5 | 参考文献 | 条目不译，只做格式 |

**Phase 规划（每次会话至少完成 1–2 块）**：
- Phase 1：c00 + c01（样板）+ 术语表冻结 + README 进度表更新；
- Phase 2：c02 + c03（第 1 章收尾）；
- Phase 3：c04 + c05；
- Phase 4：c06 + c07 + c08（第 4 章）；
- Phase 5：c09 + c10 + c11；
- Phase 6：双校（review/）、整书编译、七件套、登记表「已交付」、工程总结。

**断点续传**：每次新会话先读 `README.md` 的进度表，找到第一个 `未完成/进行中` 的块继续；
不要重译已完成块（除非审计要求返工，返工须在报告里写原因）。

---

## §4 每块工作流（六步，缺一不可）

1. **读原文文字层**：`work/en/chNN_en.txt`（或 `EN48_en_full.txt` 中对应 `===== BOOK PAGE N =====` 区段）。
   文字层只用来**定位句子与公式**，不可直接照抄进译文（见 §5）。
2. **看整页版式**：用 read_image 打开 `work/pages/pNNN.png`（PDF 页号 = 原书页 + 9），
   确认段落划分、脚注位置、公式编号、图的位置与图注。
3. **放大核对公式/图**：公式、上下标、花体、交换图、插图，一律
   `python src/tools/zoom.py <PDF页> 300 <x0> <y0> <x1> <y1>`（PDF 点坐标；1pt=1/72in，
   整页宽约 595、高 842；由 130dpi 页图换算：PDF点 = 像素 × 72 / 130），再 read_image 看高清图。
   文字层里的公式**一律不可信**（上下标被拍平、花体丢成普通字母、≠ 拆成两个字符）。
4. **写译文**：只写 `src/chunks/cNN.tex`。块首的 `% ===== 原书 p.N =====` 注释行保留，
   每页起首补一条；标题行（`\section`/`\subsection`）已给定，不要改编号，标题译文若需
   调整只改花括号内文字并同步 README 附录的标题表。
5. **单块编译自检**：`python src/tools/compile_chunk.py cNN`，要求
   `errors=0 overfull=0 undefined=0 missing_char=0`；有 overfull 就调公式换行/文字；
   有 missing char 说明用了 ctex 不支持的字符，换字或加 `\text{}`。
6. **写报告并更新状态**：`reports/cNN.md`（模板见 §9）；在 `README.md` 进度表把该块改为
   「已完成」并记日期；若本块新增/改动了术语，同步 `work/glossary.tsv` 并在报告里列出。

**每块开始前**先读 `work/glossary.tsv`（冻结术语）与 `src/tools/compile_chunk.py` 里的
块号→页码表，确认本块边界。

---

## §5 文本层的坑（pymupdf 抽取的英文层）

- **连字**：`ﬁ ﬀ ﬂ ﬃ ﬄ` 会出现在词中（ﬁbration、deﬁnition、diﬀeomorphism）。译文不受影响，
  但**检索原文关键词**时要把连字还原（`ﬁ`→`fi`）。
- **数学被拍平**：上下标、花体、`V^∨`、`H^0`、`D^b Coh`、`A_∞` 在文字层里是一串失去结构的字符
  （如 `V ∨`、`DbCoh(V )`、`A∞`）；`≠` 可能拆成 `̸=`；交换图整块散架。**一律回页图**。
- **独立公式**：文字层会把公式行按视觉顺序打散，编号 (1.1) 与公式分离。以页图为准，
  编号用 `equation` 环境的自动编号（preamble 已设 `\numberwithin{equation}{section}`）。
- **脚注**：文字层把脚注排在页末，容易误当正文；页图里脚注在页脚、有分隔线。
- **页眉页脚**：每页开头的孤立数字（页码）与章节名是页眉页脚，不是正文，删掉。
- **定理开头跨页**：`Theorem 1.1.1 ([Can]).` 之类可能被页标记截断，注意接上。
- **引用标记**：作者用 `[AAK16]`、`[Sei08]`、`[Fuk02]` 等方括号引用；译文保留原样，
  不改成 `\cite`。
- **图注**：图注以 `Figure 1.1: ...` 开头，文字层可能把图注与下一段混排；以页图为准。
- **原文笔误**：保留原样并在该处加 `% [Tutor Note: 说明]` 源码注释或在报告里记一条，
  不要擅自"修正"。

---

## §6 LaTeX 规范（preamble 已就绪，块内只用这些）

- **章节**：`\section{章标题}`（自动显示「第 N 章」）、`\subsection{...}`（自动 1.1）。
  **不要**在标题里写编号。
- **定理类环境**（全部共用计数器，自动编号，与原文一致）：
  `definition`(定义) `theorem`(定理) `proposition`(命题) `lemma`(引理) `corollary`(推论)
  `claim`(断言) `example`(例) `remark`(注) `conjecture`(猜想) `problem`(问题)。
  写法：
  ```latex
  \begin{definition}\label{def:B-side-manifold}
  设 ...
  \end{definition}
  由\ref{def:B-side-manifold}可知 ...
  ```
  原文的 `(Explanation of the diagram)` 之类括注放在环境可选参数里：
  `\begin{remark}[图示解释]\label{rem:...}`（`\newtheorem` 的 optional 标题会以括号显示）。
- **公式**：独立公式用 `equation` 环境（要编号）或 `\[ ... \]`（不编号），`align`/`align*` 处理多行。
  行内公式 `$...$`。**禁止** `\tag`、**禁止**手工编号；公式末标点按中文习惯放在公式后。
- **图**：从页图裁出存 `src/figures/fig_<章>_<序号>.png`（如 `fig_1_1.png`），用
  ```latex
  \begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/fig_1_1.png}
    \caption{...}\label{fig:1-1}
  \end{figure}
  ```
  图注译成中文；图内的英文标签（坐标轴、顶点标号）保留原样，不重绘。
- **交换图**：优先用 `tikz-cd` 重画（原书交换图是矢量排版，可精确复现）；若过于复杂，
  裁页图插入并加 `\transnote{本图为原书页图裁切，未重绘}`。
- **译者注**：`\transnote{...}` 独立成段；每块 8–15 条，只写三类（易错预警/含糊点拨/背景直觉），
  不写"这里作者意思是"式的越俎代庖，不补证明。
- **记号**：preamble 有 `\R \C \Z \Q \N \PP \cA…\cZ \fA…\fZ \Vdual \DBCoh \Hom \End …`；
  新记号先加进 preamble 的「常用记号」区并记 README，不要在每个块里重复定义。
- **不要**：`\documentclass`、`\usepackage`、`\begin{document}`、`\cite`、`\tag`、
  手工 `\setcounter`、改 `preamble.tex` 以外的全局设置（改 preamble 须在 README 变更日志记一条）。

---

## §7 术语与批注

1. **先冻结再翻译**：c01 完成后，把 `work/glossary.tsv`（草案已给 45 条）逐条复核，
   补全本论文实际出现的术语，冻结为 v1，并在 README 写「术语冻结日期 + 版本」。
   冻结后**禁止**在后续块里改译名（要改必须全局替换 + 三同步 + 记变更日志）。
2. **判定四问**（纪律 §2）：中文学界是否有通行译名？旧译是否生造？是否与已有术语撞车？
   是否一词多义？四问有一项不过，就保留英文（首次出现括注中文解释）。
3. **禁止音译**（Koszul、Morita、Novikov、Calabi–Yau 等惯用者除外）。
4. **人名**：一律保留英文原名（Cannizzo、Auroux、Kontsevich、Strominger…），不音译。
5. **首次出现**：`中文（English）`，如「同调镜像对称（homological mirror symmetry）」；
   表外术语首次出现必须括注并报备（写进报告，由 Lead/下游统一）。
6. **专有名词保留英文**：`HMS`、`SYZ`、`Fukaya–Seidel`、`wrapped Fukaya 范畴`、
   `A∞`、`Bridgeland 稳定性`、`crepant resolution`（本论文关键概念，中文无稳定译名）。
7. **批注总量**：全文 100–140 条（每块 8–15 条），三类各占约 1/3；批注不重复原文内容。

---

## §8 中文文风硬指标（`check.py` 会查）

- **病灶清单必须为 0**：「被……所」「进行……的讨论/计算」「对于……而言」「关于……的讨论」
  「使得……得以」「起到了……的作用」「有着……的意义」「众所周知」「不难发现」「值得注意的是」。
  这些是机翻腔的标志，不是绝对禁用词——但**一律绕开**，用主动句、短句。
- 一句一个逻辑重心，**单句 ≤60–70 汉字**（列举句 ≤90）。长句拆开，用「因此」「于是」「也就是说」
  衔接，不靠逗号串。
- 中文全角标点；英文术语、数字与汉字之间留半角空格（`设 $X$ 是 2 维复流形`）。
- 不用「其/该/之」堆叠；不用「笔者」「我们」（原文 "we" 译「我们」时保留，这是作者的口吻）。
- 数学陈述用「设……，则……」「若……，则……」「称……为……」，不用「如果……的话」。
- 译完自己朗读一遍：读起来像中文数学书，不像翻译腔。

---

## §9 报告模板 `reports/cNN.md`

```markdown
# cNN 报告（原书 p.X–Y）

## 完成情况
- 页数：X–Y，共 N 页；行数/字数：约 N 千字
- 小节：§…（标题）
- 图：图 X.Y（裁图 fig_X_Y.png）、交换图 N 个（tikz-cd 重画 / 页图裁切）
- 定理环境：共 N 个（定义 a、定理 b、注 c…），编号与原文核对：一致
- 自检：compile_chunk cNN → errors=0 overfull=0 undefined=0 missing_char=0

## 疑点与请示
- 原文 p.X 第 N 行：……（读法一 / 读法二），暂取……，待复核

## 术语
- 新增：English → 中文（依据：…）
- 改动：无（冻结版 v1）

## 译文取舍
- p.X：原文……译为……，理由……
```

`review/` 里每完成 2–3 块写一份 `review/chNN_chMM.md`：逐段对原文语义 + 逐公式对页图，
记录发现的问题与修正。

---

## §10 关键提醒

1. **数学正确性最高**（纪律 §0）。宁可译得朴素，不可译错；宁可保留英文，不可生造。
2. **不臆造**：原文省略处不补、含糊处加批注、疑似错误保留原样并加 `% [Tutor Note: ...]`。
3. **读不懂就写报告**：把疑点列进 `reports/cNN.md`，用最保守的译法先过，不要卡住整块。
4. **每块必须编译通过**才写报告；单块编译不过就不要进入下一块。
5. **时间分配**：一块 10–20 页的正文，通常需要 1–2 小时；不要为追求速度跳过页图核对。
6. **本文件与 README 是跨会话的记忆**：进度、术语、变更、遗留问题都写进去，
   下个会话的你能靠它们无损接续。
7. 工具受限时（如某页图看不清），用 `zoom.py` 提高 dpi 再裁；仍不行就在报告里记「待人工核对」，
   不要猜公式。

---

## §11 初始冻结译名（v0 草案，c01 后复核冻结）

见 `work/glossary.tsv`（TSV：英文 \t 中文 \t 备注/依据）。要点：

- homological mirror symmetry → 同调镜像对称；HMS 保留英文缩写
- mirror symmetry → 镜像对称；SYZ / Strominger–Yau–Zaslow → 保留英文
- Fukaya category → 深谷范畴；Fukaya–Seidel category → Fukaya–Seidel 范畴（保留）
- derived category → 导出范畴；bounded derived category of coherent sheaves → 有界相干层导出范畴
- coherent sheaf → 相干层；line bundle → 线丛；divisor → 除子；hypersurface → 超曲面
- abelian variety → 阿贝尔簇；elliptic curve → 椭圆曲线；genus 2 curve → 亏格 2 曲线
- toric variety → 环簇；fan → 扇；moment polytope → 矩多面体；moment map → 矩映射
- Lagrangian submanifold → 拉格朗日子流形；Lagrangian torus fibration → 拉格朗日环面丛
- symplectic form → 辛形式；symplectic fibration → 辛纤维丛；Kähler → 凯勒
- Calabi–Yau → 卡拉比–丘；Landau–Ginzburg model → 朗道–金兹堡模型；superpotential → 超势
- critical locus → 临界轨迹；crepant resolution → 保留英文（crepant resolution）
- exceptional collection → 例外收集体；Bridgeland stability → Bridgeland 稳定性
- tropical geometry → 热带几何；tropical curve → 热带曲线；toric degeneration → 环簇退化
- Floer cohomology → 弗洛尔上同调；pseudo-holomorphic curve → 伪全纯曲线；moduli space → 模空间
- blow-up → 爆破；orbifold → 轨形；quotient → 商；complex structure → 复结构
- A-model / A-side → A 模型 / A 侧；B-model / B-side → B 模型 / B 侧
- cohomologically fully faithful → 上同调意义下全忠实
- Lefschetz thimble → 顶针（Lefschetz thimble）；wrapped Fukaya 范畴 → 保留英文

---

## §12 交付七件套（`deliverable\`）

1. `EN48_Cannizzo_亏格2曲线HMS_中文译注本.pdf`（build.ps1 产出）
2. `README.md`（交付说明：底本、页映射、页数、术语冻结版、已知问题）
3. `译注汇总.md`（全部 `\transnote` 按块汇总，附页码）
4. `阅读参考指南.md`（各章地图、前置知识、建议阅读路径、术语速查）
5. `工程总结.md`（≥150 页必写：流程、问题、经验、耗时）
6. `术语对照表.tsv`（冻结术语最终版，从 `work/glossary.tsv` 导出）
7. `源码_LaTeX.zip`（`src/` 完整打包）

收尾：更新 `04_编号登记表.csv` 的 EN48 行（状态「已交付」、日期、路径），
在 README 记录 v1.0 交付日期与页数。
