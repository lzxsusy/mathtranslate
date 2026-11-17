# SY07-09 陈麟《代数几何讲义 I》中译注本 · 定义与定理资料卡

把 Lin Chen（陈麟）*Notes for Algebraic Geometry 1*（2025 年秋季课程讲义，英文，原书 171 页）整本译为中文，
附来源可追溯的译注、术语英中对照，以及从译注本逐条裁出的**定义/定理资料卡**。

**成品**（按 `COMPLIANCE.md` §4，图书/讲义译文成品 PDF 不随仓发布；`RELEASE_REGISTER.csv` 记「成品不公开」，需要 PDF 请来信索取）

- 中译注本 195 页、定义与定理资料卡 64 页 —— 源 `.tex` 在 `源码/` 与 `工程文件/`，两遍 `xelatex` 即可复现（发行说明见 `成品/SY07-09_交付报告.md`）
- `成品/SY07-09_术语对照表.md`（226 条）
- `成品/SY07-09_交付报告.md`（四组验收与复现）
- `成品/预览-封面.png`、`成品/预览-资料卡.png`

## 底本

- 原书 171 个 PDF 页，**印刷页码 = PDF 页码**（页眉即页码），有文本层但公式需重建。
- 结构：§0 引言（p5–8）+ Part I–VI（§1–§30）+ 附录 A 阿贝尔范畴（p164–170）+ 参考文献（p171）。
- 定理类编号为「节.小节.序号」（如 Definition 0.1.1、Theorem 20.3.2），译文编号与原书逐条对应。
- 页映射表（节 → 原书页）见译注本《译校说明》第二节。

## 结构

```
源码/
  main.tex          装配：扉页 → 译校说明 → 目录 → sec00…sec30 → 附录 A → 附录 B → 参考文献
  preamble.tex      版式、字体、定理族计数器、yizhu 译注环境、数学宏
  frontmatter.tex   扉页与译校说明（底本、页码映射、翻译原则、译注体例、版式差异）
  part1–6.tex       六个 Part 的标题页与 \input
  sec00–sec30.tex   每节一个文件
  appendixA.tex     阿贝尔范畴
  appendix_terms.tex 术语附录（由 工程文件/术语表.tsv 经脚本生成，勿手改）
  references.tex    参考文献
工程文件/
  通读笔记.md        全书结构与各节要点
  疑点清单.tsv       55 条（概念/术语/记号/跳步/笔误/歧义），未解 0
  术语表.tsv         226 条英—中—备注，冻结后正文不得改译名
  译校简报.md        分工与施工细则（标签规则、连字映射、查证工具、自检）
  代数几何资料卡.tex  资料卡源文件
  build.sh           xelatex ×2 → 成品
  tools/
    extract_cards.py 讲义源码 → cards.json（700 条，其中核心 366 条）
    gen_deck.py      cards.json → 资料卡 tex + pdf
成品/
  SY07-09_交付报告.md   四组验收、指标与复现步骤
  SY07-09_术语对照表.md 226 条英中对照
  预览-封面.png / 预览-资料卡.png
```

## 资料卡

一张卡 = 一条编号条目，标题栏「类型 + 原书编号」（如 `定理 20.3.2`），右侧标「§20.3 · 原书 p.114」。
收定义、定理、命题、引理、推论、断言、预备定义、命题—定义 8 类，共 366 条；例、注记、构造、习题、
警告依赖上下文，不入卡，按卡上节号回书查。卡内交叉引用全部换成字面编号，书末附条目索引。

## 指标

| 指标 | 值 |
|---|---|
| 书页数 / 卡页数 | 195 / 64 |
| 译注 | 205 条（逐节 4–8 条） |
| Stacks Project | 123 个不同 tag，逐条核对 |
| nLab | 15 条，均记 Last revised |
| 术语 | 226 条 |
| 编译 | xelatex ×2，0 error，0 Overfull（书） |
| 未定义引用 / 缺字 | 0 / 0 |

## 复现

```
cd 源码 && xelatex main.tex && xelatex main.tex
cd ../工程文件/tools && python extract_cards.py && python gen_deck.py
```

需要 XeLaTeX 与 Windows 自带字体（SimSun / SimHei / KaiTi，资料卡另需 Microsoft YaHei）。
