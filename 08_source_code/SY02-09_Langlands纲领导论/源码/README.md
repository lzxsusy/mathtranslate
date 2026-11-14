# Langlands纲领导论（SY02-09）：中文译注本

完整译本覆盖原 PDF 全部 198 页：课程介绍（原第 1–2 页）及第 1–23 讲（原第 3–198 页）。成品 PDF 共 **151 页**，含 ElegantBook 封面、目录、附录 A/B 与中文索引。

本轮（2026-11-14）按 v2.0 施工标准完成第三轮复核：逐页对照原稿校订译文、补学生向译注、登记原稿笔误。

## 译文与校订

- `main.tex` 为主文件；`chapters/` 含课程介绍与 23 讲译文，共 24 个文件。
- 299 个原书编号对象严格显示原书的「节号.序号」；跨讲引用附讲号以区分同号对象。原书 10 个未编号练习保持未编号。
- 原书 87 节及讲—节层级保留。目录、书签、内部引用与中文索引页码可点击；逐讲参考文献保留英文。
- 逐页对照 198 页原稿核对公式：正文可信、公式一律回页面图像逐符号核对。发现译文错误者改正文；发现原稿笔误而译文已按正确写法处理的，在源码中以 `% [Tutor Note: …]` 就地登记，并在附录 B 汇总。

## 译注（本轮新增）

- 概念首次出现处加脚注式译注：`\znote{…}` 带可追溯来源，`\znoteplain{…}` 仅据上下文推断并明示无外部依据。
- 全书中译注 **144 条**（126 条 `\znote` + 18 条 `\znoteplain`），原稿笔误登记 **146 条**。
- 附录 A《译注来源总表》按讲列出每条译注的概念、位置、来源等级与出处；附录 B《原书笔误与存疑登记》列出 Tutor Note 汇总。两份附录由 `../work/gen_appendix.py` 从 `../work/notes/notes_*.tsv` 全量重生成，不手改。
- 来源分级依 v2.0 §2.5：A 级为本讲参考文献所列教材与原始论文，B 级为 nLab、Stacks Project、MathWorld、DLMF 等，I 级为本库既有译注；无依据者只能写「译者按（上下文推断，无外部依据）」。

## 字体与编译

交付 PDF 的全部字体资源均已嵌入，阅读无需另装字体。重新编译需要 XeLaTeX、ElegantBook 所需宏包、`unicode-math`、`newcomputermodern`、`imakeidx` 及相应字体；字体文件不另行打包分发。

在本目录运行 `build.ps1`，脚本建立 `build/` 并依次运行 XeLaTeX、makeindex、XeLaTeX、XeLaTeX，结果为 `build/main.pdf`。手动编译：

```text
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
makeindex -o build/main.ind build/main.idx
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

手动执行前须建立 `build` 目录。无需 Biber：参考文献按原书逐讲分组直接排版。压缩包不包含编译或渲染缓存。

## 核查文件

`terminology.tsv` 保存 224 项中英术语（本轮新增 30 项，另有 2 项术语在全稿统一：「分圆域」「射有限」）；`page-map.tsv` 保存 198 个原页与译本页标记的对应；`reference-map.tsv` 保存 299 个原编号对象的映射。每个原页在源码中有 `sourcepage` 标记。

`audit/` 保存前两轮的原页检查、编号、公式、书签、图片、字体与最终页面检查记录：`REVIEW_PLAN.md`（修改计划）、`REVIEW_REPORT.md`（详细结果与留白说明）、`revisions.diff`（上一版到本版的正文与排版修订）、`compile-final.log`（编译日志）、`validation.json`（绑定交付 PDF 的 SHA-256）。

本轮校订记录不放在 `audit/`（那是上一轮的交付物，保持原样），而是放在 `../work/reports/ch01–ch23.md`：每讲一节，含校订清单表（位置/类型/原文/改文/依据）、译注清单表、编译自检结果与遗留问题。

章末参考文献后的自然留白保留：这与原书讲次结构及模板每讲另起一页有关。
