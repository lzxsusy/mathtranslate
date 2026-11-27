# BRIEF — SY02-44 扩展 Whittaker 范畴

## 底本

- 作者：Dennis Gaitsgory
- 题名：*Notes on Geometric Langlands: The Extended Whittaker Category*
- 形态：17 页预印本（TeX/pdfTeX），首页署 Date: December 2, 2010，无 arXiv 号、无 DOI
- 来源：私传来的 PDF（`2026-11/35fa093bc80fde151749a4aecbb2d2a5.pdf`），与系列其他笔记同源
- 权利状态：作者未正式发表的笔记，著作权归作者；本工程仅作内部研读用，成品不对外发布

## 内容与定位

这是 Gaitsgory「Notes on Geometric Langlands」系列中的一册（[GL:Eis]、[GL:contr]、[GL:Ran]、[GL:funct] 之外的独立一册）。主题：

1. 用「Borel 的有理约化」的范畴化版本 $D(\mathrm{Bun}_B^{rat})$、$D(\mathrm{Bun}_T^{rat})$ 取代 $\mathrm{Bun}_B$、$\mathrm{Bun}_T$；
2. 造 Whittaker 范畴 $\mathrm{Whit}(G)_{glob}$、既约版 $\mathrm{Whit}(G)^{red}_{glob}$ 与本册主角**扩展 Whittaker 范畴** $\mathrm{Whit}(G)^{red,ext}_{glob}$；
3. 用 Eisenstein 级数函子与其常数项 $\mathrm{Eis}$、$\mathrm{CT}$，以及它们的谱侧对应 $\mathrm{Eis}^{spec}$、$\mathrm{CT}^{spec}$，把 $D(\mathrm{Bun}_G)$ 与 $\mathrm{QCoh}_N(\mathrm{LocSys}_{\check G})$ 联系起来；
4. 证明（在 $GL_n$ 情形）系数函子 $\mathsf{coeff}^{red,ext}$ 全忠实，并给出谱侧的粘合描述（Quasi-Theorem 8.2.1）。

## 为什么读

- 要理解 [GL:funct] 中 $GL_2$ 的几何朗兰兹函子 $\Psi_G$ 是怎么造出来的，本册是它的直接前身：$\Psi_G$ 的出发点是本册 §7 的系数函子与 §8 的谱描述。
- 「有理约化」这套技巧（把叠的紧化换成范畴化的等价范畴）是几何朗兰兹里绕开 $\mathrm{Bun}_B$ 不连通的标准手段。
- 半单秩 1 与 $GL_n$ 两种情形的论证结构对照清楚，适合作为读几何朗兰兹技术性论文的入门。

## 范围

全文 8 节 + 文献，无附录，全部译出。原文 3 条脚注、3 个交换图、14 处笔误（保留原文并加注），译出 23 条译注。

## 验收标准

- 结构：节号、编号段号、定理类编号（Quasi-Theorem 等）与原书一一对应；原书编号公式只有 (4.1)、(4.2)、(7.1)、(8.1) 四条，译文只给这四条编号。
- 公式：逐条与 150 dpi 页图核对（`工程文件/公式核对记录.md`），符号字体分工与原书一致（Fraktur 映射字母、粗体 $\mathbf{oblv}/\mathbf{ind}$、无衬线 $\mathsf{coeff}/\mathsf{Poinc}$）。
- 编译：xelatex 三遍，0 error、0 Overfull、0 Underfull、0 缺字、0 未定义引用。
- 译注：每条带来源标记（A 原书/作者他文/经典教材；B 白名单交叉；I 本库；无依据者标「译者按（上下文推断）」）。
- 笔误：一律保留原文读法，另加译注说明；不擅自「改正」正文。
