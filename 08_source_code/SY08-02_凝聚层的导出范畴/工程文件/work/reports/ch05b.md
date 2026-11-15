# ch05b 交付报告

块名：ch05b（第 5 章 §5.2 + §5.3 + 第 5 章章末评注，全书最后一块）
产出：`src/chunks/ch05b.tex`、`work/proposals/ch05b.tsv`（18 条新术语）
生成日期：2026-11-15

---

## 一、覆盖范围（原书页 ↔ 生成页码）

- **起点**：原书 p.581 的节标题 “5.2. Objects representing equivalences, and groups of auto-equivalences.”（不含第 5 章章标题与 5.1 节）。
- **终点**：原书 p.589 第 2 段末 “…equals $2^{s}$, where $s$ is the number of prime divisors of $N$.”，即 `Bibliography` 之前。参考文献条目未译（由 Lead 在 `refs.tex` 处理）。
- **页数**：原书 9 页（581–589）→ 全书 11 页（PDF 82–92）；隔离构建 10 页。

全书构建（`build_ch05b/main.pdf`，136 页）中本块位于 **PDF p.82–p.92**（ch05a 落地、ch04 的环境错误修复之后的最终位置；此前一版构建为 p.97–106）。隔离构建（`_smoke_ch05b.tex` = preamble + 本块，输出 `build_ch05b_smoke/_smoke_ch05b.pdf`，10 页）的页对应为 1–10，比全书少一页，差别在章首页。

| 原书页 | 该页起首内容 | 全书 PDF 页 |
|---|---|---|
| 581 | `\section{代表等价的对象与自等价群}` + 本节重点 | 82 |
| 582 | 命题 5.2.2 | 83 |
| 583 | “先假定 $(0,0)$ 属于 $\cE$ 的支撑” | 84 |
| 584 | 命题 5.3.3 / 定义 5.3.2（§5.3 标题在 p.85） | 85–86 |
| 585 | 命题 5.3.7 | 87 |
| 586 | “$q_2(\Ker(q_1))\subset\Sigma^0(\cE)$”（p.585 末句的续句） | 88 |
| 587 | 命题 5.3.11 | 89 |
| 588 | 命题 5.3.12 | 90 |
| 589 | “把这样定义的从 $A$ 到 $B$ 的态射记作 $\psi$” | 91 |
| — | 章末评注末句“都在这套框架的覆盖之外” | 92 |

页标记 `% [原文 p.NNN]` 共 9 行（581–589 各一），单调无缺页。跨页两处（p.585→586 句中、p.588→589 例 5.3.15 内），标记按页图换页处插入。

---

## 二、`\figdiag` 登记表

**本块 0 个**：原书 p.581–589 没有二维交换图。三处“箭头带标注”的示意均为单行，按体例 §5 用行内数学手写，不需裁图、不进本表：

| 位置 | 写法 |
|---|---|
| p.584（$\Phi_\mu$ 的定义） | `\Phi_\mu=\im\bigl[D\xrightarrow{(l,\varphi_L)}D\times\hat D\bigr]` |
| p.587（命题 5.3.11 证明） | `\im\bigl[\hat A\xrightarrow{(\beta,\delta)}B\times\hat B\bigr]` |
| p.588（例 5.3.15） | `A\xrightarrow{(k\cdot\id,\,m\varphi_L)}A\times\hat A` |

另外，引理 5.2.1 证明中引用 5.1 节的**图 (51)**（属 ch05a 的图，编号未重排），只用文字引用，未重排图形。

---

## 三、陈述与公式清单（编号 ↔ 页码）

### 陈述 19 条（18 个环境 + 1 个构造）

（“隔离构建页”列的页码 +81 即全书 PDF 页：1→82，2→83，…，9→90。）

| 编号 | 类型 | 原书页 | 隔离构建页 | 备注 |
|---|---|---|---|---|
| 5.2.1 | 引理 | 581 | 1 | 带证明 |
| 5.2.2 | 命题 | 582 | 2 | 带证明；配译注 1 |
| 5.2.4 | 命题 | 583 | 3 | **原书印刷如此，应为 5.2.3**，见 §5-1 |
| 5.2.4 | 推论 | 583 | 3 | 与上一行同号（原书重复编号） |
| 5.3.1 | 定义 | 583 | 3 | 齐次丛 |
| 5.3.2 | 定义 | 584 | 4 | 幂单丛 |
| 5.3.3 | 命题 | 584 | 4 | （[28]、[30]），(i)(ii) 两条 |
| 5.3.4 | 定义 | 584 | 4 | 半齐次丛；配译注 2 |
| 5.3.5 | 命题 | 584 | 4 | （[30]，定理 5.8），(1)–(4) |
| 5.3.6 | 命题 | 584 | 4 | （[30]，7.10），(1)–(3) |
| 5.3.7 | 命题 | 585 | 5 | （[30]，6.15、6.16） |
| 5.3.8 | 引理 | 585 | 5 | 带证明；配译注 4 |
| 5.3.9 | 引理 | 585 | 5–6 | 带证明 |
| — | **构造 5.3.10** | 586 | 6 | 原书为 “Construction” 环境，本书无对应环境，按体例作粗体普通段落 |
| 5.3.11 | 命题 | 587 | 7 | 带证明 |
| 5.3.12 | 命题 | 588 | 8 | 带证明 |
| 5.3.13 | 定理 | 588 | 8 | 等价 ⇔ 等距同构 |
| 5.3.14 | 定理 | 588 | 8 | 正合列；配译注 5 |
| 5.3.15 | 例 | 588–589 | 9 | 跨页，`% [原文 p.589]` 在环境内部 |

### 编号公式 4 条（全部手工 `\tag`，无自动编号）

| 编号 | 原书页 | 隔离构建页 | 内容 |
|---|---|---|---|
| (52) | 582 | 2 | $K=\cE^\vee|_{(0,0)}\otimes\cE$ |
| (53) | 585 | 6 | $T^*_x(\cE)\cong\cE\otimes M$ |
| (54) | 585 | 6 | $\Sigma^0(\cE):=\{\delta\in\hat D\mid\cE\otimes\cP_\delta\cong\cE\}$ |
| (55) | 587 | 7 | $T^*_{(a_2-a_1,0)}\cE\cong\cE\otimes\cP_{(\alpha,\beta)}$ |

其余行间公式 26 处用 `equation*`（无号）。交叉引用一律写“命题 5.2.2”“式 (54)”形式，全文无 `\ref`。

---

## 四、译注清单

### `\yizhu` 5 条（正文可见）

| # | 位置（原书页） | 一句话 |
|---|---|---|
| 1 | p.582，命题 5.2.2 之后 | 解释“在平移意义下是层”的几何含义，并重述原书“对 K3 曲面不成立”的提示（A 级来源） |
| 2 | p.583，$\varphi_L$ 段之后 | $\varphi_L$、$\mathrm{NS}(D)\hookrightarrow\Hom(D,\hat D)$ 与自伴条件 $\hat\varphi=\varphi$ 的含义（A 级：Mumford [32]） |
| 3 | p.584，定义 5.3.4 之后 | 半齐次性是齐次性的放宽，两个不变量（斜率、平移缺陷）与对应 $\Phi_\mu$（A 级：[30]） |
| 4 | p.586，引理 5.3.9 之后 | $\Sigma^0(\cE)$ 是 $\Pic^0$ 方向的稳定化子，“阶 = 秩的平方”（A 级：[30] §7） |
| 5 | p.588，定理 5.3.14 之后 | 正合列的两层结构、不分裂与 2-上闭链（A 级：[37]） |

来源全部为 A 级（原书、[30] Mukai 1978、[32] Mumford 1970、[37] Orlov 2002），无 B 级、无黑名单来源；每条 ≤200 字。

### `% [Tutor Note]` 6 条（不印正文，进附录 B）

| # | 位置 | 内容 |
|---|---|---|
| 1 | 引理 5.2.1 之后 | 文字层把 $\mathbf{R}^{\bullet}\mathcal{H}om$ 抽成 “R·Hom”，从页图作 $\Rb\cH\mathrm{om}$ |
| 2 | 命题 5.2.4 之后 | **编号重复**：页图印 “Proposition 5.2.4” 而紧随的推论亦印 5.2.4；按顺序应为 5.2.3（引言亦引 5.2.3），照录并加注 |
| 3 | 命题 5.3.7 之后 | 陈述用 $\cF$ 表被滤链的丛、$\cE_i$ 表子商，与定义 5.3.2 的 $\cF_i$ 记号不一致；照录 |
| 4 | 引理 5.3.9 证明中（p.585–586 跨页处） | “it is known” 一句无证明，属跳步，可由命题 5.3.6 (3) 补齐（译者核对） |
| 5 | 构造 5.3.10 之后 | ①本书无 construction 环境，按体例作粗体段落；②$g$ 中的 $-\hat y^{-1}$ 指对偶同源 $\hat y$ 之逆，原书未说明 |
| 6 | 例 5.3.15 末段之后 | 末句 $\Ker(\varphi)$ 是 $\Ker(\varphi_L)$ 的简写（前几句均写 $\varphi_L$），照录 |

---

## 五、存疑与待核

1. **命题 5.2.4 / 推论 5.2.4 的编号重复（最重要）**。页图 `work/pages/p073.png` 明确印作 “Proposition 5.2.4.”，紧随其后为 “Corollary 5.2.4.”，两者同号；按 5.2.1、5.2.2 的顺序，该命题应为 **5.2.3**，而 `ch00a.tex`（引言）也正是引作“命题 5.2.3”。本译按体例 §3.3“原书编号异常时照录”处理：印作 5.2.4 + Tutor Note。**请 Lead 决定**：(a) 维持照录（则引言的“命题 5.2.3”成为悬空引用，建议在引言处加一句“原书此命题印作 5.2.4”）；(b) 改印 5.2.3（推论保持 5.2.4），此时需在报告与 Tutor Note 里说明改动理由。目前 `appendix_d` 的索引若自动抓取，会同时出现两个“5.2.4”。

2. **`src/chunks/ch04.tex` 曾缺一个 `\end{proof}`（阻断全书编译，非本块；现已修复，本条留档）**。此前第 192 行 `\begin{proof}` 之后直到文件末（第 253 行 `\chapterreview` 结束）都没有对应的 `\end{proof}`，全书构建报：
   `! LaTeX Error: \begin{proof} on input line 192 ended by \end{document}.`
   并且第 4 章的章末评注与**本块全部内容都被卷进该 proof 环境**（本块在当时那版构建里显示为 4.3/4.4 节）。我已于 2026-11-15 01:00 左右向 Lead 报告；目前该文件已补齐 `\end{proof}`，最新全书构建 `!` 计数为 0，本块节号亦恢复为 5.2/5.3。

3. **`src/chunks/ch05a.tex` 曾缺位（现已落地）**：当时第 5 章章标题缺失，本块的 `\section` 编作 4.3/4.4；现 `ch05a.tex` 已含 `\chapter{阿贝尔簇}` 与 `\section{阿贝尔簇上凝聚层范畴之间的等价}`，本块自动编为 5.2、5.3，无需改本块。

4. **评注框内段落无间距**。`preamble.tex:197` 的 `reviewbox` 未设 `parskip`，而 tcolorbox 默认 `\parindent=0`，于是五段评注在纸面上粘连成一块（已渲染核对：`build_ch05b_smoke/_smoke_ch05b.pdf` 第 10 页）。建议在 `reviewbox` 里统一加 `parskip=0.6em`（一处改动对全书五个 `\chapterreview` 同时生效）；我未擅自改动共享 preamble。

5. **p.585 末 “it is known that $q_2(\Ker q_1)\subset\Sigma^0(\cE)$”** 原书无证明、无出处，我只加 Tutor Note，未补证（补证会涉及命题 5.3.6 的次数计算，超出“不补原文没有的内容”的边界）。

6. **术语取舍**（已写 `work/proposals/ch05b.tsv`，18 条）：`isometric isomorphism`→等距同构（与全稿“霍奇等距”并行，沿用疑点清单的暂定）；`simple vector bundle`→单向丛（区别于“单丛/单射”，请 Lead 在术语表统一时定夺）；`unipotent bundle`→幂单丛（代数群惯例）；`slope`→斜率；`correspondence`→对应。另：原书把 $\End$ 排成花体 $\cE\mathrm{nd}$（因 $\cE$ 是层名），本译照页图作 `\cE\mathrm{nd}(\cE)`，与 `\End(A)`（正体，例 5.3.15）并存。

7. **p.588 例 5.3.15 的 $N$**：原书只说 $\varphi_M\circ\varphi_L=N\cdot\id_A$（$N>0$），未言 $N$ 与 $\mathrm{NS}(A)$ 生成元的次数有何关系；译文中照录，未补充解释。

---

## 六、编译自检结果

命令（独立 output-directory，绝对路径）：

```
cd <HOME>\Downloads\orlov_derived_work\src
lualatex -interaction=nonstopmode -output-directory=<HOME>\Downloads\orlov_derived_work\build_ch05b main.tex
lualatex -interaction=nonstopmode -output-directory=<HOME>\Downloads\orlov_derived_work\build_ch05b_smoke _smoke_ch05b.tex
```

（lualatex 返回 exit code 1 是 MiKTeX 更新提示，按说明忽略；PDF 正常写出。）

**A. 隔离构建（本块 10 页，`build_ch05b_smoke/_smoke_ch05b.log`）—— 本块自身零问题：**

| 项目 | 计数 |
|---|---|
| `!` 错误 | **0** |
| `Undefined control sequence` | **0** |
| `Missing character` | **0** |
| `Overfull \hbox` | **0** |
| `Underfull \hbox` | **0** |

**B. 全书构建（`build_ch05b/main.log`，136 页）：**

| 项目 | 计数 | 说明 |
|---|---|---|
| `!` 错误 | **0** | ch04 的 `\end{proof}` 补齐后归零 |
| `Undefined control sequence` | **0** | 本块原有 3 处 `\NS`（未定义宏），已改为 `\mathrm{NS}` |
| `Missing character` | **0** | 此前 3 条 `α (U+03B1)`（源头 `ch03a.tex:81` 的 Tutor Note 经 `appendix_b.tex:112` 印出）已由他块修掉 |
| `Overfull \hbox` | **1** | 唯一一条在 `ch03a.tex:30` 的章首页（`Overfull \hbox (81.81061pt too wide) in paragraph at lines 30--30`，位于 PDF p.36–37 之间），非本块；本块隔离构建 0 条 |
| `Underfull \hbox` | **0** | — |

**C. 视觉核对**（`latex_look`，隔离构建）：第 1、2、5、10 页已逐页看过——陈述标题粗体、编号齐整，译注框左侧竖线正常，`(52)` 右对齐正常，`\takeaway`/`\chapterreview` 彩框正常，无溢出行；§5.3 的 `\takeaway` 改稿后重编仍 10 页、四项计数全零。
