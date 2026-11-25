# 资料卡 05 · 卡点与 nLab 批注

本卡记录 v1.1 校订（2026-11-25）在正文中加入的 **17 条译注**，以及查证外部资料时实测到的词条可用性边界。
与 `03_translations_meta/SY02-10/工程文件/reports/03_nLab批注清单.md` 同体例，便于跨工程检索。

## 一、边界（先立规矩，再看清单）

1. **只补定义与接口**：译注只说明「这个概念在外部文献里叫什么、大致定义是什么、与本文何处衔接」，不替作者补充论证、不评价原文对错（原文笔误另立条目，见 `04-术语文献勘误.md`）。
2. **不与作者注混排**：译注统一用 `\zy`（`manyfoot` 独立序列，印作「译1、译2…」），作者脚注保原编号；两者在版面上分属不同序列，读者可一眼区分。
3. **来源分级照 `04_playbook/01_数学文献翻译纪律.md` §2.5**：A 级可作硬依据；B 级（nLab / Stacks / ProofWiki）须标「词条名 + 永久链接 + last revised 日期」，单独 B 级标「待核」；I 级只作一致性依据；知乎、百度百科、CSDN、简书、公众号、博客一律不引。**每条解释性译注末尾都带 `[来源：…]` 或 `[译者按`**。
4. **空壳 / 重定向 / 无词条不得冒充词条**：实测为空的词条（见第三节）只记「其现状如此」，不据此立论。

## 二、译注清单（17 条，按正文出现次序）

| 译注 | 节 | 概念 | 批注要点 | 来源（词条 / last revised） |
| --- | --- | --- | --- | --- |
| 译1 | §0.1 | Satake 同构 | 原文所谓「Satake 同构的重新解释」，在 §5.6 中落实为几何 Satake 等价在函子层面的对应；补来源标记 | nLab `geometric Satake equivalence`，2024-07-22（A 级：原文 §5.6） |
| 译2 | §0.3.2 | 归纳概形 | 区分「严格归纳概形」与概形范畴的一般 ind-对象：nLab 版不要求过渡映射为闭浸入，且形式概形只对应其中一部分对象 | nLab `ind-scheme`，2023-11-11 |
| 译3 | §1.1 | 仿射 Grassmann 簇 | nLab 该词条的定义逐条标注「Definition 1.1.1 / 1.1.2 of [Zhu2016]」，一般 $G$ 情形标注「Section 1.2」——本文已成本主题的标准入口 | nLab `affine Grassmannian`，2023-08-15 |
| 译4 | §1.3 | 射流群 / 环路群 | 本文 $L,L^+$ 是函子式的（群）归纳概形；nLab 的 loop group 讲拓扑环路群并记 $\mathcal LG\simeq G\times\Omega G$，两套对象到 §1.6 才接上 | nLab `loop group`，2026-03-21 |
| 译5 | §1.3 例 | 原文 π₀ 笔误 | 原文作 $\pi_0(G)$，但 $G=\bG_m$ 时 $\pi_0(G)=1$，同句前文又说 $\pi_0(\Gr_G)\cong\bZ$；按文意译作 $\pi_0(\Gr_G)$，疑点已登记（D1） | A 级：原文自身；`work/疑点清单.tsv` |
| 译6 | §1.4 | Beauville–Laszlo 下降 | 下降定理即下文 `thm:descent lemma`，把 $D$ 上与 $D^*$ 上的数据粘成曲线上的丛，是 `thm:glob aff` 的技术核心；nLab 无对应词条，只据原文所引 | A 级：`\cite{BL2}` |
| 译7 | §1.5 | 行列式线丛 | 后文用 Tate 空间与格给出 $\mL_{\det}$ 的典范构造；$\GL_n$ 情形对应相对行列式，其 $L^+G$-等变性正是 §2.5 中心扩张的来源，并用于 §3.4 | A 级：原文 §1.5 / §2.5 / §3.4 |
| 译8 | §1.6 | 拓扑环路群 | 与拓扑环路群正式接上：nLab 记 $\mathcal LG\simeq G\times\Omega G$；本文得到更强的 $\Gr\cong\Omega K$ | nLab `loop group`，2026-03-21；A 级 `\cite[\S 8.3]{PS}` |
| 译9 | §2.5 | 中心扩张 | nLab `central extension` 目前只有导引性内容，**不作定义依据**；改依 Kac 教材：$\widehat{L\frakg}=\frakg(F)\oplus k\mathbf 1$ 的括号由留数给出，与 $\widehat{LG}$ 在无穷小层面对应 | A 级 `\cite[Chap. 4, §7]{Kac}`；nLab 词条现状 2025-02-16 |
| 译10 | §3.1 | BD Grassmann 簇 | $\Gr_{\underline G,X^I}$ 是「把抛物结构放在 $I$ 个点上」的族，§3.3 用 Ran 空间把它们按点集之并粘成 $\Gr_{\Ran}$ | nLab `Ran space`，2020-07-27；`factorization algebra`，2026-08-16 |
| 译11 | §3.3 | Ran 空间 | nLab 的定义正是 $\mathrm{Ran}_X:=\varinjlim_I X^I$（$I$ 非空有限集、态射为满射），与本文一致；得名于 Ziv Ran，系统使用见 Beilinson–Drinfeld《Chiral algebras》 | nLab `Ran space`，2020-07-27；A 级 `\cite{BD}` |
| 译12 | §4.1 | 单点单值化 | 即 Weil 单值化的双商 $\Bun_{\underline G}\simeq[\underline G^{X^*}\backslash\Gr_{\underline G,x}]$；函数域情形与数域侧 $G(F)\backslash G(\mathbb A)/G(\mO)$ 并列 | nLab `Weil uniformization theorem`，2023-04-04；A 级 `\cite{BL}`、`\cite{He}` |
| 译13 | §5.1 | 反常层与 IC 层 | 「反常层」之名有误导（nLab 开篇即说「既非 perverse 也非 sheaf」）；$\on P(X)$ 是 $D^b_c(X)$ 的全 Abel 子范畴；$\IC_\mu$ 与相交上同调的关系 | nLab `perverse sheaf`，2026-10-16；`intersection cohomology`，2023-05-07 |
| 译14 | §5.2 | Tannaka 范畴 | 用「纤维函子」形式：由张量函子 $F$ 的张量自同构群重建群概形；本文把它用于 $\mC=\Sat_G$ | nLab `Tannaka duality`，2025-07-28 |
| 译15 | §5.3 | Langlands 对偶群 | nLab 该词条**只列参考文献、未给定义**，不引为定义依据；改依原文所引综述 | A 级 `\cite{Sp}`；nLab 词条现状 2014-09-07 |
| 译16 | §5.4 | 融合积 | 「交换约束是附加数据，而非幺半结构的性质」——nLab 对几何 Satake 等价的这条警告，正是本文引入融合积的动机 | nLab `geometric Satake equivalence`，2024-07-22；原文 §5.4 |
| 译17 | 附录 A.1 | 等变反常层 | 附录只在「六函子」层面使用等变导出范畴；其一般框架的入口 | nLab `six operations`，2026-09-30 |

> 记法约定：表中 `nLab` 条目的永久链接统一为 `https://ncatlab.org/nlab/show/<词条 slug>`（如 `https://ncatlab.org/nlab/show/affine+Grassmannian`），正文译注里已逐条写出，便于读者点击核对。

## 三、词条可用性实测（2026-11-25）

查证时逐页读过原页，不是按关键词猜的。结果分四类：

| 词条 | 实测情况 | 处理 |
| --- | --- | --- |
| `central extension` | 2025-02-16 修订，正文仅 `[[!include higher algebra - contents]]` 导引行，**无定义** | 不作定义依据；译9 记其现状，立论用 A 级 Kac |
| `convolution product` | 2022 前后仅导引行，无定义 | 未引（本文卷积积有自足定义） |
| `Kac-Moody algebra` | 仅导引行 | 未引；用 A 级 Kac 教材 |
| `Langlands dual group` | 2014-09-07 修订，只有 3 条 References，无定义 | 不作定义依据；译15 记其现状，立论用 A 级 `\cite{Sp}` |
| `fusion product` | **nLab 无此词条**（HTTP 404） | 不编造链接；译16 改引 `geometric Satake equivalence` 的交换约束警告 |
| `Ran space` | 页面存在（2020-07-27），但**不在本库 `07_refs_nlab/pages/`** | 正文用永久链接 + 日期；卡片第三节留档，便于后续入库 |
| `descent` | 2024-09-12，∞-范畴 split hypercover 口径 | 与 §0.3 的初等 fpqc 等化子条件不匹配，未引 |
| Stacks Project `Tag 022Y` | 实测为 §39.10 *Actions of group schemes*，**不是** fpqc 相关 | 未引；本文中出现的 Stacks 标签（`Tag01ZC`、`Tag00MB`、`Tag00MH`、`Tag0244/0246`、`Tag01WQ`、`Tag056P`、`Tag00ME`）**全部是原文自带的引用**，属 A 级，不另行核实、也不改写 |

**教训**：nLab 有页面 ≠ 有定义。`central extension`、`convolution product`、`Kac-Moody algebra`、`Langlands dual group` 四条都是「页面在、定义不在」，若按关键词命中就引用，等于给读者一个点不开内容的链接。

## 四、复现

```bash
cd 工程文件/scripts
python insert_notes.py      # 15 条新译注（行尾片段 guard，失败即整体不写）
cd ../../源码 && xelatex -interaction=nonstopmode main.tex   # 两遍
grep -c '^!' main.log ; grep -c Overfull main.log ; grep -c 'Missing character' main.log
```

译注总数核对：`grep -o '\\zy{' 源码/chunks/*.tex | wc -l` → **17**（译1–译17，序列连续、无跳号）。

## 五、遗留

- `Ran space`、`central extension`、`Langlands dual group` 三条若日后 nLab 扩写或本库入库，可回填 `07_refs_nlab/pages/`，并在此卡把「现状」一栏改掉。
- 译注只做「定义给链接」，未做「与原文论证的对照评注」；若读者需要后一类，应另立 `06-论证评注.md`，不要塞进脚注（会破坏「不与作者注混排」）。
