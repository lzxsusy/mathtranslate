# 量子力学路径积分的新视角 —— 中文译注本

**底本**：Edward Witten, *A New Look At The Path Integral Of Quantum Mechanics*,
arXiv:1009.6032v1 [hep-th], 30 Sep 2010, 77 pp（PDF 78 页）。

**成品规模**：中文 58 页；正文公式 189 个（编号与原文逐一对应）；审校批注 160 条；
原文唯一插图 Figure 1 已裁出并插入正文。

## 文件清单

```
1009.6032v1(1)_中文译注.tex     ← 单一可编辑源码（主文件，自足，无外部依赖）
1009.6032v1(1)_中文译注.pdf     ← 编译产物（XeLaTeX 两遍，58 页）
figures/fig1_cycles.png         ← 从原文 PDF 600 dpi 裁出的 Figure 1
README.md                       ← 本文件
审校批注汇总.md                  ← 全部 [Tutor Note] 的索引（不读源码也能查阅）
```

## 编译方法

```bash
xelatex 1009.6032v1(1)_中文译注.tex
xelatex 1009.6032v1(1)_中文译注.tex     # 第二遍生成目录与 PDF 书签
```

或 `latexmk -xelatex "1009.6032v1(1)_中文译注.tex"`。

- 文档类：`ctexart`，**必须用 XeLaTeX**（中文排版）。
- 依赖宏包：`amsmath, amssymb, amsthm, mathtools, bm, graphicx, xcolor,
  booktabs, array, enumitem, caption, hyperref, fancyhdr`，均为 TeX Live / MiKTeX
  常见安装自带；精简发行版可运行
  `tlmgr install ctex xecjk fandol enumitem caption mathtools bm fancyhdr`。
- 已验证：XeLaTeX 编译 0 error、0 overfull、0 缺字；PDF 书签/目录正常。
- 源码可直接编辑：章节、公式、批注均为纯文本；`% [Tutor Note: ...]` 是注释，
  删除或保留都不影响编译。

## 排版与翻译约定

1. **公式编号沿用原文**（式 (2.37)、式 (A.9) 等），用 `\tag{}` 手工标注；正文一律
   写“式 (2.37)”，不做自动交叉引用，以便与英文本逐条对读。
2. **页码对应**：PDF 页号 = 原文印刷页码 + 1（第 1 页为标题页）。
3. **图表**：原文仅一幅图（Fig. 1，p.4），已 600 dpi 裁出并插入 §1 对应位置；
   图注译为中文并标注原文位置，图注中的原文笔误在批注中指出。
4. **批注**（160 条）：`% [Tutor Note: ...]` 为源码注释（编译后不显示），内容包括
   - 易错预警：指标缩并、符号约定、全导数/边界项、上下标横线等；
   - 含糊点拨：作者用 “It is obvious / One can show” 跳过之处，补出所用定理与文献；
   - 原文笔误：如实指出并给出正确形式；
   - 术语说明：非常规译名首次出现时给出英文原词。
5. **每节重点**：§1–§5 及附录 A 开头均有 `keypoints` 环境（物理图像 / 数学工具 / 结论）。
6. **术语**：以国内理论物理界通行译法为准（规范场论、和乐、反常、余各向同性膜、
   莫尔斯理论、Floer 上同调等）。

## 章节与原文页码对照

| 章节 | 原文印刷页 | PDF 页 |
|---|---|---|
| §1 引言 | 3–5 | 4–7 |
| §2 量子力学的积分围道 | 6–29 | 7–30 |
| §2.1 预备知识 | 6–7 | 7–8 |
| §2.2 基本的费曼积分 | 8 | 9 |
| §2.3 解析延拓 | 9–11 | 10–12 |
| §2.4 最简单的积分围道 | 11–13 | 12–14 |
| §2.5 莫尔斯理论回顾 | 14–15 | 15–16 |
| §2.6 费曼积分的一个新积分围道 | 16–18 | 17–19 |
| §2.7 $I$ 与 A-模型 | 19–20 | 20–21 |
| §2.8 用 σ-模型语言解释 | 21–23 | 22–24 |
| §2.9 物理模型（含 2.9.1） | 24–27 | 25–28 |
| §2.10 还原希尔伯特空间 | 28–30 | 29–31 |
| §3 哈密顿量（3.1、3.2、3.2.1–3.2.3） | 30–38 | 31–39 |
| §4 反其道而行（4.1、4.2） | 39–47 | 40–48 |
| §5 含规范场的类比（5.1、5.1.1–5.1.3） | 47–61 | 48–62 |
| §5.2 应用于陈–西蒙斯（5.2.1–5.2.4）、§5.3 | 62–70 | 63–71 |
| 附录 A 四维边界条件的细节（A.1、A.2） | 70–75 | 71–75 |
| 参考文献 | 75–77 | 76–78 |

## 核心内容速览

- 把量子力学的相空间路径积分解析延拓到复化相空间；复化积分的“积分围道”
  （相对同调中的闭链）决定了路径积分的定义，不同围道对应不同的量子系统或同一系统
  的不同表示。
- 新的围道来自**伪全纯映射的边界值**，其在二维场论中的对应物是靶空间为复化相空间的
  **拓扑扭曲 A-模型**中的**余各向同性 A-膜**。
- 一维↔二维的对应在三维↔四维上重复：**三维陈–西蒙斯路径积分**的围道可由
  **四维 $\mathcal{N}=4$ 超杨–米尔斯理论**导出，由此在特定条件下两套路径积分等价。
- 应用（另文）：膜的 BPS 态与纽结的 Khovanov 同调之间的联系。

## 已发现的原文笔误 / 可疑处（均已在源码批注，正文按原文或已注明修正）

| # | 位置 | 原文 | 应为 / 说明 |
|---|---|---|---|
| 1 | Fig. 1 图注，p.4 | $\Gamma_1+\Gamma_1+\Gamma_2+\Gamma_3=0$ | $\Gamma_0+\Gamma_1+\Gamma_2+\Gamma_3=0$ |
| 2 | p.17 式 (2.37) | 右端 $\partial Y^A/\partial t$ | $\partial Y^C/\partial t$（同一指标 A 两端重复，与 (2.38)(2.39) 不符） |
| 3 | p.19 式 (2.38) | $I^A{}_B=g^{AB}\omega_{BC}$ | $I^A{}_C=g^{AB}\omega_{BC}$（右端自由指标为 A、C） |
| 4 | p.24 | “$\gamma$ 是 $Y$ 上的微分形式” | 应为 $\widehat{\mathcal M}$ 上 |
| 5 | p.24 式 (2.55)(2.56) | 第二个积分漏下标 | 应为 $\int_D$ |
| 6 | p.38 (3.25) 之后 | “So again $V$ preserves $\omega_I$” | $\omega_J$（紧接计算给出 $\omega_J^{-1}\mathrm{d}U=-V$） |
| 7 | p.43 式 (4.21) | $\exp(S(x(0))$ 缺右括号 | $\exp(S(x(0)))$ |
| 8 | p.44 式 (4.24) | 分母 $\mathrm{d}x$；$\partial h/\partial x^J$ | $\mathrm{d}s$；$\partial h/\partial x^I$ |
| 9 | p.42 (4.18) 括注 | $\Upsilon_p$ | $\Upsilon_{\mathrm{top}}$ |
| 10 | p.49 | “equation of motion **of motion** of D” | 重复 “of motion” |
| 11 | p.52 | “$V(\sigma)$ is the vector field on $M$” | on $Y$（本节流形记作 $Y$） |
| 12 | p.61 式 (5.33) | $\exp(S(x(0))$ 缺右括号 | $\exp(S(x(0)))$ |
| 13 | p.19 “famlliar”；p.17 “practice case”；p.35 “perserves”；p.37 “intepreted” | 拼写/用词 | familiar；previous case；preserves；interpreted |
| 14 | p.11、p.36 | “Eguchi–Hansen” | 通行拼法 Eguchi–Hanson |
| 15 | 文献 [6] | Geometric Landlands Program | Geometric **Langlands** Program |
| 16 | 文献 [23] | A. Karlhere | A. **Karlhede** |
| 17 | 文献 [28] | Commun. Math. **Pys.** | Commun. Math. **Phys.** |
| 18 | p.9 式 (2.10)、p.10 式 (2.19) | 分母 $3!R^2$，而 $R$ 全篇未定义 | 疑旧稿遗留记号；与 (2.9) 的球半径 $j$ 及 $\int_{S^2}f=4\pi j$ 不自洽。**存疑，未改**，见批注 |

另：p.74 条件 “$(1-t)/(1+t)\neq i$ 或 $t\neq -i$” 中两个条件其实等价，原文 “or” 应读作
“即”，已批注说明（非印刷错误）。

## 编译环境

XeLaTeX（TeX Live 2026 / 2025 均可），ctex 宏包，Windows/macOS 下自动使用系统中文字体。
本译本在 Windows + TeX Live 2026 下实测编译通过（58 页，0 error，0 overfull，0 缺字）。
