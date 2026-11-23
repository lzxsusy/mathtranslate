# BRIEF · SY02-28《p 进局部系统的刚性与 Riemann–Hilbert 对应》

## 原文

| 项 | 内容 |
| --- | --- |
| 原题 | Rigidity and a Riemann–Hilbert correspondence for p-adic local systems |
| 作者 | Ruochan Liu（刘若川，北京大学）、Xinwen Zhu（朱歆文，Caltech） |
| 性质 | 研究论文；*Inventiones mathematicae* 209 (2017), 291–333 |
| 底本 | arXiv:1602.06282v3（2016-07-20），35 页 |
| 版本 | v3；源文件 `工程文件/work/原文/Z4_Zhu_Rigidity_Riemann_Hilbert_p_adic_local_systems.pdf`（待归档） |
| 结构 | §1 引言（p.1–6）；§2 p 进 Simpson 对应（p.6–20，2.1–2.4）；§3 p 进 Riemann–Hilbert 对应（p.20–29，3.1 几何、3.2 算术）；§4 应用（p.29–34，4.1 刚性、4.2 志村簇）；参考文献（p.34–35） |

**原文性质。** 定义、定理、证明与构造齐备的研究论文，不是综述。全文围绕一条主链：用 pro-étale 周期层构造 $p$ 进 Riemann–Hilbert 对应，再由它推出「$p$ 进局部系统的 de Rham 性在几何族中是局部性质」这一刚性定理。第 2 节是技术主体（$p$ 进 Simpson 对应），第 3 节是主构造，第 4 节是应用。

## 一句话主旨

证明 $p$ 进平展局部系统的 de Rham 性是「几何局部」的：只要一个点处 de Rham，则处处 de Rham 且 Hodge–Tate 权相同；工具是把 Scholze 的 pro-étale 周期层搬到 $p$ 进局部系统上，造出几何与算术两个 Riemann–Hilbert 对应。

## 五步逻辑链

1. **陈述刚性**（定理 1.3）：$k$ 上几何连通刚性解析簇上的 $\Qp$ 局部系统，一点处 de Rham ⇒ 所有经典点处 de Rham，且 Hodge–Tate 权（计重数）相同。
2. **造几何 RH**（定理 1.4）：在 $\Xk$ 上以 $\OX\widehat{\otimes}\BdR$ 替代 $\OX$，用 pro-étale 周期层定义 $\mathrm{RH}(L)=R\nu'_*(\widehat L\widehat{\otimes}_{\Qp}\mathcal O_{B_{\dR}})$，得到带 Galois 半线性作用、滤过与 Griffiths 横截可积联络的向量丛。
3. **降为 Simpson 对应**（定理 1.6）：取零次分次片 $\mathcal O_C=\gr^0\mathcal O_{B_{\dR}}$，得幂零 Higgs 丛 $H(L)$；这是 $p$ 进 Simpson 对应的一个特例。
4. **算术 RH**（定理 1.5）：令 $D^i_{\dR}(L)=H^i(\Gal(\bar k/k),\phi_*\mathrm{RH}(L))$；连通且一点 de Rham 时 $D^0_{\dR}(L)$ 带滤过与可积联络，$L$ 因而是 de Rham 局部系统。
5. **应用**：把定理 1.3 用于数域上的几何连通代数簇，得定理 1.1；用于志村簇的特殊点，得定理 1.2（$L_{V,p}$ 的每个茎在 Fontaine–Mazur 意义下几何）。

## 分块表

| 块 | 节 | 原文页 | 译本页 | 目标文件 | 状态 |
| --- | --- | --- | --- | --- | --- |
| ch00 | 摘要 + §1 引言 | 1–6 | 1–9 | `源码/chunks/ch00.tex` | **完成（v0.1）** |
| ch01 | §2.1 定理陈述 | 6–9 | — | `源码/chunks/ch01.tex` | 待译 |
| ch02 | §2.2 预备 | 9–10 | — | `源码/chunks/ch02.tex` | 待译 |
| ch03 | §2.3 定理 2.1 的证明 | 10–17 | — | `源码/chunks/ch03.tex` | 待译（篇幅大，开工时按页二分） |
| ch04 | §2.4 命题 2.8 的证明 | 17–20 | — | `源码/chunks/ch04.tex` | 待译 |
| ch05 | §3.1 几何 RH | 20–24 | — | `源码/chunks/ch05.tex` | 待译 |
| ch06 | §3.2 算术 RH | 24–29 | — | `源码/chunks/ch06.tex` | 待译 |
| ch07 | §4.1–§4.2 应用 | 29–34 | — | `源码/chunks/ch07.tex` | 待译 |
| ch08 | 参考文献 | 34–35 | — | `源码/refs.tex` | 部分（引言引用的 16 条） |

## 施工流程（每块）

1. 用 pymupdf 抽原文该页段，逐句核符号与编号；2. 译成中文，定理/注/公式一律用 `\ref`/`\eqref`，label 沿用原文编号；3. `cd 源码 && xelatex -interaction=nonstopmode main.tex` 连跑三遍；4. 过滤 `^!`、`Overfull`、`Missing character`；5. 用 `latex_look` 渲染该块首页与含公式页目视核对；6. 在本文件更新分块表状态，并在 `资料卡/00-速览.md` 记该块要点。

## 纪律与已知坑

- **编号体制**：原文定理与注**各自**按节编号（定理 1.1–1.6、注 1.1–1.10 并行），公式按节编号（如 (2.1)）。preamble 已设 `\newtheorem{thm}{定理}[section]` 与 `\newtheorem{rmk}{注}[section]`，新增环境必须照此办理，不能共用一个计数器。
- **无编号猜想**：原文 §1 的 Conjecture 不编号，译文用 `conj*`；不要改成 `conj`，否则会与定理/注的编号错位。
- **符号**：$\Xk$ 是 $X$ 到 $\khb$ 的基变换；$\mathcal X$ 是环化空间 $(\Xk,\OX\widehat{\otimes}\BdR)$，不是底簇；$\bar L_x$ 是几何点 $\bar x$ 处的茎。三者不可混。
- **$\widehat{\otimes}$**：$\OX\widehat{\otimes}\BdR$ 的「$\widehat{\ }$」是完备张量积，不能写成普通 $\otimes$；`\OXB` 宏已封装。
- **引用**：`\cite{Sch2}` 等键沿用原文缩写；参考文献条目保留英文，不译书名。新增引用时同步补 `refs.tex`，否则出现 `[?]`。
- **未来节引用**：ch00 中对 §2–§4 的引用暂用字面编号（定理 3.8、§3.1 等），译到对应节后改回 `\ref`，并在 `work/label_check.txt` 记一次对账。
- **本机**：控制台 GBK，Python 读写文件统一 `encoding='utf-8'`；`xelatex` 在 MiKTeX 下用 `fontset=fandol` 可编译，`stmry` 粗体缺字形只是字体警告，不影响成品。

## 进度

- 2026-11-23：建档；ch00（摘要＋§1 全节＋记号约定＋致谢）译完，xelatex 三遍无 error，10 页；参考文献先收引言引用的 16 条。下一步：ch01 §2.1。
