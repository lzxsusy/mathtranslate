# 文献引用一致性审计（全部 `tex/chapters/*.tex` 正文 vs `bibliography.tex`）

## 方法与口径

1. 提取：扫描全部 19 个正文 `.tex`（`ch01-1`…`ch10-4`、`appendix`、`preface`，排除 `bibliography.tex`）中所有含 4 位年份（18xx/19xx/20xx，可带 a/b/c 后缀）的方括号内容，按 `;` 拆分多条目，并把“作者名 + `[年份]`”简写（原书大量使用，如 `A. Weil [2007]`、`D. Kazhdan and G. Lusztig [1987]`）按上下文回填作者。共得**渲染正文方括号引用 300 处**（含多条目方括号；拆分后计 key），另有 37 处在 `% [Tutor Note: ...]` 批注内，不渲染，单列）。
2. 归一化：去 LaTeX 重音命令与 Unicode 变音符、去撇号、统一连字符，从而识别 `Fe\u{\i}gin`＝`Feĭgin`、`Mirkovi\'c`＝`Mirković`、`Musta\c{t}\u{a}`＝`Mustată` 等。
3. 比对：`bibliography.tex` 共 **98 条**（与原书文献表页面 PDF p396–p401 抽出的 98 条一一对应，无缺条）。用集合差找出「引用无条目」「有条目无引用」；再逐条人工核对拼写/年份/后缀不一致。
4. 局限：① 有少量引用写作“作者名 + 括号年份”（非标准 `[作者 年份]`），已按上下文回填，若原文作者名与中文行文不符可能有 1 处归属歧义（见 §3 注）；② “从未引用”用“姓氏+年份邻近”辅以精确方括号匹配双重判定。

## 表 1　正文引用但文献表缺失

### 1a. 渲染正文（会印进书里）

| 引用串 | 位置 | 说明 / 建议 |
|---|---|---|
| `A. Weil [2007]` | `ch10-4.tex:96`（PDF p378，印刷 p.364） | 文献表**完全没有 Weil 条目**。已回看页面图像 p378：原文就印作 `[2007]`（作者 A. Weil 在正文）。疑原书漏排该条目或年份有误；建议 Lead 决定：补一条 Weil 条目，或按原书照排但加校注。**这是原书问题，非译文遗漏。** |
| `V. Ginzburg [1997]` | `ch10-3.tex:28`（PDF p348，印刷 p.334） | 文献表没有 `[Ginzburg 1997]`；只有 `[Chriss and Ginzburg 1997]`（而后者在 `ch10-1`/`ch10-3` 中已被正常引用 7 处）。图像 p348 确认原文印作 `V. Ginzburg [1997]`。疑应引 `[Chriss and Ginzburg 1997]`，或原书漏排 Ginzburg 1997 条目。 |

### 1b. 批注内引用（`% [Tutor Note: ...]`，不渲染；不影响成书，但建议统一）

| 引用串 | 位置 | 说明 |
|---|---|---|
| `Deligne and Milne 1982` | `ch01-2.tex:153`（批注） | 文献表无此条 |
| `Grothendieck–Dieudonné 1971` | `ch03-2.tex:63`（批注） | 文献表无此条；且用 en dash 连接，与文献表体例（`X and Y`）不同 |
| `Hartshorne 1977` | `ch03-2.tex:165`（批注） | 文献表无此条 |
| `Humphreys 1972` | `ch05-1.tex:30`（批注） | 文献表无此条 |
| `Milne 2017` | `ch01-2.tex:153`（批注） | 文献表只有 `[Milne 1980]`（年份不符） |
| `Kostant 1959` | `ch04.tex:331`（批注） | 文献表只有 `[Kostant 1963]`（年份不符；应为 1963） |

> 以上均为译者/校者批注中另加的“延伸文献”，因批注是 LaTeX 注释、不进入排版，故不阻塞成书；若 Lead 要求批注内引用也一律可在文献表中查到，需补 6 条或改写。

## 表 2　文献表有条目但正文从未引用

| 条目 | 说明 |
|---|---|
| `[Drinfel'd and Sokolov 1984]` | 正文 300 处渲染引用中从未出现；它只出现在文献表 `[Drinfel'd and Sokolov 1985]` 条目的说明文字里（“Translation of Russian original [Drinfel'd and Sokolov 1984]”）。正文对 Drinfeld–Sokolov 的引用一律用 **1985**（`ch04:225, ch04:473, ch08:885, ch09-1:93, preface:37`）。**原书亦如此**（1984 为俄文原版，1985 为英译；书里只引英译）。 |

其余 97 条均在渲染正文中被引用（含少量“作者 + `[年份]`”简写形式，已回填核对）。

## 表 3　年份 / 作者拼写不一致

| 类型 | 具体表现 | 位置 / 数量 |
|---|---|---|
| **Drinfeld vs Drinfel'd** | 文献表**内部**混用：`Beilinson and Drinfeld 1997/2004/2005`（无撇号）vs `Drinfel'd 1980/1983/1987/1988`、`Drinfel'd and Simpson 1995`、`Drinfel'd and Sokolov 1984/1985`（有撇号）。而**正文渲染引用一律写 `Drinfeld`（无撇号，0 处用 `Drinfel'd`）**，因此正文引 `[Drinfeld and Sokolov 1985]` 与文献表条目 `[Drinfel'd and Sokolov 1985]` 字面不一致。 | 正文 79 处 `Drinfeld`；文献表 7 条用 `Drinfel'd`、3 条用 `Drinfeld`。建议统一为 `Drinfel'd`（文献表多数）或全部 `Drinfeld`。 |
| **Feĭgin vs Feigin** | 文献表内部混用：`Fe\u{\i}gin and Frenkel 1988`、`Fe\u{\i}gin and Frenkel 1990a`（排版为 Feĭgin）vs `Feigin and Frenkel 1990b/1990c/1991/1992/1996/1999`、`Feigin et al. 1994`（Feigin）。**正文也不一致**：`ch05-1`、`ch06` 对 1988/1990a 用 `Feĭgin`（5 处），但 `ch06.tex:54,171` 又写成 `[Feigin and Frenkel 1990a]`（无 ĭ）；其余 36 处用 `Feigin`。 | 同一作者 B. L. Feigin 两种转写。GLOSSARY 固定英文为 `Feigin`；建议全书统一 `Feigin`（或统一 `Feĭgin`）。 |
| **Ginzburg 1997** | 正文 `V. Ginzburg [1997]` 与文献表 `Chriss and Ginzburg 1997` 不对应（同表 1a）。 | `ch10-3.tex:28` |
| **Kostant 1959 → 1963** | 批注写 `Kostant 1959`，文献表为 `Kostant 1963`。 | `ch04.tex:331` |
| **Milne 2017 → 1980** | 批注写 `Milne 2017`，文献表为 `Milne 1980`。 | `ch01-2.tex:153` |
| **Frenkel–Ben-Zvi 2004** | 批注用 en dash `Frenkel–Ben-Zvi 2004`，文献表为 `Frenkel and Ben-Zvi 2004`（写法不同、实为同一条）。 | `ch03-1.tex:247,283,344` |
| 年份后缀 a/b/c | 抽查全部带后缀引用（如 `Frenkel and Gaitsgory 2006a/b/c`、`Frenkel 2005a/b`、`Feigin and Frenkel 1990a/b/c`），除上面 Feĭgin/Feigin 的转写问题外，**年份后缀本身与文献表一一对应，无错配**。 | — |

### 补充观察（非错误）

- 原书的引用体例本就不统一：既有标准 `[Frenkel and Gaitsgory 2006c]`，也有“作者名 + `[年份]`”（如 `A. Weil [2007]`、`D. Kazhdan and G. Lusztig [1987]`、`T. Hayashi [1988]`、`G. Lusztig [1998]`），还有不用方括号的括注（如 `（Drinfeld 1980; Drinfeld 1983; Drinfeld 1987; Drinfeld 1988）`，`ch01-1.tex:240`）。译文均按原样保留；本次审计已把这些形式都回填核对。
- 文献表条数（98）与原书文献表页（PDF p396–p401）完全一致，未发现漏排/多排条目。
- 两处“有引用无条目”（Weil 2007、Ginzburg 1997）经核对**页面图像确认原书即如此**，不是翻译或转写造成。

## 结论

1. **渲染正文的引用完整度**：300 处引用中，仅 **2 处**找不到文献表条目（Weil `[2007]`、Ginzburg `[1997]`），且都是**原书自身问题**（已用页面图像核实），建议 Lead 在校注或文献表中处理；其余全部可对应。
2. **文献表覆盖**：98 条中 **97 条被正文引用**，仅 `[Drinfel'd and Sokolov 1984]` 未被正文引用（原书亦如此，属俄文原版条目）。
3. **拼写/年份不一致**：主要问题是 **Drinfeld vs Drinfel'd**（正文全无撇号、文献表 7 条有撇号）与 **Feĭgin vs Feigin**（文献表内部及正文内部都混用）；其余为批注内的 3 处年份/写法问题。建议在最终合成前统一（尤其 Drinfeld 与 Feigin 两种，影响全书的视觉一致性）。
4. 本次审计**未修改任何 `.tex` 文件**，仅新增本报告。
