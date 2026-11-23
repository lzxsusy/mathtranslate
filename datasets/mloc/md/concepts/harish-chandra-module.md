# Harish-Chandra 模

> `mloc/concept/harish-chandra-module` · type=concept · track=F · status=draft · verification=source-only

**别名**：Harish-Chandra module、$(\mathfrak{g},K)$-模、HC 模、$K$-有限的 $\mathfrak{g}$-模

## 摘要

同时是有限生成 $U(\mathfrak{g})$-模、$Z(\mathfrak{g})$-局部有限模与代数 $K$-模，且两种作用满足相容律；按无穷小特征标分层为 $\mathcal{M}_{fg}(U_\theta,K)$。

## 问题

Harish-Chandra 模的三条要求各自负责什么，为什么三者合起来就能推出模有有限长度？

## 定义

设 $(\mathfrak{g},K)$ 是 Harish-Chandra 对。Harish-Chandra 模 $V$ 是一个向量空间，满足：(i) $V$ 是有限生成 $U(\mathfrak{g})$-模，且作为 $Z(\mathfrak{g})$-模是局部有限的；(ii) $V$ 是代数 $K$-模；(iii) $\mathfrak{g}$ 与 $K$ 的作用相容，即由 $K$-作用的微分给出的 $\mathfrak{k}$-作用与 $\mathfrak{k}\subset\mathfrak{g}$ 所给的作用相同，且 $(\phi(k)\xi)\cdot v=k\cdot\xi\cdot k^{-1}\cdot v$ 对一切 $k\in K$、$\xi\in\mathfrak{g}$、$v\in V$ 成立。态射是既 $U(\mathfrak{g})$-线又 $K$-线的线性映射；范畴记作 $\mathcal{M}_{fg}(U(\mathfrak{g}),K)$。对 $\lambda\in\mathfrak{h}^*$、$\theta=W\cdot\lambda$，把无穷小特征标为 $\chi_\lambda$ 的对象构成的子范畴记作 $\mathcal{M}_{fg}(U_\theta,K)$。

记号：$\mathfrak{h}$：$\mathfrak{g}$ 的 Cartan 子代数；$W$：Weyl 群；$\chi_\lambda$：由 $\lambda\in\mathfrak{h}^*$ 决定的 $Z(\mathfrak{g})$ 的无穷小特征标；$\theta=W\cdot\lambda$：一条 Weyl 群轨道；$U_\theta=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}\mathbb{C}_{\chi_\lambda}$；$\mathcal{D}_\lambda$：旗簇上的扭微分算子层（本书约定 $\mathcal{D}_\lambda=\mathcal{D}_{X,\lambda+\rho}$）。

## 要点

- 三条要求缺一不可：$U(\mathfrak{g})$-模结构负责「有限生成」，$Z(\mathfrak{g})$-局部有限负责「有限多个无穷小特征标」，$K$-结构负责「$K$-有限」；单有代数 $K$-作用而不相容的模不在此范畴内。
- 相容条件 $(\phi(k)\xi)\cdot v=k\cdot\xi\cdot k^{-1}\cdot v$ 说明 $\mathfrak{g}$ 与 $K$ 的作用通过 $\phi$ 缠在一起：$K$ 通过 $\phi$ 作用在 $\mathfrak{g}$ 上，因此 $V$ 是真正的 $(\mathfrak{g},K)$-模，而不是两个独立结构直和。
- 「代数 $K$-模」是局部有限性的要求：每个向量生成的 $K$-子模有限维，且 $K$ 的作用是代数的；它等价于 $V$ 是有限维代数 $K$-模的并。
- 因为 $Z(\mathfrak{g})$-局部有限，$V$ 分解为有限多个广义无穷小特征标子模的直和（定理 3.7 证明中的 $P(\xi)$ 论证），故一切问题可逐 $\theta$ 处理。
- 主结论是定理 3.7：每个 Harish-Chandra 模有限长；路线是「按 $Z(\mathfrak{g})$ 分解 → 取反支配 $\lambda$ → 局部化为 Harish-Chandra 层 → 用层完整（定理 3.2）与 $\Gamma$ 正合（L.4.1）拉回」。
- 范畴 $\mathcal{M}_{fg}(U_\theta,K)$ 的 $\theta$ 是 $W$-轨道而非单个权：同一 $\theta$ 中不同的 $\lambda$ 给出同一个 $U_\theta$，这是局部化定理可以逐 $\theta$ 陈述的原因。

## 公式

$$(\phi(k)\xi)\cdot v=k\cdot\xi\cdot k^{-1}\cdot v,\qquad k\in K,\ \xi\in\mathfrak{g},\ v\in V$$

$$V=\bigoplus_{i=1}^{k}V_i,\qquad V_i=\{v\in V\mid(\xi-\chi_{\lambda_i}(\xi))^n v=0\ \text{对一切}\ \xi\in Z(\mathfrak{g})\ \text{与充分大的}\ n\}$$

$$\mathcal{M}_{fg}(U(\mathfrak{g}),K)\supset\mathcal{M}_{fg}(U_\theta,K),\qquad \theta=W\cdot\lambda$$

$$\Delta_\lambda:\mathcal{M}_{fg}(U_\theta,K)\longrightarrow\mathcal{M}_{coh}(\mathcal{D}_\lambda,K)$$

## 相关定理

### 定理 3.7（§4.3：Harish-Chandra 模有限长）

每个 Harish-Chandra 模都是有限长的。

证明状态：`complete`

1. 因 $V$ 作为 $Z(\mathfrak{g})$-模局部有限、作为 $U(\mathfrak{g})$-模有限生成，存在有限个 $\lambda_1,\dots,\lambda_k$ 与 $n$ 使 $P(\xi)=\prod_{i=1}^{k}(\xi-\chi_{\lambda_i}(\xi))^n$ 零化 $V$。
   - 为什么：取生成元的有限维 $Z(\mathfrak{g})$-包 $U$，它在 $U(\mathfrak{g})$ 下生成 $V$；$U$ 上的零化多项式（有限余维理想给出的）提升到整个 $V$。
2. 于是 $V=\bigoplus_{i=1}^{k}V_i$，其中 $V_i$ 是以 $\chi_{\lambda_i}$ 为广义无穷小特征标的子模；只需逐 $V_i$ 证明有限长。
   - 为什么：两两互素的多项式给出算子分解（中国余数），每个 $V_i$ 仍是 Harish-Chandra 模，且有限长的直和有限长。
3. 设 $V$ 被 $(\xi-\chi_\lambda(\xi))^n$ 零化。对生成元 $Z(\mathfrak{g})$-包 $U$ 的维数作归纳：取 $U$ 的一维特征子空间 $U_1$，它生成 Harish-Chandra 子模 $V_1$，商 $V/V_1$ 由维数更小的 $U_2$ 生成。
   - 为什么：得到递降滤过，其各商仍具有无穷小特征标 $\chi_\lambda$；$V_1$ 在 $U(\mathfrak{g})$ 与 $K$ 下都稳定，故是 Harish-Chandra 子模。
4. 于是可设 $V\in\mathcal{M}_{fg}(U_\theta,K)$，并在 $\theta$ 中取反支配的 $\lambda$；局部化 $\Delta_\lambda(V)$ 是 Harish-Chandra 层，由定理 3.2 长度有限。
   - 为什么：反支配的 $\lambda$ 使局部化定理（L.1.3 等）可用；Harish-Chandra 层完整（定理 3.2），而完整 $\mathcal{D}$-模长度有限。
5. 由 L.1.1 有 $V=\Gamma(X,\Delta_\lambda(V))$；$\Gamma$ 正合（L.4.1），故 $V$ 长度有限。
   - 为什么：正合函子把合成列拉成合成列，长度不增；于是层的有限长度回推为模的有限长度。

### 引理 3.1（§4.3：Harish-Chandra 层的良滤过）

任一 Harish-Chandra 层 $\mathcal{V}$ 都有良滤过 $F\mathcal{V}$，其中每一项都是 $K$-齐性凝聚 $\mathcal{O}_X$-模。

证明状态：`complete`

1. 用 $\mathcal{O}(\mu)$（$\mu$ 充分负）作扭，可设 $\lambda$ 反支配且正则；此时由 L.1.3 有 $\mathcal{V}=\mathcal{D}_\lambda\otimes_{U_\theta}V$，其中 $V=\Gamma(X,\mathcal{V})$。
   - 为什么：扭是范畴等价，不改变 $K$-等变性与凝聚性，只把参数移到反支配正则的位置，使 $\mathcal{V}$ 由其整体截面生成。
2. 取有限维 $K$-不变子空间 $U\subset V$，使 $U$ 在 $U_\theta$ 下生成 $V$。
   - 为什么：$V$ 既是有限生成 $U_\theta$-模又是代数 $K$-模，故可把一组生成元在 $K$ 下取有限维包。
3. 令 $F_p\mathcal{V}$ 为自然映射 $F_p\mathcal{D}_\lambda\otimes_\mathbb{C}U\to\mathcal{V}$ 的像，则每个 $F_p\mathcal{V}$ 都是 $\mathcal{V}$ 的 $K$-齐性凝聚 $\mathcal{O}_X$-子模。
   - 为什么：$F_p\mathcal{D}_\lambda$ 是 $K$-齐性凝聚 $\mathcal{O}_X$-模，而 $K$-等变映射的像是 $K$-齐性凝聚的。
4. 该滤过是 $\mathcal{D}_\lambda$-模滤过、穷尽，且 $F_p\mathcal{D}_\lambda\,F_q\mathcal{V}=F_{p+q}\mathcal{V}$，故是良滤过。
   - 为什么：穷尽性：任一整体截面 $v=\sum_i T_i u_i$，取 $p$ 使所有 $T_i\in\Gamma(X,F_p\mathcal{D}_\lambda)$，则 $v\in F_p\mathcal{V}$；乘法律由构造直接得到。

## 易错点

- 「$K$-有限」不等于「$K$ 作用可对角化」：代数 $K$-模只要求每个向量生成的 $K$-子模有限维；$K$ 不连通时不可约 $K$-模未必一维，$K$-类型可以带重数。
- 第 (i) 条中的「$Z(\mathfrak{g})$-局部有限」不能换成「$Z(\mathfrak{g})$-有限型」或只在生成元上验证：局部有限指每个向量都被 $Z(\mathfrak{g})$ 的某个有限余维理想零化，这正是「有限多个无穷小特征标」的来源。
- Harish-Chandra 模不必是 $K$-半单的：定理 3.7 只给有限长，$K$-类型可以出现重数；把 HC 模当作「代数 $K$-模的直和」会丢掉 $\mathfrak{g}$-作用的信息。
- 相容条件里的 $\phi(k)\xi$ 是 $\operatorname{Int}(\mathfrak{g})$ 中的元素作用在 $\xi$ 上，等价地 $k\cdot(\xi v)=(k\xi k^{-1})\cdot(kv)$；漏掉 $\phi$ 会把 $K$ 的作用误当成与 $\mathfrak{g}$ 交换。
- 范畴 $\mathcal{M}_{fg}(U_\theta,K)$ 按 Weyl 群轨道 $\theta$ 分层；$\chi_\lambda$ 的标签 $\lambda$ 可以换 $\theta$ 中任一权，但 $\theta$ 本身不能换。

## 相关卡

- `mloc/concept/harish-chandra-pair`
- `mloc/concept/harish-chandra-sheaf`
- `mloc/concept/hc-modules-and-hc-sheaves`
- `dmod/concept/holonomic-module`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §4.3 Harish-Chandra 模与 Harish-Chandra 层（定义、范畴、引理 3.1、定理 3.2） · p.[87, 88]（PDF [91, 92]） · `源码/chapters/ch04.tex:102-131（HC 模的三条定义、$\mathcal{M}_{fg}(U_\theta,K)$ 的记号、引理 3.1、定理 3.2）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §4.3 定理 3.7（Harish-Chandra 模有限长） · p.[89, 90]（PDF [93, 94]） · `源码/chapters/ch04.tex:188-200（定理 3.7 及其证明）`
