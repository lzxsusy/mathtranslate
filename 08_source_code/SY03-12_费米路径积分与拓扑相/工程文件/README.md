# 费米路径积分与拓扑相（中文译注版）

Witten, *Fermion Path Integrals And Topological Phases*（arXiv:1508.04715v2；Rev. Mod. Phys. **88**, 035001 (2016)）全文中文译注。

## 目录结构

```
费米路径积分 1508.04715v2_中文译注版/
├── 费米路径积分 1508.04715v2_中文译注版.pdf   ← 排版稿（63 页）
├── main.tex                  ← 主文件（\input 各章节）
├── preamble.tex              ← 导言区：中文版式 + 原稿全部自定义数学宏
├── zh/
│   ├── frontmatter.tex       ← 标题页、摘要、译者说明
│   ├── c01.tex               ← 第 1 节 导言
│   ├── c02.tex               ← 第 2 节 2.1.1–2.1.7
│   ├── c03.tex               ← 第 2 节 2.1.8–2.3
│   ├── c04.tex               ← 第 3 节 实费米子
│   ├── c05.tex               ← 第 4 节 复费米子 + 第 5 节 Majorana 链
│   ├── c06.tex               ← 附录 A、B
│   └── c07.tex               ← 附录 C + 参考文献
├── figs/
│   └── fig01.png … fig09.png ← 自原 PDF 裁出的 9 张插图（360 dpi）
├── spec/
│   ├── TRANSLATION_SPEC.md   ← 翻译规范
│   └── GLOSSARY.md           ← 术语对照表
└── 审校说明_勘误与批注汇编.md
```

## 编译

需要 XeLaTeX（推荐 tectonic 或 TeX Live 2022+，含 ctex）：

```
tectonic -X compile --outdir build main.tex
# 或
xelatex main.tex && xelatex main.tex          # 两遍以生成目录
```

无需 BibTeX（参考文献以 `thebibliography` 内嵌）。

## 体例速览

- 公式、`\label`、`\ref`、`\cite` 与原文逐字对应，公式编号与原文一致；
- 每节开头蓝框“本节重点（Key Takeaways）”为译者所加；
- 源码中以 `% [Tutor Note: ...]` 形式嵌入 157 条学术批注（不显示于 PDF）；
- 图注中文并标注原文页码与图号；
- 原文勘误汇总见 `审校说明_勘误与批注汇编.md`。
