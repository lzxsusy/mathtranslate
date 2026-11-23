# Kazhdan–Lusztig 算法（Verma 模合成重数的计算）

> `mloc/concept/kazhdan-lusztig-algorithm` · type=concept · track=G · status=draft · verification=source-only

**别名**：Kazhdan–Lusztig 多项式、KL 多项式、$T_\alpha$ 算子、Kazhdan–Lusztig 算法

## 摘要

用 $H$ 上的 $T_\alpha$ 递推定义 KL 多项式 $P_{wv}$，再由 $\nu(-1)$ 过 Grothendieck 群把 Verma 模合成重数化为矩阵求逆。

## 问题

Verma 模 $M(-w\rho)$ 中不可约模 $L(-v\rho)$ 的重数，怎样由 Kazhdan–Lusztig 多项式算出来？

## 定义

设 $(W,S)$ 是约化根系 $\Sigma$ 的 Weyl 群，$\ell$ 为长度函数，$\Pi$ 为单根集。令 $H=\bigoplus_{w\in W}\mathbb{Z}[q,q^{-1}]\delta_w$。对 $\alpha\in\Pi$ 定义 $H$ 的 $\mathbb{Z}[q,q^{-1}]$-线性自同态 $T_\alpha$：当 $\ell(ws_\alpha)=\ell(w)+1$ 时 $T_\alpha(\delta_w)=q\delta_w+\delta_{ws_\alpha}$，当 $\ell(ws_\alpha)=\ell(w)-1$ 时 $T_\alpha(\delta_w)=q^{-1}\delta_w+\delta_{ws_\alpha}$。Kazhdan–Lusztig 多项式是满足定理 2.1 两条件的唯一函数 $\phi:W\to H$ 的系数：$\phi(w)=\delta_w+\sum_{v<w}P_{wv}\delta_v$，其中 $P_{wv}\in q\mathbb{Z}[q]$。几何侧：$i_w:C(w)\hookrightarrow X$ 是 Bruhat 胞腔的嵌入，$\nu(F)=\sum_{w}\sum_{m}\dim_{\mathbb{C}}\bigl(R^mi_w^!(F)\bigr)q^m\delta_w$，并置 $I_w=I(w,-\rho)$、$L_w=L(w,-\rho)$。

记号：$H$：以 $\delta_w$ 为基的 $\mathbb{Z}[q,q^{-1}]$-模；$T_\alpha$：$\alpha$-算子；$P_{wv}$：KL 多项式；$\nu:\mathcal{M}_{coh}(\mathcal{D}_X,N_0)\to H$；$I_w$、$L_w$：标准与不可约 $(\mathcal{D}_X,N_0)$-模；$\chi$：到 Grothendieck 群的映射；$\mu_{wv}$：$\lambda_{wv}=P_{wv}(-1)$ 的逆矩阵系数。

## 要点

- $T_\alpha$ 是 $H$ 的 $\mathbb{Z}[q,q^{-1}]$-线性自同态，两条分支由 $\ell(ws_\alpha)=\ell(w)\pm1$ 决定；关键恒等式是 $\iota T_\alpha\iota=-T_\alpha$，其中 $\iota(q^m\delta_w)=(-1)^{m+\ell(w)}q^m\delta_w$。
- 定理 2.1（存在唯一性）：满足 (i) $\phi(w)=\delta_w+\sum_{v<w}P_{wv}\delta_v$（$P_{wv}\in q\mathbb{Z}[q]$）与 (ii) $T_\alpha(\phi(ws_\alpha))=\sum_{v\le w}c_v\phi(v)$（$\ell(ws_\alpha)=\ell(w)-1$，$c_v\in\mathbb{Z}$）的 $\phi$ 存在且唯一；唯一性由引理 2.3 对长度归纳得到。
- 引理 2.4（奇偶性）：$P_{wv}=q^{\ell(w)-\ell(v)}Q_{wv}$，$Q_{wv}\in\mathbb{Z}[q^2,q^{-2}]$；这是 $\iota$ 对合与唯一性的直接推论。
- 存在性走几何路线：命题 2.5 证明 $\phi(w)=\nu(L_w)$ 满足 2.1 的两条。引理 2.6 用 Kashiwara 定理算得 $\nu(L_w)=\sum_{v\le w}P_{wv}\delta_v$；引理 2.7 用 $U^q_\alpha(F)=p_\alpha^+\bigl(R^qp_{\alpha+}(F)\bigr)$ 的消没与半单性做长度归纳。
- 定理 2.10：$\chi(L_w)=\chi(I_w)+\sum_{v<w}P_{wv}(-1)\chi(I_v)$；证明只用两条：引理 2.8（$\nu(-1)$ 过 Grothendieck 群分解）与引理 2.9（$\nu(I_w)=\delta_w$）。
- 推论 2.11（算法）：令 $\lambda_{wv}=P_{wv}(-1)$，$\mu_{wv}$ 为其逆矩阵系数，则 $L(-v\rho)$ 在 $M(-w\rho)$ 中的重数 $=\mu_{wv}$；矩阵按 Bruhat 序下三角、对角为 $1$，故算法就是矩阵求逆。推论 2.12 给系数非负，引理 2.13 给 $qP_{wv}=P_{w,vs_\alpha}$。
- 与 §5.1 命题 1.8 的分工：1.8 只保证最高权模有限长，即合成列存在、重数有定义；本节才把重数算成 KL 多项式的矩阵逆。故本卡的算法以 1.8 为前提，但结论 $[M(-w\rho):L(-v\rho)]=\mu_{wv}$ 不能由 1.8 推出。

## 公式

$$$T_\alpha(\delta_w)=q\delta_w+\delta_{ws_\alpha}\ (\ell(ws_\alpha)=\ell(w)+1);\quad T_\alpha(\delta_w)=q^{-1}\delta_w+\delta_{ws_\alpha}\ (\ell(ws_\alpha)=\ell(w)-1)$$$

$$$\iota(q^m\delta_w)=(-1)^{m+\ell(w)}q^m\delta_w,\qquad \iota T_\alpha\iota=-T_\alpha$$$

$$$\phi(w)=\delta_w+\sum_{v<w}P_{wv}\delta_v,\qquad P_{wv}\in q\mathbb{Z}[q],\qquad P_{wv}=q^{\ell(w)-\ell(v)}Q_{wv},\ Q_{wv}\in\mathbb{Z}[q^2,q^{-2}]$$$

$$$\nu(F)=\sum_{w\in W}\sum_{m\in\mathbb{Z}}\dim_{\mathbb{C}}\bigl(R^mi_w^!(F)\bigr)q^m\delta_w,\qquad \nu(L_w)=\sum_{v\leq w}P_{wv}\delta_v,\qquad \nu(I_w)=\delta_w$$$

$$$\chi(L_w)=\chi(I_w)+\sum_{v<w}P_{wv}(-1)\,\chi(I_v)$$$

$$$[M(-w\rho):L(-v\rho)]=\mu_{wv},\qquad \sum_{v}\mu_{wv}P_{vu}(-1)=\delta_{wu}$$$

## 相关定理

### 定理 2.1（KL 多项式的存在唯一性）

存在唯一的函数 $\phi:W\to H$，使 (i) 对 $w\in W$，$\phi(w)=\delta_w+\sum_{v<w}P_{wv}\delta_v$，其中 $P_{wv}\in q\mathbb{Z}[q]$；(ii) 对 $\alpha\in\Pi$ 与满足 $\ell(ws_\alpha)=\ell(w)-1$ 的 $w$，存在 $c_v\in\mathbb{Z}$（依赖于 $\alpha,w$）使 $T_\alpha(\phi(ws_\alpha))=\sum_{v\leq w}c_v\phi(v)$。

证明状态：`sketch`

1. 唯一性化到有限层：对 $k\in\mathbb{N}$ 证明 $W_{\leq k}$ 上满足 2.1.(i)(ii) 的函数至多一个（引理 2.3）。
   - 为什么：把 $W$ 截成 $W_{\leq k}$ 后可以按长度归纳，而 2.1 的解在每个截断上的限制都满足同样的两条。
2. $k=0$ 时 $W_{\leq0}=\{1\}$，由 (i) 得 $\phi(1)=\delta_1$，(ii) 是空条件。
   - 为什么：基底唯一，无待定系数。
3. 设 $\ell(w)=k$，取 $\alpha\in\Pi$ 使 $\ell(ws_\alpha)=k-1$；对 (ii) 在 $q=0$ 处取值，得 $\sum_{v\le w}c_v\delta_v=T_\alpha(\phi(ws_\alpha))(0)$，右端由归纳假设唯一确定，故诸 $c_v$ 唯一。
   - 为什么：$q=0$ 抹掉了 $T_\alpha$ 展开中的 $q$ 项，只剩 $\delta$ 的系数。
4. 由 $c_w=1$ 反解 $\phi(w)=T_\alpha(\phi(ws_\alpha))-\sum_{v<w}c_v\phi(v)$。
   - 为什么：对 $v<y=ws_\alpha$，$T_\alpha(\delta_v)$ 只展开到长度 $\le k-1$ 的基，故 $\delta_w$ 只来自 $T_\alpha(\delta_y)$，系数为 $1$。
5. 存在性：令 $\phi(w)=\nu(L_w)$，由引理 2.6 得 (i)；由函子 $U^q_\alpha$ 的消没与半单性（引理 2.7）配合长度归纳得 $T_\alpha(\phi(ws_\alpha))=\nu(U^0_\alpha(L_{ws_\alpha}))=\sum_{v\le w}c_v\phi(v)$，即 (ii)（命题 2.5）。
   - 为什么：这是把组合递推实现为旗簇上 $(\mathcal{D}_X,N_0)$-模的几何构造：$\nu$ 把 $!$-限制的上同调维数编码成 $H$ 的元素。

> 缺口：第 5 步用到引理 2.7 的证明中的外部输入：$U^q_\alpha$ 与底本 L.5 的函子 $U^q$ 只差一个扭、Kashiwara 定理与分解定理，以及引理 1.25 的非消没性；这些译本只引用、未重证，故本卡按 sketch 处理。

### 定理 2.10（$\chi(L_w)$ 的 KL 展开）

设 $P_{wv}$ 为 $(W,S)$ 的 Kazhdan–Lusztig 多项式，$\chi:\mathcal{M}_{coh}(\mathcal{D}_X,N_0)\to K(\mathcal{M}_{coh}(\mathcal{D}_X,N_0))$ 为自然映射，则 $\chi(L_w)=\chi(I_w)+\sum_{v<w}P_{wv}(-1)\,\chi(I_v)$。

证明状态：`complete`

1. $I_w$ 以 $L_w$ 为唯一不可约子模，其余合成因子为 $L_v$（$v<w$），故 $\{\chi(I_w)\}_{w\in W}$ 构成 $K(\mathcal{M}_{coh}(\mathcal{D}_X,N_0))$ 的一组基。
   - 为什么：三角性：$I_w$ 的合成因子都落在 Bruhat 闭包 $\overline{C(w)}$ 内。
2. 于是可唯一地写 $\chi(L_w)=\sum_{v\leq w}\lambda_{wv}\chi(I_v)$，$\lambda_{wv}\in\mathbb{Z}$。
   - 为什么：用基展开，系数就是 $L_w$ 在标准模递降中的重数。
3. 对两边作用 $\nu(-1)$：由引理 2.8，$\nu(-1)$ 过 Grothendieck 群分解；由引理 2.9，$\nu(I_v)(-1)=\delta_v$；故 $\nu(L_w)(-1)=\sum_{v\le w}\lambda_{wv}\delta_v$。
   - 为什么：把范畴层面的等式降到 $H$ 的元素，才能与 $P_{wv}$ 的定义比较。
4. 与 $\nu(L_w)=\sum_{v\le w}P_{wv}\delta_v$（$P_{ww}=1$）比较 $\delta_v$ 的系数，得 $\lambda_{ww}=1$、$\lambda_{wv}=P_{wv}(-1)$。
   - 为什么：$\nu(L_w)$ 的展开式正是 $P_{wv}$ 的定义，逐系数比较即可。

### 推论 2.11（Verma 模的合成重数）

设 $\lambda_{wv}=P_{wv}(-1)$，$\mu_{wv}$ 为其逆矩阵的系数，则不可约模 $L(-v\rho)$ 在 Verma 模 $M(-w\rho)$ 中的重数等于 $\mu_{wv}$。

证明状态：`sketch`

1. 取与 Bruhat 序相容的 $W$ 上线性序，则 $(\lambda_{wv})$ 下三角且对角为 $1$，故可逆，记逆矩阵系数为 $\mu_{wv}$。
   - 为什么：下三角对角 $1$ 是 2.10 的直接推论，保证算法可执行。
2. 由定理 2.10 解出 $\chi(I_w)=\sum_{v\le w}\mu_{wv}\chi(L_v)$。
   - 为什么：这正是把 $\chi(L)$ 的展开式用矩阵求逆反过来。
3. 在 $\lambda=-\rho$（正则反支配）处把几何侧翻译成代数侧：$\Gamma(X,I_w)=I(w(-\rho))$、$\Gamma(X,L_v)=L(v(-\rho))$，即 $I_w$ 对应 $M(-w\rho)$、$L_v$ 对应 $L(-v\rho)$。
   - 为什么：引理 1.11 与定理 1.14、1.19 保证标准模与 Verma 模、不可约模与 $L(w\lambda)$ 在这些权上逐一对应。
4. 于是 $\chi(I_w)=\sum_{v\le w}\mu_{wv}\chi(L_v)$ 就是 $[M(-w\rho):L(-v\rho)]=\mu_{wv}$。
   - 为什么：在 Grothendieck 群里标准模按不可约模展开的系数正是合成重数。

> 缺口：第 3 步依赖引理 1.11（$\widetilde{L(\lambda)}=L(\lambda)$）、定理 1.14（$\lambda$ 反支配时 $\Gamma(X,I(w,\lambda))=I(w\lambda)$）与定理 1.19（$L(w,\lambda)$ 的截面非消没判据）——这些在译本第 5 章 §1 只到引用层面，未逐一重证，故本卡按 sketch 处理。

## 易错点

- 归一化：注 2.2 明说本节的 $P_{wv}$ 与经典 KL 多项式在归一化上不同。推论 2.11 用的是 $\mu$（$\lambda_{wv}=P_{wv}(-1)$ 的逆矩阵系数），不要未经核对就改写成经典的 $P_{wv}(1)$。
- $T_\alpha$ 的两条分支极易写反：$\ell(ws_\alpha)=\ell(w)+1$ 时系数是 $q$，$\ell(ws_\alpha)=\ell(w)-1$ 时是 $q^{-1}$；且 2.1.(ii) 的右端是 $\sum_{v\le w}c_v\phi(v)$（$c_v\in\mathbb{Z}$），不是 $\sum P_{wv}\phi(v)$。
- $\nu$ 用 $!$-限制 $R^mi_w^!$ 的上同调维数，而 $I_w=R^0i_{w+}(\mathcal{O}_{C(w)})$ 用 $+$-直像；$!$ 与 $+$ 不能互换，二者混用会把 $\nu(I_w)=\delta_w$ 写错。
- ρ 平移：重数公式里的参数是 $-w\rho$ 与 $-v\rho$，而 $M(\lambda)$ 的最高权是 $\lambda-\rho$，故 $M(-w\rho)$ 的最高权是 $-w\rho-\rho$；抄成 $M(w\rho)$ 或把 $\rho$ 丢掉都会整体错位。
- 校注提醒：引理 2.7 的证明把 1.25 引作 1.21、引理 2.13 的证明把 1.25 引作 1.21 与 1.24（译本已加校注），按错号回查会落到无关的零化子定理上。

## 相关卡

- `mloc/concept/composition-multiplicities`
- `mloc/concept/verma-module`
- `mloc/concept/standard-module-i-w-lambda`
- `mloc/concept/duality-and-standard-modules`
- `mloc/concept/highest-weight-module`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.2 Kazhdan–Lusztig 算法（$T_\alpha$ 的定义、定理 2.1、注 2.2、KL 多项式的命名） · p.[104]（PDF [108]） · `源码/chapters/ch05c.tex:1-32（§5.2 开头、$H$ 与 $T_\alpha$ 的定义、定理 2.1、注 2.2、KL 多项式得名）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.2 引理 2.3（唯一性）及证明与校注 · p.[104, 105]（PDF [108, 109]） · `源码/chapters/ch05c.tex:34-67（引理 2.3 的陈述、对长度归纳的唯一性证明、底本 $k>1$ 应作 $k>0$ 的校注）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.2 对合 $i$ 与 $\iota$、引理 2.4（奇偶性）、$\nu$ 与 $L_w$ 的定义 · p.[105, 106]（PDF [109, 110]） · `源码/chapters/ch05c.tex:69-114（$\iota T_\alpha\iota=-T_\alpha$、引理 2.4、$\nu$ 的定义、$I_w=I(w,-\rho)$ 与 $L_w=L(w,-\rho)$）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.2 命题 2.5、引理 2.6、函子 $U^q_\alpha$、引理 2.7 及证明 · p.[106, 107, 108]（PDF [110, 111, 112]） · `源码/chapters/ch05c.tex:116-168（$\phi(w)=\nu(L_w)$ 满足 2.1、引理 2.6、$U^q_\alpha(F)=p_\alpha^+(R^qp_{\alpha+}(F))$、引理 2.7 与校注）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.2 引理 2.8、引理 2.9、定理 2.10、推论 2.11 与算法说明 · p.[110, 111]（PDF [114, 115]） · `源码/chapters/ch05c.tex:262-323（$\nu(-1)$ 过 Grothendieck 群分解、$\nu(I_w)=\delta_w$、$\chi(L_w)$ 的展开、$\mu$ 矩阵与重数公式）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.2 推论 2.12（系数非负）与引理 2.13 及校注 · p.[112]（PDF [116]） · `源码/chapters/ch05c.tex:325-338（推论 2.12、引理 2.13 与底本引用编号之误的校注）`
