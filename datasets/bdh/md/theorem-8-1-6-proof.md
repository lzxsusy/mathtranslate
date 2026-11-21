# 定理 8.1.6 的证明

- **id**：`bdh/concept/theorem-8-1-6-proof`
- **类型**：concept
- **位置**：§6.2
- **问题**：为什么证明 V≅Vac'⊗W 的关键会落在 Vac' 的任意扩张必分裂这一条上？

> 第 6 章先用两条引理把离散 U̅'-模写成 Vac'⊗W，再把 Vac' 的任意扩张化归为 1-上闭链，并用 Kostant 截面证明它分裂，从而完成定理 8.1.6。

## 定义

设 $V$ 是离散 $\overline{U}'$-模，$\mathfrak{g}\otimes O$ 在 $V$ 上的表示可积，$L_0\in\operatorname{Der}O$ 可对角化且其谱与每个 $c+\mathbb{Z}$ 的交有下界。定理 8.1.6 断言：作为 $\overline{U}'$-模，$V\cong\mathit{Vac}'\otimes W$。第 6 章给出证明，分四步。第一步（6.2.1）：若非零 $\overline{U}'$-模 $V$ 被理想 $I\subset\mathfrak{Z}$ 零化且 $\mathfrak{g}\otimes O$ 作用可积，则 $V$ 有非零的 $\mathfrak{g}\otimes O$-不变向量。第二步（6.2.2）：若 $\mathfrak{z}_{\mathfrak{g}}(O)$-模 $N$ 带 $I/I^2$ 的作用、$L_0$ 可对角化且谱在每个 $c+\mathbb{Z}$ 中有下界，则 $N$ 是自由 $\mathfrak{z}_{\mathfrak{g}}(O)$-模。第三步（6.2.3）：对 $N=V^{\mathfrak{g}\otimes O}$ 用 6.2.2 得 $N=\mathfrak{z}\otimes W$，并证明自然映射 $f:\mathit{Vac}'\otimes W\to V$ 是同构；核用 6.2.1 直接消掉，余核若非零则给出 $\mathit{Vac}'$ 的一个不分裂扩张。第四步（6.2.4）：证明任何满足 $IP=0$ 的扩张 $0\to\mathit{Vac}'\otimes W\to P\to\mathit{Vac}'\to 0$ 必分裂；证明把扩张化为 1-上闭链，用 $\mathit{Vac}'$ 的滤链归约到 $\psi:\mathfrak{g}\otimes O\to\mathit{Vac}^{cl}$，再用 Kostant 截面 $\operatorname{Kos}_O$ 造出上边缘。

**记号**：$\mathfrak{Z}$：$\overline{U}'$ 的中心；$I\subset\mathfrak{Z}$：零化 $V$ 的理想、$\mathcal{L}_0$：Sugawara 元素（3.6.15–3.6.16）；在 $V^{\mathfrak{g}\otimes\mathfrak{m}}$ 上 $2\mathcal{L}_0$ 的作用等于 Casimir 元、$\operatorname{Kos}_O\subset\mathfrak{g}^*\otimes\omega_O$：Kostant 截面，$\operatorname{Kos}_O\to\operatorname{Hitch}_{\mathfrak{g}}(O)$ 是同构、$\beta_\psi$：由 1-上闭链 $\psi$ 定义的配对；$B_\Psi$：由群 1-上闭链 $\Psi$ 定义的配对

## 关键点

- 6.2.1：$V$ 非零、$\mathfrak{g}\otimes O$ 作用可积、$I$ 零化 $V$ $\Rightarrow$ $V^{\mathfrak{g}\otimes O}\ne 0$。证明用 $\mathfrak{g}\otimes\mathfrak{m}$ 的投射幂幺性得 $V^{\mathfrak{g}\otimes\mathfrak{m}}\ne 0$，再用 $2\mathcal{L}_0$ 在该空间上等于 Casimir、而 $\mathcal{L}_0V=0$，推出 $\mathfrak{g}$ 作用平凡。
- 6.2.2：把 $\mathfrak{z}_{\mathfrak{g}}(O)$ 换成 $A_{{}^{L}\mathfrak{g}}(O)=\mathbb{C}[u_{jk}]$，$I/I^2$ 换成 $\mathfrak{a}_{{}^{L}\mathfrak{g}}$；由 $L_0u_{jk}=(d_j+k)u_{jk}$（$d_j>0$）知 $\partial/\partial u_{jk}$ 的权 $-(d_j+k)\to-\infty$，故每个元素被几乎所有 $\partial/\partial u_{jk}$ 零化，于是 $N=A_{{}^{L}\mathfrak{g}}(O)\otimes N_0$。
- 6.2.3：对 $N=V^{\mathfrak{g}\otimes O}$ 用 6.2.2 得 $N=\mathfrak{z}_{\mathfrak{g}}(O)\otimes W$；$f:\mathit{Vac}'\otimes W\to V$ 的核满足 $(\operatorname{Ker}f)^{\mathfrak{g}\otimes O}=0$，故 $\operatorname{Ker}f=0$；若余核非零，6.2.1 给出非零映射 $\mathit{Vac}'\to\operatorname{Coker}f$，即 $\mathit{Vac}'\otimes W$ 被 $\mathit{Vac}'$ 的不分裂扩张，与 6.2.4 矛盾。
- 6.2.4：任一满足 $IP=0$ 的扩张 $0\to\mathit{Vac}'\otimes W\to P\to\mathit{Vac}'\to 0$ 分裂。证明先由 Ext 可加性化到 $\dim W<\infty$ 进而 $W=\mathbb{C}$，取 $p$ 为真空向量原像，$\varphi(a)=ap$ 是 1-上闭链；再用 $\overline{U}'$ 的滤链把 $\varphi$ 归约为 $\psi:\mathfrak{g}\otimes O\to\mathit{Vac}^{cl}$。
- 6.2.4 的后半：$\operatorname{gr}\mathit{Vac}'=\operatorname{Sym}(\mathfrak{g}\otimes K/\mathfrak{g}\otimes O)=\mathit{Vac}^{cl}$（2.4.1）；令 $\beta_\psi(a,\eta):=(\psi(a))(\eta)$（式 (293)），引理 (294) 说 $\beta_\psi$ 在正则 $\eta$ 的稳定化子 $\mathfrak{c}(\eta)$ 上为零；群版本 $B_\Psi$ 满足上闭链关系 (303)，在 $\operatorname{Kos}_O$ 上由 (305) 定义 $f$ 即得 (304)，故 $B_\Psi$ 是上边缘，扩张分裂。
- 6.2.5：命题 6.2.4 或与 [F91] 第 97–98 页的命题有关；修改 [F91] 的方法也许能证明更多。

## 公式

```latex
0\to\mathit{Vac}'\otimes W\to P\to\mathit{Vac}'\to 0
```
```latex
\beta_\psi(a,\eta):=(\psi(a))(\eta)
```
```latex
\beta_\psi(a,\eta)=0,\qquad a\in\mathfrak{c}(\eta)
```
```latex
B_\Psi(g,\eta)=0,\qquad g\in C(\eta)
```
```latex
B_\Psi(g_1g_2,\eta)=B_\Psi(g_1,\eta)+B_\Psi(g_2,g_1^{-1}\eta g_1)
```
```latex
B_\Psi(g,\eta)=f(g^{-1}\eta g)-f(\eta)
```
```latex
f(g^{-1}\eta g)=B_\Psi(g,\eta),\qquad \eta\in\operatorname{Kos},\ g\in G(O)
```

## 常见错误

- 把 6.2.2 的条件“谱与每个 $c+\mathbb{Z}$ 的交有下界”弱化成“谱有下界”：$L_0$ 与 $I/I^2$ 的作用相容，谱可整体平移，必须对每个 $c$ 都有下界；只对一个 $c$ 有下界，就得不出 $N$ 自由。
- 丢掉 6.2.4 的 $IP=0$ 条件：没有它，$\varphi$ 未必落在 $\mathit{Vac}'$ 的有限层 $\mathit{Vac}'_k$ 中，滤链归约与 $\psi$ 的构造都不成立。
- 把 (294) 的 $\mathfrak{c}(\eta)$ 与 (302) 的 $C(\eta)$ 混为一谈：前者是李代数 $\mathfrak{g}\otimes O$ 中的稳定化子，后者是群概形 $G(O)$ 中的稳定化子；证明先用李代数版本（微分为零），再积分到群版本。

## 批注

### 易错预警：2L_0 才是 Casimir

6.2.1 的证明里起作用的是 $2\mathcal{L}_0$：由 (85) 可见，$2\mathcal{L}_0$ 在 $V^{\mathfrak{g}\otimes\mathfrak{m}}$ 上的作用相当于 $\mathfrak{g}$ 的 Casimir 元。若直接用 $\mathcal{L}_0$，就会差一个因子 2，把结论误写成“$\mathcal{L}_0$ 在该空间上等于 Casimir”。这个因子 2 在后文用 $L_0$ 的特征值记账时（第 8–9 章）还会反复出现，务必记住。

### 含糊点拨：为什么可以归约到 W=ℂ

6.2.4 开头用了一句“Ext 可加，故可设 $W=\mathbb{C}$”。完整推理是：先取有限维 $W_1\subset W$ 使 $(\mathfrak{g}\otimes O)\cdot p\subset\mathit{Vac}'\otimes W_1$，故可设 $\dim W<\infty$；再把 $W$ 分解为直和，用扩张群对直和的可加性逐个处理。这不是对任意 $W$ 的断言，而是把问题化到最小情形；漏掉这一步，后面的 1-上闭链论证只在有限维 $W$ 上成立。

### 背景直觉：Kostant 截面为什么能杀掉上闭链

Hitchin 纤维化在正则部分有 Kostant 整体截面 $\operatorname{Kos}_O$，且 $\operatorname{Kos}_O\to\operatorname{Hitch}_{\mathfrak{g}}(O)$ 是同构。$B_\Psi$ 是 $G(O)\times(\mathfrak{g}^*\otimes\omega_O)$ 上的函数，其在轨道上的“平移”完全由它在截面上的值决定；于是 (305) 在 $\operatorname{Kos}$ 上定义 $f$、再沿 $G(O)$-轨道延拓，就自动满足上边缘关系 (304)。换言之，证明把 Hitchin 纤维化的截面存在性翻译成了 $H^1$ 的消失；6.2.5 提到 [F91] 正是这条思路的来源。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §6.2；印刷页 [230, 231, 232, 233, 234, 235] / PDF 页 [230, 231, 232, 233, 234, 235]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch06.tex:12-124`
- 页码为原书印刷页，PDF 页 = 印刷页（偏移 0）。第 6 章 6.2 节见 p.230–235（\SourcePage{230} 在第 7 行、{231} 在第 21 行、{232} 在第 32 行、{233} 在第 57 行、{234} 在第 87 行、{235} 在第 110 行）；6.1 节在原书仅有序号而无正文。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
