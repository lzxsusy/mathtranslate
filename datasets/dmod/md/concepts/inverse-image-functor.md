---
id: dmod/concept/inverse-image-functor
type: concept
track: D
---

# 逆像函子 $\varphi^+$

> 左 $\mathcal D_Y$-模沿 $\varphi$ 拉回为左 $\mathcal D_X$-模，右正合；开包含时就是限制。

**问题**：逆像为什么必须经相对双模 $\mathcal D_{X\to Y}$ 构造，它失去的正合性又由什么补偿？

## 定义

设 $\varphi:X\to Y$ 是光滑簇态射，$V$ 是左 $\mathcal D_Y$-模。置 $$\varphi^+(V)=\mathcal D_{X\to Y}\otimes_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}V,$$ 左 $\mathcal D_X$ 通过 $\mathcal D_{X\to Y}$ 的左作用。它是右正合函子 $\varphi^+\colon M_L(\mathcal D_Y)\to M_L(\mathcal D_X)$：层拉回 $\varphi^{-1}$ 正合，张量积右正合。仿射情形写作 $\varphi^+(M)=\mathcal D_{X\to Y}\otimes_{\mathcal D_Y}M$，与 $R(X)\otimes_{R(Y)}M$ 相容。它一般不正合，导出化见「导出逆像」卡。

*记号*：$V\in M_L(\mathcal D_Y)$；$\varphi^{-1}$：$\mathcal O$-模（层）拉回；$L_p\varphi^+$：第 $p$ 个左导出函子（同调编号，$L_p=H^{-p}$）；$\operatorname{For}$：忘记 $\mathcal D$-结构、只看 $\mathcal O$-模的函子。

## 要点

- 定义 $\varphi^+(V)=\mathcal D_{X\to Y}\otimes_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}V$ 给出右正合函子；它是 $\mathcal O$-模拉回 $\varphi^*$ 的提升，$\mathcal D$-结构由 $\mathcal D_{X\to Y}$ 提供。
- 开包含 $i:U\hookrightarrow X$：$i^+(V)=V|_U$ 且 $i^+$ 正合（注 4.3.1）；这是少数无需导出化的情形。
- 复合：$\varphi^+\circ\psi^+=(\psi\circ\varphi)^+$（引理 4.3.9），导出版本 $L\varphi^+\circ L\psi^+\cong L(\psi\circ\varphi)^+$（定理 4.3.10）。
- 与遗忘函子交换：$\operatorname{For}\circ L\varphi^+\cong L\varphi^*\circ\operatorname{For}$（定理 4.3.6）；上同调保持拟凝聚（定理 4.3.7），仿射情形由 $\operatorname{Tor}$ 计算（命题 4.3.8）。

## 关键公式

- $\varphi^+(V)=\mathcal D_{X\to Y}\otimes_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}V$
- $i^+(V)=V|_U\qquad(i:U\hookrightarrow X\ \text{开包含})$
- $\varphi^+\circ\psi^+=(\psi\circ\varphi)^+,\qquad L\varphi^+\circ L\psi^+\cong L(\psi\circ\varphi)^+$
- $\Gamma(X,L_p\varphi^+V)=\operatorname{Tor}^{-p}_{\mathcal D_Y}\bigl(\mathcal D_{X\to Y},\Gamma(Y,V)\bigr)\quad(\text{仿射})$

## 定理与证明

### 定理 4.3.6（导出逆像与遗忘函子交换）（完整）

$\operatorname{For}\circ L\varphi^+\cong L\varphi^*\circ\operatorname{For}$，即 $\mathcal D$-模的导出逆像的 $\mathcal O$-模上同调就是 $\mathcal O$-模的导出拉回。

1. 先在 $\mathcal O$-模层面：$\varphi^+(V)=\mathcal D_{X\to Y}\otimes_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}V$ 中把 $\mathcal D_{X\to Y}$ 写成 $\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}\varphi^{-1}\mathcal D_Y$，张量积的结合律把 $\varphi^{-1}\mathcal D_Y$ 的吸收掉，得 $\operatorname{For}\circ\varphi^+\cong\varphi^*\circ\operatorname{For}$。  
   *为什么*：$\mathcal D_{X\to Y}$ 作为 $\mathcal O_X$-模就是 $\varphi^*\mathcal D_Y$，而 $\varphi^*$ 与 $\operatorname{For}$ 的复合恰好是 $\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}\varphi^{-1}(-)$。
2. 取 $V$ 的平坦左 $\mathcal D_Y$-模分解来计算 $L\varphi^+$。  
   *为什么*：平坦左 $\mathcal D_Y$-模类对 $\varphi^+$ 左适合（引理 4.3.2），故可用该分解计算右导出函子。
3. 同一分解中每一项也是平坦 $\mathcal O_Y$-模，故它同时计算 $L\varphi^*$。  
   *为什么*：平坦 $\mathcal D_Y$-模必是平坦 $\mathcal O_Y$-模（引理 4.3.5），因此这些项对 $\varphi^*$ 无环。
4. 两个导出函数在同一个无环分解上给出相同复形，故 $\operatorname{For}\circ L\varphi^+\cong L\varphi^*\circ\operatorname{For}$。  
   *为什么*：导出函子在左适合类中的任一分解上都可计算，且第 1 步已把未导出层面等同。

*出处*：定理 4.3.6 / 原书 §3，p.106–107

### 定理 4.3.10（导出逆像的复合）（要点（有缺口））

$L\varphi^+\circ L\psi^+\cong L(\psi\circ\varphi)^+$。


> 缺口：讲义把证明化归为「取平坦分解并用引理 4.3.5」，未逐项验证两重复合中张量积的 $\operatorname{Tor}$-独立性；结论按引理 4.3.9 与引理 4.3.2 的适用性得到。

*出处*：定理 4.3.10 / 原书 §3，p.107


## 易错点

- $\varphi^+$ 不正合：只有开包含（注 4.3.1）等少数情形正合；闭浸入时 $L_1\varphi^+\neq0$ 是常态，不能把 $\varphi^+$ 当正合函子用。
- 张量取在 $\varphi^{-1}\mathcal D_Y$ 上而不是 $\mathcal D_Y$ 上；层拉回 $\varphi^{-1}$ 必须留在张量积里，不能与 $\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}(-)$ 交换位置。
- $\varphi^+$ 只对左 $\mathcal D_Y$-模定义；对右模须改用转置双模 $\mathcal D_{Y\leftarrow X}$ 与 $\varphi_+$ 的记法，混用会算错作用的一侧。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§3 逆像函子，p.105-106-107-108（PDF p.111-112-113-114），`源码/chapters/chap4.tex:347-520（定理 4.3.6、引理 4.3.9、定理 4.3.10）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§2 仿射簇的逆像，p.103-104（PDF p.109-110），`源码/chapters/chap4.tex:224-264（$\varphi^+(M)=\mathcal D_{X\to Y}\otimes_{\mathcal D_Y}M$、定理 4.2.2）`

## 核验

状态：`external-confirmed`（2026-11-19）
- nLab：https://ncatlab.org/nlab/show/D-module — 该页「Six operations yoga」一节称「Discussion of six operations yoga for pull-push of (coherent, holonomic) D-modules is in (Bernstein, around p. 18)」，即 $\mathcal D$-模上确有拉回（逆像）与推回（直像）两族运算并构成六运算；支持卡中「沿 $\varphi$ 存在逆像函子 $\varphi^+$、它与直像配对」这一断言。卡内具体构造 $\varphi^+(V)=\mathcal D_{X\to Y}\otimes_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}V$ 与定理 4.3.6 属讲义 §3，不在该页。
- nLab：https://ncatlab.org/nlab/show/six+operations — 该页 Idea 段把六运算规定为「(derived direct image)/(derived inverse image) adjunction $(f^\ast\dashv f_\ast)$」加「$(f_!\dashv f^!)$」再加张量/内 Hom 伴随，并把 Beck–Chevalley 型基变换列为相容条件；支持卡中「逆像与直像成伴随、且逆像的复合相容性属六运算公理」这一框架断言，具体公式仍以讲义为准。

## 关联

- `dmod/concept/bimodule-dx-to-y`
- `dmod/concept/derived-inverse-image`
- `dmod/concept/cohomological-dimension-of-i-plus`
