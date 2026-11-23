# SPEC —— 译文体例规范（LaTeX 层）

本文件规定**怎么排**；`BRIEF.md` 规定**怎么译、怎么交付**。

---

## 1. 一文一文件

| 文件 | 内容 | 原文页 |
|---|---|---|
| `sections/s00-front.tex` | 译者说明、标题信息 | — |
| `sections/s01-intro.tex` | 导引 | p.1–3 |
| `sections/s02-curve-a.tex` | §1.1–1.4 | p.3–10 |
| `sections/s03-curve-b.tex` | §1.5–1.6 | p.10–16 |
| `sections/s04-bung.tex` | §2 | p.16–23 |
| `sections/s05-grassmannian.tex` | §3 | p.23–28 |
| `sections/s06-statement.tex` | §4 | p.28–29 |
| `sections/s07-character.tex` | §5 | p.29–31 |
| `sections/s08-fisoc.tex` | §6 | p.31–34 |
| `sections/s09-compat.tex` | §7 | p.34–36 |
| `sections/s10-kottwitz.tex` | §8 | p.36–42 |
| `sections/s11-abelian.tex` | §9 | p.42–46 |
| `sections/s99-bibliography.tex` | 文献表 | p.46 |

文件内**不写** `\documentclass`、`\begin{document}`、`\input{preamble}`。

## 2. 骨架

```latex
\section{曲线}% 原文 1. The curve
\srcpage{3}

\subsection{adic 曲线}% 原文 1.1. The adic curve

设 $E$ 是剩余域有限的局部域，$q$ 为剩余域元素个数……\srcpage{4}
```

- 原文编号与 LaTeX 编号**逐条一致**：`\section` → 1…9；`\subsection` → 1.1…；定理环境按 `[section]` 计数，得 `1.1`、`1.6`、`2.3`，与原文 `Definition 1.1`、`Proposition 1.6` 完全对应。
- 原文的 "Introduction" 用 `\section*{导引}`（不编号），其余 9 节自动编号 1–9。
- 原文小节标题如 "1.1.2. The unequal characteristic case." 用 `\subsubsection`（不编号，或编号亦可；统一用不编号 `\subsubsection*`，因原文 1.1.2 这类编号在正文里被引用，标题内保留原文号）。
- 每页起点 `\srcpage{N}`；页界落在句中时用 `\srcpageinl{N}`。

## 3. 环境

| 原文 | 译法 |
|---|---|
| Definition / Proposition / Lemma / Corollary / Theorem | `definition` / `proposition` / `lemma` / `corollary` / `theorem` |
| Remark / Example / Conjecture / Question | `remark` / `example` / `conjecture` / `question` |
| Proof | `\begin{proof}…\end{proof}` |
| 无编号段落小标题（如 "Thanks:"） | `\paragraph{致谢}` 或粗体行 |

原文若把定义排成 "Deﬁnition 1.1. If $E=…$ set …"，译文用环境：`\begin{definition}\label{def:1.1} … \end{definition}`。

## 4. 译注

```latex
\yizhu{术语说明，一两句，≤120 字}{A：原文 §1.1 p.3；B：nLab "perfectoid space"}
\yizhuw{上下文可推但找不到外部依据的说明}
```
- 来源等级：A（原文/作者论文/经典教材/arXiv）、B（nLab / Stacks Project / ProofWiki，须与 A 交叉）、I（本库既有译注/术语表/卡片）。
- 同一术语全书只注一次；后面写 `\yizhu{同 §1.1 注。}{I：本工程 glossary}` 或干脆不注。

## 5. 公式与交换图

```latex
\begin{equation}\label{eq:1.1}
\delta(\varphi(y))=\delta(y)^{1/q}
\end{equation}
```
- 编号：`eq:<节>.<序>`（节号取原文，如 `eq:1.1`、`eq:8.3`）。原文有号公式必须保号；原文无号的重要公式给号并在报告登记。
- 多行用 `align`；分类讨论用 `cases`；交换图用 `tikz-cd`：

```latex
\begin{tikzcd}
Y_{S,E_\infty} \arrow[r,"(-)^\flat"] \arrow[d] & D_S^{*,1/p^\infty} \arrow[d] \\
Y_{S,E} \arrow[r,dashed] & D_S^{*,1/p^\infty}/\oo_E^\times
\end{tikzcd}
```

## 6. 记号

统一用 preamble 里的宏：`\Bun_G`、`\Gr`、`\Hck`、`\Spa`、`\cO`、`\cF`、`\FF`、`\QQ`、`\ZZ`、`\PP`、`\wt{}`、`\ol{}`；`\Spec`、`\Hom` 已声明为算子。
原文花体 $\mathscr{X}$ 用 `\mathscr{X}`；德文尖角体用 `\mathfrak{}`。

## 7. 常见坑

1. 提取文本把 $\pi$ 与 $n$ 混排（`R◦JπK` = $R^\circ\llbracket \pi\rrbracket$），**必须**看页面图像。
2. 上下标丢失（`B+ dR` = $B_{\mathrm{dR}}^+$），公式一律以 PDF 图像为准。
3. `\srcpage` 在脚注/定理环境内会漂；页界在环境中时放到环境之后或之前。
4. 中文与数学之间留半角空格由 ctex 自动处理，源码不必手打空格；但中英文词之间要空格。
5. 不写 `\\` 强制换行；段落用空行。
