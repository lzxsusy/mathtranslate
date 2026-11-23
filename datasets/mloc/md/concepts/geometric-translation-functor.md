# 几何平移函子 $V\mapsto V(\mu)$

> `mloc/concept/geometric-translation-functor` · type=concept · track=E · status=draft · verification=source-only

**别名**：geometric translation functor、平移函子、$(\mu)$-扭变、几何平移

## 摘要

几何平移 $V\mapsto V(\mu)=V\otimes\mathcal{O}(\mu)$ 是 $\mathcal{M}(D_\lambda)\to\mathcal{M}(D_{\lambda+\mu})$ 的范畴等价。

## 问题

几何平移 $V\mapsto V(\mu)$ 为什么是 $\mathcal{M}(D_\lambda)$ 与 $\mathcal{M}(D_{\lambda+\mu})$ 的范畴等价，它与 $\mathfrak{n}_x$-同调、与几何纤维 $T_x$ 又是什么关系？

## 定义

设 $\mu\in P(\Sigma)$，$V\in\mathcal{M}(D_\lambda)$。置 $V(\mu)=V\otimes_{\mathcal{O}_X}\mathcal{O}_X(\mu)$，其 $D$-模结构由 $\mathcal{O}(\mu)$ 的联络给出，于是 $V(\mu)\in\mathcal{M}(D_{\lambda+\mu})$。函子 $(\mu):\mathcal{M}(D_\lambda)\to\mathcal{M}(D_{\lambda+\mu})$ 是协变函子，称为几何平移函子；它是范畴等价，并诱导 $\mathcal{M}_{qc}$ 与 $\mathcal{M}_{coh}$ 之间的等价（§2.2 平移原理，ch02a.tex:144-160）。

记号：$D_\lambda=D_{X,\lambda+\rho}$ 按 §2.1 的约定（ch02a.tex:126-130，底本 p.20）；$(\mu)$ 表示张量 $\mathcal{O}_X(\mu)$；$P(\Sigma)$ 是整权格。要与 §3.2 的几何纤维函子严格区分：$T_x(\mathcal{F})=\mathcal{F}_x/\mathfrak{m}_x\mathcal{F}_x$ 把 $\mathcal{O}_X$-模送到复向量空间，右正合（ch03b.tex:91-93，底本 p.45）；$T_x$ 与 $\Delta_\lambda$ 的复合才计算 $\mathfrak{n}_x$-同调（定理 2.5、推论 2.6，ch03b.tex:95-101, 122-125）。

## 要点

- $V(\mu)$ 的 $D_{\lambda+\mu}$-结构来自 $\mathcal{O}(\mu)$ 的联络：$\theta\cdot(v\otimes f)=\theta v\otimes f+v\otimes\theta f$，其中 $\theta f$ 含 $\mu(\theta)f$ 项——这正是特征标从 $\lambda$ 平移到 $\lambda+\mu$ 的原因。
- $(\mu)$ 是范畴等价，逆为 $(-\mu)$（因 $\mathcal{O}(\mu)\otimes\mathcal{O}(-\mu)\cong\mathcal{O}_X$）；所以 $\mathcal{M}(D_\lambda)$ 与 $\mathcal{M}(D_{\lambda+\mu})$ 同构，但**不是**同一个范畴：平移把对象搬到另一个特征标上。
- 平移与交织函子只差一个权的置换：引理 3.5 给 $J_w(V(\nu))=J_w(V)(w\nu)$ 与 $LI_w(V(\nu))=LI_w(V)(w\nu)$（§3.3，ch03c.tex:94-99）。
- 这条置换律是定理 3.14、3.20 的证明能把 $\lambda$ 归约到反支配正则情形的技术基础：平移不改变函子的抽象性质，只改变权。
- 平移保持完整性与有限长，故在完整复形上也给等价 $D^b_{hol}(D_\lambda)\simeq D^b_{hol}(D_{\lambda+\mu})$（§3.6，ch03e.tex:278）。
- $T_x$ 不是平移：$T_x$ 是几何纤维（沿 $\{x\}\hookrightarrow X$ 的逆像），它与 $\Delta_\lambda$ 的谱序列 $L_pT_x(L_q\Delta_\lambda(V))\Rightarrow H_{-(p+q)}(\mathfrak{n}_x,V)_{(\lambda+\rho)}$ 才是「局部化后取 $\mathfrak{n}_x$-同调」的精确含义（推论 2.6）。

## 公式

$$$V(\mu)=V\otimes_{\mathcal{O}_X}\mathcal{O}_X(\mu)\in\mathcal{M}(D_{\lambda+\mu})$$$

$$$(\mu):\mathcal{M}(D_\lambda)\xrightarrow{\ \sim\ }\mathcal{M}(D_{\lambda+\mu}),\qquad (\mu)^{-1}=(-\mu)$$$

$$$J_w\bigl(V^\bullet(\nu)\bigr)=J_w(V^\bullet)(w\nu),\qquad LI_w\bigl(V^\bullet(\nu)\bigr)=LI_w(V^\bullet)(w\nu)$$$

$$$L_pT_x\bigl(L_q\Delta_\lambda(V)\bigr)\Rightarrow H_{-(p+q)}(\mathfrak{n}_x,V)_{(\lambda+\rho)}$$$

## 相关定理

### 引理 3.5：平移与交织函子交换（权按 $w$ 搬运）

对任意 $\nu\in P(\Sigma)$ 与 $V^\bullet\in D^b(D_\lambda)$，(i) $J_w(V^\bullet(\nu))=J_w(V^\bullet)(w\nu)$；(ii) $LI_w(V^\bullet(\nu))=LI_w(V^\bullet)(w\nu)$。

证明状态：`complete`

1. 把 $V^\bullet(\nu)$ 写成 $V^\bullet\otimes_{\mathcal{O}_X}\mathcal{O}(\nu)$，并用引理 3.3(i) 的 $p_1^*(\mathcal{O}(w\nu))=p_2^*(\mathcal{O}(\nu))$ 把权从 $p_2$ 侧搬到 $p_1$ 侧。
   - 为什么：引理 3.3(i) 说明在 $Z_w$ 上 $w\nu$ 的拉回与 $\nu$ 的拉回相同，这是唯一需要用到的几何事实。
2. 于是 $T_w\otimes p_2^+(V^\bullet(\nu))=T_w\otimes p_2^+(V^\bullet)\otimes p_1^*(\mathcal{O}(w\nu))$，对它取 $Rp_{1+}$ 并用投影公式把 $p_1^*(\mathcal{O}(w\nu))$ 提到直像外。
   - 为什么：直像对 $p_1$-拉回的线丛满足投影公式，故权可以作为 $\mathcal{O}(w\nu)$ 的扭整体提出。
3. 得到 $J_w(V^\bullet(\nu))=J_w(V^\bullet)\otimes\mathcal{O}(w\nu)=J_w(V^\bullet)(w\nu)$；对左导出取 $H^0$ 与逐项作用相容，即得 (ii)。
   - 为什么：左导出由投射消解定义，而上述等式对消解的每一项成立，故在导出范畴中同样成立。

### 定理 3.16：$LI_w$ 与 $L\Delta_\lambda$ 的交换

设 $\lambda$ 是 $\Sigma^+_w$-反支配的，则作为从 $D^-(U_\theta)$ 到 $D^-(D_{w\lambda})$ 的函子有 $LI_w\circ L\Delta_\lambda\cong L\Delta_{w\lambda}$。

证明状态：`sketch`

1. 先设 $w$ 是单反射 $s_\alpha$ 且 $\lambda$ 是 $\alpha$-反支配的，此时由引理 3.11，$D_{s_\alpha\lambda}\to I_{s_\alpha}(D_\lambda)$ 是同构。
   - 为什么：$\alpha$-反支配正是引理 3.11 的前提，它保证单反射的交织函子在 $D_\lambda$ 上不产生高阶项。
2. 用引理 3.13 的 $J_w(D(D_\lambda))=D(D_{w\lambda})$ 把两个函子都作用在 $D_\lambda$ 的投射消解上，得到自然同构。
   - 为什么：两个函子都是正合且与直像交换的，逐项比较即可。
3. 对一般 $w$ 取既约分解并用乘积公式（定理 3.18）与引理 3.12(iii) 逐次验证反支配性，归纳得结论。
   - 为什么：引理 3.12(iii) 说明 $\Sigma^+_{w'w}$-反支配可逐段下降为 $w'\lambda$ 的 $\Sigma^+_{w'}$-反支配，正好配合分解。
4. 其余为形式验算：把上述自然同构在 $D^-(U_\theta)$ 的生成对象上检查即可。
   - 为什么：$L\Delta_\lambda$ 的像生成 $D^-(D_\lambda)$ 的相关子范畴，逐生成元验证足够。

> 缺口：第 1 步依赖引理 3.11（单反射时 $D_{s_\alpha\lambda}\to I_{s_\alpha}(D_\lambda)$ 为同构）的完整证明（ch03d.tex:22-51，底本 p.53-54），本卡未逐行复核；第 3 步的归纳细节亦从略。

## 易错点

- 书里的「几何平移」专指 $V\mapsto V(\mu)=V\otimes\mathcal{O}(\mu)$，**不是** §3.2 的几何纤维 $T_x$。把「局部化后取 $\mathfrak{n}_x$-同调」称作几何平移是常见的名称混用，那件事由 $LT_x\circ L\Delta_\lambda$ 的谱序列实现（推论 2.6）。
- $\mu$ 必须取在 $P(\Sigma)$（整权格）内，才能保证 $\mathcal{O}(\mu)$ 是 $X$ 上的 $G$-齐性线丛；$\lambda$ 本身不必是整权。
- 平移与 §3.4 的对偶交换时要变号：$\mathbb{D}(V^\bullet(\nu))=\mathbb{D}(V^\bullet)(-\nu)$（引理 4.1）。漏掉这个负号会得到方向相反的结论。

## 相关卡

- `mloc/concept/intertwining-functor-i-w`
- `mloc/concept/weyl-group-action-on-d-lambda-modules`
- `mloc/concept/inverse-intertwining-functor`
- `mloc/concept/tensor-with-finite-dimensional`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §2.2 平移原理（几何平移函子的定义） · p.[21]（PDF [25]） · `源码/chapters/ch02a.tex:144-160（平移原理、几何平移函子的定义与等价性）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.3 平移与交织函子的交换（引理 3.5） · p.[49]（PDF [53]） · `源码/chapters/ch03c.tex:94-99（引理 3.5）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.6 几何平移在完整复形上的等价 · p.[65]（PDF [69]） · `源码/chapters/ch03e.tex:276-280（$D^b_{hol}$ 与几何平移的等价）`
