---
id: glc/concept/euler-characteristic-trace-test
type: concept
track: E
---

# 茎的 Euler 示性数判据

> 对构造出的不可约 IC 延拓，茎的 Euler 示性数 $\chi_{\mathcal K}$ 恒定且非零就足以排除边界贡献，迫使其为移位的局部系统；于是下降所需的两个条件化为两条 $\chi$ 的计算。

**问题**：为什么只需检查茎 Euler 示性数『在纤维上恒定且不为零』，就能断定不可约反常层其实是局部系统？

## 定义

设 $Y$ 光滑，$\mathcal K\in\operatorname{Perv}(Y)$ 不可约。记 $\chi_{\mathcal K}(y):=\sum_i(-1)^i\dim H^i(\mathcal K_{\bar y})$ 为茎的 Euler 示性数。对任意反常层，这个函数本身并不是局部系统判据；但这里的 $\mathcal K$ 是由该构造得到的不可约 IC 延拓，在这一情形，$\chi_{\mathcal K}$ 恒定且非零排除了边界贡献，从而迫使 $\mathcal K$ 是 $Y$ 上移位的局部系统。因此，只需证明 $\chi(\operatorname{Aut}'_E)$ 在 $\operatorname{Bun}'_n\to\operatorname{Bun}_n$ 的纤维上恒定，且 $\chi(\operatorname{Aut}'_E)\neq0$ 在 $C_n^\circ$ 上。

*记号*：$\mathcal K_{\bar y}$ 是 $\mathcal K$ 在几何点 $\bar y$ 处的茎（复形）；$H^i$ 是茎的上同调；$\chi_{\mathcal K}(y)$ 是整数（可为负）；『移位』指 $\mathcal K$ 是某个局部系统平移若干度。

## 要点

- 判据不是对任意反常层成立的：讲义明确说『对任意反常层，这个函数本身并不是局部系统判据』。
- 成立的场景是『由该构造得到的不可约 IC 延拓』——即 $\mathcal K$ 在某个稠密开部分上是平移过的局部系统，且不可约。
- 两个条件缺一不可：恒定负责去掉沿纤维的变化，非零负责排除整个纤维上为零（零层的 $\chi$ 也恒定）。
- 判据把『层是否下降』这一几何问题换成『$\chi$ 是否恒定且非零』这一可直接用迹函数计算的问题。
- ‘恒定’那一半在 §8.3 由 Deligne 真推前不变性 + FGKV 比较定理给出。

## 关键公式

- $\chi_{\mathcal K}(y):=\sum_i(-1)^i\dim H^i(\mathcal K_{\bar y})$
- $\chi(\operatorname{Aut}'_E)\ \text{在}\ \operatorname{Bun}'_n\to\operatorname{Bun}_n\ \text{的纤维上恒定}$
- $\chi(\operatorname{Aut}'_E)\neq0\quad\text{在}\ C_n^\circ\ \text{上}$

## 定理与证明

### Euler 示性数判据（纯 IC 情形）（要点（有缺口））

设 $\mathcal K\in\operatorname{Perv}(Y)$ 是不可约 IC 延拓（由本构造得到）。若茎的 Euler 示性数 $\chi_{\mathcal K}$ 在 $Y$ 的每个连通分支上恒定且处处非零，则 $\mathcal K$ 是 $Y$ 上移位过的局部系统。

1. $\mathcal K$ 不可约且是 IC 延拓，故存在稠密开 $U\subset Y$ 使 $\mathcal K|_U$ 是移位局部系统，$\mathcal K$ 是它从 $U$ 到 $Y$ 的中间延拓。  
   *为什么*：IC 延拓的定义就是『在稠密开部分取局部系统、再作中间延拓』。
2. 边界点处的茎由 $\mathcal K|_U$ 的局部系统部分加上边界贡献构成；$\chi_{\mathcal K}$ 恒定说明边界贡献（按维数交替求和后）为零。  
   *为什么*：$\chi$ 是加性的：$\chi_{\text{整体}}=\chi_{\text{局部系统部分}}+\chi_{\text{边界}}$，恒定意味着 $\chi_{\text{边界}}$ 不随点变化。
3. 非零性进一步排除边界贡献把整层吃掉的可能，于是 $\mathcal K$ 在每一点都等于其局部系统部分，即为移位局部系统。  
   *为什么*：这是讲义给出的论证要点：恒定 + 非零排除边界贡献，从而 $U=Y$。

> 缺口：讲义在原位只给出这一句论证要点（『恒定且非零排除了边界贡献』），未写细节；且判据依赖 $\mathcal K$ 为『由该构造得到的不可约 IC 延拓』这一具体性，对一般反常层不成立（讲义明言）。

*出处*：§8.2 末–§8.3 首 / 原书 p.45


## 易错点

- 把判据当成对任意反常层成立：讲义特意强调『对任意反常层，这个函数本身并不是局部系统判据』。
- 只验证恒定而忘了非零：零层（或整个纤维上为零的层）的 $\chi$ 也恒定。
- $\chi_{\mathcal K}$ 用的是茎（$\mathcal K_{\bar y}$）的上同调维数，不是整层 $\mathrm{R}\Gamma(Y,\mathcal K)$ 的。
- 不可约性不可省：可约的反常层可以 $\chi$ 恒定而不是局部系统（直和项相消）。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§8.2 沿射影丛纤维下降（末）/ §8.3 沿纤维的迹恒定性（首），p.45（PDF p.45），`源码/chapters/ch08.tex:33-36（$\chi_{\mathcal K}$ 的定义与判据）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/perverse+sheaf — 页面给出反常层的构造性定义（存在分层使 $H^k(i^*F)$ 为有限秩局部系统，$k=\dim_{\mathbb C}(S)$），并指出反常层「generalize intersection cohomology」。支持卡里 $Y$ 光滑、$\mathcal K\in\operatorname{Perv}(Y)$ 不可约 IC 延拓、「边界上可能偏离局部系统」的语境；页面没有 $\chi_{\mathcal K}(y)=\sum_i(-1)^i\dim H^i(\mathcal K_{\bar y})$ 的定义，也没有「$\chi$ 恒定且非零 $\Rightarrow$ 移位局部系统」判据。
- nLab：https://ncatlab.org/nlab/show/six+operations — 页面只给六函子公理、$f_!\to f_*$（proper 时等价）与 Beck–Chevalley 基变换，不涉及 Euler 示性数函数 $\chi_{\mathcal K}$ 及其局部系统判据。

## 关联

- `glc/concept/descent-projective-bundle`
- `glc/concept/deligne-trace-constancy`
- `glc/concept/aut-e-whittaker-laumon`
