# SY05-25 工程说明：Witten《镜像对称、Hitchin 方程与朗兰兹对偶》译注本

本目录是《镜像对称、Hitchin 方程与朗兰兹对偶》（Edward Witten, *Mirror Symmetry, Hitchin's Equations, and Langlands Duality*, arXiv:0802.0999v1, 2008-02-07, 15 页）中文译注本的完整工程：底本、译文、46 条译注、译者后记、术语表、构建脚本与校核记录。

- 成品：`源码/main.pdf`（41 页；前置 roman ii–iv，正文 arabic 1–37）
- 源码：`源码/main.tex`（主文件）、`源码/preamble.tex`（版式与宏）、`源码/front.tex`（封面、凡例、摘要）、`源码/sections/sec1–sec6.tex`、`refs.tex`、`afterword.tex`（译者后记）、`appendix_glossary.tex`、`appendix_notes.tex`
- 生成物：`源码/gen/notes_macros.tex`、`源码/sections/appendix_glossary.tex`、`源码/sections/appendix_notes.tex`、`工程文件/译注清单.tsv` —— **均由脚本生成，勿手改**
- 单一真源：`工程文件/tools/notes_data.py`（46 条译注的注文、来源、nLab 词条）

## 工作流（自底向上，可复现）

```
① 底本抽提与核对   pymupdf 抽全文 + 逐页 170dpi 渲染 → work/fulltext.txt、work/pages/pNNN.png
                   （公式字符一律以页面图为准，文本层只用于定位）
② 通读与疑点清单   先通读、先记疑，疑点未解=0 才动笔
③ 词条查证         check_nlab*.py 探 200/404；fetch_nlab2.py 抓 Last revised → work/nlab_index.tsv
④ 译注落数据       notes_data.py: NOTES[id, sec, kind, nlab, ref, text]
⑤ 生成器           gen_tables.py → 脚注宏 + 附录 A/B + 译注清单.tsv（四个产物同源）
⑥ 排版             xelatex main.tex ×2（ctexart + 手工 TikZ 两张图）
⑦ 校验             日志零 Overfull / 零缺字 / 零 undefined；latex_look 逐页目视；
                   pymupdf 抽页核对目录、页码、公式编号
⑧ 打包             工程文件 + 源码 + 成品 + 精选片段 + 校核记录
```

## 构建

```powershell
# 推荐：一条命令重建（会先跑生成器，再编译两遍）
powershell -ExecutionPolicy Bypass -File 工程文件\tools\build.ps1
```

依赖：MiKTeX（xelatex，含 ctex、tikz、booktabs、longtable）、Python 3（脚本仅用标准库，`notes_data.py` 为纯数据）。

## 体例要点

- 正文为**语义级忠实翻译**：不改写、不删节、不合并段落、不调整论证次序；节号、公式号、脚注位置、参考文献条目保留原位。
- 脚注两类：**【原注】**（作者脚注，5 条）/**【译注 x.y】**（译者所加，46 条）；译注来源分三级：A 原文或经典原始文献、B nLab 等社区来源（均与 A 交叉核对）、I 本库内部或纯由原文推得（标「译者按」）。
- 篇末《译者后记》梳理全文框架与六节推导链，并给出一张依赖关系图（图 2）。
- 附录 A 术语与记号对照表（38 + 18 条）；附录 B 译注汇编（与正文脚注同源）。

## 契约

- `源码/gen/` 与两个 `appendix_*.tex` 是生成物，改动会被下次 `gen_tables.py` 覆盖；要改译注请改 `工程文件/tools/notes_data.py`。
- 正文中 `\zhnt{4.5}` 只写 id，注文与来源由宏注入；**新增译注必须同时改 `notes_data.py` 与正文 id**，否则编译缺宏。
- 本工程不含底本 PDF；底本见投稿信息中的 arXiv 编号。
