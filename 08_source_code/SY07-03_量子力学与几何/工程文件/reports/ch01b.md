# 块报告：ch01b

## 1. 块名与页段
- 块名：`ch01b`
- 页段：PDF 31–48 = 原书 p.30–47
- 源文件：`work/en/ch01b.txt`（清洗稿 `work/review/ch01b_clean.txt`）

## 2. 节清单（标题按原文，不写编号）
- §1.5.4 定态（收尾一段，属 ch01a 页段；自上页残句 "Equation (*) is called..." 起译）
- §1.6 自由粒子：连续谱的例子
  - 1.6.1 波包
  - 1.6.2 群速度
- §1.7 谐振子：离散谱的例子
  - 1.7.1 阶梯算子
  - 1.7.2 基态
  - 1.7.3 激发态
- §1.8 方势阱：混合谱的例子
  - 1.8.1 匹配条件
  - 1.8.2 束缚态
  - 1.8.3 散射态

## 3. 陈述编号清单（手工照抄原文）
| 环境 | 编号 | 位置 |
|---|---|---|
| example | 1.6.1（高斯波包） | 原书 p.31 |
| proposition | 1.7.1 | 原书 p.37 |
| proposition | 1.7.2 | 原书 p.37 |
| proposition | 1.7.3 | 原书 p.38 |

另：原文式号 $(*)$（衔接条件，p.41）、$(**)$（$\lambda=\mu\tan\mu a$，p.41）用 `equation*` + `\tag` 复现。

## 4. 图清单
| 文件 | 来源页 | 处理方式 |
|---|---|---|
| `figures/fig_p32_a.png` | 原书 p.31 | 裁切（高斯曲线 + δ√ħ 双向箭头；顶部混入正文一行，已裁掉） |
| `figures/fig_p33_a.png` | 原书 p.32 | 裁切（φ̂₀ 尖峰 + k₀ + 坐标轴；同上处理） |
| `figures/fig_p35_a.png` | 原书 p.34 | 裁切（弹簧–质量块装置图，含 F=−kx 与位移 x 括号；同上处理） |
| `figures/fig_p40_a.png` | 原书 p.39 | 裁切（方势阱剖面 V(x)） |
| `figures/fig_p42_a.png` | 原书 p.41 | 裁切（势阱 + 能级线 E） |
| `figures/fig_p43_a.png` | 原书 p.42 | 裁切（y=tan u 与 y=√((u₀/u)²−1) 交点图） |
| `figures/fig_p44_a.png` | 原书 p.43 | 裁切（y=−cot u 交点图） |
| `figures/fig_p44_b.png` | 原书 p.43 | 裁切（势阱 + 虚线能级 E₀,E₁,E₂） |
| `figures/fig_p45_a.png` | 原书 p.44 | 裁切（ψ₀,ψ₁,ψ₂ 三条波形） |
| `figures/fig_p45_b.png`、`fig_p45_c.png` | 原书 p.44 | 裁切（深阱极限偶/奇两图），下方英文 "even case / odd case" 改排中文「偶情形／奇情形」 |
| `figures/fig_p46_a.png` | 原书 p.45 | 裁切（势阱 + E>0） |
| `figures/fig_p48_a.png` | 原书 p.47 | 裁切（T–E 振荡曲线，含 T、E 轴标与 1 虚线） |
| TikZ（2 张，原书 p.46） | 原书 p.46 | 按原文重绘：势阱轮廓 + A/B/F 波包箭头；图内 legend 原为英文，已译「A：入射波振幅／B：反射波振幅／F：透射波振幅」 |

未采用的 auto 候选：`fig_p47_a.png`、`fig_p47_b.png`（只有势阱轮廓、顶部被自动裁切，已改用 TikZ 重绘）。
所有裁切图均为 300 dpi 灰度 PNG，宽 0.52–0.90\textwidth，不加题注。

## 5. 未决术语
见 `work/term_requests_ch01b.md`（20 条）：德布罗意关系、物质波、色散关系、群速度、相速度、高斯波包、定态、定态薛定谔方程、升算子、降算子、厄米多项式、数算子、概率流、入射/反射/透射波振幅、衔接条件、深阱极限、共振透射、偶函数、奇函数。

## 6. 自检
```
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch01b.pdf
```
`python tools/lint.py ch01b` → 合计：问题 0 条，提示 0 条。
渲染抽查（`work/preview/ch01b_*.png`，共 21 页）：公式与原书逐条核对，无溢出页边，图清晰，标点全角。

## 7. 存疑处 / 需 Lead 决定
1. **块首残留**：已按 Lead 指示从「方程 $(*)$ 称为定态薛定谔方程」起译，不重复 `ψ`；本块开头一段属 §1.5.4，故不写 `\takeaway`（§1.5 的五段 takeaway 归 ch01a）。
2. **圈号 ①②**：Unicode 圈号在 `lmroman` 中缺字（missingchar=4），改用标准 `\textcircled{1}`、`\textcircled{2}`。若全书想统一成 `（1）（2）` 或换字体，请 Lead 定。
3. **式号**：`(*)(**)` 用 `\begin{equation*}...\tag{$*$}\end{equation*}`，与手册「原文 (*) 用 \tag」一致。
4. **原文笔误**：p.44 "Surprisedly" → 已加 `% [Tutor Note: ...]`，正文译作「令人惊讶的是」。
5. **深阱极限段**：原文 "Nevertheless, it is clear that we have at least one solution, no matter how small u₀ is." 指偶解（tan 曲线必与红线相交），照译未改写。
6. 紧接本块的 §1.9 散射从 PDF 49 起，不在本块范围。
