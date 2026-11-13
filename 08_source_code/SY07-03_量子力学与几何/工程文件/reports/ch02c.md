# ch02c 译注报告

## 1. 块名与页段

- 块名：ch02c（第 2 章末块，章末含 `\chapterreview`）
- 页段：PDF 139–161（原书 p.138–160），共 23 个原书页
- 输出文件：`src/chunks/ch02c.tex`（1369 行，37843 字符，汉字 4038）
- 本块从 §2.8 开头起。`ch02b.tex` 末尾已给出 §2.7 的 `\takeaway`，块界处无重复、无残缺句；本块不再补写前一节的收束。
- 本块是第 2 章最后一块，故节末除 §2.8 的 `\takeaway` 外，块末另加 `\chapterreview`。

## 2. 节清单

- §2.8 微扰展开（`\section`）
  - 2.8.1 Wick 定理（内含 `\subsubsection*{高斯积分}`、`\subsubsection*{Wick 定理}`）
  - 2.8.2 费曼图展开
  - 2.8.3 再论外尔量子化
  - 2.8.4 $S^1$ 关联（内含 `\subsubsection*{$S^1$ 传播子}`、`\subsubsection*{$S^1$ 关联}`）
  - 2.8.5 霍赫希尔德同调（内含 `\subsubsection*{霍赫希尔德同调}`、`\subsubsection*{量子 HKR}`）

`\takeaway` 1 处（§2.8 末，77 汉字）；`\chapterreview` 1 处（块末，247 汉字）。两者均在手册规定区间内。

## 3. 陈述编号清单（共 19 条，编号全部照抄原文）

| 类型 | 编号 | 名称 |
| --- | --- | --- |
| 例 | 2.8.1 | 两点函数 |
| 例 | 2.8.2 | 四点函数 |
| 例 | 2.8.3 | $x^ix^jx^kx^l$ 的期望值 |
| 定义 | 2.8.4 | 图（graph） |
| 例 | 2.8.5 | $\Theta$ 图 |
| 定义 | 2.8.6 | 图的同构与自同构 |
| 例 | 2.8.7 | 三点图的两种画法 |
| 例 | 2.8.8 | 双圈图的自同构群 |
| 例 | 2.8.9 | $\omega_\Gamma$ 的赋值 |
| 命题 | 2.8.10 | 费曼图展开公式 |
| 命题 | 2.8.11 | $g(\theta)$ 的分段表达式 |
| 定义 | 2.8.12 | $S^1$ 关联 |
| 例 | 2.8.13 | 两个多项式的 $S^1$ 关联 |
| 例 | 2.8.14 | 三个多项式的 $S^1$ 关联 |
| 例 | 2.8.15 | $HH_0(A)$ 的计算 |
| 定理 | 2.8.16 | Hochschild–Kostant–Rosenberg 定理 |
| 注 | 2.8.17 | 非交换微分形式 |
| 定义 | 2.8.18 | 量子 HKR 映射 |
| 注 | 2.8.19 | Feigin–Felder–Shoikhet 迹公式 |

说明：
- 陈述带括注名的一律写成 `\begin{example}{2.8.1}` + 正文首句加粗括注（如 `\textbf{（两点函数）}`），避免「2.8.1.（两点函数）」双标点。
- 命题 2.8.11 的证明用 `proof` 环境；其余「Check:」类验证按原书排版写成正文 `\underline{验证}：`，不套 `proof`。

## 4. 图清单

lint 统计「图 20（TikZ 5）」。实际构成：

- **裁切 PNG 20 张**（均 300 dpi，无题注，图后只留 `% [图：原书 p.N]`）：

| 文件 | 来源页 | 内容 |
| --- | --- | --- |
| `figures/fig_p141_b.png` | 原书 p.140 | Wick 配对总图（$i_1,\dots,i_{2m}$ 与弧线配对） |
| `figures/fig_p142_a.png` | 原书 p.141 | 两点函数图（$i$、$j$ 两点一弧） |
| `figures/fig_p142_b.png` | 原书 p.141 | 部分配对图（$i_1,\dots,i_k$，两点弧 + 省略号） |
| `figures/fig_p144_a.png` | 原书 p.143 | $\Theta$ 图（$a,b,b',c$ 四边） |
| `figures/fig_p144_b.png` | 原书 p.143 | $\Theta$ 图的另一画法 |
| `figures/fig_p145_a.png` | 原书 p.144 | 双圈图（两顶点两边） |
| `figures/fig_p145_v.png` | 原书 p.144 | 三价顶点组图（$I(x)^m$ 的顶点） |
| `figures/fig_p146_a.png` | 原书 p.145 | 例 2.8.9 的 $\Theta$ 图 |
| `figures/fig_p147_a.png` | 原书 p.146 | 四面体图（$l=3$） |
| `figures/fig_p147_b.png` | 原书 p.146 | 椭圆图（$l=2$） |
| `figures/fig_p149_a.png` | 原书 p.148 | $G=\tfrac12\sgn(t_1-t_2)$ 阶梯图（蓝） |
| `figures/fig_p150_a.png` | 原书 p.149 | $f$ 的星形顶点 |
| `figures/fig_p150_b.png` | 原书 p.149 | $g$ 的星形顶点 |
| `figures/fig_p151_a.png` | 原书 p.150 | $f$–$g$ 关联的图展开总和 |
| `figures/fig_p151_b.png` | 原书 p.150 | 配对半边 $\mathbb X(t_2)$–$\mathbb P(t_1)$ |
| `figures/fig_p151_c.png` | 原书 p.150 | 配对半边 $\mathbb P(t_2)$–$\mathbb X(t_1)$ |
| `figures/fig_p153_a.png` | 原书 p.152 | $g(\theta)$ 锯齿图（蓝） |
| `figures/fig_p155_a.png` | 原书 p.154 | $\mathrm{Cyc}_{m+1}(S^1)$ 圆上 $\theta_0,\theta_1,\theta_2,\theta_m$ |
| `figures/fig_p157_bop.png` | 原书 p.156 | $b=\sum\pm$ 的两个圆（霍赫希尔德微分） |
| `figures/fig_p159_a.png` | 原书 p.158 | 循环顺序 $\theta_{k-1},\theta_k,\theta_{k+1}$ |

- **TikZ 小图**：`\wickfour` 13 次（例 2.8.2/2.8.3 的配对图）、`\timeline` 3 次（§2.8.3 时间轴）、`\trivertex` 1 次、`\edgeij` 1 次（$\omega_\Gamma$ 的赋值规则），以及原书 p.151 的 $S^1\to\R^{2n}$ 示意图 1 处。这些原书都是纯黑线条 + 数学标签的示意，按手册重绘，图后注「% [图：原书 p.N，本图按原文重绘，图内标注已译为中文；原图无题注]」。
- 重裁记录：`fig_p142_a`（首裁把 $i,j$ 标签切掉）、`fig_p155_a`（首裁把 $\theta_m$ 切掉）、`fig_p159_a`（加边距）各重裁一次；原书 p.151 的裁图只剩一个圆（箭头与 $\R^{2n}$ 被切），改为 TikZ 重绘并删除 `fig_p152_a.png`。
- 四个宏 `\wickfour`、`\trivertex`、`\edgeij`、`\timeline` 定义在 `ch02c.tex` 第 6–49 行（紧随文件头注释），仅本块使用，未改 `preamble.tex`。

## 5. 术语与宏

- 术语全部照 `术语对照表.tsv`：微扰展开、Wick 定理、高斯积分、传播子、费曼图、连通图、顶点、边、半边、关联映射、完美匹配、自同构、圈数、格林函数、外尔量子化、外尔代数、Moyal 乘积、形变量子化、霍赫希尔德同调、霍赫希尔德复形、HKR 定理、量子化映射、迹映射、微分形式、内乘、李导数、泊松双向量、拟同构、交换化等。
- 人名：Wick、Feynman（费曼）、Moyal、Hochschild（霍赫希尔德）、Kostant（科斯坦特）、Rosenberg、Weyl（外尔）、Batalin–Vilkovisky（保留）、Feigin–Felder–Shoikhet（保留）。
- 未收术语，建议增补：
  - graph expansion 图展开
  - loop number 圈数（已按表 ${l(\Gamma)}$）
  - half-edge 半边（表内已有，本块高频）
  - incidence map 关联映射（表内已有）
  - quantum HKR map 量子 HKR 映射
  - noncommutative differential forms 非交换微分形式
  - cyclic order 循环顺序
  - zero mode 零模（表内已有）
  - test function 检验函数（表内已有）
- 用到的宏：`\hs \ii \ee \rd \pa \nab \R \C \Z \sgn \Aut \operatorname{Map} \operatorname{Cyc} \operatorname{Tr} \mathbb{X} \mathbb{P} \mathcal{E} \mathcal{H} \mathcal{O} \mathbf{x} \mathbf{p} \mathrm{Cyc}_{m+1}(S^1) \overleftarrow{} \overrightarrow{}`；未改 preamble。

## 6. Tutor Note（共 4 条）

1. 定义 2.8.4 处：原书 $\gamma$ 与 $\Gamma$ 混用，译文统一写 $\Gamma$。
2. §2.8.3 的 $S_0[\gamma]$ 矩阵式：原书只印 $-\frac{\rd}{\rd t}$、$\frac{\rd}{\rd t}$ 两块，两个零块从略，译文按 $2\times2$ 补全。
3. 命题 2.8.11 证明第二步：原书分部积分漏写因子 $\frac{\ii}{2\pi n}$（原文自身滑笔），译文照原书排，另加注说明。
4. 注 2.8.19 之前：原书把 $\rho^\hs$ 误写作 $\sigma^\hs$，译文统一写 $\rho^\hs$。

（第 3 条为审校 tr01 提出、经本块确认后补入。）

## 7. 自检

```
build.ps1 -Chunk ch02c
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch02c.pdf（24 页）

python tools\lint.py ch02c
OK   ch02c  字符 37843  节 1  小节 5  陈述 19  公式 160  图20(TikZ 5)  注释 4
合计：问题 0 条

python tools\crosscheck.py ch02c
ch02c   原书=6  译文=6  页标=23  陈述=19  汉字=4007
OK 结构一致
```

- 渲染目检：`work/review/v2_p*.png`、`zoom_p*.png`（100/110/200 dpi），抽查原书 p.140（Wick 定理与 $(*)$ 式）、p.141（例 2.8.1–2.8.3 与配对图）、p.147（有限维/无穷维对照表）、p.148（$G$ 阶梯图与检验函数）、p.151（$S^1\to\R^{2n}$ 示意图、时间轴）、p.152（命题 2.8.11 与分布验证）、p.154（$\mathrm{Cyc}$ 圆图与定义 2.8.12）、p.158（定义 2.8.18 与 Wick 显式式）、p.160（$\rho^\hs(b)=i\hs\Delta\rho^\hs$、注 2.8.19、`\takeaway`、`\chapterreview`）。
- 修掉的排版问题 8 处（全在长公式/集合定义）：`\tag{$*$}` 位置、例 2.8.3 十图分 3 行、$\mathrm{Cyc}_{m+1}(S^1)$ 的 `\substack` 条件、例 2.8.14 两处断行、$b$ 定义末行、$\rho(b(-))=0$ 末行、定义 2.8.12 与定义 2.8.18 的长显示公式。

## 8. 存疑与交接

1. **块界**：从 §2.8 标题起，与 `ch02b.tex` 末段（§2.7 的 `\takeaway`）无重叠。
2. **原书 $S_0$ 矩阵式**：见 Tutor Note 2，译文补全 $2\times2$ 矩阵，数学上等价，但与原书字面不同。
3. **原文 $\sigma^\hs$ 笔误**：见 Tutor Note 4。
4. **命题 2.8.11 证明缺因子**：见 Tutor Note 3，公式照原书，注文说明。
5. **`\chapterreview`** 概括第 2 章全章（费曼核、高斯积分、渐近方法、格林函数与 WKB、微扰展开与量子 HKR），只述主线不评价；合书时若各块作者另有章末口径，可与 Lead 统一。
6. **审校**：tr01（task-14）正在逐页对照 p.139–161 页图审校，已并入的两处改动（p.143 页标位置、命题 2.8.11 的 Tutor Note 3）见本文 §6；其完整审校记录见 `reports/review_ch02c.md`（由 tr01 出）。并入后本块 build/lint/crosscheck 三连仍全绿。
