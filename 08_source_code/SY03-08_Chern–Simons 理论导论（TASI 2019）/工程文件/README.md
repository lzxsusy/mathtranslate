# Chern-Simons 理论导论 —— TASI 2019 讲义中译本（LaTeX 工程）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：全库统一 CC BY 4.0，明确欢迎用于训练、蒸馏与商用（署名即可）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

原文：**Gregory W. Moore, _Introduction To Chern-Simons Theories_**, TASI 2019 暑期学校讲义
（249 页 PDF，MiKTeX/pdfTeX 排版，2019-06-07 版；原文件 `TASI-ChernSimons-StudentNotes(3)(1)(1).pdf`）。

本工程是该讲义**逐页对照的中文 LaTeX 译本**，附公式级校对、图表裁剪与学术批注。

---

## 一、编译

本工程**已实际编译通过**：`main.pdf`，**234 页，0 error，0 缺字**（`main.log` 无 `Missing character`、无 undefined reference、无 multiply-defined label）。

编译引擎用 **LuaLaTeX**：

```bash
lualatex main
lualatex main          # 第二遍：目录、交叉引用
lualatex main          # 第三遍：确保 \eqref / \ref 与目录页码全部收敛
```

> **为什么不用 XeLaTeX**：这台机器上 XeTeX 的 PDF 驱动 `xdvipdfmx` 会崩溃（`Error -1073740777 (driver return code) generating output`，`main.pdf` 变 0 字节），TeX 层本身无错。换成 LuaLaTeX 后一次通过，中文（`ctex` 默认 Windows 字体集，SimSun）与 1136 个 `\tag` 公式编号都正常。
>
> 若你本机 XeLaTeX 正常，也可以直接用 `xelatex main` 跑三遍——源码本身与引擎无关（未用任何 XeTeX/LuaTeX 专有命令）。

依赖宏包：`ctex, amsmath, amssymb, amsthm, mathtools, bm, graphicx, geometry, xcolor, enumitem, booktabs, array, hyperref`（TeX Live 标准发行版自带）。

## 二、目录结构

```
main.tex                 主文件：preamble、标题页、译者说明、目录、\input 全部片段、文献
chunks/
  c01.tex … c29.tex      正文片段（按原文页码顺序，每片段 7–13 页原文）
  c-refs.tex             参考文献 [1]–[72]（保留英文原貌）
figures/
  fig01.png … fig40.png  原 PDF 中裁出的 40 张图表（300 dpi PNG）
TRANSLATION_SPEC.md      翻译与排版规范（术语表、公式 \tag 规则、批注格式等）
审校批注.md              源码中 % [Tutor Note: ...] 的汇总（便于阅读，不参与排版）
work/                    工程中间产物：页面位图、文本层转储、结构地图、校验脚本
```

## 三、约定（阅读与修改前必看）

1. **公式编号与原文完全一致**：每个带编号公式用 `\tag{原编号}` 锁定，例如

   ```latex
   \begin{equation}
     \delta \mathrm{cs}(A) = 2\,\mathrm{tr}(\delta A\,F) - d\,\mathrm{tr}(A\,\delta A)
     \tag{1.6}
     \label{eq:1.6}
   \end{equation}
   ```

   因此正文里的 `\eqref{eq:1.6}` 渲染出来就是 **(1.6)**，可直接与原 PDF 对照核查，不受译文增删影响。
2. **图号与原文一致**：原文 Figure 1–40 全部收入、顺序未变，LaTeX 自动编号即为原图号；每张图的 caption 末尾注明「（原文 Fig.~N，第 X 页）」。
3. **章节编号与原文一致**：`1.`/`A.` → `\section`，`2.1`/`A.1` → `\subsection`，`2.2.7`/`I.7.1` → `\subsubsection`；编号由 LaTeX 自动生成，未手打。
4. **译者添加、非原文内容**（三处，均可一键删除）：
   - 每节开头的 `keytakeaways` 环境（「本节重点」）；
   - 源码中的 `% [Tutor Note: ...]` 注释（不进入排版，汇总见 `审校批注.md`）；
   - 标题页/译者说明。
5. **原文的编辑性标记照原样保留**：作者在稿件中留下的 `****`、`♣…♣`、`NEED TO COMMENT ON …`、`[1988 ??]` 等，译文中显示为小号斜体「［原文标记：…］」，并加注释说明。未作删改，以保持原稿状态。
6. **术语**：按中文学界通行译法，首次出现括注英文（Gauge theory 规范场论、Holonomy 和乐、Anomaly 反常、Moduli space 模空间、Framing anomaly 标架反常……完整词表见 `TRANSLATION_SPEC.md` §9）。
7. **文献**：正文沿用原文方括号编号 `[15]`，对应 `chunks/c-refs.tex` 中的 [15]（条目保留英文原貌，未翻译）。

## 四、译文与原文的对应关系

| 片段 | 原印刷页 | 覆盖章节 | 图 |
|---|---|---|---|
| c01 | 5–13 | §1–2.1.1 | Fig.1 |
| c02 | 14–21 | §2.1.2–2.2.2 | — |
| c03 | 22–30 | §2.2.3–2.2.6 | — |
| c04 | 31–38 | §2.2.7 | Fig.2、Fig.3 |
| c05 | 39–46 | §2.2.8–2.2.9 | — |
| c06 | 47–54 | §2.2.10–2.2.11 | Fig.4 |
| c07 | 55–63 | §2.2.12–2.2.15 | Fig.5、Fig.6 |
| c08 | 64–71 | §2.2.16–2.2.18 | Fig.7、Fig.8、Fig.9 |
| c09 | 72–78 | §2.3–2.4 | Fig.10 |
| c10 | 79–87 | §2.4.1–3.1 | — |
| c11 | 88–95 | §3.1.1–3.3 | — |
| c12 | 96–106 | §3.3.2–4.1.1 | Fig.11、Fig.12 |
| c13 | 107–113 | §4.1.2–4.2 | — |
| c14 | 114–126 | §4.2.1–4.5.1 | Fig.13、Fig.14、Fig.15、Fig.16 |
| c15 | 127–134 | §4.5.2–4.6 | Fig.17、Fig.18 |
| c16 | 135–141 | §4.7–4.8 | Fig.19 |
| c17 | 142–148 | §4.8.1–5.1 | Fig.20、Fig.21、Fig.22 |
| c18 | 149–155 | §5.1.1–5.2.1 | Fig.23、Fig.24、Fig.25、Fig.26、Fig.27 |
| c19 | 156–164 | §5.2.2–10.1 | Fig.28、Fig.29、Fig.30、Fig.31 |
| c20 | 165–165 | §11–11.4 | — |
| c21 | 166–171 | §A–B.1 | — |
| c22 | 172–181 | §B.2–B.3 | Fig.32 |
| c23 | 182–191 | §D–E.5 | — |
| c24 | 192–199 | §E.6–G.1 | Fig.33、Fig.34 |
| c25 | 200–210 | §G.2–H | Fig.35、Fig.36 |
| c26 | 211–222 | §I–I.7 | Fig.37、Fig.38 |
| c27 | 223–235 | §I.7.1–K | — |
| c28 | 236–242 | §K.1–L.1 | Fig.39 |
| c29 | 243–244 | §L.4–M | Fig.40 |
| c-refs | 244–248 | 参考文献 [1]–[72] | — |

## 五、已知问题与建议复核点

### 5.1 原 PDF 有 9 张图是空白占位框（重要）

原 PDF 里下列图的**图注存在、图形内容缺失**（页面上是纯白空白，作者显然留了位置但没插入图形）。译本不插入空白图片，改用占位框 `\MissingFigureNote` 并保留图号与图注，以免后文图号错位：

| 图号 | 原印刷页 | 原图注（节录） |
|---|---|---|
| Fig. 11 | 103 | Two slightly different $(2n+1)$-chains $B,B'$ in $G$ bounding the same $2n$-cycle |
| Fig. 12 | 103 | Two different $(2n+1)$-chains in $G$ bounding the same $2n$-cycle |
| Fig. 13 | 119 | Feynman graphs in the expansion of $\Gamma(A^-)$ in a power series in $A^-$ |
| Fig. 14 | 119 | Momentum $q$ flows into the two-point graph |
| Fig. 15 | 125 | Schematic drawing of points with nonzero multiplicity in the highest weight representation |
| Fig. 16 | 125 | Degeneracies of \ldots（图注在原 PDF 中被截断） |
| Fig. 18 | 134 | Identifications in the $z=\sigma+it$ plane induced by taking a trace |
| Fig. 37 | 220 | A triangle of connections in $\mathcal{A}(P)$ |
| Fig. 38 | 221 | Triangle of connections in $\mathcal{A}(P)$ used to compute the gauge-dependence |

对应的空白裁切文件留在 `work/missing_figures/`（未删，供核对）。其余 31 张图均已按 300 dpi 裁出并插入原位。

### 5.2 其他

- 原稿是**未完成稿**：§6–§11 多为提纲式的一两句话；多处 `Appendix ****`、`****`、`♣…♣`、`NEED TO COMMENT ON …` 是作者留给自己的编辑标记。译本一律以小号斜体「［原文标记：…］」原样保留并加批注，**未代作者补写任何内容**。
- 原稿笔误照原文转写并加 `[Tutor Note]`，例如：p.12–13 脚注把作用量编号写成 (2.31)（实为 (2.1)）；p.45 (2.176) 指数多一个 $i$；p.179 (K.52) 漏 $\\oplus$；p.195 (E.65) 下标 $s_I$ 应为 $s_J$；p.242 $\\operatorname{DET}V_1<本地路径> 的箭头疑为 $\\otimes$。全部清单见 `审校批注.md` 中标 **[文本]** 的条目。
- 原文第 5–6 页的目录是作者手工排的，译本改用 `\\tableofcontents` 自动生成，条目结构相同（含附录 A–M）；原目录里已被作者省略的条目（如附录 C、G、L 部分小节）在自动目录中会完整出现。
- 少数页面的字体级细节（如虚数单位用直立体 `\\mathrm{i}`、`cs(A)` 用斜体 `$cs$`）是逐页放大核对后的判断，见各片段 `[Tutor Note]`。
- 个别地方原文只有标题、没有正文（如附录 E.8），译本以「［本节在原稿中仅有标题，正文尚未写出。］」占位，并加批注。

## 六、实际编译结果与机器校验

**编译结果：`main.pdf`，234 页，0 error，0 缺字，0 悬空引用，0 重复 label**（`main.log`）。用了 3 遍 LuaLaTeX：第 1 遍后补两处 `enumitem` 选项语法（`[(a)]` → `[label=(\alph*)]`），并把正文里的 `♣ ✱ ∼` 换成 `$\clubsuit$ / $\ast$ / $\sim$`（Latin 字体无这些字形），此后 3 遍全绿。图 1 等 31 张插图、9 个「原图缺失」占位框、161 条 PDF 书签均正常。

| 检查项 | 结果 |
|---|---|
| 实际编译 | ✅ 234 页，exit 0 |
| `Missing character` / 缺字 | 0 |
| undefined reference / multiply defined label | 0 |
| Overfull/Underfull box | 32 处（均为轻微，最长 17 pt，不影响阅读） |
| 片段文件齐全（c01–c29 + c-refs） | 30/30 |
| 花括号配平 / `\begin`–`\end` 配平 | 全部通过 |
| 数学模式内混入中文全角字符 | 0 处 |
| 带编号公式 | 1136 个 `\tag`（`equation` 环境 1127 个 + `align`/`gather` 内多行编号 9 个）；另有 11 条无编号 `equation*` |
| 公式编号与原文逐页核对（`\tag` 与原 PDF 文本层比对） | 1136/1136 全部命中，0 条对不上 |
| 公式编号连续性（按章：1、2、3、4、E、F、G、H、I、J、K、L） | 无缺号 |
| 章节标题层级 vs 原文编号点数 | 0 处错级（初检发现 c05、c14 共 7 处，已修正） |
| 章节标题序列 vs 原文 TOC/正文 | 无缺标题、无多余编号标题 |
| 图号 1–40 连续、每图只出现一次 | 40 个 float，31 个 `\includegraphics` + 9 个占位框 |
| 使用到的宏包/环境是否都在主文件 preamble 内 | 全部标准环境（`equation/align/gathered/split/cases/pmatrix/array/tabular/figure/...`），无 tikz、无未定义宏包 |
| `% [Tutor Note: …]` 批注条数 | 238 条，已汇总到 `审校批注.md` |
| 「本节重点」 | 27 处（24 个 `\section` + 3 处重点小节） |
| PDF 书签（hyperref） | 161 条，章节层级正确 |

**剩下可挑的问题**：32 处轻微 overfull box（长公式/长 URL 顶到边距），如需精修可对相应行加 `\raggedright` 或手动断行——不影响阅读，未改。

