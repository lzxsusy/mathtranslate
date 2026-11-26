# 工作流（本篇实际怎么做的）

## 1. 顺序与每步产出

| 步 | 做了什么 | 产出 |
|---|---|---|
| 1 | 读 `TASK.md`、`XREF.md`（`tools/xref.py 21` 已生成）、`BRIEF.md` §9/§10、`cards/SCHEMA.md`，再读 `tools/lint_cards.py`、`tools/verify_pages.py`、`tools/term_index.py` 的源码 | 弄清可核验边界：quote 12–120 字符、pages 两整数、anchor 正则、summary 去公式后 ≤120 字、概念/推导卡各自必填字段、errata 表头与 high 的双依据要求 |
| 2 | 用 `tools/extract.py 21` 生成 `txt/21/p001–p089.txt`，抽验页脚（p003→2、p045→44、p060→59、p083→82、p089→88）确认 **PDF = 印刷 + 1** | 页码口径定死；后续所有 locator 用 PDF 页 |
| 3 | 通读 v2：先 §1 摘要+引言+结论定「解决什么」，再按节读；§2 逐式读 (2.7)–(2.45)，§3 逐式读 (3.1)–(3.80)，§4 读到 (4.59) | 手写骨架 40 余节、主定理 20 条、公式-页码对照表（写进 `notes.md` §1、§2） |
| 4 | 外部校正：`curl` 拉 **v1**（83 页）到 `external/v1.pdf`，用 runtime python 的 `fitz` 抽成 `external/v1_pages/p001–p083.txt`；比对 v1/v2 的节列表与 (3.52) | 得到两条硬结论：v2 新增 §3.9（约 5 页），(3.52) 与非增排序在 v1 p060 已有 ⇒ 排序条件不是新版才加 |
| 5 | 建「引文库」：写 `external/checkq.py`（与 verify_pages 同款归一化），把候选英文句逐条搜全 89 页，只留 12–120 字符且唯一落页的 | `q1.txt`/`q2.txt`/`q3.txt` + 约 60 条已核 quote（页码即命中页） |
| 6 | 立卡：先 3 张概念（OSp/$\hat G$/矩映射），再 5 张概念（超凯勒商、复轨道、源方程、排序、自对偶三形式），再 4 张推导，最后补第 9 张概念（§3.8 对偶） | `cards/concepts/*.json` 9 张、`cards/derivations/*.json` 4 张，全部 draft |
| 7 | 逐卡自查 locator：把每个 `p.N eq (x.y)` 回该页 `grep` 式号；发现 `nahm-moduli-to-orbit` 第一条 quote 该在 p33 不在 p34，改 pages 并补 `provenance_note` | 12 张卡 locator 与 pages 全部对上 |
| 8 | 写 `notes.md`（骨架/主定理/接口/核对与勘误/不懂）、`terms.tsv` 27 条、`excerpts.md` 4 段、`errata.tsv` 2 条 low、`trace.md` 13 条、`workflow.md` | 训练数据三件（cards + notes + terms）齐；trace 13 条含 4 条弯路 |
| 9 | 跑三件质检并修：`lint_cards.py --max-pages 89 --strict`、`verify_pages.py --strict`、`term_index.py check` | 见 §3；lint 由「缺 notes.md」2 错修到 0 error |

## 2. 哪一步最耗时、哪一步最易错

- **最耗时：第 3 步通读 + 第 5 步建引文库**，合计约七成时间。89 页里 §3 占了一半以上（(3.1)–(3.80)），而卡片真正用到的只有 (3.3)(3.4)(3.6)(3.7)(3.23)(3.24)(3.26)–(3.31)(3.52) 等十几条；把 §3.5.1、§3.7、§3.9 的枝节读完花了很久，收益主要是「知道哪些不该建卡」。
- **最易错：页码**。三个具体坑：①PDF 与印刷页差 1，`p.34` 与 `p.33` 一字之差就整条出处作废；②节标题页 ≠ 该节内容页（§3.2 标题在 p34，而关于「除以 $\hat G_{\mathbb C}$」的关键句在 p33 末）；③同一句可能同时出现在两页（`the appropriate boundary condition for n D3-branes ending on a` 在 p54 与 p75 都有，是 §4.1.1 复述 §3.4.3），pages 区间只要含任一命中页就算过，但 anchor 必须写**主出处**那一页。
- 第二易错是**符号**：$\gamma$ vs $\tau$、$X/Y$ 在 §2.1 与 §2.3 之间互换、$H$ 既是子群又被误写成流形（E1）。这类错 lint 查不出，只能靠「写卡时回原文那一页再读一眼」。

## 3. 重做会怎么改

1. **先建引文库再读书**：先用脚本把 89 页切成「式号索引」（正则抓 `(x.y)` 与页码），读书时随手把候选句丢进 `q*.txt`，比读到一半再回头找句快得多。
2. **卡片顺序改成「推导卡先行」**：这次先写概念卡，结果推导卡要反复回改概念卡的 formulas（例如 $\gamma$ 的记法、$s$ 与 $(s-n)/2$ 的层次）。下次先写 4 张推导卡（论证链是骨架），概念卡只做「定义 + 主定理」的封装，回改会少一半。
3. **每张卡写完立刻跑一次 `verify_pages --strict`**，不要攒到 13 张一起跑；这次第 7 步才发现 p34→p33，若逐卡跑能早半小时发现。
4. **§3.5.1、§3.9 只读结论**：这两节的细节（n=3=2+1 的三流形逐参数对比、$T^\rho_\ell$ 的正则化 holonomy）对卡片贡献很小，重做时只读每节首末段，省下的时间给 §4.4（那里的零子空间论证才是第 4 张推导卡的全部内容）。
5. **保留 `external/checkq.py` 与 `q*.txt`**：它们不是交付物，但是「quote 可核验」这一步的可复现证据；重做时同一脚本能直接复用，且能防止把「记得的句子」当成原文。

## 4. 交付清单自查

- 概念卡 9 张（`osp-boundary-superconformal`、`infinite-dimensional-gauge-group`、`boundary-moment-map-shift`、`nahm-moduli-hyperkahler`、`nahm-moduli-complex-orbit`、`sourced-nahm-equation`、`pole-ordering-condition`、`selfdual-three-form-bc`、`neumann-dual-pole`）
- 推导卡 4 张（`b-matrix-to-bc-family`、`moment-map-shift`、`nahm-moduli-to-orbit`、`selfdual-form-from-null-subspace`）
- `terms.tsv` 27 条；`excerpts.md` 4 段（p7/p10/p45/p60）；`errata.tsv` 2 条 low（E1、E2）；`notes.md` 含骨架 40 余节、主定理 20 条、接口 8 篇判断、核对与勘误（外部来源 6 行 + 勘误 2 条）、不懂 5 条；`trace.md` 13 条（弯路 4 条）。
- 未跑：`build_train.py`、`thinking_card.py`、`package.py`、`gglq.py done`（按要求不跑）。
