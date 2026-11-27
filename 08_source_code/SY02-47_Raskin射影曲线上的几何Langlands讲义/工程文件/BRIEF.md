# BRIEF · SY02-47

| 项 | 内容 |
| --- | --- |
| 编号 | **SY02-47** |
| 原名 | *Notes for “Geometric Langlands for Projective Curves”* |
| 讲授 / 笔记 | Sam Raskin 讲授；Lin Chen 笔记 |
| 性质 | 暑期课程讲义（2025 年 7 月 7–11 日，共五讲） |
| 底本 | 18 页（印刷页 1–18），pdfTeX 2025-07-20 排版；公开副本 `https://www.math.columbia.edu/~okounkov/Sam_lecture_notes.pdf` |
| 文本层 | 可用；但公式下标、上标与连字有粘连，**公式一律对页面图核** |
| 规模 | 英文约 3.3 万字符；五讲、13 个小节、1 幅手绘示意图、1 个参考文献页 |
| 体例 | 讲义体：`1.1.` 起小节，条目用 `Definition / Construction / Remark / Proposition / Theorem / Corollary / Exercise / Question / Conjecture` 环境 |
| 译本 | article 类（A4，11pt，xelatex + ctex），六个 section 文件：五讲 + 附录 |
| 术语 | `工程文件/work/glossary.tsv`，开工前冻结；依据代号 A（权威）/ B（白名单）/ I（本库）/ L（本库冻结） |
| 状态 | **v1.3 勘误详注与 18 卡**（2026-11-27）：五讲全译、xelatex 三遍 0 error、24 页；译注 24 条；独立审校 S1–S8/G1–G12 与第二轮 9 条意见已处理；资料卡五件套、`05-原文勘误详注.md`（10 页）与 18 张结构化卡已生成；五道闸门通过 |

## 1. 结构（讲 / 节 / 印刷页 / 文件）

| 讲 | 节 | 标题 | 页 | 文件 |
| --- | --- | --- | --- | --- |
| 1 | §1.1 | 层论 | 2 | `s01-intro.tex` |
| 1 | §1.2 | 几何类域论（交换情形） | 2–4 | `s01-intro.tex` |
| 1 | §1.3 | 非交换理论（$G=\mathrm{PGL}_2$） | 4–6 | `s01-intro.tex` |
| 2 | §2.1 | 尖点性 | 6–7 | `s02-cusp.tex` |
| 2 | §2.2 | 系数 | 7–8 | `s02-cusp.tex` |
| 3 | §3.1 | 系数（续） | 8–9 | `s03-coeff.tex` |
| 3 | §3.2 | Fourier 变换 | 9–10 | `s03-coeff.tex` |
| 3 | §3.3 | 几何 Langlands 对应（$\mathrm{PGL}_2$） | 10–11 | `s03-coeff.tex` |
| 4 | §4.1 | Hecke 函子 | 12–14 | `s04-hecke.tex` |
| 4 | §4.2 | Hecke 性质 | 14–15 | `s04-hecke.tex` |
| 4 | §4.3 | 几何 Langlands 对应（一般 $G$） | 15–16 | `s04-hecke.tex` |
| 5 | §5.1 | Whittaker 系数 | 16–17 | `s05-whittaker.tex` |
| 5 | §5.2 | 范畴化几何 Langlands 等价 | 17–18 | `s05-whittaker.tex` |
| 附录 | A–D | 参考文献 / 译名对照 / 原文勘误 / 底本与版权 | 18 | `s06-refs.tex` |

## 2. 这份讲义为什么重要

这是 Raskin 在 2025 年暑期学校讲几何 Langlands 的五讲纲要，篇幅只有 18 页，却把
「$\mathrm{GL}_1$ 的 Deligne 构造 → $\mathrm{PGL}_2$ 的尖点性、系数与 Fourier 变换 →
一般约化群的 Hecke 特征层 → Whittaker 系数与范畴化等价」这条主线完整走了一遍。
它不追求证明细节，而是把每个定理的**精确陈述、归一化与互相依赖**摆出来，适合作为
读 2024 年五篇证明论文（GLC I–V）之前的路线图。翻译方针：**术语先冻结，公式零臆造；
原文的笔误照录并加注，不静默改。**

## 3. 质量承诺（逐条验收）

1. 不臆造、不补写、不美化；原文含糊或错误处照译，并加 `\yizhu` 译注。
2. 译注只写三类：术语背景 / 原文省略 / 原文笔误；每条都能追溯到 A/B/I 级来源。
3. 公式零容忍：每个公式对 `fulltext.txt` 与页面图核对，尤其上下标与 $\otimes$、$\boxtimes$。
4. 编号零手写：条目用环境，编号由 LaTeX 计数器生成；交叉引用用 `\eqref` / `\ref`。
5. 一句 ≤60–70 汉字；中英之间半角空格；全角标点；不用「被……所……」。
6. 术语按 `work/glossary.tsv` 冻结；异译黑名单为零。
7. 独立审校（`reports/审校.md`），严重项必须清零。
8. 人眼抽检至少 8 页（`work/抽检记录.md`）。
9. 参考文献逐条外核（`work/refs.tsv`）。
10. 成品 PDF 与源码一致；资料卡五件套齐全。

## 4. 交付清单

- [x] `源码/` 六个 section 文件，`xelatex` 三遍 0 error
- [x] `成品/SY02-47_..._中译注本.pdf`
- [x] `工程文件/work/{通读笔记.md,疑点清单.tsv,glossary.tsv}`
- [x] `工程文件/work/refs.tsv`、`工程文件/work/抽检记录.md`（12 页人眼抽检）
- [ ] `工程文件/reports/审校.md`（独立子代理）
- [x] `资料卡/00-速览.md` … `04-术语文献勘误.md`
- [x] `datasets/raskin_glc/cards/` 18 张 JSON 卡（含 7 张 correction），`card_spec_check.py --set raskin_glc --strict` hard=0
- [x] `资料卡/05-原文勘误详注.md` 与 `成品/SY02-47_原文勘误详注.pdf`（10 页，原文/修正/推导/外部佐证）
- [x] `03_translations_meta/SY02-47/投稿信息.md`、`RELEASE_REGISTER.csv` 一行
- [ ] 仓库闸门：`make_stats.py --check`、`tools/check_numbers.py`、`tools/build_norm.py --check`
- [ ] `conflict_report.py check --delivery` P0 = 0
- [ ] 推送 AtomGit + Gitee 镜像

## 5. 已知风险与缺口

1. **公式粘连**：底本文字层把 $\Bun^d_B$ 与 $\Bun_B^d$ 混排，个别上下标需对页面图确认；
   已在 `work/疑点清单.tsv` 逐条登记。
2. **原文笔误**：Abel–Jacobi 纤维写成 $\Gamma(X,L)\setminus 0$（应为 $\mathbb P\Gamma$）、
   $B H^1(X,L)$（应为 $B H^0$ 或 $R\Gamma[1]$）、$\sigma^{(d)}$ 的 perverse/lisse 互换、
   $\Rep(G)$ 应为 $\Rep(\widehat G)$、Vilonen 拼写等；正文照录并加注，附录 C 汇总。
3. **通用秩公式的 $d_i$ 约定**：原文称 $d_i$ 为 $G$ 的指数；按通常指数（$\mathrm{PGL}_2$ 为 1）
   公式给 1，按不变多项式次数（$\mathrm{GL}_2$ 为 1, 2）则给 $2^{3g-3}$。已加译注说明，
   **不擅自改公式**，留待审校与资料卡 04 讨论。
4. **手绘图**：Figure 1 为原文手绘，重绘为示意图；不追求与原图逐笔一致，只保留
   「两个连通分支 + 底部半稳定开子叠 + 上方 $\Bun^d_B$ 分层」的结构。
5. **术语风险**：perverse sheaf 统一译「反常层」（不用「错致层」）；lisse 保留英文；
   cuspidal 译「尖点」；Hecke eigensheaf 译「Hecke 特征层」。

## 6. 可复用清单（下一本可直接拿去用）

| 件 | 路径 | 可复用性 |
| --- | --- | --- |
| 译注宏 | `源码/preamble.tex` 的 `\yizhu{内容}{类别与依据}` | 高。脚注自动带「译注」标记，类别与来源等级写在参数里 |
| 页锚 | `\srcpage{n}` 边注 | 高。把底本印刷页映射到编译稿页边，便于抽检 |
| 通读笔记 | `work/通读笔记.md` | 中。按「主旨—论证地图—体裁—阅读顺序」四段写，换书改内容 |
| 疑点清单 | `work/疑点清单.tsv` | 高。六类疑点（概念/术语/记号/跳步/笔误/歧义）+ 状态列，`未解=0` 才准开译 |
| 术语表 | `work/glossary.tsv` | 高。沿用 SY02-45 的几何 Langlands 词表，新增本讲义特有词条 |
| 编译脚本 | `工程文件/tools/build.sh` | 高。三遍 xelatex + 日志过滤，换工程只改文件名 |
