# TASK-translator · SY02-45 译手契约（主控制定，逐条强制）

> 本文件是 8 个译手 subagent 的唯一施工契约。凡与本文件冲突的"我觉得更好"一律无效。
> 主控（lead）保留术语裁定权与合并权；译手**不得**修改 `源码/preamble.tex`、`源码/main.tex`、`工程文件/work/glossary.tsv`、`工程文件/work/条目总表.tsv` 以及别人的 `sections/*.tex`。

---

## 0. 工程坐标

- 仓库根：`C:\Users\admin\Desktop\数译发布\gitee_shuyi`
- 工程根：`08_source_code/SY02-45_Scholze布尔巴基1252几何Langlands的证明/`
- 底本：Peter Scholze, *Geometric Langlands [after Gaitsgory, Raskin, …]*, Séminaire BOURBAKI 78e année (2025–2026), n° 1252, Mars 2026。**印刷页 = PDF 页**（页眉 `1252–NN`，NN 即印刷页号）。
- 逐页文本：`工程文件/work/src/p001.txt … p056.txt`（页首行就是 `1252–NN`）
- 分节文本：`工程文件/work/src/src-sNN.txt`（NN=01..13；其中 `1252–NN` 行是**页界**，必须原样理解成"以下内容属于印刷页 NN"）
- 页面图（**核对公式的唯一权威**）：`工程文件/work/pages/pNNN.png`，150 dpi，NNN 三位数
- 节清单与条目序列：`工程文件/work/sections.json`
- 术语冻结表：`工程文件/work/glossary.tsv`（英文 / 中文 / 依据 / 首现页 / 备注）
- 输出：`源码/sections/sNN-<slug>.tex`，slug 见 main.tex 的 `\input` 列表
- 自检：`工程文件/tools/check_sections.py`

Python 解释器一律用：
`C:/Users/admin/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/python.exe`
xelatex：`C:/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe`

---

## 1. 开工必读（按顺序，读完再动笔）

1. `04_playbook/01_数学文献翻译纪律.md` 的 §0（五条公理）、§2（术语纪律）、§3（数学内容纪律）、§4（十三条铁律）——只读这四节即可；
2. `工程文件/work/通读笔记.md` 与 `工程文件/work/通读笔记_4-13.md` 中**属于你分包的那几节**（了解该节在全篇论证中的位置，避免把承接句译成孤立句）；
3. `工程文件/work/glossary.tsv`（全文，约 130 条；冻结，改词只有主控能做）；
4. `源码/preamble.tex`（宏清单，写公式前必须看一遍）；
5. 你分包的 `工程文件/work/src/src-sNN.txt`。

---

## 2. 逐页工作流（不许跳步）

对每一页 NN：

1. 读 `src/pNNN.txt` 的文本，理解该页在说什么；
2. 打开 `pages/pNNN.png` **看图**，逐个核对：上标下标、花体字母、`\mathcal` 与 `\mathbb`、`^{\mathcal O_C}`、`\pi_1^{\mathrm{et}}`、`\hat G`、`\tilde G`、`G^\vee`、`\mathbb G_m`、`\overline{\mathbb Q}_\ell`、`\mathrm{Bun}`、`\mathrm{LocSys}`、`\mathrm{IndCoh}`、`\mathrm{Perv}`、`\ell`-adic 的 `\ell`、`\otimes` 与 `\oplus`、`!` 与 `*`（`f_!` / `f_*` / `f^!` / `f^*`）、`\mathbf{1}`（单位对象）、`\Delta`、`\to` 与 `\mapsto`；
3. 落笔写中文。**每一段开始前**先写页锚（见 §4.1）；
4. 写完该页再回头对一次图，确认没有把 `\mathcal{O}` 写成 `O`、把 `\mathfrak{g}` 写成 `g`。

**连字粘连黑名单（文本层的通病，必须靠图还原）**：
`XOC` → `X_{\mathcal O_C}`；`πet` 断成 `πet` + `1` → `\pi_1^{\mathrm{et}}`；`Ǧ` 被抽成 `G` 或 `Ǧ`；`BunG` → `\Bun_G`；`IndCohNilp` → `\IndCoh_{\Nilp}`；`Dqc` → `\Dqc`（`\D_{\qc}`）；`ffl`/`ffi` 连字 → `ffl`/`ffi` 正常；`Qℓ` → `\Ql`；`Fq` → `\Fq`；`SL2` → `\mathrm{SL}_2`；`GLn` → `\mathrm{GL}_n`；`H1(X,Ω1)` → `H^1(X,\Om^1_X)`。

---

## 3. 语言纪律

1. **一句 ≤60–70 汉字**。超过就断句，断在逻辑接点，不要断在"的"字后面。
2. 中文与拉丁字母/数字之间**一个半角空格**：`几何 Langlands 猜想`、`第 2 节`、`p 充分大`、`G-丛`（连字符两侧不加空格）。
3. **全角标点**：，。；：？！（）「」；但公式内的逗号、括号用半角。
4. **逻辑连接词逐一对应，禁止一律"因此"**：
   - Thus → 因此；Hence → 从而；Therefore → 所以；Consequently → 于是；
   - In particular → 特别地；Conversely → 反之；Similarly → 类似地；Likewise → 同样地；
   - Indeed → 事实上；Note that → 注意；Recall that → 回忆；More precisely → 更确切地说；
   - However → 然而；Moreover → 此外；Nevertheless → 尽管如此；On the other hand → 另一方面；
   - In fact → 实际上；As a consequence → 作为推论；For this reason → 出于这个原因。
   **英文原句没用连接词，中文也不许加**（这是"不补写"的一部分）。
5. 禁「被……所……」「进行……的讨论」「对……进行刻画」这类翻译腔；「其中」不要滥用；「即」与「也就是说」择一。
6. 人名、定理名、软件名、期刊名不译：Scholze、Gaitsgory、Langlands、Weil、Beilinson、Drinfeld、Fargues–Fontaine、Kac–Moody、Satake、Whittaker、Hecke、Eisenstein、Frobenius、Riemann–Hilbert、Casselman–Shalika、Harder–Narasimhan、Cartier、Verdier、Serre、Poincaré。
7. 书名/论文名在正文首次出现时给英文原名 + 中文意译括号，之后只中文；参考文献节保留原文不动（只把 `References` → `参考文献`）。

---

## 4. LaTeX 体例

### 4.1 页锚与节标题

```latex
\section{引言}\srcpage{1}
```
- 每个 `\section{中文标题}` 后紧跟 `\srcpage{N}`（该节起始印刷页）。
- 之后**每换一页**（含跨页的段落！）在正文中插入 `\srcpage{N}`，N 为该处印刷页。
  段落跨页时，页锚插在跨页处的句子之前或之后均可，但**必须精确**。
- 页锚是零宽宏，插在句中不会破坏排版；但不要插在 `$...$` 内部、不要插在命令参数里。
- §13 参考文献用 `\section*{参考文献}`，同样带 `\srcpage{53}`。

### 4.2 编号条目（**编号零手写**）

原文形如 `Remark 2.1. — 正文…`、`Theorem 2.2. — 正文…`、`Conjecture 2.10 (Geometric Langlands Conjecture). — 正文…`，
一律译成对应环境，**按原文出现顺序逐个排**，编号由 LaTeX 计数器自动生成（同节共用序号，见 preamble）：

| 原文 | 环境 | 首行写法 |
| --- | --- | --- |
| Theorem 2.2. — | `theorem` | `\begin{theorem}正文…\end{theorem}` |
| Remark 2.1. — | `remark` | `\begin{remark}…\end{remark}` |
| Conjecture 2.10 (Geometric Langlands Conjecture). — | `conjecture` | `\begin{conjecture}[几何 Langlands 猜想]…\end{conjecture}` |
| Definition 5.5. — | `definition` | `\begin{definition}…\end{definition}` |
| Proposition 5.8. — | `proposition` | 同上 |
| Corollary 5.3. — | `corollary` | 同上 |
| Lemma | `lemma` | 同上 |
| Example 8.1. — | `example` | 同上 |
| Assumption 1.1. — | `assumption` | 同上 |
| Problem 1.2. — | `problem` | 同上 |

- `(...)` 中的原名（如 `(Geometric Langlands Conjecture)`）放**可选参数**，译成中文。
- **禁止**手写"定理 2.2"作为条目标题（正文内**引用**时当然要写"定理 2.2"，那是文字，不是编号）。
- 条目内的段落照样分段；条目末尾可带 `\srcpage{}`。
- 原文条目内若有 `Proof.`：`\begin{proof}…\end{proof}`；`Sketch of proof.` → `\begin{proof}[证明概要]`。

### 4.3 禁用命令（全书零容忍）

`\ref`、`\eqref`、`\label`、`\cite`、`\pageref`、`\autoref`、`\nocite`、`\bibliography`。
- 原文交叉引用一律写成**文字**：`Theorem 2.2` → `定理 2.2`；`§5` → `第 5 节`；`(3.4)` 之类公式号 → `前式`；`loc. cit.` → `同上`；`ibid.` → `同上`。
- 行间公式一律不编号：用 `\[ … \]` 或 `\begin{equation*}…\end{equation*}`，不要 `equation`。
- 需要 `\begin{aligned}` 时放在 `\[ … \]` 内。

### 4.4 宏（优先用 preamble 里已有的）

```latex
\Bun \Hck \Gr \LocSys \Rep \IndCoh \Coh \Perf \Perv \Sch \Corr \Fun \End \Hom \Map
\Spec \Pic \Sht \KL \Op \Whit \Sat \Frob \tr \Eis \CT \Higgs \Aut \id \pr \crit
\Gd \Bd \Td \Ud \Md        % \check G, \check B, ...（对偶群/对偶环面）
\LG \LpG \LU \LT \LB \LUd  % ^L G, ^L G^+, ^L U, ...
\cA … \cZ                 % 花体大写
\gc \bc \uc \nc \tc \pc \mc % 哥特体 g,b,u,n,t,p,m
\Z \Q \R \C \F \A \Gm \Ql \Zl \Fq \Fp
\dR \et \Betti \qc \Nilp \Ran \Weil \coarse \restr \irred \monfree \lisse \prim \suave \Lisse \Ind \PrL \e \Th \Om \OmX \Dmod \perf \pt \loc \alg \der \op \ee{}
\dsp \refitem{}{}
```
用法示例：`\Bun_G`、`\LocSys_{\Gd}`、`\LocSys^{\Betti}_{\Gd}`、`\IndCoh_{\Nilp}(\LocSys_{\Gd})`、`\D_{\qc}(\Bun_G)`、`\Perv(\Hck^{\loc}_G)`、`\Rep(\Gd)`、`\Ql`、`\Fq`、`\Gm`、`\LG`、`\LpG`、`\cO_C`、`\gc`。
**不要给这两个宏改名，也不要新增与它们同名的宏。** 确实缺宏时：在自己文件顶部用一行 `\providecommand{\xxx}{...}` 声明并在 reports 里登记。

### 4.5 译注

格式：`\yizhu{内容}{等级（出处）}`，只许三类：
1. 术语背景（A/I/B 级来源必写）；
2. 原文省略（Bourbaki 体例省掉的细节，如"此处 X 设为 g≥2 的紧 Riemann 面"，须说明依据）；
3. 原文笔误（须给出页码与判断依据）。

- 每条译注**必须**带等级与出处：如 `\yizhu{Betti 与 étale 情形的术语差异见 \textit{Geometric Satake} 综述（A 级：AGKRV 2020b §1）}{A（AGKRV 2020b §1）}`。
- 若无外部依据、纯由上下文推断，写 `{译者按（上下文推断，无外部依据）}`，不得伪装成 A 级。
- **严禁**在正文里写"作者大概是说""此处应为"而不进译注；也**严禁**用译注补写原文没有的数学内容。
- 数量控制：每节 ≤6 条，宁少勿滥。

---

## 5. 数学内容纪律

1. **照译**：原文含糊就照译 + 译注；原文错误照译 + 译注；原文省略就省略，不补。
2. **不合并、不拆分段落**：原文一段 = 中文一段（列表项、脚注同）。
3. **不美化**：不要给"显然""容易看出"加上原文没有的证明思路；不要把 `It is expected that` 译成"可以证明"。
4. 定理陈述里的条件（"p 充分大""k 特征 0""k 特征 p > c(G)""除 g=2 且 G 为 A₁ 型外"）一个字都不能丢。
5. 引用他人结果时保留"（作者 年份，定理号）"结构：`（Gaitsgory–Raskin 2025a，定理 0.2.2）`。
6. 脚注照译，编号由 LaTeX 自动生成；脚注内若有公式，同样对图核。

---

## 6. 自检与交付

每写完一节（一个文件）立刻跑：

```bash
cd "C:/Users/admin/Desktop/数译发布/gitee_shuyi/08_source_code/SY02-45_Scholze布尔巴基1252几何Langlands的证明"
"C:/Users/admin/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/python.exe" 工程文件/tools/check_sections.py NN
```

必须看到 `OK` 才能交付。该脚本检查：
- 文件存在且以 `\section{` 开头；
- 禁用命令为零；
- 环境 `begin/end` 配对（含 `$` 的奇偶、`\[ \]` 配对、花括号平衡）；
- 页锚覆盖该节全部印刷页且单调递增；
- 编号条目的**类型顺序**与 `sections.json` 的 `seq` 完全一致（数量、类型、先后）；
- 条目编号不被手写（不得出现 `\begin{theorem}[2.2]` 这种把号塞进可选参数的写法）。

编译自检（可选但推荐，一条命令）：
```bash
"C:/Users/admin/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/python.exe" 工程文件/tools/compile_section.py NN
```
它只在临时目录编译你这一节，报错就改，改到 0 error。**不要**在主目录反复编译 main.tex（会互相踩 aux 文件）。

交付前在你的分包内自查这张表（逐项打勾，写进 reports）：

- [ ] 段落数 = 原文段落数（粗略对：原文有几段，中文几段）
- [ ] 条目类型顺序与 `sections.json` 一致
- [ ] 每个页码都有 `\srcpage`
- [ ] 每页的公式都与 `pages/pNNN.png` 对过（尤其上标下标、花体、对偶群）
- [ ] 禁用命令 0 个
- [ ] 术语全部来自 `glossary.tsv`，没有自造
- [ ] 一句不超过 70 汉字（抽查 10 句）
- [ ] 中英之间半角空格（抽查 20 处）
- [ ] 译注 ≤6 条且格式合规

最后写 `工程文件/reports/sNN.md`（一节一份），四栏：

```markdown
# sNN 交付报告
- 范围：印刷页 X–Y（共 Z 页），段落 W 段，编号条目 V 条（类型序列 …）
- 术语新增：无 / 列出（英文 → 建议中文，依据）
- 疑点：逐条列（页码 + 原文 + 我的处理 + 为何存疑）
- 遗留：无 / 列出（如某公式图不清、某处原文疑似笔误）
```

---

## 7. 十四个常见坑（都是这本底本真会踩的）

1. `\mathcal{O}` 与 `\mathbb{O}`、`O` 三者在文本层都是 `O`，只能看图。
2. `\Bun_G` 的下标是 `G`，不是 `\check G`；对偶群只出现在 `\LocSys_{\Gd}` 一侧。
3. `G^\vee` 与 `\Gd` 是同一对象，本书统一用 `\Gd`（原文写 `\check G`）。
4. `D(Bun_G)` 与 `\D_{\qc}(\Bun_G)` 是两个不同范畴，别混；`\D_{\Nilp}` 是幂零奇异支撑子范畴。
5. `f_!` 与 `f_*`、`f^!` 与 `f^*` 在文本层常被打成 `f!`/`f∗`，必须对图。
6. `\mathbf{1}`（单位对象）与数字 1 不同；`\Delta`（对角）与 `\delta` 不同。
7. `\ell`-adic：写成 `\ell`-进（`\ell` 保留），不要写成 `l`。
8. `\overline{\Q}_\ell` → `\Ql`；`\overline{\F}_p` 照写。
9. `\mathrm{pt}`、`\Spec k`、`\mathrm{LocSys}^{\Betti}`：正体与斜体不能错（叠的名字用正体）。
10. 原文的 `—`（em dash，条目后）在中文里用 `．`？不，用 `。` 结束标题行，正文另起；即 `\begin{remark}` 后直接写正文。
11. 原文 `§2.3` 指"第 2 节第 3 条"，译作「第 2 节定理 2.3」或「定理 2.3」，视上下文。
12. Bourbaki 的 `cf.` → 参见；`e.g.` → 例如；`i.e.` → 即；`resp.` → 分别；`vice versa` → 反之亦然。
13. 脚注里的 `14` 之类原本是上标数字，译文由 LaTeX 自动编号，**不要手写**。
14. `\srcpage` 不是行间命令，插在正文流里；若一段跨页，宁可多插一个页锚，也不要漏。

---

## 8. 时间与汇报

- 分包翻译限时 **90 分钟**（主控 17:00 硬停）。
- 交付时必须：`check_sections.py NN` → OK，`reports/sNN.md` 已写，回复里给出一行结论：
  `sNN 完成：页 X–Y，条目 N 条（序列一致），check OK，疑点 k 条`。
- 做不完就如实说做到哪一页、剩下什么，**不许虚报**。宁可交部分，不可交错。
