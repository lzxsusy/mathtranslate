# ch05a 报告（第 5 章标题 + §5.1）

## 一、覆盖范围

- 原书 **p.573–p.580**（8 页），起于第 5 章标题 “Abelian varieties”，止于 §5.2 标题
  “Representing objects for equivalences and the group of autoequivalences” 之前。
- 生成位置：`src\chunks\ch05a.tex`，在 `main.pdf` 中占 **第 78–85 页**（印刷页码 72–79）；
  §5.2 从第 85 页中部开始，属 `ch05b.tex`，本块不写。
- 本块含 `\chapter{阿贝尔簇}`、`\section{阿贝尔簇上凝聚层范畴之间的等价}` 与一条 `\takeaway`；
  按分工不写 `\chapterreview`。

| 原书页 | PDF 页（印刷页） | 该页起首内容 |
|---|---|---|
| 573 | 78 (72) | 章/节标题、$m$、$T_a$、$\hat A$、Poincaré 丛、定义 5.1 |
| 574 | 79 (73) | 命题 5.1.2、注 5.1.3、式 (49)(50)、$\Phi_{S_A}$、定义 5.1.4 |
| 575 | 80 (74) | 命题 5.1.5 证明续、定义 5.1.6、图 (51)、定理 5.1.7、引理 5.1.8 |
| 576 | 81 (75) | 引理 5.1.9、定理 5.1.7 证明第 1–2 步 |
| 577 | 82 (76) | 第 2 步末、第 3 步、同构链、粘接成 $X\into(A\times\hat A)\times(B\times\hat B)$ |
| 578 | 83 (77) | 推论 5.1.10、命题 5.1.11 |
| 579 | 84 (78) | $\mathrm{Eq}$、群胚 $\mathfrak A,\mathfrak D$、命题 5.1.12、推论 5.1.13、矩阵 |
| 580 | 84–85 (78–79) | 集合 $U$、定义 5.1.14、命题 5.1.15、定理 5.1.16、推论 5.1.17 |

## 二、交换图（原 `\figdiag`，现改为 TikZ 重绘）

本块只有 1 个二维交换图。`src\figures\` 已清空，按 Lead 指示改用 preamble 的 tikzcd 直接重排，
不再走 `\figdiag` 占位框（`\diag` 内含 `center` 环境，不能嵌在 `equation` 里，故在 `equation`
内直接用 `tikzcd` 环境，以便保留手工 `\tag{51}`）。位置：`ch05a.tex` 中部，`% [原文 p.575]` 段内。

| 页 | 内容 | 排版位置 |
|---|---|---|
| 575 | 图 (51)：$D^b(A\times\hat A)\xrightarrow{\Phi_{S_A}}D^b(A\times A)$ 与 $D^b(B\times\hat B)\xrightarrow{\Phi_{S_B}}D^b(B\times B)$ 的方块，编号 (51) 在右侧 | `main.pdf` 第 80 页（印刷 74） |

节点与箭头（已逐条对照 `work\pages\p065.png` 核对）：

- 节点：左上 $D^b(A\times\hat A)$，右上 $D^b(A\times A)$，左下 $D^b(B\times\hat B)$，右下 $D^b(B\times B)$。
- 箭头 1：左上 → 右上，标 $\Phi_{S_A}$（横向，带上箭头）。
- 箭头 2：左下 → 右下，标 $\Phi_{S_B}$（横向）。
- 箭头 3：左上 → 左下，标 $\Phi_{\mathcal J(\mathcal E)}$（纵向，向下）。
- 箭头 4：右上 → 右下，标 $\mathrm{Ad}_{\mathcal E}$（纵向，向下）。
- 编号 (51) 印在方块右侧中部。

代码形态（标签一律带花括号，避免 tikz 引号解析吞掉上下标）：

```latex
\begin{equation}
\begin{tikzcd}[row sep=2.6em,column sep=3.2em,ampersand replacement=\&]
\Db(A\times\hat A) \arrow[r, "\Phi_{S_A}"] \arrow[d, "\Phi_{\cJ(\cE)}"]
  \& \Db(A\times A) \arrow[d, "\mathrm{Ad}_{\cE}"] \\
\Db(B\times\hat B) \arrow[r, "\Phi_{S_B}"]
  \& \Db(B\times B)
\end{tikzcd}
\tag{51}
\end{equation}
```

## 三、陈述与公式清单

陈述环境共 **17** 条（编号全部照抄原书）：

| 编号 | 类型 | 页 |
|---|---|---|
| 定义 5.1 | definition | 573 |
| 命题 5.1.2 [29] | proposition | 574 |
| 注 5.1.3 | remark | 574 |
| 定义 5.1.4 | definition | 574 |
| 命题 5.1.5 | proposition | 574 |
| 定义 5.1.6 | definition | 575 |
| 定理 5.1.7 | theorem | 575 |
| 引理 5.1.8 [37] | lemma | 575 |
| 引理 5.1.9 [37] | lemma | 576 |
| 推论 5.1.10 | corollary | 578 |
| 命题 5.1.11 | proposition | 578 |
| 命题 5.1.12 | proposition | 579 |
| 推论 5.1.13 | corollary | 579 |
| 定义 5.1.14 | definition | 580 |
| 命题 5.1.15 | proposition | 580 |
| 定理 5.1.16 | theorem | 580 |
| 推论 5.1.17 | corollary | 580 |

证明 7 处：命题 5.1.5、定理 5.1.7（`\begin{proof}[定理 5.1.7 的证明]`，含第 1–3 步）、
推论 5.1.10、命题 5.1.11、命题 5.1.12、命题 5.1.15、推论 5.1.17。

手工编号公式 **3** 条：

| 编号 | 内容 | 页 |
|---|---|---|
| (49) | $\Phi_{(a,\alpha)}(\cdot):=T_{a*}(\cdot)\otimes\cP_\alpha=T^*_{-a}(\cdot)\otimes\cP_\alpha$ | 574 |
| (50) | $S_{(a,\alpha)}=\cO_{\Gamma_a}\otimes p^*_2(\cP_\alpha)$ | 574 |
| (51) | 图 (51) 的交换方块（tikzcd 重绘） | 575 |

正文中另引原书既有编号：定理 3.2.2、命题 2.1.7、式 (7)、(10)、(11)、(12)；交叉引用一律
写「定理 5.1.16」「式 (49)」，未用 `\ref`。

## 四、译注清单

`\yizhu` 4 条（均在正文印出）：

| 类型 | 页 | 一句话 |
|---|---|---|
| 概念 | 573 | 「细」模空间保证泛线丛存在；$\{e\}\times\hat A$ 上平凡才把 $\cP$ 钉死，否则可乘 $\hat A$ 提升的线丛。 |
| 概念 | 573–574 | $A$ 与 $\hat A$ 一般不同构而导出范畴等价；$\Phi_\cP$ 是 Fourier–Mukai 变换的原型，即本节构造的起点。 |
| 概念 | 575–576 | 引理 5.1.8 沿域扩张下降、引理 5.1.9 保证全忠实/等价在域扩张下不变，合起来是「可设 $k$ 代数闭」的下降论证。 |
| 概念 | 579–580 | 「等距」的条件 $\tilde f=f^{-1}$ 把矩阵与其对偶矩阵绑在一起，故强于一般簇同构。 |

`% [Tutor Note: …]` 8 条（不印出）：

| # | 页 | 内容 |
|---|---|---|
| 1 | 573 | 定义 5.1 前句用 $A_1,\dots,A_m$、$(\alpha_1,\dots,\alpha_m)$，后句印 $\cP_{(\alpha_1,\dots,\alpha_k)}$ 与 $A_1\times\cdots\times A_k$，下标不一致。 |
| 2 | 573 | 同一丛在页图上印作斜体 $P_{\hat A}$ 与花体 $\cP_A$，字体不一致。 |
| 3 | 574 | 命题 5.1.5 证明末句印 $p^*_1(\cP_\alpha)$，与 (50) 及命题 5.1.5 b) 的 $p^*_2$ 不符。 |
| 4 | 575 | 引理 5.1.8 末字印 $j=\overline{\subset}$，当为 $j=\bar\iota$（$i$ 在 $\bar k$ 上的基变换）。 |
| 5 | 577 | 第 3 步两处把 $(a,\alpha)$ 印作 $(a,a')$。 |
| 6 | 577 | 同构链第二、三个 $\cong$ 各只留一个因子，应合写为 $\Phi_\cE\circ\Phi_{(a_1,\alpha_1)}\Phi_{(a_2,\alpha_2)}\circ\Phi_\cE^{-1}$。 |
| 7 | 577 | 原文引「按定义 (49) 等于 $T^*_a$」，而 (49) 印 $T^*_{-a}$，且 $T^*_a=T_{-a*}\ne T_{a*}$。 |
| 8 | 578 | 命题 5.1.11 前印 $\cP_{(\alpha,-a)}$、后印 $\cP_{(\alpha,a)}$；又「5.1.1」应是「定义 5.1」。 |

## 五、存疑与待核

1. **核对象的字体**：原书 §5.1 把核与层印作斜体 $P_A,\ S_{(a,\alpha)}$，本块照页图用斜体；
   但已完成的 `ch05b.tex`（§5.2）沿用花体 $\cP_A,\ \cS_A$。两处需 Lead 决定是否统一，
   若统一则本块须把 `$P_A$`、`$S_{(a,\alpha)}$` 一并改花体（约 20 处）。
2. **引理 5.1.8 末字**：页图确为带上划线的 $\subset$；语义上只能是 $j=\bar\iota$。已照录并加注，
   若 Lead 认为应直接印正确形式，删掉 `\overline{\subset}` 换成 `\bar\iota` 即可。
3. **命题 5.1.11 的「5.1.1」**：全书编号只有定义 5.1，无 5.1.1。已照录加注；若确认是笔误，
   可改为「定义 5.1」。
4. **图 (51)**：已按 Lead 指示改为 tikzcd 重绘（见 §二），不再依赖 `figures/dg_575_a.pdf`；
   重绘后与页图核对一致，标签、箭头方向、编号位置均无误。
5. **定理 5.1.16 的逆命题**：原文只说「在代数闭、特征 0 域上成立，[38] 已证，§5.3 另证」，
   本块照译，未在 takeaway 里写成双向等价（初稿曾误写「当且仅当」，已改）。
6. **页眉**：fancyhdr 的 `\headheight` 12.4pt 警告为全书既有，与本块无关。

## 六、编译自检结果

编译命令（独立输出目录）：

```
cd C:\Users\admin\Downloads\orlov_derived_work\src
lualatex -interaction=nonstopmode -output-directory=C:\Users\admin\Downloads\orlov_derived_work\build_ch05a main.tex
```

全書 `main.log`（139 页）：

| 项目 | 计数 |
|---|---|
| `!` 致命错误 / file:line | 0 |
| `Undefined control sequence` | 0 |
| `Missing character` | 0 |
| `Overfull \hbox` | 0 |

隔离验证（只含 `preamble` + 本块，`src\_t05a.tex` → `build_ch05a\_t05a.pdf`，8 页）：
`!` 0、`Undefined control sequence` 0、`Missing character` 0、`Overfull \hbox` 0
（含 tikzcd 图 (51)，无 `Argument of \tikz@quote@@parser` 报错）。

图 (51) 已渲染核对：`main.pdf` 第 80 页，方块四节点、四箭头方向与标签、右侧编号均与原书 p.575 一致。

备注：期间曾有一次全量编译失败，原因是 `chunks/ch03a.tex` 第 44 行 `tikzcd` 未闭合（其他译者
正在改该块），与本块无关；该块恢复后重编即通过（137 页、0 错误）。
