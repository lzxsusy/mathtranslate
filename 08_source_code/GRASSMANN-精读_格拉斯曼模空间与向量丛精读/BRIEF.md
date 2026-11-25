# 格拉斯曼流形精读工程 · 总任务书（BRIEF）

> 本文件是本工程**唯一权威说明**。Lead、章读者、卡片手开工前必须读完本文件与 `STATUS.md`。
> 与子任务书冲突时以本文件为准；本文件没写的，按 `_cards_shtuka` / `Shtuka校定` 的既有惯例办。

---

## 0. 目标与交付物

对象是一本书：**《Grassmannians, Moduli Spaces and Vector Bundles》**（Clay Mathematics Proceedings 14，
AMS/Clay 2011）——9 篇彼此独立的会议论文，主题围绕格拉斯曼流形、模空间与向量丛。已有一份完整的
中文译本（170 页）与完整 LaTeX 源（77,000 中文字）。

任务：**读 + 审校**，产出四类交付物。

| # | 交付物 | 位置 | 内容 | 数量 |
|---|---|---|---|---|
| 1 | 导读 | `产出\导读\` | `00-全书导读.md` + `chNN-导读.md` | 1 + 9 |
| 2 | 批注 | `产出\批注\` | `chNN-批注.md`（每章 ≥12 条）+ `00-审校总表.tsv` + `00-修订补丁.md` | 9 + 2 |
| 3 | 读书笔记 | `产出\笔记\` | `chNN-笔记.md` | 9 |
| 4 | 资料卡 | `..\_cards_grassmann\`（Downloads 根） | 概念卡 60–75 + 例子卡 15–20 | ~85 |

「审校」不是第五类文件，而是贯穿在批注里的两件事：

- **对读**：中文 .tex ↔ 英文原书 PDF，找误译、漏译、术语不统一、公式抄错、编号错位；
- **校核已有译注**：译者自己登记了 **81 处「原书错误/译注」**（清单在 `source\PROGRESS.md` 的
  `## 原书错误（译注清单）`，按篇分 9 张表）。你要判断这些译注**说得对不对**，并**不再重复登记**它们。

审校结论落两张表：`errata.tsv`（问题清单，带位置与证据）与 `00-修订补丁.md`（原句 → 改句，可直接照改）。

**不在本轮范围**：改写 `source\` 下的 .tex、重编译交付版 PDF、翻译新文献。`source\` 全程只读。

---

## 1. 输入（三条材料，权威性不同，别搞混）

| 材料 | 路径 | 页数 | 用途 | 权威性 |
|---|---|---|---|---|
| 中文 LaTeX 源 | `source\chapters\ch01..ch09.tex`、`frontmatter.tex` | — | 中文正文与公式 | ★★★ 文字与公式 |
| 中文交付版 | `zh-译文.pdf` | 170 | 版面、页码、定理盒、脚注实物 | ★★★ 页码与版面 |
| 英文原书 | `original\en-原书.pdf` | 190 | 审校对照底本 | ★★★ 原文 |

铁律：

1. **中文数学内容是 .tex 说的算**。PDF 文字层把公式拆碎（例：p12 抽出 `DV f = V [f] + ˜D(V )(f)`、
   `ˆ∇e_V T (k)`），只能用来定位页码与看版面。
2. 页码必须写清是哪种：`原书 p.N`（AMS 页码）/ `中译 p.N`（zh-译文.pdf 页序）/ `英文 PDF p.N`。
   关系：**英文 PDF 页 = 原书页 + 9**（原书 p.1 = 英文 PDF p.10）。中译页与原书页**不是**线性平移
   （ch1 是 +6，ch9 是 −9），**只信下表**。
3. `source\` 与 `original\` 只读。所有产出写 `产出\` 与 `..\_cards_grassmann\`。

### 1.1 页表（`tools\pdf_pages.py` 的 CH 表，权威）

| 篇 | 作者 | 主题 | 中译页 | 英文 PDF 页 | 原书页 | 源文件 |
|---|---|---|---|---|---|---|
| 前言 | 编者 | 引言 | 1–6 | 1–9 | i–viii | `frontmatter.tex` |
| ch1 | Andersen & Gammelgaard | Hitchin 射影平坦联络、Toeplitz 算子与 TQFT | 7–29 | 10–33 | 1–24 | `ch01.tex` |
| ch2 | Aprodu & Farkas | Koszul 上同调及其在模空间中的应用 | 30–54 | 34–59 | 25–50 | `ch02.tex` |
| ch3 | Arcara & Bertram | 重访 Reider 定理与 Thaddeus 对 | 55–71 | 60–77 | 51–68 | `ch03.tex` |
| ch4 | Jeffrey | 奇异向量丛模空间中的相交配对 | 72–81 | 78–89 | 69–80 | `ch04.tex` |
| ch5 | Kamnitzer | Beilinson–Drinfeld 格拉斯曼流形与辛纽结同调 | 82–93 | 90–103 | 81–94 | `ch05.tex` |
| ch6 | Lieblich | 曲线上层模空间的算术方面 | 94–115 | 104–129 | 95–120 | `ch06.tex` |
| ch7 | Newstead | 代数曲线上 α-稳定凝聚系的存在性 | 116–134 | 130–149 | 121–140 | `ch07.tex` |
| ch8 | Pareschi & Popa | 阿贝尔簇上的正则性 III | 135–159 | 150–177 | 141–168 | `ch08.tex` |
| ch9 | Teixidor i Bigas | 可约曲线上的向量丛及应用 | 160–170 | 178–189 | 169–179 | `ch09.tex` |

已核实：全书 **81 处译注**（ch1 8 / ch2 14 / ch3 5 / ch4 3 / ch5 7 / ch6 13 / ch7 6 / ch8 18 / ch9 7），
参考文献 **323 条**，插图仅 ch1 两幅行内示意图（`source\figures\ch01-link.png`、`ch01-curveop.png`）。

### 1.2 术语

`source\TERMINOLOGY.md`（345 行）是译名权威，分「书名与核心术语 / 论文集与会议 / 代数几何 / …」等小节。
写作要求：导读、批注、笔记、卡片里的中文术语**一律照它**；它没收的术语，写 `产出\汇总\术语增补.tsv`
（`en <TAB> zh <TAB> 出处 <TAB> 备注`），**不要改 TERMINOLOGY.md**。

### 1.3 编号体制（写批注时别把编号当成错）

- ch1：`\setupchapterindep`，定理/定义/引理各自独立编号（Theorem 1–13、Definition 1–7…），公式 (1)–(23)。
- ch2 / ch5 / ch7 / ch8 / ch9：`\setupchaptersecshared`，按节共享（Theorem 1.1、Definition 2.5…）。
- ch3：混合——`application`/`proposition`/`corollary` 按节共享，`iquestion` 独立编号 1–5。
- ch4：混合——`definition`/`theorem`/`remark` 按节共享，`iremark` 独立编号 1–3。
- ch6：按节 / 按小节混合（§5 用 `5.1.1` 式；附录 A 先 `A.1` 后 `A.1.1`，附录 B/C 按节 `B.1`–`C.4`）。

---

## 2. 环境与命令

```
PY  = C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe
（3.12.14，含 pymupdf / Pillow / numpy / pandas / python-docx / openpyxl）
pandoc = C:\Users\admin\AppData\Local\Pandoc\pandoc.exe     # md → docx
xelatex = C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe
```

工程内工具（本目录下跑）：

```
python tools\preflight.py                 # 环境自检：文件/页数/页表/字体/pandoc，产出 preflight.txt
python tools\pdf_pages.py map             # 打印页表
python tools\pdf_pages.py text zh 30-34   # 导中译文本（默认写到 tmp\）
python tools\pdf_pages.py text en 43-47 -o tmp\en_ch02.txt
python tools\pdf_pages.py png zh 30 --dpi 140 --out 产出\_pages   # 渲页看公式
python tools\chapter_task.py 3            # 打印第 3 章任务书（Lead 直接发给 subagent）
```

坑（都是本机实测过的）：

- **没有 `read` 工具**：读文件用 `ops_inspect_local_file`（带 offset/limit）。
- **PowerShell 没有 heredoc**；`ops_bash` 是 Git Bash，可以用 heredoc，但超过 1KB 的脚本一律先 `write` 成
  `.py`/`.sh` 再跑。
- 终端编码偶发乱码：脚本结果写 UTF-8 文件，再用 `ops_inspect_local_file` 读，别靠 stdout 判断中文。
- 本会话审批被自动拒绝：**不要请求提权**（`sandbox_permissions` 一律不填）。
- 本地编译不可靠：缺 Noto Serif CJK SC / AR PL Kaiti GB / DejaVu Serif，`build_local.py` 换字体后能出 167 页
  （交付版 170），且有缺字与 undefned 警告。**版面与页码判断一律以 `zh-译文.pdf` 为准，不要拿本地编译当证据。**

---

## 3. 工程结构与写入权限

```
Grassmannians-精读\
  BRIEF.md              本文件（Lead 维护）
  STATUS.md             进度台账（Lead 每 phase 更新，唯一真相来源）
  source\               中文 LaTeX 源（只读）
  zh-译文.pdf           中文交付版 170 页（只读）
  original\en-原书.pdf  英文原书 190 页（只读）
  tools\                pdf_pages.py / preflight.py / chapter_task.py
  build_local.py        本地试编译（只用于粗检，结论不作数）
  tmp\                  临时文本/渲染（可随时删，不入交付）
  产出\
    导读\  批注\  笔记\  汇总\  _pages\
```

写入权限（违反即返工）：

- 章读者：只写 `产出\导读\chNN-导读.md`、`产出\批注\chNN-批注.md`、`产出\批注\chNN-errata.tsv`、
  `产出\笔记\chNN-笔记.md`、`产出\汇总\cards-chNN.tsv`、`产出\汇总\chNN-report.md` 与自己章号的 `tmp\*`。
- 卡片手：只写 `..\_cards_grassmann\cards\*\*.json` 与自己的 `产出\汇总\cardNN-report.md`。
- Lead：其余全部（BRIEF/STATUS/00-* 汇总/术语增补/汇编）。
- **任何人不得写 `source\`、`original\`、`zh-译文.pdf`**；`TERMINOLOGY.md` 只读。

---

## 4. 工作流（Phase 0 → 4）

### Phase 0 · 预热（Lead，~30 min）

1. `python tools\preflight.py`，全 OK 才开工；有 FAIL 先修（页数不对说明 PDF 换了）。
2. 读 `STATUS.md`：若某章已是 `done` 就跳过，**不要重做**（本任务可能被重跑/中断）。
3. 读 `source\PROGRESS.md` 的 `## 原书错误（译注清单）` 全部 9 张表，把 81 处译注按章抄成
   `产出\汇总\existing-notes.tsv`（`ch <TAB> 原书页 <TAB> 一句话摘要`），发给各章读者，避免重复登记。
4. `python tools\chapter_task.py NN` 生成 9 份任务书备用（不必一次全发）。
5. 抽检：`python tools\pdf_pages.py png zh 7 --out 产出\_pages`，确认渲染正常、页表没漂。

### Phase 1 · 骨架（Lead，~40 min，与 Phase 2 并行）

1. 写 `产出\导读\00-全书导读.md`：这本书是什么（Clay 文集、9 篇独立论文、2011）、为什么这 9 篇能凑成一本书
   （共同对象：曲线/阿贝尔簇上的模空间与向量丛；共同工具：稳定性、上同调、Koszul、一般消没）、
   三条阅读路线（① 模空间主线 ch2→ch7→ch9→ch6；② 几何/量子主线 ch1→ch3→ch4；③ 阿贝尔簇与 representation
   主线 ch5→ch8）、各章一句话定位、术语地图。目标 2000–3000 字。
2. 建 `产出\汇总\` 下的空台账：`existing-notes.tsv`、`术语增补.tsv`、`交叉引用.md`。
3. 开跑 Phase 2 后，Lead 不要空等：起草 `00-修订补丁.md` 的骨架与 `汇总\审校方法.md`。

### Phase 2 · 九章精读 + 审校（9 个 subagent 并行）

一章一个 subagent，用 `tools\chapter_task.py NN` 打印的任务书（模板见 §6）。每人交 6 个文件（§8 格式）。

产出重心（每章）：

- **导读** 1200–2000 字：本章在全书的位置、前置知识、阅读路线（哪节可跳）、核心结果 3–5 条、术语对照。
- **批注** ≥12 条，覆盖五种类型（见 §7），尤其要有「数学-难点」「译注-核对」。
- **笔记** 1500–2500 字：主线复述（用自己的话）、关键构造的逻辑链、自己补的推导/例子、疑问清单、延伸阅读。
- **errata**：对照英文逐段核，登记新问题；**81 处已登记的不许重登**（若认为某条登记有误，另立
  `type=existing-note-wrong` 行并在批注里说明）。
- **卡片候选** `cards-chNN.tsv`：≥6 概念 + ≥1 例子，一行一卡，带 anchor（`chapters/chNN.tex:行号`）。

并行度：9 个同时发。若并发受限或上下文吃紧，分两波（ch1–ch5 / ch6–ch9），第一波回来立刻发第二波。

Lead 在这一阶段的工作：逐章验收（§7），不合格打回一次（附具体缺什么），仍不合格就自己补。

### Phase 3 · 资料卡（3–4 个卡片手并行）

1. Lead 汇总 9 份 `cards-chNN.tsv` → 去重、并卡、定 id，写 `..\_cards_grassmann\taxonomy.md` 清单表。
2. 按轨道分工发卡片手（见 §9），每人 15–25 张 JSON。
3. `python ..\_cards_grassmann\tools\validate_cards.py --strict`，0 error；`build_index.py` 生成 index。
4. Lead 抽查 1/3 的卡：定义是否与正文一致、公式有没有抄错、anchor 行号是否真指向该内容、related 是否能解析。

### Phase 4 · 收尾（Lead）

1. `00-审校总表.tsv` 合并 9 份 errata，按 `章节/类型/严重度` 排序；统计：新发现问题数、其中译文错 / 原书错 /
   术语问题 / 排印问题各多少；与 81 处已有译注交叉（有没有漏网、有没有误判）。
2. `00-修订补丁.md`：每条给「位置 / 原句 / 改句 / 依据」，按章排列，可直接照改。
3. `汇总\格拉斯曼精读报告.md`：做了什么、四个交付物清单、9 章一句话结论、审校统计、遗留问题。
4. 用 pandoc 把 `导读\00` + 9 章导读 + 报告合成 `汇总\格拉斯曼精读·导读与审校报告.docx`
   （`pandoc -f markdown -t docx --toc -o ... *.md`；中文 docx 不需要额外字体）。
5. 更新 `STATUS.md` 全绿，向用户中文汇报（结论先行、给路径、说统计）。

---

## 5. 九章任务卡

> 每章的「必抓」是**提示**不是清单：以正文实际核心对象为准，缺了要补、多了可减。

### ch1 · Andersen & Gammelgaard · Hitchin 射影平坦联络、Toeplitz 算子与 TQFT 曲线算子的渐近展开
- 范围：中译 p.7–29（23 页）= 英文 PDF p.10–33 = 原书 p.1–24。源：`chapters\ch01.tex`（76,698 B）。
- 结构：§1 引言 / §2 Hitchin 联络 / §3 Toeplitz 算子与 Berezin–Toeplitz 形变量子化 / §4 形式 Hitchin 联络。
- 必抓：Hitchin 联络、射影平坦性、模空间 M 与紧化 M̄、曲线算子（TQFT）、Toeplitz 算子、
  Berezin–Toeplitz 形变量子化、星积 ⋆^BT、Bohr–Sommerfeld 层、几何量子化、半经典（h→0）渐近展开。
- 难点：微分几何与辛几何前置多（联络、曲率、复结构形变）；Toeplitz 算子的符号计算密集；
  (3) 式与 Theorem 7 的一阶项符号分歧（已有译注 7、8）。本章定理环境是 `i*` 独立编号（Theorem 1–13）。
- 已有译注 8 处。卡片配额：概念 8 / 例子 2。

### ch2 · Aprodu & Farkas · Koszul 上同调及其在模空间中的应用
- 范围：中译 p.30–54（25 页）= 英文 PDF p.34–59 = 原书 p.25–50。源：`chapters\ch02.tex`（89,032 B）。
- 结构：§1 引言 / §2 Koszul 上同调（合冲、定义、核丛、Hilbert 概形）/ §3 模空间上的几何闭链
  （Brill–Noether 闭链、Koszul 闭链、小斜率除子）/ §4 Green 猜想、棱性猜想 / §5 强极大秩猜想、
  极小合冲猜想。
- 必抓：Koszul 上同调 K_{p,q}(X;L)、合冲 syzygy、极小自由分解、核丛、Hilbert 概形、
  Brill–Noether 闭链、Koszul 闭链、小斜率除子、Green 猜想、棱性（gonality）猜想、强极大秩猜想、
  极小合冲猜想。25 个 theorem、7 个 conjecture——本书概念密度最高的一章。
- 难点：Eagon–Northcott 复形与 Koszul 复形的具体构造；各猜想之间的关系网（谁强谁弱、哪些情形已知）。
- 已有译注 14 处。卡片配额：概念 12 / 例子 3。

### ch3 · Arcara & Bertram · 重访 Reider 定理与 Thaddeus 对
- 范围：中译 p.55–71（17 页）= 英文 PDF p.60–77 = 原书 p.51–68。源：`chapters\ch03.tex`（56,962 B）。
- 结构：§1 引言 / §2 原始的 Reider 定理 / §3 重访 Reider 定理 / §4 重访 Thaddeus 对 / §5 三维情形的
  Reider 定理？
- 必抓：Reider 定理、Thaddeus 对、Bridge 与翻转（flip）、例外对象/正交基、Bogomolov 型稳定性、
  曲面上的模空间、射影对偶、导出范畴视角（若正文出现）。
- 难点：曲面上向量丛的 moduli 与稳定性理论；Reider 的证明用到的构造（本章 §3 是重写版，要抓「重访」
  相比原版的改动）。编号混合：`application`/`proposition`/`corollary` 按节共享，`iquestion` 独立 1–5。
- 已有译注 5 处。卡片配额：概念 7 / 例子 2。

### ch4 · Jeffrey · 奇异向量丛模空间中的相交配对
- 范围：中译 p.72–81（10 页）= 英文 PDF p.78–89 = 原书 p.69–80。源：`chapters\ch04.tex`（32,374 B）。
  （原书 p.80 是空白背面页。）
- 结构：§1 引言 / §2 部分消奇异 / §3 M(2,0) 的部分消奇异 / §4 相交上同调 / §5 Kiem 的等变上同调与
  相交同调结果 / §6 关于 M(n,d) 的相交上同调结果。
- 必抓：部分消奇异（partial desingularization）、相交上同调、等变上同调、Kiem 定理、
  M(n,d) 与 M(2,0)、相交配对、Kirwan 消奇异、局部化公式。
- 难点：相交上同调的层论定义与 de Rham 版本对照；等变上同调在奇点上的行为。编号混合（`iremark` 独立）。
- 已有译注 3 处。卡片配额：概念 6 / 例子 1。

### ch5 · Kamnitzer · Beilinson–Drinfeld 格拉斯曼流形与辛纽结同调
- 范围：中译 p.82–93（12 页）= 英文 PDF p.90–103 = 原书 p.81–94。源：`chapters\ch05.tex`（49,385 B）。
- 结构：§1 引言 / §2 纤维化（仿射格拉斯曼、Hecke 型概念、整体卷积格拉斯曼、整体奇异格拉斯曼、
  开整体卷积/奇异格拉斯曼）/ §3 半局部几何 / §4 与切片解消的比较（切片及解消、例子、比较定理）/
  §5 纤维的仿射性。
- 必抓：仿射格拉斯曼流形 Gr、Beilinson–Drinfeld 格拉斯曼流形、Hecke 修正、卷积（convolution）积、
  整体奇异格拉斯曼、半局部几何、切片（slice）与切片解消、比较定理、辛纽结同调、Khovanov 同调/量子群。
- 难点：卷积格拉斯曼的因子化结构；「奇异」与「卷积」两种版本的差异；与 knot homology 的桥在哪一句。
- 已有译注 7 处。卡片配额：概念 8 / 例子 2。

### ch6 · Lieblich · 曲线上层模空间的算术方面
- 范围：中译 p.94–115（22 页）= 英文 PDF p.104–129 = 原书 p.95–120。源：`chapters\ch06.tex`（92,033 B）。
- 结构：§1 引言 / §2 记号与假设 / §3 模空间形式与等平凡 Torelli / §4 Brauer 群与有理点 /
  §5 稳定扭曲层模空间与周期-指标定理 / §6 P¹ 上抛物丛 / §7 通过分裂分歧构造抛物模空间（一般性结果、
  延伸例子）/ §8 问题清单 / 附录 A Gerbe 与扭曲层（模空间、形变理论）/ B Brauer 群基本事实 /
  C Brauer 类的分歧。
- 必抓：模叠 Bun_{n,d}、Gerbe（带 band）、扭曲层（twisted sheaf）、Brauer 群 Br(X)、周期-指标定理、
  抛物丛、分裂分歧（ramified splitting）、Torelli 定理、有理点、形变-障碍理论。
- 难点：非交换几何术语（gerbe/band/中立化）与层论上同调的对应；附录 A–C 是自足的技术摘要，值得单独导读。
  编号：§1–4 按节、§5 按小节、附录混合。
- 已有译注 13 处。卡片配额：概念 8 / 例子 2。

### ch7 · Newstead · 代数曲线上 α-稳定凝聚系的存在性
- 范围：中译 p.116–134（19 页）= 英文 PDF p.130–149 = 原书 p.121–140。源：`chapters\ch07.tex`（58,639 B）。
  （原书 p.140 空白背面页。）
- 结构：§1 定义 / §2 存在性问题 / §3 方法 / §4 0<k≤n / §5 0<d≤2n / §6 k=n+1 / §7 n=2,k=4 /
  §8 k≥n+2 / §9 n=2,det E=K / §10 特殊曲线 / §11 奇异曲线 / §12 开放问题。
- 必抓：凝聚系 (E,V)、α-半稳定/稳定、模空间、存在性定理、边界情形 k=n+1 与 k≥n+2、
  Brill–Noether 型方法、特殊曲线、奇异曲线。12 个 question——本章的「开放问题」节是全书最有价值的部分之一。
- 难点：α 的阈值与稳定性判据；不同 (n,d,k) 区域的证明策略差异（这是本章的组织逻辑，笔记里要画成表）。
- 已有译注 6 处。卡片配额：概念 8 / 例子 2。

### ch8 · Pareschi & Popa · 阿贝尔簇上的正则性 III
- 范围：中译 p.135–159（25 页）= 英文 PDF p.150–177 = 原书 p.141–168。源：`chapters\ch08.tex`（92,371 B）。
  （原书 p.168 空白背面页。）
- 结构：§1 引言 / §2 GV-层与 M-正则层 / §3 张量积 / §4 GV-层的 nef 性 / §5 M-正则层的生成性质 /
  §6 极大 Albanese 维数非正则簇的多典范映射 / §7 M-正则性的进一步应用（指标与 Seshadri 常数、
  Picard 丛的正则性与对称积上的消没、半齐次向量丛的数值研究）。
- 必抓：GV-层（generic vanishing）、M-正则层、Ishida 复形、Fourier–Mukai 变换、nef、多典范映射、
  Seshadri 常数、Picard 丛、对称积、半齐次向量丛。
- 难点：一般消没理论的前置（GV 猜想的背景）；Fourier–Mukai 与「M-正则 ⇒ 生成」的推理链。
  11 theorem + 11 remark：remark 里常藏反例与比较，批注要抓。
- 已有译注 18 处（全书最多）。卡片配额：概念 9 / 例子 2。

### ch9 · Teixidor i Bigas · 可约曲线上的向量丛及应用
- 范围：中译 p.160–170（11 页）= 英文 PDF p.178–189 = 原书 p.169–179。源：`chapters\ch09.tex`（37,545 B）。
  （英文 PDF p.190 是封底，不译。）
- 结构：§1 引言 / §2 斜率稳定无挠层的模空间 / §3 模空间的 Hilbert 紧化及其与斜率稳定模空间的关系 /
  §4 极限线性系 / §5 向量丛的子丛 / §6 在 Brill–Noether 理论中的若干应用。
- 必抓：可约曲线、斜率稳定无挠层、Hilbert 紧化（Hilbert 多项式）、极限线性系、子丛、Brill–Noether。
- 难点：曲线可约/带奇点时稳定性的定义与紧化的比较（Gieseker vs 斜率）；短小但结论密度高。
- 已有译注 7 处。卡片配额：概念 6 / 例子 1。

---

## 6. 章读者任务书模板（`tools\chapter_task.py NN` 会自动填好）

```
你是《Grassmannians, Moduli Spaces and Vector Bundles》中译精读工程的第 <<NN>> 章读者。
工程根：C:\Users\admin\Downloads\Grassmannians-精读
你的章：<<chNN · 作者 · 标题>>，中译 p.<<a>>–<<b>>，英文 PDF p.<<c>>–<<d>>，原书 p.<<e>>–<<f>>。

## 先读
1. BRIEF.md 全文（尤其 §1 页表、§7 质量门、§8 文件格式）与 STATUS.md。
2. 产出\汇总\existing-notes.tsv 里你这一章的已有译注（<<n>> 条）——这些不要重复登记。
3. source\TERMINOLOGY.md（术语权威，只读）。
4. 你的中文源：source\chapters\ch<<NN>>.tex（<<size>> 字节，全章）。
5. 英文对照：python tools\pdf_pages.py text en <<c>>-<<d>> -o tmp\en_ch<<NN>>.txt，然后逐页读。
6. 版面核对：python tools\pdf_pages.py png zh <<a>> --out 产出\_pages（只渲你需要的页，别全渲）。

## 产出（6 个文件，路径与格式见 BRIEF §8）
1. 产出\导读\ch<<NN>>-导读.md     1200–2000 字
2. 产出\批注\ch<<NN>>-批注.md     ≥12 条，五种类型都要有
3. 产出\批注\ch<<NN>>-errata.tsv  对读发现的问题（类型/严重度/位置/原文/问题/建议）
4. 产出\笔记\ch<<NN>>-笔记.md     1500–2500 字
5. 产出\汇总\cards-ch<<NN>>.tsv   ≥6 概念卡 + ≥1 例子卡候选
6. 产出\汇总\ch<<NN>>-report.md   做了什么/统计/存疑/给 Lead 的 TODO

## 硬规则
- 只写上面 6 个路径；不改 source\ 与 original\；不改别的章的文件。
- 中文数学以 .tex 为准，公式不要从 PDF 文字层抄（会被拆碎）。
- 页码三种写法别混：原书 p.N / 中译 p.N / 英文 PDF p.N。
- 已有 81 处译注不重复登记；认为登记有误，另立 type=existing-note-wrong 并说明。
- 术语照 TERMINOLOGY.md；新术语写进 cards-chNN.tsv 的 note 列，不新建文件。
- 有卡片候选的 anchor 必须真指向该内容（写完用 ops_inspect_local_file 回查行号）。
- 不编造：读不懂的地方写进笔记的「疑问」，并在 report 里点出来。
- 文件 UTF-8 无 BOM、LF；用 write 工具写，不要 shell 重定向写中文。
- 交前自检：六个文件都在、字数达标、批注编号连续、tsv 列数对（tab 分隔，不许有裸 tab 混进正文）。
```

---

## 7. 质量门（Lead 验收用）

**每章必过**

- [ ] 六个文件齐、UTF-8 无 BOM、md 标题层级正常（`#` 章标题，`##` 小节）
- [ ] 导读 ≥1200 字，含五节：本章位置 / 前置知识 / 阅读路线 / 核心结果 / 术语对照
- [ ] 批注 ≥12 条，编号连续；类型覆盖：`数学-难点`、`数学-补证`、`译注-核对`、`译文-问题`、`联系-他章`
      各 ≥1；每条含「位置 + 原文摘录 + 批注 + 类型」
- [ ] 笔记 ≥1500 字，含五节：主线 / 关键构造 / 我的补全 / 疑问 / 延伸
- [ ] errata.tsv 列数一致、类型在枚举内、每条都能按位置回查（抽查 3 条）
- [ ] 卡片候选 ≥7 条，anchor 全部 `chapters/chNN.tex:行号` 且行号真指向
- [ ] **没有重复登记** 81 处已有译注（抽查该章前 3 条已有译注，确认没被当新问题）
- [ ] report.md 里「存疑」不为空（一章 12–26 页的数学论文，不可能零疑问；空说明没读进去）

**全篇必过**

- [ ] 9 章齐全，`00-审校总表.tsv` 行数 = 各章 errata 行数之和
- [ ] `00-修订补丁.md` 每条都有「原句 / 改句 / 依据」，抽查 10 条，原文能在 .tex 里 grep 到
- [ ] `_cards_grassmann` validate --strict 0 error，`index.jsonl` 与文件数一致
- [ ] 交叉引用：导读/笔记里提到别的章时，章号与 BRIEF §1.1 页表一致（抽查 10 处）
- [ ] 术语：随机抽 5 个术语，导读/批注/笔记/卡片四处译法一致，且与 TERMINOLOGY.md 一致
- [ ] `汇总\格拉斯曼精读报告.md` 的统计数字能对上实际文件（行数/字数/卡数）

---

## 8. 文件格式

### 8.1 `chNN-导读.md`

```markdown
# 第 N 篇 · 作者 · 标题（中译 p.a–b）

## 一、这一章在书里干什么
## 二、读它之前要知道什么
## 三、怎么读（路线 / 可跳过的部分 / 第一遍看到哪）
## 四、核心结果（3–5 条，每条给编号 + 一句话 + 为什么重要）
## 五、术语对照（中文 / English / 本章首次出现处）
```

### 8.2 `chNN-批注.md`

```markdown
# 第 N 篇批注（共 K 条）

> 位置写法：原书 p.N / 中译 p.N / chNN.tex:行号，三者并给其一即可。

## 1. 【数学-难点】标题
- 位置：原书 p.12；ch01.tex:233
- 原文：「……」
- 批注：……
- 关联：[[ch02-批注#7]]

## 2. 【译注-核对】……
```

类型枚举：`数学-难点` / `数学-补证` / `译注-核对` / `译文-问题` / `联系-他章` / `背景-补充`。

### 8.3 `chNN-errata.tsv`

表头固定：

```
chapter	loc_book	loc_zh	loc_tex	type	severity	original	problem	suggestion	evidence
```

- `type` ∈ `translation-error`（译文错）/ `original-error`（英文原书错）/ `term`（术语不统一）/
  `formula`（公式差异）/ `typo`（错字标点）/ `numbering`（编号错位）/ `existing-note-wrong`（已有译注说错）
- `severity` ∈ `high`（读不懂/结论错）/ `medium`（意思偏了）/ `low`（文字/标点）
- `evidence`：你凭什么这么判（对照的英文原句，或 .tex 里的公式）。

### 8.4 `chNN-笔记.md`

```markdown
# 第 N 篇读书笔记

## 一、主线（我自己的话复述）
## 二、关键构造的逻辑链
## 三、我补的推导 / 例子 / 反例
## 四、疑问（读不懂、想不通、需要查文献）
## 五、延伸（下一步读什么、能用在哪）
```

### 8.5 `cards-chNN.tsv`

```
local_id	type	title_en	title_zh	track	one_line	anchor
```

`local_id` 只在本章内唯一（如 `hitchin-conn`），最终 id 由 Lead 定。

### 8.6 `chNN-report.md`

做了什么（分节）、统计（批注数/errata 数/卡片候选数/字数）、存疑处、给 Lead 的 TODO。

---

## 9. 资料卡流水线（`..\_cards_grassmann\`）

与 `_cards_shtuka` 同一套（规范见该库 `SCHEMA.md`，本库 `SCHEMA.md` 是精简改写版）。要点：

- id：`grassmann/concept/<slug>` 或 `grassmann/example/<slug>`，文件名 = 最后一段。
- `track`：`A` 基础（模空间/稳定性/上同调，跨章）｜`1`–`9` 对应 chapter 1–9。
- `sources.anchor` 固定 `chapters/chNN.tex:行号`；`pages_zh` / `pages_en` 用中译页 / 英文 PDF 页。
- `summary` ≤120 汉字；`key_points` ≥3；`formulas` ≥1；`theorems` ≥1（proof.status=complete 需 steps≥2 且
  每步有 text+why；sketch 需 gap_note）；`pitfalls` ≥1（真坑，不是「注意细节」这种废话）；
  `related` ≥2 且必须能解析到真实存在的卡 id。
- `rights` 固定 `rewritten`；`status` 先 `draft`，Lead 抽查后改 `reviewed`。
- 卡片内容必须与**中译本正文**一致（不是英文原书的说法）；英文原书只在译文错时作依据，此时在
  `pitfalls` 里写清「中译此处与原文不符，见 errata」。
- 例子卡另有 `concept_refs`（≥2，指向概念卡）、`setup`、`computation`。

分派（Lead 按章把候选并成 3–4 组）：

| 组 | 轨道 | 卡数 |
|---|---|---|
| 甲 | A 基础 + ch1 + ch3 | 15–20 |
| 乙 | ch2 + ch7 | 18–22 |
| 丙 | ch5 + ch8 | 16–20 |
| 丁 | ch4 + ch6 + ch9 | 16–20 |

---

## 10. 失败处理

- **subagent 超时/崩**：把任务书减半（先交导读+批注，再补笔记+卡片），别重发同一个 prompt。
- **PDF 打不开/页数不对**：`preflight.py` 会报；先用 `pymupdf` 查 page_count，确认没换文件；换了就停下来问用户。
- **某章实在读不动**（数学太深）：允许「导读 + 少量批注 + 笔记里明写读不懂的地方」，但必须在 report 里
  标 `status=partial` 并说明卡在哪一节——**不许假装读懂**。
- **卡片 validate 不过**：按 error 行号改，不要改工具。
- **时间不够**：优先级 导读 > 批注 > 笔记 > 卡片。宁可 9 章导读都完整、卡片只做 40 张，也不要 3 章完美 6 章空白。
- 中断恢复：看 `STATUS.md`，已完成的不重做；`tmp\` 里的半成品可以复用。

---

## 11. 时间预算（18:00 起，单人 lead + 并行 subagent）

| Phase | 内容 | 预算 | 完成标志 |
|---|---|---|---|
| 0 | 预热 | 30 min | preflight.txt 全 OK、existing-notes.tsv 建好 |
| 1 | 全书导读 | 40 min | 00-全书导读.md 落盘 |
| 2 | 九章并行 | 3–4 h | 9×6 文件齐、验收过 |
| 3 | 资料卡 | 1.5–2 h | validate --strict 0 error |
| 4 | 汇总 | 1 h | 报告 + docx + STATUS 全绿 |

目标：次日 01:00–02:00 全部收工。写不完就按 §10 的优先级砍，并在报告里写清砍了什么。
