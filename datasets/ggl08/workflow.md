# 第 08 篇 · 工作流记录

按实际发生的顺序写，没有做的事不写。

## 1. 读任务与规则（约 0.5 h）

- 读 `TASK.md`、`XREF.md`、`BRIEF.md` §9/§10、`cards/SCHEMA.md`。
- 读 `tools/lint_cards.py`、`tools/verify_pages.py`、`tools/term_index.py` 的源码，抄出硬规则：
  id 正则与 slug=文件名、`type` 与目录对应（概念 `concept` / 推导 `derivation`，但 id 段用 `deriv`）、
  `sources.pages` 对所有 text 都要求 $1\le lo\le hi\le$ `--max-pages`、`text=A` 的 quote 12–120 字符且逐字、
  `related` 必须指向存在的卡、`corrections.id` 必须在 errata.tsv、notes 必须有「## 核对与勘误」且其下表格 ≥4 行。
- 跑 `tools/xref.py 8`（此前已生成 `XREF.md` 与 `external/xref.json`）。
- **产出**：一份规则清单（写在草稿里，后来落进 notes 的「核对与勘误」）。

## 2. 逐页读原文（约 3 h，最耗时）

- `txt/08/p001.txt … p030.txt` 已由 `tools/extract.py 8` 生成，逐页读，记「页 → 公式/命题」表。
- 发现纯文本抽取会丢上下标（例如 $\tau^\vee=-1/(n_g\tau)$ 抽成 `τ∨ = −1/ngτ`），于是用 pymupdf 把
  p3/8/10/11/12/13/14/16/19/20/21/22/24/25/26/27 渲染到 `external/pageNNN.png`（170 dpi），逐张目视核公式。
- **产出**：`external/` 16 张页图 + 一张「式号 → 页码 → 逐字形式」的核对表（这张表后来决定所有 locator）。

## 3. 外部核对（约 2 h）

- 目标只有一个：把写进卡片的关键公式各找到两处独立出处。
- 实读：`pdf/01`（KW06）p.9–11 的 $\mathrm{Tr}$ 归一化与 (2.11)(2.12)、p.35–36 的扭化作用量、p.48 的欧氏 (4.16)；
  `pdf/02`（Gukov–Witten）p.13 的 $e^{i\theta d}$、p.17 的 (2.26)、p.21 的 (2.38)(2.39)；`pdf/06` p.5 的 Hecke/'t Hooft 句；
  `pdf/07`（0902.0948）p.6 的 Taub-NUT 度量。
- 网页：nLab「geometric Langlands correspondence」、arXiv:0711.2083 的 abs 页（用 `web_fetch`）。
- **产出**：E1 的判级（high）、notes 的「外部来源」六行表。

## 4. 写卡片（约 2 h）

- 不手写 JSON，写两个生成脚本 `_gen_concepts.py`、`_gen_deriv.py`：把卡片写成 Python 字典、`json.dump(ensure_ascii=False, indent=2)`，
  避免漏逗号/中文转义。用完即删（脚本已删）。
- 10 张概念卡：六维 gerbe、四维 $U(1)$ 对偶、$(0,2)$ 理论、共形块与 Heisenberg 群、't Hooft→Hecke、各种维数的缺陷、
  Taub-NUT、$\Gamma_k$、BPS 两种描述、电/磁分级。
- 4 张推导卡：$U(1)$ 对偶（含 E1 订正）、$\tau\to-1/\tau$、反常流入、$\Gamma_k$ 分解。
- **产出**：`cards/concepts/*.json` 10 张、`cards/derivations/*.json` 4 张。

## 5. 迭代质检（约 1.5 h，最易错）

1. `lint_cards.py`：第一轮报 6 个 `related` 指向不存在的推导卡（预期，推导卡还没写）。
2. 写完推导卡后报 4 个「type 与目录不符」：`type` 要写 `derivation` 而 id 段是 `deriv`；改字段后只剩 notes 缺失。
3. `verify_pages.py`：第一轮报 3 条「搜不到 quote」，全是 `electric-magnetic-grading` 的句子（我凭压缩摘要转述的）；
   回读 p.23/p.24 改逐字引文，并发现两条页码应是从 23 而不是 24；再跑 57 条、0 问题。
4. 写完 notes/terms/excerpts/errata/trace/workflow、回填 XREF 后跑三项质检（结果见文末）。

## 6. 写笔记与训练数据（约 1.5 h）

- `notes.md`：骨架表、主定理清单、与已译篇目的接口表、XREF 五项回填、外部来源表、勘误、约定差异、「不懂」六条。
- `terms.tsv` 31 行（30 条术语 + 表头）、`excerpts.md` 4 段、`errata.tsv` 1 行、`trace.md` 14 条（4 条真实弯路）、`workflow.md`（本文）。

## 最耗时 / 最易错

- **最耗时**：逐页核公式。纯文本丢了上下标，几乎每个公式都必须回 PDF 目视；30 页里真正要核的约 15 页。
- **最易错**：①quote 的逐字性（凭记忆/摘要转述必被打回）；②页码漂移（式号在页首还是页尾决定它属于哪页，
  (5.4)(5.5) 在 p.17 不是 p.16）；③lint 的 `max_pages` 对 B/C 源同样生效，KW06 的 (4.16) 在 p.48 就进不了 sources。

## 如果重做

1. 第一步就把「式号 → 页码 → 逐字 LaTeX」做成一张 grep 表，所有 locator 从表里取，不靠记忆——可省掉两轮 verify 返工。
2. 写 quote 时直接从 `txt/08/pNNN.txt` 复制粘贴（而不是先从压缩摘要里写、再回查），一步到位。
3. 先读 lint 源码再动笔，`type`/`max_pages`/`related` 这三类错误可以完全避免。
4. 外部核对前先列「要核哪几个公式、每个需要哪两处出处」，避免在读无关页面上花时间。
