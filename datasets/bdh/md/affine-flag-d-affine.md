# 仿射旗空间的 D-仿射性

- **id**：`bdh/concept/affine-flag-d-affine`
- **类型**：concept
- **位置**：§7.15
- **问题**：为什么仿射旗空间上的扭 $\mathcal{D}$-模恰好对应水平小于临界值的仿射李代数表示，而有限维的 Kostant 论证在这里失效？

> 若 $\chi$ 反占优且正则，整体截面函子 $\Gamma:\mathcal{M}^{\chi}(X)\to\mathcal{M}^{r}(\Gamma\mathcal{D}^{\chi})$ 是范畴等价，从而把低于临界水平的仿射 Kac–Moody 表示等同于仿射旗空间上的扭 $\mathcal{D}$-模。

## 定义

设 $K=\mathbb{C}((t))$、$O=\mathbb{C}[[t]]$，$\mathfrak{g}$ 是单有限维李代数、$G$ 是相应的单连通单群。$G(K)$ 在 $\mathfrak{g}(K)$ 上的伴随作用给出中心扩张 $G(K)^{\flat}$，其李代数 $\mathfrak{g}(K)^{\flat}$ 由余圈 $\phi,\psi\mapsto\operatorname{Res}(d\phi,\psi)$ 定义，其中 $(a,b):=\operatorname{Tr}(\operatorname{ad}_a\cdot\operatorname{ad}_b)$；$G(O)^{\flat}$ 是 $G(O)$ 的原像，并有典范同构 $s:G(O)^{\flat}\cong G(O)\times\mathbb{G}_m$（7.15.1）。取 $N\subset B\subset G$（$B$ 为 Borel 子群、$N$ 为其幂幺根、$H=B/N$），令 $N^{+},B^{+}$ 为 $N,B$ 在 $G(O)\to G$ 下的原像，$B^{\dagger}\subset G(K)^{\flat}$ 为 $B^{+}$ 的原像；置 $H^{\flat}:=B^{\dagger}/N^{+}$、$\mathfrak{h}^{\flat}=\operatorname{Lie}H^{\flat}$，则 $\mathfrak{h}^{\flat}\cong\mathfrak{h}\times\mathbb{C}$。仿射旗空间是 $X:=G(K)/B^{+}=G(K)^{\flat}/B^{\dagger}$：既约、连通、归纳投射、形式光滑的归纳概形，光滑纤维化到仿射 Grassmann 流形 $G(K)/G(O)$ 上；$X^{\dagger}:=G(K)^{\flat}/N^{+}$ 是 $X$ 上的左 $H^{\flat}$-torsor（主齐性空间），投影记 $p:X^{\dagger}\to X$。令 $\mathcal{M}^{\dagger}(X)$ 为 $X^{\dagger}$ 上弱 $H^{\flat}$-等变 $\mathcal{D}$-模的范畴，$\mathcal{D}^{\dagger}:=(p_{\cdot}\mathcal{D}^{\dagger}_{X})^{H^{\flat}}$ 是 $X$ 上的 Diff-代数，且为 $\operatorname{Sym}(\mathfrak{h}^{\flat})$-族的 tdo；由引理 7.15.3，$M\mapsto M_X:=(p_{\cdot}M)^{H^{\flat}}$ 与右作用给出范畴等价 $\mathcal{M}^{\dagger}(X)\cong\mathcal{M}(X,\mathcal{D}^{\dagger})$（385）。对 $\chi=(\chi_0,c)\in\mathfrak{h}^{\flat*}=\mathfrak{h}^{*}\times\mathbb{C}$ 取相应 tdo $\mathcal{D}^{\chi}$（$\mathcal{D}^{(0,0)}=\mathcal{D}_X$），置 $\mathcal{M}^{\chi}(X):=\mathcal{M}(X,\mathcal{D}^{\chi})$，并考虑拓扑代数 $\Gamma\mathcal{D}^{\chi}:=\Gamma(X,\mathcal{D}^{\chi})$ 与函子 (386) $\Gamma:\mathcal{M}^{\chi}(X)\to\mathcal{M}^{r}(\Gamma\mathcal{D}^{\chi})$，$\Gamma M:=\Gamma(X,M)$。称 $\chi$ 反占优，若 Verma 模 $M(\chi)$ 不可约（等价于 7.15.5 的三条显式条件）；称 $\chi$ 正则，若 $\rho:=(\rho_0,1/2)$ 使 $\chi+\rho$ 在仿射 Weyl 群 $W_{\mathrm{aff}}$ 中的稳定化子平凡。定理 7.15.6（本节的 D-仿射性定理）：若 $\chi$ 反占优且正则，则 (386) 是范畴等价。

**记号**：$G(K)^{\flat}$、$\mathfrak{g}(K)^{\flat}$：$G(K)$ 被 $\mathbb{G}_m$ 的中心扩张及其李代数，$1^{\flat}$ 是中心元、$H^{\flat}=B^{\dagger}/N^{+}$：水平方向的环面，$\mathfrak{h}^{\flat}\cong\mathfrak{h}\times\mathbb{C}$，故 $\chi=(\chi_0,c)$ 有水平分量 $c$、$X^{\dagger}\to X$：左 $H^{\flat}$-torsor；弱 $H^{\flat}$-等变 $\mathcal{D}$-模即 $X^{\dagger}$ 上沿纤维等变的 $\mathcal{D}$-模、$\mathcal{D}^{\dagger}$：$(p_{\cdot}\mathcal{D}^{\dagger}_{X})^{H^{\flat}}$，$X$ 上 $\operatorname{Sym}(\mathfrak{h}^{\flat})$-族的 tdo，$\mathcal{D}^{\chi}$ 是它在 $\chi$ 处的纤维、$\Gamma\mathcal{D}^{\chi}=\Gamma(X,\mathcal{D}^{\chi})$：整体微分算子构成的拓扑代数，$\Gamma M=\Gamma(X,M)$

## 关键点

- 7.15.1 的几何：$X=G(K)/B^{+}=G(K)^{\flat}/B^{\dagger}$ 既约、连通、归纳投射、形式光滑，且光滑纤维化到 $G(K)/G(O)$；$X^{\dagger}=G(K)^{\flat}/N^{+}$ 是左 $H^{\flat}$-torsor，作用为 $h^{\flat}\cdot x^{\dagger}=x^{\dagger}h^{\flat-1}$，并带显然的 $G(K)^{\flat}$-作用。
- 7.15.2–7.15.3：$\mathcal{D}^{\dagger}$ 是 $\operatorname{Sym}(\mathfrak{h}^{\flat})$-族 tdo，映射 (384) $\mathfrak{h}^{\flat}\to\Gamma(X,\mathcal{D}^{\dagger})=\Gamma(X^{\dagger},\mathcal{D}^{\dagger}_{X^{\dagger}})^{H^{\flat}}$ 等于沿 $p$ 纤维左作用的相反数、像在中心；右作用给出 (385)，且它是范畴等价。
- 7.15.4：$\chi=(\chi_0,c)$ 参数化 tdo 族的纤维，$\mathcal{M}^{\chi}(X)=\mathcal{M}(X,\mathcal{D}^{\chi})$；$\mathfrak{g}(K)^{\flat}\to\Gamma\mathcal{D}^{\chi}$ 连续且把 $1^{\flat}$ 送到 $-c$（负号来自 7.15.1 的中心扩张约定）。
- 7.15.5：反占优 $\iff$ Verma 模 $M(\chi)$ 不可约 $\iff$ (i) $c\ne-1/2$；(ii) 任意正余根 $(\chi_0+\rho_0)(h_{\alpha})\ne1,2,\ldots$；(iii) $\pm(\chi_0+\rho_0)(h_{\alpha})+2n\frac{c+1/2}{(\alpha,\alpha)}\ne1,2,\ldots$。正则指 $\chi+\rho$（$\rho=(\rho_0,1/2)$）在 $W_{\mathrm{aff}}$ 中稳定化子平凡。
- 7.15.6 的证明路线：7.15.8 给出 (i) $\chi$ 反占优时 $H^{r}(X,M)=0\ (r>0)$、(ii) $\chi$ 正则且 $M\ne0$ 时 $\Gamma M\ne0$，再由 [BB81]/[Kas] 的论证把消没性与非消没性合成范畴等价；7.15.15 用 Schubert 胞腔给出 $H^{a}(\mathfrak{n}^{+},\Gamma M)\cong\bigoplus_{w}H^{a-l(w)}_{\mathrm{DR}}(Y_{w},i_{w}^{!}M)$ 作为计算工具。

## 公式

```latex
\Gamma:\mathcal{M}^{\chi}(X)\to\mathcal{M}^{r}(\Gamma\mathcal{D}^{\chi}),\qquad \Gamma M:=\Gamma(X,M)
```
```latex
\mathcal{D}^{\dagger}:=(p_{\cdot}\mathcal{D}^{\dagger}_{X})^{H^{\flat}}
```
```latex
H^{a}(\mathfrak{n}^{+},\Gamma M)\cong\bigoplus_{w\in W_{\mathrm{aff}}}H^{a-l(w)}_{\mathrm{DR}}(Y_{w},i_{w}^{!}M)
```
```latex
\rho:=(\rho_0,1/2)\in\mathfrak{h}^{\flat*}
```

## 定理

**定理 7.15.6（仿射旗空间的 $\mathcal{D}$-仿射性）**：设 $\chi$ 反占优且正则，则函子 (386) $\Gamma:\mathcal{M}^{\chi}(X)\to\mathcal{M}^{r}(\Gamma\mathcal{D}^{\chi})$ 是范畴等价。

证明：略证（§7.15.6、§7.15.8，原书 p.362–363）

- 7.15.8(i)：$\chi$ 反占优时，任意 $M\in\mathcal{M}^{\chi}(X)$ 与 $r>0$ 有 $H^{r}(X,M)=0$，故 $\Gamma$ 正合
- 7.15.8(ii)：$\chi$ 正则且 $M\ne0$ 时 $\Gamma M\ne0$，故 $\Gamma$ 忠实
- 按 [BB81]/[Kas] 的论证（原文 7.15.6 后说「我们在下文 7.15.8 中证明」），由消没性与非消没性得到 $\Gamma$ 是范畴等价

缺口：原文只给出「如 [BB81]/[Kas]」的指引与 7.15.8 的两条性质，未展开等价性的逐步推导。

**定理 7.15.8（消没与非消没）**：(i) 若 $\chi$ 反占优，则对任意 $M\in\mathcal{M}^{\chi}(X)$ 与 $r>0$ 有 $H^{r}(X,M)=0$，其中 $H^{r}(X,M):=\varinjlim H^{r}(Y,M_{(Y)})$。(ii) 若 $\chi$ 正则且 $M\ne0$，则 $\Gamma M\ne0$。

证明：略证（§7.15.8、§7.15.12、§7.15.16，原书 p.363–365）

- (i) 用 7.15.9 的丰沛线丛 $L$ 与 (388) 的嵌入 $M\to V\otimes L\otimes M$，把 $H^{r}(Y,L\otimes F)$ 的高阶消没化归为可计算的情形（7.15.12）
- (ii) 用 7.15.15 的 Schubert 胞腔分解：若 $\Gamma M=0$，则 $H^{a}(\mathfrak{n}^{+},\Gamma M)=0$，而该分解的非零项给出矛盾（7.15.16）

缺口：两条的证明都依赖 7.15.9–7.15.17 的 Borel–Weil 与 Schubert 胞腔技术，此处只保留路线。

## 常见错误

- 把「反占优」当成有限维意义下的支配性：7.15.5 的三个条件里，(i) 单独排除 $c=-1/2$，(iii) 含仿射平移项 $2n\frac{c+1/2}{(\alpha,\alpha)}$；只检查 (ii) 的 $(\chi_0+\rho_0)(h_{\alpha})\ne1,2,\ldots$ 会漏掉 $c=-1/2$ 附近与仿射平移，从而把可约的 Verma 模当成不可约，进而误用定理 7.15.6。
- 把 $1^{\flat}$ 的作用符号弄反：7.15.4 明说 $\mathfrak{g}(K)^{\flat}\to\Gamma\mathcal{D}^{\chi}$ 把 $1^{\flat}$ 送到 $-c$。若记成 $+c$，则「水平 $c$」与「水平 $-c$」互换：7.15.5(i) 的 $c\ne-1/2$、7.15.9 的丰沛条件 $\frac{2b}{(\alpha,\alpha)}<\psi_0(h_{\alpha})<0$ 以及 7.15.7(i) 的 $\mathcal{M}^{c}(\mathfrak{g}(K))$ 全部错位。
- 以为可以照搬有限维的 Kostant 论证：7.15.7(ii) 指出，仿射情形的经典论断（$\mathfrak{g}(K)\hookrightarrow\Gamma(X,\Theta_X)$ 在 $\bigoplus_{n\ge0}\Gamma(X,\Theta_X^{\otimes n})$ 中稠密）是假的——$\mathfrak{g}(K)\to\Gamma(X,\Theta_X)$ 甚至不满。因此「生成稠密 $\Rightarrow$ 范畴等价」的有限维路线在仿射旗空间失效，定理 7.15.6 必须走 7.15.8 的消没/非消没，而不能由某个稠密性推出。

## 批注

### 背景直觉：D-仿射是「整体截面为等价」的仿射类比

仿射概形上 quasi-coherent 层的整体截面函子是范畴等价，这是「仿射」的本义；$\mathcal{D}$-仿射就是把 $\mathcal{O}$-模换成 $\mathcal{D}$-模后的同一性质。有限维的原型是 flag variety 上的 Beilinson–Bernstein 局部化（$\mathfrak{g}$-模 $\leftrightarrow$ flag variety 上的 $\mathcal{D}$-模），而 7.15 把它搬到 $X=G(K)/B^{+}$ 上：$\Gamma$ 从 $\mathcal{M}^{\chi}(X)$ 到 $\Gamma\mathcal{D}^{\chi}$-模，等价性即「$X$ 上没有额外的 $\mathcal{D}$-模上同调」。7.15.9 用丰沛线丛 $L$ 与 Borel–Weil 表示 $V$ 造出的 (388) 嵌入、7.15.11 说它是直和项，正是这个类比的表示论影子。

### 易错预警：正则性里的 $\rho=(\rho_0,1/2)$ 不能简化成 $\rho_0$

7.15.5 定义正则性用 $\rho:=(\rho_0,1/2)\in\mathfrak{h}^{\flat*}$，其中 $1/2$ 是水平方向的平移；$\chi+\rho$ 在 $W_{\mathrm{aff}}$ 中的稳定化子平凡。若按有限维习惯只用 $\rho_0$ 判断（即把水平分量当作 0），稳定化子的计算会漏掉仿射反射中 $1^{\flat}$ 的贡献，把本非正则的 $\chi$ 判成正则，于是错误地对不可约性未知的 $\chi$ 引用定理 7.15.6。注意这个 $1/2$ 与 7.15.5(iii) 的 $c+1/2$ 是同一约定的两面。

### 含糊点拨：定理只说「范畴等价」，不说「代数同构」

7.15.7(ii) 指出一个容易越界的地方：期望 $\mathfrak{g}(K)^{\flat}$ 在 $\Gamma\mathcal{D}^{\chi}$ 中生成稠密子代数，且 $\Gamma\mathcal{D}^{\chi\circ}$ 应是水平 $c$ 的包络代数 $\bar U^{c}$ 的某个拓扑完备化，但「能否显式确定该拓扑」原文明确说是开问题。因此从 7.15.6 只能读出 $\mathcal{M}^{\chi}(X)\cong\mathcal{M}^{r}(\Gamma\mathcal{D}^{\chi})$ 这一范畴等价，不能反推 $\Gamma\mathcal{D}^{\chi}\cong\bar U^{c}$，更不能据此断言两边的表示论（例如单模分类）逐字对应——那是尚未解决的问题。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §7.15.1；印刷页 [360] / PDF 页 [360]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch07.tex:3371-3376`
- 原书 p.360：\SourcePage{360} 在第 3366 行、\SourcePage{361} 在第 3377 行，锚点整段落在两者之间。本书 PDF 页 = 印刷页。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §7.15.4；印刷页 [361] / PDF 页 [361]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch07.tex:3394-3401`
- 原书 p.361：\SourcePage{361} 在第 3377 行、\SourcePage{362} 在第 3405 行，锚点（定义 $\chi$、$\mathcal{D}^{\chi}$ 与函子 (386)）整段落在两者之间。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §7.15.6；印刷页 [362] / PDF 页 [362]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch07.tex:3419-3421`
- 原书 p.362：\SourcePage{362} 在第 3405 行、\SourcePage{363} 在第 3432 行，定理 7.15.6 的陈述与「下文 7.15.8 中证明」一句落在两者之间。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
