# TASK-translator · SY02-46 译手契约（主控制定，逐条强制）

> 本文件是译手 subagent 的唯一施工契约。凡与本文件冲突的「我觉得更好」一律无效。
> 主控（lead）保留术语裁定权与合并权；译手**不得**修改 `源码/preamble.tex`、
> `源码/main.tex`、`工程文件/work/glossary.tsv`、`工程文件/work/sections.json`、
> `工程文件/STYLE_GUIDE.md` 以及别人的 `sections/*.tex`。

---

## 0. 工程坐标

- 仓库根：`C:\Users\admin\Desktop\数译发布\gitee_shuyi`
- 工程根：`08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应`
- 底本：Gérard Laumon, *Travaux de Frenkel, Gaitsgory et Vilonen sur la correspondance
  de Drinfeld–Langlands*, Séminaire BOURBAKI 54e année (2001–2002), n° 906, Juin 2002。
  **印刷页 = PDF 页**（页眉 `906–NN`，NN 即印刷页号）。
- 逐页文本：`工程文件/work/src/pNN.txt`（NN=01..19，已做 Unicode NFC 规范化）
- 页面图（**核对公式的唯一权威**）：`工程文件/work/pages/pNNN.png`（150 dpi，NNN 三位）
- 节清单与条目序列：`工程文件/work/sections.json`
- 术语冻结表：`工程文件/work/glossary.tsv`（法文 / 中文 / 依据 / 首现页 / 备注）
- 通读笔记：`工程文件/work/通读笔记.md`；疑点清单：`工程文件/work/疑点清单.md`
- 输出：`源码/sections/sNN-<slug>.tex`
- 自检：`工程文件/tools/check_sections.py`；单节编译：`工程文件/tools/compile_section.py`

Python：
`C:/Users/admin/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/python.exe`
xelatex：`C:/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe`

**分包**（一个译手只做自己那一行）：

| 译手 | 文件 | 范围 | 页 |
| --- | --- | --- | --- |
| t01 | `s00-intro.tex` + `s01-prelim.tex` | 引言 + §0 预备 | 1–4 |
| t02 | `s02-classfield.tex` | §1 几何类域论 | 4–6 |
| t03 | `s03-main.tex` + `s04-perverse.tex` | §2 主定理 + §3 反常层 | 6–9 |
| t04 | `s05-autprime.tex` | §4 复形 Aut′ | 9–11 |
| t05 | `s06-fourier.tex` | §5 Fourier 构造 | 11–13 |
| t06 | `s07-vanishing.tex` | §6 消没定理 | 13–15 |
| t07 | `s08-descente.tex` + `s09-refs.tex` | §7 下降 + 参考文献 | 15–19 |

---

## 1. 开工必读（按顺序，读完再动笔）

1. `工程文件/work/通读笔记.md` 的你那几节（了解该节在全篇论证中的位置）；
2. `工程文件/work/glossary.tsv`（全文，冻结；改词只有主控能做）；
3. `工程文件/STYLE_GUIDE.md`（文风条款）；
4. `源码/preamble.tex`（宏清单，写公式前必须看一遍）；
5. 你分包范围内的 `工程文件/work/src/pNN.txt`。

---

## 2. 逐页工作流（不许跳步）

对每一页 NN：

1. 读 `src/pNN.txt`，理解该页在说什么；
2. 打开 `pages/pNNN.png` **看图**，逐个核对：上标下标、$\vee$ 的位置、$\mathcal$ 与
   $\mathbb$、`Aut′` 的撇、`E (d)` 与 `E^{(d)}`、`LdE` 与 `L^d_E`、`Dcb` 与 `D^b_c`、
   `Qℓ` 与 `\Ql`、`Ω1X` 与 `\OmX`、`Fibn′ n(n−1)(g−1)` 与
   `\Fib'^{n(n-1)(g-1)}_n`、`U n` 的下划线、`∧i L` 与 `\bigwedge^i L`、`!` 与 `*`；
3. 落笔写中文。**每一页开始前**先写页锚（见 §4.1）；
4. 写完该页再回头对一次图，确认没有把 $\mathcal{O}$ 写成 $O$、把 $\vee$ 写成 $*$。

**文本层已知坏点（必须靠图还原）**：
- `LdE` → `L^d_E`；`E (d)` → `E^{(d)}`；`Aut′E` → `\Aut'_E`；`Fibn′` → `\Fib'_n`；
- `Dcb` → `\Dbc`；`Cohd0` → `\Coh^d_0`；`Moddi` → `\Mod^d_i`；`V ∨` → `V^\vee`；
- `φ (d)` → `\varphi^{(d)}`（原文用 $\phi$ 或 $\varphi$ 以图为准）；
- `Vi L`（p16）→ `\bigwedge^i L`；`Symdx` → `\Sym^{d_x}`；
- `∧`、`⊗`、`−` 在文本层常错位，一切以页面图为准。

---

## 3. 语言纪律

1. **一句 ≤60–70 汉字**。超过就断句，断在逻辑接点，不要断在「的」字后面。
2. 中文与拉丁字母/数字之间**一个半角空格**：`秩 n 向量丛`、`第 2 节`、`G-丛`。
3. **全角标点**：，。；：？！（）「」；公式内逗号、括号用半角。
4. 逻辑连接词逐一对应（见 STYLE_GUIDE §2）；**原文没连接词，中文不许加**。
5. 禁「被……所……」「进行……的讨论」「对……进行刻画」；「其中」不要滥用。
6. 人名、定理名、期刊名不译：Laumon、Langlands、Drinfeld、Frenkel、Gaitsgory、Vilonen、
   Beilinson、Braverman、Lysenko、Lafforgue、Deligne、Serre、Grothendieck、Shintani、
   Plücker、Radon、Fourier、Jacobian（雅可比）、Picard、Hecke、Riemann、Bernstein–Luntz、
   Brylinski、Illusie、BBD、Zariski、étale（保留）。
7. 参考文献节保留原文不动，仅把 `BIBLIOGRAPHIE` 译为「参考文献」，`et` 等连接词也不译。

---

## 4. LaTeX 体例

### 4.1 页锚与节标题

```latex
\section{几何类域论}\srcpage{4}
```

- 每个 `\section{中文标题}` 后紧跟 `\srcpage{N}`（该节起始印刷页）。
- 之后**每换一页**（含跨页段落！）在正文中插入 `\srcpage{N}`；必须精确。
- 页锚不得插在 `$...$` 内部或命令参数里。
- §0 用 `\section*{0.\ 预备}` + `\addcontentsline{toc}{section}{0.\ 预备}`（见 s01 模板）。
- 参考文献用 `\section*{参考文献}\srcpage{18}`。

### 4.2 编号条目（**编号零手写**）

原文 `THÉORÈME 2.2. — 正文` 译成环境，按出现顺序排，编号由计数器自动生成：

| 原文 | 环境 |
| --- | --- |
| THÉORÈME / Théorème | `theorem` |
| DÉFINITION / Définition | `definition` |
| LEMME / Lemme | `lemma` |
| PROPOSITION | `proposition` |
| COROLLAIRE | `corollary` |
| Remarque 6.2 : | `remark`（原文此处用冒号，不用破折号，照译） |

- 可选参数放原名：`\begin{theorem}[Abel--Jacobi]`、`\begin{lemma}[Deligne, {[Il]} 推论 2.10]`。
- **§0 特例**：原文编号为 `(0.2)`, `(0.3)`, `(0.4)`，用不编号环境 + 可选参数：
  `\begin{definitionZ}[(0.2)]`、`\begin{lemmaZ}[(0.3)]`。这是唯一允许在可选参数里
  出现数字的情形。
- 公式 `(0.1)`、`(1.3)` 用
  `\[ \tag*{(0.1)} ... \]`；`(1.3)` 同理。**不要**用 `equation` 环境（会与条目编号冲突）。
- 引用公式写「由 (0.1)」「由公式 (1.3)」。

### 4.3 禁用命令（零容忍）

`\ref`、`\eqref`、`\label`、`\cite`、`\pageref`、`\autoref`、`\nocite`、`\bibliography`。
- 交叉引用一律写文字：`Theorem 2.2` → 「定理 2.2」；`§5` → 「第 5 节」；`(1.3)` → 「(1.3)」；
  `loc. cit.` → 「同上」。
- 行间公式不编号（除 (0.1)、(1.3) 用 `\tag*`）。
- `\begin{aligned}` 放在 `\[ … \]` 内。

### 4.4 可用宏（不要新增同名宏）

```latex
\Fib \Coh \Mod \Perv \Pic \Jac \Four \Rad \Hck \Aut \Sym \Ext \Hom \Spec \Det
\id \pt \rss \Bun \Rep \LocSys \tr \op \der
\Db \Dbc
\cA … \cZ        % 花体
\Z \Q \R \C \F \A \Gm \Ql
\OmX \Dmod \dR \et \Betti \lisse \irred \Pv \GG
\srcpage{} \yizhu{}{} \refitem{}{} \dsp
```

用法示例：`\Fib_n(X)`、`\Fib'_n(X)`、`\Fib_n^d(X)`、`\Coh^d_0(X)`、`\Mod^d_i(X)`、
`\Perv(S)`、`\Four_{V/S}`、`\Rad_{\Pv(V)/S}`、`\Hck_n(X)`、`\Aut_E`、`\Aut'_E`、
`\Ext^1_{\cO_X}(\OmX^{\otimes i-1}, M_i)`、`\Dbc(S)`、`\cO_X`、`\Gm`、`\Ql`、`\Pv(V)`、
`\bigwedge^i L`、`\underline{\cU}_n`。

确缺宏时：在自己文件顶部用一行 `\providecommand{\xxx}{...}` 并在报告里登记。

### 4.5 译注

格式 `\yizhu{内容}{等级（出处）}`，只许三类：术语背景 / 原文省略 / 原文笔误。
- 每条必须带等级与出处（A/B/I 或「上下文推断，无外部依据」）。
- 严禁在正文写「作者大概是说」「此处应为」而不进译注；严禁用译注补写原文没有的数学。
- 每节 ≤6 条，宁少勿滥。已知该加译注的点见 `work/疑点清单.md`。

---

## 5. 数学内容纪律

1. **照译**：原文含糊就照译 + 译注；原文错误照译 + 译注；原文省略就省略，不补。
2. **不合并、不拆分段落**：原文一段 = 中文一段。
3. **不美化**：不加原文没有的「显然」「容易看出」。
4. 定理条件一个字不能丢（`g ≥ 2`、`n ≥ 2`、`d ≥ 0`、`d > in(2g−2)` 等）。
5. 引用他人结果保留「（作者，[编号] 定理号）」结构。

---

## 6. 自检与交付

每写完一节立刻跑：

```bash
cd "C:/Users/admin/Desktop/数译发布/gitee_shuyi/08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应"
"C:/Users/admin/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/python.exe" 工程文件/tools/check_sections.py NN
```

必须看到 `OK` 才能交付。它检查：文件存在且以 `\section{` 开头；禁用命令为零；
环境配对；花括号与 `$` 平衡；页锚覆盖该节全部页且单调；条目类型顺序与 `sections.json`
一致；不手写编号（§0 例外）。

编译自检：

```bash
"C:/Users/admin/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/python.exe" 工程文件/tools/compile_section.py NN
```

必须 0 error。**不要**在主目录反复编译 main.tex（会互相踩 aux）。

交付前自查：

- [ ] 段落数 = 原文段落数
- [ ] 条目类型顺序与 `sections.json` 一致
- [ ] 每个页码都有 `\srcpage`
- [ ] 每页公式都与 `pages/pNNN.png` 对过
- [ ] 禁用命令 0 个
- [ ] 术语全部来自 `glossary.tsv`
- [ ] 一句不超过 70 汉字（抽查 10 句）
- [ ] 中英之间半角空格（抽查 20 处）
- [ ] 译注 ≤6 条且格式合规

最后写 `工程文件/reports/sNN.md`，四栏：

```markdown
# sNN 交付报告
- 范围：印刷页 X–Y（共 Z 页），段落 W 段，编号条目 V 条（类型序列 …）
- 术语新增：无 / 列出（法文 → 建议中文，依据）
- 疑点：逐条列（页码 + 原文 + 我的处理 + 为何存疑）
- 遗留：无 / 列出
```

---

## 7. 常见坑（这本底本真会踩）

1. `Aut'_E` 的撇：`\Aut'_E` 会报错，用 `\Aut'{}_E` 或 `{\Aut}'_E`。
2. `V^\vee` 不是 `V^*`；`(p^\vee)_!` 的 `!` 是下叹号。
3. `\Fib'^{n(n-1)(g-1)}_n(X)` 的上下标顺序：先撇，再上标，再下标。
4. §0 用不编号环境；若用 `definition` 环境会把编号算成 1，全篇编号崩。
5. `\tag*{(0.1)}` 只能在 `\[ ... \]` 里用，不能在 `$...$` 里。
6. 页锚 `\srcpage` 是 `\marginpar`，不能写进 `$...$`。
7. 原文 `Remarque 6.2 :` 用冒号，译成「注 6.2：」，不要改成破折号。
8. 参考文献 `[B-L]` 的年份 `(1974)` 照录，不改（主控负责在资料卡记疑）。
9. 法文 `no 906` 的 `no` 是 numero，译「第 906 期」，不是 «n°» 的排版问题。
10. `54ème` 原文用 `ème`，译文统一「第 54 年」。
11. `faisceau pervers ponctuel` 不是「点状层」，是「点状反常层」。
12. `à homothétie près` = 「模数乘」，不要译成「相差一个数乘」这种啰嗦说法（首现可括注）。
13. `gros ouvert` = 「大的开集」，不要译「胖开集」。
14. `en deux temps` = 「分两步」，不是「两次」。
