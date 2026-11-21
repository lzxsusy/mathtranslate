# 扭微分算子的交换环 $\mathfrak{z}$

- **id**：`bdh/concept/twisted-differential-operators`
- **类型**：concept
- **位置**：§0
- **问题**：为什么量子化 $\mathfrak{z}^{cl}$ 必须先把算子「扭」一下，直接取 $\operatorname{Bun}_G$ 上的整体微分算子为什么不行？

> 把 Hitchin 的 $\mathfrak{z}^{cl}$ 换成作用在 $\omega_{\operatorname{Bun}_G}$ 的平方根上的微分算子，所得交换环 $\mathfrak{z}$ 的象征恰为 $\mathfrak{z}^{cl}$，这就是 Hitchin 可积系统的量子化。

## 定义

取 $\operatorname{Bun}_G$ 的典范丛 $\omega_{\operatorname{Bun}_G}$ 的一个平方根 $\omega_{\operatorname{Bun}_G}^{1/2}$。扭微分算子是指作用在这个平方根上的微分算子，其层记为 $\mathcal{D}'$。本书定义 $\operatorname{Bun}_G$ 上一族这样的算子构成的交换环 $\mathfrak{z}=\mathfrak{z}(X)\subset\Gamma(\operatorname{Bun}_G,\mathcal{D}')$，使得 $\mathfrak{z}$ 中算子的象征恰好构成 Hitchin 哈密顿量的环 $\mathfrak{z}^{cl}$。于是有交换图式的量子化：$\operatorname{gr}\mathfrak{z}\simeq\mathfrak{z}^{cl}$，其中滤链来自微分算子的阶。

**记号**：$\omega_{\operatorname{Bun}_G}$：$\operatorname{Bun}_G$ 上的典范丛；$\omega_{\operatorname{Bun}_G}^{1/2}$：其平方根、$\mathcal{D}'$：扭微分算子层（本书第 1 章用 $D'=D^{1/2}$ 的记号）、$\mathfrak{z}=\mathfrak{z}(X)$：量子化的交换环；$\operatorname{gr}\mathfrak{z}$：其伴随分次代数

## 关键点

- 「扭」是指算子作用在 $\omega_{\operatorname{Bun}_G}$ 的一个平方根上，而不是作用在函数上；这是构造能整体存在的前提。
- 众所周知，$\operatorname{Bun}_G$ 上唯一的整体非扭微分算子是乘以局部常值函数，所以不做扭就没有非平凡的量子化可谈。
- 象征映射给出 $\operatorname{gr}\mathfrak{z}\simeq\mathfrak{z}^{cl}$，因此 $\mathfrak{z}$ 的谱是 $\mathfrak{z}^{cl}$ 的谱的量子形变。
- 在单连通情形，$\omega_{\operatorname{Bun}_G}^{1/2}$ 唯一，于是 $M_{\mathfrak{F}}\cong\omega_{\operatorname{Bun}_G}^{-1/2}\otimes N_{\mathfrak{F}}$（见 0.2(d)）。

## 公式

```latex
\mathfrak{z}=\mathfrak{z}(X)\subset\Gamma(\operatorname{Bun}_G,\mathcal{D}')
```
```latex
\operatorname{gr}\mathfrak{z}\simeq\mathfrak{z}^{cl}
```
```latex
M_{\mathfrak{F}}\cong\omega_{\operatorname{Bun}_G}^{-1/2}\otimes N_{\mathfrak{F}}
```

## 常见错误

- 把扭理解成「乘一个线丛」的权宜之计：扭改变的是算子作用的模，象征映射与滤链都要重算，否则 $\operatorname{gr}\mathfrak{z}\simeq\mathfrak{z}^{cl}$ 无从谈起。
- 以为任何平方根都存在：只有当 $\omega_{\operatorname{Bun}_G}$ 在 $\operatorname{Pic}$ 中可开方时才谈得上「那个」平方根，单连通情形唯一，一般情形要靠线丛 $\lambda_{\mathfrak{F}}$ 补足。
- 把 $\mathfrak{z}$ 当成非交换的：它按构造是交换环，交换性正是可积性在量子侧的对应物。

## 批注

### 背景直觉：量子化 = 把函数换成算子、把符号换成象征

经典可积系统给的是相空间上的函数 $\mathfrak{z}^{cl}$。量子化的标准配方是「函数 → 算子、泊松括号 → 换位子、符号 → 象征」，并要求伴随分次代数回到原来的函数环。本书的特别之处在于：$\operatorname{Bun}_G$ 上不存在非平凡的整体微分算子，所以必须先把算子扭到 $\omega^{1/2}$ 上；扭完之后，$\mathfrak{z}$ 的谱才与 $^{L}\mathfrak{g}$-oper 的模空间对上，这正是几何朗兰兹的入口。

### 易错预警：$\mathfrak{z}$ 与 $\mathfrak{z}^{cl}$ 不同层

$\mathfrak{z}^{cl}$ 是 $T^*\operatorname{Bun}_G$ 上的函数代数，$\mathfrak{z}$ 是 $\operatorname{Bun}_G$ 上扭微分算子层的整体截面。断言「$\mathfrak{z}$ 就是 $\mathfrak{z}^{cl}$ 的量子化」只在象征映射 $\operatorname{gr}\mathfrak{z}\simeq\mathfrak{z}^{cl}$ 的意义下成立；把两者当成同一个环、或把 $\mathfrak{z}$ 的元素直接当成 $\operatorname{Bun}_G$ 上的函数，都会让 0.2(a) 的整条论证失去对象。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §0.2(a)；印刷页 [3, 4] / PDF 页 [3, 4]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch00.tex:9-9`
- 原书 p.3；本书 PDF 页 = 印刷页。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §2.5；印刷页 [24, 25, 26] / PDF 页 [24, 25, 26]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch02.tex:230-243`
- 定理 2.5.5 与 $\mathfrak{z}^{(x)}(X)$ 的构造；页码按原书页眉。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
