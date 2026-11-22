# workflow — 本篇实际是怎么做的

工作对象：arXiv:0807.3720，172 页（PDF 页序），Gaiotto–Witten。
产出：14 概念卡 + 6 推导卡 + notes.md / terms.tsv / excerpts.md / errata.tsv / trace.md / workflow.md，两条自检 exit 0。

## 1. 实际顺序（含每步产出）

| # | 步骤 | 产出 | 用时量级 |
|---|---|---|---|
| 1 | 读 TASK.md → BRIEF.md → cards/SCHEMA.md → `out/19_ggl19/` 整个目录 | 知道交付物清单、字段名与「密度基准」（19 是 12 卡 + 23KB notes） | 中 |
| 2 | 读 `tools/` 的 lint_cards.py、verify_pages.py、term_index.py 源码 | 把机检规则逐条抄成清单：quote 12–120 字符、A 类必须 quote、errata 9 列、notes 外部来源 ≥3 行等 | 中（很值） |
| 3 | 跑 `python tools/xref.py 22` | XREF.md：v1 唯一版本、INSPIRE 791356、ATMP 13 (2009) 721–896、Zbl 1206.81082 | 小 |
| 4 | 读目录页 + §1 + 每节首段，定主线 | notes §2 骨架表；决定精读哪 8 个节 | 小 |
| 5 | 精读 §2.1–2.4（p007–p029） | brane 构造、两约束、S-对偶作用、monopole R-荷公式 (2.15)–(2.23) | 大 |
| 6 | 精读 §3.3–3.4（p050–p075） | $T(SU(n))$、$T_\rho$、$T^\rho_{\rho'}$、ungauging、(3.13) | 最大 |
| 7 | 精读 §4.1–4.3、§5.1（p082–p107） | $T(G)$、Table 1、SO/Sp 的 good 条件 | 中 |
| 8 | 精读 §6.1/6.3、§7.1–7.2、§8（p122–p168） | 三类 involution、Table 2/3、O3 四型、$SL(2,\mathbb Z)$、$(p,q)$ 五膜 | 大 |
| 9 | 写 14 张概念卡（先概念后推导） | `cards/concepts/*.json` | 大 |
| 10 | 写 6 张推导卡 | `cards/derivations/*.json` | 中 |
| 11 | 写 notes.md（骨架/主命题/接口/记号/不懂/枝节/核对与勘误） | notes.md | 大 |
| 12 | 写 terms.tsv、excerpts.md、errata.tsv、trace.md、workflow.md | 五个配套文件 | 中 |
| 13 | status: draft → dev，跑 lint_cards + verify_pages | 两条 exit 0 | 小 |

## 2. 哪一步最耗时

**§3.3–3.4（p050–p075）**。理由：这一段是全文的技术核心，(3.13) 的推导要同时处理「ungauging」「五膜排序」「哪一侧耦合 Coulomb 分支」三件事，而原文用了 25 页、大量依赖图 38/49 的构型图；光靠文字无法复原，必须把 p070–p073 反复对读，才能把 6 个推导步骤排对。第二耗时的是 §3.3.2 的 Nahm 极点/Young 图/幂零共轭类三者的对应——它是三套语言（表示论、五膜、quiver）的交叉点，任何一处页号或下标写错，下游的 $T_\rho$、$T^\rho$、$T^\rho_{\rho'}$ 三张卡全错。

## 3. 哪一步最易错

1. **页码**：本库要求 PDF 页序，而原文页脚印的是印刷页（PDF = 印刷 + 1）。一旦在心里做换算，就会系统性偏移一页；上一班（out/19）就栽在这里。对策：所有页号只从 txt 文件名取，绝不从页脚读。
2. **quote 的页归属**：verify_pages 只认「单页内」的子串，跨页的句子会被判失败。对策：写卡时先把候选 quote 批量跑一遍归一化匹配（我写了个一次性脚本 `_check.py`，跑完即删），确认每句命中唯一一页，再写进 JSON。
3. **上标/下标方向**：$T_\rho$ 与 $T^\rho$、$T^\rho_{\rho'}$ 与 $T^{\rho'}_\rho$，原文的排版在 OCR 后容易看反。对策：用分支公式反推（见 trace 第 5 条），并把推断标成 provenance B。
4. **errata 的置信度**：high 要求两处独立出处，很容易把同一页的两句话当两处。对策：宁低勿高，本篇只给 medium 与 low。
5. **控制台编码**：GBK 控制台 print 中文会 UnicodeEncodeError。对策：Python 输出 `PYTHONIOENCODING=utf-8` 重定向到文件再读，绝不 print 中文。

## 4. 重做会怎么改

1. **先写「句子—页号」表，再写卡**：这次是边读边写卡，导致同一页（p073、p168）被反复回读。重做时先建一个 `page → 可用引文` 的清单（我已经在压缩笔记里维护了一份），写卡时直接查表，能省约 1/3 的读页时间。
2. **推导卡先列 step 骨架、再填 why**：现在 6 张推导卡是先写正文再补 provenance，有些步骤的 `why` 写得比 `text` 还长。重做时先把 5–6 个 locator 排好（对应原文的几个式子），再填文字，结构会更稳。
3. **Table 类内容统一标 D 并在 notes 里给整表**：这次 Table 1/3/4 的处理方式不一致（Table 1 并入卡、Table 3 只在 notes、Table 4 进卡）。重做时一律「卡里只引用一行、notes 里给完整表 + 页码」，便于以后查。
4. **少读算例，把省下的时间给 §4.5 与 §7.1.2**：这两节我完全没读，notes 的「不懂」清单里只能写「没读」；其实它们与 $q_R\le0$ 判据和 monopole/orientifold 有关，值得读。
5. **早点跑 lint**：我在写完 20 张卡后才第一次跑 lint，虽然有 note 缺失的两条包级错误，但卡片本身一次过。若更早跑一次骨架（一张卡），可以更早发现 summary 的 120 字上限与 quote 长度限制。

## 5. 与其它班次的分工

- 只写 `out/22_ggl22/`。`pdf/`、`txt/`、`tools/`、`cards/SCHEMA.md`、`BRIEF.md`、`MANIFEST.tsv`、`state.json` 与其他 `out/*` 一律未改。
- 一次性辅助脚本 `_check.py`、`_qc.json`、`_lint.txt`、`_vp.txt` 用完即删，不留在交付目录。
- 未做 git commit / push / 打包。
