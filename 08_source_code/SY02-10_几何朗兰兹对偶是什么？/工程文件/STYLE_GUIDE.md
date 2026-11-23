# STYLE GUIDE — 中译注本排版与术语规范

## 一、排版体例

| 项 | 规定 |
|---|---|
| 文档类 | `ctexart`，11pt，A4，`fontset=windows`（宋体正文 / 黑体标题），UTF-8 |
| 西文与数学 | Latin Modern（`lmodern` + `unicode-math` 关闭，沿用 ctex 默认数学字体） |
| 页眉 | 左「几何朗兰兹对偶是什么？」，右「David Ben-Zvi」，fancyhdr 单线 |
| 页码 | 页脚居中 |
| 节号 | 起于正文，编号 1–6，与原文章节号严格对应；`\S2.2.3` 这类交叉引用直接写节号 |
| 定理环境 | `theorem*`（无编号），定理的石名与文献放在可选参数里：`\begin{theorem*}[GLC，[GR24a, …]]` |
| 公式 | 只用 `equation` / `align`；原编号 (1)–(6) 用 `\tag` 保留；禁用 `eqnarray` |
| 图 | `\includegraphics` 独立文件（`源码/figures/fig1–3.jpg`），`[tbp]` 浮动，图注末尾标「（插图：Elliot Kienzle）」 |
| 表格 | 三线表（booktabs），长表用 `p{}` 列 + `\raggedright`；术语表外层 `{\small}` |
| 标点 | 中文标点（，。；：？！「」——……），西文括号保留为 `()`；数字区间用 en dash |
| 强调 | 原文斜体 → `\emph{}`；句内被强调的 slogan 单独成段，不缩进 |

## 二、译名规范（首批冻结，全文一致）

### 2.1 核心对象

| 原文 | 译名 | 备注 |
|---|---|---|
| geometric Langlands correspondence (GLC) | 几何朗兰兹对偶（GLC） | correspondence 译「对偶」，不译「对应」，与原文"duality"口气一致 |
| automorphic sheaf | 自守层 | |
| Hecke eigensheaf | Hecke 本征层 | eigen- 一律译「本征」 |
| eigenvalue / eigenspace | 本征值 / 本征空间 | |
| spectral side | 谱侧 | |
| Langlands dual group | 朗兰兹对偶群 | |
| moduli stack | 模栈 | |
| character variety | 特征簇 | 整体版称「$\check G$-局部系统的模栈」 |
| local system | 局部系统 | |
| perverse sheaf | 反常层（perverse sheaf） | 首次出现保留原文 |
| skyscraper sheaf | 摩天楼（层） | |
| factorization algebra / homology | 因子化代数 / 因子化同调 | fusion 译「融合」 |
| affine Grassmannian | 仿射 Grassmannian | 不音译 |
| oper | oper | 不译，首现加说明「由『有理标准形』刻画」 |
| Whittaker function / period | Whittaker 函数 / Whittaker 周期 | |
| Eisenstein series | Eisenstein 级数 | |
| singular support | 奇异支撑 | |
| nilpotent singular support | 幂零奇异支撑 | |
| unramified | 非分歧 | tame ramification 译「温和分歧」 |
| ramified | 分歧 | |

### 2.2 分析/代数词条

| 原文 | 译名 |
|---|---|
| functional calculus | 泛函演算 |
| projection-valued measure | 投影值测度 |
| direct integral | 直积分 |
| monodromy | 单值性 |
| six-functor formalism | 六函子形式 |
| ind-coherent sheaves | 归纳凝聚层 |
| quasi-coherent | 拟凝聚 |
| Tannaka duality | Tannaka 对偶 |
| derived category | 导出范畴 |
| Fourier–Mukai / Mukai transform | 傅里叶–Mukai / Mukai 变换 |
| Higgs bundle, Hitchin fibration | 希格斯丛、Hitchin 纤维化 |
| spectral curve | 谱曲线 |
| abelianization | 阿贝尔化 |
| geometric Satake equivalence | 几何 Satake 等价 |
| spectral action | 谱作用 |

### 2.3 保留原文不译

人名、群名、定理名（Hecke、Hitchin、Langlands、Satake、Whittaker、Kac–Moody、Kazhdan–Lusztig、
Beilinson–Drinfeld、Fargues–Fontaine、Kapustin–Witten、Montonen–Olive、Weil、Gaudin、Calogero–Moser、
Kloosterman、Bessel、Ramanujan、Arthur、Ngô、Lafforgue、Yun、Gaitsgory、Arinkin……）；
刊名、丛书名、拉丁语（de Rham、étale、motivic、Hodge、twistor）；「白光」（White Field）为原文修辞，
译文保留引号并加译注；「跳动的心脏」「赫拉克勒斯」「棱镜」「罗塞塔石碑」同理保留原比喻。

## 三、译注格式

- 正文脚注：`\zhnote{…}` → 渲染为「译注｜……」，与 `\anote{}` 渲染的「原注｜……」并列。
- 每条以「（B 级）」或「（A/I 级）」收尾；I 级另写「译者按（无外部依据）」。
- 结构：**先给技术定义 → 再给与本文语境的接点 → 最后给可查链接**。
- 附录「译注汇总」把 14 条按节重列（不加链接堆砌，保留完整句），末尾附 nLab 对照表。

## 四、引用格式

- 正文引用一律写 `[KEY]`（如 `[GR24a]`、`[ABC+24b]`），不使用 `\cite`，以保证与原文行文一致。
- 参考文献表用 `thebibliography` 风格的 `\item[{KEY}]`，122 条按原文顺序照排，**不译、不改写**；
  只做三件事：修复 PDF 抽取造成的连字断行、去掉 `.ezproxy` 代理前缀、还原变音符。
