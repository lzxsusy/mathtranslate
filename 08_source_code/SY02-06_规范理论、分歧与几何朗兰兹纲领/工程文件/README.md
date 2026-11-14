# 中文学术译本：Gukov–Witten《规范理论、分歧与几何朗兰兹纲领》

本目录是英文理论物理论文 **Gauge Theory, Ramification, And The Geometric Langlands Program**
（S. Gukov & E. Witten, arXiv:hep-th/0612073v2, 2007）的完整简体中文 LaTeX 译本，
含逐节「本节重点」、学术审校译注、从原文 PDF 精确裁切的 9 张图与 1 张表。

- **原文**：Sergei Gukov, Edward Witten, *Gauge Theory, Ramification, And The Geometric Langlands Program*,
  arXiv:hep-th/0612073v2 [hep-th], 8 Oct 2007, 160 pp.（后收入 *Current Developments in Mathematics, 2006*）
- **译本**：正文、脚注、图表标题全译；参考文献按学术惯例保留英文著录与原文编号。
- **规模**：111 页 PDF；正文与附录共 8 节、28 个小节；**252 个编号公式**（编号与原文逐一对应）；9 张图、1 张表；**78 条译注**、7 个「本节重点」方框；参考文献 91 条。
- **编译产物**：`main.pdf`

---

## 1. 编译方法

### 1.1 标准方式（XeLaTeX）

```bash
xelatex main.tex     # 第一遍
xelatex main.tex     # 第二遍，生成目录与交叉引用
```

- 引擎必须是 **XeLaTeX**（中文由 `ctex` 处理，不能用 pdfLaTeX）。
- 中文字体默认 `fontset=windows`（Windows 的 SimSun/SimHei/SimKai）；
  在 Linux/macOS 上把 `main.tex` 中 `fontset=windows` 改为 `fontset=fandol`（TeX Live 自带）即可。
- 依赖宏包：`ctex, amsmath, amssymb, mathtools, bm, geometry, graphicx, xcolor, tcolorbox, enumitem,
  booktabs, array, longtable, multirow, caption, cite, hyperref`（TeX Live 2022+ 完整安装自带）。

### 1.2 单二进制方式（无需 TeX Live）

本仓库在无 TeX 发行版的环境中用 [Tectonic](https://tectonic-typesetting.github.io/)（XeTeX 引擎）完成编译验证：

```bash
tectonic -X compile main.tex
```

## 2. 目录结构

```
deliverable-0612073/
├── main.tex                 导言区、标题页、章节装配、参考文献
├── main.pdf                 编译产物
├── macros.tex               原文 harvmac 记号宏的 LaTeX 移植（由 arXiv 源码自动生成）
├── MACROS.md                上述记号宏的对照表
├── SPEC.md                  翻译与排版规范（术语表、数学保真规则、批注格式）
├── REVIEW-NOTES.md          全部译注的汇总索引（权威文本在各分片行内）
├── README.md                本文件
├── sections/                正文分片，与原文节次一一对应
│   ├── s00-front.tex        题名页、摘要、译者说明、目录
│   ├── s01-intro.tex         §1 引言
│   ├── s02a-definition.tex   §2 开头、2.1 面算符的定义、2.2 参数的几何解释、2.3 θ 角
│   ├── s02b-duality.tex      §2.4 电磁对偶、2.5 θ 角平移、2.6 列维子群与更一般的面算符
│   ├── s03a-quotient.tex     §3 开头、3.1 超 Kähler 商、3.2 复观点、3.3 非正则情形
│   ├── s03b-parabolic.tex    §3.4 抛物丛、3.5 M_L(α;p) 的拓扑
│   ├── s03c-topology.tex     §3.6 M_H 的拓扑、3.7 仿射外尔群的作用
│   ├── s03d-nahm.tex         §3.8 Nahm 方程与 M_H 的局部奇点、3.9 Hitchin 纤维化
│   ├── s04a-branes.tex       §4 开头、4.1 无分歧情形回顾、4.2 带分歧的 σ 模型、4.3 膜、4.4 扭曲 D-模
│   ├── s04b-lines.tex        §4.5 线算符与单值性、4.6 表示与膜
│   ├── s05a-framework.tex    §5 开头、5.1 一般框架、5.2 B-模型
│   ├── s05b-amodel.tex       §5.3 A-模型
│   ├── s06-local.tex         §6 局部模型与弦论实现（6.1–6.4）
│   ├── sA-duality.tex        附录 A 对偶性回顾
│   ├── sB-notation.tex       附录 B 记号索引
│   ├── s10-refs.tex          参考文献（91 条，原文编号）
└── figures/                 9 张图（300 dpi PNG，逐张质检）
    └── FIGURE-QA.md         裁片质检记录（PDF 页码、裁切矩形、目视结论）
```

## 3. 排版与体例约定（改稿前请先读这一段）

1. **公式编号锁定原文编号**：每个公式写为 `\setcounter{equation}{N}` + `\begin{equation}\label{eq:X.Y}`，
   编号由 `\numberwithin{equation}{section}` 自动生成，因此与原文 (2.1)–(2.63)、(3.1)–(3.109)、(4.1)–(4.20)、
   (5.1)–(5.18)、(6.1)–(6.24)、(A.1)–(A.18) 逐一对应，可与原文 PDF 逐式对照。
   交叉引用用 `\eqref{eq:3.40}`。代价是：增删公式需同时改 `\setcounter`，这是刻意的选择。
2. **节标题层级与原文完全一致**，编号由 LaTeX 自动生成；每个 `\section`/`\subsection` 后紧跟 `\label{sec:<编号>}`。
3. **页码锚点**：正文每个小节标题前有注释 `% ==== 原文 §X.X：PDF 第 N 页（印刷第 N-1 页）====`，
   其中 **PDF 页码 = 原文印刷页码 + 1**。
4. **「本节重点」方框**（`keytakeaways` 环境，蓝色）是译者所加，非原文内容；标题后标「（译者所加）」。
5. **译注**（`yizhu` 环境，橙色）——成品中可见、全文连续编号，三类内容：
   - 审校批注：易错点预警、作者省略论证的点拨、物理图像补充；
   - `\begin{yizhu}[原文疑误]`：原文疑似笔误，**照原文保留公式**，注中说明理由与建议；
   - 编译期不出现 `[待确认]`（本次交付 0 条）。
   译注可整体关闭：`main.tex` 里 `\showyizhutrue` → `\showyizhufalse`，方框与编号全部消失，正文回到纯译本状态。
   `REVIEW-NOTES.md` 是与成品编号一一对应的索引。
6. **图、表编号自动生成**，与原文 Figure 1–9、Table 1 一一对应；图注末尾标注原文位置（PDF 页码）。
7. **文献引用**沿用原文 `\cite{refN}`，编号与原文 `[N]` 完全一致；参考文献表保留英文著录。
8. **原文 harvmac 记号宏**（`\EUM`、`\MH`、`\TT`、`\CA` 等）保留在 `macros.tex` 中，
   以保证数学与原文逐字一致；完整对照表见同目录 `MACROS.md`。

## 4. 本次交付的校验记录

- **编译**：XeTeX（Tectonic）完整编译通过，0 error；
  交叉引用与文献全部解析，无 `??`、无未定义引用。
- **公式**：252 个编号公式全部就位、区间与原文一致、节内连续无重复；
  复杂公式（矩阵、分段函数、谱序列表格、交换图、长根式）已逐式对照原文整页图像核验。
- **图/表**：9 张图与表 1 均已插入，图注中译并标注原文 PDF 页码；裁片逐张目视核验无切边、无正文渗入。
- **结构**：§1–§6 与附录 A、B 及其子节的层级、顺序与原文目录逐条比对一致。
- **译注**：成品中 78 条橙色方框，编号 1–78 与 `REVIEW-NOTES.md` 一致。
- **数学保真自动比对**：逐式对比「译文章节」与「机械转换的英文源」，

  `\setcounter` 序列、`\label`、`\cite`、`\ref`、`\eqref`、`\includegraphics` 与 252 个公式体全部一致。

## 5. 校对中发现的原文问题（19 条，均照原文保留并加注）

| 位置 | 原文页 | 原文 | 判断 / 建议 |
|---|---|---|---|
| §1 | PDF 4 | “In sections 2, we consider…” | sections 应为单数 section（只指第 2 节） |
| §1 | PDF 4 | “the action of the affine braid group on the cohomology…” | 按 §3.7 正文，上同调上的作用实为仿射外尔群；仿射辫群要到 §4.5 才在 A/B-膜上出现 |
| §2.1 | PDF 10 | $(1,0$) | 正文一处 `$` 位置错置（源码第 800 行），应为 $(1,0)$；PDF 渲染上几乎不可见 |
| §2.5 | PDF 16 | $\mathrm{Im}\,{}^L\tau=1/n_{\mathfrak g}\cdot\mathrm{Im}\,\tau$ | 与式 (2.19)、(2.23)–(2.24) 互逆性矛盾，应为 $1/(n_{\mathfrak g}\,\mathrm{Im}\,\tau)$ |
| §2.5 | PDF 17 | “eqn. (4.1)” | 应为式 (2.52)：源码两个公式共用引用宏，后定义者覆盖前者（详见源码注释） |
| §2.6 | PDF 28 | “second Stieffel–Whitney class” | Stieffel 应为 Stiefel |
| §3.4 | PDF 48 | “Narashimhan” | 应为 Narasimhan |
| §3.5 | PDF 56 | “the fibrations (3.41) and (3.42) are precisely valid” | 此处指纤维化，应为 (3.38) 与 (3.39)；(3.41)/(3.42) 是上同调正合列 |
| §3.5 | PDF 61 | $\sum_a y_a=1$ | 与前文 $\sum_a y_a=0$（$\alpha=i\,\mathrm{diag}(y)$ 无迹）矛盾 |
| §3.6 | PDF 67 | 式 (3.81) 后 “$3g$” | 应为 $3g_C$（同句上限与 $V$ 的维数均为 $3g_C$） |
| §3.6 | PDF 65 | “a singularity of whose codimension is twice as great” | 英文语法错误，语义为“其奇点的余维是前者的两倍” |
| §3.7 | PDF 71–72 | 余权族指标 $i=1,\dots,n$ | 同段其余均为 $s$，应为 $i=1,\dots,s$ |
| §3.8 | PDF 77 | 公式中的 $r>>f$ | 应为 $r\gg f$（源码用两个 > 代替 \gg；PDF 中可见为 >>） |
| §4.4 | PDF 96 | 式 (4.10) 中 $w=0\oplus(-\eta-i(\mathrm{Im}\,\tau)\gamma^*)$ 的 $\eta$ 符号 | 与同页启发式推导差一符号；按脚注 25 与“指数=单值性本征值”判断 (4.10) 自洽 |
| §4.5 | PDF 99 | $\Lambda_{\mathrm{char}}/\Lambda_{\mathrm{rt}}=\pi({}^LG)$ | 应为 $\pi_1({}^LG)$（与同句 $\pi_1(G)$ 及式 (4.13) 一致） |
| §4.6 | PDF 107 | $M_{H}({}^L\alpha,{}^L\beta,\gamma;p)$ | 第三个参数缺左标，应为 ${}^L\gamma$ |
| §5.3 | PDF 125 | 投影算子 $p_1,p_2$ 与 $\pi_1,\pi_2$ | 原文刚定义 $\pi_1,\pi_2$，随后写 $p_2$、$p_1^*$，应为 $\pi$ |
| §6.2 | PDF 133 | $\mathbb{H}^2/\!\!/\!\!/U(1))$ | 多排一个右括号（源码如此） |
| 文献 [70] | PDF 156 | “A Proof of Jantzen Conjectures,” | 原文用直引号而非 ``…''，排版细节 |

> 其中 **§2.5 PDF 17 的 “eqn. (4.1)” 应为 (2.52)** 与 **§2.5 PDF 16 的 $\mathrm{Im}\,{}^L\tau$ 公式**
> 是唯一两处会影响读者推导的原文笔误（前者译文按作者原意排为 (2.52) 并在注中说明原书印作 (4.1)；
> 后者照原文保留、在注中给出正确形式）。其余为拼写、编号引用或语法层面的笔误，不影响物理内容。

## 6. 转换过程中对原文源码缺陷的处理

1. 原文是 1990 年代 harvmac（plain TeX）手写源码。其中 `\CA`、`\CO`、`\CF` 三处宏**只有使用、没有定义**
   （应属作者本地宏），arXiv 源码无法直接编译；译本按上下文补为 $\mathcal{A}$、$\mathcal{O}$、$\mathcal{F}$。
2. 原文源码中若干引用宏名被**重复定义**（如 `\olpo` 先后指 (2.52) 与 (4.1)，另有 `\ijon`、`\nobo` 等），
   harvmac 预载引用定义会使前向引用取到较晚的值——§2.5 PDF 17 的错号即由此而来。
   译本改用 LaTeX 的 `\label`/`\eqref`，按“最近的前一处定义”解析，并逐一核对了全部此类前向引用。
3. 原文用 `\matrix` + `\noalign{\hrule}` 排的谱序列表格（式 (3.40)）、主丛交换图（式 (3.43)）
   以及 `\cases` 中夹 `$...$` 的写法（式 (A.17)–(A.18)）无法机械转换，已按原图手写为 `array`/`cases`。
4. 原文用两套字体（Euler Roman / Euler Script）区分符号（如 $\mathfrak{N}$ 瞬子数与 $\mathcal{N}$ 幂幺根），
   译本以 `\mathfrak` / `\mathcal` 对应，附录 B 中有译注说明。
5. 个别纯排版性内容（如公式列表的竖排间距、`\bigskip`）未逐字复刻，不影响数学内容。

## 7. 使用建议

- **只需讲课用的干净正文**：把 `main.tex` 的 `\showyizhutrue` 改为 `\showyizhufalse`
  （译注方框与编号全部消失），再删除各 `keytakeaways` 环境即可；无需改动任何一节正文。
- **只删个别译注**：定位 `\begin{yizhu} ... \end{yizhu}`（`REVIEW-NOTES.md` 给出每个编号的 `文件:行号`），
  整段删除即可，其余编号会自动重排。
- **对照原文核对某式**：按 `\setcounter` 上的注释 `% 式 (X.Y)` 直接翻原文，或用小节前的页锚点定位页码范围。
- **把某个分片单独发给学生**：整段复制即可，它只依赖 `main.tex` 导言区、`macros.tex` 与 `figures/` 目录。

## 8. 版权与分享（全文见 PDF 第 1 页底部）

- **原著版权**：原文 © 2006 Sergei Gukov and Edward Witten，经 arXiv 以「永久、非独占分发许可」
  （arXiv.org perpetual, non-exclusive license）发布。该许可**只授权 arXiv 分发原文**，
  不授予第三方翻译、改编或再发布的权利；因此原文著作权仍完全归作者。
- **本译本**：属于原文的演绎作品。翻译、图表重制、译注与排版由 DeepSeek Harness 智能体集群完成，
  译注与「本节重点」系译者独立添加的评论，不代表原作者观点；译文讹误由译者负责。
- **可以做什么**：学术研究与教学使用；**原样**转发本 PDF 全文（不得改动正文、不得删除版权声明）。
- **不可以做什么**：任何商业使用；未经许可的改编、摘编、再发布（尤其投稿、出版、收录进教材）。
  这类使用须先取得**原作者**（著作权人）与本译者的书面许可。译注部分可单独按 CC BY-NC-SA 4.0 使用，
  但整份文档的许可上限由原文决定。
- **引用**：请同时标注原文与本译本，例如：S. Gukov and E. Witten, *Gauge Theory, Ramification,
  And The Geometric Langlands Program*, arXiv:hep-th/0612073；中译本（含译注），第 1.0 版，2026。
- 本译本非 arXiv 或原作者发布的官方版本；如原作者或 arXiv 提出异议，将立即停止分发。
