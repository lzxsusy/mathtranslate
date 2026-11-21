# SY05-29 工程说明

本目录是《朗兰兹对偶 Hitchin 系统的增强镜像对称》中译注本的施工现场。翻译正文在 `源码/`，成品在 `成品/`，过程记录在 `工程文件/reports/`。

## 目录

```text
SY05-29_朗兰兹对偶Hitchin系统的增强镜像对称/
├── 投稿信息.md                  版本登记（原文题名/底本/成品/源码/备注）
├── 成品/
│   └── SY05-29_朗兰兹对偶Hitchin系统的增强镜像对称_中译注本.pdf   （28 页，0.38 MB）
├── 源码/
│   ├── main.tex                 入口（\input preamble → ch0_front → ch1–3 → refs → 附录）
│   ├── preamble.tex             版式 + 中文定理环境 + 218 条原文宏（机械抽取）
│   ├── ch0_front.tex            封面、摘要、译者说明、原书页码对照表、目录
│   ├── ch1_intro.tex            §1 引言
│   ├── ch2_background.tex       §2 背景（2.1–2.5）
│   ├── ch3_enhanced.tex         §3 幂零锥尖端处的增强镜像对称（3.1–3.4）
│   ├── refs.tex                 文献表（52 条，照录原文顺序与标号）
│   ├── app_terms.tex            附录 A 术语表（112 行）
│   ├── _build_pre.py            从原文抽宏区的脚本
│   └── original/                底本 arXiv 源码 HauselICM-arxiv.tex
└── 工程文件/
    ├── BRIEF.md                 任务书与验收标准
    ├── README.md                本文件
    └── reports/
        ├── 01_通读笔记.md        22 页页表 + 逐节要点 + 写卡须知
        ├── 02_疑点清单.tsv       24 行，六类，未解 = 0
        ├── 03_术语表.md          由 app_terms.tex 导出
        └── 04_交付核对.md        交付清单逐条核对
```

## 编译

```bash
cd 源码
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex    # 第二遍为目录与交叉引用
```

本机使用 MiKTeX 26.5 + XeTeX（`ctexart` 的 `fontset=windows` 需要 XeTeX）。已实测两遍后 28 页、0 error、0 Overfull、0 未定义引用。

## 约定

- **两套编号不混**：原文定理编号 3.1–3.20、公式编号 (1.1)(2.1)–(2.5)(3.1)–(3.14)；译本页眉只印译本页码，原文页码以段首灰色 `[p. 2229]` 标记。
- **`\origpage{NNNN}`** 输出灰色小字，标在该段所属的印本页；它只作定位，不影响编号。
- **正文一律用 `\cite{key}` 与 `\eqref{label}`**，不手写编号：文献表顺序与原文完全一致，渲染出的 `[HMP]`、`[Hi3]` 等标号与印本相同。
- **译注**写成 `\footnote{译注：……[来源：…]}`，共 5 条；原文自带脚注保留并标明。
- 原文笔误不擅改：照录 + 加译注 + 登记 `reports/02_疑点清单.tsv`。

## 与资料卡的关系

`datasets/hausel22/`（29 张卡）的 `sources[].pages` 全部用印本页，anchor 形如 `A p.2243 eq (3.12)`；卡内术语与 `源码/` 一致。改动译文术语时，记得同步 `app_terms.tex`、`03_术语表.md` 与资料卡。
