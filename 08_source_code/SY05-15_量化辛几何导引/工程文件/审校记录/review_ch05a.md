# 第 5 章前半（5.1 Morse 理论、5.2 持续模）原文疑误与待核清单

- 覆盖范围：印刷页 p.101–p.119，扫描 PDF p.109–p.127（5.2 节末尾两段文字位于 PDF p.128 顶部，按分工由本译者写入 `ch05a-s02.tex`）。
- 译文文件：`qsg/tex/ch05a-s01.tex`、`qsg/tex/ch05a-s02.tex`。
- 说明：下列「原文疑误」均在译文中保留原文写法，并加 `% [Tutor Note: ...]` 注释；「待核」项仅作提示，未改动原文语义。

| # | 位置（印刷页/PDF 页） | 原文 | 疑点 | 建议 |
|---|---|---|---|---|
| 1 | p.101 / PDF 109 | 「denote by $\mathrm{Crit}(F)$ the critical points of $F$ on $X$ (i.e., $\mathrm{d}F(p)=0$ for any $p\in\mathrm{Crit}(X)$)」 | 括注中写成 $p\in\mathrm{Crit}(X)$，临界点集是函数 $F$ 的属性，应与 $X$ 无关 | 改为 $p\in\mathrm{Crit}(F)$ |
| 2 | p.106 / PDF 114 | 「Given the initial condition $t(-\infty)=p_2$ and $t(+\infty)=p_0$」 | $t$ 是定义域参数，流的端点应写成 $u(\pm\infty)$ | 改为 $u(-\infty)=p_2$、$u(+\infty)=p_0$ |
| 3 | p.106 / PDF 114 | 「$u(t)=(u_1(t),3\pi/2)$, where $u_1$ is solved from the second equation above」 | $u_1$ 只出现在第一个方程 $\dot u_1=-\cos u_1$ 中，应说「第一个方程」 | 改为 the first equation above |
| 4 | p.118 / PDF 126 | 例 5.2.4：「the persistence $\mathbf k$-module $\mathbb V_F$ in Example 5.1.10」 | $\mathbb V_F$ 是在例 5.2.2 中定义的；例 5.1.10 只定义了 Morse 同调群，尚未引入持久模 | 改为 Example 5.2.2 |
| 5 | p.118 / PDF 126 | 「enabling homological invisible generators to be investigated」 | 应为副词 homologically（同调不可见地） | 改为 homologically invisible generators |
| 6 | p.113 / PDF 121 | 定理 5.1.2：「$\mathrm{HM}_*\cong\mathrm{HM}_*$ for any field $\Z_2$」 | $\Z_2$ 已固定，「for any field」与 $\Z_2$ 冲突；结合注 5.1.4，本意应是「对任意系数域 $\mathbf k$」 | 改为 for any coefficient field $\mathbf k$（或删去 for any field） |
| 7 | p.115 / PDF 123 | 「introduced by G. Carlsson and A. Zamorodian [248]」，随后同一段又写 A. Zomorodian | 同一作者（Zomorodian）两种拼写 | 统一为 Zomorodian |
| 8 | p.101 / PDF 109 | 定义 5.1.1：「local coordinates $(x_i)_{i=1,\cdots,\dim M}$」 | 上下文流形记作 $X$、维数记作 $n$，唯此处用 $M$ | 记号不统一，建议改 $\dim X$ 或 $n$；译文照原文保留 |
| 9 | p.107 / PDF 115（待核，非定论） | 命题 5.1.1 后结论 (i)：「若 $\operatorname{ind}(x)-\operatorname{ind}(y)\geqslant1$，则 $\widetilde{\mathcal M}$ 与 $\mathcal M$ 非空」 | 维数公式只约束模空间维数，不能推出非空性；可证明的是一般方向 (iii)（非空 ⇒ 指标严格下降，见 Tutor Note 中的 $\R$-轨道论证）。(i) 是否另有作者未写出的论证，未能确认 | 保留原文，加 Tutor Note 提示读者注意 (i) 与 (iii) 的逻辑地位不同；请教授裁定是否需要加脚注 |
| 10 | p.116 / PDF 126（体例说明，非疑误） | 「Definition 5.1.2 [41,68,142]」等标题后紧跟文献编号 | 原书体例，译文照排（编号置于标题后） | 无需改动 |

## 体例与宏说明

1. **Fact 环境**：preamble 未提供 `wfact` 环境（且 preamble 禁改）。译文对「事实 5.1.1 / 5.1.2」采用与 `\whead` 等价的手工排版（`\textbf{事实 5.1.1}\quad`），编号照原文。若教授希望全书统一，可在 preamble 增加 `wfact` 后由 lead 统一替换。
2. **`\codim`**：preamble 未定义 `\codim`，译文中改用 `\operatorname{codim}`（不影响排版）。
3. **例/注末尾的 `//`**：原书用 `//` 标记例、注的结束，译文用 `\hfill$//$` 保留。
4. **图注**：12 幅插图均从扫描页按 300 dpi 裁剪（`qsg/figures/fig_pNNN_k.png`），图注为中文并标注原书图号、印刷页与 PDF 页。

## 自检结果

- `python qsg/tools/check.py ch05a`：覆盖 PDF p109–p127 共 19/19 页（另在 `ch05a-s02.tex` 末尾含 p128 顶部 5.2 收尾两段，故报「越界页标记 [128]」，属分工接缝，非缺页）；节 2、keytakeaways 2、Tutor Note 39、图 12、公式编号 14（(5.1)–(5.14)）；无 LaTeX 结构错误、无缺失图片、无重复 tag、无禁用命令。
- 另用临时文档（`preamble` + 本两文件，封面独立）以 XeLaTeX 试编译通过（17 页），无 Overfull/Underfull 警告、无 undefined control sequence。
