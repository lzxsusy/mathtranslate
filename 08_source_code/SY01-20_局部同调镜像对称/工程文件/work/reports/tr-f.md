# tr-f 译手报告（ch09 / ch10）

## 1. 交付物

| 文件 | 内容 | 原文范围 |
| --- | --- | --- |
| `src/chunks/ch09.tex` | §5d 限制到子群概形；§5e 群概形作用的乘积；§5 章末 keytakeaways | main.tex 2671–3290 |
| `src/chunks/ch10.tex` | §6 扭 Künneth 公式（开头）；§6a 导出 dg 范畴；§6b $G$-等变导出 dg 范畴（到 `dfn:GEquivQCohdg` 之前） | main.tex 3291–3657 |
| `work/terms_zh_tr-f.tsv` | 本两章新增术语 22 条 | — |
| `work/check/ch09_test.tex`、`ch10_test.tex` | 自检脚手架（两遍编译） | — |

未改动 `src/preamble.tex`、`main.tex`、`work/terms_zh.tsv` 及他人 chunk；未做 git 操作。

## 2. 边界说明（与 tr-g 对齐）

ch10 按 lead 调整后的边界止于 main.tex 3657：§6b 的「$G$-不变 Čech 上链复形」叙述完（「…且记 $s=(…)_{i_0<\cdots<i_p}$。」）即收尾，**不包含** `\begin{dfn}\label{dfn:GEquivQCohdg}`（3658 行起），故 ch10 末尾没有未闭合环境，可独立编译；该定义整体归 tr-g 的 ch11。tr-g 早前提出的「ch10 留 `\end{dfn}`」约定已按 lead 的新切分作废（新边界下无此问题）。

## 3. 译注与概念框

ch09（4 yizhu + 1 conceptbox + 1 keytakeaways）
- yizhu「限制的方向」：$\theta|_H$ 沿 $i_H\times\id_X$ 拉回，复合顺序不可颠倒。
- yizhu「零化子零化了什么」：$H^\perp$ = $H$ 看不见的权，$H$-权分解按 $H^\perp$-陪集重组，对应推论里的按 $H^\perp$ 取商。
- yizhu「推论略去的前提」：`crl:orbit-category-GH-restriction` 的证明引用 `prop:HInvariantsOfHomSpace`，后者要求 $\mathcal{F}$ 有限呈现，而推论对一般拟凝聚层陈述；提示常用补法（滤过余极限），并注明原文一句带过。
- yizhu「外张量积为什么不必担心符号」：两侧线性化作用于不相交变量，无 Koszul 号；真正要核对的是 $\tilde\pi_{G\times X},\tilde\pi_{H\times Y}$ 的方向。
- conceptbox「等变层的外张量积」（首次出现处；库中无此条，参考 nLab *equivariant sheaf* + Waterhouse GTM 66）。
- keytakeaways 4 条（§5 收束：限制 / 权分解 / 轨道范畴嵌入 / 外张量积为下一节 Künneth 铺路）。

ch10（4 yizhu + 2 conceptbox）
- conceptbox「Čech 复形」（含「取乘积而非直和」的理由）、yizhu「Čech 微分里的符号与删除」。
- yizhu「指标 $i\in\mathbb{Z}$ 是原文笔误」：见 §5 存疑 5。
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
5. ch10 复合与单位公式中的下标集合 `i\in\mathbb{Z}`：按上下文应为 $i_0\in I$（同一处紧接 $i_0<\cdots<i_p$）。公式照抄，另加译注提示。
6. ch10 证明末 `$H\Mod (\Coh(X)_{dg}))$` 多一个右括号：照抄，未改。
7. ch10 证明末等式 $H^0\hom^{\bullet}_{\Coh(X)}(\mathcal{F}^{\bullet},\mathcal{G}^{\bullet})_{dg}\simeq\bigoplus_{p\in\mathbb{Z}}\hom_{\Coh(X)}(\mathcal{F}^p,\mathcal{G}^p)$：按原文照录；若按双复形全复形的 $H^0$ 理解，右侧下标似应为双指标 $(p,q)$。**存疑，未改动**，建议 lead 对照原文 PDF 或作者原稿核实。

## 6. 术语

新增术语见 `work/terms_zh_tr-f.tsv`（限制函子、对角化群概形、零化子、外张量积、导出 dg 范畴、dg 增强、凝聚导出 dg 范畴、Čech 上链复形、G-不变 Čech 上链复形、双复形、全复形、全微分、内射消解、松弛层 flasque、内射、完美复形、局部完美、严格完美、Leibniz 法则、齐次态射、有界上链复形、仿射开覆盖）。其中「松弛层」「局部完美 / 严格完美」与后续章节可能相关，建议由 lead 合入 `terms_zh.tsv` 后全书统一。

另：公式内 `\text{...}` 的英文词按上下文译为中文（其中 / 对每个 / 对一切 / 在 / 与），编译无 Missing character 与 Overfull；若全书希望公式内保留英文，可统一替换。
