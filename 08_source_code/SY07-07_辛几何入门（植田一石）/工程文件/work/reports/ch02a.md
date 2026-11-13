# ch02a 施工报告

## 负责页段
PDF 15–30 = 原书 p.6–21（第 2 章「分析力学」前半：章首引言 + 2.1 Newton 运动定律 ～ 2.5 Hamilton 形式的分析力学开头）。

## 文件
- `src/chunks/ch02a.tex`：36,767 bytes（约 35.9 KB），1,118 行，UTF-8 无 BOM、LF 换行（crlf=0）。
- 本章的 `\chapter{分析力学}` **在本 chunk 写**（全书仅此一次）；本 chunk **不写** `\chapterreview`（章末由 ch02b 收尾）。
- 页面标记 `% [原文 p.N]`：p.6–p.21 共 16 处齐全。
- 结尾停在 p.21 末句「在 Lagrange 形式的分析力学中，」，下接注释 `% [本 chunk 到此为止；该句续见 ch02b（原书 p.22）]`，与 ch02b 开头（p.22 上半，2.5 收尾要点清单与 Liouville 形式）首尾相接、无重复。

## 节与公式
- 章首引言：分析力学 200 年历史；不循「非退化闭 2 形式」定义辛流形之路，先公理化泊松流形、再作为特殊情形引出辛流形。
- **2.1 Newton 运动定律**：(2.1.1) 运动方程；三定律以 description 环境逐条列出（第一/二/三定律，手工编号不编号）；Galilei 坐标系、动量守恒、Noether 定理与守恒量。
  - 2.1.1 简谐振动（图 2.1）：(2.1.2)–(2.1.4)。
  - 2.1.2 单摆（图 2.2）：(2.1.5)–(2.1.11)，能量守恒、分离变量、椭圆积分。
  - 2.1.3 Kepler 问题：(2.1.12)–(2.1.52)；约化质量、角动量守恒（(2.1.31) 四行 aligned）、能量守恒、轨道方程（(2.1.39)–(2.1.52)，含圆锥曲线 (2.1.52) 与图 2.3）。
  - `\takeaway`（本节重点）：Newton 三定律以 Galilei 坐标系为前提，其「力」概念不明、坐标系受限。
- **2.2 Lagrange 形式的分析力学**：(2.2.1)–(2.2.35)。
  - 2.2.1 变分原理：(2.2.1)–(2.2.8)；Fermat 原理（`\fkstmt` 框）、光程泛函、折射率、Snell 法则 (2.2.6)、作用泛函。
  - 2.2.2 Euler--Lagrange 方程式：(2.2.9)–(2.2.17)；变分 (2.2.11)–(2.2.14)、变分法基本引理 (2.2.15)、EL 方程 (2.2.16)、L=K−V (2.2.17)。
  - 例 2.2.2 简谐振动 (2.2.18)–(2.2.21)；例 2.2.3 单摆 (2.2.22)–(2.2.25)；例 2.2.4 Kepler 问题 (2.2.26)–(2.2.31)；remark 2.2.1（高阶 jet 丛理论）。
  - 2.2.3 动量的守恒定律：(2.2.32)–(2.2.35)；循环坐标、共轭动量、平移生成。
  - `\takeaway`：运动是作用量的驻点；变分原理给出 Euler--Lagrange 方程，循环坐标对应动量守恒。
- **2.3 Legendre 变换**：(2.3.1)–(2.3.10)；严格凸、Hesse 矩阵、Legendre 变换 (2.3.4)、两次变换复原 (2.3.8)–(2.3.10)。`\takeaway` 一处。
- **2.4 Legendre--Fenchel 变换**：(2.4.1)–(2.4.6)（图 2.4）；支撑超平面、凸包、LF 变换的几何意义；itemize 四条性质。`\takeaway` 一处。
- **2.5 Hamilton 形式的分析力学（开头）**：(2.5.1)–(2.5.19)；相空间、Hamilton 函数、正则运动方程式、Hamilton 原理（相空间上的变分 (2.5.14)–(2.5.18)）。2.5 的 `\takeaway` 属 ch02b（本节未完）。
- 小结：`\takeaway` 共 4 处（2.1 / 2.2 / 2.3 / 2.4），无 `\chapterreview`；插图 4 张（fig2.1–2.4），均带中文 `\figtitle`。

## 编译判据
`powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch02a`（工程根目录）：

```
==> pass 1 exit=0
==> pass 2 exit=0
LOG  file:line=0  fatal=0  undefined=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> tmp_ch02a.pdf
```

- 草稿 PDF：`tmp_ch02a.pdf`，18 页。
- 渲染抽查（pymupdf / pdftoppm 100dpi）：第 1、2、3、8、13、14、18 页，中文正文、公式编号、图与本节重点框均正常；4 张图无日文图题残留、图不残缺。

## 批注（共 14 条：背景 6 / 难点 5 / 校勘 3）
16 页平均 0.88 条/页，未超 2 条/页上限。

| 原书页 | 类型 | 内容（摘要） |
|---|---|---|
| p.6 | 背景 | Newton 三定律出自《自然哲学的数学原理》(1687)；第一定律实质是断言惯性系存在。 |
| p.7 | 背景 | Noether 定理（1918）：时间平移→能量、空间平移→动量、旋转→角动量。 |
| p.9 | 背景 | Kepler 问题是二体问题，解空间 12 维，约化到质心 3 维 + 相对平面轨道 2 维。 |
| p.9 | 难点 | (2.1.12)(2.1.13) 力大小相同、方向相反，正是第三定律。 |
| p.10 | 背景 | 角动量守恒对应旋转对称性，是 Kepler 第二定律（面积速度一定）的内蕴原因。 |
| p.10 | 难点 | (2.1.25) 用 $\dot{\bm{x}}\times\dot{\bm{x}}=0$ 与 (2.1.19)；$\bm{x}\times(-\bm{x}/|\bm{x}|^3)=0$ 因共线。 |
| p.11 | 难点 | (2.1.35) 右端 $\grad f\cdot\dot{\bm{x}}$ 即 $f$ 沿轨道的方向导数。 |
| p.11 | 校勘 | 原书「(2.1.32) を」应为 (2.1.33)，照录原文。 |
| p.12 | 校勘 | 由 (2.1.49) 的 $M^2=el$，(2.1.50) 末项应为 $el/r-1$、(2.1.51) 应为 $er\cos\theta=el-r$；原书印作 $el/4-1$、$el-1$，照录。 |
| p.13 | 背景 | Fermat 原理严格说应表述为光程取驻值（一般非最小），原书作「最小」，译文照原书。 |
| p.16 | 校勘 | 例 2.2.3、例 2.2.4 原书 Lagrange 函数均印作 $L(x,v)$，按坐标应分别为 $L(\theta,\omega)$、$L(\bm{x}_1,\bm{x}_2,\bm{v}_1,\bm{v}_2)$；(2.2.25) 第二项按推导应含 $m$。均照录。 |
| p.17 | 难点 | (2.2.31) 即二体分解为重质心运动（质量 $m_1+m_2$）与相对运动（约化质量）。 |
| p.18 | 背景 | 取 $V=T_qW$、$f=L(q,\cdot)$，(2.3.4) 给出 Hamilton 函数，$p=\partial L/\partial\dot q$ 即共轭动量。 |
| p.21 | 难点 | 此处把 $\bm{p}$ 视为与 $\bm{q}$ 独立的变量（不再要求 $\bm{p}=\partial L/\partial\dot{\bm{q}}$），是相空间表述的关键。 |

## 新增术语（TERMS.md 未收，本 chunk 自定）
| 原文 | 译名 | 备注 |
|---|---|---|
| 換算質量 | 约化质量 | reduced mass（(2.1.18)，首现括注西文） |
| 配位空間 | 位形空间 | configuration space |
| 相空間 | 相空间 | phase space |
| 共役運動量 | 共轭动量 | conjugate momentum |
| 循環座標 | 循环坐标 | cyclic coordinate |
| 停留点 | 驻点 | stationary point（作用量的驻点） |
| 厳密凸 | 严格凸 | strictly convex |
| 支持超平面 | 支持超平面 | supporting hyperplane |
| 凸包 | 凸包 | convex hull |
| 光学距離 | 光学距离 | optical distance |
| ジェット束 | jet 丛 | jet bundle（$k$ 阶 jet 丛） |
| 楕円積分／楕円関数 | 椭圆积分／椭圆函数 | elliptic integral / elliptic function |
| 焦点／準線 | 焦点／准线 | focus / directrix |

## 疑似原书笔误（均照原样译，另加校勘批注）
1. p.11 正文：「(2.1.32) を」由上下文应为 (2.1.33)。
2. p.12 (2.1.50)：$M^2/r-1=el/4-1$，由 (2.1.49) 的 $M^2=el$ 及 (2.1.52) 应为 $el/r-1$。
3. p.12 (2.1.51)：$er\cos\theta=el-1$ 应为 $er\cos\theta=el-r$。
4. p.16 例 2.2.3、例 2.2.4：Lagrange 函数印作 $L(x,v)$，按各自坐标应为 $L(\theta,\omega)$、$L(\bm{x}_1,\bm{x}_2,\bm{v}_1,\bm{v}_2)$。
5. p.16 (2.2.25)：$mgR\sin\theta+\frac{\rd}{\rd t}(R^2\dot\theta)=0$，第二项按推导应含因子 $m$（应为 $\frac{\rd}{\rd t}(mR^2\dot\theta)$）。

## 图片与版面
- 4 张 `figures/fig2.N.png` 原图底部内嵌原书日文图题（「図 2.1 単振動.」等），与中文 `\figtitle` 重复。处理：用 `trim`+`clip` 裁掉底部日文图题条带（PNG 含 300 dpi 元数据，natural size = px×0.24 bp）：fig2.1 `trim=0 19.2bp 0 0`、fig2.2 `trim=0 6.48bp 0 0`、fig2.3 `trim=0 32.88bp 0 0`、fig2.4 `trim=0 14.16bp 0 0`。裁切量与各 PNG 的暗行分组精确对齐（已按行扫描核算），渲染确认无日文残留、图不残缺。
- fig2.2 底部左侧有一个原图自带的极小扫描杂点（非图题残留），未作处理。
- 若后续在 `figures/` 层统一裁切图题，可删去以上 `trim` 参数。

## 事故记录（编码损坏与恢复，供 Lead 知悉）
- 15:31 前后我用 PowerShell `Get-Content -Raw` + `[System.IO.File]::WriteAllText` 修改 `\includegraphics` 行；PS 5.1 默认按 ANSI/GBK 解码 UTF-8，导致整份 ch02a.tex 变成「双重编码」乱码（典型字：鈥 锛 銆 鍒 鏂 鐨），编译报 `./draft.tex:5: File ended while scanning use of \textbf`、missingchar=26。
- 恢复方式：从 build 镜像快照 `<本地路径>`（2026-11-08 15:24:22，33313 bytes，干净，止于 (2.5.9)）二进制复制回 `src/chunks/ch02a.tex`，再用 `edit` 工具补写 p.21 内容、重做 4 处 trim、补 2.3 的 `\takeaway`。
- 之后所有 `.tex` 改动只用 `write`/`edit` 工具；python 校验脚本只读（显式 `encoding='utf-8'`）。最终乱码字符扫描 = 0。
- 教训：本工程禁止用 PowerShell 的 Get-Content / Set-Content / Out-File 处理 .tex。

## 待核 / 未解
- (2.1.50)(2.1.51) 按原书照录并加校勘；若书末勘误表另有说明，以勘误表为准。
- 本 chunk 末句为半句（续 ch02b），属刻意拆分；ch02b 已注明从 p.22 上半接续，无重复。
- 2.5 节的 `\takeaway` 未写（本节延续到 ch02b），由 ch02b 负责该节小结。

## 需要的宏
无。全部使用 preamble 已有宏（`\rd`、`\R`、`\cP`、`\grad`、`\bm`、`\fkstmt`、`\figtitle`、`\takeaway`、statement 环境等）；未修改 `preamble.tex`。
