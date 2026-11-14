# 术语一致性与体例审校

## 一、总原则

1. **术语**：以中文学界通行译法为准，首次出现处写成"中文（English）"，后文只用中文；
   专有名词（BRST、BV、Fedosov、Moyal、Wick、Noether、Chevalley–Eilenberg 等）保留英文原拼写。
2. **风格**：学术中文、长句拆分、逻辑连接词显化；不增删原意，不添加原文没有的物理断言。
3. **公式内不夹中文**（`\text{}` 内除外）；中文与行内公式由 ctex 自动处理间距。
4. **章节标题中英并出**：`\section{上同调与积分（Cohomology and Integration）}`，便于对照原文。

## 二、核心术语对照（全书统一，摘录）

| English | 中译 | English | 中译 |
|---|---|---|---|
| action / action principle | 作用量 / 作用量原理 | gauge theory | 规范场论 |
| field space / space of fields | 场空间 | gauge symmetry / gauge fixing | 规范对称性 / 规范固定 |
| observable / observable algebra | 可观测量 / 可观测量代数 | ghost field / ghost number | 鬼场 / 鬼数 |
| equation of motion | 运动方程 | anti-field / anti-ghost | 反场 / 反鬼场 |
| Noether current / charge | Noether 流 / Noether 荷 | anomaly / gauge anomaly | 反常 / 规范反常 |
| de Rham cohomology | de Rham 上同调 | BRST operator | BRST 算子 |
| cochain/chain complex | 上链复形 / 链复形 | master equation (CME/QME) | 主方程（经典/量子） |
| differential form | 微分形式 | polyvector field | 多向量场 |
| exterior derivative | 外微分 | Schouten–Nijenhuis bracket | Schouten–Nijenhuis 括号 |
| compact support | 紧支集 | shifted symplectic structure | 平移辛结构 |
| Poincaré lemma | Poincaré 引理 | quantization | 量子化 |
| Stokes' theorem | Stokes 定理 | deformation quantization | 形变量子化 |
| Cartan formula | Cartan 公式 | star product / Moyal product | 星积 / Moyal 积 |
| Lie derivative / contraction | Lie 导数 / 缩并 | Fedosov quantization | Fedosov 量子化 |
| vector field / principal bundle | 向量场 / 主丛 | index theorem / algebraic index | 指标定理 / 代数指标 |
| connection / curvature | 联络 / 曲率 | heat kernel | 热核 |
| Chern–Simons / Yang–Mills | Chern–Simons / Yang–Mills | propagator | 传播子 |
| $\sigma$-model | $\sigma$ 模型 | correlation function | 关联函数 |
| path integral / Wiener measure | 路径积分 / Wiener 测度 | Green's function | Green 函数 |
| asymptotic / perturbative expansion | 渐近展开 / 微扰展开 | Feynman graph | Feynman 图 |
| renormalization | 重整化 | loop / tadpole | 圈 / 蝌蚪图 |
| counter-term / regularization | 抵消项 / 正则化 | Wick's theorem | Wick 定理 |
| cut-off | 截断 | Gaussian integral | 高斯积分 |
| effective field theory | 有效场论 | homotopy RG flow | 同伦重整化群流 |
| factorization algebra | 因子化代数 | prefactorization algebra | 预因子化代数 |
| cosheaf / sheaf | 余层 / 层 | operator product expansion (OPE) | 算子乘积展开（OPE） |
| vertex algebra / vertex operator algebra | 顶点代数 / 顶点算子代数 | chiral | 手征 |
| holomorphic | 全纯 | descent | 下降 |
| DGLA | 微分分次 Lie 代数 | $L_\infty$-algebra | $L_\infty$ 代数 |
| homotopy / chain homotopy | 同伦 / 链同伦 | obstruction | 障碍 |
| elliptic complex | 椭圆复形 | Kuraníshi | Kuranishi |
| Weyl bundle / Weyl algebra | Weyl 丛 / Weyl 代数 | holonomy | 和乐（群） |
| instanton | 瞬子 | spontaneous symmetry breaking | 自发对称性破缺 |
| holomorphic anomaly | 全纯反常 | quasi-modular | 准模 |
| regularized integral | 正则化积分 | almost-elliptic | 几乎椭圆 |

> 完整术语表（约 150 条）见 `PROTOCOL.md` §8。

## 三、记号约定（全书统一）

| 对象 | 记法 | 说明 |
|---|---|---|
| 场空间 / 向量丛 | $\mathcal{E}$ / $E$ | 原文正文用花体 $\mathcal{E}$、丛用 $E$；截面空间 $\mathcal{E}=\Gamma(X,E)$，三者严格区分 |
| 微分、虚数、指数 | $\dd$、$\ii$、$\ee$ | 原文排印为直立体；变量 $d,i,e$ 照常 |
| 微分算子 | $d$（de Rham）、$d_{\mathrm{CE}}$（Chevalley–Eilenberg）、$\Delta$（BV/散度）、$\delta$（形变微分） | 与原文一致 |
| 分次 | $\vert a\vert$、$W[n]$、$\mathfrak{g}[1]$ | 与原文一致；Koszul 符号 $(-1)^{\vert a\vert\vert b\vert}$ |
| 椭圆/热核 | $P_\varepsilon^L$、$P^{r'}_r$、$K_r$ | 上下标方向与原文逐一核对 |
| 积分 | $\int$；正则化积分 $\fint$（原文"积分号加横杠"） | `\fint` 定义见 preamble |
| 带圈编号 | ①②③ | 原文用于列举，已交由中文字体排版 |

## 四、体例决定

1. **定理类环境**：原文编号是"节号.序号"（如 Definition 2.1、Example 5.4、Theorem 10.12），
   且并非 LaTeX 自动编号。译本用 `\begin{wdefn}{2.1}` 等带参数环境**手动保留编号**，
   避免重排后与原文对不上。
2. **公式**：原文展示公式**不编号**（已逐页核对，全篇仅例 5.x 的 $(*)$ 一处标记），
   故译本一律用 `\[ … \]`；个别多行公式用 `aligned`/`cases`，$(*)$ 用 `\tag*{$*$}`。
3. **图**：原文只有两张编号图（Figure 1、Figure 2），其余为正文内嵌示意图。
   译本的图题统一为"中文图题（原文 PDF p.NNN 示意图，原文无编号）"；
   两张编号图写作"（原文 Figure k，原文 p.N ／ PDF p.N+1）"。
4. **表**：5 处表格用 `booktabs` 重排（不截图），表头译中文。
5. **Key Takeaways**：每个 `\section` 开头 3–5 条（核心物理图像 / 数学工具 / 主要结论 / 译者评注）。
6. **Tutor Note**：统一格式 `% [Tutor Note: …]`，为 LaTeX 注释、不进入排版正文，四类内容
   （易错预警 / 含糊点拨 / 原文疑误 / 术语依据）见 README 第四节。
7. **参考文献**：条目照录英文原文，仅统一标点为 LaTeX 形式（`--` 连接号、`\&` 等），不翻译。

## 五、抽查到的术语不统一及处理

| 位置 | 原文/初稿 | 统一处理 |
|---|---|---|
| 第 4 章 | "Chevally-Eilenberg" | 正文统一 Chevalley–Eilenberg |
| 第 8 章 | "Costello-Gwillian" | 统一 Costello–Gwilliam |
| 第 9 章 | "Moayl product" | 统一 Moyal |
| 第 1、10 章 | twist / descent 等 | 按术语表：扭曲 / 下降 |
| 全书 | instanton 的"瞬子" | 统一瞬子（不写"伪粒子"） |
| 第 5 章 | propagator | 统一传播子（原文亦称 Green's function，按原文区分） |
| 第 6 章 | ghost / anti-field | 鬼场 / 反场（"反鬼场"仅用于 anti-ghost） |
