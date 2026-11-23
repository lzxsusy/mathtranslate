# SPEC —— 译文体例规范（LaTeX 层）

本文件规定**怎么排**；`BRIEF.md` 规定**怎么译、怎么交付**。

---

## 1. 一文一文件

| 文件 | 内容 | 原文页 |
|---|---|---|
| `sections/s00-front.tex` | 译者说明、标题信息 | — |
| `sections/s01-intro.tex` | 导引 | p.1–3 |
| `sections/s02-sec1.tex` | §1 $L$ 函数的极点与函子性 | p.3–12 |
| `sections/s03-sec2.tex` | §2 函数域情形 | p.12–17 |
| `sections/s04-sec3a.tex` | §3 标题 + 3.1 假设 + 3.2 测度 | p.17–25 |
| `sections/s05-sec3b.tex` | 3.3 Steinberg–Hitchin 底 + 3.4 椭圆正则元 | p.25–33 |
| `sections/s06-sec3c.tex` | 3.5 沿稳定共轭类的积分 | p.33–38 |
| `sections/s07-sec4.tex` | §4 阿代尔化 | p.38–46 |
| `sections/s08-sec5.tex` | §5 主项 | p.46–52 |
| `sections/s99-bibliography.tex` | 文献表 | p.53–54 |

文件内**不写** `\documentclass`、`\begin{document}`、`\input{preamble}`。

## 2. 骨架

```latex
\section{\texorpdfstring{$L$ 函数的极点与函子性}{L 函数的极点与函子性}}% 原文 §1
\srcpage{3}

\subsection{...}
...
```

- 每页开头必须出现 `\srcpage{N}`（N 为原书页，本底本等于 PDF 页）。
- 页界落在句子中间时，在该处插 `\srcpageinl{N}`，不另起段。
- 引用原文页码一律用原书页，不用 PDF 页号。

## 3. 编号

- 公式：`\begin{equation}\tag{1.4} ... \end{equation}` 手工编号，与原文逐条一致。
  原文同一编号下并列的两行（如 (1.1) 与"部分 $L$ 函数"）在译本中标 `(1.1$'$)`。
- 断言：定理类环境共用计数器 `theorem`，按 `[section]` 计数。原文编号跨节连续，
  故在环境前用 `\setcounter{theorem}{N}` 对齐：
  Lemme 2.6 → 5；Lemme 3.26 → 25；Proposition 3.29 → 28；Lemme 4.1 → 0；Lemme 4.2 → 1；
  Lemme 5.4 → 3；Proposition 5.6 → 5；Lemme 5.8 → 7；Lemme 5.10 → 9；Lemme 5.13 → 12。
- 文献：`[A1]`–`[W2]`，用 `thebibliography` 手工条目，编号与原文一致。
- 脚注：`\footnote{}` 自然编号；译本新增 14 条译注，故脚注编号为译本连续编号，与原书 10 条脚注不一一对应；原书编号见各注的来源标注。

## 4. 译注

- `\yizhu{内容}{来源}`：内容为易错预警 / 含糊点拨 / 背景直觉，来源写 A、B、I 级出处。
- `\yizhuw{内容}`：无外部依据的上下文推断，自动补"译者按"标记。
- 译注不重复正文，不写"这里作者说……"；每条不超过 120 字（公式不计）。
- 原书笔误：正文照录原文（含错号），译注说明"原文如此"并给正确写法。

## 5. 文风

- 全角标点；英文术语、数字与汉字之间留半角空格。
- 避免"被……所……""进行……的讨论""对于……而言"；单句不超过 70 字。
- 原文的让步、保留语气（"我们期望""原则上"）必须保留，不得改写成断言。

## 6. 编译

```bat
cd 源码
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

判据：日志中 `^!` 为 0、`Overfull` 为 0、`undefined` 为 0。
