# 标准模 $I(w,\lambda)$

> `mloc/concept/standard-module-i-w-lambda` · type=concept · track=G · status=draft · verification=source-only

**别名**：standard module、$I(w,\lambda)$、$I(\lambda)=\widetilde{M(\lambda)}$、双 Verma 模

## 摘要

Bruhat 胞腔 $C(w)$ 上标准齐性联络的 $i_+$-推前；$\lambda$ 反支配时截面为 $I(w\lambda)$，$w=1$ 时即 $\widetilde{M(\lambda)}$。

## 问题

为什么 $w=1$ 时几何标准模 $I(1,\lambda)$ 的截面是 Verma 模 $M(\lambda)$，而代数侧的 $I(\lambda)$ 却是它的对偶？

## 定义

几何侧：设 $\lambda\in\mathfrak{h}_0^*$，$\mathcal{D}_\lambda=\mathcal{D}_{X,\lambda+\rho}$。$X$ 中的 $N_0$-轨道是 Bruhat 胞腔 $C(w)$（$w\in W$），$\dim C(w)=\ell(w)$，且 $C(s)\subset\partial C(w)$ 蕴含 $\ell(s)<\ell(w)$。$C(w)$ 上存在唯一的不可约 $N_0$-齐性 $(\mathcal{D}_\lambda)_{i_w}$-联络 $\mathcal{O}_{C(w)}$。定义标准模 $I(w,\lambda)=i_{w+}(\mathcal{O}_{C(w)})$（$i_w:C(w)\hookrightarrow X$），它是 $\mathcal{D}_\lambda$-模；其唯一不可约 $\mathcal{D}_\lambda$-子模记 $L(w,\lambda)$。代数侧：置 $I(\lambda)=\widetilde{M(\lambda)}$（对偶 Verma 模），并当 $\lambda$ 反支配时把 $\Gamma(X,I(w,\lambda))$ 也记作 $I(w,\lambda)$——定理 1.14 给出 $\Gamma(X,I(w,\lambda))=I(w\lambda)$。

记号：$C(w)$：$w$ 对应的 Bruhat 胞腔；$i_w:C(w)\hookrightarrow X$；$i_{w+}$：$\mathcal{D}$-模的（奇）直接像；$\mathcal{O}_{C(w)}$：$C(w)$ 上唯一的不可约 $N_0$-齐性 $(\mathcal{D}_\lambda)_{i_w}$-联络；$I(\lambda)=\widetilde{M(\lambda)}$：对偶 Verma 模；$\ell(w)$：$w$ 的长度。

## 要点

- 标准模有两副面孔：几何上它是 $i_{w+}(\mathcal{O}_{C(w)})$（支集为 $\overline{C(w)}$ 的 $\mathcal{D}_\lambda$-模），代数上（$\lambda$ 反支配时）它是 $\Gamma(X,I(w,\lambda))=I(w\lambda)$（最高权模）。局部化定理保证两者由 $\Delta_\lambda$ 与 $\Gamma$ 互逆。
- $w=1$ 的特例：$C(1)=\{1\}$ 是点，$I(1,\lambda)=i_{1+}(\mathbb{C}_{\lambda+\rho})$ 显然不可约。引理 1.15 在 $\lambda$ 反支配时给出 $\Gamma(X,I(1,\lambda))=M(\lambda)=L(\lambda)=I(\lambda)$——注意这里的 $M(\lambda)$ 与 $I(\lambda)$ 在反支配时重合，一般情形 $I(\lambda)=\widetilde{M(\lambda)}$ 与 $M(\lambda)$ 不同。
- 方向要小心：几何 $I(1,\lambda)$ 的截面是 $M(\lambda)$（Verma 模），而代数 $I(\lambda)$ 是 $M(\lambda)$ 的对偶。两者用同一字母 $I$ 是书中的记号习惯，$w=1$ 且 $\lambda$ 反支配时才通过 $M(\lambda)=I(\lambda)$ 汇合。
- 定理 1.14 是标准模理论的主定理：$\lambda$ 反支配时，标准层 $I(w,\lambda)$ 的截面恰是最高权模 $I(w\lambda)$，与 $w$ 无关地由 $w\lambda$ 决定。证明先把 $w$ 化到 $w_0$（引理 1.16 与推论 1.17），再用 $C(w_0)$ 仿射开导致的上同调消没（引理 1.18）与几何平移。
- 标准模带正合列：引理 1.22 对 $p=-\alpha^\vee(\lambda)\in\mathbb{Z}$、$w=w's_\alpha$、$\ell(w)=\ell(w')+1$ 给出 $0\to U^0(I(w',s_\alpha\lambda))\to I(w,\lambda)\to I(w',\lambda)\to0$，其中 $U^0\neq0$ 是 $p_\alpha^+(V)$ 型模的平移。这条正合列是计算合成重数与证明不可约性判据（定理 1.23）的工具。
- $w=w_0$ 时 $C(w_0)$ 是仿射开胞腔，故 $p>0$ 时 $H^p(X,I(w_0,\lambda))=H^p(C(w_0),\mathcal{O}_{C(w_0)})=0$（引理 1.18(i)），截面为 $I(w_0\lambda)$（引理 1.18(ii)）；这是定理 1.14 的起点。

## 公式

$$I(w,\lambda)=i_{w+}(\mathcal{O}_{C(w)}),\qquad L(w,\lambda)\ \text{为}\ I(w,\lambda)\ \text{的唯一不可约}\ \mathcal{D}_\lambda\text{-子模}$$

$$\Gamma(X,I(w,\lambda))=I(w\lambda)\qquad(\lambda\ \text{反支配})$$

$$I(\lambda)=\widetilde{M(\lambda)},\qquad \Gamma(X,I(1,\lambda))=M(\lambda)=L(\lambda)=I(\lambda)\ (\lambda\ \text{反支配})$$

$$H^p(X,I(w_0,\lambda))=0\ (p>0),\qquad \Gamma(X,I(w_0,\lambda))=I(w_0\lambda)$$

$$0\to U^0(I(w',s_\alpha\lambda))\to I(w,\lambda)\to I(w',\lambda)\to0$$

## 相关定理

### 定理 1.14（§5.1：标准模的截面）

设 $\lambda\in\mathfrak{h}_0^*$ 是反支配的。则对一切 $w\in W$ 有 $\Gamma(X,I(w,\lambda))=I(w\lambda)$。

证明状态：`sketch`

1. 用引理 1.16（$LI_w(\mathcal{D}(I(1,\lambda)))=\mathcal{D}(I(w^{-1},w\lambda))$）与推论 1.17，取 $w'=w_0w$ 把 $\Gamma(X,I(w,\lambda))$ 化到 $\Gamma(X,I(w_0,w'\lambda))$ 的形状。
   - 为什么：交织函子 $LI_w$ 把标准层按 $w$ 搬运，且与截面函子交换，故只需处理 $w_0$。
2. 对 $w_0$ 情形：$C(w_0)$ 是 $X$ 中的仿射开子集，故 $p>0$ 时 $H^p(X,I(w_0,\mu))=H^p(C(w_0),\mathcal{O}_{C(w_0)})=0$（引理 1.18(i)）。
   - 为什么：仿射概形的凝聚层上同调在高阶消没；$I(w_0,\mu)$ 是 $C(w_0)$ 上结构层的直接像。
3. 由引理 1.18(ii)，$\Gamma(X,I(w_0,\mu))=I(w_0\mu)$ 对一切 $\mu$ 成立；其证明先取常函数截面 $1\in\Gamma(X,I(w_0,\mu))^{w_0\mu-\rho}$，得非零态射 $I(w_0\mu)\to\Gamma(X,I(w_0,\mu))$。
   - 为什么：常函数是最自然的一维最高权向量；$w_0\mu-\rho$ 正是 $I(w_0\mu)$ 的最高权。
4. 再用几何平移 $I(w_0,\mu+\nu)=I(w_0,\mu)\otimes\mathcal{O}(\nu)$ 与引理 1.12(ii)（唯一不可约子模 + 权空间维数相等 ⟹ 同构），把第 3 步的非零态射提升为同构。
   - 为什么：引理 1.12(ii) 是「由最高权与权空间维数判定标准模」的判别法，几何平移让权空间维数的比较对所有 $\mu$ 一次完成。
5. 把 $w_0$ 情形的结论代回第 1 步，对一切 $w$ 得 $\Gamma(X,I(w,\lambda))=I(w\lambda)$。
   - 为什么：$w'=w_0w$ 与 $w$ 一一对应，$w_0^2=1$。

> 缺口：证明由第 5 章第 1 节后半（`ch05b.tex:6-58`）给出，但依赖三处只引用未重证的结果：L.4.1（标准层的截面或为零或不可约最高权模）、L.5.3（$p_\alpha$ 的直接像与基变换）、以及引理 1.16 与推论 1.17 中的交织函子理论（L.3.x）。

### 引理 1.15（§5.1：点轨道标准模的截面）

设 $\lambda$ 反支配。则 $\Gamma(X,I(1,\lambda))=M(\lambda)=L(\lambda)=I(\lambda)$。

证明状态：`sketch`

1. $I(1,\lambda)=i_{1+}(\mathbb{C}_{\lambda+\rho})$ 是点 $C(1)$ 上的标准层，显然不可约；由 L.4.1，$\Gamma(X,I(1,\lambda))$ 或为不可约最高权模或为 0。
   - 为什么：截面函子把不可约标准层送到不可约对象或零，这是局部化理论的基本性质。
2. 其支集是 $\overline{C(1)}=\{1\}$，排除 0；故截面是不可约最高权模。
   - 为什么：支集非空的标准层其截面非零（否则支集会落到边界并降维）。
3. 作为右 $\mathcal{D}_{-\lambda}$-模，$i_1^*(\mathcal{D}_{-\lambda,C(1)\to X})=U(\mathfrak{g})/\mathfrak{n}_0U(\mathfrak{g})$；再模上 $I_{-\lambda+\rho}$ 得 $\Gamma(X,I(1,\lambda))\cong\mathbb{C}_{-\lambda+\rho}\otimes_{U(\mathfrak{b}_0)}U(\mathfrak{g})$，即 $M(\lambda)$ 的对偶 $I(\lambda)$。
   - 为什么：点轨道上的 $\mathcal{D}$-模截面由 $U(\mathfrak{g})/\mathfrak{n}_0U(\mathfrak{g})$ 给出，模上权 $-\lambda+\rho$ 的扭化正是对偶 Verma 模的张量写法。
4. $\lambda$ 反支配时 $M(\lambda)$ 不可约（定理 1.24），故 $M(\lambda)=L(\lambda)$；其对偶由引理 1.11 仍为 $L(\lambda)$，于是 $\Gamma(X,I(1,\lambda))=M(\lambda)=L(\lambda)=I(\lambda)$。
   - 为什么：反支配保证 $M(\lambda)$ 不可约，自对偶性把 $I(\lambda)$ 拉回 $M(\lambda)$。

> 缺口：第 3 步的 $\mathcal{D}$-模计算依赖 L.4.1 与点轨道直接像的标准公式，书中未逐项展开；第 4 步用定理 1.24，其证明又依赖 1.14 与 1.22，形成一处循环依赖需按原文顺序读（1.15 属于 1.14 之前，原文用独立论证）。

## 易错点

- 记号冲突：$I(w,\lambda)$（标准 $\mathcal{D}_\lambda$-模 / 标准 HC 层）与 $I(\lambda)=\widetilde{M(\lambda)}$（对偶 Verma 模）不是同一个构造；$w=1$ 时由引理 1.15 在 $\lambda$ 反支配下通过 $M(\lambda)=I(\lambda)$ 才汇合。论文里必须写清用的是哪一个。
- **$\rho$ 平移**：$\mathcal{D}_\lambda$ 在书中一律指 $\mathcal{D}_{X,\lambda+\rho}$（`ch02a.tex:130` 有明确校注），所以 $I(w,\lambda)$ 的扭化参数是 $\lambda+\rho$；而截面出的 $I(w\lambda)$ 作为最高权模其最高权是 $w\lambda-\rho$。两处 $\rho$ 的符号必须配套，否则 $w=1$ 时 $\Gamma(X,I(1,\lambda))=M(\lambda)$ 这条就对不上（$M(\lambda)$ 的最高权是 $\lambda-\rho$）。
- 定理 1.14 要求 $\lambda$ 反支配；一般 $\lambda$ 时 $\Gamma(X,I(w,\lambda))$ 可能为零，非零的判据是定理 1.19（$w$ 为左 $W(\lambda)$-陪集最短元）。
- 标准模一般不可约（定理 1.23 判据：$\Sigma_w^+\cap\Sigma_\lambda=\emptyset$ 才不可约）；$I(w,\lambda)$ 与它的唯一不可约子模 $L(w,\lambda)$ 不能混用。
- $I(w,\lambda)$ 的支集是 $\overline{C(w)}$ 而非 $C(w)$；作为 $\mathcal{D}$-模它是闭支集的，虽然构造从开的（胞腔上的）局部系统出发。
- $\dim C(w)=\ell(w)$ 只是胞腔维数；标准层的特征簇落在 $N_K\cap\pi^{-1}(\overline{C(w)})$ 上，不能据此以为 $I(w,\lambda)$ 是「$\ell(w)$ 维的」。

## 相关卡

- `mloc/concept/verma-module`
- `mloc/concept/unique-irreducible-quotient`
- `mloc/concept/duality-and-standard-modules`
- `mloc/concept/harish-chandra-sheaf`
- `mloc/concept/composition-multiplicities`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.1 标准模 $I(w,\lambda)$ 的几何构造与 $L(w,\lambda)$ · p.[97]（PDF [101]） · `源码/chapters/ch05a.tex:191-199（Bruhat 胞腔、$\mathcal{O}_{C(w)}$、$I(w,\lambda)$ 与 $L(w,\lambda)$ 的定义）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.1 定理 1.14 与引理 1.15 · p.[97]（PDF [101]） · `源码/chapters/ch05a.tex:200-212（定理 1.14 的陈述与引理 1.15 及其证明）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.1 引理 1.18（$w_0$ 标准模的上同调与截面） · p.[99]（PDF [103]） · `源码/chapters/ch05b.tex:16-24（引理 1.18 及其证明）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §5.1 引理 1.22（标准模的滤过正合列） · p.[101]（PDF [105]） · `源码/chapters/ch05b.tex:111-118（引理 1.22 的陈述与证明）`
