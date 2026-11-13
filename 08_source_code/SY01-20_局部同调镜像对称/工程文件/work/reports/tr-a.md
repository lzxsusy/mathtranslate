# tr-a 报告（ch01、ch02）

## 1. 交付物

| 文件 | 内容 | 规模 | 编译页数 |
| --- | --- | --- | --- |
| `src/chunks/ch01.tex` | §1b 多重单值性、§1c Hirzebruch 面、§1d 全文结构、致谢、AI 使用声明（原文 p.6–p.9，含推论 1.6–1.10、问题 1.11） | 243 行 / 13.1k 字符 | 5 页 |
| `src/chunks/ch02.tex` | §2 定理的证明：预备与蓝图、扇形下降与真下降、环面丛、Hirzebruch 面（原文 p.9 尾–p.14） | 232 行 / 16.2k 字符 | 6 页 |
| `work/check/ch01_test.tex` | 自检壳 | — | — |
| `work/check/ch02_test.tex` | 自检壳 | — | — |
| `work/reports/tr-a-terms.tsv` | 18 条新增术语 | — | — |

## 2. 边界说明

- 只写了上述两个 chunk、两个自检壳、本报告与术语补表；**未改** `src/preamble.tex`、`src/main.tex`、他人 chunk；未做任何 git 操作。
- ch01 不写 `\section`（§1 的标题在 ch00 内），只用 `\subsection`/`\subsection*`；ch02 以 `\section{定理的证明\label{sec:proof-of-theorems}}` 开头，与 main.tex 的输入顺序一致。
- 公式、`tikz`/`tikzcd` 图、环境名、`\label`、`\cite`、`\ref` 全部按原文；不手写编号、不用 `\tag`。
- 原文笔误一律**照原样排印**，另用 `yizhu` 指出（见 §5）；拼写错误的英文单词按正确词义翻译，不复制错拼。

## 3. 编译自检

`cd work\check` 下各跑两遍 `xelatex -interaction=nonstopmode`：

| 文件 | 页数 | `!` 错误 | Overfull | Underfull | Missing character |
| --- | --- | --- | --- | --- | --- |
| `ch01_test` | 5 | 0 | 0 | 0 | 0 |
| `ch02_test` | 6 | 0 | 0 | 0 | 0 |

- 剩余 warning 全部是**跨 chunk** 的 undefined citation/reference（正文显示 `[?]`），合成全书后消失：ch01 的 `thm:HMS-projective-bundle`、`defn:*` 等来自 ch02/后续章；ch02 的 `defn:Liouville-sector-inf`、`prp:Kartal-modification-Weinstein` 等来自 ch00/§3。
- `latex_look(audit:true)` 结果：两份都只有「章/节末页」一个短页（ch02 第 6 页只剩本节重点框，属正常分页），无其他版面塌陷。
- 目检覆盖：ch01 p.1–p.5、ch02 p.1–p.6 全部渲染后逐页看过（图、方框、方图、长公式均无溢出）。

## 4. 批注清单

### ch01（5 条译注 + 2 个概念框 + 1 个本节重点）

| 行号 | 类型 | 标题 / 要点 |
| --- | --- | --- |
| `:20` | yizhu | 下标 `∞` 与真下降的意思：`\Coh(\cdot)_{\infty}` 指 ∞-范畴版本，与 `dg` 下标切换；方框图的四个顶点是四个范畴，「真下降」= 把两个分支的凝聚复形沿公共截面拼起来 |
| `:33` | yizhu | `0` 与 `∞` 的记号错位：`P(Y,ξ₁)` 贡献无穷远截面、`P(Y,ξ₂)` 贡献零截面，故 `Coh(Y)→Coh(P(Y,ξ₁))` 应是 `i_∞`、`Coh(Y)→Coh(P(Y,ξ₂))` 应是 `i_₀`；原文第一张方图两个下标写反（与 §2b 图相反），照排并给出读者应以哪条约定为准 |
| `:95` | yizhu | 图中的虚线只是「链还没画完」：虚线边不是特殊粘合方式，只是链继续向左右延伸，`k` 可任意；推论的环形情形要把首尾接上 |
| `:149` | yizhu | 原文笔误：`π₁(𝕋ⁿ)` 应为 `π₁(𝕋ᵏ)`——同段前文取 `Σ⊂ℝᵏ`、`φ₁,…,φ_k`，`n` 是环面丛的维数参数，读到下标 `n` 请自行换成 `k` |
| `:186` | yizhu | `\rF_n` 的记号与「微分同胚不算辛同构」：花体 `\rF` 是翻转的 `F`，表示 `𝔽_n` 的镜像而非新曲面；推论给两个层次（带边流形微分同胚 / 带超势全纯流形同构），都弱于精确辛同胚 |
| `:167` | conceptbox | Hirzebruch 面（Hartshorne V.2；同构只依赖 `|n|`、`𝔽₀=ℙ¹×ℙ¹`、`𝔽₁=Bl_pt ℙ²`、不同 `n` 复结构不同但辛流形互变形） |
| `:198` | conceptbox | 异域 Weinstein 结构（Kartal arXiv:2204.04928；本文 §1c 推论 1.10） |
| `:209` | keytakeaways | 3 条：多重单值性的机制、链式粘合的 `0/∞` 账本、Hirzebruch 面的显式例子 |
| `:10/:106/:146/:219` | `% [原文 p.N]` | p.6 / p.7 / p.8 / p.9 |

### ch02（5 条译注 + 2 个概念框 + 1 个本节重点）

| 行号 | 类型 | 标题 / 要点 |
| --- | --- | --- |
| `:17` | yizhu | Kartal 的修改在改什么：公式写 `T*ℝ×X`、正文写 `X×ℂ`，二者同一空间（`T*ℝ≅ℝ²≅ℂ`，`z` 是复坐标）；乘积 Weinstein 结构一般不是 `ℤ`-不变，直接取商会丢掉 Liouville 形式、破坏凸性；Kartal 的修改把辛结构调成 `ℤ`-不变 |
| `:52` | yizhu | 脚注里的 `\Perf` 不是平常的 `\Perf`：`\Perf_{𝔾_m}(ℙ¹)_{dg}` 取 `𝔾_m`-等变完美模，只有等变版本才与 `𝒲(T*ℝ,e^z+e^{-z})` 拟等价 |
| `:88` | yizhu | 链接圆盘 `D[0]` 与 `0/∞` 的不对称：`D[0]` 是以标号 0 的停止位为边界的链接圆盘，在 `\Perf 𝒲` 中对应零截面的结构层 `𝒪₀`（差一个平移）；`op` 不是装饰；主丛情形把 0 换成 ∞、`𝒪₀` 换成 `𝒪_∞`，两条推论不能混用 |
| `:129` | yizhu | 两个 `𝔾_m` 各管一个方向：一个作用在 ℙ¹ 纤维方向（射影丛的等变结构），一个沿 `L(Y,ξ)^×→Y` 的主丛方向；两者交换，故有分解 `[P(Y,ξ)/𝔾_m²]=[ℙ¹/𝔾_m]×Y×[pt/𝔾_m]` |
| `:219` | yizhu | 原文的 `𝒳` 应为 `\rF_n`：证明末出现 `𝒳≅_alg ℂ*×ℂ*`，但正文此前未引入 `𝒳`；按上下文（投影 `\rF_n→ℂ*×ℂ*`、每根纤维单点）此处应为 `\rF_n`。照原样排印 |
| `:47` | conceptbox | 扭 Künneth 公式（nLab: Künneth theorem；本文 §2a、§6c） |
| `:75` | conceptbox | 映射柱与停止位（Kartal arXiv:2204.04928；Sylvan arXiv:1601.05080；本文 §2a、§2d） |
| `:223` | keytakeaways | 3 条：A 侧的映射柱与 Kartal 修改、B 侧的扭张量积与半正交分解、两条下降归约到 ℙ¹∪ℙ¹ 的万有情形。**brief 只要求 ch01 有本节重点，这条属加写，若与下一章重复可由 lead 删除** |
| `:14/:63/:113/:146/:203` | `% [原文 p.N]` | p.10 / p.11 / p.12 / p.13 / p.14 |

## 5. 存疑清单

1. **ch01 第一张真下降方图（`:33`）**：`i_0`/`i_∞` 与 `{z_1=∞}≅{z_2=0}` 的约定以及 §2b 的真前推方图相反，判为原文笔误，照排并加译注；是否统一改正请示 lead。
2. **ch01 `:147`**：`π₁(𝕋ⁿ)` 应为 `π₁(𝕋ᵏ)`（同段前文均为 `k`），已加译注 4，未改正文。
3. **ch02 `:216`**：证明末 `𝒳≅_alg ℂ*×ℂ*` 应为 `\rF_n≅_alg ℂ*×ℂ*`（`𝒳` 未定义），已加译注 5，未改正文。
4. **ch02 `:201`（§2c 推论 1.9 证明末）**：`\Coh\left[\mathcal{Y}(Y;\xi_1,\cdots,\xi_k)\right]` 漏下标 `Σ`（前一句是 `\mathcal{Y}_\Sigma`），照原文，未加注——若统一加注请 lead 定。
5. **原文拼写错误**：ch01 §1c 的 `projectization`、致谢的 `wth`、`Insititut`、AI 声明的 `refernces`；译文按正确词义处理，不保留错拼。另 ch02 定理 1.2 中作用记号 `((1), L(\xi)\otimes-)` 括号不成对（原文如此），照排。
6. **`\mathcal{Y}(Y;\xi_1,\dots)` 与 `\mathcal{Y}_\Sigma(Y;\xi_1,\dots)` 的前后不一致**：首现带 `Σ`，其后有时省略，已照原文保留。

## 6. 术语

新增 18 条写入 `work/reports/tr-a-terms.tsv`（toric bundle 环面丛、nodal curve 节点曲线、integral convex polytope 整凸多面体、exact symplectomorphism 精确辛同胚、linking disk 链接圆盘、semi-orthogonal decomposition 半正交分解、invertible sheaf 可逆层、coherent-constructible correspondence 凝聚—可构造对应、sheaf–Floer correspondence 层—Floer 对应、valuative criterion 赋值判据、closed immersion 闭浸入、homotopy pushforward 同伦前推、exotic Weinstein structure 异域 Weinstein 结构、essential surjectivity 本质满射、twisted Künneth formula 扭 Künneth 公式、projective toric surface 射影环簇曲面、quasi-projective 拟射影、mapping torus 映射环面）。其余一律沿用已冻结的 `work/terms_zh.tsv`（含 停止位（stop）、映射柱、射影丛、零截面、无穷远截面、异域 Weinstein 扇形 等）。

## 7. 概念库勘误

- **「轨道范畴」条**：与 tr-b 报告的判断一致——该条把 orbit category 与 Keller 的三角/导出轨道范畴混在一起叙述。我原先在 ch02 §2a 写过这个框，发现与 tr-b 已写在 ch04 §3c 的框重复（且 §3c 才是定义所在），已整块换成「映射柱与停止位」；建议全书只在 §3c 保留一处。
- **「Hirzebruch 面」条**：`n↔−n` 同构、`𝔽₀`/`𝔽₁` 的识别、不同 `|n|` 复结构不同而辛流形可互变形，均与原文推论 1.10 及 Hori–Vafa 段落相容；框内已注明同构类型只依赖 `|n|`。

## 8. 格式自检

- 标点：全角标点、引号用「」；中文与数学/英文之间保留半角空格。
- 禁用句式扫描（python 统计）：`进行` 0、`对于` 0、`而言` 0、`被…所` 0、`\tag` 0。
- `tikzcd` 箭头标签内的引号一律 ASCII `"`（曾误用全角「」，xelatex 报 `Package xcolor Error: Undefined color`、`Missing \endcsname inserted`，报错行还落在 `\end{tikzcd}` 上，已全部改回；ch01 4 处、ch02 6 处）。
- `yizhu` 可选短标题里若含 `]`，必须写成 `${[0]}$` 之类保护（ch02 `:88` 的 `D[0]` 曾因此报 `! Extra }, or forgotten $.`）。
- 文件为 UTF-8、行尾 LF；每条 `% [原文 p.N]` 都落在对应页起始的源码位置（显示公式之后或段首），不引入额外分页。
