# probe.md —— 能力探测与底本尽调（实测证据，2026-11-03）

## 1. 环境探测
| 项 | 实测结果 |
|---|---|
| xelatex | `<本地路径>`（PATH 内） |
| pdflatex / lualatex / latexmk | 同在 MiKTeX bin（未使用） |
| TeX Live 目录 | `C:\` 下无 texlive / tinytex 目录（本机只用 MiKTeX） |
| 冒烟测试 | `ctexart` + `fontset=none` + `simsun.ttc`/`simhei.ttf`/`simkai.ttf` 绝对路径 → **xelatex 退出码 0，PDF 18560 字节**，中文与数学均正常 |
| TMP | 本机 `%TMP%` 可写；编译时仍显式设 `TMP/TEMP=proj\build` |
| Python | 3.12.14（DSH 运行时），`pymupdf` 1.28.5 可用；`pdftotext.exe` 亦有（MiKTeX 附带） |
| 写入权限 | 工作区 `<本地路径>` 可写（已实测渲染 169 页 PNG） |
| 字体 | `C:\Windows\Fonts\simsun.ttc / simhei.ttf / simkai.ttf / simfang.ttf` 均存在 |

**结论**：xelatex + ctexbook 路线可行（未使用 lualatex；本工作区是纯 ASCII 路径，无需镜像编译目录）。

## 2. 底本尽调（Deck Check）
| 检查项 | 实测 |
|---|---|
| 作者/标题 | 首页：**Kevin Setter**, *Topological Quantum Field Theory and the Geometric Langlands Correspondence*；Caltech 博士论文 2013（答辩 2012-08-24）。PDF 元数据无作者/标题，creator=TeX, producer=pdfTeX-1.40.11, 生成于 2012-09-19 |
| 总页数 | **169**（含封面/前言 x 页）|
| 页码偏移 | **PDF 页号 = 印刷页码 + 10**（PDF p.11 页脚 "1"；PDF p.169 页脚 "159"）|
| 正文范围 | 印刷 pp.1–154（9 章 + 附录 A–D）；pp.155–159 参考文献 |
| 位图/矢量 | `get_images()` 41 个位图对象（集中在 p.13 封面图 1 张 + p.50 图 4.7 的 40 个切片）；`get_drawings()` 649 条（多为分式横线），**图共 10 张**（1.1, 2.1, 4.1–4.7, 6.1）|
| 编号公式 | **57 条**（1.1–1.3, 2.1–2.4, 3.1–3.11, 5.1–5.8, 7.1–7.9, 8.1–8.3, 9.1–9.3, B.1–B.14, D.1–D.2）；第 4、6 章与附录 A、C 无编号公式 |
| 定理类环境 | 定理 3.3（印刷 p.97）；第 9 章 定义 1–7、命题 1–10；附录 D 命题 1–2 |
| 表格 | **0 张**（原文没有表格）|
| 目录 | 印刷 pp.vi–ix，与实际章节起始页一致；`get_toc()` 无 PDF 书签 |
| 其它 | 原文有若干**方框公式**（如 (1.2) 两方框+双向箭头）|

## 3. 素材制备（已完成）
- `pages/p001.png … p169.png`：200 dpi 逐页渲染
- `split/pNNN.txt`：逐页文字层（已做连字归一 ﬁ→fi 等）+ 页脚/印刷页号表头
- `full.txt`：全书文字层
- `tags.txt` / `tags_bypage.txt`：57 条编号公式清单（由右边界 span 位置判定，避免把行文引用误判为公式）
- `src/figures/fig11.png … fig61.png`：10 张图按 400 dpi 裁剪，已逐张 `read_image` 目视复核（完整、无截断、无原编号）
