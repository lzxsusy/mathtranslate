# tr-h 译手报告（ch13 / ch14：附录 A）

## 1. 交付物

| 文件 | 内容 | 原文范围 |
| --- | --- | --- |
| `src/chunks/ch13.tex` | 附录 A §A.a：链复形的 Eilenberg–Zilber 映射（洗牌映射、Alexander–Whitney 映射、链同伦），定义 A.1、命题 A.2；§A.b 开头（$C_{\otimes}$、$C_{\times}$ 两个上链复形与 $f,g,h$ 的分解，到「这些符号按下面的等同来理解：」） | main.tex 4656–5023 |
| `src/chunks/ch14.tex` | 附录 A §A.b：三个等同式、多重次数齐次元、$S^{\ast},T^{\ast},\mathbb{H}^{\ast}$ 的图、定义 A.3（三部分）、命题 A.4（五条）、证明、dg 范畴概念框、附录总结 keytakeaways | main.tex 5024–5545 |
| `work/reports/tr-h-terms.tsv` | 新增术语 14 条 | — |
| `work/check/ch13_test.tex`、`ch14_test.tex` | 自检脚手架（各两遍编译） | — |
| `work/check/tr-h_appendix_test.tex` | ch13+ch14 合并编译，验证跨 chunk 引用与编号 | — |

未改动 `src/preamble.tex`、`src/main.tex`、他人 chunk；未做 git 操作。

## 2. 边界与编号

- 按 lead m00069 的新切分：ch13 止于 `\begin{align*}` 之前（`under the identifications`），ch14 从该 `\begin{align*}` 起、含整个「等同式」display。两 chunk 首尾恰好相接：ch13 末句「这些符号按下面的等同来理解：」，ch14 以该 display 开头。
- `\appendix` 放在 `ch13.tex` 开头（`src/main.tex` 第 40 行注释已说明此处不再重复），定义/命题全部由计数器编号，未手写编号、未用 `\tag`。
- 合并编译 `tr-h_appendix_test` 的 `.aux` 实测：`sec=Eilenberg-Zilber-constraction` 编为 **A**（subsection A.1、A.2），`defn:EZMaps` 编为 **A.1**，`prp:chain-homotopy-TS` 编为 **A.2**，无 label 的 `dfn` 落在 **A.3**，`prp:STHd-relation` 编为 **A.4**。ch13↔ch14 的交叉引用（`\ref{eqn:EZMaps}`、`\ref{defn:EZMaps}`、`\ref{prp:chain-homotopy-TS}`）全部解析；ch14 引用的 `\ref{prop:BoxTensorFunctorFullyFaithful}` 由 `src/chunks/ch09.tex:402` 定义，在 main 中可解析。
- `work/pagemarks/ch13.txt`（p.48、p.49）与 `ch14.txt`（p.50、p.51）的四个页起点均按要求插在最近段落边界：p.50 落在 display 内部，故 `% [原文 p.50]` 放在 ch14 第一行、display 之前；p.51 落在 `\end{tikzcd}` 之后，故放在 `\begin{dfn}` 之前。

## 3. 译注与概念框

ch13（2 yizhu + 1 conceptbox）：
- yizhu「分次符号与一处下标笔误」：$(C_\bullet(I)\otimes\partial_\bullet(J))_t$ 中 $\partial_\bullet(J)$ 应为 $C_\bullet(J)$；$(-1)^p$ 来自把 $\partial$ 越过第一个因子时的 Koszul 符号。
- yizhu「为什么只是同伦等价，不是同构」：两个复形次数结构不同（$p+r=t$ 的张量积 vs 长度为 $t$ 的链），故不可能同构；$S\comp T=\id$、$T\comp S$ 只与恒等相差一个同伦；原文 $T\bullet S$ 即 $T\comp S$。
- conceptbox「Eilenberg–Zilber 收缩与 Čech 复形」（取 `work/concepts_library.md` 同名条，末行参考 Eilenberg–Zilber, *On products of complexes*, Amer. J. Math. 75 (1953)；本文附录 A）。全书只开一次。

ch14（4 yizhu + 1 conceptbox + 1 keytakeaways）：
- yizhu「等同式里的指标笔误」：第一个等同式右端 $(\mathcal F'^i,\theta'^{i+q}|_{U_{i_0\cdots i_p}})$ 的读法；第二个等同式 Hom 下标 $V_{j_0\cdots j_p}$ 应为 $V_{j_0\cdots j_r}$。
- yizhu「方向警告：$S^*$ 与 $S$ 反着走」：$\Hom$ 反变使诱导映射反向；$T^{\ast}S^{\ast}=\id$ 而 $S^{\ast}T^{\ast}$ 只与恒等相差同伦，对应链层面的 $S\comp T=\id$、$T\comp S\sim\id$。
- yizhu「符号 $(-1)^{qr+qs+si}$ 怎么读」：分次交换下 $q$ 越过 $r+s$ 个次数、$i$ 越过 $s$ 个次数；与命题 A.4 的 $dT^{\ast}=T^{\ast}d$ 一致。
- yizhu「原文 (3) 与证明里的几处笔误」：(3) 中 $f_{\beta_0\dotsb\beta_{t+1}^k}$ 的上标 $k$ 误入下标；正文 $H$ 与图中 $\mathbb{H}$ 指同一同伦；证明末的 \ref{prp:STHd-relation} 是自指。
- conceptbox「dg 范畴与 A∞ 范畴」（参考 nLab, *dg-category*；B. Keller, arXiv:math/0601185）。
- keytakeaways 4 条：EZ 收缩三元组 $(S,T,\mathbb{H})$；三张链映射作用到 Čech 复形得 $S^{\ast},T^{\ast},\mathbb{H}^{\ast}$ 与系数取值；命题 A.4 的五条即 dg 层面的收缩；Koszul 符号的核对口诀。

## 4. 编译自检

`work/check/` 下各跑两遍 `xelatex -interaction=nonstopmode`：

| 文件 | 页数 | `!` 错误 | Overfull | Underfull | Missing character |
| --- | --- | --- | --- | --- | --- |
| ch13_test | 3 | 0 | 0 | 0 | 0 |
| ch14_test | 4 | 0 | 0 | 0 | 0 |
| tr-h_appendix_test（ch13+ch14 合并） | 6 | 0 | 0 | 0 | 0 |

剩余 LaTeX Warning 只有「Citation/外部 label undefined」（孤立编译无 .bib、他章 label 不在本文件），属预期；合并编译里只剩 citation 警告与 `prop:BoxTensorFunctorFullyFaithful`（在其他 chunk）。

目检（`latex_look`，130 dpi）：ch13 p1–p3、ch14 p1–p4 逐页渲染检查——标题 A / A.1 / A.2、定义 A.1、命题 A.2、图（tikzcd）的 $S^{\ast},T^{\ast},\mathbb{H}^{\ast}$ 标签、译注框、概念框、keytakeaways 位置正常；display C 与两条 $\boxtimes$ 同构显示用 `\resizebox{0.98\textwidth}{!}` 缩到版心内，缩后仍清晰可读；ch14 末页只有 keytakeaways，是附录收尾的自然页。

## 5. 原文笔误 / 存疑（均照原文排印，未改公式）

ch13：
1. $(C_\bullet(I)\otimes\partial_\bullet(J))_t$ 应为 $(C_\bullet(I)\otimes C_\bullet(J))_t$（见 yizhu 1）。
2. 命题 A.2 陈述处原文写 $T\bullet S$，与 $T\comp S$ 同义（$\bullet$ 是旧排版，前后文用 $\comp$）。

ch14：
3. display C 第二个等同式 $\Hom_{\VB_H(V_{j_0\cdots j_p})}$ 的下标应为 $V_{j_0\cdots j_r}$。
4. display C 第一个等同式 $(\mathcal F'^i,\theta'^{i+q}|_{U_{i_0\cdots i_p}})$ 括号错位，应读作 $(\mathcal F'^{i+q},\theta'^{i+q})|_{U_{i_0\cdots i_p}}$。
5. display D 末 $(\mathcal G'^{j+s},\eta'^{j+s})|_{V_{j_0\cdots j_s}}$ 的下标应为 $V_{j_0\cdots j_r}$。
6. (3) 里 $f_{\beta_0\dotsb\beta_{t+1}^k}$ 的 $k$ 误入下标；同段 $f^k_{\beta_0\cdots\beta_{t+1}}$ 才是正确写法。
7. 正文「映射 $S$、$T$ 与 $H$」与图中 $\mathbb{H}$ 混用，指同一个同伦。
8. 证明末「relations in Proposition \ref{prp:STHd-relation}」是自指，实际应为 \ref{prp:chain-homotopy-TS}（照原文保留 \ref，未改）。
9. `ch14_src.tex` 第 237 行被注释掉的 `% \arrow[loop left, <-, "H"]` 是旧稿，按规范未译。

## 6. 版式适配与引号事故

- preamble 未载 `adjustbox` 宏包：原文 `\adjustbox{scale=0.8}{…}`、`\adjustbox{max width=\textwidth}{…}` 分别改为 `\text{\scalebox{0.8}{…}}` 与 `\begin{center}\resizebox{0.98\textwidth}{!}{…}\end{center}`（display C、两条 $\boxtimes$ 同构显示、$(S^{\ast}h)$ 显示）。数学内容与符号未改。
- 首轮编译的三处 Overfull（display C 58.5pt、以「确定，并且」起头的段落 40.2pt、$(S^{\ast}h)$ 显示 71.7pt）均只改排版容器/断行，未动符号。
- **引号事故**：12:26:59 有一次全局引号规范化把 ch13.tex、ch14.tex 的 ASCII 引号全换成「」，连 tikzcd 的 `\arrow[...]` 标签也改了，编译报 `! Package pgfkeys Error: I do not know the key '/tikz/「S^*」'`。已还原 6 处箭头标签（ch13：`"S"`、`"T"`、`"\mathbb{H}"`；ch14：`"S^*"`、`"T^*"`、`"\mathbb{H}^{\ast}"`）。若再跑批量规范化，请把 `work/fix_tikz_quotes.py` 放在其后，否则 `\arrow` 标签会再次变「」。

## 7. 术语

新增见 `work/reports/tr-h-terms.tsv`（14 条）：洗牌映射、Alexander–Whitney 映射、链复形、上链复形、链同伦、上链映射、收缩、dg 函子、Koszul 符号、有序集、多重次数、齐次元、递增指标组、张量积。其中「Eilenberg–Zilber 收缩」「Čech 复形」「完美模」等已在 `work/terms_zh.tsv`，直接沿用，未重写该表。
