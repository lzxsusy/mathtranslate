# 译文施工规范 · SY02-18（给翻译协作者）

底本：`C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-18_shtuka及其模空间导论\工程文件\work\原文\main.tex`
（Zhiwei Yun, *Introduction to Shtukas and their moduli*, arXiv:2411.10248，38 页，amsart）

## 一、你只做一件事

把分配给你的原文行段（见任务说明）逐句译成**中文 LaTeX**，写进指定的 `源码/chunks/chNN.tex`。**不要**修改 `main.tex`、`preamble.tex`、`preamble_macros.tex`，也不要动别的块。

## 二、必须保留的结构

1. **节标题**：原文 `\section{...}\label{...}`、`\subsection{...}\label{...}`、`\sss{...}`（原文把 `\subsubsection` 重定义为小标题 `\sss`）一律保留。译 `\section`/`\subsection` 的标题文字，label 原样保留（英文，不改）。`\sss{...}` 译成一个不带编号的小标题：写成
   `\medskip\noindent\textbf{中文标题}` 并保留原文该处若有的 `\label`。
2. **定理类环境**：原文 `\begin{theorem}...\end{theorem}` → `\begin{thm}...\end{thm}`；`lemma→lem`、`prop→prop`、`cor→cor`、`conj→conj`、`fact→fact`、`ansatz→ansatz`、`defn→dfn`、`cons→cons`、`remark→rmk`、`exam→exam`、`ques→ques`。**环境名必须换**（preamble 里是这些名字），**不要手写编号**（编号由 LaTeX 生成）。
3. **公式**：`\begin{equation}`、`\begin{align}`、`\begin{equation*}`、`\[ ... \]` 原样保留；`\label`/`\eqref`/`\ref` 原样保留（key 不改）。
4. **文献**：`\cite{...}` 原样保留，不译 key。
5. **希腊字母/记号宏**：原文用 `\cE \cO \cV \cF \cZ \fm \bK \bI \bP \Sig \NN \ZZ \QQ \FF \GG \GL \SL \Sp \Val \val \ot \isom \d \fl \KR` 等，全部由 `工程文件/work/原文/main.tex` 的宏定义提供，**照抄即可，不要改成 `\mathcal{E}` 之类**（少数如 `\sss`、`\hotimes`、`\ov` 也在同一处定义；`\sss` 除外，见上）。
6. 数学模式里的中文必须包 `\text{...}`。英文术语首现可用 `（英文）` 括注。

## 三、语言纪律

- 数学工作者的中文；一句不超过 60–70 汉字，长句拆开。
- 中文全角标点；英文术语、数字两侧各留一个半角空格。
- 消灭「被……所」「进行……的」「对于……而言」「使得……得以」「以及」堆叠。
- 允许拆句、调序，**禁止增删信息**，禁止加自己的解释。译注最多 2 条，格式 `\zy{……}`，只写：易错预警／含糊点明／背景直觉，并给出依据（例如「[依据：原文 §2 定义 2.3.1]」）。
- 人名、论文名、机构名保留原文；定理类名称「定理／命题／引理／推论／定义／注／例」由环境自动给出，正文里引用时写「定理 \ref{...}」这种形式（沿用原文 `\ref`）。

## 四、术语表（冻结，必须遵守）

| 英文 | 中文 |
| --- | --- |
| shtuka / $G$-shtuka | shtuka／$G$-shtuka（**不译**） |
| $G$-torsor | $G$-主丛 |
| level structure | 水平结构 |
| level group | 水平群 |
| parahoric subgroup | 抛孔子群 |
| Iwahori subgroup | Iwahori 子群 |
| formal arc group / formal loop group | 形式弧群／形式环路群 |
| principal congruence subgroup | 主同余子群 |
| Hecke stack | Hecke 叠 |
| Hecke correspondence | Hecke 对应 |
| modification | 修正 |
| bounded | 有界的 |
| partial Frobenius | 部分 Frobenius |
| excursion operator | 游走算子 |
| Drinfeld module | Drinfeld 模 |
| Deligne–Lusztig variety | Deligne–Lusztig 簇 |
| affine Deligne–Lusztig variety | 仿射 Deligne–Lusztig 簇 |
| motive | 动机 |
| $L$-function | $L$-函数 |
| automorphic form / representation | 自守形式／自守表示 |
| moduli stack | 模叠 |
| compactification | 紧化 |
| special cycle | 特殊圈 |
| intersection number | 相交数 |
| virtual fundamental class | 虚拟基本类 |
| nearby/vanishing cycles | 邻近圈／消没圈 |
| perverse sheaf | 反常层 |
| Weil restriction | Weil 限制 |
| Newton stratum | Newton 分层 |
| Harder–Narasimhan | Harder–Narasimhan（不译） |
| generic fiber | 通用纤维 |
| smooth / proper / finite type | 光滑／proper／有限型 |
| derived algebraic geometry | 导出代数几何 |
| global function field | 整体函数域 |
| local function field | 局部函数域 |

已在本库冻结的译法（必须沿用）：「反常层」（perverse sheaf）、「几何 Satake 等价」、「Langlands 对偶群」、「抛孔」、「单值化」。

## 五、输出

- 文件开头加注释行标明块名与原文行段，例如
  `% ch02  §2.4 Iso-Shtukas / §3.1–§3.3 / §4.1–§4.2（原文 963–1295 行）`
- 只输出 LaTeX 正文，不加 markdown 代码围栏，不写「以下是译文」之类的话。
- 写完请报告：写入了哪个文件、覆盖的原文行段、遇到的原文疑点（笔误/记号不一致）各一句。
