# Hitchin 哈密顿量的量子化与水平性定理

- **id**：`bdh/concept/quantization-of-hitchin-hamiltonians`
- **类型**：concept
- **位置**：§2.5
- **问题**：为什么量子化 $\mathfrak{z}(X)$ 要经由 Kac--Moody 中心扩张与 $D_X$-模的水平截面两步构造，而不能直接在 $\operatorname{Bun}_G$ 上取整体微分算子？

> 量子化要造一个滤交换代数 $\mathfrak{z}(X)$、象征同构与滤态射 $h_X$；局部用 Kac--Moody 中心扩张与临界扭包络代数给出 $\mathfrak{z}_x$，整体用 $\mathbb{C}[[t]]$-族的水平截面 $H_{\nabla}(X,\mathfrak{z})$ 给出 $\mathfrak{z}(X)$，并用式 (28) 证其象征映射。

## 定义

2.2.5 的量子化问题是：造出 $\operatorname{Hitch}(X)$ 上函数环 $\mathfrak{z}^{cl}(X)$ 的滤交换代数提升 $\mathfrak{z}(X)$，以及同构 $\sigma_{\mathfrak{z}(X)}:\operatorname{gr}\mathfrak{z}(X)\xrightarrow{\sim}\mathfrak{z}^{cl}(X)$，并造滤代数态射 $h_X:\mathfrak{z}(X)\to\Gamma(\operatorname{Bun}_G,D')$，使 $\sigma_{\operatorname{Bun}_G}\circ\operatorname{gr}h_X=h_X^{cl}\circ\sigma_{\mathfrak{z}(X)}$。局部（2.5）的做法：取 $\mathfrak{g}\otimes K_x$ 的 Kac--Moody 中心扩张，其余圈为 $\operatorname{Res}_x c(du,v)$，其中 $c(a,b):=-\frac{1}{2}\operatorname{Tr}(\operatorname{ad}_a\cdot\operatorname{ad}_b)$（式 (18)）；令 $\mathfrak{z}_x:=\mathfrak{z}_{\mathfrak{g}}(\mathcal{O}_x):=D'_{(\mathfrak{g}\otimes K_x,G(\mathcal{O}_x))}$ 为临界扭的完备化包络代数的不变部分。整体（2.7）的做法：对 $\mathcal{O}=\mathbb{C}[[t]]$、$K=\mathbb{C}((t))$ 令 $\mathfrak{z}:=\mathfrak{z}_{\mathfrak{g}}:=\mathfrak{z}_{\mathfrak{g}}(\mathcal{O})_X$，并令 $\mathfrak{z}(X):=\mathfrak{z}_{\mathfrak{g}}(X):=H_{\nabla}(X,\mathfrak{z})$（式 (27)）为水平截面，即水平 $D_X$-模的整体截面。

**记号**：$K_x$：$x$ 处的形式幂级数域，$\mathcal{O}_x$：其整数环；$\mathcal{O}=\mathbb{C}[[t]]$，$K=\mathbb{C}((t))$、$D'_{(\mathfrak{g}\otimes K_x,G(\mathcal{O}_x))}$：临界扭（critically twisted）的完备化包络代数的不变部分、$H_{\nabla}(X,\mathfrak{z})$：$D_X$-模 $\mathfrak{z}$ 的水平（水平截面）整体截面、$h_X:\mathfrak{z}(X)\to\Gamma(\operatorname{Bun}_G,D')$：量子化的 Hitchin 哈密顿量

## 关键点

- 量子化的定义不是「造一个算子」，而是一个三元组：滤交换代数 $\mathfrak{z}(X)$、象征同构 $\sigma_{\mathfrak{z}(X)}:\operatorname{gr}\mathfrak{z}(X)\xrightarrow{\sim}\mathfrak{z}^{cl}(X)$、以及滤代数态射 $h_X$ 使方块 $\sigma_{\operatorname{Bun}_G}\circ\operatorname{gr}h_X=h_X^{cl}\circ\sigma_{\mathfrak{z}(X)}$ 交换（ch02.tex:70-76）。
- 局部构造（2.5）的关键是 Kac--Moody 中心扩张：$\mathfrak{g}\otimes K_x$ 上的余圈取 $\operatorname{Res}_x c(du,v)$，$c(a,b):=-\frac{1}{2}\operatorname{Tr}(\operatorname{ad}_a\cdot\operatorname{ad}_b)$（式 (18)）；它把 $G(\mathcal{O}_x)$ 的作用提升到中心扩张上（式 (19)），使临界扭包络代数的不变部分有良好定义（ch02.tex:161-175）。
- 定理 2.5.2 [FF92]：$\mathfrak{z}_x$ 交换，且扭局部量子化条件成立，即 $\sigma_{\mathfrak{z}_x}:\operatorname{gr}\mathfrak{z}_x\to\mathfrak{z}^{cl}_x$ 是同构——这正是「象征 = 函数」在局部的量子化版本（ch02.tex:184-188）。
- 为什么是「临界」扭：2.5.3 说明 $\omega_{\operatorname{Bun}_G}$ 上的 $(\widehat{\mathfrak{g}\otimes K_x},G(\mathcal{O}_x))$-作用中中心元 $\mathbf{1}$ 作用为乘 $2$（ch02.tex:198-222）；这个 $2$ 与 $D'=D^{1/2}$（$\lambda=1/2$）相配，故扭曲必须是临界的，否则整体截面只剩局部常值函数。
- 整体构造（2.7）：把 $x$ 换成形式圆盘族，$\mathfrak{z}_{\mathfrak{g}}(\mathcal{O}):=D'_{(\mathfrak{g}\otimes K,G(\mathcal{O}))}$ 是 $\operatorname{Aut}\mathcal{O}$-代数，$\mathfrak{z}:=\mathfrak{z}_{\mathfrak{g}}(\mathcal{O})_X$ 的纤维正是 $\mathfrak{z}_x$；水平性定理 2.7.3 说 $h:\mathfrak{z}\to\Gamma(\operatorname{Bun}_G,D')_X$ 是 $D_X$-代数态射，于是可取水平截面（ch02.tex:536-554）。
- 式 (27)：$\mathfrak{z}(X)=\mathfrak{z}_{\mathfrak{g}}(X):=H_{\nabla}(X,\mathfrak{z})$；象征映射 $\sigma_{\mathfrak{z}}:\operatorname{gr}\mathfrak{z}\xrightarrow{\sim}\mathfrak{z}^{cl}$，而 $j:\mathfrak{z}^{cl}(X)=H_{\nabla}(X,\mathfrak{z}^{cl})\longrightarrow\operatorname{gr}\mathfrak{z}(X)$ 是满射。式 (28) 的交换方块说明 $j$ 是同构，于是 $\sigma_{\mathfrak{z}(X)}:=j^{-1}$，三元组解决量子化问题（ch02.tex:558-608）。
- 两条路的关系：2.7.5 用 $h_x=h_X\theta_{\mathfrak{z}_x}$（$\theta$ 满且严格相容滤链）由整体结果推出局部定理 2.5.5；所以 2.5 是「易表述」的版本，2.7 是「完全典范」的版本（ch02.tex:610-621）。

## 公式

```latex
c(a,b):=-\frac{1}{2}\operatorname{Tr}(\operatorname{ad}_a\cdot\operatorname{ad}_b)
```
```latex
\mathbf{1}\mapsto\mathbf{1},\qquad u\mapsto gug^{-1}+\operatorname{Res}_x c(u,g^{-1}dg)\cdot\mathbf{1}
```
```latex
\mathfrak{z}_x=\mathfrak{z}_{\mathfrak{g}}(\mathcal{O}_x):=D'_{(\mathfrak{g}\otimes K_x,G(\mathcal{O}_x))}
```
```latex
\sigma_{\mathfrak{z}_x}:\operatorname{gr}\mathfrak{z}_x\xrightarrow{\sim}\mathfrak{z}^{cl}_x
```
```latex
\mathfrak{z}(X)=\mathfrak{z}_{\mathfrak{g}}(X):=H_\nabla(X,\mathfrak{z})
```
```latex
j:\mathfrak{z}^{cl}(X)=H_\nabla(X,\mathfrak{z}^{cl})\longrightarrow\operatorname{gr}\mathfrak{z}(X)
```
```latex
\sigma_{\operatorname{Bun}_G}\circ\operatorname{gr}h_X=h_X^{cl}\circ\sigma_{\mathfrak{z}(X)}
```

## 定理

定理 2.5.2 [FF92]：$\mathfrak{z}_x$ 交换，且扭局部量子化条件成立，即 $\sigma_{\mathfrak{z}_x}:\operatorname{gr}\mathfrak{z}_x\to\mathfrak{z}^{cl}_x$ 是同构（ch02.tex:184-188，p.24）。

水平性定理 2.7.3：$h:\mathfrak{z}\to\Gamma(\operatorname{Bun}_G,D')_X$ 是 $D_X$-代数态射（ch02.tex:554，p.33）。

定理 2.5.5：上述局部构造满足扭整体量子化条件；于是 $\mathfrak{z}^{(x)}(X):=h_x(\mathfrak{z}_x)$ 的伴随分次同构于 $\mathfrak{z}^{cl}(X)$（ch02.tex:230-239，p.25）。

2.7.4：式 (28) 的交换方块表明 $j$ 是同构，定义 $\sigma_{\mathfrak{z}(X)}:=j^{-1}$ 后 $(\mathfrak{z}(X),\sigma_{\mathfrak{z}(X)},h_X)$ 给出量子化问题的一个解（ch02.tex:596-607，pp.33-34）。

## 常见错误

- 把「量子化」当成给每个 Hitchin 哈密顿量配一个算子：定义要求的是整个滤交换代数 $\mathfrak{z}(X)$ 及其象征同构，单个算子的提升必须与滤链和象征的交换方块相容（式 (28)）。
- 把 $\mathfrak{z}_x$ 与 $\mathfrak{z}(X)$ 混同：前者是形式圆盘处的局部对象（$K_x$、$G(\mathcal{O}_x)$），后者是水平截面 $H_{\nabla}(X,\mathfrak{z})$；$\mathfrak{z}(X)$ 的纤维才是 $\mathfrak{z}_x$，局部到整体要经过水平性定理与式 (28)。
- 忽略「临界」而只写「扭」：中心元 $\mathbf{1}$ 作用为 $2$（2.5.3）与 $D'=D^{1/2}$ 必须匹配；换成别的扭 $D^{\lambda}$（$\lambda\neq 1/2$）后整体截面只剩局部常值函数，量子化构造会塌缩（ch02.tex:20、198-222）。
- 把 $j$ 的满射直接当同构：2.7.4 是先有满射 $j$，再用式 (28) 的交换方块与 $h_X^{cl}$ 的单射性证明它可逆，最后才定义 $\sigma_{\mathfrak{z}(X)}:=j^{-1}$；跳过这一步会把结论当成前提。
- 把水平性当成自动性质：$h$ 是 $D_X$-代数态射（2.7.3）是需要证明的定理，它保证 $\mathfrak{z}$ 是水平 $D_X$-模、从而 $H_{\nabla}(X,\mathfrak{z})$ 可取；没有它，$\mathfrak{z}(X)$ 的定义无从谈起。

## 批注

### 背景直觉：为什么中心扩张会出现

把 $G((t))$ 的作用搬到 $\omega_{\operatorname{Bun}_G}$ 上时会多出射影项（Fock 空间上的正常序），必须用 Kac--Moody 中心扩张把这部分吸收掉；余圈 $c$ 正是这个射影反常。选临界扭 $\lambda=1/2$ 让反常与典范丛的平方根精确抵消，作用才真正下降为 $G((t))$-作用。于是「Hitchin 哈密顿量的量子化」在局部被归结为一个熟知的定理：临界扭包络代数的中心在象征意义下等于 Casimir 不变量。

### 含糊点拨：两种量子化版本的分工

2.5 版本在一个固定点 $x$ 上工作：$\mathfrak{z}_x$ 只在形式圆盘处定义，整体化靠把 $h_x$ 拼起来，叙述短但依赖 $x$ 的选取。2.7 版本把 $x$ 换成整个 $X$ 上的形式圆盘族（$D_X$-概形 $\mathfrak{z}$），再取水平截面 $H_{\nabla}$：这样得到的三元组与 $x$ 无关，是「完全典范」的解。2.7.5 再由整体结果倒推 2.5.5，说明两者给出同一个 $\mathfrak{z}(X)$。

### 易错预警：式 (28) 的交换性方向

式 (28) 是 $\sigma_{\operatorname{Bun}_G}\circ\operatorname{gr}h_X=h_X^{cl}\circ\sigma_{\mathfrak{z}(X)}$：象征在左、分次在右。写反或省略其中一边，都无法说明 $h_X$ 是「量子化」——真正的内容是 $h_X$ 与滤链、象征同时相容。检查时可代 $\mathfrak{z}(X)$ 的生成元：$\operatorname{gr}$ 给出 Hitchin 坐标，$h_X$ 给出扭微分算子，两边作用在 $\operatorname{gr}\Gamma(\operatorname{Bun}_G,D')$ 上应一致。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §2.5；印刷页 [23, 24, 25, 26] / PDF 页 [23, 24, 25, 26]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch02.tex:161-243`
- §2.5 从 p.23 中部开始（`\SourcePage{23}` 在 ch02.tex:141）：式 (18)(19) 与 2.5.1 在 p.23；`\SourcePage{24}` 在 ch02.tex:168，定理 2.5.2 与 2.5.3 起于 p.24；`\SourcePage{25}` 在 ch02.tex:207，2.5.4、2.5.5 在 p.25；`\SourcePage{26}` 在 ch02.tex:241，2.5.5 的末尾落在 p.26。印刷页 = PDF 页。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §2.7；印刷页 [32, 33, 34, 35] / PDF 页 [32, 33, 34, 35]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch02.tex:508-621`
- §2.7 起于 p.32（`\SourcePage{32}` 在 ch02.tex:486）；`\SourcePage{33}` 在 ch02.tex:523，式 (27) 与 2.7.1–2.7.3 在 p.33；`\SourcePage{34}` 在 ch02.tex:563，式 (28) 与 2.7.4 横跨 p.34；`\SourcePage{35}` 在 ch02.tex:616，2.7.5 起于 p.35。印刷页 = PDF 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
