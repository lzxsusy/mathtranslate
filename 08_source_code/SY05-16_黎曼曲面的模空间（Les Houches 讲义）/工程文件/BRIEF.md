# BRIEF.md — 项目总览（所有队友必读，先读这个再动手）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

## 项目

把 **Giacchetto & Lewański, _Les Houches lecture notes on moduli spaces of Riemann surfaces_（arXiv:2410.13273v2 [math.AG], 46 页）** 翻译成**中文 LaTeX 译注本**：
中文正文 + 原文全部编号公式（155 条）+ 原文全部编号环境（35 处）+ 原文 3 张表 + 图注译文（图不复刻）+ 学术级 Tutor Note 批注（LaTeX 注释形式，另汇总成 `译注汇总.md`）。

主题：黎曼曲面模空间 $\mathcal M_{g,n}$ 与 $\overline{\mathcal M}_{g,n}$ 的递归边界结构、相交理论、Witten 猜想与 Kontsevich 定理、上同调场论（CohFT）、Givental 作用、拓扑递归（TR），以及 JT 引力/双曲几何/拓扑弦的进一步方向。

## 目录（全部在 `<本地路径>`）

| 路径 | 内容 |
|---|---|
| `probe.md` | 实测环境与底本信息 |
| `STYLE_GUIDE.md` | **硬性规范**，违反即返工 |
| `TIMELINE.md` | 分块表：页码、公式、环境、图的归属 |
| `glossary.tsv` | 术语冻结表（制表符分隔：en, zh, note） |
| `pages/pNN.png` | 46 页 200 dpi 渲染（**公式的唯一真值**） |
| `split/pNN.txt` | 逐页文字层（定位用；**数学不可信**） |
| `full.txt` | 全书文字层（全局检索） |
| `tags.txt` | 155 条编号公式清单（验收依据） |
| `crop.py` | 裁剪放大脚本（看公式用） |
| `check_block.py` | 单块静态自检（你交前必须跑） |
| `src/preamble.tex` | 导言区（**Lead 独占，只读**） |
| `src/*.tex` | 各块译文片段（每人只写自己那一个） |
| `main.tex` | 主文件（**Lead 独占**） |
| `ERRATA.md` | 原文笔误登记（Lead 汇总） |

## 铁律（摘要，细则见 STYLE_GUIDE）

1. **数学必须看图抄**：`pages/pNN.png` 是唯一真值。文字层里 `\frac{m}{2}` 会变成 `2m`，矩阵会碎成单字符，`\overline` 会丢。逐条公式对着图看。
2. **编号是王**：你负责的 `\tag{x.y}` 一个不能少、不能重、不能自造。任务书给了你首尾锚点。
3. **正文照译不许改**：原文笔误照排，批注里指出。
4. **批注写成 `% [Tutor Note: ...]`**，不进排版；`$` 成对；每条要有价值（核对方法/补论证/指笔误/辨记号）。
5. **不插图、不造表**（3 张原表要抄）、不补文献、不写 markdown 粗体、不写 `\newcommand`、不写 `\section`。
6. **只写自己的文件**，UTF-8 无 BOM + LF；用 Python 写，别用 PowerShell `Out-File`。
7. **不自己编译**；交前跑 `python check_block.py <你的文件>` 到 `OK`。
8. **不确定就写批注问，绝不编造物理**。搞不定的写 `% [TODO-LEAD: ...]` 并在回报里说清。

## 工具用法

```powershell
$env:PYTHONIOENCODING='utf-8'                                  # 必设，否则中文 print 崩
$py = '<本地路径>'
& $py crop.py 16 0.30 0.55 d16_mid.png                         # 页 16，纵向 30%–55%，整宽，400dpi
& $py crop.py 16 0.10 0.85 0.30 0.65 d16_eq.png                # 页 16，x 10%–85%，y 30%–65%
& $py check_block.py sec23a.tex
```
然后用 **read_image 工具**看 `d16_mid.png`（可用 glob+read_image；不要用 read 读 PNG）。
一次裁一小块（1/4 页以内）能看清上下标；看不准就再裁更小。

## 上下文节约

- 不要整本 `full.txt` 读进来，按页读 `split/pNN.txt`。
- 每页先看渲染图，再对着文字层定位段落。
- 别反复读 `STYLE_GUIDE.md`，读一遍记住要点。

## 回报

一条消息，格式见 STYLE_GUIDE §10。Lead 汇总编译后会把编译错误定向派回给你修。
