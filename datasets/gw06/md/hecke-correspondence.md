# 赫克对应与仿射赫克代数

- **id**：`gw06/concept/hecke-correspondence`
- **类型**：concept
- **位置**：§3.7
- **问题**：赫克对应、仿射赫克代数、仿射辫群这三层分别在哪个范畴里起作用，为什么作者对 M_H 上的赫克作用只说「很可能」？

> 赫克对应是「在一点修改丛」的几何操作，其代数影子是仿射赫克代数；作者只猜想它作用在 M_H 的等变理论中，并未证明。

## 定义

赫克对应指在曲线上一点 $p$ 处修改丛（或把两个丛在 $p$ 外粘起来）得到的一族对应，它是几何朗兰兹中把「局部修改」翻译成「算子作用」的基本机制；在 $p$ 处反复修改并取线性组合，就得到仿射赫克代数 $\mathcal H_{\mathrm{aff}}$（$\mathbb C[W_{\mathrm{aff}}]$ 的 $q$-形变，$q\to1$ 时退化）。与 $\mathcal M_H$ 相关的是三层结构：$W_{\mathrm{aff}}$ 在上同调/K-理论上的作用是本节的定理（由参数空间单值性得到）；$\mathcal H_{\mathrm{aff}}$ 在等变 $K$-理论上的作用在 Springer 情形由 Kazhdan–Lusztig 证明，在 $\mathcal M_H$ 上作者只说「很可能」（may well admit）；仿射辫群（$W_{\mathrm{aff}}$ 的辫子化）则作用在 A-膜/B-膜范畴这类导出范畴上，属范畴化层面。

**记号**：$\mathcal H_{\mathrm{aff}}$：仿射赫克代数、$W_{\mathrm{aff}}$：仿射外尔群、$q$：赫克代数的形变参数

## 关键点

- 赫克对应是几何操作（在一点改丛），仿射赫克代数是它的代数化，仿射辫群是它的范畴化，三者不可混为一谈。
- $\mathcal H_{\mathrm{aff}}$ 是 $\mathbb C[W_{\mathrm{aff}}]$ 的 $q$-形变；KL 基的乘法常数是 Kazhdan–Lusztig 多项式，$q\to1$ 时退回外尔群代数。
- 在 $\mathcal M_H$ 上，作者给出的确定陈述只有 $W_{\mathrm{aff}}$ 的作用；赫克代数作用是对 $\beta=\gamma=0$（此时 $\mathcal M_H$ 有 $\mathbb C^*$ 作用，可谈等变上同调/K-理论）的猜想。
- 与局部情形（复余伴随轨道、Slodowy 切片）的类比是本节动机：Springer 表示在局部已升级为 $\mathcal H_{\mathrm{aff}}$ 的等变 K-理论作用，作者希望 $\mathcal M_H$ 上的整体版本也成立。
- 第 4.5 节会把 $W_{\mathrm{aff}}$ 的作用进一步丰富为仿射辫群在 A-膜/B-膜范畴上的作用。

## 公式

```latex
\mathcal H_{\mathrm{aff}}\ \text{是}\ \mathbb C[W_{\mathrm{aff}}]\ \text{的}\ q\text{-形变}
```
```latex
\mathcal H_{\mathrm{aff}}\curvearrowright K^{\mathbb C^*}_{\mathrm{eq}}(\mathcal M_H)\quad(\beta=\gamma=0)
```

## 定理

**Springer 情形的 KL 定理（作类比用）**：仿射赫克代数作用在 Springer 消解的等变 K-理论上，其 KL 基的乘法常数即 Kazhdan–Lusztig 多项式。

证明：gap（§3.7，仿射赫克代数段落及其后的译注）

1. 在 Springer 消解上构造赫克对应，得到 $\mathcal H_{\mathrm{aff}}$ 在等变 K-理论上的作用。 —— 这是局部（复余伴随轨道）版本，由 Kazhdan–Lusztig 证明。
2. 把局部构造搬到 $\mathcal M_H$（整体希格斯丛模空间）上。 —— 作者只提出「很可能」，未给证明。

缺口：第 2 步在原文中是猜想（may well admit），不是定理；写到卡片上必须标明。

## 常见错误

- 把「很可能作用」写成「作用」：原文 may well admit 是猜想，误当定理会把未证结论塞进朗兰兹对应。
- 把仿射赫克代数与仿射外尔群当成同一个东西：前者是后者的 $q$-形变，作用范畴也不同（等变 K-理论 vs 上同调）。
- 把辫群作用与赫克代数作用混为一层：辫群作用在导出范畴（膜范畴）上，是范畴化，不是同一个表示。

## 批注

### 易错预警：三层不可叠成一层

读这一段最容易把所有「仿射」开头的对象糊成一个。请按作用范畴分层：$W_{\mathrm{aff}}$ 作用于上同调/K-理论（定理）；$\mathcal H_{\mathrm{aff}}$ 作用于等变 K-理论（局部已证、整体是猜想）；仿射辫群作用于 A/B-膜范畴（范畴化）。

### 含糊点拨：为什么必须令 β=γ=0

等变上同调需要一个群作用才能定义。$\beta=\gamma=0$ 时 $\mathcal M_H$ 保留 $\mathbb C^*$ 作用，于是可以谈等变理论；一般参数下没有这个作用，赫克代数的猜想也就无从陈述。

### 背景直觉：赫克对应就是「改一点」

在 $p$ 处把丛 $E$ 改成 $E'$（两者在 $p$ 外相同），得到一个对应 $\mathcal M\leftarrow\mathcal H\rightarrow\mathcal M$；它作用在上同调上就是「在一点做修改」的算子。仿射赫克代数正是这些算子在 $q$ 形变下的代数封闭。

## 出处

- Gukov–Witten 2006（hep-th/0612073v2）中译校订本 §3.7；印刷页 [69, 71] / PDF 页 [70, 72]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03c-topology.tex:210-246`
- Springer/赫克代数/辫群三层见 PDF 第 70–72 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
