# workflow.md —— 第 18 篇实际工作流

记录本篇真实走的顺序、每步产出、最耗时/最易错处，以及「若重做怎么改」。不含本机路径。

## 1. 实际顺序（共 11 步）

| 步 | 做什么 | 产出 |
|---|---|---|
| 1 | 读 `TASK.md`、`XREF.md`、`BRIEF.md` §9/§10、`cards/SCHEMA.md`，扫 `out/17_ggl17/`、`datasets` 的既有卡风格 | 交付清单与字段约束台账（写在纸上，不进仓） |
| 2 | 读 `txt/18/p001.txt` 摘要 + 引言 + 结论，定主线 | 一句话主题与四段式主线（模型 → 代数等价 → 水平关系 → 几何翻译） |
| 3 | 扫节标题与定理/公式陈述（p002–p097），只对主线公式逐步推 | notes.md 骨架表与主定理清单的草稿；7 处验算 |
| 4 | 下载并比对 arXiv v1（2007-10-31）与 v5（2008-03-12）的 LaTeX 源 | `external/v1/main.tex`、`external/v5/main.tex`、`external/v1_v5.diff`（6658 行，+3047/−2696）；确认中心荷式两版相同、E1 两版都在 |
| 5 | 下载 Paper II（0804.0804）与 Frenkel 讲义源，抽 §5 的一般群推导 | `external/paperII_main.tex`、`external/frenkel_lectures.tex`；(3.60)–(3.63) 的第二独立出处 |
| 6 | 用 pymupdf 抽 KW06（`pdf/01`）印刷页 122/130/149 原文，核 Hecke 算子/特征层的对照句 | B 类 sources 的实文依据 |
| 7 | 建页码地图：把 50 余个式号映射到 PDF 页（脚本在 `txt/18` 上跑正则） | 式号→页码表；卡片 `anchor` 与推导卡 `locator` 的页码全部由此表定 |
| 8 | 逐页实读关键页（p008–p011、p021–p025、p033、p047–p059、p064–p068、p069–p072、p074–p080、p082–p086）并筛 A 类引文 | 39 条通过归一化匹配的英文短引（12–120 字符） |
| 9 | 写 `terms.tsv`（28 行）、`errata.tsv`（4 条）、`notes.md` | 三件基础交付物 |
| 10 | 写 12 张卡（概念 9 + 推导 3），每张按 schema 填 sources/quote/related | `cards/concepts/*.json`、`cards/derivations/*.json` |
| 11 | 跑四道闸门并修：lint → verify → audit_locators → term_index；status 统一改 `dev` | 全绿；另补 `excerpts.md`、`trace.md`、`workflow.md` |

## 2. 最耗时的三步

1. **页码地图 + 引文筛选（第 7、8 步）**：约占总时间的三分之一。式号与页码没有现成对照表，只能靠正则在 100 个 txt 上批量定位再人工核对；引文要同时满足「12–120 字符」「归一化后逐字命中」「落在声明页」，平均每条试 2–3 个候选串才中。
2. **一般 N 的中心荷验算（第 3 步）**：(3.54) 的常数项 $N^4-2N^3+N$ 与 $N^4-1$ 必须对上 (3.31) 的 ghost 求和，$N=2,3$ 各算一遍才敢写进 notes §5，并据此判断 W₂/W₃ 的值不是笔误。
3. **v1↔v5 的 diff 判读（第 4 步）**：6658 行的 diff 里要确认「公式骨架没变」，只能盯着中心荷式与 E1/E4 所在行的行号比对；行号在 diff 里不可直接用，要回到两个 `main.tex` 里 `grep -n` 定位。

## 3. 最易错的四处

- **页码约定**：本篇 PDF 页 = 印刷页（p001 标题页），而 KW06 印刷页 = 其 PDF 页 −1。两套约定混用会让 B 类 `section` 的页码整体错 1。
- **式号与「最近引用」**：原文常在式后隔两段才引用它，凭上下文猜式号会错（例如把 (2.61) 当成 (2.62)）。
- **B/C 类 anchor 的写法**：`audit_locators.py` 只看 `locator`/`source`/`anchor`，且只要片段里同时出现 `p.N` 与圆括号式号就会校验。外部式号必须写进 `section`，否则必报「eq not on p.」。
- **errata 的字段数**：9 个制表符分隔字段，空字段（影响卡片）也必须占位；多一个 tab 就把「状态」挤到第 10 列，lint 报「状态非法」。

## 4. 若重做，怎么改

1. **先建页码地图再做精读**：把「式号 → 页码」与「节标题 → 页码」两张表一次性生成（正则 + 人工抽检 10%），后面的引文筛选与 anchor 填写都查表，可省三分之一时间。
2. **引文先 grep 后写卡**：每张卡动笔前，先在目标页 `grep` 关键词，把命中的整句复制进临时清单并立刻过一遍 `verify_pages`，避免写完 12 张卡再统一返工。
3. **外部核对提前到第 3 步之后**：先拿到 Paper II 的 §5 与 KW06 印刷页 122/130/149 的原文，再写任何涉及「水平关系/oper/Hecke 算子」的卡，这样 notes 的外部来源表与卡片的 C 类 sources 可以一次写对。
4. **errata 与 corrections 同批维护**：先在 `errata.tsv` 定稿四条，再写卡时直接引用序号，避免卡片 `corrections[].id` 与 errata 序号脱节。
5. **闸门按「lint → term_index → verify → audit」顺序**：lint 查结构与包级文件（最快暴露字段错误），term_index 查撞名（改 alias 会影响 lint 的 related 不变，但越早越好），verify 与 audit 查页码（最慢，放最后）。

## 5. 本次实际返工清单（真实发生）

| 返工 | 触发 | 改法 |
|---|---|---|
| 三张推导卡 `type: "deriv"` → `"derivation"` | `lint_cards.py` 报「type 与目录不符」 | 逐卡改字段后重跑，错误 0 |
| `errata.tsv` E4 行多一个 tab | lint 报「第 4 行状态非法」 | 脚本规整为 9 字段 |
| 推导卡 locator `A p.62 eq (3.50)` | `audit_locators.py` 报 eq (3.50) 在 p.63 | 改为 `A p.63 §3.3（规范固定前的 Sugawara 部分）`，不再绑式号 |
| 两处 term_index 撞名 | `term_index.py check` 报 2 处 | 删通用 alias / 加限定词，重跑得 0 处 |
| (2.61)/(2.62) 记混 | 实读 p.23 后发现 | 卡片与 notes 一律按 p.23 原文重写 |
| E4 置信度 high → low | 独立出处只有一处（同篇 v5） | 改 low、open、影响卡片留空 |
