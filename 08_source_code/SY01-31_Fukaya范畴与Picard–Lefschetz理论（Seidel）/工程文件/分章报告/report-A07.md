# A07 校对报告

## 一、范围与工作量

| 文件 | 原书印刷页 | 行数 | 修订 | 译者注 |
|---|---|---|---|---|
| `src\chapters\section-12-ad.tex` | 174–179 | 118 | 0 | 3 |
| `src\chapters\section-12-ef.tex` | 179–183 | 109 | 1 | 2 |
| `src\chapters\section-12-gh.tex` | 183–187 | 105 | 2 | 3 |
| `src\chapters\section-12-ij.tex` | 188–190 | 50 | 0 | 2 |
| `src\chapters\section-13-ab.tex` | 191–195 | 84 | 0 | 3 |
| `src\chapters\section-13-c.tex` | 195–198 | 65 | 1 | 3 |
| 合计 | 174–198（25 页） | 531 | 4 | 16 |

工作方式：逐段对照 `work\en\bundles\A07.txt`（印刷页 175–198，来源页码已按「印刷页 = `\SourcePage` − 8」重建，见 lead 更正），中文与英文逐句比对，重点核查符号、上下标、正负号、次数、量词与方向；对含公式的可疑处回到 `work\pages\pNNN.png` 原页图核对（本次据 p174 原图确认了二次典范丛的指数，据 p183 原图确认了 $c_u$ 的取值域）。术语一律对照 `术语表.csv`。16 条注中，nLab 页面均用 web_fetch 实际打开（HTTP 200，2026-11-15 访问）；Pin 结构所引的 nLab 页面抓取失败（`/nlab/print/Pin+structure` 重定向到首页），故该条改引原书 §11j 与例题 11.20，未引任何二手博客或 AI 摘要。

六个文件均通过 `work\tools\check.ps1`，输出 `OK`：

```
OK section-12-ad.tex
OK section-12-ef.tex
OK section-12-gh.tex
OK section-12-ij.tex
OK section-13-ab.tex
OK section-13-c.tex
```

## 二、译文修订表

| # | 文件:行 | 原文 | 改文 | 理由 |
|---|---|---|---|---|
| 1 | `section-12-ef.tex`:106 | `c_u:o(\Lambda_{y,0}^\#,\Lambda_{y,1}^\#\otimes\lambda^{\mathrm{top}}(\Lambda_{y,1}))\longrightarrow\R.` | 末项改为 `\longrightarrow\K.` | 原书印刷页 183 作 `cu: o(Λ#_{y,0}, Λ#_{y,1}⊗λtop(Λ_{y,1})) → K`。同段上文链映射已取值于 $\K$，$c_u$ 正是用来把 $|c|_\K$ 逐项求和的对象；若取值于 $\R$，规范化和与 $\mu^d$ 的 $\pm1$ 系数都无从谈起，与全段自相矛盾。 |
| 2 | `section-12-gh.tex`:24 | 模空间 $\M^{d+1}(y_0,\ldots,y_d)$ 的维数为 $i(y_0)-i(y_1)-\cdots-i(y_d)+d-2$ | 末项改为 $+2-d$ | 原书印刷页 184 明确作 `i(y0) − i(y1) − ··· − i(yd) + 2 − d`；同段下一句「$i(y_0)=i(y_1)+\cdots+i(y_d)+2-d$」与 $\mu^d$ 要求的次数 $2-d$ 都只能是 $+2-d$。旧译把 $2$ 与 $d$ 的次序颠倒，使维数公式与紧随其后的零维条件互相矛盾。 |
| 3 | `section-12-gh.tex`:8 | $(z_3,\allowbreak \ldots,\allowbreak z_d)\subset(\partial D)^{d-2}$ | 改为 `\in(\partial D)^{d-2}` | 原书印刷页 183 作 `(z3,…,zd) ∈ (∂D)^{d−2}`：这是一个 $d-2$ 元组，属于该乘积空间，不是它的子集。$\subset$ 会让读者误以为在讨论某个子集族，属记号笔误。 |
| 4 | `section-13-c.tex`:25 | 图 13.2 把它画成两个竖直边相识别的正方形 | 改为「两个竖直边相粘合的正方形」 | 英文为 `a square with the two vertical sides identified`。「相识别」不成词（把「识别/认同」与「粘合」混写），且与图 13.2 的构造（矩形的两竖直边等同得到 $S^1\times[-1;1]$）不符。 |

## 三、译者注表

| # | 文件:行 | 原书页 | 主题 | 来源级别 |
|---|---|---|---|---|
| A07-01 | `section-12-ad.tex`:7 | 174 | 膜 = 平方相位提升 + Pin 结构 | A |
| A07-02 | `section-12-ad.tex`:13 | 175 | $\operatorname{Gr}(TM)^\#$ 的纤维 $\Z\times\RP^\infty$ | A |
| A07-03 | `section-12-ad.tex`:56 | 177 | Koszul 符号来自行列式线 | A |
| A07-04 | `section-12-ef.tex`:48 | 180 | 非 Frobenius 配对与 Serre 函子 | B |
| A07-05 | `section-12-ef.tex`:67 | 181 | $\partial$ 的逐点计数与符号 | A |
| A07-06 | `section-12-gh.tex`:6 | 183 | Deligne–Mumford 边界面 = $\Ai$ 关系 | B |
| A07-07 | `section-12-gh.tex`:32 | 184 | $\mu^1$ 与 $(-1)^\dagger$ 的符号选择 | A |
| A07-08 | `section-12-gh.tex`:98 | 187 | 平移对象作为 $\Ai$ 范畴公理 | A |
| A07-09 | `section-12-ij.tex`:23 | 188 | 弱作用与弱 $2$ 群 | A |
| A07-10 | `section-12-ij.tex`:43 | 189 | 抽象 Serre 函子与弱 Calabi–Yau | B |
| A07-11 | `section-13-ab.tex`:46 | 192 | 自动正则性为何只在 $\dim M=2$ 成立 | A |
| A07-12 | `section-13-ab.tex`:78 | 194 | 单值化定理 $\Rightarrow$ 多边形组合模型 | A |
| A07-13 | `section-13-ab.tex`:82 | 195 | 常值多边形使引理 13.2 失效 | A |
| A07-14 | `section-13-c.tex`:7 | 195 | 曲面膜 = 子丛同伦 + 实线丛 | A |
| A07-15 | `section-13-c.tex`:23 | 196 | 多边形分解与曲面组合范畴 | B |
| A07-16 | `section-13-c.tex`:38 | 197 | $\gamma^d$ 只依赖绝对指标 | A |

来源级别：A = 原书章节/例题或经典教材；B = nLab 等权威百科或研究文献（均已实际访问）。注文均 120–260 汉字，单段，无 `%`、无 `\begin/\end`、无行间公式；每段最多 1 条，无「连续三句各一条」。

## 四、存疑未改

| 位置 | 原文 | 疑点 | 已查证 | 建议 |
|---|---|---|---|---|
| `section-12-ef.tex`:104 | 由此得到适当意义下的拓扑量子场论 | 英文 `this leads to a TQFT in a suitable sense`，直译语气更强；此处严格说只得到 TQFT 式的配对结构，尚无完整的函子性 | 核对英文原句；12e 的配对与 12j 的 Serre 函子确实给出「TQFT 式」的框架 | 保留原译。若统稿时想更贴切，可改为「这给出了一种适当意义下的拓扑量子场论式的结构」，但会略增冗长 |
| `section-12-gh.tex`:24 | 模空间 $\M^{d+1}(y_0,\ldots,y_d)$ 的维数为……，且相对于 $o(y_0)\otimes o(y_1)^\vee\otimes\cdots$ 定向 | 句子过长（一句内含膜、固定点、维数、定向四件事），可读性差 | 原书同样是一句长句，属原文风格 | 仅改数学错（$+2-d$），不拆句，以免无谓 diff |
| `section-13-c.tex`:7 | 相应平方相位映射可视为实射影化切丛的平凡化 $\alpha_M:\RP(TM)\to S^1$ | 「平凡化」易被误读为 $TM$ 平凡 | 原书作 `a trivialization of the projectivized tangent bundle`，指 $\RP^1$-丛的平凡化，非切丛 | 保留；术语表可加一条「射影化切丛的平凡化」 |

## 五、原书可疑处

经与 `work\pages\pNNN.png` 原页图逐处核对，本区段未发现原书自身的数学错误。两处曾疑而复核无误，记录以备统稿：

1. `section-12-ad.tex`:3（印刷页 174）：$K_M^2=\lambda^{\mathrm{top}}_{\CC}(TM)^{\otimes-2}$。英文文本 OCR 曾读作 $\otimes 2$（负号被识别为制表符），据 p174 原页图确认原书印的是 $\otimes-2$，与 $K_M=\det(T^*M)=\lambda^{\mathrm{top}}(T^*M)$、$K_M^2\cong(\Lambda^nTM)^{\otimes-2}$ 一致。译文正确，不需改动。
2. `section-12-ef.tex`:106（印刷页 183）的 $\K$ 与 `section-12-gh.tex`:24 的 $+2-d$，原书均无误，是译文抄错，已在第二节改正。

## 六、通读小结

本区段（印刷页 174–198）是全书的技术核心：第 12 节把 Fukaya 范畴从初步版本升级为完整版本，第 13 节则把曲面情形化归为纯组合计数。12a–12c 补齐膜的定义（平方相位提升加 Pin 结构）、抽象膜空间 $\operatorname{Gr}(TM)^\#$ 与定向空间，并说明粘合公式中的 Koszul 符号来自行列式线的分次记账；12d–12e 用一族圆盘与扩展算子 $D_{S,r,u}$ 串起 K-规范化、PSS 与配对次数 $-n$，明确指出一般情形下范畴不是 Frobenius，扭转被 $\lambda^{\mathrm{top}}(TL)$ 吸收；12f–12h 逐点计数定义 $\mu^d$，借 Deligne–Mumford–Stasheff 紧化证明 $\Ai$ 关系，并把平移表述为 $\Ai$ 范畴的公理；12i–12j 讨论分次自同构、弱 $2$ 群与弱 Calabi–Yau 性质。第 13 节转向曲面：自动正则性使 Floer 理论无须扰动，浸入多边形与零维模空间一一对应，单值化定理把分析化为组合，于是可以只用多边形分解定义有向 $\Ai$ 范畴，而常值多边形是唯一的例外。译文整体忠实，公式系统（(12.1)–(12.29)、(13.1)–(13.6)）的符号、上下标与正负号逐条核对无误，术语与术语表一致。本次改 4 处确凿问题：两处数学错（ef:106 的值域、gh:24 的次序），一处记号错（gh:8 的 $\subset$），一处病句（c:25「相识别」）。16 条译注沿五条主线展开：膜与抽象膜、K-规范化与非 Frobenius、DM 紧化与符号约定、弱作用与弱 CY、曲面组合模型。两点提醒统稿者：本区段正文未出现 Novikov 环与多值扰动，它们被「正合」与「已选定 Floer 数据」的假设吸收，读者对照其他文献会觉得跳跃；12j 的弱 CY 与 13b 的组合模型仅靠「有向子范畴」衔接，译文未加说明，注 13 与注 15 已略作补充。
