# 弦对偶的数学（TASI 2021 讲座）——中文译注本

原文：Niklas Garner, Natalie M. Paquette,
*TASI Lectures on the Mathematics of String Dualities*,
arXiv:2204.01914v2 [hep-th], 12 Apr 2022, 85 pp.（PoS 会议文集，TASI 2021 讲义）

> 说明：所给 PDF 的作者是 Garner 与 Paquette，并非 Witten。本译本按实际作者处理，
> 未在任何位置冒称 Witten 的工作。

## 1. 交付物结构

```
asi2204-zh/
├── main.tex                 # 导言区、标题页、摘要、译者说明、分片装配
├── sections/                # 21 个正文分片（s01 … s08-refs）
├── figures/
│   ├── fig01.png … fig14.png        # 14 幅插图，300 dpi 矢量渲染
│   └── inline/eq-p42-a.png …        # 5 处公式内嵌示意图（树图/阶梯图）
├── notes/annotations-index.md       # 228 条审校批注的分类索引与疑误汇总
├── pages/                   # 原文 85 页的 160 dpi 页面图（核对用）
├── text/                    # 原文 85 页文字层（措辞参考用）
├── build/main.pdf           # 编译产物
├── GLOSSARY.md              # 强制统一术语表
├── SPEC.md                  # 交付契约（分片规则、数学保真、批注规范）
├── REVIEW-NOTES.md          # 学术审校报告
├── README.md
├── build.ps1                # 编译脚本（tectonic）
└── tools/                   # crop.py / lint_frag.py / verify.py / crop_figs.py 等
```

## 2. 编译

```
pwsh -File build.ps1
```

或（有 TeX Live 时）：

```
xelatex main.tex && xelatex main.tex
```

中文使用 ctex 的 fandol 字库，无需系统字体；Windows 上若要用宋体/黑体，把 main.tex 中
`fontset=fandol` 改为 `fontset=windows`。公式编号全部用 `\tag{}` 锁定为原文编号。

## 3. 标记约定

源码中以 LaTeX 注释形式嵌入学术批注（不影响排版输出）：

| 标记 | 含义 |
|---|---|
| `% [Tutor Note: ...]` | 推导补足、易错预警、物理图像说明 |
| `% [原文疑误: ...]` | 已判定为原文笔误处，附判断依据 |
| `% [存疑: ...]` | 无法从页面图确证、但疑有问题之处 |
| `% [背景补充: ...]` | 对中文读者构成实质门槛的术语或背景 |
| `% ==== 原文 PDF 第 N 页 ====` | 页码锚点，保证逐页可对照 |
| `% [跨页接续: ...]` | 跨页断句说明 |
| `% [说明: 该式为原文矢量树图…]` | 公式内嵌示意图的来源说明 |

## 4. 图表清单

| 图 | 原文页 | 所在分片 | 内容 |
|---|---|---|---|
| Figure 1 | 7 | s02b | 二维 $\mathcal{N}=(2,2)$ 超对称代数的幂零簇 |
| Figure 2 | 24–25 | s02f | 2d TQFT 边界条件范畴中态射的合成 |
| Figure 3 | 25 | s02f | $\mathrm{Hom}_{\mathrm{Bdy}}(B_1,B_2)$ 的三种解释 |
| Figure 4 | 25 | s02f | 开弦粘合给出的态射合成 |
| Figure 5 | 26 | s02f | 边界局域算子与体局域算子的交换性 |
| Figure 6 | 31 | s02h | 世界面瞬子修正与全纯圆盘 |
| Figure 7 | 33 | s03a | Floer 乘积对应的全纯圆盘 |
| Figure 8 | 38 | s03b | 迭代乘积 $(O_1O_2)O_3$ 的小球嵌入 |
| Figure 9 | 43 | s03c | 四点构型空间与 $K_4(\epsilon)$ |
| Figure 10 | 47 | s03e | 三穿孔球面与三个拉格朗日 |
| Figure 11 | 50 | s03e | 体算子到 Hochschild 上链的前三个映射 |
| Figure 12 | 50 | s03e | 四面体 $\Delta^3$ 与边界算子位置 |
| Figure 13 | 51 | s03f | 构型空间中的 3-链 $B_3(\epsilon)$ |
| Figure 14 | 54 | s03f | 3-链 $L_3$ 的切片 |
| Table 1 | 19 | s02e | $B$ 扭变手征多重态的扭变自旋与分次 |
| Table 2 | 21 | s02e | $A$ 扭变手征多重态的扭变自旋与分次 |

公式内嵌示意图：第 42 页两行树图（$\mu_1,\mu_2,\mu_3$ 与 $A_\infty$ 关系）、
第 43 页第三条 $A_\infty$ 关系的树图、第 44 页第 $n$ 条 $A_\infty$ 关系的树图、
第 69 页 (B.18) 的 $\bar Q/Q$ 阶梯图。

## 5. 完整性核对

`python tools/verify.py` 检查：

- 21 个分片齐全；
- 182 个带号公式编号与原文逐一对应（2.1–2.54、3.1–3.76、A.1–A.9、B.1–B.27、C.1–C.16），无缺号、无重号；
- 页码锚点覆盖原文第 1–85 页；
- 14 幅插图与 5 个内嵌示意图全部被引用且文件存在；
- 各分片批注数量。

（具体核对结果见 `REVIEW-NOTES.md`。）
