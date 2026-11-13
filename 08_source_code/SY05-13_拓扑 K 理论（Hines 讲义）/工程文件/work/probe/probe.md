# 能力探测 + 底本尽职调查（实测，2026-11-04）

> 本文件是「先探测、后假设」的证据链：每一项都是本机实际跑出来的结果，不是推测。

## 一、环境能力探测

| 能力 | 实测结果 | 证据 |
|---|---|---|
| Python | 3.12.14，`<本地路径>` | `python --version` |
| PDF 库 | **pymupdf 2.0 / MuPDF 1.28.5 可用**（无需自写 PDF 解析器） | `import pymupdf` |
| 页面渲染 | PyMuPDF `get_pixmap(dpi=200)` 直接出 PNG（无需 WinRT/Edge） | `work/pages/p001..p010.png`，1700×2200 |
| TeX（PATH） | `<本地路径>`（xelatex / lualatex / latexmk） | `Get-Command` |
| TeX（非 PATH） | `<本地路径>`（lualatex） | 目录存在，含 lualatex.exe |
| **真编译** | **通过**：LuaLaTeX ×3，ctex 中文 + amsmath + tikz-cd + tcolorbox 可用，0 error / 0 missing char | `main.pdf` 185,792 bytes（冒烟版） |
| xdvipdfmx 崩溃问题 | 本机 MiKTeX 的 xelatex 实测可正常出 PDF（1 页 25 KB），未复现旧项目的 0xC0000409 | 冒烟测试 `probe.pdf` 25,227 bytes |
| 写盘 | Desktop（含中文路径）可写；仍按惯例镜像到 ASCII 目录编译 `default-workspace\hinesbuild` | `write_test.txt` 成功 |
| 网络 | 不依赖（全程离线） | — |

**结论**：旧反馈文档里「无 PDF 库、需手写解析器、需 WinRT 渲染、TeX 驱动全崩」的场景在本机**已不存在**。
本次直接用 PyMuPDF 出页图、LuaLaTeX 出 PDF。

## 二、底本尽职调查（Deck Check）

| 检查项 | 实测值 |
|---|---|
| 文件 | `<本地路径>` |
| 标题 / 作者 / 日期 | Topological K-theory / Robert Hines / December 15, 2016（首页文本实测） |
| 页数 | **10 页**，Letter 612×792 pt，pdfTeX-1.40.16 |
| 页码偏移 | **0**（PDF 页号 = 印刷页码） |
| 位图 | 0 张（`get_images()` 全页为 0） |
| 矢量图 / 交换图 | 仅 p2（9）、p3（4）、p5（9）、p6（8）、p7（4）有 drawings，**全是分段函数花括号、矩阵、交换图**，无插图 |
| 表 | **0 张**（全文无 `Table`） |
| 图 | **0 张**（全文无 `Figure`） |
| **编号公式** | **0 条**（`\(\d+\.\d+\)` 右侧 tag 扫描为空）→ 译本不使用 `\tag` |
| 编号定理类 | 定义 1–8；命题 1–3；引理 1；**定理 1–9**（与原文逐条对应，手工给号） |
| 章节 | §1 Vector Bundles and K(X)；§2 Classification of vector bundles；§3 Bott Periodicity and K-theory as a generalized cohomology theory（§3.1 Another version of Bott periodicity）；§4 An application of K-theory；§5 Other flavors of K-theory（§5.1 Real K-theory；§5.2 Algebraic K-theory） |
| 参考文献 | p.10 共 **5 条**（[Bott] [VBKT] [AGP] [K] [May]），保留英文原貌 |
| 脚注 | 0 条 |
| 习题 | 0 道 |

## 三、素材制备（已生成）

| 路径 | 内容 |
|---|---|
| `work/pages/p001.png … p010.png` | 200 dpi 页图（公式唯一真值） |
| `work/split/p001.txt … p010.txt` | 逐页文字层（仅用于定位，数学不可信） |
| `work/full.txt` | 整本文字层 |
| `work/tags.txt` | 空（原文 0 条编号公式） |
| `work/src/preamble.tex`、`main.tex`、`build.ps1` | 工程骨架，冒烟编译通过 |

## 四、文字层可靠度（实测本例）

- ✅ 正文英文词句、段落边界、章节标题、文献条目 —— 可信；
- ❌ 数学符号 —— 不可信。本例文字层把 `fi` 连字抽成乱码（"de铿乶ition" = definition），
  希腊字母与花体全部丢失（`φ`→`蠁`、`\mathcal`→普通字母、上下标错位）。
  **每个公式必须对着 200 dpi 页图逐符号抄写。**
