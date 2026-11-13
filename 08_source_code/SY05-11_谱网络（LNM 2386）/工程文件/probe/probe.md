# probe.md —— 环境与底本实测记录（禁止猜测，全部为实测值）

日期：2026-11-03　执行：Lead

## 一、能力探测

| 项目 | 实测结果 | 证据 |
|---|---|---|
| 工作目录 | `<本地路径>`（**必须全 ASCII 路径**） | 见下条 |
| TeX 工具链 | TeX Live 2026，`<本地路径>`（**不在 PATH**，要用绝对路径） | `xelatex --version` → XeTeX 3.141592653-2.6-0.999998 (TeX Live 2026) |
| 冒烟测试 | ✅ 通过：`ctexart` + `fontset=none` + `simsun.ttc` 出 1 页中文 PDF（31,717 bytes，0 error，0 Missing character） | `work/tools/smoke/` |
| 中文字体 | `C:\Windows\Fonts\simsun.ttc`、`simhei.ttf`、`simkai.ttf`、`simfang.ttf` 均在 | `Get-ChildItem C:\Windows\Fonts` |
| **路径限制** | **中文/非 ASCII 路径下 xelatex 无法写文件**（`! I can't write on file smoke.log`），ASCII 路径正常 | 对照实验：`Desktop\中文测试\` 失败，`_sn_probe\` 成功 |
| **TMP 必须设置** | 编译前设 `$env:TMP`/`$env:TEMP` 到工作区内的 `work\tmp`（SOP 事故 #2：xdvipdfmx 崩溃） | 本次编译均如此 |
| Python | `<本地路径>`（3.12） | `python --version` |
| PyMuPDF | ✅ `PyMuPDF 2.0`（MuPDF 1.28.5）→ 可渲染、可抽文字、可 `get_drawings()` | `import pymupdf` |
| PyMuPDF 渲染 | 200 dpi；Letter 612×792pt → 1700×2200 px | `get_pixmap(dpi=200)` |
| 字体嵌入 | 用 `Path=C:/Windows/Fonts/` 显式文件路径，不用 fontconfig | 冒烟日志无 fontconfig error |
| 标准字体名 | ❌ 不可用：`\setmathfont{Latin Modern Math}` 报 "font cannot be found"（无 fontconfig）；**数学字体一律用 .otf 文件名或默认 CM 数学** | 冒烟日志 |
| 写入权限 | Desktop 可写；dsh 策略 danger-full-access | 实测 |

## 二、底本尽职调查（Deck Check）

| 检查项 | 实测值 |
|---|---|
| 真实标题 | *Spectral Networks: Bridging higher-rank Teichmüller theory and BPS states* |
| 真实作者 | Clarence Kineider; Georgios Kydonakis; Eugen Rogozinnikov; Valdo Tatitscheff; Alexander Thomas |
| 来源 | Springer Lecture Notes in Mathematics 2386（arXiv:2412.03588v3 [math-ph], 7 May 2026） |
| PDF 总页数 | **514** |
| 页面尺寸 | Letter 612 × 792 pt |
| **页码映射** | **印刷页码 = PDF 页号 − 40**（p43 = 印刷 p.3；实测 p53→13, p61→21, p77→37, p93→53） |
| 结构 | 封面/前言 pp.i–xix（PDF 1–40）；Motivation & Historical Perspective pp.xxi–xl；Part I–V；**26 章**；Appendix A（PDF 461–484）；Bibliography（PDF 485–504）；Index（PDF 505–514） |
| 位图 | 全本仅 **2** 个位图（封面装饰 + 1 处），其余图形全部是**矢量绘图**（`get_drawings()` 共 9086 条路径） |
| **插图** | **165 个 `Fig. X.Y` 图注**，多章有子图 (a)(b) |
| 编号公式 | 文字层抽到 **197 个唯一编号**（`(\d+\.\d+)`），各章分布见 `work/tags.txt`（文字层可能漏，公式以图像为准，验收时以 tags.txt 为基准再人工核对） |
| 定理类环境 | Definition / Theorem / Proposition / Lemma / Corollary / Example / Exercise / Remark / Notation / Convention 等，编号手工给定 |
| 表格 | 有少量 Table（文字层 `Table` 计数见 `work/envcount.json`）；表格按原文重排，不造新表 |
| 目录 | 印刷 pp.vii–xv 有完整 Contents，与正文实际起始页一致（已核对章节起始页） |
| 链接/脚注 | 无超链接依赖；脚注为页内文字 |

## 三、环境要点（给全体译者）

1. 编译由 Lead 统一执行，**译者不要自己编译**；源文件只要片段。
2. 项目路径必须 ASCII；不要在路径里放中文。
3. 公式文字层**不可信**（Springer 数学字体无 ToUnicode：`𝜋1`、`𝑤𝑗𝑏`、`≅` 抽成 `\x1b`）→ **公式一律逐页看 200dpi 图像抄**。
4. 插图由 Lead 统一裁切到 `work/figures/`；译者只写 `\Fig{...}{...}{...}` 引用，**不得自造插图**。
