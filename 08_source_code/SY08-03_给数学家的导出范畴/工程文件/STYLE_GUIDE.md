# 文风与排版规范（STYLE_GUIDE）

本文件记录 SY08-03 的既定选择，后续补译、校订一律照此执行；与《数学文献翻译纪律》
v2.0 冲突时以纪律为准，本文件只补充本书特有的约定。

## 一、语言

- 一句不超过 60–70 汉字；长句拆短，拆不动就换主语。
- 禁用：「被……所……」「进行……的讨论」「对于……而言」「起到了……的作用」。
- 少用「以及」；并列三项以上尽量用顿号，或用「与/和」分层次。
- 全角标点；英文术语、数字、公式两侧留半角空格（如「导出范畴 $D^b(\A)$ 的」）。
- 人名：Kontsevich 孔采维奇、Verdier 韦迪耶、Grothendieck 格罗滕迪克、
  Dold–Puppe 多尔德–普佩、Whitehead 怀特海、Hurewicz 胡尔维茨、Leray 勒雷、
  Serre 塞尔、Hartshorne 哈茨霍恩、MacLane 麦克莱恩、Gelfand–Manin 盖尔范德–马宁、
  Kashiwara–Schapira 柏原–夏皮拉、Weibel 韦贝尔、Koszul 科斯居尔、Hodge 霍奇、
  Dolbeault 多博、Kähler 凯勒。外文人名首次出现给中文，其后可仍用原文缩写。
- 书名：正文用《》；参考文献条目照录原文，不译。

## 二、术语

- 以附录 A（73 条）与 `work/glossary.tsv` 为唯一标准；同一英文词只有一个译法。
- 关键术语首次出现用 `\term{中文}{English}`，形如「导出范畴（derived category）」。
- 本书特有选择：
  - distinguished triangle → 特异三角（不用「好三角」「 distinguished 三角」）；
  - roof → 屋顶；calculus of fractions → 分数演算；
  - adapted → 适应（适应类、适应消解）；
  - acyclic → 无环（无环复形）；acyclic resolution → 无环消解；
  - quasi-isomorphism → 拟同构；localisation → 局部化；
  - bounded below/above → 有界下方/上方；
  - injective/projective/flat → 内射/投射/平坦；
  - fine sheaf → 细层；soft sheaf → 软层；flabby → 松弛；
  - hypercohomology → 超上同调；spectral sequence → 谱序列；
  - shift → 平移（$\Sigma$ 亦称悬挂，仅在拓扑语境用「悬挂」）；
  - cylinder → 柱；cone → 锥；suspension → 悬挂；
  - perfect complex → 完美复形；dualising → 对偶化。

## 三、数学排版

- 态射用 `\colon`（如 `f\colon X\to Y`），不用 `:`。
- 范畴名正体加粗：`\A \B \C`；层用 `\F`；结构层 `\OO`；实数域 `\R`。
- 导出函子 `\R F`、`\L F` 用正体 R/L；`\R\mathcal Hom` 的 `\mathcal Hom` 不倾斜。
- 公式编号：只给被正文引用的公式编号（全书 6 个：2.1–2.3、3.1、5.1–5.2），
  其余用 `$$...$$` 不编号。
- 交换图用 `array`/`matrix` 手排，箭头一律 `\to`、`\xrightarrow{f}`；虚线用
  `\dashrightarrow`。
- 定理类环境共享计数器、按节编号，中文名「定理/引理/命题/推论/定义/例/注」；
  引用写作「定义 4.2」「例 6.6」。

## 四、译注、概念卡片、校勘、本节重点

- **译注**（橙框，自动编号）：补原文没有的信息——为什么、依据、量级、反例、指代落点；
  末句必须 `[来源：…]`（A/B/I，含定位与访问日期）或 `[译者按（无外部依据）…]`。
  只复述原文的，删。
- **概念卡片**（紫框）：给核心概念一个可查证的标准表述，标题后缀「（译者所加）」；
  末尾同样交代依据（`[来源：…]`）。
- **校勘**（红框，自动编号）：先判定（误/疑），再给原文、依据、建议；不改正文数学。
  与附录 B 的编号对应关系写在框内（「详见附录 B 校勘 n」）。
- **本节重点**（蓝框）：每节末尾 3–5 条，回答「这节到底做了什么、下一步用什么」。

## 五、编译

- 引擎：XeLaTeX（ctex + fandol 字体），两遍。
- 页面：A4，11pt，geometry 2.5cm/2.6cm，页眉左书名右节名。
- 图：TikZ 重绘，灰色 `gray!55` 实心块表示空间，锥线用直线收到顶点，与原文 EPS 拓扑一致。
- 开关：`\showyizhufalse` 等四个开关可隐藏译注/概念卡片/本节重点/校勘后重排。
