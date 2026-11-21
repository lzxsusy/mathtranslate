# STYLE_GUIDE —— GMN 系列中译的统一文风与机械规范

本文件是全系列的「排版与用词宪法」。单篇 BRIEF 可以加限定，但不得与本文件冲突。改动本文件需说明理由并同步已译各章。

## 一、文件与编译

```
源码/
  main.tex        主控（导言区在 preamble.tex）
  preamble.tex    ctex + 数学宏 + 定理环境 + 译注环境
  chunks/chNN.tex 每块一个文件（ch01, ch02, …, appA, …）
  refs_bbl.tex    参考文献（由原文 .bbl 机械转换）
  figures/        插图（原文 PDF 图直接复制，不重画）
成品/             编译产物 PDF
工程文件/
  BRIEF.md  STYLE_GUIDE.md  build.ps1
  work/     通读笔记、疑点清单、术语表
  reports/  施工记录
```

- 编译：`build.ps1`（xelatex ×3）。**必须 0 error**；overfull > 3pt 要修。
- 每块独立可编：`main.tex` 里只 `\input` 已完成的块，未完成的块留注释。
- 文档类固定 `ctexart`，`fontset=fandol`，`scheme=chinese`，A4，边距 2.6cm，行距 1.18。

## 二、术语（硬性表，违反即返工）

| 英文 | 中文 | 依据 |
|---|---|---|
| wall-crossing (formula) | 穿墙（公式） | 数译全库 83/31 处；**不用**「墙穿越」 |
| wall of marginal stability | 边缘稳定墙 | 全库 25 处；**不用**「边际稳定」 |
| BPS state | BPS 态 | 全库 320 处 |
| BPS degeneracy | BPS 简并度 | 全库「简并度」62 处 |
| central charge | 中心荷 | 全库 479 处 |
| hyperkähler | 超凯勒 | 全库 157 处 |
| quaternionic-Kähler | 四元数凯勒 | 通行 |
| Kähler | 凯勒 | 通行 |
| Coulomb branch | 库仑分支 | 全库 412 处 |
| multiplet / hyper / vector | 多重态 / 超多重态 / 矢量多重态 | 全库 2044 / 1006 / 377 |
| moduli space | 模空间 | 通行 |
| symplectomorphism | 辛同胚 | 全库 308 处 |
| semiflat metric | 半平坦度量 | 全库「半平坦」92 处 |
| twistor (space) | 扭量（空间） | 全库 14 处 |
| Darboux coordinates | 达布坐标 | 全库 7 处 |
| isomonodromic deformation | 等单值形变 | 全库 3 处 |
| spectral network | 谱网络 | 全库 309 处（GMN2 起大量出现） |
| WKB approximation | WKB 近似 | 全库 31 处 |
| line defect | 线缺陷 | 全库 40 处 |
| BPS instanton / multi-instanton | BPS 瞬子 / 多瞬子 | 本文特有用法，见译注 |
| Riemann–Hilbert problem | 黎曼–希尔伯特问题 | en dash，不写「黎曼希尔伯特」 |
| Kontsevich–Soibelman | Kontsevich–Soibelman（不音译）；其后 KS | 人名保留拉丁原文 |
| Seiberg–Witten | 塞伯格–威滕（首次）；其后 SW | 同上 |
| thermodynamic Bethe ansatz | 热力学贝特拟设 | 通行 |
| theta functions / tt* equations | theta 函数 / $tt^*$ 方程 | 保留原文记号 |
| turning point | **转向点** | 冻结表第 72 行；**不用**「转折点」（交接说明的写法与冻结表冲突，以冻结表为准） |
| branch point | 分支点 | 原文 §6.1；与 ramification「分歧」区分 |
| spectral curve | 谱曲线 | 原文 §3.1；与 Seiberg–Witten 曲线同指时写「Seiberg–Witten 曲线（谱曲线）」 |
| WKB curve | WKB 曲线 | 原文 §6.1；finite WKB curve → 有限 WKB 曲线 |
| Stokes graph | 斯托克斯图 | 原文 §6 起；与 Stokes line 斯托克斯线、Stokes multiplier 斯托克斯乘子 区分 |
| Hitchin moduli space | Hitchin 模空间 | 原文 §4 |
| Fenchel–Nielsen coordinates | Fenchel–Nielsen 坐标 | 原文 §1、§5；人名不音译 |
| trace coordinates | 迹坐标 | 原文 §5；Fock–Goncharov 的另一组坐标 |
| abelianization | 阿贝尔化 | 原文 §5.2 起（谱网络/平坦联络的） |
| Novikov ring | 诺维科夫环 | 原文 §5 与附录（KS 的 DT 进路） |
| lamination | 叶层 | 冻结表已有（状态「待议」），本篇沿用「叶层」 |
| flip / juggle / pop / omnipop | **保留拉丁原文**，不译 | 原文 §5.9；omnipop = 同时对全部顶点作 pop |
| Higgs bundle | Higgs 丛 | 摘要、§4.2 |
| decorated / ideal / limit triangulation | 装饰三角剖分 / 理想三角剖分 / 极限三角剖分 | 原文 §5、§5.9 |
| spectrum generator | 谱生成元 | 原文 §11 |

**人名规则**：**一律保留拉丁原文**（Kontsevich–Soibelman、Seiberg–Witten、Witten、Nekrasov…），**不新造中文音译**；数译全库统计亦是拉丁名占绝对多数（Witten 2500 处 vs 威滕 122 处）。仅当某译名已在汉语文献中固定下来（如「嘉当」「黎曼」「希尔伯特」）才用汉字。参考文献条目一律保留原文，不译。
**不译的专名**：BPS、WKB、K3、SW（作形容词时）、Donaldson–Thomas、Bridgeland、Joyce、Hitchin、LeBrun、Cecotti–Vafa、Ooguri–Seiberg、TBA（可作「TBA 方程」）、arXiv 编号。

## 三、中文文风

1. **一句一意**：原文的 60 词长句，中文常要拆成两三句；不许为对齐原文而写出「的的」连环。
2. **逻辑词显式**：「indeed」「on the one hand/other hand」「in particular」译出，不省。
3. **语气保真**：`we expect` → 「我们预期」；`it would be interesting` → 「……将会很有意思」；`we do not understand` → 「我们尚不理解」。不得升格或降格。
4. **数字与单位**：`$d=4$`、`$N=2$` 保留数学模式；「四维」只作形容词（四维理论）。
5. **破折号**：中文用「——」；英文人名间用 en dash（`--`）。
6. **引号**：中文引号「」；原文引号内的英文术语保留英文。
7. **脚注**：原文脚注照译，编号随文；译者补充的说明另用 `\zy{}`（橙色【译注】），正文一律 `yizhu` 环境放章末。

## 四、公式与图表

- 公式**逐字符**对照原文；行内公式不改写、不「化简」。
- 多行公式用 `align`；原文的 `\be…\ee` 对应 `equation`。
- 公式编号：`\numberwithin{equation}{section}`，与原文一致（(1.1)、(2.18)…）。**译文不得增删公式**；若原文一处公式被拆成两行显示，编号仍挂在第一行。
- 引用：块内用 `\eqref{}`；跨块引用暂写原文编号（如 (2.18)）并加 `% TODO 合稿改 \eqref`。
- 图：原文 PDF 图直接 `\includegraphics`，图注照译。**GMN2 有 80 幅图**：一律用 preamble 里定义的 `\insfig{宽度}{文件名}{图注}`（等价于 `width` + `figures/<文件名>-crop.pdf` + `\label{fig:<文件名>}`），文件名照抄原文 `\insfig` 的第二参数，不重画、不裁切。
- 表格：`booktabs`，表注照译。

## 五、译注的使用门槛

只在以下情形加：
1. 术语有多个中文译法且读者可能误解（如 instanton 在这里指绕 $S^1$ 的组态）；
2. 原文记号与通行记号不同（如 $\degen\equiv\Omega$、$\vm\equiv\mathcal{B}$）；
3. 原文有笔误或前后不一致（须同时记入 `资料卡/04-术语文献勘误.md`）。

不加：个人理解、延伸、文献补充、「这里是重点」。

## 六、章节标题

- 一级标题照译，副标题用「：」分隔：`\section{四维穿墙：经由三维场论}`。
- 原文的 `\subsection*{Summary}`（不编号）译作 `\subsection*{小结}`，`Discussion` → `\subsection*{讨论}`。
- 编号小节照译，编号由 LaTeX 自动生成（与原文节号一致，因为块顺序相同）。

## 七、提交前自检清单

- [ ] `build.ps1` 0 error、无 overfull > 3pt
- [ ] 块内公式编号与原文一一对应（随机抽 5 个回原文核对）
- [ ] 无 `??`、无 `\ref` 悬空、无未定义 citation
- [ ] 术语全部命中硬性表；新术语已入 `glossary_master.tsv`
- [ ] 段数与原文对照（漏段是最高频事故）
- [ ] `进度.md` 与本篇 `BRIEF.md` 状态已更新

## 八、GMN2（0907.3987）专用规则

本篇篇名：《穿墙、Hitchin 系统与 WKB 近似》（Wall-crossing, Hitchin Systems, and the WKB Approximation），180 页，编号公式约 544 条，插图 80 幅，参考文献 93 条。

1. **三套 $X$ 不许混**：$X^{\rm RH}_\gamma$（黎曼–希尔伯特解）、$X^\vartheta_\gamma$（本文构造的典范坐标）、$X^T_E$（Fock–Goncharov 坐标）。原文用 $\CX$ 统一，译文一仍其旧，但上标逐字照抄，**任何上标改写都算错**。
2. **WKB 语汇内部的层次**：转向点（turning point）⊂ 分支点（branch point）之上另有边界点（singular point）；有限 WKB 曲线（finite WKB curve）起止于分支点或闭合；谱网络（spectral network）是 WKB 曲线族的极限；斯托克斯图（Stokes graph）是三角剖分的对偶图。各级术语不得互相顶替。
3. **与 GMN1 的「墙」严格分开**：GMN1/GMN2 的「穿墙」「边缘稳定墙」指模空间里的墙；WKB 几何里的「网络边」「壁（wall segment）」指 $C$ 上的曲线段。译文中后者一律写「网络边」「壁段」，**不写「墙」**。
4. **flip / juggle / pop / omnipop 保留原词**（斜体 `\emph{}` 首次出现），首次出现处可加一句括注；不新造中文译名。
5. **class $\CS$**：写作「$\CS$ 类理论」，首次出现时括注「取『六』之意」。
6. 原文 `\be…\ee` 在本篇是 `\bar e` 的含义，**不要**当公式环境；译文公式一律 `equation`/`align`。
7. 原文小节计数器被 `\sect` 宏重置，节号与公式编号是一一对应的（(3.74) 一定在 §3.2.4 内），**逐节核对编号，不要按 PDF 页序数式**。
8. 图号：原文 `\ref{fig:xxx}` 在 v0.1 阶段一律硬编码成 PDF 上的实际图号并加 `% TODO 合稿改 \ref`。
