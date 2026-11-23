# nLab 与 Stacks Project 检索记录（B 级来源）

> 依 `04_playbook/01_数学文献翻译纪律.md` §2.5：nLab、Stacks Project 属 B 级白名单，
> 只能作旁证，须与 A 级（底本原文）交叉，正文不缓存其文本，只留链接与 ≤200 字短引。
> 本文件记录本工程实际查过的条目、查到什么、以及没有查到什么。

## 1. nLab: Ran space

- 链接：<https://ncatlab.org/nlab/show/Ran+space>
- 短引：「the space of all nonempty finite subsets of X, equipped with geometric structure
  that knows about several coincident points merging to a single point」。
- 用处：底本定义 3.1.1.1 取**带单位**（含空集）版本，并在注 3.1.1.2 自陈与他处约定不同。
  nLab 的非空版本正说明「约定分歧是文献常态」，佐证该注并非作者自造的托辞。
- 已用于：`源码/sections/s03-1-1-basics.tex` 注 3.1.1.2 后的译注（B 级）。

## 2. nLab: factorization algebra

- 链接：<https://ncatlab.org/nlab/show/factorization+algebra>
- 短引：「a factorization algebra is an algebra over an operad where the operad in question
  is like the little disk operad, but with each disk embedded into a given manifold X」。
- 用处：该词条讲的是 Costello–Gwilliam 意义下量子场论的**分解代数**，与底本的
  **因子化范畴**（Ran 上的范畴层）不是同一概念。译名因此冻结为「因子化范畴」，
  并在第 1 章首次出现处加注区分。
- 已用于：`源码/sections/s01-intro.tex` 第 1 章「因子化」首次出现处的译注（B 级）。

## 3. Stacks Project: pseudo-coherent

- 链接：<https://stacks.math.columbia.edu/tag/064Q>（定义 15.66.1）
- 短引：「An object K• of D(R) is pseudo-coherent if it is quasi-isomorphic to a bounded
  above complex of finite free R-modules」。
- 用处：底本第 101 页讨论 `B_classical` 时用「伪紧对象 = 紧对象」，此处「伪紧」即
  pseudo-coherent；Stacks 的定义只能给出该词的经典含义（环上的有界上复形），
  **不能**直接支撑「伪紧 = 紧」这一步（那是 DG 范畴内的断言，依赖 [DT25]/[Bez16]）。
  故该处仍按「照译 + 待核」处理，疑点清单未关。
- 结论：Stacks Project 对本篇可提供的旁证有限（不覆盖 D-模、因子化范畴、ind-几何），
  只有 pseudo-coherent、perfect complex 这类基础条目可用。

## 4. 没有查到的

- nLab 无「factorization category」（只有 factorization algebra / Ran space / chiral algebra）。
- nLab 无「ind-coherent sheaf」的独立条目（相关材料散在 IndCoh 论文与 Gaitsgory 的
  「Ind-coherent sheaves」词条引用中），故未引。
- Stacks Project 不覆盖 D-模、Iwahori 子群、oper，这三类只靠 A 级（底本 + 其引文）。
