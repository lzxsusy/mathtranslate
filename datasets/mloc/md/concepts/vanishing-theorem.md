# 消没定理：$H^i(X,V)=0$（$i>n(\lambda)$）

> `mloc/concept/vanishing-theorem` · type=concept · track=C · status=draft · verification=source-only

**别名**：vanishing theorem、消没定理、第 2 章定理 3.1、上同调的消没界

## 摘要

拟凝聚 $D_\lambda$-模的旗簇上同调在次数超过 $n(\lambda)$ 时全消没；$\lambda$ 反支配时 $n(\lambda)=0$，$\Gamma$ 正合。

## 问题

拟凝聚 $D_\lambda$-模的上同调能持续到多少次？消没界由 $\lambda$ 的什么不变量控制？

## 定义

设 $X=G/B$ 是旗簇，$\lambda\in\mathfrak{h}^*$，$D_\lambda$ 是 $X$ 上的扭微分算子层。消没定理断言：对拟凝聚 $D_\lambda$-模 $V$，上同调 $H^i(X,V)$ 只在 $0\le i\le n(\lambda)$ 内可能非零。这里 $n(\lambda)$ 是 $\lambda$ 的 Weyl 群 $W_\lambda$ 中把 $\lambda$ 送到反支配位置所需的最短长度。

记号：$X=G/B$，$n=\dim X=\operatorname{Card}\Sigma^+$；$W_\lambda=\{w\in W\mid w\lambda-\lambda\in Q(\Sigma)\}$ 是 $\Sigma_\lambda=\{\alpha\in\Sigma\mid\alpha^\vee(\lambda)\in\mathbb{Z}\}$ 的 Weyl 群；$\Sigma_\lambda^+=\Sigma^+\cap\Sigma_\lambda$；$\ell_\lambda$ 是 $(W_\lambda,S_\lambda)$ 的长度函数；$\mathcal{M}_{qc}(D_\lambda)$ 是拟凝聚 $D_\lambda$-模范畴。

## 要点

- 消没界是 $n(\lambda)=\min\{\ell_\lambda(w)\mid w\in W_\lambda,\ w\lambda\ \text{反支配}\}$：用 $\ell_\lambda$（$W_\lambda$ 的长度），不是 $W$ 的长度 $\ell$，也不是 $\dim X$。
- $n(\lambda)=0$ 当且仅当 $\lambda$ 反支配；此时定理就是「$i>0$ 时全消没」，并推出 $\Gamma$ 在 $\mathcal{M}_{qc}(D_\lambda)$ 上正合（第 2 章推论 3.2）。
- 证明先处理反支配情形：取支配权 $\mu$ 使 $H^i(X,G(-\mu))=0$，其存在性由 $\mathcal{O}(-2\rho)$ 的丰富性保证；再由 $i_V$ 的左逆 $j_V$ 夹出 $H^i(\varphi)=0$。
- 一般情形对 $n(\lambda)$ 归纳：第 2 章引理 2.3 给出 $0\to V\to G\to V(p_\alpha)\to0$，其中 $n(\lambda+p_\alpha)<n(\lambda)$，再用上同调长正合列。
- 上同调 $H^i(X,V)$ 带 $U_\theta$-模结构（$\theta=W\cdot\lambda$）；消没界只经 $n(\lambda)$ 依赖 $\lambda$，不单独依赖 $\theta$。

## 公式

$$$H^i(X,V)=0,\qquad i>n(\lambda)$$$

$$$n(\lambda)=\min\{\ell_\lambda(w)\mid w\in W_\lambda,\ w\lambda\ \text{反支配}\}$$$

$$$0\longrightarrow V\longrightarrow G\longrightarrow V(p_\alpha)\longrightarrow 0,\qquad n(\lambda+p_\alpha)<n(\lambda)$$$

$$$G=\bigl(V(-s_\alpha w^{-1}\sigma)\otimes_{\mathcal{O}_X}\mathcal{F}\bigr)[\lambda]$$$

## 相关定理

### 第 2 章定理 3.1（消没定理）

设 $V\in\mathcal{M}_{qc}(D_\lambda)$。则对一切整数 $i>n(\lambda)$ 有 $H^i(X,V)=0$。

证明状态：`complete`

1. 先证 $\lambda$ 反支配（$n(\lambda)=0$）时 $\Gamma$ 在 $\mathcal{M}_{qc}(D_\lambda)$ 上正合，即第 2 章推论 3.2，作为对 $n(\lambda)$ 归纳的底情形。
   - 为什么：$n(\lambda)=0$ 当且仅当 $\lambda$ 反支配；底情形要证的正是 $i>0$ 的全部消没。
2. 对凝聚 $G\subset V$ 取支配权 $\mu$ 使 $H^i(X,G(-\mu))=0$（$1\le i\le\dim X$），并以最高权 $\mu$ 的 $F$ 构造 $i_G:G\to G(-\mu)\otimes\mathcal{F}$。
   - 为什么：$\mathcal{O}(-2\rho)$ 丰富，故存在这样的支配权；$\mathcal{F}=\mathcal{O}_X\otimes F$ 自由，故 $H^i(G(-\mu)\otimes\mathcal{F})=H^i(G(-\mu))\otimes F$。
3. 由第 2 章引理 2.1，$V(-\mu)\otimes\mathcal{F}$ 是 $V$ 与其余项的直和，$i_V$ 有左逆 $j_V$；图表给出 $H^i(i_V)\circ H^i(\varphi)=0$。
   - 为什么：$i_V$ 是直和项的包含，故有左逆；与 $H^i(\varphi)$ 复合后由交换图得零。
4. 于是 $H^i(\varphi)=H^i(j_V)\circ H^i(i_V)\circ H^i(\varphi)=0$；对 $G\subset V$ 取直极限，得一般拟凝聚 $V$ 的 $H^i(X,V)=0$（$i>0$）。
   - 为什么：凝聚子模的直极限是 $V$，且层上同调与直极限交换；故第 2 章推论 3.2 成立。
5. 现设 $n(\lambda)=k>0$，取 $w\in W_\lambda$、$\ell_\lambda(w)=k$、$w\lambda$ 反支配，用第 2 章引理 2.3 得 $0\to V\to G\to V(p_\alpha)\to0$，其中 $G=(V(-s_\alpha w^{-1}\sigma)\otimes\mathcal{F})[\lambda]$。
   - 为什么：第 2 章引理 2.3 的构造同时给出 $n(\lambda+p_\alpha)<k$ 与 $n(\lambda-s_\alpha w^{-1}\sigma)<k$。
6. 对 $G$ 的项用第 2 章引理 2.2 与归纳假设：$i>k-1$ 时 $H^i(X,G)=H^i(X,V(-s_\alpha w^{-1}\sigma))\otimes F$ 的 $[\lambda]$-部分为零；同法得 $H^i(X,V(p_\alpha))=0$。再取长正合列，得 $i>k$ 时 $H^i(X,V)=0$。
   - 为什么：$n(\lambda-s_\alpha w^{-1}\sigma)<k$，故归纳假设可用于扭变后的模；长正合列把两端消没传给中间项。

### 第 2 章推论 3.2（反支配时 $\Gamma$ 正合）

设 $\lambda\in\mathfrak{h}^*$ 反支配。则 $\Gamma:\mathcal{M}_{qc}(D_\lambda)\to\mathcal{M}(U_\theta)$ 是正合函子。

证明状态：`complete`

1. 只需证 $i>0$、$V\in\mathcal{M}_{qc}(D_\lambda)$ 时 $H^i(X,V)=0$；先对凝聚 $G$ 证明。
   - 为什么：$\Gamma$ 左正合；正合性等价于 $i>0$ 的高阶上同调消没。
2. 取支配权 $\mu$ 使 $H^i(X,G(-\mu))=0$（$1\le i\le\dim X$），由 $\mathcal{O}(-2\rho)$ 的丰富性保证存在。
   - 为什么：丰富线丛的高次上同调消没，取足够大的 $\mu$ 即得。
3. 由交换图 $H^i(\varphi(-\mu)\otimes1)\circ H^i(i_G)=H^i(i_V)\circ H^i(\varphi)$ 与 $H^i(i_V)\circ H^i(\varphi)=0$，配合 $i_V$ 的左逆得 $H^i(\varphi)=0$。
   - 为什么：$i_V$ 有左逆 $j_V$，故 $H^i(\varphi)=H^i(j_V)H^i(i_V)H^i(\varphi)=0$。
4. 对 $G\subset V$ 取直极限，得 $H^i(X,V)=0$（$i>0$）。
   - 为什么：层上同调与直极限交换，$V$ 是其凝聚子模的直极限。

### 第 2 章引理 2.3（把 $n(\lambda)$ 降下来的短正合列）

设 $\lambda\in\mathfrak{h}^*$，$n(\lambda)=k>0$，取 $w\in W_\lambda$ 使 $\ell_\lambda(w)=k$、$w\lambda$ 反支配，并写既约表达式 $w=s_{\beta_1}\cdots s_{\beta_k}$。置 $\alpha=w^{-1}\beta_1$、$p_\alpha=-\alpha^\vee(\lambda)$。则对任意 $V\in\mathcal{M}(D_\lambda)$ 存在短正合列 $0\to V\to G\to V(p_\alpha)\to0$，其中 $G=(V(-s_\alpha w^{-1}\sigma)\otimes\mathcal{F})[\lambda]$ 对某个支配权 $\sigma$ 与最高权 $\sigma$ 的 $F$ 取得，且 $n(\lambda+p_\alpha)<k$、$n(\lambda-s_\alpha w^{-1}\sigma)<k$。

证明状态：`sketch`

1. 由 $w\lambda$ 反支配及 $w'=s_{\beta_1}w$ 满足 $w's_\alpha\lambda=w\lambda$，得 $n(s_\alpha\lambda)\le\ell_\lambda(w')=k-1$，即 $n(\lambda+p_\alpha)<k$。
   - 为什么：$s_\alpha\lambda=\lambda+p_\alpha$，而 $w'$ 的长度比 $w$ 少一。
2. 取 $\sigma\in P(\Sigma)\cap C_\lambda$ 使 $\beta_1^\vee(\sigma)=p=-\beta_1^\vee(w\lambda)$，令 $F$ 以 $\sigma$ 为最高权，构造 $G=(V(-s_\alpha w^{-1}\sigma)\otimes\mathcal{F})[\lambda]$。
   - 为什么：$C_\lambda$ 是 $\Sigma_\lambda^+$ 对应的 Weyl 房，$\beta_1^\vee$ 在其墙上取到所需整数 $p$。
3. 对 $G$ 的合成列逐项计算，$V(-s_\alpha w^{-1}\sigma)\otimes\mathcal{F}$ 的合成因子中只有两个落入 $\theta$：一个给出 $V$，一个给出 $V(p_\alpha)$，其余被 $[\lambda]$-截断杀掉；于是得到 $0\to V\to G\to V(p_\alpha)\to0$。
   - 为什么：$\sigma$ 的选取保证 $w\nu-s_{\beta_1}\sigma$ 是 $\Pi_\lambda$ 中根的非负整数组合，从而只剩两个极端权。

> 缺口：正合列的逐项构造（含 $\sigma$、$\mathcal{F}$ 的选取与两个极端权的计算）在 ch02a.tex:209-273；讲义只记录结论与函子性，本卡未重复逐项验证。

## 易错点

- $n(\lambda)$ 用的是 $\ell_\lambda$（$W_\lambda$ 的长度），不是 $W$ 的长度 $\ell$；把它写成 $\dim X$ 或 $\ell(w_0)$ 会给出错误的消没界。
- $\lambda$ 反支配 $\Leftrightarrow n(\lambda)=0$，但反支配与正则互不蕴含；消没定理不需要正则性，非消没定理（§4）才需要。
- $D_\lambda=D_{X,\lambda+\rho}$：第 2 章的下标比第 1 章 §2 的 $D_{X,\lambda}$ 小 $\rho$；抄成 $D_{X,\lambda}$ 会把消没界与 $\mathcal{O}(\lambda)$ 的模结构同时错位。
- $H^i(X,V)$ 的 $U_\theta$-模结构经 $U_\theta\to\Gamma(X,D_\lambda)$，$\theta=W\cdot\lambda$ 只依赖轨道；不要因为消没界里出现 $\lambda$ 就以为 $U_\theta$ 也依赖 $\lambda$ 本身。

## 相关卡

- `mloc/concept/nonvanishing-theorem`
- `mloc/concept/borel-weil-bott-for-d-lambda`
- `dmod/concept/coherent-d-module`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3 $D_\lambda$-模上同调的消没定理 · p.[25, 26]（PDF [29, 30]） · `源码/chapters/ch02b.tex:11-82（第 2 章定理 3.1、第 2 章推论 3.2 及证明）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §2 平移原理（第 2 章引理 2.3 的构造） · p.[23, 24, 25]（PDF [27, 28, 29]） · `源码/chapters/ch02a.tex:209-273 与 ch02b.tex:4-9（第 2 章引理 2.3 的构造与陈述）`
