# STYLE_GUIDE —— GMN 系列中译的统一文风与机械规范（GMN3 版）

本文件是全系列的「排版与用词宪法」。单篇 BRIEF 可以加限定，但不得与本文件冲突。改动本文件需说明理由并同步已译各章。本版由 GMN2 版改写：删去 GMN2（0907.3987）专有项，补入 GMN3（1006.0146）的术语与坑。

## 一、文件与编译

```
源码/
  main.tex        主控（导言区在 preamble.tex）
  preamble.tex    ctex + 数学宏 + 定理环境 + 译注环境
  chunks/chNN.tex 每块一个文件（ch01…ch16；ch15 内含 \appendix）
  refs_bbl.tex    参考文献（由原文 .bbl 机械转换，make_bbl.py）
  figures/        插图（原文 PDF 图直接复制，不重画）
成品/             编译产物 PDF
工程文件/
  BRIEF.md  STYLE_GUIDE.md  make_bbl.py  qa.py
  work/     通读笔记、疑点清单、eqnum.py、chunk_stats.py
  reports/  施工记录
```

- 编译：`cd 源码 && xelatex -interaction=nonstopmode main.tex` ×3。**必须 0 error**；overfull > 3pt 要修；不得有 `??` 或未定义引用（Underfull \hbox 若只来自 `refs_bbl.tex` 的 DOI/URL 行可接受，须在报告里注明）。
- 每块独立可编：`main.tex` 里只 `\input` 已完成的块，未完成的块留注释。
- 文档类固定 `ctexart`，`fontset=fandol`，`scheme=chinese`，A4，边距 2.6cm，行距 1.18，`\numberwithin{equation}{section}`。
- 附录：`\appendix` 写在 **ch15 开头**（§13 + 致谢之后），main.tex 不再重复；`refs_bbl` 置于末尾。

## 二、术语（硬性表，违反即返工）

| 英文 | 中文 | 依据 |
|---|---|---|
| framed BPS state | **带框 BPS 态**（首现括注 framed BPS state） | 本文新术语；术语表旧条作「framed BPS 态」，书名取「带框」，冲突见疑点清单 |
| vanilla BPS state | **「原味」BPS 态** | 原文 §3.1 的戏称；保留引号 |
| framed BPS index | 带框 BPS 指标 | 原文 (1.1) 后 |
| protected spin character (PSC) | **保护自旋特征标**（PSC） | 原文 §3.2，(3.12)(3.14) |
| spin character | 自旋特征标 | 同上 |
| refined BPS index | 精细化 BPS 指标 | 原文 §3.2 |
| halo | **保留拉丁原文**（halo 束缚态 / halo 构型 / halo Fock 空间） | 原文 §3.3；与超引力 halo 同源 |
| halo Fock space | halo Fock 空间 | 原文 §3.3 |
| wall-crossing (formula) | 穿墙（公式） | 数译全库 83/31 处；**不用**「墙穿越」 |
| wall of marginal stability | 边缘稳定墙 | 全库 25 处；**不用**「边际稳定」 |
| semiprimitive | 半本原 | 原文 §3.5；KS 公式的半本原情形 |
| motivic wall-crossing formula | motivic 穿墙公式 | 原文 §3.5；motivic 不译 |
| quantum dilogarithm | 量子双对数 | 原文 §3.4 |
| BPS state / BPS degeneracy | BPS 态 / BPS 简并度 | 全库 320 / 62 处 |
| BPS ray | BPS 射线 | 原文 §3.4、§4.1 |
| central charge | 中心荷 | 全库 479 处 |
| line operator | 线算子 | 全库通行 |
| 't Hooft–Wilson operator | 't Hooft–Wilson 算子 | 人名保留；首现括注 |
| Wilson line | Wilson 线 | 原文 §10 |
| vacuum expectation value | 真空期望值（vev） | vev 可直接用，首现给全称 |
| hyperkähler | 超凯勒 | 全库 157 处 |
| Kähler | 凯勒 | 通行 |
| Coulomb branch | 库仑分支 | 全库 412 处 |
| multiplet / hyper / vector | 多重态 / 超多重态 / 矢量多重态 | 全库 2044 / 1006 / 377 |
| moduli space | 模空间 | 通行 |
| Darboux coordinates | 达布坐标 | 全库 7 处 |
| holonomy | 和乐 | 原文 §7、§11 |
| flat connection | 平坦联络 | 原文 §7 |
| puncture | **穿刺点** | 术语表第 125 行（数译库 588 处）；**不写「尖点」、不留英文** |
| lamination | 叶层（首现括注 lamination） | 术语表 76 / 100 行，状态「待议」；本文 §9.4 定义 |
| traffic rule | **保留拉丁原文**（traffic rule 算法） | 原文 §9.3、附录 F.2；不译 |
| cluster algebra | 簇代数 | 原文 §5 |
| cluster transformation | 簇变换 | 原文 §5.1 |
| exchange matrix | 交换矩阵 | 原文 §5.1 |
| tropical / tropical label | 热带 / 热带标签 | 原文 §12 |
| Laurent phenomenon | 洛朗现象 | 原文 §5.1 |
| strong positivity | 强正性 | 原文 §3.2 猜想 |
| generating function | 生成函数 | 原文 §3.2 |
| deformed ring | 形变环 | 原文 §3.6 |
| spectrum generator | 谱生成元 | 原文 §11 |
| Fock–Goncharov coordinates | Fock–Goncharov 坐标 | 人名不音译 |
| decorated / ideal / limit triangulation | 装饰三角剖分 / 理想三角剖分 / 极限三角剖分 | 原文 §9.4、附录 F |
| juggle / flip / pop | **保留拉丁原文**，不译 | 与 GMN2 一致 |
| Argyres–Douglas | Argyres–Douglas（保留） | 原文 §4.3、§10.1 |
| Taub-NUT | Taub-NUT（保留） | 原文 §8.1 |
| millipede expansion | **millipede 展开**（首现括注「千足虫展开」，中译名待议） | 原文 §10.8 |
| dyon | 双荷子 | 原文 §1 |
| Seiberg–Witten | 塞伯格–威滕（首次）；其后 SW | 人名规则例外（已固定） |
| Kontsevich–Soibelman | Kontsevich–Soibelman（不音译）；其后 KS | 人名保留拉丁原文 |
| class $\CS$ | $\CS$ 类理论（首现括注「取『六』之意」） | 与 GMN2 一致 |
| $\CN=2$ supersymmetry | $\CN=2$ 超对称 | 保留数学模式 |
| hypermultiplet moduli space | 超多重态模空间 | 原文 §7.3 |
| Tchebyshev polynomial | 切比雪夫多项式（首现括注 Tchebyshev） | 原文附录 G |

**人名规则**：**一律保留拉丁原文**（Gaiotto、Moore、Neitzke、Kontsevich、Soibelman、Fock、Goncharov、Seiberg、Witten、Nekrasov、Argyres、Douglas、Taub、NUT、Tchebyshev…），**不新造中文音译**。仅当某译名已在汉语文献中固定下来（如「黎曼」「希尔伯特」「切比雪夫」）才用汉字。参考文献条目一律保留原文，不译。
**不译的专名**：BPS、WKB、K3、SW、DT、arXiv 编号、vev、PSC、halo、traffic rule、motivic、cluster（仅作 cluster algebra 时译簇代数）、juggle、flip、pop、millipede。

## 三、中文文风

1. **一句一意**：原文的 60 词长句，中文常要拆成两三句；不许为对齐原文而写出「的的」连环。
2. **逻辑词显式**：「indeed」「on the one hand/other hand」「in particular」译出，不省。
3. **语气保真**：`we expect` → 「我们预期」；`it would be interesting` → 「……将会很有意思」；`we do not understand` → 「我们尚不理解」。不得升格或降格。
4. **数字与单位**：`$d=4$`、`$\CN=2$` 保留数学模式；「四维」只作形容词（四维理论）。
5. **破折号**：中文用「——」；英文人名间用 en dash（`--`）。
6. **引号**：中文引号「」；原文引号内的英文术语保留英文。
7. **脚注**：原文脚注照译，编号随文；译者补充的说明另用 `\zy{}`（橙色【译注】），长说明一律 `yizhu` 环境放块末。**GMN3 的 §1 没有脚注**，其余各节以原文为准。

## 四、公式与图表

- 公式**逐字符**对照原文；行内公式不改写、不「化简」。
- 多行公式用 `align`；原文 `\be…\ee`（本文真的是 `equation` 环境）对应译文的 `equation`，原文不编号才用 `\[…\]`。
- 公式编号：`\numberwithin{equation}{section}`，与原文一致（(1.1)、(3.12)…）。**译文不得增删公式**；若原文一处公式被拆成两行显示，编号仍挂在第一行。
- 引用：块内用 `\eqref{}`；跨块引用 v0.1 阶段写原文编号（如 (6.3)）并加 `% TODO 合稿改 \eqref{eq:...}`。原文 label 名照抄（如 `eq:trh-large-r`、`eq:Def-Framed-PSC`）。
- 图：原文 PDF 图直接引用，图注照译。**本文 52 幅图**：一律用 preamble 的 `\insfig[宽度]{文件名}{图注}`（宽度缺省 `0.8\textwidth`；内部拼 `figures/<文件名>-crop.pdf` 并加 `\label{fig:<文件名>}`），文件名照抄原文 `\insfig` 的第一参数，不重画、不裁切。`\instwofigs` / `\insthreefigs` 照原文 6 / 9 参定义使用。
- 表格：`booktabs`，表注照译。

## 五、译注的使用门槛

只在以下情形加：
1. 术语有多个中文译法且读者可能误解（如 framed、lamination、halo 的处理）；
2. 原文记号与通行记号不同（如 `\fro` 是 $\overline{\underline{\Omega}}$、`\nsing` 是穿刺点个数）；
3. 原文有笔误或前后不一致（须同时记入 `资料卡/04-术语文献勘误.md`）。

不加：个人理解、延伸、文献补充、「这里是重点」。

## 六、章节标题

- 一级标题照译，副标题用「：」分隔：`\section{带框穿墙}`。
- 原文的 `\subsection*{…}`（不编号）照译，编号由 LaTeX 自动生成（与原文节号一致，因为块顺序相同）。
- 附录标题照译，`\appendix` 由 ch15 负责；附录字母编号由 LaTeX 自动给出（A–G），与原文一致。

## 七、提交前自检清单

- [ ] `xelatex` ×3 后 0 error、无 overfull > 3pt、无 `??`、无未定义 citation
- [ ] 块内公式编号与原文一一对应（随机抽 5 个回 PDF 核对；跨块引用见 `% TODO`）
- [ ] 术语全部命中硬性表；新术语已入 `glossary_master.tsv`（只追加）
- [ ] 段数与原文对照（漏段是最高频事故）
- [ ] 图号与原文对照（`\insfig` 名逐字）
- [ ] `进度.md` 与本篇 `BRIEF.md` 状态已更新

## 八、GMN3（1006.0146）专用规则

本篇篇名：《带框 BPS 态》（Framed BPS States），124 页（印刷 123），编号公式 333 条（PDF 行末实测），插图 52 幅，参考文献 84 条。

1. **`\be`/`\ee` 是公式环境，别学 GMN2**：原文 `\def\be{\begin{equation}}`、`\def\ee{\end{equation}}`；GMN2 的 `\be` 是 `\bar e`。移植旧经验前先看本文导言区。
2. **`\sect` 重置式号**：`\newcommand{\sect}[1]{\setcounter{equation}{0}\section{#1}}`；译文靠 `\numberwithin{equation}{section}` 复现，若原文混用 `\section` 会整体错位——每块抽 5 条回 PDF 核对，`work/eqnum.py` 有全文 label→式号可查。
3. **framed 与 vanilla 是一条线**：带框 BPS 态 = 线算子存在时的 BPS 态；原味 BPS 态 = 没有线算子时的普通 BPS 态。$\zeta$ 是 $S^1$ 的角变量，$y$ 是 PSC 的自旋变量（$y=-1$ 退化为指标），两者**不可互换**。
4. **halo 的图像**：BPS 粒子云束缚在线算子上，逐层「套」上去，形成 halo Fock 空间；halo 与「墙」无关，不要与穿墙的墙混写。
5. **traffic rule 是算法名，保留拉丁**：附录 F.2 给出局部规则，§9.3、§10 用它算 framed BPS 谱。译文写「traffic rule 算法」（空格），不用连字符（否则会被 TeX 折成 traf-fic）。
6. **lamination 的层次**：§9.4 定义在装饰黎曼面 $C$ 上；叶层不是三角剖分的边，而是「带权重的曲线族」；traffic 在叶层上做。与 GMN2 的 lamination 同源、同译「叶层」。
7. **簇代数与热带标签是两条平行线索**：§5 讲 $\CN=2$ 理论的形式线算子代数就是簇代数，§12 讲热带极限下的标签；两节的 $X_\gamma$、$y$、$q$ 记号要逐节核对。
8. **六维记号**：$C$ 是黎曼面，$R$ 是半径，$\epsilon_1,\epsilon_2$ 是 $\Omega$-背景参数，$q=e^{\epsilon_1}$；六维部分（§7、附录 E）与四维部分的 $\zeta$、$y$ 不要混。
9. **`\N` 是 $\mathcal N$**，`\CN` 同义；bbl 里一处 `\N` 已由 `make_bbl.py` 转 `\CN`。
10. **引理的编号**：原文定理/引理无统一计数（多为行内陈述），译文不新造定理环境，除原文明确编号者外一律用正文叙述，避免增删编号。
