# SY02-38《朗兰兹纲领入门课程讲义》中文译注本 · 作战计划（BRIEF）

<!-- TRANSLATION-STANDARD:v2.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.1** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（SY02-09 / SY02-24 术语表），再查 nLab / Stacks Project 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制，权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：`04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md

体例看 `STYLE_GUIDE.md`（必读，先读完再动手）。本文件只讲分工、进度与协作。

## 目标

把 Anschütz《Lecture notes for an introductory course on the Langlands program》（2020-07-22，103 页，含 Ben Heuer 三讲）完整译成中文译注本，交付：成品 PDF + 可独立编译的 LaTeX 源码 + 通读笔记 + 疑点清单 + 术语表 + 分章报告 + 资料卡（数据集 `datasets/anschuetz/`）+ 思考链（`09_thinking/` 登记）+ 工程总结。

- 登记号：**SY02-38**（主工程发号，按 `make_stats.py` 的 THEMES）；口径登记号 **LL-E02**（`04_playbook/21_Arthur与吴宝珠讲义包_选题_2026-11.md`、`_meta/文献补遗.tsv` 中的选题编号，只记入 BRIEF 与 RELEASE_REGISTER 备注）。
- 底本权利：作者 Johannes Anschütz（Bonn），2020-07-22 修订稿；讲义性质，权利归原作者；本库按「L2 公开·受限（可撤下）」处理。

## 工程根目录

```
C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-38_朗兰兹纲领入门课程讲义\
  工程文件\            00_开工必读.md、BRIEF.md、STYLE_GUIDE.md
  工程文件\work\       pages\pNNN.txt、fulltext.txt、chunks.json、通读笔记.md、疑点清单.tsv、glossary.tsv、definitions.tsv、reports\
  源码\               main.tex、chapters\preface.tex、lectureNN.tex、appendix_refs.tex
  成品\               SY02-38_朗兰兹纲领入门课程讲义_中译注本.pdf
```

## 分工（Lead 统一编译与交付）

| 成员 | 负责 | 输出 |
|---|---|---|
| Lead | 讲 1、2、3、4、5、6、9、11、12 + 前言 + 参考文献 + main.tex + 编译 + 资料卡 + 登记 + 上传 | `源码/chapters/lecture01–06,09,11,12.tex` 等 |
| tr1（Heuer 组一） | 讲 7、8 | `源码/chapters/lecture07.tex, lecture08.tex` |
| tr2（Heuer 组二） | 讲 10 | `源码/chapters/lecture10.tex` |

## 章节表（页 = PDF 页 = 原书页）

| 讲 | 中文标题 | 页 | 作者 |
|---|---|---|---|
| 1 | 关于本讲稿的说明 | 2 | Anschütz |
| 2 | 一般性介绍 | 3–10 | Anschütz |
| 3 | 从模形式到自守表示 I | 11–23 | Anschütz |
| 4 | 从模形式到自守表示 II | 24–32 | Anschütz |
| 5 | 从模形式到自守表示 III | 33–45 | Anschütz |
| 6 | 新形式的 Langlands 互反 | 46–54 | Anschütz |
| 7 | 模曲线作为椭圆曲线的模空间 | 55–61 | Ben Heuer |
| 8 | Eichler–Shimura 关系 | 62–69 | Ben Heuer |
| 9 | 附着于新形式的 Galois 表示 | 70–78 | Anschütz |
| 10 | 权 1 形式的 Galois 表示 | 79–87 | Ben Heuer |
| 11 | 一般群的 Langlands 纲领 I | 88–93 | Anschütz |
| 12 | 一般群的 Langlands 纲领 II | 94–101 | Anschütz |
| — | 参考文献 | 102–103 | — |

## 质量标准（交付闸门，逐条可查）

1. 三遍 xelatex 编译无 error，未定义引用 0、重复书签 0、Overfull ≤ 5（每页）、缺字 0。
2. 术语全部并入 `源码/terminology.tsv` 与 `work/glossary.tsv`，两处一致。
3. 每讲有页标记注释，页覆盖率 100%（p2–p101）。
4. 疑点清单「未解」= 0，每条有依据等级与「下一步」。
5. 译注每条带 `[来源：…]` 或 `[译者按（无外部依据）：…]`。
6. 登记：`RELEASE_REGISTER.csv` 一行 + `03_translations_meta/SY02-38/` 三件（工程登记、底本信息、交付清单）。
7. 资料卡：`datasets/anschuetz/` 不少于 12 张，每张带页码与 verification 段，`tools/ds_lint.py` 通过。

## 进度

- [x] 通读（103 页，2026-11-26 完成）→ `work/通读笔记.md`、`work/疑点清单.tsv`
- [x] 术语冻结（`work/glossary.tsv`、`work/definitions.tsv`）
- [x] 讲 1–12 译文（Lead 讲 1–2；tr-heuer-1 讲 7–8；tr3 讲 3–4；tr4 讲 5–6；tr5 讲 9；tr-heuer-2 讲 10；tr6 讲 11–12）
- [x] 全书编译与校订（xelatex 三遍：0 error、0 Overfull，成品 101 页（38 条术语索引）；第 2 轮四路校对 104 条意见已处理，中文粗体生效）
- [x] 资料卡集 `datasets/sy0238/`（53 张：概念 48 + 推导 5；lint 0 error，quote 179 条 0 问题）
- [x] 登记与上传（`RELEASE_REGISTER.csv`、`03_translations_meta/SY02-38/`、AtomGit）
- [x] 译名对齐中文数学社区（`work/reports/译名社区对照.md`；改 `幂幺根`、`埃尔米特对称域` 2 处）
- [x] 四路校对（`work/reports/校对_rev-{a,b,c,d}.md`，104 条）与修稿复编译
- [x] 知识库插件测试反馈（`工程文件/work/reports/kb_plugin_feedback.md`，另见 `09_thinking/chains/SY02-38_本地知识库插件实测反馈.md`）
