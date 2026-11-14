# 电磁对偶、磁单极子凝聚与 N=2 超对称杨–米尔斯理论中的禁闭 —— 中文译注本

**底本**：N. Seiberg, E. Witten, *Electric-Magnetic Duality, Monopole Condensation,
and Confinement in N=2 Supersymmetric Yang-Mills Theory*，arXiv:hep-th/9407087v1
[hep-th]，1994 年 7 月 15 日，45 个 PDF 页（印刷页 1–44；PDF 第 1 页为标题/摘要页，
无印刷页码）。报告号 RU-94-52、IAS-94-43。期刊版为 Nucl. Phys. B426 (1994) 19–52，
另有 Erratum: Nucl. Phys. B430 (1994) 485–486。

**成品规模**：编译后 **32 页**；中文正文约 **1.74 万汉字**（源码约 12.2 万字节）；
编号公式 **108 个**，编号与原文逐一对应（§1: 2，§2: 16，§3: 30，§4: 9，§5: 21，§6: 30）；
`% [Tutor Note: ...]` 审校批注 **63 条**；脚注 5 条；参考文献 33 条（编号 [1]–[33] 与
原文一致）；原文插图 **2 幅**（原书 p.28 的图 1、p.38 的图 2），已裁出并插入正文。

## 1. 文件清单

```
9407087v1_中文译注.tex   ← 单一自足源码（主文件，无外部依赖）
9407087v1_中文译注.pdf   ← 编译产物（XeLaTeX 两遍，32 页，含目录/PDF 书签）
figures/fig1_u_plane.png ← 原书 p.28 图 1（$u$ 平面与单值性）
figures/fig2_one_cycle.png ← 原书 p.38 图 2（$x$ 平面中的围道提升为一维闭链）
README.md                ← 本文件
术语表.md                 ← 冻结术语表（正文术语的裁决书）
审校批注汇总.md           ← 63 条 [Tutor Note] 的分类索引（不读源码也能查阅）
静态校验报告.txt          ← 交付前静态审计 + 实际编译记录的逐项存档
```

## 2. 编译方法

```bash
xelatex 9407087v1_中文译注.tex
xelatex 9407087v1_中文译注.tex     # 第二遍生成目录与 PDF 书签
```

或 `latexmk -xelatex "9407087v1_中文译注.tex"`。

- 文档类：`ctexart`，**必须用 XeLaTeX**（中文排版）。
- 本稿用 `\documentclass[...,fontset=fandol]{ctexart}`，Fandol 字体随 TeX Live 提供，
  没有中文字体的最小 TeX 环境也能编译；若想改用系统字体，把 `fontset=fandol` 换成
  `fontset=windows`（Windows）或 `fontset=macnew`（macOS）。
- 依赖宏包：`geometry, fancyhdr, amsmath, amssymb, amsthm, mathtools, bm, graphicx,
  xcolor, booktabs, array, enumitem, caption, hyperref`（TeX Live / MiKTeX 常规安装均自带）。
- 源码中 `% [Tutor Note: ...]` 是 LaTeX 注释，编译后不显示；删除不影响编译。
- `keypoints` 环境与全部自定义宏都定义在导言区，无需外部文件。

## 3. 排版与翻译约定

1. **公式编号沿用原文**（如式 (2.14)、式 (3.30)），用 `\tag{}` 手工标注；正文一律写
   “式 (2.14)”，不做自动交叉引用，便于与英文本逐条对读。
2. **页码对应**：印刷页 = PDF 页 − 1。本 README 与批注中的“原书 p.N”均指印刷页。
3. **号差约定**：原文只在 §3.2 说明 “We work in Minkowski space … $F^2_{\mu\nu}=-(\ast F)^2_{\mu\nu}$、
   $\ast(\ast F)=-F$”，**并未明确写出度规号差**；这两条等价于“$*^2=-1$（4 维 2-形式）”，
   在 $(-,+,+,+)$ 与 $(+,-,-,-)$ 下都成立。译本照原文不擅自补写号差，相关讨论见 §3.2
   的批注。原文以 $\ast$ 表示 Hodge 对偶（原文印作 `*`），译本统一 `\ast`。
4. **记号统一**：原文 `N=2` 与 `\mathcal N=2` 混用，译本统一 `$\mathcal N=2$`；
   `U(1)_{\mathcal R}` 统一 `$U(1)_R$`；预势一律 `$\mathcal F$`，超势 `$W$`；
   微分一律 `\mathrm{d}`。
5. **术语**：以国内理论物理界通行译法为准（规范场、预势、模空间、磁单极子、双荷子、
   单值性、凯勒度规等）；人名、模型名保留拉丁字母（Seiberg、Witten、Olive、Montonen、
   Prasad、Sommerfield、Bogomol'nyi、Wess、Bagger）。冻结术语表见 `术语表.md`（随工作稿）。
6. **批注只写三类**：易错预警（指标、符号、归一化、号差、括号位置）、含糊点拨（作者写
   “显然/容易看出”而跳过的论证）、背景直觉（一两句物理图像）。每条都给出公式号与页码。
7. **每节开头「本节重点」**：6 个编号 section 各有一个 `keypoints` 环境（3–5 条提炼）。
8. **不臆造**：原文笔误一律照排并加批注，正文不“悄悄改正”；清单见 §8。

## 4. 章节与原文页码对照

| 章节 | 原文印刷页 | 原文 PDF 页 | 译本页 |
|---|---|---|---|
| 标题页／摘要 | — | 1 | 1 |
| 译者说明、目录 | — | — | 1–2 |
| §1 引言 | 1–4（p.4 仅顶部一段） | 2–5 | 3–4 |
| §2 $\mathcal N=2$ 超对称的回顾 | 4–8 | 5–9 | 5–8 |
| 　2.1 表示 | 4 | 5 | 5 |
| 　2.2 可重整拉格朗日量与经典平坦方向 | 5 | 6 | 6 |
| 　2.3 低能有效作用量 | 6–8 | 7–9 | 6–8 |
| （式 (2.15)(2.16) 与 §2.3 收尾） | 9（仅顶部） | 10 | 8 |
| §3 对偶 | 9–16 | 10–17 | 9–13 |
| 　3.1 数学描述 | 9–11 | 10–12 | 9–10 |
| 　3.2 对偶的物理诠释 | 11–14 | 12–15 | 10–12 |
| 　3.3 与引力的耦合 | 14–16 | 15–17 | 12–13 |
| §4 双荷子的质量 | 16–20 | 17–21 | 14–16 |
| §5 模空间的结构 | 21–33 | 22–34 | 17–24 |
| 　5.1 无穷远处的奇点 | 21 | 22 | 17 |
| 　5.2 强耦合处的奇点 | 22 | 23 | 18 |
| 　5.3 奇点的诠释 | 23–25 | 24–26 | 19 |
| 　5.4 无质量磁单极子的效应 | 25–26 | 26–27 | 20 |
| 　5.5 第三个奇点 | 26–27 | 27–28 | 21 |
| 　5.6 磁单极子凝聚与禁闭 | 28–31 | 29–32 | 22–23 |
| 　5.7 有效参数 | 32–33 | 33–34 | 24 |
| §6 模型的解 | 33–41 | 34–42 | 25–30 |
| 致谢 | 42 | 43 | 31 |
| 参考文献 | 43–44 | 44–45 | 31–32 |

> 说明：原文分页处偶有“上半页属前一节、下半页属后一节”的情况（如 p.5 顶部为 §1
> 余段、p.10 顶部为 §2.3 收尾、p.17 顶部为 §3.3 收尾、p.34 上半为 §5.7），表中按
> 正文归属标注。

## 5. 核心内容速览

- **目标**：精确求解四维 $\mathcal N=2$、$SU(2)$ 纯超杨–米尔斯理论的低能有效作用量，
  得到预势 $\mathcal F(a)$、真空模空间度规、以及电子/磁单极子/双荷子的精确质量公式。
- **工具**：低能有效作用量的全纯性；超对称代数的中心扩张（$Z=an_e+a_Dn_m$）；
  电磁对偶 $S:\tau\to-1/\tau$ 与 $T:\tau\to\tau+1$ 生成的 $SL(2,\mathbb Z)$；
  模空间上的凯勒几何与“特殊几何”变换。
- **关键突破**：量子模空间不作拓扑改变，但**强耦合区必须至少有两个奇点**，它们对应
  磁单极子（或双荷子）质量趋于零；磁单极子凝聚给出电荷禁闭。由此构造
  $y^2=(x-1)(x+1)(x-u)$ 的椭圆曲线族与 Seiberg–Witten 微分
  $\lambda=\frac{\sqrt2}{2\pi}\frac{\mathrm{d}x\,y}{x^2-1}$，其周期给出 $a,a_D$，
  单值性自动落在 $\Gamma(2)\subset SL(2,\mathbb Z)$ 中，从而唯一确定度规。
- **谱**：BPS 饱和态的谱不必在 $\Gamma(2)$ 下不变——穿过 $a_D/a$ 为实的曲线时谱会跳变；
  只有在实 $u$ 轴的 $|u|>1$ 一段才能从半经典区无跳跃地走到 $u=\pm1$，这保证强耦合处
  无质量粒子必须能由半经典磁单极子/双荷子连续演化而来。

## 6. 术语对照表（核心条目）

| English | 中文 | 备注 |
|---|---|---|
| $\mathcal N=2$ supersymmetric Yang–Mills | $\mathcal N=2$ 超对称杨–米尔斯 | 原文 N=2 |
| vector / chiral / hypermultiplet | 矢量 / 手征 / 超多重态 | hypermultiplet 首次括注英文 |
| superpotential / prepotential | 超势 / 预势 | $\mathcal F$ |
| Kähler potential / metric | 凯勒势 / 凯勒度规 | |
| moduli space of vacua | 真空模空间 | $u=\operatorname{Tr}\phi^2$ |
| central charge | 中心荷 | $Z=an_e+a_Dn_m$ |
| BPS bound / BPS-saturated | BPS 界 / BPS 饱和态 | |
| magnetic monopole / dyon | 磁单极子 / 双荷子 | dyon 首次括注 |
| electric-magnetic duality | 电磁对偶 | |
| Olive–Montonen duality | Olive–Montonen 对偶 | 人名保留拉丁字母 |
| monodromy / monodromy matrix | 单值性 / 单值矩阵 | $M_\infty,M_1,M_{-1}$ |
| modular domain / cusp | 模域 / 尖点 | |
| upper half plane / $\Gamma(2)$ | 上半平面 / $\Gamma(2)$ | |
| elliptic curve / one-cycle | 椭圆曲线 / 一维闭链 | |
| meromorphic differential / residue | 亚纯微分 / 留数 | |
| asymptotic freedom / $\beta$ function | 渐近自由 / $\beta$ 函数 | |
| instanton / condensate | 瞬子 / 凝聚 | |
| confinement | 禁闭 | |
| double cover / branch point | 二重覆盖 / 分支点 | |
| Weyl fermion | Weyl 费米子 | 首次括注“外尔费米子” |

> 完整冻结术语表（含记号表与反例表）见工作稿 `术语表.md`。

## 7. 图表核查

原文共两幅插图，均为矢量线条图（无位图）：图 1 位于原书 p.28（PDF 29），图 2 位于
原书 p.38（PDF 39）。核查方法（PyMuPDF：`page.get_drawings()` 与逐页渲染目视复核），
全篇仅 p.29 与 p.39（PDF 页号）含矢量绘图对象，与原文图位一致；两图已按绘图包围盒
裁出（350 dpi），置于 `figures/`，并在正文对应位置以 `figure` 环境插入、图注译为中文
并标注原书页码。正文中两处 “as shown in figure 1/2” 均照译为“如图 1/2 所示”。

## 8. 原文疑似笔误与可疑处

> 处理原则：**正文照原文排印**（个别处按语法作最小修正以读通），并在相应位置加
> `% [Tutor Note: ...]` 批注；不擅自“改正”数学内容。

| # | 位置（印刷页/公式） | 原文 | 判断与处理 |
|---|---|---|---|
| 1 | p.2 | “Prasad and Sommerfeld” | 文献 [10] 作 Sommerfield；人名拼写笔误，译文从通行拼法 |
| 2 | p.6 | “and a a complex parameter” | 重复 a；排印笔误 |
| 3 | p.7 式 (2.9) 后正文 | “$\mathcal F(\mathcal A)=\frac12\tau_{\rm cl}A^2$” | 花体 $\mathcal A$ 与斜体 $A$ 混用；式 (2.14) 作 $\mathcal F_0=\frac12\tau_{\rm cl}\mathcal A^2$，以后者为准（批注） |
| 4 | p.8 式 (2.12) | $W^a_\alpha W^b_\alpha$（两 $\alpha$ 均下标） | 按指标规则应为 $W^a_\alpha W^{b\alpha}$；对照 (2.7)(2.11)，疑笔误（批注） |
| 5 | p.13 式 (3.13) 后 | “is the the field strength” | 重复 the；排印笔误 |
| 6 | p.13 式 (3.25) | $f_{ij}f_D^{jk}=-\delta_i^k$ | 按 (3.24) 定义应为 $\tau_{ij}\tau_D^{jk}=-\delta_i^k$；疑 $\tau$ 误排为 $f$（照排＋批注） |
| 7 | p.16 式 (3.30) | $a_{D,0}=-iM_{\rm Pl}/2$ | 由 $G=(a^0)^2G_0,\ a_{D,0}=2a^0G_0$ 及量纲应为 $-iM_{\rm Pl}^2/2$；疑漏排平方（照排＋批注） |
| 8 | p.16 脚注 2 | “Once once considers …” | 重复 once；排印笔误 |
| 9 | p.17 | “from the the low energy” | 重复 the；排印笔误 |
| 10 | p.18 式 (4.6) | $\mp\sqrt2\,\partial_i(B_i^ah_a)$ 排在 $\Im\{\cdots\}$ 之外 | 原书排版如此，疑括号位置之疵；照排＋批注（按“全导数→表面项”解释） |
| 11 | p.21 | “So the transformation are” | 单复数（应为 transformations are）；照译 |
| 12 | p.24 | “counter intuitive” | 通行作 counterintuitive；轻微，译文无碍 |
| 13 | p.26 式 (5.10) | $a(u)=-h_D(u)$ | 按 §3 (3.19)–(3.20) 应为 $a=-h_D(a_D)$；原文简写/笔误（照排＋批注） |
| 14 | p.41 | “the region $u>1$” | 按上下文跳跃曲线为 $\|u\|=1$，避开区应为 $\|u\|>1$（或实轴 $u>1$ 一支）；疑笔误（照译＋批注） |
| 15 | p.13 式 (3.12)(3.14) | 公式末尾孤立句点 | 排版不一致；(3.13) 无句点；译本照原文 |
| 16 | 全文 | 期刊版另有 Erratum（Nucl. Phys. B430 (1994) 485–486） | 译本依据 arXiv v1，**未逐条比对勘误**；若需与期刊版一致请另行核对 |

> 第 3、4、6、7、10、13 条影响数学内容，均已在正文加批注；第 15 条为排版问题。
> 另有一处**记号提醒**：原文 §3.2 的 $F^2_{\mu\nu}=-(\ast F)^2_{\mu\nu}$ 若按矩阵平方
> $(F^2)_{\mu\nu}=F_{\mu\alpha}F^\alpha{}_\nu$ 理解并不成立，正文 (3.12) 展开实际用的是
> **标量** $F^2=-(\ast F)^2$；(3.12) 的整体符号亦与常见 $(+,-,-,-)$ 约定差一整体负号，
> 对偶推导只用相对符号，故 $\tau\to-1/\tau$ 的结论不变（详见 §3.2 批注）。

## 9. 已知限制

1. **未逐句回译**：译文以“读懂后重述”为主，长句按中文学术文风拆分；数学内容与公式
   逐符号对照页面图像核对，但个别语序调整未保留英文句法。
2. **批注取舍**：批注聚焦数学与物理，不解释基础概念；纯拼写/重复字问题汇总在 §8 表。
3. **号差**：原文未明确度规号差，译本未补写（见 §3、§8 说明）；涉及 $\ast$ 的公式
   照原文排印。
4. **勘误**：未逐条比对期刊版 Erratum（见 §8 第 16 条）。
5. **插图**：仅有原文两幅线条图；如后续版本含更多图，需另行处理。

## 10. 生成方式与可复现性

- 源文本：PyMuPDF `page.get_text("text")` 逐页提取（只用于定位段落），
  页面图像以 150 dpi 渲染（`pages/pNN.png`），公式逐一对图核对。
- 组装：`preamble.tex`（导言区）+ `front.tex`（标题/摘要/译者说明）+ 各节片段
  （`sections/s01–s06.tex`、`s02b.tex`、`refs.tex`）由 `build.py` 合并为单一自足源码，
  并把 `% @@FIG1@@`、`% @@FIG2@@` 替换为 figure 环境。
- 批注索引：`make_notes.py` 从源码自动抽取，批注改动后需重新生成（禁止手改生成物）。
- 静态审计：`final_audit.py` 生成 `静态校验报告.txt`（公式编号连续性、术语、禁用命令、
  编译日志、PDF 页数等逐项检查）。
- 实测编译：TeX Live 2026 + XeLaTeX 两遍 → 32 页，0 error，0 Overfull，0 缺字，
  1 处 Underfull（正文单行折行，纯视觉、可忽略）；目录与 PDF 书签正常。
