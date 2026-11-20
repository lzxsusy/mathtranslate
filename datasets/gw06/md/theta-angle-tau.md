# θ 角与复化耦合 τ

- **id**：`gw06/concept/theta-angle-tau`
- **类型**：concept
- **位置**：§2.3
- **问题**：四维 θ 角、复化耦合 τ 与面算符的二维 θ 角 η 之间是什么关系？

> 四维规范耦合 τ = θ/2π + 4πi/e² 含四维 θ 角；面算符还带支撑面上的二维 θ 角 η，取值于对偶环面。

## 定义

四维 $\mathcal{N}=4$ 超杨–米尔斯理论的耦合由复参数 $\tau=\theta/2\pi+4\pi i/e^2$ 刻画，其中 $\theta$ 是四维 $\theta$ 角、$e$ 是规范耦合。面算符除了 $(\alpha,\beta,\gamma)$ 之外还带一个额外参数：支撑曲面 $D$ 上二维规范理论的 $\theta$ 角 $\eta$。若 $G$ 的秩为 $r$，$\mathbb{T}\cong U(1)^r$，则 $\eta\in\mathrm{Hom}(\Lambda_{\mathrm{cochar}},U(1))={}^L\!\mathbb{T}$（式 (2.13)），即对偶群 ${}^LG$ 的极大环面；等价地，$\mathrm{Hom}(U(1),\mathbb{T})={}^L\!\mathbb{T}$ 的两端分别分类 $G$ 的磁荷与 ${}^LG$ 的电荷（式 (2.14)），这就是基本的 GNO 对偶。于是面算符的完整参数是 $(\alpha,\beta,\gamma,\eta)$，$S$-对偶会把 $\tau$ 与 $\alpha,\eta$ 一起变换。

**记号**：$\tau$：复化规范耦合；$\theta$：四维 $\theta$ 角；$e$：规范耦合常数；$\eta$：$D$ 上的二维 $\theta$ 角；${}^L\!\mathbb{T}$：对偶群的极大环面；$\Lambda_{\mathrm{char}}$：特征格。

## 关键点

- $\tau=\theta/2\pi+4\pi i/e^2$：$\theta$ 的周期是 $2\pi$，$\tau$ 的虚部是 $4\pi/e^2$（不是 $2\pi/e^2$）。
- 面算符多一个参数 $\eta\in\mathrm{Hom}(\Lambda_{\mathrm{cochar}},U(1))={}^L\!\mathbb{T}$，它是 $D$ 上二维规范场的 $\theta$ 角（式 (2.13)）。
- ${}^L\!\mathbb{T}={}^L\mathfrak{t}/\Lambda_{\mathrm{char}}$，而 $\mathbb{T}=\mathfrak{t}/\Lambda_{\mathrm{cochar}}$：对偶把特征格与余特征格互换。
- 两个 $\theta$ 角层级不同：四维 $\theta$ 进入 $\tau$、影响整体耦合；二维 $\eta$ 只活在面算符的 $D$ 上，但 $S$-对偶把它与 $\alpha$ 混合成对偶环面上的坐标。

## 公式

```latex
\tau=\frac{\theta}{2\pi}+\frac{4\pi i}{e^2}
```
```latex
{\rm Hom}(\Lambda_{\rm cochar},U(1))={}^L\!\mathbb{T}
```
```latex
{}^L\!\mathbb{T}={}^L\mathfrak{t}/\Lambda_{\rm char}
```

## 常见错误

- 把 $\eta$ 当成四维 $\theta$ 角：$\eta$ 只定义在面算符的支撑曲面上，是二维理论的 $\theta$ 角，量纲与作用都不同。
- 把 $\tau$ 的虚部写成 $2\pi i/e^2$ 或 $\theta/2\pi+2\pi i/e^2$：本文约定是 $4\pi i/e^2$，与 $e$ 的定义（以及 $\tau\to-1/(n_{\mathfrak g}\tau)$ 的 $S$-对偶）配套。
- 把 ${}^L\!\mathbb{T}$ 与 $\mathbb{T}$ 混同：对偶群的环面用特征格作商，不是余特征格。

## 批注

### 易错预警：$4\pi$ 不是 $2\pi$

$\tau=\theta/2\pi+4\pi i/e^2$ 里的 $4\pi$ 来自 $\mathcal{N}=4$ 理论的规范化：$\mathrm{Im}\,\tau=4\pi/e^2$，于是 $S$-对偶 $\tau\to-1/(n_{\mathfrak g}\tau)$ 才给出 $e\to 4\pi/e$ 的正确互换。写成 $2\pi i/e^2$ 会让 $S$-对偶的因子整体错位，并且与式 (2.57) 中 $\tau$-平移的周期 $2\pi$ 对不上。

### 含糊点拨：$\eta$ 为什么在对偶环面上

$D$ 上的二维规范场有 $r$ 个 $U(1)$ 因子，每个都可以加一个 $\theta$ 角；它们的整体取值空间是对偶环面 ${}^L\!\mathbb{T}$，因为 $\theta$ 角按特征格$\Lambda_{\mathrm{char}}$ 量子化（周期 $2\pi$ 对应 $\Lambda_{\mathrm{char}}$ 的整数值）。这就是 GNO 对偶在面算符上的体现。

### 背景直觉：两个 θ 角，一个对偶

四维 $\theta$ 与二维 $\eta$ 在 $S$-对偶下并不是各自独立变换：$S$ 把 $\tau\to-1/(n_{\mathfrak g}\tau)$ 的同时，把 $(\alpha,\eta)$ 送到 $(\eta,-\alpha)$。也就是说，面算符的参数空间本身参与了对偶，而不只是旁观者。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §2.3；印刷页 [11, 12] / PDF 页 [12, 13]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s02a-definition.tex:238-286`
- 式 (2.13)–(2.14)：二维 θ 角与 GNO 对偶；印刷页 11–12，原文 PDF 第 12–13 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
