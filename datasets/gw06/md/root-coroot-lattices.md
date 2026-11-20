# 根格、余根格、权格与余权格

- **id**：`gw06/concept/root-coroot-lattices`
- **类型**：concept
- **位置**：附录A
- **问题**：根格与余根格、权格与余权格之间是什么关系，为什么取对偶时这两对格要互换？

> 四个格由根系与其对偶生成，包含关系 Λ_rt⊂Λ_wt、Λ_cort⊂Λ_cowt 指数有限；取对偶时两对格整体互换。

## 定义

设 $\Phi$ 为 $G$ 的根系，$\Lambda_\rt=\mathbb{Z}\Phi$ 为根格；余根 $\mu^\vee=2\mu/(\mu,\mu)$ 生成余根格 $\Lambda_\cort=\mathbb{Z}\Phi^\vee$（式 (A.3)）。权格与余权格取对偶格：$\Lambda_\wt=(\Lambda_\cort)^*$、$\Lambda_\cowt=(\Lambda_\rt)^*$，即 $\nu\in\Lambda_\cowt$ 当且仅当 $\nu(\mu)=(\nu,\mu)\in\mathbb{Z}$ 对一切根 $\mu$ 成立。于是得到同秩、有限指数的包含 $\Lambda_\rt\subset\Lambda_\wt$ 与 $\Lambda_\cort\subset\Lambda_\cowt$（式 (A.5)）。特征格 $\Lambda_\char$ 可在 $\Lambda_\rt$ 与 $\Lambda_\wt$ 之间任取（式 (A.6)），其在 $\eurme^\vee$ 中的对偶 $\Lambda_\cochar$ 落在 $\Lambda_\cort$ 与 $\Lambda_\cowt$ 之间（式 (A.7)）。物理上，$\Lambda_\wt$ 标号 Wilson 线（电），$\Lambda_\cowt$ 标号 't Hooft 线（磁），而 $\Lambda_\rt$ 是“哪些权真正来自 $G$ 的表示”的整性底线；取对偶群时这两对格整体互换，$B_n$ 与 $C_n$ 的差别正在于此。对偶之后包含关系在两个方向上同时反向，$\Lambda_\char$ 的位置也移到对偶侧，于是权格与余权格的角色互换。

**记号**：$\Lambda_\rt$：根格；$\Lambda_\cort$：余根格；$\Lambda_\wt$：权格；$\Lambda_\cowt$：余权格；$\Lambda_\char$：特征格；$\Lambda_\cochar$：余特征格；$(\Lambda)^*$：对偶格，指 $\mathrm{Hom}(\Lambda,\mathbb{Z})$。

## 关键点

- $\Lambda_\wt$ 与 $\Lambda_\cowt$ 是互为对偶的一对：$\Lambda_\wt=(\Lambda_\cort)^*$、$\Lambda_\cowt=(\Lambda_\rt)^*$，故取对偶时 $(\Lambda_\rt,\Lambda_\wt)$ 与 $(\Lambda_\cort,\Lambda_\cowt)$ 互换。
- 式 (A.5) 的两个包含同秩且指数有限；对 $\Lambda_\char=\Lambda_\wt$ 有 $\Lambda_\wt/\Lambda_\rt=\mathcal{Z}(G)^\vee$（式 (A.10)），指数就是中心的大小。
- 特征格 $\Lambda_\char$ 可取 $\Lambda_\rt$ 与 $\Lambda_\wt$ 之间任一格（式 (A.6)）；$\Lambda_\char=\Lambda_\wt$ 对应单连通 $G$，$\Lambda_\char=\Lambda_\rt$ 对应伴随型。
- 格的商给出拓扑不变量：$\pi_1(G)=\Lambda_\cochar/\Lambda_\cort$（式 (A.13)）、$\mathcal{Z}(G)=\Lambda_\cowt/\Lambda_\cochar$（式 (A.11)）。
- 对偶把四格整体翻转：$\Lambda_\rt({}^LG)=\Lambda_\cort(G)$、$\Lambda_\wt({}^LG)=\Lambda_\cowt(G)$，故单连系（$A$、$D$、$E$ 型）自对偶，$B_n$ 与 $C_n$ 互换（李代数层面）。

## 公式

```latex
\mu^\vee={2\mu\over (\mu,\mu)}
```
```latex
\Lambda_\rt\subset \Lambda_\char\subset\Lambda_\wt
```
```latex
\Lambda_\cort\subset \Lambda_\cochar\subset\Lambda_\cowt
```
```latex
\pi_1(G)=\Lambda_\cochar/\Lambda_\cort
```

## 常见错误

- 把 $\Lambda_\rt$ 与 $\Lambda_\cort$ 当成同一个格：非单根系中长根满足 $\mu^\vee=\mu/n_{\mathfrak g}$（式 (A.17)），两格只差有限指数；混同会把 $B_n$ 的对偶写成 $B_n$ 而不是 $C_n$。
- 把包含方向写反（$\Lambda_\wt\subset\Lambda_\rt$）：商 $\Lambda_\wt/\Lambda_\rt$ 的指数变成倒数，由式 (A.10) 得到的中心大小随之出错。
- 只用 $\Lambda_\rt$ 与 $\Lambda_\wt$ 判断群：忽略 $\Lambda_\char$ 的中间取值，会把 $SU(N)$ 与 $PSU(N)$ 当成同一个群；特征格才是群不变量（式 (A.6)）。

## 批注

### 易错预警：度规归一化会搬动余根格

$\Lambda_\cort$ 由 $\mu^\vee=2\mu/(\mu,\mu)$ 生成，这个定义依赖 $(\mu,\mu)$ 的归一化：换一种归一化会让 $\Lambda_\cort$ 作为 $\eurme$ 的子格整体缩放。式 (A.5) 的包含关系仍成立，但若把格当成与度规无关的集合去代入式 (A.13) 的商，就会得到非整数的指数。更稳的做法是先固定“短根长度平方为 $2$”的约定，再谈格与指数。

### 含糊点拨：对偶格为什么可以不写度规

文中把 $\Lambda_\wt$ 定义成 $\Lambda_\cort$ 的对偶格，又借度规把它认成 $\eurme$ 中的格。严格说对偶格住在 $\eurme^\vee$ 里，度规只提供识别；正因如此配对 $\langle\nu,\mu\rangle$ 与 $(\,,\,)$ 的归一化无关（式 (A.4)），而 $\Lambda_\wt$ 作为抽象格本身是有定义的，这也是它不必写成 $\eurme$ 的子集的理由。若强行把对偶格塞回同一个空间，就会把包含关系误当成等式。

### 背景直觉：四个格就是两类算符

Wilson 线按 $\Lambda_\wt$ 标号（电），'t Hooft 线按 $\Lambda_\cowt$ 标号（磁），而 $\Lambda_\rt$、$\Lambda_\cort$ 是整性底线：只有落在 $\Lambda_\rt$ 的权才对应 $G$ 的真正表示。四格之间的有限指数就是两类算符的错位，它也正是面算符参数 $\alpha$ 的周期来源；若把周期直接写成 $2\pi$，就会与这个指数差一个因子。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 附录 A；印刷页 [145, 148] / PDF 页 [146, 149]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/sA-duality.tex:40-160`
- 式 (A.1)–(A.15)：两对格、特征格及各自的商；印刷页 145–148，原文 PDF 第 146–149 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
