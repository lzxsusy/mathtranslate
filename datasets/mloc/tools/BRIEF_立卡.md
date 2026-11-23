# 立卡规范（mloc 资料卡）

本文件是分派给子代理的立卡要求，与 `SCHEMA.md`、`taxonomy.md` 合起来读。

## 0. 一卡一问

一张卡回答**一个**能独立成立的问题。读者不需要读全书就能看懂并复述。
粒度参考：`datasets/dmod/cards/concepts/` 里的既有卡（先读 2–3 张，照它的密度与口吻写）。

**只收本书特有的东西**：通用 D-模概念（如「D-模」「导出范畴」）若 dmod 已有卡，不要重复立；
本书特有的构造（齐性扭层、`D_λ`、`∆_λ`、交织函子 `$I_w$`、HC 层、广义 Verma 模、KL 算法）必须立。

## 1. 语言

- 中文；术语以 `工程文件/work/术语表.tsv` 为准；人名保留拉丁字母。
- `summary` ≤ 120 字（concept）/ 100 字（example），一句话说清「这是什么」。
- `question` 以「？」结尾（全角）。
- `key_points` 每条一个断言，不要「首先/其次」这种空话。

## 2. 数学

- 公式用 MathJax 标准宏：`$D_\lambda$`、`$\mathcal{M}_{qc}(D_\lambda)$`、`$\Gamma(X,-)$`、`$H^i(\mathfrak{n}_x,V)$`。
  不用 LaTeX 自定义宏（`\g`、`\h`、`\D`、`\calO` 一律展开成 `\mathfrak{g}`、`\mathfrak{h}`、`D`、`\mathcal{O}`）。
- 定理的 `proof.steps` 最多 6 步，每步 `{no,text,why}`；`why` 写「为什么这步合法」（用了哪条引理、哪个性质）。
- 证明有洞时 `proof.status="sketch"` + `gap_note` 写清洞在哪；**不许**用「显然」掩盖。
- `pitfalls` 至少 1 条，写真实易错点（记号冲突、下标 −ρ 平移、单复形与双复形混淆之类）。

## 3. 页码与对照

- `sources[].book` 固定写 `Miličić, Localization and Representation Theory of Reductive Lie Groups`。
- `pages` 是**印刷页**（底本印在页脚的号），`pdf_pages = pages + 4`。
- **页眉里的页码属于该 PDF 页本身**：`en/chNN.txt` 的 `===== BOOK PAGE n (PDF m) =====` 标记是最可靠来源，
  不要拿上一章某页页眉上的号当作下一章的起始页（第 3 章 §9 的页眉是 83，第 4 章却从 85 起，极易错位）。
- `anchor` 写译本的定位：`源码/chapters/ch02a.tex:88-96（引理 1.2）`，行号可用
  `grep -n "引理 1.2" 源码/chapters/ch02a.tex` 查到。
- 一张卡可给多条 `sources`（定义在一处、证明在另一处）。

## 4. 核验（verification）

- 默认 `status="source-only"`、`checked_on="2026-11-23"`、`checks=[]`。
- 若你**真的**访问了 nLab / Stacks Project / ProofWiki 并确认，写进 `checks`
  （`{source,entry,url,last_revised,asserts,verdict}`），`status="external-confirmed"`；
  没访问就**不要**编造——本库对编造核验零容忍。
- 与权威陈述冲突时 `status="rejected"`，并在 `pitfalls` 说明。

## 5. 字段与文件

- 文件名 = slug：`cards/concepts/kazhdan-lusztig-algorithm.json`。
- `id = "mloc/concept/<slug>"`；example 卡 `id = "mloc/example/<slug>"`。
- `related` 至少 2 条，可以指向 `mloc/...`（必须存在）或 `dmod/...`（跨库，不校验）。
- `rights="rewritten"`，`status="draft"`。
- 写完后自检：
  ```bash
  cd datasets/mloc && python tools/lint.py
  ```
  自己负责的那几张必须 0 error（warning 可接受，但 summary 超长要改）。
