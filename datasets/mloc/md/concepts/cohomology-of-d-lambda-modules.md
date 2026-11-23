# $D_\lambda$-模的上同调：$U_\theta$ 与诱导模的计算

> `mloc/concept/cohomology-of-d-lambda-modules` · type=concept · track=C · status=draft · verification=source-only

**别名**：cohomology of D-lambda-modules、$D_\lambda$-模上同调、第 2 章定理 6.1、第 2 章定理 6.5、第 2 章推论 6.6

## 摘要

$D_\lambda$ 的截面是 $U_\theta$，无高阶上同调；诱导模 $D_h\otimes_{U(\mathfrak{h})}V$ 的截面为 $U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}V$。

## 问题

$D_\lambda$ 自身作为 $D_\lambda$-模，各阶上同调是什么？诱导 $D_\mathfrak{h}$-模的整体截面能否用中心特征标直接算出？

## 定义

对 $V\in\mathcal{M}(D_\lambda)$，$H^i(X,V)$ 经 $U_\theta\to\Gamma(X,D_\lambda)$ 成为 $U_\theta$-模。本节把 $V=D_\lambda$ 与更一般的诱导模 $D_\mathfrak{h}\otimes_{U(\mathfrak{h})}V$ 的上同调算到底：整体截面由张量积 $U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}-$ 给出，高阶全消没。这是 §6 的骨干结果，也是局部化函子在 $V=U_\theta$ 处「单位同构」的来源。

记号：$D_\mathfrak{h}=D_h$ 是 $X$ 上由 $\mathfrak{h}$-不变微分算子生成的子层；$U^\circ$ 是由 $U(\mathfrak{g})$ 与 $\mathcal{O}_X$ 生成的层；$\mathfrak{n}^\circ$ 是 $\mathfrak{n}$ 对应的向量场层；$C^\bullet=U^\circ\otimes_{\mathcal{O}_X}\wedge\mathfrak{n}^\circ$，$C^i=U^\circ\otimes\wedge^{-i}\mathfrak{n}^\circ$；$Z(\mathfrak{g})$ 是 $U(\mathfrak{g})$ 的中心；$C_{\lambda+\rho}$ 是一维 $U(\mathfrak{h})$-模，$h$ 作用为 $(\lambda+\rho)(h)$。

## 要点

- 第 2 章定理 6.1 有两半：$U_\theta\cong\Gamma(X,D_\lambda)$（典范映射），以及 $i>0$ 时 $H^i(X,D_\lambda)=0$；两者都是 $\lambda$ 的整族结论，不只对正则或反支配 $\lambda$。
- $U_\theta\cong\Gamma(X,D_\lambda)$ 是「$D_\lambda$ 的整体截面实现中心特征标」的精确陈述，也是所有 $H^i(X,V)$ 上 $U_\theta$-模结构的来源。
- 工具是 $C^\bullet=U^\circ\otimes_{\mathcal{O}_X}\wedge\mathfrak{n}^\circ$：它带第二个左 $\mathfrak{g}$-作用 $\kappa$，是 $(\mathfrak{g}\times\mathfrak{g},G)$-模复形，并且是 $D_h$ 的左消解（第 2 章命题 6.3）。
- 对 $D_h$ 的谱序列退化给出第 2 章定理 6.5：$\Gamma(X,D_h)=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}U(\mathfrak{h})$，高阶消没；对任意 $U(\mathfrak{h})$-模 $V$ 张量后得第 2 章推论 6.6。
- 取 $V=\mathbb{C}_{\lambda+\rho}$ 并用 $D_\lambda=D_h\otimes_{U(\mathfrak{h})}\mathbb{C}_{\lambda+\rho}$、$U_\theta=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}\mathbb{C}_{\lambda+\rho}$，即得第 2 章定理 6.1。
- 对 $\Delta_\lambda(V)=D_\lambda\otimes_{U_\theta}V$ 一般没有「$\Gamma(\Delta_\lambda(V))=V$」；这需要 $\lambda$ 反支配（第 3 章引理 1.1），且是第 3 章局部化理论的起点。

## 公式

$$$U_\theta\cong\Gamma(X,D_\lambda),\qquad H^i(X,D_\lambda)=0\ (i>0)$$$

$$$C^\bullet=U^\circ\otimes_{\mathcal{O}_X}\wedge\mathfrak{n}^\circ,\qquad C^i=U^\circ\otimes\wedge^{-i}\mathfrak{n}^\circ$$$

$$$\Gamma(X,D_h)=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}U(\mathfrak{h}),\qquad H^i(X,D_h)=0\ (i>0)$$$

$$$\Gamma\bigl(X,D_h\otimes_{U(\mathfrak{h})}V\bigr)=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}V,\qquad H^i=0\ (i>0)$$$

## 相关定理

### 第 2 章定理 6.1（$D_\lambda$ 的上同调）

设 $\lambda\in\mathfrak{h}^*$。(i) 自然映射 $U_\theta\to D_\lambda$ 诱导的 $U_\theta$-模同态 $U_\theta\to\Gamma(X,D_\lambda)$ 是同构；(ii) 对一切 $i>0$ 有 $H^i(X,D_\lambda)=0$。

证明状态：`complete`

1. 构造 $C^\bullet=U^\circ\otimes_{\mathcal{O}_X}\wedge\mathfrak{n}^\circ$，用第二个左 $\mathfrak{g}$-作用 $\kappa(\xi)(u\otimes v)=-u\xi\otimes v+u\otimes\xi\cdot v$ 使其成为 $(\mathfrak{g}\times\mathfrak{g},G)$-模复形。
   - 为什么：$\kappa$ 与第一个作用交换，且微分 $d$ 与两个作用交换。
2. 由 $F_pC^\bullet$ 滤过与 $\operatorname{Gr}C^\bullet=S_{p+q}(\mathfrak{g}^\circ)\otimes\wedge^{-q}\mathfrak{n}^\circ$ 的 Koszul 复形计算，得 $C^\bullet$ 零调（第 2 章引理 6.2）。
   - 为什么：$\mathfrak{g}^\circ=\mathfrak{n}^\circ\oplus\mathfrak{h}^\circ\oplus\mathfrak{n}_-^\circ$，$\wedge\mathfrak{n}^\circ$ 上 Koszul 微分零调。
3. 于是 $C^\bullet$ 是 $D_h$ 的左消解（第 2 章命题 6.3）；对 $D_h$ 计算 $R\Gamma$，谱序列 $E_2^{p,q}=H^p(X,H^q(C^\bullet))\Rightarrow H^{p+q}(R\Gamma(C^\bullet))$ 中 $H^q(C^\bullet)$ 只在 $q=0$ 非零，故 $E_2$ 退化。
   - 为什么：$C^\bullet$ 是 $D_h$-模的消解，$H^q(C^\bullet)$ 作为 $D_h$-模只在 $q=0$ 有贡献；退化给出 $H^i(X,D_h)=\Gamma(X,H^i(C^\bullet))$。
4. 逐项计算 $\Gamma(X,D_h)$ 的 $F$-滤过：$F_k/F_{k-1}$ 是 $\operatorname{Card}W(k)$ 个 $U(\mathfrak{g})$ 的直和，故 $\Gamma(X,D_h)=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}U(\mathfrak{h})$，且 $i>0$ 时 $H^i(X,D_h)=0$（第 2 章定理 6.5）。
   - 为什么：关键用第 2 章引理 6.4：$U(\mathfrak{h})$ 是秩 $\operatorname{Card}W$ 的自由 $Z(\mathfrak{g})$-模；$F_k$ 的秩与 $\operatorname{Card}W(k)$ 匹配。
5. 对任意 $U(\mathfrak{h})$-模 $V$，$D_h\otimes_{U(\mathfrak{h})}V$ 的消解由 $C^\bullet\otimes_{U(\mathfrak{h})}V$ 给出，谱序列同样退化，得 $\Gamma(X,D_h\otimes_{U(\mathfrak{h})}V)=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}V$ 且高阶消没（第 2 章推论 6.6）。
   - 为什么：$C^\bullet$ 的各项是自由 $U(\mathfrak{h})$-模，张量后仍零调；$\Gamma$ 与 $\otimes_{U(\mathfrak{h})}V$ 在自由项上交换。
6. 取 $V=\mathbb{C}_{\lambda+\rho}$：$D_\lambda=D_h\otimes_{U(\mathfrak{h})}\mathbb{C}_{\lambda+\rho}$，$U_\theta=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}\mathbb{C}_{\lambda+\rho}$，即得 (i)(ii)。
   - 为什么：$\mathbb{C}_{\lambda+\rho}$ 把 $Z(\mathfrak{g})$ 的作用经 $U(\mathfrak{h})$ 的 $\gamma$ 拉回成 $\chi_\lambda$，正好是 $U_\theta$ 的定义。

### 第 2 章命题 6.3（$C^\bullet$ 是 $D_h$ 的左消解）

复形 $C^\bullet=U^\circ\otimes_{\mathcal{O}_X}\wedge\mathfrak{n}^\circ$ 是 $D_h$ 的左消解，且各项是 $(\mathfrak{g}\times\mathfrak{g},G)$-模。

证明状态：`complete`

1. 由 $C^\bullet$ 的 $F$-滤过，$\operatorname{Gr}C^\bullet$ 是 $S(\mathfrak{g}^\circ)\otimes\wedge\mathfrak{n}^\circ$ 上的 Koszul 复形。
   - 为什么：$F_pC^\bullet$ 的定义把 $U^\circ$ 的滤过与 $\wedge$ 的次数配合起来。
2. Koszul 复形在 $\mathfrak{n}^\circ$ 部分零调，故 $C^\bullet$ 零调（第 2 章引理 6.2）。
   - 为什么：$\mathfrak{n}^\circ$ 是 Koszul 复形的正则序列方向。
3. $H^0(C^\bullet)=U^\circ/(\mathfrak{n}^\circ U^\circ)=D_h$，故 $C^\bullet$ 是 $D_h$ 的左消解。
   - 为什么：零次同调正是 $U^\circ$ 模去由 $\mathfrak{n}^\circ$ 生成的左理想。

### 第 2 章定理 6.5（$D_h$ 的上同调）

(i) $\Gamma(X,D_h)=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}U(\mathfrak{h})$；(ii) $i>0$ 时 $H^i(X,D_h)=0$。

证明状态：`complete`

1. 用第 2 章命题 6.3 的左消解 $C^\bullet$ 计算 $R\Gamma(X,D_h)$。
   - 为什么：$C^\bullet$ 由 $\Gamma$-零调对象组成（$U^\circ$ 是自由 $\mathcal{O}_X$-模）。
2. 谱序列 $E_2^{p,q}=H^p(X,H^q(C^\bullet))\Rightarrow H^{p+q}(R\Gamma(C^\bullet))$ 退化，因为 $H^q(C^\bullet)$ 只在 $q=0$ 非零。
   - 为什么：$C^\bullet$ 除零次外零调。
3. 计算 $F_k\Gamma(X,D_h)/F_{k-1}$：它是 $\operatorname{Card}W(k)$ 个 $U(\mathfrak{g})$ 的直和，故 $\Gamma(X,D_h)=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}U(\mathfrak{h})$。
   - 为什么：第 2 章引理 6.4 给出 $U(\mathfrak{h})$ 是秩 $\operatorname{Card}W$ 的自由 $Z(\mathfrak{g})$-模，$\sum_k\operatorname{Card}W(k)=\operatorname{Card}W$。
4. $i>0$ 时 $E_2^{p,q}=0$（$q>0$ 时 $H^q=0$；$q=0$ 时 $p>0$ 时 $H^p(X,D_h)=0$ 需由消解直接算），故 $H^i(X,D_h)=0$。
   - 为什么：$D_h$ 是 $C^\bullet$ 的零次同调，谱序列的 $E_2$ 项在 $p>0,q=0$ 处为零由 $H^p(X,U^\circ)$ 的消失给出。

### 第 2 章推论 6.6（诱导模的整体截面）

设 $V$ 是任意 $U(\mathfrak{h})$-模。则 $\Gamma(X,D_h\otimes_{U(\mathfrak{h})}V)=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}V$，且 $i>0$ 时 $H^i(X,D_h\otimes_{U(\mathfrak{h})}V)=0$。

证明状态：`complete`

1. $C^\bullet\otimes_{U(\mathfrak{h})}V$ 的各项是自由 $U(\mathfrak{h})$-模张量 $V$，仍零调，故是 $D_h\otimes_{U(\mathfrak{h})}V$ 的左消解。
   - 为什么：$C^i$ 是自由 $U(\mathfrak{h})$-模。
2. 对 $C^\bullet\otimes_{U(\mathfrak{h})}V$ 用谱序列，退化后得 $\Gamma=R\Gamma=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}V$。
   - 为什么：与第 2 章定理 6.5 同法，把 $\otimes_{U(\mathfrak{h})}V$ 逐项施于消解。
3. 高阶项同理由谱序列退化消没。
   - 为什么：$E_2$ 只在 $(0,0)$ 处非零。

## 易错点

- $D_\lambda$ 的上同调是「$U_\theta$ 在 $0$ 次、其余为零」；这与 $\mathcal{O}(\lambda)$ 的上同调（BWB）完全不同，$D_\lambda$ 是局部化函子的像而非标准模。
- $C^\bullet$ 的指标是负的：$C^i=U^\circ\otimes\wedge^{-i}\mathfrak{n}^\circ$，只有 $i\le0$ 非零；把它当正次数消解会把 $H^0$ 与 $H^{n}$ 弄反。
- $\Gamma(X,D_h\otimes_{U(\mathfrak{h})}V)=U(\mathfrak{g})\otimes_{Z(\mathfrak{g})}V$ 里的张量是 $Z(\mathfrak{g})$，不是 $U(\mathfrak{h})$ 或 $U(\mathfrak{g})$；$V$ 只是 $U(\mathfrak{h})$-模，中心通过 $\gamma$ 作用。
- $D_\lambda=D_h\otimes_{U(\mathfrak{h})}\mathbb{C}_{\lambda+\rho}$，故 $\lambda$ 的平移在 $D_h$-侧由 $\mathbb{C}_{\lambda+\rho}$ 承担；$D_\lambda=D_{X,\lambda+\rho}$ 的 $\rho$ 就在这里。
- $\Gamma(X,\Delta_\lambda(V))=V$ 一般不成立，只有 $\lambda$ 反支配时（第 3 章引理 1.1）才成立；不要把第 2 章定理 6.1 误读成对一切 $V$ 的单位同构。
- 与第 3 章 §2 的分工：本节只算 $D_\lambda$ 与 $D_h\otimes_{U(\mathfrak{h})}V$ 这类局部化对象的上同调；一般 $V\in\mathcal{M}(U_\theta)$ 的 $H^\bullet(X,\Delta_\lambda(V))$ 与 $\mathfrak{n}$-同调的对应（谱序列）属第 3 章 §2，两套计算不可互相代入。

## 相关卡

- `mloc/concept/localization-functor-delta`
- `mloc/concept/global-sections-functor`
- `mloc/concept/localization-and-n-homology`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §6 $D_\lambda$-模的上同调 · p.[31, 32]（PDF [35, 36]） · `源码/chapters/ch02b.tex:302-336（第 2 章定理 6.1）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §6 消解与诱导模 · p.[32, 33, 34]（PDF [36, 37, 38]） · `源码/chapters/ch02b.tex:376-402（第 2 章命题 6.3）、ch02b.tex:425-453（第 2 章定理 6.5、第 2 章推论 6.6）`
