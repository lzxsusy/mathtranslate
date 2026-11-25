你是《Grassmannians, Moduli Spaces and Vector Bundles》中译精读工程的第 04 章读者。
工程根：C:\Users\admin\Downloads\Grassmannians-精读
你的章：ch04 · Jeffrey · 《奇异向量丛模空间中的相交配对》
       中译 p.72–81（10 页）= 英文 PDF p.78–89 = 原书 p.69–80

## 先读（按顺序）
1. `BRIEF.md` 全文（尤其 §1 页表、§7 质量门、§8 文件格式）与 `STATUS.md`。
2. `产出\汇总\existing-notes.tsv` 里你这一章的已有译注（3 条）——**这些不要重复登记**；
   若认为某条登记有误，另立 `type=existing-note-wrong` 并说明理由。
3. `source\TERMINOLOGY.md`（术语权威，只读）。全书 81 处译注的原始清单在 `source\PROGRESS.md`
   的 `## 原书错误（译注清单）` 里，需要原话时去查你那一篇的表。
4. 你的中文源：`source\chapters\ch04.tex`（32,374 字节，全章）。
5. 英文对照：`python tools\pdf_pages.py text en 78-89 -o tmp\en_ch04.txt`，然后逐页读。
6. 版面核对：`python tools\pdf_pages.py png zh 72 --out 产出\_pages`，只渲真正需要的页。

## 本章提示（来自 BRIEF §5，是提示不是清单，以正文为准）
- 必抓对象：部分消奇异（partial desingularization）、相交上同调、等变上同调、Kiem 定理、M(n,d) 与 M(2,0)、相交配对、Kirwan 消奇异、局部化公式
- 难点：相交上同调的层论定义与 de Rham 版本对照；等变上同调在奇点上的行为。原书 p.80 是空白背面页。编号混合（iremark 独立 1–3）
- 卡片配额：概念 6 / 例子 1

## 产出（6 个文件，格式见 BRIEF §8）
1. `产出\导读\ch04-导读.md`      1200–2000 字，五节：位置 / 前置知识 / 阅读路线 / 核心结果 / 术语对照
2. `产出\批注\ch04-批注.md`      ≥12 条，编号连续；五种类型都要有（数学-难点 / 数学-补证 / 译注-核对 /
                                    译文-问题 / 联系-他章），可另加 背景-补充
3. `产出\批注\ch04-errata.tsv`   对读发现的问题：chapter,loc_book,loc_zh,loc_tex,type,severity,original,problem,suggestion,evidence
4. `产出\笔记\ch04-笔记.md`      1500–2500 字，五节：主线 / 关键构造 / 我的补全 / 疑问 / 延伸
5. `产出\汇总\cards-ch04.tsv`    ≥6 概念卡 + ≥1 例子卡候选：local_id,type,title_en,title_zh,track,one_line,anchor
6. `产出\汇总\ch04-report.md`    做了什么 / 统计 / 存疑 / 给 Lead 的 TODO

## 硬规则
- 只写上面 6 个路径（以及 `tmp\` 下你自己的临时文件）；不改 `source\`、`original\`、别的章的文件。
- 中文数学以 .tex 为准；公式不要从 PDF 文字层抄（会被拆碎，如 `DV f = V [f] + ˜D(V )(f)`）。
- 页码三种写法别混：`原书 p.N` / `中译 p.N` / `英文 PDF p.N`。
- 术语照 `TERMINOLOGY.md`；新术语记在 `cards-ch04.tsv` 的 note 里或在 report 里列，不改术语表。
- 卡片候选的 `anchor` 必须是 `chapters/ch04.tex:行号`，且行号真指向该内容（写完回查一次）。
- 不编造：读不懂的地方写进笔记「疑问」节并在 report 里点出来，不许假装读懂。
- 文件 UTF-8 无 BOM、LF；用 write 工具写，不要用 shell 重定向写中文。
- 交前自检：6 个文件都在、字数达标、批注编号连续、tsv 每个字段数与表头一致（正文里不许出现裸 tab）。
