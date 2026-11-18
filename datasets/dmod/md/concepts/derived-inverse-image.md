---
id: dmod/concept/derived-inverse-image
type: concept
track: D
---

# 导出逆像 $L\varphi^+$

> 逆像的导出化：由相对双模与导出张量积定义，可用平坦分解计算；与遗忘函子、复合相容，是六运算中逆像一族的导出版本。

**问题**：为什么 $L\varphi^+$ 可用平坦 $\mathcal D_Y$-模分解直接计算，它与 $\mathcal O$-模的导出拉回又是什么关系？

## 定义

对 $V^\bullet\in D^-(\mathcal D_Y)$，置 $$L\varphi^+(V^\bullet)=\mathcal D_{X\to Y}\otimes^L_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}(V^\bullet),$$ 这是 $\varphi^+$ 的右导出函子；同调编号写作 $L_p\varphi^+=H^{-p}L\varphi^+$。计算时可用平坦左 $\mathcal D_Y$-模分解：平坦左 $\mathcal D_Y$-模类对 $\varphi^+$ 左适合（引理 4.3.2），于是 $L\varphi^+$ 存在，且在平坦分解上直接由张量积给出。由于 $\varphi^+$ 的左同调维数有限（引理 4.3.3，$\le2\dim Y$），$L\varphi^+$ 在有界导出范畴上取值。

*记号*：$D^-(\mathcal D_Y)$：上同调有界的左 $\mathcal D_Y$-模导出范畴；$\otimes^L$：导出张量积；$L_p\varphi^+=H^{-p}L\varphi^+$：同调编号；$\operatorname{For}$：忘记 $\mathcal D$-结构的函子；$M^L_{qc}(\mathcal D_Y)$：左 $\mathcal D_Y$-模中拟凝聚者。

## 要点

- 平坦左 $\mathcal D_Y$-模类对 $\varphi^+$ 左适合：对直和封闭、每个左 $\mathcal D_Y$-模是平坦模的商、$\varphi^{-1}$ 保持平坦（引理 4.3.2），故 $L\varphi^+$ 存在并可由平坦分解计算。
- $L\varphi^+(V^\bullet)=\mathcal D_{X\to Y}\otimes^L_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}(V^\bullet)$（引理 4.3.4），这把导出逆像写成单个导出张量积。
- 与遗忘函子交换：$\operatorname{For}\circ L\varphi^+\cong L\varphi^*\circ\operatorname{For}$（定理 4.3.6）；上同调保持拟凝聚（定理 4.3.7）。
- 复合：$L\varphi^+\circ L\psi^+\cong L(\psi\circ\varphi)^+$（定理 4.3.10），双模形式为 $\mathcal D(\mathcal D_{X\to Z})=\mathcal D(\mathcal D_{X\to Y})\otimes^L\mathcal D(\varphi^{-1}\mathcal D_{Y\to Z})$（推论 4.3.11）。
- 仿射情形：$\Gamma(X,L_p\varphi^+V)=\operatorname{Tor}^{-p}_{\mathcal D_Y}(\mathcal D_{X\to Y},\Gamma(Y,V))$（命题 4.3.8）；左同调维数 $\le2\dim Y$（引理 4.3.3）。

## 关键公式

- $L\varphi^+(V^\bullet)=\mathcal D_{X\to Y}\otimes^L_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}(V^\bullet)$
- $\operatorname{For}\circ L\varphi^+\cong L\varphi^*\circ\operatorname{For}$
- $L\varphi^+\circ L\psi^+\cong L(\psi\circ\varphi)^+$
- $L_p\varphi^+(V)=\operatorname{Tor}^{\mathcal D_Y}_p\bigl(\mathcal D_{X\to Y},V\bigr)\quad(\text{仿射})$

## 定理与证明

### 引理 4.3.2（平坦类对 $\varphi^+$ 左适合）（完整）

左 $\mathcal D_Y$-模的平坦类对函子 $\varphi^+$ 是左适合的，即：对直和封闭、每个左 $\mathcal D_Y$-模是该类中某个模的商、且 $\varphi^{-1}$ 把该类送到平坦 $\mathcal O$-模；从而 $L\varphi^+$ 存在。

1. 对直和封闭：平坦左 $\mathcal D_Y$-模的直和仍平坦。  
   *为什么*：张量积与直和交换，直和项平坦则直和平坦。
2. 每个左 $\mathcal D_Y$-模 $V$ 都有自由 $\mathcal D_Y$-模的满射 $F\to V$，而自由模平坦，故 $V$ 是平坦模的商。  
   *为什么*：$\mathcal D_Y$-模张量积对自由模的计算与模同构，自由模因此平坦；满射的复合仍是满射。
3. $\varphi^{-1}$ 保持平坦：$\mathcal O_X$ 在 $\varphi^{-1}\mathcal O_Y$ 上平坦（$\varphi$ 光滑），故平坦 $\mathcal D_Y$-模经 $\varphi^{-1}$ 后对 $\varphi^+$ 无环。  
   *为什么*：$\varphi^+$ 是 $\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}\varphi^{-1}(-)$ 与 $\otimes_{\varphi^{-1}\mathcal D_Y}$ 的复合，$\mathcal O_X$ 平坦使第一层正合。
4. 由第 1–3 条，平坦类给出 $\varphi^+$ 的左适合类，故 $L\varphi^+$ 存在且在每个平坦分解上计算。  
   *为什么*：左适合类的存在性是右导出函子存在与可用该类分解计算的充分条件。

*出处*：引理 4.3.2 / 原书 §3，p.105

### 定理 4.3.6（与遗忘函子交换）（要点（有缺口））

$\operatorname{For}\circ L\varphi^+\cong L\varphi^*\circ\operatorname{For}$。


> 缺口：讲义把证明归到引理 4.3.4（$L\varphi^+=D_{X\to Y}\otimes^L_{\varphi^{-1}D_Y}\varphi^{-1}$）、引理 4.3.5（平坦 $D_Y$-模平坦于 $O_Y$）与导出函子复合定理；逐项验证未写出，详见「逆像函子」卡的同名定理。

*出处*：定理 4.3.6 / 原书 §3，p.106–107


## 易错点

- $L\varphi^+$ 不是 $\mathcal O$-模的 $L\varphi^*$：两者只经遗忘函子相等（定理 4.3.6），$\mathcal D$-结构由 $\mathcal D_{X\to Y}$ 提供。
- 分解要取左 $\mathcal D_Y$-模的平坦分解；用 $\mathcal O_Y$-平坦分解会算错，因为平坦 $\mathcal D_Y$-模平坦于 $\mathcal O_Y$ 只是单向（引理 4.3.5）。
- 把 $L\varphi^+$ 当作有界导出范畴上的函子需要左同调维数有限（引理 4.3.3）；无界情形不能直接套用。
- $L_p$ 与 $H^p$ 的编号相差一个符号（$L_p=H^{-p}$），仿射公式里的 $\operatorname{Tor}^{-p}$ 不能写成 $\operatorname{Tor}^{p}$。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§3 逆像函子（导出化），p.105-106-107-108（PDF p.111-112-113-114），`源码/chapters/chap4.tex:376-474（引理 4.3.2、引理 4.3.4、定理 4.3.6、命题 4.3.8）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§10 逆像（仿射情形），p.41-42-43（PDF p.47-48-49），`源码/chapters/chap1.tex:1467-1470（$L^iF^+(N)=\operatorname{Tor}^{-i}_{\mathcal D_Y}(\mathcal D_{X\to Y},N)$）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/inverse-image-functor`
- `dmod/concept/six-operations`
- `dmod/concept/cohomological-dimension-of-i-plus`
