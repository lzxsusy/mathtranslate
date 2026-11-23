# 整体截面函子 $\Gamma(X,-)$ 与伴随对 $(\Delta_\lambda,\Gamma)$

> `mloc/concept/global-sections-functor` · type=concept · track=D · status=draft · verification=source-only

**别名**：global sections functor、整体截面函子、$\Gamma(X,-)$、伴随对

## 摘要

$\Gamma=\operatorname{Hom}_{D_\lambda}(D_\lambda,-)$ 右伴随于 $\Delta_\lambda$；反支配时 $\varphi_V$ 同构且 $\Gamma$ 正合。

## 问题

整体截面与局部化如何互为伴随？单位与余单位在什么条件下是同构？

## 定义

整体截面函子 $\Gamma(X,-)=\operatorname{Hom}_{D_\lambda}(D_\lambda,-)$ 把 $D_\lambda$-模送到 $U_\theta$-模。它与局部化函子 $\Delta_\lambda$ 构成伴随对 $(\Delta_\lambda,\Gamma)$：局部化是左伴随，整体截面是右伴随。这一伴随关系把 $D_\lambda$-模的上同调问题翻译成 $U_\theta$-模的代数问题。

记号：$\Gamma(X,W)=\operatorname{Hom}_{D_\lambda}(D_\lambda,W)$；单位 $\varphi_V:V\to\Gamma(X,\Delta_\lambda(V))$；余单位 $\psi_W:\Delta_\lambda(\Gamma(X,W))\to W$；$\Gamma$ 的右导出 $R\Gamma$ 用 $\Gamma$-零调消解计算。

## 要点

- 伴随对是 $\operatorname{Hom}_{D_\lambda}(\Delta_\lambda(V),W)\cong\operatorname{Hom}_{U_\theta}(V,\Gamma(X,W))$，由张量–Hom 伴随与 $\Gamma=\operatorname{Hom}(D_\lambda,-)$ 复合得到。
- $\Gamma$ 左正合；$\lambda$ 反支配时 $\Gamma$ 正合（第 2 章推论 3.2），这是消没定理的直接推论。
- $\Gamma(X,D_\lambda)=U_\theta$ 且 $i>0$ 时 $H^i(X,D_\lambda)=0$（第 2 章定理 6.1）；这给出 $\Gamma$ 在「自由」对象上的行为。
- 第 3 章引理 1.1：$\lambda$ 反支配时，单位 $\varphi_V$ 对一切 $V\in\mathcal{M}(U_\theta)$ 是同构；证明经 $V=U_\theta$、自由模直和与右正合性做图追踪。
- 余单位 $\psi_W$ 一般不是同构；其核与余核的整体截面为零，故在商范畴 $Q\mathcal{M}_{qc}$ 中 $\psi$ 成为同构（第 3 章定理 1.2 的关键）。

## 公式

$$$\operatorname{Hom}_{D_\lambda}\bigl(\Delta_\lambda(V),W\bigr)\cong\operatorname{Hom}_{U_\theta}\bigl(V,\Gamma(X,W)\bigr)$$$

$$$\varphi_V:V\longrightarrow\Gamma(X,\Delta_\lambda(V)),\qquad \psi_W:\Delta_\lambda(\Gamma(X,W))\longrightarrow W$$$

$$$\Gamma(X,D_\lambda)=U_\theta,\qquad H^i(X,D_\lambda)=0\ (i>0)$$$

$$$\Gamma\ \text{正合}\iff H^i(X,-)=0\ (i>0)\qquad(\lambda\ \text{反支配})$$$

## 相关定理

### 伴随对 $(\Delta_\lambda,\Gamma)$

设 $\lambda\in\mathfrak{h}^*$。则对 $V\in\mathcal{M}(U_\theta)$、$W\in\mathcal{M}(D_\lambda)$ 有自然同构 $\operatorname{Hom}_{D_\lambda}(\Delta_\lambda(V),W)\cong\operatorname{Hom}_{U_\theta}(V,\Gamma(X,W))$，即 $\Delta_\lambda$ 左伴随于 $\Gamma$。

证明状态：`complete`

1. 由张量–Hom 伴随，$\operatorname{Hom}_{D_\lambda}(D_\lambda\otimes_{U_\theta}V,W)\cong\operatorname{Hom}_{U_\theta}(V,\operatorname{Hom}_{D_\lambda}(D_\lambda,W))$。
   - 为什么：这是模范畴中 $-\otimes_{U_\theta}V$ 与 $\operatorname{Hom}_{U_\theta}(V,-)$ 的伴随。
2. $\operatorname{Hom}_{D_\lambda}(D_\lambda,W)=\Gamma(X,W)$ 按定义，故得到所需同构。
   - 为什么：$\Gamma$ 的定义就是 $\operatorname{Hom}_{D_\lambda}(D_\lambda,-)$。
3. 自然性来自张量–Hom 伴随的自然性。
   - 为什么：伴随同构对 $V,W$ 自然。

### 第 3 章引理 1.1（反支配时单位是同构）

设 $\lambda\in\mathfrak{h}^*$ 反支配。则对任意 $V\in\mathcal{M}(U_\theta)$，单位 $\varphi_V:V\to\Gamma(X,\Delta_\lambda(V))$ 是 $\mathfrak{g}$-模同构。

证明状态：`sketch`

1. 先取 $V=U_\theta$：$\Delta_\lambda(U_\theta)=D_\lambda$，$\varphi_{U_\theta}$ 是 $U_\theta\to\Gamma(X,D_\lambda)$，由 C.6.1 它是同构。
   - 为什么：C.6.1 是 $U_\theta\cong\Gamma(X,D_\lambda)$ 的原始出处；本书第 2 章定理 6.1 给出同一结论。
2. 自由模 $U_\theta^{\oplus I}$：$\Delta_\lambda$ 与 $\Gamma$ 都与直和交换，逐项取同构。
   - 为什么：张量积与 $\Gamma$ 保持直和。
3. 一般 $V$ 取自由表示 $F\to V\to0$；由 C.3.2，$\Gamma$ 在 $\lambda$ 反支配时正合，配合 $\Delta_\lambda$ 右正合，对 $0\to K\to F\to V\to0$ 做图追踪得 $\varphi_V$ 同构。
   - 为什么：$\lambda$ 反支配使 $\Gamma$ 正合，五引理给出中间项同构。

> 缺口：第 3 章引理 1.1 的证明依赖 C.6.1 与 C.3.2；译本 annote（ch03a.tex:39-41）说明 C.6.1/C.3.2 指参考文献 [9][10] 两部未刊讲义，本书无附录，编号照录。本卡只复述图追踪骨架，未展开 C.6.1 的原始证明。

### 第 2 章推论 3.2（反支配时 $\Gamma$ 正合）

设 $\lambda\in\mathfrak{h}^*$ 反支配。则 $\Gamma:\mathcal{M}_{qc}(D_\lambda)\to\mathcal{M}(U_\theta)$ 正合。

证明状态：`complete`

1. 正合性等价于 $i>0$ 时 $H^i(X,V)=0$ 对一切 $V\in\mathcal{M}_{qc}(D_\lambda)$ 成立。
   - 为什么：$\Gamma$ 左正合，故只需高阶消没。
2. 消没定理由 $n(\lambda)=0$（$\lambda$ 反支配）给出 $i>0$ 的全部消没。
   - 为什么：第 2 章定理 3.1：$i>n(\lambda)$ 时 $H^i=0$，而 $n(\lambda)=0$。

## 易错点

- $\Gamma$ 只是左正合；一般 $\lambda$ 下不要用「正合」做图追踪，反支配条件不能省。
- 单位 $\varphi_V$ 反支配时才同构；对一般 $\lambda$，$\Gamma(X,\Delta_\lambda(V))$ 会严格大于 $V$。
- 余单位 $\psi_W$ 一般不是同构；它在商范畴 $Q\mathcal{M}_{qc}$ 中才成为同构（第 3 章定理 1.2），不要在 $\mathcal{M}_{qc}$ 里直接消去。
- $U_\theta$ 的下标是中心特征标轨道 $\theta=W\cdot\lambda$，不是 $\lambda$ 本身；$\Gamma(X,D_\lambda)=U_\theta$ 对同一 $\theta$ 的所有 $\lambda$ 一致。

## 相关卡

- `mloc/concept/localization-functor-delta`
- `mloc/concept/localization-equivalence`
- `mloc/concept/cohomology-of-d-lambda-modules`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §1 整体截面与伴随 · p.[35, 36]（PDF [39, 40]） · `源码/chapters/ch03a.tex:10-23（伴随对与第 3 章引理 1.1）、ch03a.tex:59-63（第 3 章推论 1.3 的前提）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3 反支配时 $\Gamma$ 正合 · p.[25, 26]（PDF [29, 30]） · `源码/chapters/ch02b.tex:22-82（第 2 章推论 3.2）`
