# probe.md — SY05-24 备料说明

## 素材清单（均在 `工程文件\`）

| 文件/目录 | 内容 | 谁生成 |
|---|---|---|
| `底本_arXiv-2006.13630.pdf` | 底本副本（32 页，541,715 B） | 已备 |
| `pages\pNN.png` | 逐页渲染图，200 dpi，NN = PDF 页序 01–32 | `prep.py` 已跑 |
| `split\pNN.txt` | 逐页文字层 | `prep.py` 已跑 |
| `full.txt` | 全文文字层（**别整本读**） | `prep.py` 已跑 |
| `eqs_raw.txt` | 机械抓取的公式号与所在页 | `prep.py` 已跑 |
| `probe_raw.txt` | 元数据、目录、逐页首末行 | `prep.py` 已跑 |
| `TIMELINE.md` | 分块表、公式→页、小节页、坑 | Lead |
| `glossary.tsv` | 215 条术语（真 TAB） | `gen_glossary.py` 已跑 |
| `check_block.py` | 单块自检（内建 10 块的期望号表） | Lead |
| `crop.py` | 页面局部放大 | Lead |
| `build.ps1` | 全本编译（Lead 专用，块施工者不要跑） | Lead |

## 常用命令

```powershell
$env:PYTHONIOENCODING='utf-8'
$py='<本地路径>'
# 自检
& $py 工程文件\check_block.py 源码\sec1a.tex
# 裁切：第 10 页，纵向 0%–30%
& $py 工程文件\crop.py 10 0.0 0.30 工程文件\work\t10.png
# 裁切：第 13 页的表格区（纵向 30%–80%），600 dpi
& $py 工程文件\crop.py 13 0.3 0.8 工程文件\work\t13.png --dpi 600
```

## 已知坑

1. **文字层塌公式**：pdfLaTeX 产物，分式/上下标/矩阵会串行，`(3.32)` 甚至被挤到行首 `c)]. (3.32)`。公式只看页面图。
2. **表格文字层逐格碎行**：p10 的 Table 1 在 `split\p10.txt` 里每格一行，顺序不可靠；必须看 `pages\p10.png`。
3. **PDF 页 = 印刷页 + 1**：p1 是 JHEP 标题页（无页码）；`split\p01.txt` 里是标题/作者/摘要。
4. **页码是 PDF 页序**，不是页面上印的页码。
5. **控制台中文乱码**：读文件内容用 read 工具，不要 `Get-Content` 判断内容；PowerShell 写文件用 write 工具（UTF-8），别用 `Set-Content`。
6. **PYTHONIOENCODING=utf-8** 必须设，否则 python 打印中文可能抛 UnicodeEncodeError。
7. **不要跑 `build.ps1`**；它需要 UTF-8 BOM 才能被 PowerShell 5.1 正确解析（Lead 已处理）。
