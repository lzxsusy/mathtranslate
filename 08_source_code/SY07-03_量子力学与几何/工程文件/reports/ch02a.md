# 块报告：ch02a

## 1. 块名与页段
- 块名：`ch02a`
- 页段：PDF 81–108 = 原书 p.80–107
- 源文件：`work/en/ch02a.txt`（清洗稿 `work/review/ch02a_clean.txt`）
- 说明：本块是**第 2 章章首**，文件以 `\chapter{路径积分形式}` 开头；译到原书 p.107 页末（最后一幅图）为止，p.108（PDF 109）起由 ch02b 接续。

## 2. 节清单（标题按原文，不写编号）
- §2.1 路径积分引论：2.1.1 量子演化与费曼核；2.1.2 位置与动量表示
- §2.2 时间切片下的路径积分：2.2.1 自由粒子；2.2.2 无穷小时间；2.2.3 复合律；2.2.4 路径积分；2.2.5 虚时间
- §2.3 高斯路径积分：2.3.1 高斯积分；2.3.2 zeta 函数正则化
- §2.4 谐振子：2.4.1 积分核；2.4.2 配分函数
- §2.5 渐近方法：2.5.1 拉普拉斯方法；2.5.2 最速下降法；2.5.3 Morse 流；2.5.4 Stokes 现象
  - 另有原文未编号的粗体小标题三处，用 `\subsection*{}` 处理：艾里函数、Stokes 射线、渐近求和
- 每个完整节末均写了 `\takeaway{}`（§2.1–§2.4 共 4 条）。**§2.5 在本块只译到一半**，其 takeaway 留给 ch02b 在节末补写。

## 3. 陈述编号清单（手工照抄原文）
| 环境 | 编号 | 原书页 |
|---|---|---|
| remark | 2.2.1 | p.84 |
| proposition | 2.3.1 | p.89 |
| remark | 2.3.2 | p.89 |
| example | 2.5.1 | p.97 |
| example | 2.5.2 | p.98–99 |
| example | 2.5.3 | p.100 |
| example | 2.5.4 | p.100–102 |

式号：Proposition 2.3.1 中的 $(*)$ 用 `equation*` + `\tag{$*$}` 复现（p.89）；§2.5.1 的极限公式 $(*)$（p.96）同样处理。

## 4. 图清单（共 20 幅：16 幅裁切 + 4 幅 TikZ 重绘）
| 文件 | 来源页 | 处理方式 |
|---|---|---|
| `figures/fig_p82_a.png` | 原书 p.80 | 裁切；`\fignote` 译 classical trajectory → 经典轨迹 |
| `figures/fig_p87_a.png` | 原书 p.86 | 裁切（复合律路径族示意，含 blue/red/green 曲线与 x₁,x₂,v₂,v₁ 标注） |
| `figures/fig_p87_b.png` | 原书 p.86 | 裁切后 `trim_ink.py` 去顶部混入正文 |
| `figures/fig_p88_a.png` | 原书 p.87 | 裁切（时间细分轴 + 路径族） |
| `figures/fig_p89_a.png` | 原书 p.88 | 裁切（x′→x″ 路径 + 蓝色切片线 + 红色 t′,t″） |
| `figures/fig_p91_a.png` | 原书 p.90 | 裁切（经典轨迹 x_cl(t) 与涨落后路径 x(t)） |
| `figures/fig_p98_a.png` | 原书 p.97 | 裁切（f(x) 图像 + δ 带 + a,b,x₀±ε 标注） |
| TikZ | 原书 p.98 | 重绘复围道 C_θ；图内「θ>0 small」改「$\theta>0$ 且很小」 |
| `figures/fig_p101_a.png` | 原书 p.100 | 裁切（45° 最速下降围道 C_{π/4}） |
| `figures/fig_p102_a.png` | 原书 p.101 | 裁切（流方程两支解，角度 π/2−θ/2） |
| `figures/fig_p102_b.png` | 原书 p.101 | 裁切（合并后的曲线 C） |
| `figures/fig_p103_a.png` | 原书 p.102 | 裁切（切线角 π/2−½Arg f″(z₀)，含红色虚线角） |
| `figures/fig_p104_a.png` | 原书 p.103 | 裁切（流场方向 + 虚线双曲线 x²=y²+1） |
| `figures/fig_p105_a.png` | 原书 p.104 | 裁切（C_− 与 C_+ 两条最速下降曲线） |
| `figures/fig_p106_a.png` | 原书 p.105 | 裁切（P_± 曲线经 f 映到平行四边形的边长图） |
| TikZ | 原书 p.106 | 重绘 λ 平面上的 Stokes 射线（双箭头 + λ 平面框） |
| `figures/fig_p107_b.png` | 原书 p.106 | 裁切（z 平面上的 C^λ_±、p_−、p_+）；`\fignote` 译 z-plane |
| `figures/fig_p107_c.png` | 原书 p.106 | 裁切（跨过 Stokes 射线时三幅曲线变化图）；`\fignote` 译 across the Stokes ray |
| TikZ | 原书 p.107 | 重绘 λ 平面 anti-Stokes 射线分区图（∫ 占主导区域） |
| TikZ | 原书 p.107 | 重绘跨过 Stokes 射线 λ∈ℝ_{>0} 的小图 |

- 未采用的 auto 候选：`fig_p107_a.png`、`fig_p107_d.png`、`fig_p108_a.png`、`fig_p108_b.png`、`fig_p80_a/b`、`fig_p99_a.png`（前几张为同一图的碎片或与重绘重复；`fig_p99_a` 的复围道改 TikZ 重绘）。
- 所有裁切图用 300 dpi PNG，宽度 0.34–0.90\textwidth，不加题注。

## 5. 未决术语
见 `work/term_requests_ch02a.md`（24 条）：复合律、费曼核、位置与动量表示、威克转动、欧氏路径积分、费曼–卡茨公式、zeta 函数正则化、椭圆算子、泛函行列式、量子涨落、配分函数、拉普拉斯方法、斯特林公式、Hessian 矩阵、Morse 流、艾里积分、Stokes 现象、Stokes 射线、anti-Stokes 射线、渐近求和、Dirichlet 边界条件、柯西–黎曼方程、Γ 函数、归一化常数。

## 6. 自检
```
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch02a.pdf
```
`python tools/lint.py ch02a` → 合计：问题 0 条，提示 1 条（提示内容：`\section` 数比 `\takeaway` 数多一个——即 §2.5 尚未结束，属预期）。
`python -c "open(...,encoding='utf-8').read()"` → `UTF8 OK`；草稿 30 页，已渲染 `work/preview/ch02a_*.png` 抽查（第 1、10、12、22、29、30 页等）：公式与原书一致、无溢出页边、图清晰、标点全角。

## 7. 存疑处 / 需 Lead 注意
1. **§2.5 跨块**：`\section{渐近方法}` 已在原书 p.96 写出，ch02b 从 p.108 接续时**不要再写一次** `\section{渐近方法}`；块尾已留两条注释说明此事与块界。
2. **原书未编号的粗体小标题**（Airy Function / Stokes Ray / Asymptotic Sum）用 `\subsection*{}`，不进入编号体系；若全书体例另有规定请 Lead 统一。
3. **重绘图**：p.98 复围道、p.106/p.107 的 λ 平面示意图均为简单示意图且原图内有英文（θ>0 small、Stokes rays、λ-plane、across the Stokes ray），按手册用 TikZ 重绘并把图内标注译为中文，未加题注。p.106 的 z 平面图与三幅曲线变化图含英文框注但不是简单示意图，保留裁切图并加了 `\fignote`。
4. **公式核对**：谐振子核、配分函数的两种算法、$\det A=2T$、Stirling 公式各步、艾里积分的 $I(\lambda)=2\pi\lambda^{-1/3}\mathrm{Ai}(-\lambda^{2/3})$ 均逐式回页图核对；抽取文本在这些地方错位严重，未采用。
5. **术语**：`Ré`/`Im` 一律 `\operatorname{Re}`、`\operatorname{Im}`；`Arg` 用 `\operatorname{Arg}`；艾里函数写作 `\operatorname{Ai}`。
6. 原文 p.95 一句 "Physics works!" 译作「物理是自洽的！」（口语感叹，保持原意不添内容）。
