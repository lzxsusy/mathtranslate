# tr-b 译手报告（ch03 / ch04）

## 1. 交付物

| 文件 | 内容 | 原文范围 |
| --- | --- | --- |
| `src/chunks/ch03.tex` | §3a $A_{\infty}$-范畴与 dg 范畴；§3b $A_{\infty}$-模与完美模 | main.tex 516–810（原文 p.14 中–p.17） |
| `src/chunks/ch04.tex` | §3c 群作用与轨道范畴；§3d dg 范畴的张量积；§3 章末 keytakeaways | main.tex 811–1054（原文 p.18–p.20） |
| `work/reports/tr-b-terms.tsv` | 本两章新增术语 21 条 | — |
| `work/check/ch03_test.tex`、`ch04_test.tex` | 自检脚手架（各跑两遍 `xelatex`） | — |

未改动 `src/preamble.tex`、`main.tex`、`work/terms_zh.tsv` 及他人 chunk；未做 git 操作。

## 2. 边界说明

- ch03 从 `\section{Algebraic Preparations}` 开始，该处位于原文 p.14 中部，故文件顶部不插 p.14 注释；页注释只有 p.15、p.16、p.17 三处。
- ch04 止于 §3 末尾（`prp:twisted-tensor-equal-quotient` 的证明之后），故按约定在末尾放 §3 的 keytakeaways；`\section{Fukaya Categories of Discrete Quotients}` 及 `thm:wrapped-Fukaya-quotient` 属 ch05，不在本 chunk。
- `_src/ch03_src.tex` 第 291 行以后是注释掉的旧稿（Künneth 双模那一段，含 `% \begin{dfn}\label{dfn:Kunneth-bimodule-construction}`），不属于本 chunk 的正文，未译；因此本 chunk 的 `\label` 数比源文件 grep 结果少 1 个，属预期。

## 3. 编译自检

`work/check/` 下各跑两遍 `xelatex -interaction=nonstopmode`：

| 文件 | 页数 | `!` 错误 | Overfull | Underfull | Missing character |
| --- | --- | --- | --- | --- | --- |
| ch03_test | 4 | 0 | 0 | 0 | 0 |
| ch04_test | 4 | 0 | 0 | 0 | 0 |

剩余 LaTeX Warning 只有 `Citation ... undefined` 与 `Reference ... undefined`（孤立 chunk 无 `.bib`，其他 chunk 的 label 不在本文件），ch00 等自检同样如此，属预期；正文中显示为 `[?]`。

## 4. 译注与概念框

ch03（4 yizhu + 2 conceptbox，行号见 `ch03.tex`）
- 41 行 yizhu「原文拼写与笔误」：`recollment`→recollection、`Liebnitz`→Leibniz、dg 范畴刻画写成 $\mu^k_{\mathcal{A}}=0$（$k\geq 2$）应为 $k\geq 3$（否则连 $\mu^2$ 也被消掉，§3c 原文自己写的是 $d\geq 3$）。
- 50 行 yizhu「符号警告：$\bullet$ 与复合方向」：区分缩小 bullet 的复合算子 $\comp$ 与分次指标 $\bullet$；说明 $f\comp f'=(-1)^{-\lvert f\rvert}\mu^2(f',f)$ 的图解次序与通常 $f'\circ f$ 相反。
- 65 行 yizhu「原文笔误：$A_{\infty}$-函子的目标空间」：$\phi^d$ 值域下标应为 $\mathcal{B}$；并说明 $\bullet+1-d$ 与 $[1-d]$ 是同一移位。
- 159 行 yizhu「为什么 Yoneda 嵌入送的是 $\mathcal{A}^{op}$」：$X$ 占 Hom 第一个槽，故 $X\mapsto\hom(X,-)$ 反变；这解释「$\Perf\mathcal{A}$ 是 $\mathcal{A}^{op}$ 的幂等完备化」。
- 45 行 conceptbox「dg 范畴与 $A_{\infty}$ 范畴」（参考 nLab *dg-category*；Keller, arXiv:math/0601185）。
- 169 行 conceptbox「完美模」（参考 nLab *perfect complex*；Keller, arXiv:math/0601185）。

ch04（3 yizhu + 2 conceptbox + 1 keytakeaways）
- 10 行 yizhu「严格作用」：$g^0$、$g^1$ 即对象与态射上的映射，故每个 $g$ 其实是要求为拟等价的普通 dg 函子；高阶分量全为零；轨道范畴公式只用 $g^0,g^1$ 正依赖于此。
- 44 行 yizhu「证明中的笔误与读法」：$p_{j+l+1}$ 未定义（应为 $a_{j+l+1}$），$\mathbf{g}$ 与 $\mu^l$ 的括号略多余；并给出「展开后用 $\mathcal{A}$ 的 Maurer–Cartan 方程相消」的读法。
- 144 行 yizhu「扭张量积的符号与复合次序」：$d(f\otimes g)=df\otimes g+(-1)^{\lvert f\rvert}f\otimes dg$ 是标准 Koszul 微分；复合公式的 $(-1)^{\lvert g\rvert\lvert f'\rvert}$ 来自把 $g$ 移过 $f'$ 时的 Koszul 符号；$\Lambda=\{1\}$ 时退化。
- 48 行 conceptbox「轨道范畴」：对象一个不删，态射取 $\bigoplus_{g}\hom(g(L),K)$；与 Keller 三角轨道范畴（需要 $F$ 拟可逆/局部化）的区别；本文严格作用 + $\mathbb{Z}$ 情形无需局部化。
- 206 行 conceptbox「扭张量积」：把 $\Lambda$ 的等变信息打包进 dg 范畴，等价于 $(\mathcal{A}\otimes\mathcal{B})/\Lambda$，供后续 Künneth 型论证使用。
- 211 行 keytakeaways 4 条：语言层面（$A_{\infty}$/dg/完美模）/ 轨道范畴 / 扭张量积 / 下一节用途（$\mathcal{W}(X)/G$）。

## 5. 存疑清单（原文可疑处，均照原文保留并加译注）

1. ch03 开头 `recollment`、`Liebnitz`、$\mu^k_{\mathcal{A}}=0$（$k\geq 2$）三处笔误 —— 见 41 行译注；译文按原意处理，公式符号未改。
2. ch03 $A_{\infty}$-函子定义中 $\phi^d$ 的值域写作 $\hom_{\mathcal{A}}^{\bullet+1-d}(\phi(L_0),\phi(L_d))$，应为 $\hom_{\mathcal{B}}$ —— 见 65 行译注；公式照抄未改。
3. ch03 首句原文语法略拗口（“whose Hom are cochain complexes of $\field$-vector spaces, enriched over the $A_{\infty}$-operad”），按「以 $\field$-向量空间的上链复形为 Hom、在 $A_{\infty}$-operad 上丰富的范畴」译。
4. ch04 轨道范畴态射空间原文写作 $\hom_{\mathcal{A}}(g(L),(K))$，多一层括号 —— 照抄（见 `ch04.tex` 17 行）。
5. ch04 定义中 $a_i\in\hom_{\mathcal{A}}(L_i,g_i(L_{i+1}))$：与 $\mu^d_{\mathcal{A}/G}$ 实际使用的移位后分量（$a_i\colon(g_1\dotsb g_{i+1})(L_i)\to(g_1\dotsb g_i)(L_{i+1})$）对不上，原文记号不严谨 —— 公式照抄，未擅改下标。
6. ch04 证明中 $p_{j+l+1}$ 全文未定义（应为 $a_{j+l+1}$）；另 $\mathbf{g}$ 与 $\mu^l_{\mathcal{A}}$ 的括号配对稍多 —— 见 44 行译注；公式照抄。
7. ch04「dg 情形与 FKQ24 的 dg enhanced orbit category 一致、无需局部化」：原文只给结论与一两句理由，未展开证明，译文照此，未补证。
8. ch03 的 Yoneda 构造与 $\Mod(\mathcal{A})$ 的微分都只引用 `Seidel08` 的页码/小节，原文未列细节，译文保留 `\cite` 并照译「按……中描述的方式」。

## 6. 术语

新增 21 条见 `work/reports/tr-b-terms.tsv`。要点：

- `cohomology category` 译「上同调范畴」（记 $H^{\bullet}(\mathcal{A})$），与表内已冻结的「同伦范畴」（homotopy category）区分。
- `pretriangulated dg category` 译「预三角 dg 范畴」；`idempotent completion` 译「幂等完备化」。
- `orbit category` 用表内「轨道范畴」；`dg enhanced orbit category` 译「dg 强化轨道范畴」（FKQ24 用语）。
- `twisted tensor product` 译「扭张量积」；`strict action` 译「严格作用」；`quasi-embedding` 译「拟嵌入」。
- `enriched over` 译「在……上丰富」；`operad` 保留英文（与表内 `Fukaya 范畴` 等保留英文的惯例一致）。

## 7. 概念库勘误（请 lead 处理 `work/concepts_library.md`）

「轨道范畴与导出自等价」条目有两处问题，写 conceptbox 时未照抄该条，改按本文定义写：

1. 该条称轨道范畴「把对象取 $F$-轨道」。本文 §3c 的定义是：对象保持 $\Obj\mathcal{A}$ 不变，只把态射换成 $\bigoplus_{g\in G}\hom_{\mathcal{A}}(g(L),K)$。Keller 的三角轨道范畴虽然对象确实取轨道，但要求 $F$ 拟可逆并在必要时局部化；与本文的「严格作用 + 不取对象轨道」不是同一套约定。
2. 该条目正文在文件中重复出现，且混入了「完美模」条目的部分文字，建议合并去重。

其余参考（nLab *dg-category*、nLab *perfect complex*、Keller arXiv:math/0601185、Keller arXiv:math/0610212）均可保留。

## 8. 格式自检

- ASCII 直引号 `"` 计数为 0；引号统一用「」。
- 无「被……所」「进行……的」「对于……而言」；无「的的」。
- 汉字后无 ASCII `, : ; ? !`、无 ASCII 半角括号直接紧跟、中文与英文/行内公式之间统一留半角空格（脚本核对结果为 0 处违规）。
- 环境 `begin`/`end` 全部配对：ch03 为 dfn 6/6、yizhu 4/4、conceptbox 2/2、rmk 1/1；ch04 为 dfn 4/4、yizhu 3/3、conceptbox 2/2、keytakeaways 1/1、lmm 1/1、proof 2/2、prp 1/1、exmp 1/1。
- `\label` 与源文件正文一致（ch03 5 个、ch04 2 个，见第 2 节的边界说明）；未手写编号、未用 `\tag`；`\cite` 的可选参数原样保留。
- 译注/概念框里额外自引了 `\cite{FKQ24}`（2 处）、`\cite{Ornaghi25}`（1 处），均在参考行或说明文字内，正文引用的位置与数量未改。
