# Verma 模

> `mloc/concept/verma-module` · type=concept · track=G · status=draft · verification=source-only

**别名**：Verma module、$M(\lambda)$、广义 Verma 模

## 摘要

$M(\lambda)=U(\mathfrak{g})\otimes_{U(\mathfrak{b}_0)}\mathbb{C}_{\lambda-\rho}$：最高权 $\lambda-\rho$，有唯一极大子模与唯一不可约商。

## 问题

为什么 Verma 模的张量积用 $\mathbb{C}_{\lambda-\rho}$ 而不是 $\mathbb{C}_\lambda$，这个 $-\rho$ 平移究竟在补偿什么？

## 定义

设 $\lambda\in\mathfrak{h}_0^*$。记 $\mathbb{C}_\lambda$ 为由 $\lambda$ 定义的一维 $\mathfrak{b}_0$-模：$\mathfrak{n}_0$ 作用为零，$\mathfrak{h}_0$ 以 $\lambda$ 作用（即 $\xi\cdot1=\lambda(\xi)$）。以 $\lambda$ 为参数的 Verma 模定义为 $M(\lambda)=U(\mathfrak{g})\otimes_{U(\mathfrak{b}_0)}\mathbb{C}_{\lambda-\rho}$，其中 $\rho=\frac12\sum_{\alpha\in\Sigma^+}\alpha$。由 PBW 定理，$M(\lambda)\cong U(\bar{\mathfrak{n}}_0)\otimes_{\mathbb{C}}\mathbb{C}_{\lambda-\rho}$ 是 $\mathfrak{h}_0$-模同构。

记号：$\mathbb{C}_\lambda$：$\mathfrak{b}_0$ 通过 $\lambda$ 作用的一维模（$\mathfrak{n}_0$ 作用为 0）；$\rho$：正根之和的一半；$\bar{\mathfrak{n}}_0$：负根张成的幂零子代数；$N(\lambda)$：$M(\lambda)$ 的唯一极大子模；$L(\lambda)=M(\lambda)/N(\lambda)$。

## 要点

- 平移在张量因子内部：$\lambda$ 是 $M(\lambda)$ 的参数（标号），实际张量的是 $\mathbb{C}_{\lambda-\rho}$。于是 $M(\lambda)$ 的最高权是 $\lambda-\rho$，权空间 $M(\lambda)^{\lambda-\rho}$ 一维。
- 为什么是 $\rho$：$\mathbb{C}_{\lambda-\rho}$ 上的 $\mathfrak{h}_0$ 作用取 $\lambda-\rho$，使得半单元素 $\xi$ 在 $M(\lambda)$ 上的广义特征值整体下移 $\rho(\xi)$——这正是把「Borel 的权重」与「无穷小特征标 $\chi_\lambda$」对齐所需，因为 $\chi_\lambda$ 由 $\lambda+\rho$ 决定（Harish-Chandra 同态的平移 $\lambda\mapsto\lambda+\rho$）。
- 同一约定贯穿几何侧：$\mathcal{D}_\lambda$ 在书中一律指 $\mathcal{D}_{X,\lambda+\rho}$（$\mathcal{D}_{X,\lambda+\rho}$ 的扭化），不是 $\mathcal{D}_{X,\lambda}$；因此「$\lambda$ 标记的 Verma 模」与「$\lambda$ 标记的 $\mathcal{D}$-模」在几何上对应同一参数，正因为两处都做了 $+\rho$ / $-\rho$ 的补偿。
- 由 PBW 同构，$M(\lambda)$ 的权恰为 $\lambda-\rho-\nu$（$\nu$ 为若干正根之和），且一维权空间 $M(\lambda)^{\lambda-\rho}$ 生成整个 $M(\lambda)$，故任何真子模都不含它；由此得唯一极大子模 $N(\lambda)$ 与唯一不可约商 $L(\lambda)$。
- 对偶 $I(\lambda)=\widetilde{M(\lambda)}$（「双 Verma 模」）有唯一不可约子模 $L(\lambda)$，是标准模 $I(w,\lambda)$ 在 $w=1$ 的特例；$M(\lambda)$ 与 $I(\lambda)$ 在 $\lambda$ 反支配时重合（引理 1.15）。
- 定理 1.24：$M(\lambda)$ 不可约当且仅当 $\lambda$ 反支配（$\alpha^\vee(\lambda)\notin\mathbb{Z}_{>0}$ 对一切 $\alpha\in\Sigma^+$）。

## 公式

$$M(\lambda)=U(\mathfrak{g})\otimes_{U(\mathfrak{b}_0)}\mathbb{C}_{\lambda-\rho}$$

$$M(\lambda)\cong U(\bar{\mathfrak{n}}_0)\otimes_{\mathbb{C}}\mathbb{C}_{\lambda-\rho}\qquad(\mathfrak{h}_0\text{-模同构})$$

$$M(\lambda)^{\lambda-\rho}=\mathbb{C}\cdot(1\otimes1),\qquad \mathrm{wt}\,M(\lambda)\subset\lambda-\rho-\mathbb{N}\Sigma^+$$

$$M(\lambda)\twoheadrightarrow L(\lambda)=M(\lambda)/N(\lambda)$$

$$Z(\mathfrak{g})\ \text{通过}\ \chi_\lambda\ \text{作用在}\ M(\lambda)\ \text{上}$$

## 相关定理

### 引理 1.5（§5.1：Verma 模的权结构与唯一极大子模）

设 $\lambda\in\mathfrak{h}_0^*$。则：(i) $M(\lambda)$ 的权都形如 $\lambda-\rho-\nu$，其中 $\nu$ 是若干正根之和；(ii) $\dim M(\lambda)^{\lambda-\rho}=1$；(iii) $M(\lambda)$ 有唯一极大 $\mathfrak{g}$-子模 $N(\lambda)$；(iv) $N(\lambda)^{\lambda-\rho}=0$。

证明状态：`complete`

1. 由 PBW 定理，$U(\mathfrak{g})=U(\bar{\mathfrak{n}}_0)U(\mathfrak{b}_0)$，故乘法诱导 $\mathfrak{h}_0$-模同构 $M(\lambda)=U(\mathfrak{g})\otimes_{U(\mathfrak{b}_0)}\mathbb{C}_{\lambda-\rho}\cong U(\bar{\mathfrak{n}}_0)\otimes_{\mathbb{C}}\mathbb{C}_{\lambda-\rho}$。
   - 为什么：PBW 把 $U(\mathfrak{g})$ 分解为负根、Cartan、正根三部分的张量积；$\mathfrak{b}_0=\mathfrak{h}_0\oplus\mathfrak{n}_0$ 的部分已被张量消去。
2. $U(\bar{\mathfrak{n}}_0)$ 由负根向量张成，每个负根把 $\mathfrak{h}_0$-权降低一个正根，故 $M(\lambda)$ 的权都形如 $\lambda-\rho-\nu$，$\nu$ 为若干正根之和——(i) 成立。
   - 为什么：$\bar{\mathfrak{n}}_0$ 的权都是负根之和；张量因子 $\mathbb{C}_{\lambda-\rho}$ 的权是 $\lambda-\rho$。
3. 在 $\nu=0$ 处，$U(\bar{\mathfrak{n}}_0)$ 中唯一的权零元素是常数，故 $M(\lambda)^{\lambda-\rho}=\mathbb{C}\cdot(1\otimes1)$，一维——(ii) 成立。
   - 为什么：PBW 基中权为 0 的单项式只有空单项式。
4. 该一维子空间生成整个 $M(\lambda)$（它是循环模，循环向量即 $1\otimes1$），故任何真子模都不含它；于是每个真子模都含于 $\bigoplus_{\nu\neq0}M(\lambda)^{\lambda-\rho-\nu}$。
   - 为什么：若真子模含循环向量则它等于整个模。
5. 取极大真子模 $M$。若 $N$ 是另一真子模且 $N\not\subset M$，则 $M+N=M(\lambda)$，于是 $(M+N)^{\lambda-\rho}=M(\lambda)^{\lambda-\rho}\neq0$；但 $M^{\lambda-\rho}=N^{\lambda-\rho}=0$，矛盾。故 $M$ 唯一——(iii) 与 (iv) 同时成立。
   - 为什么：极大性迫使 $M+N$ 等于全模；而两个真子模在最高权处都为零，其和的最高权空间也是零，这是矛盾。

### 引理 1.7（§5.1：中心特征标）

对一切 $\lambda\in\mathfrak{h}_0^*$，$Z(\mathfrak{g})$ 通过 $\chi_\lambda$ 作用在 $M(\lambda)$ 上，即 $z\cdot m=\chi_\lambda(z)m$（$z\in Z(\mathfrak{g})$，$m\in M(\lambda)$）。

证明状态：`complete`

1. 由 Harish-Chandra 同态，$Z(\mathfrak{g})\subset U(\mathfrak{h}_0)\oplus U(\mathfrak{g})\mathfrak{n}_0$；写 $z=\gamma(z)+u$，$\gamma(z)\in U(\mathfrak{h}_0)$，$u\in U(\mathfrak{g})\mathfrak{n}_0$。
   - 为什么：这是 Harish-Chandra 同态的基本性质，把中心元素沿 $U(\mathfrak{g})\mathfrak{n}_0$ 投影到 $U(\mathfrak{h}_0)$。
2. $u$ 作用在循环向量 $1\otimes1$ 上为零，因为 $\mathfrak{n}_0$ 作用在 $\mathbb{C}_{\lambda-\rho}$ 上为零、而 $\mathfrak{n}_0$ 是 Borel 的理想，$U(\mathfrak{g})\mathfrak{n}_0$ 把 $\mathbb{C}_{\lambda-\rho}$ 送到 0。
   - 为什么：$\mathfrak{n}_0\cdot\mathbb{C}_{\lambda-\rho}=0$ 且 $\mathfrak{n}_0$ 是 $\mathfrak{b}_0$ 的理想，故 $U(\mathfrak{g})\mathfrak{n}_0\otimes\mathbb{C}_{\lambda-\rho}=0$。
3. $\gamma(z)\in U(\mathfrak{h}_0)$ 通过 $\lambda-\rho$ 作用在 $1\otimes1$ 上；而 $\chi_\lambda(z)=\gamma(z)(\lambda)$（Harish-Chandra 同态定义中的 $+\rho$ 平移），故 $z\cdot(1\otimes1)=\chi_\lambda(z)(1\otimes1)$。
   - 为什么：这正是 $\rho$ 平移出现的地方：$\chi_\lambda$ 是 $\gamma$ 在 $\lambda+\rho$ 处的取值，而 $M(\lambda)$ 的张量因子是 $\lambda-\rho$，两者相差 $\rho$ 恰好抵消。
4. $M(\lambda)$ 由 $1\otimes1$ 生成且 $Z(\mathfrak{g})$ 是中心的（与 $\mathfrak{g}$ 作用交换），故 $z$ 在整个 $M(\lambda)$ 上按 $\chi_\lambda(z)$ 作用。
   - 为什么：中心元素与所有 $\mathfrak{g}$-作用交换，故由循环向量上的作用决定整体作用。

### 定理 1.24（§5.1：Verma 模不可约的判别）

$M(\lambda)$ 不可约，当且仅当 $\lambda$ 是反支配的（即对一切 $\alpha\in\Sigma^+$，$\alpha^\vee(\lambda)$ 都不是严格正整数）。

证明状态：`sketch`

1. 设 $\lambda$ 反支配。由定理 1.14（$\Gamma(X,I(w,\lambda))=I(w\lambda)$）与引理 1.15 得 $I(\lambda)=\Gamma(X,I(1,\lambda))$，而 $I(1,\lambda)$ 不可约（它是点轨道上的标准层，由 $\mathcal{O}_{C(1)}$ 给出）；由 L.4.1，其截面或为零或不可约，支集排除零，故 $I(\lambda)$ 不可约。
   - 为什么：把 Verma 模的对偶实现为点轨道标准层的截面，是局部化理论的直接应用。
2. 取对偶得 $M(\lambda)=\widetilde{I(\lambda)}$ 不可约，因为不可约模的对偶不可约（引理 1.11 的论证）。
   - 为什么：$\widetilde{\cdot}$ 是正合反变函子且 $\widetilde{\widetilde{V}}\cong V$，故把不可约对象送到不可约对象。
3. 反之设 $M(\lambda)$ 不可约。取最短的 $w$ 使 $w^{-1}\lambda$ 反支配，由 1.14 得 $\Gamma(X,I(w,w^{-1}\lambda))=I(\lambda)=L(\lambda)=M(\lambda)$。
   - 为什么：若 $\lambda$ 非反支配，这样的 $w\neq1$ 存在；$\lambda$ 反支配时结论已由第 1 步给出。
4. 对 $w\neq1$ 取单反射分解 $w=w's_\alpha$（$\ell(w)=\ell(w')+1$），用引理 1.22 的正合列 $0\to U^0(I(w',s_\alpha(w^{-1}\lambda)))\to I(w,w^{-1}\lambda)\to I(w',w^{-1}\lambda)\to0$；由 C.3.2 得 $\Gamma(X,U^0)=0$，从而 $I(\lambda)\cong I(s_{w'\alpha}\lambda)$。
   - 为什么：截面函子正合且把 $I(w,\cdot)$ 送到 $I(\cdot)$；$U^0$ 的截面为零说明 $\Gamma$ 穿过中间的满射。
5. 取对偶得 $M(\lambda)\cong M(s_{w'\alpha}\lambda)$，这只在 $s_{w'\alpha}\lambda=\lambda$ 时可能；但 $\alpha^\vee(w^{-1}\lambda)\in\mathbb{N}$ 与 $\lambda$ 的选取矛盾。
   - 为什么：$M(\mu)$ 的最高权 $\mu-\rho$ 决定 $\mu$（引理 1.5(ii)），故 $M(\lambda)\cong M(s_{w'\alpha}\lambda)$ 迫使参数相等；而反支配性给出 $\alpha^\vee(w^{-1}\lambda)>0$。

> 缺口：证明依赖三处第 5 章只引用未重证的结果：定理 1.14（$\lambda$ 反支配时 $\Gamma(X,I(w,\lambda))=I(w\lambda)$）、引理 1.22（单反射的滤过正合列）与 C.3.2（$U^0$ 的截面消没）；其中 1.14 本身的证明又用 L.4.1 与 L.5.3。

## 易错点

- **$\rho$ 平移**：$M(\lambda)=U(\mathfrak{g})\otimes_{U(\mathfrak{b}_0)}\mathbb{C}_{\lambda-\rho}$，最高权是 $\lambda-\rho$ 而不是 $\lambda$；把「$M(\lambda)$ 的最高权」写成 $\lambda$ 是最常见的错误，且会连锁地把 $L(\lambda)$ 的最高权、$\mathfrak{n}$-同调的平移全部算错。
- 平移的理由必须配套读：$\chi_\lambda$ 由 Harish-Chandra 同态在 $\lambda+\rho$ 处给出，而 $M(\lambda)$ 的张量因子是 $\lambda-\rho$；两者相差 $\rho$ 恰好抵消。几何侧的 $\mathcal{D}_\lambda=\mathcal{D}_{X,\lambda+\rho}$ 是同一约定的另一半——两处都用「$\lambda$」作为统一标号。
- $M(\lambda)$ 一般不可约：只有 $\lambda$ 反支配时才是（定理 1.24）。不要把「$M(\lambda)$ 有唯一不可约商」误读成「$M(\lambda)$ 不可约」。
- 反支配是 $\alpha^\vee(\lambda)\notin\mathbb{Z}_{>0}$（可以等于 0 或负），不是「严格负」；$\lambda=0$ 就是反支配的，此时 $M(0)$ 不可约。
- $\mathbb{C}_\lambda$ 里 $\mathfrak{n}_0$ 作用为零、$\mathfrak{h}_0$ 以 $\lambda$ 作用；张量后 $\mathfrak{h}_0$ 在 $1\otimes1$ 上的作用值是 $\lambda-\rho$。别把 $\mathbb{C}_\lambda$ 的 $\lambda$ 与 $M(\lambda)$ 的权混为一谈。
- Verma 模不是有限维的（$\dim U(\bar{\mathfrak{n}}_0)=\infty$），虽然它是循环模、由一维最高权空间生成。

## 相关卡

- `mloc/concept/highest-weight-module`
- `mloc/concept/unique-irreducible-quotient`
- `mloc/concept/standard-module-i-w-lambda`
- `mloc/concept/duality-and-standard-modules`
- `mloc/concept/highest-weight-category`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.1 Verma 模的定义、引理 1.5 与 $L(\lambda)$ 的构造 · p.[94, 95]（PDF [98, 99]） · `源码/chapters/ch05a.tex:72-92（$M(\lambda)$ 的定义、引理 1.5 及其证明、唯一不可约商 $L(\lambda)$）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.1 引理 1.7（中心特征标） · p.[95]（PDF [99]） · `源码/chapters/ch05a.tex:105-109（引理 1.7 及其证明）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.1 定理 1.24（$M(\lambda)$ 不可约 $\iff$ $\lambda$ 反支配） · p.[102]（PDF [106]） · `源码/chapters/ch05b.tex:172-178（定理 1.24 及其证明）`
