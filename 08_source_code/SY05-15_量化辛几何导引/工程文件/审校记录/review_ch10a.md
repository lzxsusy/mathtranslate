# 第 10 章前半「生成函数与层速成」疑误记录（review_ch10a.md）

记录范围：PDF p.290–p.306（印刷页 282–298，即 10.1、10.2 两节）。每条给出原文、
所在页（印刷页 / PDF 页）、疑点与建议改法。均已在正文对应位置以
`% [Tutor Note: 原文疑误 ...]` 标注，译文保留原文写法，未擅自改动。

| # | 印刷页 / PDF 页 | 原文（摘录） | 疑点 | 建议 |
|---|---|---|---|---|
| 1 | p.286 / PDF p.294 | 式 (10.5)：$\psi_t^{(i)}=\varphi_{\frac{(i-1)t}{N}}\circ\varphi_{\frac{it}{N}}^{-1}$ | 按通常的复合次序取乘积 $\psi^{(1)}\circ\cdots\circ\psi^{(N)}$，对 $N=2$ 得 $\psi^{(1)}\circ\psi^{(2)}=\varphi_t^{-1}$，一般地也得到 $\varphi_t^{-1}$ 而非 $\varphi_t$。要使乘积伸缩相消为 $\varphi_t$，应取 $\psi_t^{(i)}=\varphi_{\frac{it}{N}}\circ\varphi_{\frac{(i-1)t}{N}}^{-1}$（或等价地把乘积的复合次序反过来）。 | 核对原书；若原书如此，建议改正为 $\varphi_{it/N}\circ\varphi_{(i-1)t/N}^{-1}$。 |
| 2 | p.287 / PDF p.295 | 命题 10.1.1："$F_2\colon\R^{2n}\times\R^{N_1}\to\R$ is the generating function of $\varphi_2$" | 同一命题中 $F_1\#F_2$ 的变量 $e_2\in\R^{N_2}$，故 $F_2$ 的定义域第二因子应为 $\R^{N_2}$。 | 改为 $F_2\colon\R^{2n}\times\R^{N_2}\to\R$。 |
| 3 | 3a. 296 / PDF p.304 | 核层茎的计算："$\ker(\mathbf{k}_X\to i_\ast(i^{-1}\mathbf{k}_X))_0$"，其中框架是 $Z=(0,1)\subset\R=Y$、$i\colon\R\setminus(0,1)\to\R$ | 环境空间是 $Y=\R$，所裁剪的常值层应为 $\mathbf{k}_Y$；此处 $X$ 疑为 $Y$ 之误（本节其余地方均用 $\mathbf{k}_Y$）。 | 改为 $\mathbf{k}_Y$；或统一说明 $X=Y=\R$ 的记号约定。 |
| 4 | p.298 / PDF p.306 | 例 10.2.11 末：$\bigl((\mathbf{k}_\R)_{(0,1]}\bigr)((a,b))=\mathbf{k}$ 若 "$a\in[0,1]$" | 按该段自身的计算，$a=1$ 时 $\bigl((\mathbf{k}_\R)_{(-\infty,1]}\bigr)((a,b))=\mathbf{k}$、$\bigl((\mathbf{k}_\R)_{(-\infty,0]}\bigr)((a,b))=0$，核为 $\mathbf{k}$；但若同时 $b\le 1$，区间 $(1,b)$ 为空，端点约定需与全书的「左开右闭」约定核对。疑应为 $a\in[0,1)$ 或需补充 $b$ 的条件。 | 核对原书端点约定（$(a,b)$ 为通常开区间还是 $(a,b]$）。 |
| 5 | p.287 / PDF p.295 | 定义 10.2.1："for any $U\in\Op(x)$" | 应为 $\Op(X)$（同一句前后均用 $\Op(X)$）。 | 改为 $\Op(X)$。 |

## 已加 Tutor Note 提示、但不算疑误的易错点

- 生成函数中「$\partial_eF=0$ 的临界纤维」与「对 $x$ 求导」的先后（定义 10.1.1）；
- 例 10.1.2 中 $F$ 即作用量泛函，$L=\operatorname{graph}(\dd F)$ 是 Hamilton--Jacobi
  方程的全局解，符号约定 $\lambda_{\mathrm{can}}=\sum p_i\dd q_i$；
- 定理 10.1.1 中「无穷远处为二次型」保证临界集的 properness；
- 例 10.1.3 中 $\tau$ 的辛同胚验证（$-\omega_{\mathrm{std}}\oplus\omega_{\mathrm{std}}$
  的负号位置）；
- 常值层 $=$ 常值预层的层化（$\mathbf{k}_X$ 并非常值预层 $U\mapsto\mathbf{k}^N$）；
- $\R_\gamma$ 上的层 $=$ 持续 $\mathbf{k}$-模（例 10.2.4 (iii)），并与定理 5.2.1 对照；
- 茎（stalk）与纤维（fiber）的区别：$\mathcal{F}_x$ 是邻域基上的正向极限（芽），
  纤维是 $\mathcal{F}_x/\mathfrak{m}_x\mathcal{F}_x$ 或局部自由时的
  $\mathcal{F}_x\otimes_{\mathcal{O}_{X,x}}\mathbf{k}$；
- 定理 10.2.1 中的 $\mathbf{k}_I$（裁剪常值层）与定理 5.2.1 中的 $\mathbf{k}_I$
  （区间型持续模）同名而所指不同。

---

## 10.3–10.4（PDF p.307–p.314；译者 ch05a-floer）

| # | 印刷页 / PDF 页 | 原文（摘录） | 疑点 | 建议 |
|---|---|---|---|---|
| 6 | p.305 / PDF p.313 | 定义 10.4.1 的等价关系：「there exists $F^\bullet\in\mathrm{Ob}(\mathcal A)$ such that the following diagram commutes」 | $F^\bullet$ 是复形（屋顶图中间的对象），应属 $\mathrm{Ob}(C(\mathcal A))$，而非 $\mathrm{Ob}(\mathcal A)$；否则无法定义 $q''$、$f''$ | 改为 $F^\bullet\in\mathrm{Ob}(C(\mathcal A))$（或 $\mathrm{Ob}(D(\mathcal A))$）；译文照原文保留并加 Tutor Note |
| 7 | p.305 / PDF p.313 | 「Definition 10.4.2 (Proposition)」 | 「定义 10.4.2」后括注「（命题）」，标签体例特殊（原书把一条泛性质命题作为定义陈述） | 体例问题，非笔误；译文保留为「定义 10.4.2（命题式定义）」 |
| 8 | p.304 / PDF p.312 | (10.19) 后：「Here, proper means the pre-image of a compact subset of $Y$ is also compact in $X$.」 | 该紧合性针对的是映射 $f:\operatorname{supp}(s)\to U$，故「紧子集」应是 $U$ 的紧子集（而非整个 $Y$ 的） | 建议写成「$U$ 的紧子集」；不影响 (10.19) 的数学内容 |
| 9 | p.299–300 / PDF p.307–308 | (10.15) 左侧记 $\check H^*$、右侧用指标 $n$ | 上下标约定混用（$*$ 与 $n$ 表示同一次数），原书惯用 $*$ 作占位 | 体例问题；译文照原文，注意 (10.15) 的 $n$ 即 $*$ 的取值 |
| 10 | p.299 / PDF p.307 | 注 10.2.5：「for any $s\leqslant t$ ... for any $s\leqslant t$」 | 同一限定语在相邻两句中重复出现 | 原文如此；译文合并重复，未改数学内容 |

**接缝说明（10.2 → 10.3）**：PDF p.307 顶部依次是图 10.3、承接 p.306 末句「It is in fact」的段落（"an interesting question to explore the relation between these two $\mathbf{k}_I$'s"）与**注 10.2.5**，之后才是 10.3 节标题。按分工这些内容由本译者写入 `ch10a-s03.tex` 开头（含 `% >>> p307` 标记）；已核对 `ch10a-s02.tex` 末尾未重复写入（其末行仅留一句接缝注释）。

**体例**：本章 10.3–10.4 的 2 幅插图（图 10.3、图 10.4）均从扫描页 300 dpi 裁剪为 `qsg/figures/fig_p307_1.png`、`fig_p310_1.png` 并经 `read_image` 验证；preamble 无 tikz，故定义 10.4.1 的「屋顶」交换图与定义 10.4.2 的三角形交换图用 `array` + `\swarrow`/`\nearrow`/`\big\uparrow` 手工排版。

**全章渲染提醒（非本章特有）**：preamble 中 `\newcommand{\Op}{\operatorname}`，因此 `\Op{Sh}` 渲染为 Sh、`\Op{supp}` 渲染为 supp；但若写成 `\Op(X)`，`\operatorname` 会把 `(` 当作参数，导致 "Op" 丢失（渲染成 "(X)"）。本译者文件已统一改用 `\operatorname{Op}(X)`；提醒其他章节（如 ch10b）排查同类写法。

## 自检结果（本半 p307–p314）

- `python qsg/tools/check.py ch10a`：本半 **p307–p314 全覆盖、无缺页、无结构错误、无重复 tag、无缺失图片、无禁用命令**；节 2、keytakeaways 2、Tutor Note 本半新增 14 条、图 2、公式编号 8（(10.13)–(10.20)）。
- 试编译（`preamble` + ch10a-s03/s04）通过：8 页，零 Overfull/Underfull、零 undefined；测试文件已删除，未改 preamble/main/00-front 及他人文件。

---

## 补充：PDF p315 上半页（10.4 节收尾）的补译（QA 缺口修复）

**缺口**：10.4 节的末尾——例 10.4.3 的 (ii)（$Rf_!$ 与 $R\Gamma_c$）、(iii)（$R\mathrm{Hom}$）、
$R\mathrm{Hom}$ 双函子、双复形 $C^{p,q}=\mathrm{Hom}_{\operatorname{Sh}(\mathbf{k}_X)}(\mathcal F^p,\mathcal G^q)$、
全复形 (10.21)、有界性说明与导出张量——位于 PDF **p315 上半页**。原先 ch10a 止于 p314、
ch10b 从 p315 的 §10.5 标题起笔，导致 (10.21) 及这半页无人翻译，且 `ch10b-s01.tex:227`
对 (10.21) 的引用悬空。

**修复**：已将 p315 上半页补译到 `qsg/tex/ch10a-s04.tex` **末尾**（不新建文件、不写
`\chapter`），开头加 `% >>> p315`；公式 (10.21) 用 `\begin{equation}\tag{10.21}…`；
例 10.4.3 的 (ii)(iii) 仍在其环境内（
已把原 p314 处的 `\end{wexam}` 移到 p315 半页末尾的 `\hfill$//$` 之后），与 s04 前文
的 $Rf_\ast$、双函子、双复形记号衔接；末尾止于 §10.5 标题之前（未写 `\section`）。

**Tutor Note**：新增 1 条（全复形 (10.21) 的微分构造 $d=d_h+(-1)^p d_v$ 与有界性；
提示原文未写出微分、读者需自行补符号约定）。

**ranges.json**：`ch10a` 的 `pdf` 由 `[290,314]` 扩为 `[290,315]`、`printed` 由
`[282,306]` 改为 `[282,307]`（接缝页 p315 与 ch10b `[315,342]` 重叠，与 ch05a/ch05b
的接缝处理一致）；`ch10b` 未改动。

**自检**：`python qsg/tools/check.py ch10a` → PDF p290–p315 共 **26/26 页全覆盖**、
无缺页、无结构错误、无重复 tag（21 个，(10.1)–(10.21)）、无缺失图片；`check.py ch10b`
仍 28/28 页通过。单章试编译（preamble + ch10a-s03/s04）通过：8 页，零警告。
