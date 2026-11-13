==== tr-e.md ====
存疑（均按原意译，未改数学内容）

1. ch08 特征定义：「a global section … of the trivial $\Gm$-bundle $\mathcal{O}_X^\times$ on $X$」与紧接的 $\Gamma(G,\mathcal{O}_G^\times)$、$\mathcal{O}_{G\times G}^\times$ 不符，应为 $G$ 上的 $\mathcal{O}_G^\times$；译文按 $G$ 处理并加译注。
2. ch08 对角化群概形定义：「the group $\cha$ is canonically identified with the character group $\widehat{G}$」中的 $\cha$ 应为 $\Lambda$；译文按 $\Lambda$ 处理并加译注。
3. ch08「which we call customly weight space decompositions」：`customly` 应为 `customarily`；按「我们称之为权空间分解」译，未保留错拼。
4. ch08 引理证明中「$\mathcal{O}_{G\times X}(G\times U)$-模」与同段其余处的 $G\times X$ 不一致（$U$ 应为 $X$）；公式照抄，未改。
5. ch08 推论 label 为 `thm:EmbeddingOfTheOrbitCategory` 而环境是 `cor`（推论），与 tr-f 对 ch09 同一 label 的记录一致；保持原样，未改 label。
6. ch07 中的对称幺半范畴单位对象记号 $({\mathcal{O}_X},\theta(0))$ 与定义开头的 $\id_{\mathcal{O}_{G\times X}}$ 不统一（见译注 2）；照原文保留。
7. 原文 §5a–§5c 中有若干被 `%` 整段注释掉的 tikzcd 交换图（未进入 `_src`）；按 `_src` 交付，译文未补画这些图。若后续需要图上排版，请 lead 决定是否恢复。
8. 「有限表现」在原文脚注中定义为「$\VB$ 或（$X$ 局部 Noether 且凝聚）」，与通常的有限表现定义略有出入；照原文译出，未加解释性改写。

## 6. 术语

新增术语见 `work/reports/tr-e-terms.tsv`（28 条，含 group algebra 群代数、right comodule 右余模、weight space 权空间、twisting 按特征作扭、strict action 严格作用、fully faithful embedding 全忠实嵌入 等）。其中「特征群」「权空间分解」「轨道范畴」沿用 `terms_zh.tsv` 既
==== tr-f.md ====
存疑 5。
- yizhu「$\Perf$ 的约定与通常不同」：局部完美 vs 严格完美（local vs strictly perfect），对应原文注释里被注释掉的 (GSP) 讨论。
- conceptbox「dg 增强」（nLab *dg-category*；Keller arXiv:math/0601185）、yizhu「谱序列为什么退化为同构」。

## 4. 编译自检

`work/check/` 下各跑两遍 `xelatex -interaction=nonstopmode`：

| 文件 | 页数 | `!` 错误 | Overfull | Underfull | Missing character |
| --- | --- | --- | --- | --- | --- |
| ch09_test | 5 | 0 | 0 | 0 | 0 |
| ch10_test | 4 | 0 | 0 | 0 | 0 |

剩余 LaTeX Warning 只有「Reference/Citation undefined」（孤立 chunk 无 .bib、其他 chunk 的 label 不在本文件）——ch00/ch03 等自检同样如此，属预期。

类型排版微调（内容与符号未改）：ch10 中 $f$、$f'$ 的定义原本一行排不下（Overfull 35.85pt），把各自的「$\in\check{C}^{p}(…)$」移到续行，其余公式逐符号照抄。

另用脚本与 `_src` 逐项比对：`\label`、`\ref`、`\cite`（含可选参数）、`\tag` 全部一致（译文只多出译注/要点里自引的 `\ref`）；定理环境名按原文保留（ch09 用 `prop`，ch10 用 `prp`），未手写编号。

## 5. 原文笔误 / 存疑（均未改原文，按原意译）

1. ch09 正文「Similar to corollary \ref{thm:EmbeddingOfTheOrbitCategory}」：文字称「推论」，而 label 前缀是 `thm:`；照原样保留 `\ref` 与「推论」字样。
2. ch09 推论证明对一般拟凝聚层使用要求有限呈现的命题（已在译注 3 说明）。
3. ch10 §6b「Let $G$ be an affine **gorup** scheme」：拼写笔误，按 affine group scheme 译为「仿射群概形」。
4. ch10「We **customly** write $\Perf(X;\mathfrak{U})_{dg}$」：应为 customarily；正文按「按惯例」译，未保留错拼。
5. ch10 复合与单位公式中的下标集合 `i\in\mathbb{Z}`：按上下文应为 $i_0\in 