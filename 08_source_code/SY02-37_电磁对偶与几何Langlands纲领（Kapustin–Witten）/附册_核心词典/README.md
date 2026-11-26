# 核心罗塞塔石碑词典（Core Rosetta Stone）

数学 ↔ 物理对应的**最小组件集**：15 条核心词条，每条按百科词条（nLab 式）的严格度写——精确定义、可核对的陈述、可手算的例子、出处与真伪状态——外加一张「石碑总表」和一页版对照表。

与详册（`交付/罗塞塔词典/`，108 条、87 页）的分工：详册是**查阅**用的（按轨道铺开、每词条 250–520 字）；本册是**骨架**用的（只留不可再分的核心组件，每词条 700–1200 字、按定义—陈述—证明/构造—例—状态写）。

## 为什么叫罗塞塔石碑

Weil 在 1940 年代的信里说自己的工作「consists in deciphering a trilingual text」，手里只有「little pieces of the dictionary」——三栏即：数论 / $\mathbb F_q$ 上的函数域 / 黎曼面上的复分析。Frenkel 2009（arXiv:0906.2747）把这个比喻接到 Langlands 纲领上；几何 Langlands 是把第三栏换成「黎曼面上的几何」，KW06 再把它换成「4d $\mathcal N=4$ 超对称规范理论」这一物理栏。所以本册的每条词目都尽量写成**三栏并置**（数论、曲线、几何/物理），附录 A 是这张总表。

源流与引文见 `front.tex` 前言，原始文献：

- A. Weil, *Œuvres scientifiques*, Vol. I, 1940 年代书信（Frenkel 2009 §1 引）
- E. Frenkel, *Gauge theory and Langlands duality*, Séminaire Bourbaki 2009（arXiv:0906.2747）§1
- A. Kapustin, E. Witten, *Electric-magnetic duality and the geometric Langlands program*, arXiv:hep-th/0604151

## 目录

| 文件 | 内容 |
|---|---|
| `preamble.tex` | 版式与宏（`\mathdef \physdef \mathex \physex \bridge \intuit \pitfall`、`centry` 环境） |
| `main.tex` | 主文件（front → 15 条 → 附录 A） |
| `front.tex` | 扉页、前言（三栏石碑的来历、怎么读、体例） |
| `c1-duality.tex` | 1 电磁对偶；2 Langlands 对偶群；3 拓扑扭化与典范参数；4 Hitchin 模空间与超凯勒结构；5 Hitchin 纤维化与可积系统 |
| `c2-branes.tex` | 6 A/B 模型与膜的类型；7 B-膜=相干层；8 A-膜= Lagrange 膜与余各向同性膜；9 线算子：Wilson 与 't Hooft；10 特征膜 |
| `c3-langlands.tex` | 11 Hecke 算子与 Hecke 特征层；12 单极子模空间=Hecke 修正空间；13 D-模与平坦联络（量子 Langlands）；14 几何 Langlands 对应；15 翻译器 $B_{cc}$ |
| `appendix-stone.tex` | 附录 A：石碑总表（数学侧 ↔ 对译机制 ↔ 物理侧） |
| `stone-onepage.tex` | 一页版石碑（独立编译，横版四栏：核心组件 / 数论 / $\mathbb F_q$ 曲线 / 黎曼面 / 4d $\mathcal N=4$） |
| `SCHEMA.md` | 写作规范（含完整示范词条） |
| `blind/` | 盲测题面、词典纯文本、答卷、评分 |

## 构建

```bash
export PATH="/c/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64:$PATH"
xelatex -interaction=nonstopmode main.tex   # 跑 2–3 遍
xelatex -interaction=nonstopmode stone-onepage.tex
```

产物：`main.pdf` 24 页；`stone-onepage.pdf` 1 页。两份都应 `grep -c '^!' main.log` = 0、`Overfull` = 0。

## 质控（v1.0.3）

- 编译：24 页 / 0 error / 0 overfull / 0 undefined reference。
- 三条写作纪律：① 真伪状态必须标——每条末尾「状态与出处」写明定理（引用）/ 原文推导（argued）/ 纲要；② 例子必须可验算（如自对偶点 $g^2=4\pi$、$m_W=m_{\text{单极子}}=\sqrt{4\pi}v$；$g=2$ 亏格 $2$ 时 $\dim_{\mathbb C}\mathcal M_H=6$）；③ 单条 700–1200 汉字，定义自足。
- 盲测：见 `blind/CORE-ANSWERS.md` 与 `rosetta/blind/评分报告.md`。

## 版权

译文与注疏由本工程自行撰写；引用的原文公式、编号、图号均标注出处（arXiv:hep-th/0604151v3）。不收录原文连续段落。引用请注明：数译发布·SY02-37 附册。
