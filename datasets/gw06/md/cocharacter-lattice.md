# 余特征格

- **id**：`gw06/concept/cocharacter-lattice`
- **类型**：concept
- **位置**：§2.1
- **问题**：余特征格 Λ_cochar 为什么决定面算符参数 α 的周期性，它与群中心有什么关系？

> 余特征格 Λ_cochar 是 α 的周期格，商 t/Λ_cochar 给出极大环面；它同时决定群中心与磁荷的量子化。

## 定义

余特征格 $\Lambda_{\mathrm{cochar}}=\mathrm{Hom}(U(1),\mathbb{T})$ 是极大环面$\mathbb{T}$ 的一参数子群的格。按定义 $\mathbb{T}=\mathfrak{t}/\Lambda_{\mathrm{cochar}}$，因此 $\alpha$ 与 $\alpha+\lambda$（$\lambda\in\Lambda_{\mathrm{cochar}}$）给出同一个面算符。群中心由余权格与余特征格之商给出：$\mathcal{Z}(G)=\Lambda_{\mathrm{cowt}}/\Lambda_{\mathrm{cochar}}$（式 (2.4)）。当 $G$ 非单连通时，把 $\alpha$ 平移一个格矢会同时改变丛的拓扑：规范变换 $(r,\theta)\to\exp(\theta u)$ 在原点奇异，把 $E$ 扭成另一个 $G$-丛，其扭曲类 $\xi\in H^2(M,\pi_1(G))$ 与 $\alpha$ 的平移一起变化（式 (2.5)–(2.7)）。此外，若 $D$ 的自交数非零，$\alpha$ 还要满足量子化条件（式 (2.9)–(2.10)）。

**记号**：$\Lambda_{\mathrm{cochar}}$：余特征格；$\Lambda_{\mathrm{cowt}}$：余权格；$\Lambda_{\mathrm{char}}$：特征格；$\xi$：阻碍 $G$-丛提升为 $\bar G$-丛的特征类；$[D]$：庞加莱对偶于 $D$ 的类。

## 关键点

- $\mathbb{T}=\mathfrak{t}/\Lambda_{\mathrm{cochar}}$，这是 $\alpha$ 周期性的来源；$\alpha$ 不是 $\mathfrak{t}$ 中的元素。
- $\mathcal{Z}(G)=\Lambda_{\mathrm{cowt}}/\Lambda_{\mathrm{cochar}}$（式 (2.4)）：中心越大，余特征格在余权格中越“密”，$\alpha$ 的周期越小。
- 非单连通 $G$ 时，平移 $\alpha$ 伴随丛的扭曲类 $\xi$ 改变；只有把 $(\alpha,\xi)$ 一起看，才得到规范等价的正确分类（式 (2.6)–(2.7)）。
- 当 $D$ 的自交数 $D\cap D\neq 0$ 时，$\alpha$ 不能整体取任意值，而须满足由 $\int_M\delta_D\wedge\delta_D$ 决定的量子化条件（式 (2.9)–(2.10)）。

## 公式

```latex
\mathbb{T}=\mathfrak{t}/\Lambda_{\mathrm{cochar}}
```
```latex
{\mathcal Z}(G)=\Lambda_{\rm cowt}/\Lambda_{\rm cochar}
```
```latex
\mathrm{Hom}(U(1),\mathbb{T})\cong\pi_1(\mathbb{T})
```

## 常见错误

- 把余特征格与余根格混为一谈：余根格由余根生成，余特征格是它的整张成；两者只在 $G$ 单连通且单连时相同，一般情形差一个有限群（正是 $\mathcal{Z}(G)$ 的对偶）。
- 以为 $\alpha$ 是 $\mathfrak{t}$ 中的普通元素：忽略格的周期性会把参数空间写成 $\mathfrak{t}^3$ 而不是 $\mathbb{T}\times\mathfrak{t}\times\mathfrak{t}$。
- 忽略非单连通情形的丛扭曲：只平移 $\alpha$ 而不看 $\xi$，会把两个不同的规范场论误当成同一个。

## 批注

### 含糊点拨：周期为什么是格而不是 2π

常有人把 $\alpha$ 的周期记成 $2\pi$。在本文约定下 $A=\alpha\,d\theta$，绕一圈的和乐是 $\exp(-2\pi\alpha)$；要让它等于 $1$，只需 $\alpha$ 是余特征格中的元素，而不是 $2\pi$ 的整数倍。$2\pi$ 因子已经吃进指数里。

### 背景直觉：格与磁荷

$\mathrm{Hom}(U(1),\mathbb{T})\cong\pi_1(\mathbb{T})$ 的分类意义是磁荷：一个 $U(1)$ 嵌入给出一个磁通量子。对偶群侧的电荷格 $\Lambda_{\mathrm{char}}$ 满足 $\Lambda_{\mathrm{char}}=\mathrm{Hom}(\Lambda_{\mathrm{cochar}},\mathbb{Z})$，这正是 GNO 对偶的起点（附录 A）。

### 易错预警：自交数非零时

本文大部分应用取 $D$ 不自交（几何朗兰兹紧化时 $D=C\times\{p\}$ 的自交数为零），但四维流形理论中一般 $D\cap D\neq 0$ 很重要。此时 $\alpha$ 的量子化条件依赖自交数，直接套用自由情形会漏掉整数量子化。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §2.1；印刷页 [5, 6] / PDF 页 [6, 7]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s02a-definition.tex:84-130`
- 式 (2.4)–(2.7)：群中心、丛扭曲与 α 的平移；印刷页 5–6，原文 PDF 第 6–7 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
