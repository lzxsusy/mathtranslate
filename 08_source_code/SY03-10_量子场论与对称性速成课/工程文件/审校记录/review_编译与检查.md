# 编译验证与静态检查报告

**工程**：《A Crash Course on QFT and Symmetry》（Si Li, 2025.7）中文译注版
**日期**：2026-10-22
**结论**：源码在本环境实际编译**通过**（非静态推测），成品 108 页，0 错误，0 overfull/underfull 警告；
14 个片段全部通过静态检查；102/102 页正文逐页覆盖。

---

## 一、编译环境与方法

| 项目 | 说明 |
|---|---|
| 编译器 | `tectonic 0.17.0`（XeTeX 引擎，TeX Live 2022 组件 bundle，离线缓存） |
| 中文方案 | `ctexart` + Fandol 字体（`ctex-fontset-fandol`） |
| 命令 | `tectonic --keep-logs --outdir build main.tex`（两遍，自动重跑以生成目录/书签） |
| 源文件 | `main.tex` + `preamble.tex` + `tex/part01.tex … part14.tex` |
| 输出 | `build/main.pdf`，108 页，约 3.63 MiB |

`main.log` 中 **没有任何 `!` 开头的错误**；最终一遍编译的 overfull/underfull box 计数为 **0**。

## 二、编译过程中发现并修复的问题（如实记录）

| # | 现象 | 原因 | 修复 |
|---|---|---|---|
| 1 | `! Illegal parameter number in definition of \reserved@a`（preamble 原稿） | `\IfFileExists` 分支内 `\newcommand{\fmsl}[1]{…#1…}` 的 `#` 未加倍 | 改为直接 `\usepackage{slashed}` + 单一定义 |
| 2 | `! Missing \begin{document}` | 宏名 `\w@envhead` 含 `@`，在 `\makeatletter` 外被拆读 | 改名 `\wenvhead` |
| 3 | `Missing character: 𝓚 / ∂ / ⃗ / ①…`（缺字） | 图题/正文里的 Unicode 数学符号未进入数学模式；带圈数字未被当作 CJK 字符 | 图题改为 `$\mathcal{K}$` 等 LaTeX 数学；unpublished Unicode 数学符号全部转为 LaTeX；用 `\xeCJKDeclareCharClass{CJK}{"2460 -> "2473}` 把 ①②③ 交给中文字体 |
| 4 | `! Undefined control sequence \fint`（22 处） | 原文"积分号加横杠"的正则化积分记号；`esint` 宏包不在离线 bundle 内 | 在 `preamble.tex` 用 `\mathchoice` + `\rule` 叠加实现 `\fint`（横杠置于积分号上部），并经样张目检 |
| 5 | `Overfull \hbox`（4 处） | 中英混排断行、两个超宽展示公式 | 设置 `\emergencystretch=2.5em`、`\tolerance=1500`；Gauss 积分公式拆分 `aligned` 两行；Moyal 结合性公式整体 `\small` |
| 6 | 图题中 `$` 丢失/重复转义 | 批量文本替换时的转义错误 | 逐条重写 6 条规定图题并复验 |
| 7 | 浮动体导致个别图源裁切不全（Wick 配对图、Feynman 图等） | 自动按"图形簇"裁切时把同一图的左右半簇当成两张图 | 建立 `工具/fig_overrides.json` 手工坐标表（50 条），重裁 87 张图并逐页目检 |

## 三、静态检查项目与结果

### 3.1 `lint.py`（语法/体例）

检查 14 个片段：花括号配平、环境 begin/end 配对、`$` 奇偶、`\left/\right` 配对、
BOM/乱码、`???`/`TODO`/`待补` 占位、`equation` 环境误用、`\tag` 误用、
`\caption` 位置、`\includegraphics` 文件存在性。

```
[ OK ] part01.tex … part14.tex
---- 0/14 files have problems ----
```

### 3.2 `coverage.py`（逐页覆盖）

按每个 PDF 页正文开头的 `% >>> pNNN` 标记核验：

```
part01 5/5   part02 8/8   part03 8/8   part04 8/8   part05 10/10
part06 7/7   part07 8/8   part08 5/5   part09 10/10  part10 6/6
part11 10/10 part12 6/6   part13 9/9   part14 3/3
---- union: expected 102 pages (p002–p103), covered 102, missing [] ----
```

### 3.3 `qc.py`（内容质量）

- 未翻译英文长句检测：仅 `part14.tex`（参考文献条目，学术惯例保留英文）被标记；
- 定理类编号重复检测：14 个片段均无重号；
- 残留标记/占位符：0。

### 3.4 结构核对

| 项目 | 原文 | 译本 | 结果 |
|---|---|---|---|
| Section | 10 | 10 | 一一对应 |
| Subsection | 38 | 38 | 一一对应 |
| 定理/定义/例/注环境 | — | 126 个 | 编号与原文一致，无重号、无跳号 |
| 展示公式编号 | 无（仅 1 处 `(*)`） | 全部 `\[ \]`，1 处 `\tag*{$*$}` | 符合原文体例 |
| 图 | 2 张编号图 + 正文示意图 | 87 张裁切图 | 全部插入对应位置 |
| 表 | 5 处 | 5 处 `booktabs` 重排 | 表头已译 |

## 四、成品抽查（编译后 PDF）

- 封面、摘要、目录（自动生成，页码与正文一致）；
- 首页示例：第 1 章作用量公式、第 3 章 Maxwell 方程组、第 5 章 Wick 定理框（`\boxed`）、
  第 6 章 Figure 2（规范固定切片）、第 9 章 Moyal 积、第 10 章 OPE 均与原文对照无误；
- 图浮动体位置：逐页目检 87 张图，均完整、无截断、图题与图对应；
- 中文与数学混排、`\fint` 记号、①②③、`\boxed`、`cases`、`aligned` 均正常显示。

## 五、复现方式

```bash
# 在 QFT_中文译注版/ 目录下
python 工具/build.py            # 生成 main.tex（自动列出 tex/part*.tex）
xelatex main.tex && xelatex main.tex
# 或使用本环境的 tectonic：
tectonic --keep-logs --outdir build main.tex
```

静态检查：

```bash
python 工具/lint.py
python 工具/coverage.py
python 工具/qc.py
```
