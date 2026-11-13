# ch02b 译注报告

## 1. 块名与页段

- 块名：ch02b（第 2 章中段块，非章首）
- 页段：PDF 109–138（原书 p.108–137），共 30 个原书页
- 输出文件：`src/chunks/ch02b.tex`（1534 行）
- 本块开头承接 §2.5 尾部（原书 p.108 顶部），故块首先补写 §2.5 的 `\takeaway`（第 20 行），再开 §2.6。`ch02a.tex` 末行注释已声明该 `\takeaway` 由本块补写，两文件无重复。本块非章首、非章末，无 `\chapter`、无 `\chapterreview`。

## 2. 节清单

- §2.6 半经典近似
  - 2.6.1 半经典的费曼核（内含 `\subsubsection*{行列式计算}`，Coleman 论证全程）
  - 2.6.2 雅可比场
  - 2.6.3 时间切片方法
- §2.7 格林函数
  - 2.7.1 固定能量下的格林函数
  - 2.7.2 半经典分析（含无编号小标题「情形 $x'<0<x''$」与「情形 $x'<x''<0$」）
  - 2.7.3 经由路径积分的 WKB（内含 `\subsubsection*{量子隧穿}`、`\subsubsection*{连接公式再探}`）

`\takeaway` 共 3 处：§2.5（第 20 行）、§2.6（第 565 行）、§2.7（第 1532 行）。

## 3. 陈述编号清单（共 9 条，编号全部照抄原文）

- 注 2 条：2.6.1、2.7.4
- 例 7 条：2.6.2（自由粒子）、2.6.3（谐振子）、2.7.2（自由粒子）、2.7.3、2.7.5（自由粒子）、2.7.6（线性势）

说明：
- 例 2.6.2、2.6.3、2.7.2、2.7.5、2.7.6 的标题写在编号后（如 `\begin{example}{2.7.6（线性势）}`），避免出现「2.7.6.（线性势）」双标点。
- 例 2.7.6 跨原书 p.123–130，`\end{example}` 置于 §2.7.3 `\subsection` 之前，与原书排版一致。
- 原书该段无 theorem/proposition 环境，无 `proof` 环境（证明以正文直述），故未使用 `proof` 环境。

## 4. 图清单（23 张，全部为裁切 PNG，TikZ 0 张）

| 文件 | 来源页 | 处理方式 |
| --- | --- | --- |
| `figures/fig_p114_a.png` | 原书 p.113 | 雅可比场示意，裁切 PNG |
| `figures/fig_p115_a.png` | 原书 p.114 | 共轭点椭圆，裁切 PNG |
| `figures/fig_p117_a.png` | 原书 p.116 | 时间轴 $t_0,\dots,t_N$ 与 $\varepsilon$ 括号，裁切 PNG |
| `figures/fig_p120_a.png` | 原书 p.119 | $p$ 平面红半圆与极点 $p_\pm$，裁切 PNG |
| `figures/fig_p126_a.png` | 原书 p.125 | $V$–$x$ 图（$0<x'<x''$），裁切 PNG（重裁一次去正文残行） |
| `figures/fig_p127_a.png` | 原书 p.126 | $T$ 平面四个实鞍点，裁切 PNG（重裁一次） |
| `figures/fig_p128_a.png` | 原书 p.127 | 四鞍点切向蓝线段，裁切 PNG |
| `figures/fig_p128_b.png` | 原书 p.127 | 红色最速下降围道＋Case 标签，裁切 PNG |
| `figures/fig_p129_a.png` | 原书 p.128 | $V$–$x$ 图（$x'<0<x''$），裁切 PNG（重裁一次） |
| `figures/fig_p129_b.png` | 原书 p.128 | $T$ 平面四个复鞍点，裁切 PNG |
| `figures/fig_p130_a.png` | 原书 p.129 | 切向方向与红色最速下降曲线，裁切 PNG |
| `figures/fig_p131_a.png` | 原书 p.130 | $V$–$x$ 图（$x'$、$x''$ 均在禁区），裁切 PNG |
| `figures/fig_p131_b.png` | 原书 p.130 | $T$ 平面纯虚四鞍点，裁切 PNG（重裁去正文残字） |
| `figures/fig_p132_a.png` | 原书 p.131 | 形变后的两条围道曲线，裁切 PNG |
| `figures/fig_p133_a.png` | 原书 p.132 | 势垒 $V(x)$、$E$、$a$、$b$，裁切 PNG |
| `figures/fig_p134_a.png` | 原书 p.133 | 两幅 $V$–$x$ 图与箭头，裁切 PNG |
| `figures/fig_p135_a.png` | 原书 p.134 | $x'$ 平面半圆与红色箭头，裁切 PNG（重裁，避开正文与标签） |
| `figures/fig_p135_b.png` | 原书 p.134 | when $0<x'<x''$ 图，裁切 PNG |
| `figures/fig_p136_a.png` | 原书 p.135 | when $x'<0<x''$ 图，裁切 PNG |
| `figures/fig_p137_a.png` | 原书 p.136 | 四鞍点与红色曲线（多支鞍点），裁切 PNG，保留彩色 |
| `figures/fig_p137_b.png` | 原书 p.136 | $\theta=0,\pi/3,\pi$ 三格图，裁切 PNG（重裁，右侧 $T_s^{(++)}$ 曾被切） |
| `figures/fig_p138_a.png` | 原书 p.137 | 两幅 $V$ 图＋两幅 $T$ 平面图，裁切 PNG（重裁一次） |
| `figures/fig_p138_b.png` | 原书 p.137 | 从 $T_s^{(--)}$ 出发的最速下降线（半圈）图，正文由此得鞍点贡献 $T_s^{(-+)}+\tfrac12 T_s^{(--)}$，裁切 PNG |

- 以上图均无题注（原书无题注），图后注释「原书 p.N，图内文字照原样保留」。
- 5 处图内含英文整句，加 `\fignote`（p.127 的 `Case: $0<x'<x''$.`；p.134 的 `x'-plane`；p.134/135 的 `when …`；p.136 的 `when …`），并译出中文。
- 原书 p.127 的 $S_{cl}''$ 符号刻度小图属数学装饰，未嵌图，改写为正文句子（$T_s^{(--)}$ 处 $S_{cl}''>0$、$T_s^{(+-)}$ 处 $S_{cl}''<0$、$T_s^{(-+)}$ 处 $>0$、$T_s^{(++)}$ 处 $<0$）。

## 5. 术语与宏

- 未收术语 7 条，已登记 `work/term_requests_ch02b.md`：semi-classical Feynman kernel 半经典费曼核（p.108）、Jacobi field 雅可比场（p.112）、Jacobi equation 雅可比方程（p.113）、conjugate point 共轭点（p.113）、Van Vleck–Pauli–Morette formula 范弗莱克–Pauli–Morette 公式（p.114）、Cauchy principal value 柯西主值（p.118）、Wronskian 朗斯基行列式（p.119）。
- 表内术语照用：semi-classical 半经典的、stationary phase 驻定相位、steepest descent 最速下降、saddle point 鞍点、oscillatory integral 振荡积分、Green's function 格林函数、turning point 转折点、WKB 近似、Maslov index 马斯洛夫指标、connection formula 连接公式、Stokes phenomenon 斯托克斯现象、Stokes line 斯托克斯线、Airy function 艾里函数、time slicing 时间切片、resolvent 预解式、propagator 传播子、semi-classical parameter 半经典参数、van Vleck 范弗莱克、Jacobi 雅可比、Feynman 费曼。
- 用到的宏：`\hs`、`\ii`、`\ee`、`\rd`、`\pa`、`\abs`、`\norm`、`\bra`、`\ket`、`\braket`、`\mel`、`\wh`、`\ol`、`\eps`、`\R`、`\C`、`\Z`、`\R_{\ge0}`、`\Imag`、`\Real`、`\Res`、`\tr`、`\mathcal{D}`（路径积分测度）；未改 preamble。

## 6. Tutor Note

本块未加 Tutor Note（0 条）。原书个别记号不一致（如 T 带共轭横线）按原样照抄，见第 8 节。

## 7. 自检

```
build.ps1 -Chunk ch02b
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch02b.pdf（33 页）

python tools\lint.py ch02b
OK   ch02b  字数 35480  段 2  小节 6  陈述 9  公式 218  图23(TikZ 0)  脚注 0
合计：问题 0 条 提示 1 条
```
唯一提示「`\section`=2 而 `\takeaway`=3」：多出的 1 条是块首为 §2.5 补写的 `\takeaway`（ch02a 末尾已注明交由本块补），属预期的跨块现象。

渲染抽查：`work/preview/ch02b_*.png`（100 dpi，33 页）逐页看，抽查第 1、3、12、20、24、25、27、29、30、31、32、33 页：公式与原书一致、无溢出页边、图清晰、中文全角标点。

## 8. 存疑与交接

1. **块界**：原书 p.108 顶部「The asymptotic expansion $I(\lambda)\simeq n_-\int_{C^\lambda_-}+n_+\int_{C^\lambda_+}$ will display a jump … which is given by the dominate term $n_+\int_{C^\lambda_+}$。」承接 ch02a（§2.5 尾部），已核对与 `src/chunks/ch02a.tex` 末段无重复、与本块第 6–18 行逐句一致。
2. **原书记号**：p.126–127 的最速下降流方程中 $T$ 带共轭横线，即 $\frac{\rd T}{\rd u}=\ii\left[-\frac{m}{2\bar T^2}(x''-x')^2+\frac{\lambda}{2}(x''+x')-\frac{\lambda^2\bar T^2}{8m}\right]$，按原书照抄，未统一记号。
3. **图内英文**：p.127 的 `Case: $0<x'<x''$.`、p.134–136 的 `when …`、`x'-plane` 均以 `\fignote{图内文字：…（译：…）}` 给出，图内原样保留。
4. **例 2.7.6 跨页**：该例从原书 p.123 起、在 p.130 结束，跨 §2.7.2 与 §2.7.3 交界，`\end{example}` 置于 §2.7.3 之前，与原书排版一致；合书时若与 ch02c 有块界重叠需复核。
5. **p.136–137 多支鞍点图**：按 Lead 要求裁切 PNG 保留彩色，未做 TikZ 重绘（图内为彩色曲线与箭头，非简单示意）。
