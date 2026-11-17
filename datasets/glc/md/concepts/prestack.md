---
id: glc/concept/prestack
type: concept
track: B
---

# 预叠

> $k$ 上的预叠是一个伪函子 $y:\operatorname{Aff}_k^{\mathrm{op}}\to\operatorname{Grpd}$：每个仿射 $k$-概形给出一个群胚，每个映射给出拉回函子，并满足通常的相容性条件。

**问题**：预叠的定义中，目标范畴换成 $\operatorname{Set}$ 时得到什么？

## 定义

$k$ 上的预叠是一个伪函子 $y:\operatorname{Aff}_k^{\mathrm{op}}\to\operatorname{Grpd}$。因此，每个仿射 $k$-概形 $S$ 给出一个群胚 $y(S)$，每个映射 $f:S_1\to S_2$ 给出拉回函子 $f^*:y(S_2)\to y(S_1)$，满足通常的相容性条件。若目标范畴是 $\operatorname{Set}$，这就是通常的预层概念。

*记号*：$\operatorname{Aff}_k$：仿射 $k$-概形的范畴，$\operatorname{Aff}_k^{\mathrm{op}}$ 为其反范畴；$\operatorname{Grpd}$：群胚的范畴；伪函子：只在同构意义下保持复合的函子。

## 要点

- 取值是群胚而不是集合：$y(S)$ 的对象可以带自同构，这正是把 $\operatorname{Bun}_G$ 做成叠（而非概形或集合值函子）所需的语言。
- 每个映射 $f:S_1\to S_2$ 给出拉回函子 $f^*:y(S_2)\to y(S_1)$，方向与 $f$ 相反。
- 目标范畴换成 $\operatorname{Set}$ 时，预叠就是通常的预层。
- 预叠还不是叠：还差对某个 Grothendieck 拓扑 $\tau$ 的覆盖的下降条件（定义 2.1.2）。

## 关键公式

- $y:\operatorname{Aff}_k^{\mathrm{op}}\longrightarrow\operatorname{Grpd}$
- $f^*:y(S_2)\longrightarrow y(S_1)$

## 易错点

- 伪函子的相容性只在同构意义下成立；当成严格函子会丢掉叠论所需的相干数据。
- 预叠不必满足下降：「预叠」与「$\tau$-叠」只差下降这一条，而这一条正是定义 $\operatorname{Bun}_G$ 时不能省的部分。
- 拉回的方向是反变的：$f:S_1\to S_2$ 给的是 $f^*:y(S_2)\to y(S_1)$。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§2.1 预叠与叠，p.12（PDF p.12），`源码/chapters/ch02.tex:8-12（定义 2.1.1）`

## 核验

状态：`external-confirmed`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/prestack — 原文「A (2,1)-presheaf is a presheaf with values in Grpd … Sometimes this is also called a prestack」直接支持卡中「预叠 = 取值在 Grpd 的（伪）函子 Aff_k^op → Grpd」；同一句把取值范畴换成 Set 即支持「就是预层」。
- Stacks Project：https://stacks.math.columbia.edu/tag/02ZH — 该节把 site 上的叠定义为群胚纤维范畴并附加下降条件，与卡中预叠/叠的群胚值函子框架一致（框架性支持，非逐字）。

## 关联

- `glc/concept/tau-stack`
- `glc/concept/bun-g-artin-stack`
- `glc/concept/global-hecke-stack`
