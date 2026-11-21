# BRIEF · SY02-15 相对朗兰兹对偶（LAWRGE 2024 讲义）

## 原文

| 项 | 内容 |
|---|---|
| 原题 | *LAWRGE 2024 Notes*（2024 Los Angeles Workshop on Representations and Geometry，参会者笔记） |
| 主题 | *Relative Langlands Duality* |
| 讲者 | David Ben-Zvi、Yiannis Sakellaridis、Akshay Venkatesh |
| 记录者 | 研讨会参会者集体（各节另有 Written by / Typed by 署名，译本照保留） |
| 版本 | MiKTeX pdfTeX 1.40.25，2024-12-02 生成，无元数据 |
| 规模 | 73 页；15 节＝15 场报告（Day1 三场、Day2 四场、Day3 三场、Day4 两场、Day5 三场） |
| 结构 | 无目录页、无文献表、无附录；引用一律以脚注给出 |
| 文件名 | `20-BenZvi_LAWRG2024_lectures.pdf` |

**原文性质**：这是研讨会笔记，不是论文。p1 有集体免责声明（「极不完整、未校订，错误归于记录噪声」）；正文保留大量口语、`?` 标记、自承错误（(11.12) 写着 *not true, to be corrected*）、断号（(13.1)(13.2)、(15.2) 被计数器吃掉）与整页白板照片（p70、p71）。**译本必须忠实保留这些痕迹，不得替作者「修正」。**

## 一句话主旨

Langlands 猜想在 4 维 TQFT 的语言下可以「加一个边界条件」而不改变形状：球 $G$-簇 $X$ 给出周期层 $P_X$，对偶侧给出 $(\check G,\check M)$ 与 $L$-层 $L_{\check M}$，两者匹配即相对朗兰兹对偶，而 $L$-函数就是这一配对在不动点上的局部因子。

## 五步逻辑链

1. **TQFT 语言**（§1–§4）：$A_G$ 把 3-流形送向量空间、2-流形送范畴；相对朗兰兹 = 带边配边的边界条件 $\Theta_{G,X}$。
2. **局部代数核心**（§5–§6）：Riemann $\zeta$ 的「奇迹」与 Satake 同构 $H_G\simeq\mathbb C[\mathrm{Rep}\,\check G]$，把分析问题变成 $H_G$-模问题。
3. **Hecke 范畴**（§7）：$\mathrm{Bun}_G(\text{raviolo})=G(O)\backslash G(F)/G(O)$，几何 Satake 与 spectral action 把 $H_G$ 的作用几何化。
4. **球簇的一般理论**（§8–§10）：重数自由 $\iff$ 球簇（Thm 8.19）；$\check G_X$、相对 Cartan $A_X$、小 Weyl 群 $W_X$、$SL_2$-三元组、超球簇。
5. **匹配猜想与验证**（§11–§15）：局部 Plancherel 猜想 → 整体几何猜想（Beilinson 投影后 $P_X\mapsto L_{\check M}$）→ Iwasawa–Tate 检验 (13.29)–(13.35) → $L$-层纤维 $=\bigoplus\wedge^*H^1(T_x)$。

## 分块表

页码为 PDF 页；行号为 `工程文件/work/原文/chNN.txt` 在 `full.txt` 中的位置（由 `scripts/split_chunks.py` 生成，见 `work/原文/chunk_map.tsv`）。

| 块 | 节 | PDF 页 | 原文行 | 编号条目 | 图 | 目标文件 | 状态 |
|---|---|---|---|---|---|---|---|
| ch01 | §1 TQFT 导论 | 1–7 | 23–254 | 8 | 内联 4（拼贴、单位、迹、乘法图） | `chunks/ch01.tex` | ☑ 完成 |
| ch02 | §2 算术拓扑与 Langlands | 7–12 | 255–470 | 2 | Fig 2.1–2.4 | `chunks/ch02.tex` | ☑ 完成 |
| ch03 | §3 相对 Langlands（Yiannis） | 12–18 | 471–735 | 3 | 内联 2（配边、边界条件） | `chunks/ch03.tex` | ☑ 完成 |
| ch04 | §4 自守理论、Hecke 算子 | 18–24 | 736–978 | 8 | Fig 4.1–4.3 + 内联菱形图 | `chunks/ch04.tex` | ☑ 完成 |
| ch05 | §5 奇迹 / Mellin / Satake | 24–29 | 979–1249 | 21 | 0 | `chunks/ch05.tex` | ☑ 完成 |
| ch06 | §6 局部模型例 | 29–31 | 1250–1370 | 0 | 内联 1（$(q+1)$-正则树） | `chunks/ch06.tex` | ☑ 完成 |
| ch07 | §7 Hecke 范畴与几何 Satake | 31–38 | 1371–1645 | 11 | 内联 3（raviolo、裤衩） | `chunks/ch07.tex` | ☑ 完成 |
| ch08 | §8 球簇 | 38–44 | 1646–1980 | 23 | 0 | `chunks/ch08.tex` | ☑ 完成 |
| ch09 | §9 历史与设定（Venkatesh） | 44–48 | 1981–2120 | 2 | 内联 2（树、匹配图） | `chunks/ch09.tex` | ☑ 完成 |
| ch10 | §10 球簇的对偶群 | 48–53 | 2121–2434 | 22 | 内联 2（类型表、锥） | `chunks/ch10.tex` | ☑ 完成 |
| ch11 | §11 Plancherel 与局部猜想 | 53–56 | 2435–2603 | 16 | 0 | `chunks/ch11.tex` | ☑ 完成 |
| ch12 | §12 整体设定与 $L$-函数史 | 56–60 | 2604–2797 | 0 | 0 | `chunks/ch12.tex` | ☑ 完成 |
| ch13 | §13 整体几何猜想 | 60–66 | 2798–3112 | 35 | 内联 2 | `chunks/ch13.tex` | ☑ 完成 |
| ch14 | §14 全分歧与 Whittaker | 66–71 | 3113–3265 | 8 | 白板照片 1（p70） | `chunks/ch14.tex` | ☑ 完成 |
| ch15 | §15 不动点与 $L$-层纤维 | 71–73 | 3266–3366 | 5 | 白板照片 1（p71） | `chunks/ch15.tex` | ☑ 完成 |

## 施工流程（每块）

1. 读 `work/通读笔记.md`、本 BRIEF、`work/glossary.tsv`、上一块 `work/handoff/chNN.md`。
2. 打开 `work/原文/chNN.txt` 读原文；**同时打开对应页面图 `work/pages/pNNN.png`（170 dpi）逐符号核对公式与定理陈述**——文本层的公式一律不可用。
3. 写 `源码/chunks/chNN.tex`：保留原文编号、保留 `?` 与自承错误、术语按冻结表、不补写、不合并步骤。
4. 单块编译（`xelatex chNN_draft.tex`），查未定义引用、Overfull、缺字。
5. 写 `work/reports/chNN.md`（5 行：页范围/条目数/译注数/回图核对处/遗留问题）、`work/handoff/chNN.md`（200 字）。
6. 回写 `work/glossary.tsv`、`work/疑点清单.tsv`、`work/cost_log.tsv`。

## 质量标准

- 忠实：编号条目与原书逐条对齐；公式逐符号与页面图一致；原文省略/含糊/笔误照译并批注。
- 排版：定理与公式共号（`\newtheorem{...}[equation]{...}`）；图号按节（`\numberwithin{figure}{section}`）；断号处用计数器对齐，不重排。
- 语言：一句一逻辑重心，≤60–70 汉字，全角标点，英文术语与汉字间半角空格。
- 译注：只在会误解处，≤120 字，必须带 `[来源：…]` 或 `[译者按（无外部依据）：…]`。
- 编译：未定义引用 0、重复书签 0、Overfull 0、缺字 0。

## 交付物

- `源码/`：`main.tex`、`preamble.tex`、`chunks/ch01–ch15.tex`、`figures/`
- `工程文件/`：`BRIEF.md`、`work/`（通读笔记、疑点清单、glossary、原文、pages、reports、handoff、cost_log）、`reports/`、`scripts/`
- `资料卡/`：五件套（第二步）
- `投稿信息.md`

## 已知坑

1. **文本层公式不可用**：分式/上下标/大括号被打散成多行（`Z\nG∨\nc` 实为 $\int_{\check G^\vee_c}$）；`§n¡1` 是 $\Sigma^{n-1}$，`@in` 是 $\partial_{\mathrm{in}}$，`Ξ` 有时是 $\Sigma$。**每条公式回图。**
2. **$\check G$ 与 $\hat G$**：原文用「check」，不要打成 hat。
3. **编号断号**：(13.1)(13.2)、(15.2) 在印刷面不存在但计数器已进；译本用 `\addtocounter{equation}{2}`（或 1）对齐，不得重新编号。
4. **定理环境共号**：原文 Example/Remark/Definition/Theorem 与公式共用一个节内计数器；(8.1) 是 Example 8.1 而不是公式。
5. **白板照片**：p70、p71 各一张，是原文本体，须裁图保留。
6. **未编号内联示意图**：文本层已成乱码，需从 300 dpi 页面图裁；重绘者必须在 `reports/` 登记「本图为译者重绘」。
7. **脚注编号**：原文脚注按页编号（1,2,3…每页重置？——以页面图为准）；译本的 `\footnote` 全书连续，须在报告中登记「脚注编号与原文不一致，内容按原文位置」。
