# Yoneda 嵌入

> `seidel/concept/yoneda-embedding` ｜ track A ｜ draft

**一句话**：把对象 Y 送到右 A∞ 模 hom_A(−,Y) 的全忠实 A∞ 函子；它给出自由（可表示）模，并把线性 A∞ 范畴嵌入 dg 模型。

**自测**：为什么把 Y 换成 hom_A(−,Y)，就能把 A∞ 范畴的问题化成链复形上的线性代数？

## 定义

设 $\mathcal A$ 是非含幺 A∞ 范畴，$\mathcal Q=\mathrm{nu\text{-}mod}(\mathcal A)=\mathrm{nu\text{-}fun}(\mathcal A^{\mathrm{op}},\mathrm{Ch})$ 是右 A∞ 模范畴（p.19）。对每个对象 $Y$，定义右模 $\mathcal Y$：
$$\mathcal Y(X)=\hom_{\mathcal A}(X,Y),\qquad \mu^d_{\mathcal Y}=\mu^d_{\mathcal A},$$
即把 $Y$ 放在最后一个变量上。Yoneda 嵌入 $\mathcal I=\mathcal I_{\mathcal A}:\mathcal A\to\mathcal Q$ 在对象上为 $Y\mapsto\mathcal Y$，在态射上对 $c\in\hom_{\mathcal A}(Y_0,Y_1)$ 给出预模同态
$$\mathcal I^1(c)^d(b,a_{d-1},\ldots,a_1)=\mu^{d+1}_{\mathcal A}(c,b,a_{d-1},\ldots,a_1),$$
高阶项 $\mathcal I^d$（$d\ge2$）由同一公式的显然推广给出（p.21）。
$\mathcal Y$ 叫自由模或可表示模：它由 $Y$ 自由生成，从它出发的映射就是「在 $Y$ 处取值」，这正是 A∞ 版 Yoneda 引理。原书用 $\lambda=\lambda_{\mathcal M}:\mathcal M(Y)\to\hom_{\mathcal Q}(\mathcal Y,\mathcal M)$（式 (1.25)）把这个对应写成显式链映射，并用线性化函子 $L$（注 1.17）刻画 $λ$：$L$ 由 $\mathcal I_{\mathcal A}$ 的拉回与 $\mathcal I_{\mathcal Q}$ 复合而成，是 dg 函子，其像中模同态只有一阶项非零。

记号：$\mathcal Q=\mathrm{nu\text{-}mod}(\mathcal A)$，$\mathcal Y=\mathcal I(Y)$；$b\in\mathcal Y(X_{d-1})=\hom_{\mathcal A}(X_{d-1},Y)$，$a_i\in\hom_{\mathcal A}(X_{i-1},X_i)$。

## 要点

- $\mathcal I$ 是同调全忠实 A∞ 函子（推论 2.13，p.31）：$H(\hom_{\mathcal Q}(\mathcal Y_0,\mathcal Y_1))\cong H(\hom_{\mathcal A}(Y_0,Y_1))$，这就是 Yoneda 引理。
- 自由/可表示：$\lambda_{\mathcal M}$ 给出 $H(\mathcal M(Y))\cong H(\hom_{\mathcal Q}(\mathcal Y,\mathcal M))$——「从 $\mathcal Y$ 出发的映射」等于「$\mathcal M$ 在 $Y$ 处的值」。
- 作为 dg 模型：$\mathcal M_{\mathrm{lin}}(Y)=\hom_{\mathcal Q}(\mathcal Y,\mathcal M)$，$L:\mathcal Q\to\mathcal Q$ 的像中模同态只有一阶项非零，并带自然变换 $l:\mathrm{Id}_{\mathcal Q}\to L$（$l^1=\lambda$，差符号 $(-1)^{|c|}$）。
- 与拉回相容：原书 (1.23) 给出自然变换 $T:\mathcal I_{\mathcal A}\to\mathcal F^*\circ\mathcal I_{\mathcal B}\circ\mathcal F$，故 Yoneda 嵌入在 A∞ 函子下是自然的（p.21）。
- $\mathcal Y$ 与 $Y$ 不是一回事：$\mathcal Y$ 是一个模（一族链复形加高阶作用），$Y$ 只是 $\mathcal A$ 的对象；$\mathcal I$ 也远不是恒等函子。

## 公式

$$\mathcal I:\mathcal A\longrightarrow\mathcal Q=\mathrm{nu\text{-}mod}(\mathcal A),\qquad Y\longmapsto\mathcal Y=\hom_{\mathcal A}(-,Y)$$
$$\lambda_{\mathcal M}(c)^d(b,a_{d-1},\ldots,a_1)=\mu^{d+1}_{\mathcal M}(c,b,a_{d-1},\ldots,a_1)$$
$$\mathcal M_{\mathrm{lin}}(Y)=\hom_{\mathcal Q}(\mathcal Y,\mathcal M),\qquad L:\mathcal Q\longrightarrow\mathcal Q$$

## 定理与证明

### A∞ 版 Yoneda 引理（非含幺形式）

设 $\mathcal A$ 是 c-unital A∞ 范畴，$\mathcal M$ 是 c-unital 右模，$\mathcal Y=\mathcal I(Y)$。则式 (1.25) 的 $\lambda_{\mathcal M}:\mathcal M(Y)\to\hom_{\mathcal Q}(\mathcal Y,\mathcal M)$ 是链映射且是拟同构（引理 2.12）；特别取 $\mathcal M=\mathcal Y_1$，得 $\mathcal I$ 同调全忠实（推论 2.13）。

（sketch；来源：原书 p.21 式 (1.25)、p.22 注 1.17、p.30 引理 2.12 与 p.31 推论 2.13）

1. $\lambda_{\mathcal M}$ 是链映射：$\mu^1_{\mathcal Q}\lambda_{\mathcal M}(c)$ 按 $\mathcal Q$ 的微分公式展开后，正是 $\mu_{\mathcal M}$ 的模关系 (1.19) 在 $d+1$ 阶的左端，而 $\lambda_{\mathcal M}(\mu^1_{\mathcal M}c)$ 是同一式子的另一项。  
   为什么：$c\mapsto\mu^{d+1}_{\mathcal M}(c,\ldots)$ 把 $\mathcal M$ 的微分与 $\mathcal Q$ 的微分对齐；模关系保证 $\mu^1_{\mathcal Q}\lambda=\lambda\mu^1_{\mathcal M}$。
2. $\lambda_{\mathcal M}(c)$ 的一阶分量是 $t^1(b)=\pm\mu^2_{\mathcal M}(c,b)$（$b\in\hom_{\mathcal A}(Y,Y)$），符号由 Koszul 规则给出。  
   为什么：在 (1.25) 中取 $d=1$，即得 $\lambda(c)^1(b)=\mu^2_{\mathcal M}(c,b)$；$c$ 的次数给出 $(-1)^{|c|}$ 型的符号。
3. 在 c-unital 假设下取 $H(\mathcal A)$ 中 $Y$ 的单位类 $[e_Y]$；$c\mapsto t^1([e_Y])$ 给出 $H(\hom_{\mathcal Q}(\mathcal Y,\mathcal M))\to H(\mathcal M(Y))$ 的逆映射（同调层面）。  
   为什么：$[e_Y]$ 是 $\mathcal Y(Y)$ 的同调单位；模同态在同调上由它在单位处的值决定，其余分量由模关系递推。
4. 两步互逆：$\lambda(c)$ 同调为零则 $t^1([e_Y])=[c]$ 为零；反之给定 $t$，它在 $[e_Y]$ 上的值唯一确定 $H(t)$，故 $H(\lambda)$ 是同构。  
   为什么：这正是 Yoneda 引理的核心：从可表示模出发的映射由它在「单位元」上的取值决定；c-unital 保证单位类存在。
5. 取 $\mathcal M=\mathcal Y_1$，得 $H(\hom_{\mathcal Q}(\mathcal Y_0,\mathcal Y_1))\cong H(\hom_{\mathcal A}(Y_0,Y_1))$，即 $\mathcal I$ 全忠实。  
   为什么：全忠实的定义就是 $\hom$ 上的同调同构。

缺口：原书只写下 $\lambda$ 的定义 (1.25) 与两条同调性质 (1.26)、(1.27)，未陈述完整的 Yoneda 引理。非含幺情形下「在单位处取值」需用 c-unital 的同伦单位替代严格单位，这一步的符号与递推未在本书展开；步骤 3–4 的「模同态由单位值决定」也只给了同调层面的论证。

## 易错点

- 不要漏掉 $Y$ 在最后一个变量：$\mathcal Y(X)=\hom_{\mathcal A}(X,Y)$ 是右模（$\mathcal A^{\mathrm{op}}$ 上的函子）；写成 $\hom(Y,X)$ 得到左模，模范畴与 $\lambda$ 的方向都会反。
- $\lambda$ 的符号与顺序：原书 (1.25) 的 $d$ 阶分量用 $\mu^{d+1}$，自变量顺序是 $(c,b,a_{d-1},\ldots,a_1)$；把 $c$ 放到最后或按升序排列会差 Koszul 符号。
- 「自由模」不是「$\mathcal Y$ 作为链复形自由」；自由指的是可表示：$\hom_{\mathcal Q}(\mathcal Y,\mathcal M)\simeq\mathcal M(Y)$，即由 $Y$ 的自由生成性。
- A∞ 版 Yoneda 引理要求 $\mathcal M$ 是 c-unital 模（引理 2.12）；若只假设 $\mathcal A$ 非含幺而不管 $\mathcal M$，$\lambda_{\mathcal M}$ 未必是同调同构。
- $L$（线性化）不是恒等函子，只是带自然变换 $\mathrm{Id}\to L$ 的 dg 函子；它把高阶模同态截断成一阶，故 $\mathcal M_{\mathrm{lin}}$ 与 $\mathcal M$ 只在 A∞ 等价意义下相同。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§1(j)，p.19–19（原书 p.19）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§1(l)，p.21–21（原书 p.21）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§1 注 1.17，p.22–22（原书 p.22）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§2g 引理 2.12、推论 2.13，p.30–31（原书 p.30–31 §2g）

关联：`seidel/concept/a-infinity-category`、`seidel/concept/a-infinity-algebra`、`seidel/concept/karoubi-envelope`

来源说明：原书 p.19（$\mathrm{nu\text{-}mod}$ 的定义）、p.21（Yoneda 嵌入、式 (1.25)）、p.22（注 1.17 的线性化函子）；译者注 A01-14。外部核实：nLab “Yoneda embedding”（https://ncatlab.org/nlab/show/Yoneda+embedding，2026-11-19 访问）称 $\mathcal C\hookrightarrow[\mathcal C^{\mathrm{op}},\mathrm{Set}]$、$c\mapsto\mathrm{Hom}_{\mathcal C}(-,c)$ 是全忠实函子（fully faithful），这正是一阶的 Yoneda 引理。
