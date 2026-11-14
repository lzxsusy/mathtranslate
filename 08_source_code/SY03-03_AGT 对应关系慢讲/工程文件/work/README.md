# 《AGT 对应关系慢讲》(A Slow Review of the AGT Correspondence) 中文译注本

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 为准：语料 / 轨迹 / 会话 CC BY 4.0，明确欢迎用于训练与蒸馏（译文与工程文档 CC BY-NC-SA 4.0）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

**底本**：Bruno Le Floch, *A Slow Review of the AGT Correspondence*,
arXiv:2006.14025v3 [hep-th], 6 Apr 2022；2022 年 1 月定稿，系作者在冬季学校 “YRISW 2020”
所作讲座的扩展写本（拟发表于 J. Phys. A 专刊）。
原文 PDF 共 **136 页**：正文 pp.1–106，参考文献 pp.106–136（共 **1309** 条）。

**本译本**：正文 pp.1–106 全译（中文 LaTeX 重排 + 174 条编号公式逐符号对照原文图像转写 +
156 条学术批注），参考文献保留英文原貌并自动转录收录。成品 131 页。

> 本译本仅供个人学习与研究使用，不作商业传播。原文版权归作者所有。

---

## 1. 页码映射（重要）

| 项目 | 说明 |
|---|---|
| 原 PDF 页号 | = 原文印刷页码（**偏移 0**） |
| 译本页码 | 与原文**不一一对应**（中文排版密度不同） |
| 源码中的定位注释 | 每个原文页起始处有 `% [原文 p.N]`；每个片段开头有 `% ===== 原文 pp.X–Y =====` |
| 公式编号 | 与原文**完全一致**，可据式号直接对照原文 |

## 2. 结构清单

- 摘要、译者说明、目录
- §1 引言与纲要（1.1 class S 理论 / 1.2 基本 AGT 对应 / 1.3 既有综述）
- **第一篇 class S 理论**：§2 ADE 型 6d (2,0) SCFT（2.1–2.4）、§3 由 6d 得到 class S 理论（3.1–3.4）、
  §4 class S 理论的拉格朗日量（4.1–4.4）
- **第二篇 AGT 对应**：§5 4d 箭图的局域化（5.1–5.4）、§6 SU(2) 箭图的 AGT 对应（6.1–6.3）
- **第三篇 AGT 的推广**：§7 一般 class S 理论（7.1–7.3）、§8 各种维数的算子（8.1–8.4）、
  §9 其他几何（9.1–9.4）、§10 结论、致谢、缩写表、附录 A 特殊函数
- 参考文献（英文原貌，1309 条）

## 3. 编译方法

```powershell
# 工作区：work/src/  （main.tex 为汇总文件）
powershell -ExecutionPolicy Bypass -File build.ps1
```

- 引擎：**LuaLaTeX**（TeX Live 2026，`ctex` 宏包；本机 xdvipdfmx 不稳定，故不用 XeLaTeX）。
  需编译 3 遍（目录/交叉引用）。
- 字体：`ctex` 在 Windows 下自动使用系统字体（宋体/黑体等），无需手工配置 fontconfig。
- **本机两个坑（已写进 build.ps1）**：
  1. **lualatex 在非 ASCII 路径下无法写 `.log`**（中文目录会报 `I can't write on file main.log`）；
  2. 子进程不能写 Desktop（同样报 `I can't write on file`）。
     故 build.ps1 先把 `src/` 与 `figures/` 镜像到 `<本地路径>`
     再编译，最后把 `main.pdf` 拷回 `src/`。在别的机器上可直接 `lualatex main.tex` ×3。
- 依赖宏包：amsmath, amssymb, amsthm, mathtools, bm, graphicx, xcolor, enumitem, booktabs, array,
  multirow, longtable, multicol, fancyhdr, caption, tcolorbox, tikz, hyperref（均为 TeX Live 标准包）。

## 4. 译校体例

1. **公式**：174 条编号公式与原文一一对应（`\tag{}` 手工锁定；其中式 (1.2)、(1.6) 为“图形化公式”，
   由原图截取，编号随原图或手工 `\tag`）；原文中大量**无编号公式**照原样不编号。
   正文引用公式用纯文本“式 (3.13)”。
2. **图**：原文 5 张图（Figure 1–5）与图形化公式均按原 PDF 矢量图 400–500 dpi 截取重排；图注照译。
   原文**无任何位图**，全部为矢量绘制。
3. **表**：原文有 Table 1（p.10）、Table 2（p.13）、Table 3（p.61）与缩写表（p.105），均按原内容重排为中文表。
4. **要点框**：原文每节开头的灰底框（部分无标题条）是原文内容，以 `keybox`/`keyboxplain` 环境照译。
5. **强调**：原文斜体强调在中文里统一用粗体表示（中文字体无真斜体）。
6. **批注**：`% [Tutor Note: …]` 为译者批注，编译后不进入排版，仅供读源码时阅读；
   全部 156 条汇总见《译注汇总.md》。批注内容限定为：可验证的易错点、补出的省略论证、原文笔误订正。
7. **参考文献**：不翻译（学术惯例），由原文 PDF 文字层自动转录，见 §6 限制说明。
8. **术语**：以中文学界通行译法为准，人名/模型名/缩写（AGT、class S、CFT、SYM、SQCD 等）保留英文。

## 5. 原文笔误与可疑之处登记表

> 原则：**正文一律照原文排印**，笔误只在批注中指出并给出正确形式（SOP 铁律 R3）。
> 下表为全部已发现项，便于读者对照原文核查。

| # | 原文页 | 原文 | 说明 / 正确形式 |
|---|---|---|---|
| 1 | p.6 | `e6 ⊃ su(3)^3` | **不是笔误**：T_su(3) 三个穿刺各带 su(3)，SU(3)³ 是 E6 极大子群（秩 6=3×2） |
| 2 | p.14 | `adds k! ∂_[α1 Λ_{α2…αk}]` | 系数应为 `k`（k≤2 时 k!=k 巧合相同，k≥3 才暴露），见批注 |
| 3 | p.21 | `ε^{μν} = δ^μ_4 δ^ν_5 − δ^ν_5 δ^μ_4` | 两项相同故恒为零；正确应为 `δ^μ_4 δ^ν_5 − δ^μ_5 δ^ν_4` |
| 4 | p.24 | `transformaions` | 拼写：transformations |
| 5 | p.25 脚注 27 | `…a holomorphic cycle inside Q` | 记号 `Q` 全文未定义（疑为省写），照译并批注 |
| 6 | p.28 | `θ = Im log|q|` | 应为 `θ = Im log q`（`log|q|` 为实数，Im≡0），见批注反解 |
| 7 | p.30 | `quivers gauge theories` | 应为 `quiver gauge theories` |
| 8 | p.33 / p.36 | `six/eight point on Σ` | 应为 `points`（数值 6=3×2、8=4×2 均正确） |
| 9 | p.38 | `renormalization scheme` | 应为 `schemes` |
| 10 | p.40 | 习题 4.11 小问编号 `1. 2. 2. 3.` | 小问编号重复 2.、末问错成 3.；译文按内容排 1.–4. |
| 11 | p.43 | `accomodate` / p.47 `sucessfully` | 拼写 |
| 12 | p.44 | `su*(4|2)` 而 (5.2) 写 `su*(2|4)` | 指标顺序自相矛盾，两种约定并存，见批注 |
| 13 | p.54 | `Many 4d N=2 Lagrangian theory` | 应为 `theories` |
| 14 | p.55 | 脚注 46 “References welcome…” | 作者自己的求文献留言，照译保留 |
| 15 | p.69 | `b=√(q̃/q)` 与 (6.20) 反解 | 参数化约定差异（不同文献 s、b、q̃/q 约定不同），见批注 |
| 16 | p.77 | 质量参数 `n_1+⋯+n_{ℓ-1}=N_1−1` | 疑应为 `n_1+⋯+n_ℓ−1`（Y=1^N 时原文写法给 0，应为 N−1） |
| 17 | p.81 | `corespondence` | 拼写：correspondence |
| 18 | p.84 | `two fixed point of an U(1) isometry` | 应为 `points`、`a U(1)` |
| 19 | p.91 | `a Riemann surface with punctures which extra data D` | 应为 `with` |
| 20 | p.92 / p.102 | `envelopping` | 拼写：enveloping |
| 21 | p.93 | `the two fixed point of the supercharge squared` | 应为 `points` |
| 22 | p.94 | `it is an renormalization group flow invariant` | 应为 `a` |
| 23 | p.98 | `dimensional oxydation` | 旧拼法（oxidation），照译保留 |
| 24 | p.100 | `developped` | 拼写：developed |
| 25 | p.101 | `Ÿ_{q_1,q_2,q_3}` 与该条定义的 `h_1,h_2,h_3` | 原文 q/h 两种参数化混用，照抄并批注 |
| 26 | p.102 | `I do not know if there is are analogues` | 应为 `are`（或 `is`） |
| 27 | p.102 | `Skylanin algebra` | 应为 Sklyanin |
| 28 | p.104 | `dimensionally reduction` | 应为 `dimensional reduction` |

## 6. 已知偏差与限制（不静默降级，如实声明）

1. **参考文献为自动转录**：1309 条由原文 PDF 文字层脚本转录并重排为双栏，**未逐条人工校对**；
   文字层会把标题中的数学拍平（例如 `C²/Z_p` 记为 `C2/Zp`、上下标丢失），仅作检索/定位用，细节以原文为准。
2. **图形化公式**：(1.2) 为原图直接截取（编号在图中）；(5.37)、(5.39) 亦为原图截取。
   其余示意图（3.17、3.18、3.24、4.9、4.11、4.16、4.21–4.23、4.26、4.28、5.31、7.8、7.15、8.8、8.10 等）
   为 **TikZ 重画**，节点/连线/标签照原图，但线条细节不可能与原矢量图逐像素相同。
3. **目录**：译本目录只收 section/subsection 级；原文目录中的 “Acknowledgments / Table of acronyms” 未列入目录
   （正文中有这两个标题）。
4. **原文斜体 → 中文粗体**（见 §4.5）。
5. **批注不进入排版**：全部批注在源码中，故成品 PDF 不含批注文字。
6. **原文标记保留**：作者留的编辑性标记（如 “References welcome”）在译本中照译保留，未删。

## 7. 统计

| 项目 | 数值 |
|---|---|
| 原文页数 / 正文字数范围 | 136 页（正文 pp.1–106 + 参考文献 pp.106–136） |
| 译本页数 | 131 页 |
| 编号公式 | 174 条（174/174 回读验证通过） |
| 图 | 5 张（原图截取重排） |
| 表 | 3 张 + 缩写表（33 条） |
| 参考文献 | 1309 条（自动转录，英文原貌） |
| 批注（Tutor Notes） | 156 条，见《译注汇总.md》 |
| 编译状态 | LuaLaTeX ×3：0 error、0 undefined、0 missing character |

## 8. 文件清单

```
AGT对应关系慢讲_中文译注本.pdf   成品（131 页）
src/
  main.tex                        汇总文件
  preamble.tex                    导言区（宏、环境、页眉）
  chunks/                         各章片段（c00/c01/tr01–tr08/c-refs）
  figures/                        图与图形公式（原图截取）与 TikZ 无需的裁图
  build.ps1                       一键编译
build.ps1                         一键编译（副本）
compile.log                       真实编译日志（main.log）
译注汇总.md                        全部 Tutor Note 索引
README.md                         本文件
```
