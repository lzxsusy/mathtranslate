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
- 图：原文 PDF 图直接 `\includegraphics`，图注照译；GMN1 无插图（核对过源码，无 `\includegraphics`）。
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
