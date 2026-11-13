# BRIEF.md — 项目总览（所有队友必读，先读这个再动手）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

## 项目

把 **Kenji Ueno（上野健爾）, _Conformal Field Theory with Gauge Symmetry_（Fields Institute Monographs 24, AMS）** 翻译成**中文 LaTeX 译注本**：
中文正文 + 原文全部编号公式 + 全部编号环境（定义/定理/引理/命题/推论/例/注）+ 原文图不复刻（原位保留图注译文）+ 学术级 Tutor Note 批注（LaTeX 注释形式）。

## 底本信息（实测）

- 文件：`<本地路径> field theory with gauge symmetry (Kenji Ueno  上野 健爾) (z-library.sk  1lib.sk  z-lib.sk).pdf`
- 178 个 PDF 页；**正文印刷页 p.1–168**，页码偏移固定：
  **PDF 页 = 印刷页码 + 9**（印刷 p.1 = PDF p.10；印刷 p.161 = PDF p.170）。
- 文字层是劣质 OCR（`∈`→`G`、`m`→`ra`、公式碎成单字符、`$` 丢失）。**文字层只用来定位段落，数学一律以页面图为准。**
- 编号体系：定义/定理/引理/命题/推论/例/注**共用一个章内计数器**（如 Definition 1.1、Theorem 1.2、Lemma 1.3 连续）；公式 `(1.1)`、`(1.2)` 也是**章内连续**。

## 目录（工程根目录 `<本地路径>`）

| 路径 | 内容 |
|---|---|
| `BRIEF.md` | 本文件：项目总览 |
| `STYLE_GUIDE.md` | **硬性规范**，违反即返工 |
| `TIMELINE.md` | 分块表：PDF 页、印刷页、归属 |
| `glossary.tsv` | 术语冻结表（制表符分隔：en, zh, note） |
| `pages/pNNN.png` | 178 页 200 dpi 渲染（**公式的唯一真值**） |
| `split/pNNN.txt` | 逐页文字层（定位用；**数学不可信**） |
| `full.txt` | 全书文字层（全局检索） |
| `crop.py` | 裁剪放大脚本（看公式用） |
| `check_block.py` | 单块静态自检（交前必须跑） |
| `src/preamble.tex` | 导言区（**Lead 独占，只读**） |
| `src/bNN.tex` | 各块译文片段（每人只写自己那几个） |
| `main.tex` | 主文件（**Lead 独占**） |
| `ERRATA.md` | 原文笔误登记（Lead 汇总） |
| `block-reports/` | 各块回报（译手写，Lead 读） |

## 铁律（摘要，细则见 STYLE_GUIDE）

1. **数学必须看图抄**：`pages/pNNN.png` 是唯一真值。逐条公式对着图看，看不清就 `crop.py` 裁小块放大。
2. **编号是王**：`\tag{1.7}` 与 `\begin{theorem}[1.4]` 一个不能少、不能重、不能自造，也不能跳号。
3. **正文照译不许改**：原文笔误照排，在批注里指出（并报给 Lead 登记 ERRATA）。
4. **不插图、不造表、不补文献**；原文有图处用 `\figomit{1.1}{图注译文}`。
5. **批注写成 `% [Tutor Note: ...]`**，不进排版；每条必须有干货（核对方法/补论证/指笔误/辨记号）。
6. **只写自己的文件**，UTF-8 无 BOM + LF；**用 Python 写文件**，别用 PowerShell `Out-File`。
7. **不自己编译**；交前跑 `python check_block.py <你的文件>` 到 `OK`。
8. **不确定就写批注问，绝不编造数学**。搞不定的写 `% [TODO-LEAD: ...]` 并在回报里说清。

## 工具用法

```powershell
$env:PYTHONIOENCODING='utf-8'
$py = '<本地路径>'
& $py crop.py 16 0.30 0.55 d16_mid.png                        # PDF 第 16 页，纵向 30%–55%，整宽，400dpi
& $py crop.py 16 0.10 0.85 0.30 0.65 d16_eq.png               # PDF 第 16 页，x 10%–85%，y 30%–65%
& $py check_block.py src/b01.tex
```

然后用 **read_image 工具**看 `d16_mid.png`（不要用 read 读 PNG）。一次裁 1/4 页以内，看不清再裁更小。

## 上下文节约

- 不要整本 `full.txt` 读进来；按页读 `split/pNNN.txt` 定位，主要靠 `read_image` 看 `pages/pNNN.png`。
- 每页先看渲染图，再对着文字层找段落。
- 别反复读 `STYLE_GUIDE.md`，读一遍记住要点。

## 回报

写到 `block-reports/<你的块号>.md`，并给 Lead 发一条消息，格式见 STYLE_GUIDE §10。
