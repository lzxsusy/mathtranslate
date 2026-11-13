# tr-d 报告：ch06（§4a 末 + §4b + §4c + §4d）

## 1. 完成范围

- 交付文件：`src/chunks/ch06.tex`（387 行），对应 `src/main.tex` 第 1192–1478 行，即原文 PDF 第 24 页末至第 30 页。
- 原定范围为主文件 1301–1478 行；按 Lead 批准（m00072），把 `_src/ch05_src.tex` 第 146 行起的例 `exmp:wrapped-Fukaya-cat-twice-punctured-equivariant` 与整幅 figure `fig:Z2-cover-twice-punctured-disk` 整体收下，以保证 exmp/figure 环境完整。p.24 页首标记留在 ch05，ch06 只标 p.25–p.30（共 6 个 `% [原文 p.N]`）。
- 内容：§4a 末（二穿孔圆盘的 $\mathbb{Z}^2$-覆盖例、高维 FLTZ 情形、定理 4.3 层–Floer 对应、命题 4.4）、§4b 商的包裹 Fukaya 范畴、§4c Künneth 定理与形变不变性、§4d Kartal 修改。
- 环境名、`\label`、`\ref`、`\cite`、全部公式与 tikz/tikzcd 代码按原文保留；未手写编号、未用 `\tag`。

## 2. 编译自检

`work/check/ch06_test.tex`（`\input{../../src/preamble.tex}` + `\begin{document}` + `\input{../../src/chunks/ch06.tex}`），两遍 `xelatex -interaction=nonstopmode`：

- `!` 错误 **0**；Overfull **0**；Missing character **0**；输出 7 页。
- 仅有 citation / reference undefined 警告（单块编译无 bib 与其他 chunk，属正常）。
- 残留 1 条 `Underfull \hbox (badness 4328) in paragraph at lines 204--205`（yizhu「原文此处若干笔误」内长公式换行所致），不影响编译、无 Overfull，未强行改动。

## 3. 结构与译者注

- `yizhu` 6 条：①标号 $L_i[a,b](c)$ 怎么读；②原文此处若干笔误；③$\widehat{\Lambda}_{\Sigma}$ 与 $\widetilde{\Lambda}_{\Sigma}$；④无限型为何落到同伦极限；⑤链层面的直和其实有限；⑥$\mathcal{W}^{big}$ 是什么。
- `conceptbox` 2 个：层--Floer 对应（概念库无此条，按原文定理与 GPS24M 撰写，未标 nLab）；Kartal 修改（参考 Kartal21 §2）。
- `keytakeaways` 1 个、4 条，总结整个 §4（商与轨道范畴、二穿孔圆盘例子、高维 FLTZ + 层–Floer、Künneth/形变/Kartal 修改）。

## 4. 两处需 Lead 留意的技术处理

1. **tikzcd 的 ASCII 双引号必须保留**。源文 Künneth 证明中写作 `\arrow[r,"\simeq"]`（4 个 ASCII 引号），这是原文公式的一部分。preamble 未加载 tikz 的 `quotes` 库，故在本 chunk 顶部加了 `\usetikzlibrary{quotes}`（只写 `src/chunks/ch06.tex`，未改 preamble）。
   **请勿对 `ch06.tex` 运行 `fix_quotes.py` 一类的引号替换脚本**：把 `"\simeq"` 换成「\simeq」会触发 `! Missing \endcsname inserted`，tikzcd 直接编译失败。本次写作过程中该文件的引号曾被外部脚本改过一次，我已改回并复测通过。
2. **$\mu^k$ 长公式断行**。原单行 `\[...\]` 实测 Overfull 18.85pt，改为 `multline*` 在 `\to` 处断成两行，公式符号一字未改。另把 cases 中 `\text{if}` / `\text{and}` / `\text{otherwise}` 译为 `\text{若}` / `\text{且}` / `\text{其他情形}`。

## 5. 存疑 / 原文笔误（正文照排，均已在 yizhu ② 交代）

1. 图 4 图注中「Larangian」应为 Lagrangian（图注是原样 tikz 代码，未改）。
2. `$CW^{\ast}(L_i[a,b](c),L_j[c,d](c);\Bbbk)$`：第二个对象同时用了 $c,d$ 又把第三槽写作 $c$，与下文 $L_j[a_1,b_1](c_j)$ 不一致，疑为 $L_j[a',b'](c')$。
3. 引理 `lmm:Fukaya-category-Gmn-equivariant-generation` 处写 $\widehat{\Lambda}_{\Sigma}$，本节其余地方全用 $\widetilde{\Lambda}_{\Sigma}$，当作笔误。
4. 商的命题证明中 `$CF^{\ast}(L,K)=\bigoplus_{g\in G}(g(\tilde L),\tilde K)$` 漏写一项 $CF^{\ast}$，照排。
5. 「for some $g_i$ modulo $k$」语序混乱，译文按「$g_i$ 取某个元素、指标按模 $k$ 计」处理。
6. 证明中 `constrctible`（应为 constructible）；Kartal 修改一节 $p^{\ast}$ / $\pi^{\ast}$ 混用（均源文如此）。

## 6. 新增术语

见 `work/reports/tr-d-terms.tsv`（35 条）。其中「扇形粘合（sectorial gluing）」「环绕圆盘（linking disk）」首次出现处括注英文。

## 7. 文件范围

只写 `src/chunks/ch06.tex`、`work/check/ch06_test.tex`、`work/reports/tr-d.md`、`work/reports/tr-d-terms.tsv`；另有辅助脚本 `work/_splice_ch06.py`（把原文 figure/tikzcd 代码块拼进译文，不参与编译）。未改 preamble / main / 他人 chunk，未执行 git 操作。
