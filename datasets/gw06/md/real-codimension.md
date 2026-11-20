# real codimension 被吞成「其实余维」

- **id**：`gw06/correction/real-codimension`
- **类型**：correction
- **位置**：§3.2
- **问题**：为什么把 “real codimension” 译成「其实余维」会改变数学含义？

> 英文 “of real codimension at least two” 的 real 被译成同音的「其实」，句子仍通顺，却把实余维与复余维混为一谈。

## 位置

§3.2，s03a-quotient.tex:260（原文 ramified.tex:2206，PDF 第 39 页）

## 原文片段

```latex
此过程中必须避开的奇点在第~\ref{sec:3.6}~节中描述，其实余维（codimension）至少为二。
```

## 改为

```latex
此过程中必须避开的奇点在第~\ref{sec:3.6}~节中描述，实余维（real codimension）至少为二。
```

## 依据

英文原文为 “are of real codimension at least two”。“real” 与「其实」同音，被顺手写成了副词，读者会把整句读成「（这些奇点）其实余维至少为二」——一个语气强调，而不是一个数学限定。差别是实质的：复余维 1 的奇点，实余维恰为 2；说成复余维至少 2 就把爆破后出现的复余维 1 奇点排除在外，而 §3.3 正是讲 $\beta\neq 0$ 时爆破使奇点轨迹降到复余维 1。同节开头 keytakeaways 第 18 行本就写「实余维至少为二的奇点」，可作内部旁证。

## 说明

已按英文原文改正；本条只涉及一个限定词，不涉及公式与引用。

## 批注

### 易错预警：同音吞词是校对的盲区

「其实」在中文里是高频副词，读起来毫无破绽，所以逐句通读很难发现。判断依据只能是英文原词：凡原文出现 real / complex / proper / flat 这类限定词，先回查中文有没有对应的字，再看那个位置是不是被一个语气词占住了。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §3.2；印刷页 [35] / PDF 页 [36]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03a-quotient.tex:258-262`
- 该句位于§3.2（小节的起始印刷页为第 35 页，PDF 第 36 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
