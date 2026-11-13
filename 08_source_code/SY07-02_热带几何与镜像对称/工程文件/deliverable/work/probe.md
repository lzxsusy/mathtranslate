# 底本尽调（实测）

- 文件：`src/Gross_TropicalGeometryAndMirrorSymmetry.pdf`
- 标题：Tropical Geometry and Mirror Symmetry
- 作者：Mark Gross（UCSD）
- 出版：AMS, CBMS Regional Conference Series in Mathematics 114, 2011
- 元数据：{'format': 'PDF 1.6', 'title': '', 'author': '', 'subject': '', 'keywords': '', 'creator': '', 'producer': 'ESP Ghostscript 815.02', 'creationDate': 'D:20101002113445Z', 'modDate': "D:20130510153715+02'00'", 'trapped': '', 'encryption': None}
- 总页数（PDF）：332；PDF 页 = 印刷页 + 14
- 编号公式（去重后）：128 条
- 图（Figure N. 标题数）：34 张；表（Table N.）：0 张
- 定理类环境出现次数：{'Definition': 80, 'Example': 146, 'Lemma': 83, 'Proposition': 114, 'Theorem': 96, 'Exercise': 1, 'Corollary': 7}

## 章节页段（印刷页 / PDF 页）

| 章节 | 印刷页 | PDF 页 |
|---|---|---|
| Ch1 The tropics | pp.1--32 | PDF p.15--46 |
| Ch2 A- and B-models | pp.33--89 | PDF p.47--103 |
| Ch3 Log geometry | pp.91--129 | PDF p.105--143 |
| Ch4 Mikhalkin's curve counting formula | pp.133--171 | PDF p.147--185 |
| Ch5 Period integrals | pp.173--244 | PDF p.187--258 |
| Ch6 The Gross-Siebert program | pp.247--306 | PDF p.261--320 |

## 素材

- `split/pNNN.txt`：逐页文字层（仅用于定位；数学符号一律以 `pages/pNNN.png` 为准）
- `pages/pNNN.png`：150 dpi 逐页渲染
- `tags.txt` / `tags_bypage.txt`：编号公式清单（验收唯一依据）
- `figs.tsv`：图标题所在页
## 修正说明（实测）

- 本 PDF 的文字层是重新 OCR/排版过的，页码：**PDF 页（1-based）= 印刷页 + 15**。
- 公式编号（如 (1.1)）在文字层里是单独一行，位置不固定（本版靠左），已按“整行匹配 (x.y)”提取。
- 图是全书连续编号 **Figure 1..N.**（不是 Figure 1.1 这种小节编号）。
- 图标题页见 `figs.tsv`；图的裁剪见各分块任务说明。
