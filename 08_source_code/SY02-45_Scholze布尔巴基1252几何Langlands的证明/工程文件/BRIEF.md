# BRIEF · SY02-45

| 项 | 内容 |
| --- | --- |
| 编号 | **SY02-45** |
| 原名 | *Geometric Langlands [after Gaitsgory, Raskin, …]* |
| 作者 | Peter Scholze |
| 性质 | 布尔巴基讨论班报告（Séminaire BOURBAKI，78e année 2025–2026，n° 1252，Mars 2026） |
| 底本 | 56 页（印刷页 1–56，页眉 `1252–NN`），12 节 + 参考文献；pdfTeX 排版，无插图 |
| 文本层 | 可用，但连字与上下标粘连严重（`XOC` = $X_{\mathcal O_C}$，`πet`+`1` = $\pi_1^{\mathrm{et}}$）；**公式一律对页面图核** |
| 规模 | 英文约 13.4 万字符；编号条目 **57 条**（注 32、定理 14、定义 3、猜想 2、推论 2、假设 1、问题 1、命题 1、例 1） |
| 体例 | 原文条目格式为**类型在前**：`Remark 2.1. — …`、`Theorem 2.2. — …`（不是 Bourbaki 传统的「2.1. Theorem.」） |
| 译本 | article 类（A4，11pt，xelatex+ctex），12 个 `\section` + 1 个 `\section*{参考文献}`，共 13 个 section 文件 |
| 术语 | `工程文件/work/glossary.tsv` 129 条，开工前冻结；依据代号 L（本库冻结）/A（权威通行）/I（待裁定） |
| 状态 | **已交付 v1.0（2026-11-27）**：13 节全译、xelatex 0 error、45 页；57 条编号条目对账；术语 123 条冻结且 check_terms 0 违规；独立审校（2 严重 + 4 一般问题已全部整改清零，见 `reports/审校.md` §7）+ 12 页抽检；资料卡五件套 + leanstmt gap 卡 1 张；文献 56 条外核 |

## 1. 结构（节 / 印刷页 / 条目数 / 文件 / 译手）

| 节 | 标题 | 页 | 条目 | 文件 | 译手 |
| --- | --- | --- | --- | --- | --- |
| 1 | 引言 | 1–11 | 9 | `s01-intro.tex` | t01 |
| 2 | 几何 Langlands 等价 | 11–19 | 13 | `s02-glc.tex` | t02 |
| 3 | $\Bun_G$ 上的层 | 19–23 | 4 | `s03-sheaves.tex` | t03 |
| 4 | 局部系统的叠 | 23–25 | 0 | `s04-locsys.tex` | t03 |
| 5 | 谱作用 | 25–33 | 11 | `s05-spectral.tex` | t04 |
| 6 | $G=\mathbb G_m$ | 33–35 | 1 | `s06-gm.tex` | t05 |
| 7 | Beilinson 谱投影子 | 35–38 | 1 | `s07-projector.tex` | t05 |
| 8 | Frobenius 的迹 | 38–40 | 3 | `s08-frobenius.tex` | t05 |
| 9 | Whittaker 系数 | 40–45 | 7 | `s09-whittaker.tex` | t06 |
| 10 | Eisenstein 级数 | 45–49 | 2 | `s10-eisenstein.tex` | t07 |
| 11 | Kac–Moody 局部化 | 49–52 | 5 | `s11-kacmoody.tex` | t07 |
| 12 | 尖点形式 | 52–53 | 1 | `s12-cusp.tex` | t08 |
| 13 | 参考文献 | 53–56 | 0 | `s13-refs.tex` | t08 |

## 2. 这本书为什么重要

Gaitsgory–Raskin 等 2024 年几何 Langlands 猜想证明（五篇论文、上千页）目前唯一一份由 Scholze 本人撰写的权威路线图。第 5–12 节依次是谱作用、Beilinson 谱投影子、Frobenius 迹、Whittaker 系数、Eisenstein 级数、Kac–Moody 局部化、尖点形式、合拢，正是 `12_sandbox/` 形式化项目缺的那张依赖图。翻译方针：**宁可句子朴素，不可模糊「由此可得」**。

## 3. 质量承诺（逐条验收）

1. 不臆造、不补写、不美化；原文含糊/错误照译 + `\yizhu` 译注（只许术语背景/原文省略/原文笔误三类）。
2. 逻辑连接词按词义分译，禁止一律「因此」。
3. 公式零容忍：每页对照 `pages/pNNN.png`。
4. 编号零手写：条目用环境，编号由 LaTeX 计数器生成；全库无 `\ref/\label/\eqref/\cite`。
5. 一句 ≤60–70 汉字，中英之间半角空格，全角标点。
6. 段落与编号条目 1:1 对账（`条目总表.tsv` + `tools/check_sections.py`）。
7. 独立审校（`reports/审校.md`），严重项必须清零。
8. `tools/check_terms.py`：glossary 覆盖率、异译黑名单为 0、术语使用计数表。
9. 人眼抽检 ≥12 页（`work/抽检记录.md`）。
10. 参考文献逐条外核（`work/refs.tsv` → 资料卡 04）。

## 4. 交付清单

- [ ] `源码/` 13 个 section 文件，`xelatex` 三遍 0 error
- [ ] `成品/SY02-45_...pdf`
- [ ] `工程文件/reports/s01..s13.md` + `审校.md`
- [ ] `工程文件/work/{glossary.tsv,条目总表.tsv,术语使用统计.txt,抽检记录.md,通读笔记*.md,TASK-translator.md}`
- [ ] `工程文件/tools/{check_sections.py,compile_section.py,check_terms.py}`
- [ ] `资料卡/00-速览.md,01-结果清单.md,02-论证地图.md,03-条款索引.md,04-术语文献勘误.md`
- [ ] `datasets/leanstmt/cards/statements/` 至少 1 张 gap 对齐卡，`lint_cards.py --strict` 0 error
- [ ] `03_translations_meta/SY02-45/投稿信息.md`、`RELEASE_REGISTER.csv` 一行
- [ ] 仓库闸门：`make_stats.py --check`、`tools/check_numbers.py`、`tools/build_norm.py --check`
- [ ] 推送 atomgit + origin

## 5. 已知风险与缺口

1. **漏译风险集中在页边界**：`\srcpage` 锚若漏插，跨页段落最容易被并段。`check_sections.py` 已把「范围内每页必须有锚」设为硬检查。
2. **条目统计口径与任务书不一致**：任务书说「约 89 条（定理 34/注 38/…）」，实测 **57 条**（注 32/定理 14/…）。原因：任务书的统计把行首交叉引用（如 `Conjecture 1.5 would be even more precise…`）也算进去了。以 `条目总表.tsv` 为准，差异记入 `资料卡/04`。
3. **三套 setting 的术语**（Betti / de Rham / étale）在 §3–§7 反复切换，误译一处会串错整段，glossary 已固定译名。
4. **Gestalt / shtuka / transmutation / oper / suave / prim / Hecke-lisse** 保留英文（本库与香蕉空间均无稳定中文名），首现括注。
5. 若 17:00 前未收口，逐节标 `partial` 并在本文件登记缺口，不虚报。

## 6. 可复用清单（下一本可直接拿去用）

| 件 | 路径 | 可复用性 |
| --- | --- | --- |
| 自检三件套 | `工程文件/tools/{check_sections.py,compile_section.py,check_terms.py}` | **高**。`check_sections.py` 的六项检查（页锚覆盖、环境配对、$ 配对、禁用命令、条目类型序列、禁手写编号）对任何「单篇论文/讲义 → 编号条目逐条对账」的工程都适用，只需改 `工程文件/work/sections.json` 的路径与 `PAGES_DIR`；`compile_section.py` 单节隔离编译可让译手自查而不互相干扰；`check_terms.py` 的「覆盖率 + 异译黑名单 + 计数表」是术语冻结协议的执法工具 |
| 术语生成器 | `工程文件/work/make_glossary.py` | **高**。内置条目表 + 扫描原文求首现页；换工程改候选词表与 `src/pNNN.txt` 路径即可。**注意**：本文未出现的词条会因首现页空而被误判，需像本工程那样另存 `glossary-本文未用.tsv` |
| 条目总表生成器 | `工程文件/work/make_items.py` | **高**。正则「类型名 + 节号.序号 且节号==当前节」+ 同键只取首见，能避开行首交叉引用的误计（这是本工程 89 vs 57 的根因） |
| 切分脚本 | `工程文件/work/split_sections.py` | 中。节标题硬编码，换书要改 `HEADS` |
| 抽检工具 | `工程文件/tools/sample_pages.py` | **高**。用编译稿页边 `1252--NN` 边注把原文页映射到编译稿页码，再 `pdftoppm` 渲染并与原文页图并排；换工程只改页眉正则与两处目录 |
| 文献外核 | `工程文件/tools/check_refs.py` | **高**。`extract` 依赖 `list` 环境的 `\item` 排版（本工程 s13 的写法），`verify` 走 arXiv API + Crossref，输出 10 列 TSV；换工程改期刊缩写映射与书目正则 |
| 译手契约 | `工程文件/work/TASK-translator.md` | **高**。含逐页看图流程、连字黑名单、条目环境映射表、十四个常见坑（含 `\srcpage` 是 `\marginpar` 不能写进 `$…$`、`\Fr`/`\D` 宏不存在等实测坑）、四栏交付报告格式。已在 SY02-45 上被 8 个译手实际使用并验证 |
| 香蕉空间增量 | `SY02-41_…/工程文件/work/术语外部核对_香蕉空间.md` 末尾「六、SY02-45 增量词表」 | **中**。19 条增量裁定 + 5 条「不译」建议（`Hecke-lisse`/`suave`/`prim`/`Gestalt`/`transmutation`），已标注「**建议并入 termbase**」，等 Lead 统一并入 `TERMS.tsv` |
| 资料卡生成器 | `工程文件/tools/{gen_card04.py,gen_card04_refs.py}` | 中。前者从 glossary 生成 ①，后者从 refs-check 生成 ③；都靠 `## ①/## ③` 标题定位截断，换卡要改锚点 |

**新增术语条目**（123 条中本文首次确立、可供后续几何 Langlands 工程复用的）：`Gestalt`（不译，首现括注「格式塔」）、`transmutation`（不译，待裁定）、`Hecke-lisse`（不译）、`suave`/`prim`（Heyer–Mann 术语，不译）、`pinning`（钉扎）、`Theta 特征`、`对偶化层`、`归纳投射概形`、`归纳完备化`、`外张量积`、`轨迹`（trace 的范畴化用法）、`保守性`、`分歧群`、`非挠素数`、`泛局部无环`、`粗糙模空间`。全部落在 `工程文件/work/glossary.tsv`，依据代号 A/I 者可被下一本直接继承。
