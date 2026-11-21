# oper：带附加结构的局部系统

- **id**：`bdh/concept/oper`
- **类型**：concept
- **位置**：§0
- **问题**：为什么在 oper 的定义里，必须要求每个单负根方向的分量处处非零，而不能只要求联络落在某处？

> oper 是 $G$-局部系统加上一个与 Borel 旗相容、且各单负根分量处处非零的联络；它把「局部系统」筛成与 $^{L}G$-oper 模空间对偶的那一类。

## 定义

设 $G$ 连通约化，$B$ 是 Borel 子群，$\mathfrak{n}=[\mathfrak{b},\mathfrak{b}]$，$\mathfrak{h}=\mathfrak{b}/\mathfrak{n}$。$X$ 上的 $G$-oper 是一对 $(\mathfrak{F}_B,\nabla)$：其中 $\mathfrak{F}_B$ 是 $B$-丛，$\nabla$ 是与之相容的 $G$-联络（即 $\mathfrak{F}_G=\mathfrak{F}_B\times_B G$ 上的联络），满足两条：① 投影 $c(\nabla)$ 落在 $\operatorname{gr}^{-1}\mathfrak{g}_{\mathfrak{F}}\otimes\omega_X$ 中；② 对每个单负根 $\alpha$，分量 $c(\nabla)^\alpha$ 处处非零。直观上，oper 是一个 G-局部系统，其结构群被「压」到 Borel 上，且压得尽可能深（只差一个非零常数）。$G=\mathrm{SL}_n$ 时 oper 结构就是一个满足 Griffiths 横截性的完全旗，$\mathrm{PSL}_2$-oper 等同于射影联络。

**记号**：$\mathfrak{F}_B\subset\mathfrak{F}_G$：$B$-丛与其诱导的 $G$-丛；$\mathfrak{b},\mathfrak{n},\mathfrak{h}$：李代数的 Borel、幂零根、Cartan、$c:\operatorname{Conn}(\mathfrak{F}_G)\to(\mathfrak{g}/\mathfrak{b})_{\mathfrak{F}}\otimes\omega_X$：到负根部分的投影、$\operatorname{gr}^{-1}\mathfrak{g}=\bigoplus_{\alpha<0}\mathfrak{g}^\alpha$：单负根空间的直和

## 关键点

- 定义有两条：$c(\nabla)\in\operatorname{gr}^{-1}\mathfrak{g}_{\mathfrak{F}}\otimes\omega_X$（落在最深层）与非零条件（每个单负根分量处处非零），缺一不可。
- 非零条件把 oper 与「任意 $B$-丛加联络」区分开：没有它，oper 模空间会在退化处爆掉。
- oper 的自同构群是中心 $Z=Z_G$；在完备、正亏格的曲线上，一个局部系统至多承载一个 oper 结构（3.1.4/3.1.5）。
- $\mathfrak{g}$-oper 是伴随群 $G_{ad}$ 的 oper；$G$ 单连通时 $^{L}G$-oper 与 $^{L}\mathfrak{g}$-oper 没有区别。
- $\mathrm{PSL}_2$-oper $=$ $X$ 上的射影联络 $=$ Sturm-Liouville 算子，这是最具体的例子。

## 公式

```latex
c(\nabla)\in\operatorname{gr}^{-1}\mathfrak{g}_{\mathfrak{F}}\otimes\omega_X
```
```latex
c(\nabla)^{\alpha}\neq 0\quad(\alpha<0\text{ 单根})
```
```latex
\operatorname{gr}^{-1}\mathfrak{g}=\bigoplus_{\alpha<0}\mathfrak{g}^{\alpha}
```

## 定理

**oper 结构的唯一性（命题 3.1.4/3.1.5）**：设 $X$ 完备、$g>1$，则一个 $G$-局部系统上至多有一个 oper 结构；等价地，oper 结构由 Harder–Narasimhan 旗唯一决定。

证明：sketch（原书 §3.1，命题 3.1.4、3.1.5）

- 把 oper 结构记为 $B$-丛加满足两条的联络。
- 用 $B$-丛的 Harder–Narasimhan 旗把可能的 $B$-结构定死。
- 非零条件保证不同旗不会给出同一个 oper。

缺口：原书只给论证要点，细节见 3.1 与 3.5。

## 常见错误

- 漏掉非零条件：只要求 $c(\nabla)$ 落在最深层，会得到 $\lambda=0$ 的退化情形，oper 模空间不再是 $\mathfrak{z}$ 的谱。
- 把 oper 当成「$G$-丛加联络」：oper 是局部系统（带平坦联络的丛）加 Borel 结构，缺了平坦性就不是局部系统。
- 在 $G=\mathrm{SL}_n$ 时把完全旗的 Griffiths 横截性当成全部：还要加上每个 $\operatorname{gr}_i$ 之间的同构条件（3.1.6），否则只得到「滤链」而不是 oper。

## 批注

### 背景直觉：oper 是朗兰兹对应的「最小」对象

几何朗兰兹想把 $X$ 上的 $^{L}G$-局部系统对应到 $\operatorname{Bun}_G$ 上的 $\mathcal{D}$-模。一般局部系统太「大」，无法整体处理；oper 是局部系统里被 Borel 结构压到最扁的那一类，恰好使对应的 $\mathcal{D}$-模可以用 $\mathfrak{z}$ 的商构造出来。所以 oper 不是人为的技术假设，而是让对应能落地的那一小片模空间：$^{L}\mathfrak{g}$-oper 的模空间正是 $\mathfrak{z}$ 的谱（0.2(b)）。

### 易错预警：$\mathfrak{g}$-oper 与 $G$-oper 不是同一个东西

本书同时用 $G$-oper（$G$-局部系统 + Borel 结构）与 $\mathfrak{g}$-oper（伴随群 $G_{ad}$ 的 oper）。$G$ 单连通时两者一致，因为此时 $G\to G_{ad}$ 的核是中心、不改变 oper 结构；一旦 $G$ 不单连通，$^{L}G$-oper 与 $^{L}\mathfrak{g}$-oper 就有区别，这也正是 0.2(d) 需要引入 $\lambda_{\mathfrak{F}}$、并把 $M_{\mathfrak{F}}$ 写成 $\lambda_{\mathfrak{F}}^{-1}\otimes N_{\bar F}$ 的原因。把两者混用，会看不出 $\lambda_{\mathfrak{F}}$ 为什么必须出现。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §0.3；印刷页 [4] / PDF 页 [4]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch00.tex:24-24`
- 原书 p.4；本书 PDF 页 = 印刷页。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §3.1；印刷页 [61, 62, 63] / PDF 页 [61, 62, 63]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch03.tex:14-20`
- 定义 3.1.3；页码按原书页眉。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
