# 仿射外尔群在 M_H 上同调上的作用

- **id**：`gw06/concept/affine-weyl-action`
- **类型**：concept
- **位置**：§3.7
- **问题**：仿射外尔群并不作用在 M_H 上，那它究竟「作用」在什么上，为什么这种作用能被 H² 里的一个公式唯一确定？

> 参数空间的单值性给出仿射外尔群在上同调与 K-理论上的表示，H² 中的公式 (3.86) 确定了这个作用的具体形式。

## 定义

对单连通的 $G$ 与 $\mathbb L=\mathbb T$，分歧参数 $(\alpha,\beta,\gamma)$ 取值于 $\mathfrak t^3$；让它模去仿射外尔群 $W_{\mathrm{aff}}$（由 $0\to\Lambda_{\mathrm{cort}}\to W_{\mathrm{aff}}\to W\to1$ 定义，平移格是余根格），等价于让 $(\alpha,\beta,\gamma)\in\mathbb T\times\mathfrak t\times\mathfrak t$ 模去外尔群 $W$。把 $\mathfrak t^3$ 中使 $\mathcal M_H$ 出现局部或整体奇点的那些实余维三的仿射线性子空间挖掉，得到连通的单连通空间 $\mathcal X$。在 $\mathcal X$ 上 $W_{\mathrm{aff}}$ 自由作用，故 $\mathcal X/W_{\mathrm{aff}}$ 是光滑流形、基本群为 $W_{\mathrm{aff}}$；$\mathcal M_H(\alpha,\beta,\gamma;p)$ 的上同调沿这个底变化，作为某个平坦丛的纤维，其单值性给出表示 $\rho:W_{\mathrm{aff}}\to\mathrm{Aut}\,H^*(\mathcal M_H;\mathbb Z)$。这就是所谓「仿射外尔群作用」的准确含义——流形 $\mathcal M_H$ 上并没有群作用。

**记号**：$W_{\mathrm{aff}}$：仿射外尔群、$\Lambda_{\mathrm{cort}}$：余根格、$\Lambda_{\mathrm{wt}}$：权格、$\mathcal X$：去掉奇点轨迹后的参数空间

## 关键点

- 恒等式 $(\mathfrak t^3)/W_{\mathrm{aff}}=(\mathbb T\times\mathfrak t\times\mathfrak t)/W$ 只因 $\mathbb T=\mathfrak t/\Lambda_{\mathrm{cort}}$（单连通情形）而成立，它把「平移 $\alpha$」与「$\alpha$ 取值于 $\mathbb T$」两种观点统一起来。
- 奇点出现在 $W_{\mathrm{aff}}$ 作用非正则处：被某个像非零的 $x\in W_{\mathrm{aff}}$ 固定，会对 $\alpha,\beta,\gamma$ 各加一个实条件，合计实余维三。
- $\mathcal X$ 连通且单连通，故 $\mathcal X/W_{\mathrm{aff}}$ 的基本群恰为 $W_{\mathrm{aff}}$，单值性表示没有额外的模糊。
- $H^2(\mathcal M_H;\mathbb Z)=\mathbb Z\oplus\Lambda_{\mathrm{wt}}$，辛形式类 $[\omega_I/2\pi]=e\oplus(-\alpha^*)$ 在 $W_{\mathrm{aff}}$ 的联合作用下不变，这唯一确定了作用：$W$ 平凡作用于 $\mathbb Z$、按通常方式作用于 $\Lambda_{\mathrm{wt}}$，平移 $\mathfrak m\in\Lambda_{\mathrm{cort}}$ 把 $e$ 送到 $e\oplus\mathfrak m^*$。
- 多个分歧点时群是 $(W_{\mathrm{aff}})^s$，作用在 $\mathcal X_s$ 上；非单连通 $G$ 时 $\mathcal M_H$ 有 $\#\pi_1(G)$ 个分支，$\Lambda_{\mathrm{cochar}}$ 置换分支，而固定在一个分支上的作用仍由 $\Lambda_{\mathrm{cort}}$ 给出。

## 公式

```latex
0\to\Lambda_{\mathrm{cort}}\to W_{\mathrm{aff}}\to W\to 1
```
```latex
(\mathfrak t\times\mathfrak t\times\mathfrak t)/W_{\mathrm{aff}}=(\mathbb T\times\mathfrak t\times\mathfrak t)/W
```
```latex
H^2(\mathcal M_H(\alpha,\beta,\gamma;p);\mathbb Z)=\mathbb Z\oplus\Lambda_{\mathrm{wt}}
```
```latex
[\omega_I/2\pi]=e\oplus(-\alpha^*)
```
```latex
e\to e\oplus\mathfrak m^*
```

## 定理

**参数空间单值性定理**：在 $\mathcal X$ 内变动 $(\alpha,\beta,\gamma)$ 时 $\mathcal M_H$ 的拓扑不变，且这族流形的单值性给出 $W_{\mathrm{aff}}$ 在 $H^*(\mathcal M_H;\mathbb Z)$ 与 $K^*(\mathcal M_H)$ 上的表示。

证明：sketch（§3.7，式 (3.83)–(3.87)）

1. 从 $\mathfrak t^3$ 中挖掉使局部或整体奇点出现的余维三仿射线性子空间，得 $\mathcal X$。 —— 奇点只沿这些轨迹出现，避开它们后每根纤维都是光滑紧流形。
2. $\mathcal X$ 连通且单连通，故纤维的拓扑不变（Ehresmann）。 —— 余维三的闭集不影响 $\mathbb R^n$ 的连通与单连通性；族的局部平凡性由固有性保证。
3. $W_{\mathrm{aff}}$ 在 $\mathcal X$ 上自由作用，于是 $\mathcal X/W_{\mathrm{aff}}$ 的基本群是 $W_{\mathrm{aff}}$。 —— 正则性即稳定子平凡；基本群等于被作用的单连通空间上的自由群作用之群。
4. 上同调沿底构成平坦丛，其单值性即为所求表示。 —— 局部系数系（local system）的标准构造。

缺口：原文省略了 Ehresmann 与固有性的技术前提；$H^2$ 上的作用则另需 (3.86) 的不变性来唯一确定。

## 常见错误

- 以为 $W_{\mathrm{aff}}$ 作用在 $\mathcal M_H$ 本身：流形上没有这个作用，只有上同调/K-理论上的单值性表示。
- 把平移格当成权格：$\mathbb T=\mathfrak t/\Lambda_{\mathrm{cort}}$ 对单连通 $G$ 成立，非单连通时 $\alpha$ 取值于 $\mathfrak t/\Lambda_{\mathrm{cochar}}$，二者互换是本节最常见的错误。
- 把 $\mathfrak m^*$ 放进 $\mathbb Z$ 那一项：这会破坏 $e$ 的整性，并使 (3.86) 不再不变。
- 把多个分歧点的群误写成 $W_{\mathrm{aff}}$：应为 $(W_{\mathrm{aff}})^s$，且还可扩大为 $\Lambda^*\rtimes W^s$（只要总平移属于余根格）。

## 批注

### 易错预警：「作用」二字要打引号

作者说 $W_{\mathrm{aff}}$ 作用在 $H^*(\mathcal M_H)$ 上，指的是平坦丛的单值性表示 $\rho:W_{\mathrm{aff}}\to\mathrm{Aut}\,H^*(\mathcal M_H;\mathbb Z)$，只在共轭意义下确定。真正的群作用不会有换基点就共轭这种含糊，也不需要在参数空间里绕路。

### 含糊点拨：余维三从哪来

被 $x\in W_{\mathrm{aff}}$ 固定意味着 $x$ 在 $\alpha$、$\beta$、$\gamma$ 上各施加一个独立条件；若 $x$ 的像是单位元（纯平移），它只在 $\alpha$ 上有条件，不产生奇点——这正是「$\Lambda_{\mathrm{cort}}$ 在 $\alpha$ 上自由作用」的那句话。

### 背景直觉：为什么 $H^2$ 能定住整个作用

$H^2$ 里既有 $\mathbb Z$（辛形式）又有 $\Lambda_{\mathrm{wt}}$（与分歧数据对偶），而 $\omega_I$ 的类在参数变换与上同调变换的联合下必须不变。这个不变性像一把尺子，把 $W_{\mathrm{aff}}$ 的平移部分钉在 $\Lambda_{\mathrm{wt}}$ 上、把 $W$ 部分钉成通常作用。

## 出处

- Gukov–Witten 2006（hep-th/0612073v2）中译校订本 §3.7；印刷页 [67, 70] / PDF 页 [68, 71]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03c-topology.tex:176-290`
- 仿射外尔群、$\mathcal X$ 与 H² 作用见 PDF 第 68–71 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
