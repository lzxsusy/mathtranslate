---
id: dmod/concept/direct-image-functor
type: concept
track: D
---

# 直像函子 $\varphi_+$

> 右 $\mathcal D_X$-模的直像须先张量相对双模再取 $\mathcal O$-模直像，才能得到 $\mathcal D_Y$-模。

**问题**：为什么 $\mathcal O$-模直像不能直接给 $V$ 一个 $\mathcal D_Y$-结构，$\varphi_+$ 的正确定义是什么、何时正合？

## 定义

对右 $\mathcal D_X$-模复形 $V^\bullet$，置 $$\varphi_+(V^\bullet)=R\varphi_\bullet\bigl(V^\bullet\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y}\bigr),$$ 其中 $\varphi_\bullet$ 是 $\mathcal O$-模直像，$\mathcal D_{X\to Y}$ 经其右作用成为右 $\mathcal D_X$-模。这给出函子 $D(M_R(\mathcal D_X))\to D(M_R(\mathcal D_Y))$。仿射情形 $\varphi_+(N)=N\otimes_{\mathcal D_X}\mathcal D_{X\to Y}$，其左导出为 $L_j\varphi_+(N)=\operatorname{Tor}^{\mathcal D_X}_j(N,\mathcal D_{X\to Y})$；讲义 §2 用转置双模 $\mathcal D_{Y\leftarrow X}$ 把左模写法记为 $F_+(M)=\mathcal D_{Y\leftarrow X}\otimes_{\mathcal D_X}M$。

*记号*：$V^\bullet\in D(M_R(\mathcal D_X))$：右 $\mathcal D_X$-模的导出范畴；$\varphi_\bullet$：$\mathcal O$-模直像；$\mathcal D_{Y\leftarrow X}$：$\mathcal D_{X\to Y}$ 两个作用取转置所得的 $(\mathcal D_Y,\mathcal D_X)$-双模；$L_j\varphi_+$：同调编号的左导出函子。

## 要点

- 定义 $\varphi_+(V^\bullet)=R\varphi_\bullet(V^\bullet\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y})$；$\mathcal O$-模直像 $\varphi_\bullet$ 一般不给 $\mathcal D_Y$-结构（$X=\{0\}$ 的反例见 §11 开头），必须先张量再导出。
- 开包含 $i:U\hookrightarrow X$：$i_+=Ri_\bullet$（注 4.5.2）；闭光滑浸入时 $i_+$ 是 $H^0\circ i_+\circ D$ 的右导出函子（定理 4.6.4）。
- 复合：$\psi_+\circ\varphi_+\cong(\psi\circ\varphi)_+$（定理 4.5.3），证明用投影公式（引理 4.4.5）；$\varphi_+$ 保持有限振幅（引理 4.5.1）。
- 仿射情形（命题 4.5.5）：$H^p\varphi_+V$ 拟凝聚，$p>0$ 时为零，且 $\Gamma(Y,H^p\varphi_+V)=\operatorname{Tor}^{-p}_{\mathcal D_X}(\Gamma(X,V),\mathcal D_{X\to Y})$（$p\le0$）。

## 关键公式

- $\varphi_+(V^\bullet)=R\varphi_\bullet\bigl(V^\bullet\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y}\bigr)$
- $\psi_+\circ\varphi_+\cong(\psi\circ\varphi)_+$
- $i_+=Ri_\bullet\qquad(i\ \text{开包含})$
- $\Gamma(Y,H^p\varphi_+V)=\operatorname{Tor}^{-p}_{\mathcal D_X}\bigl(\Gamma(X,V),\mathcal D_{X\to Y}\bigr)\quad(\text{仿射},\ p\le0)$
- $F_+(M)=\mathcal D_{Y\leftarrow X}\otimes_{\mathcal D_X}M,\qquad \mathcal D_{Y\leftarrow X}=\mathcal D_Y\otimes_{\varphi^{-1}\mathcal D_X}\varphi^{-1}\mathcal D_X$

## 定理与证明

### 定理 4.5.3（直像的复合）（完整）

对态射 $\varphi:X\to Y$、$\psi:Y\to Z$，有 $\psi_+\circ\varphi_+\cong(\psi\circ\varphi)_+$。

1. 把 $\mathcal D_{X\to Y}$、$\mathcal D_{Y\to Z}$ 都看作 $(\mathcal D_Y\otimes_k\psi^{-1}\mathcal D_Z^{\mathrm{opp}})$-模层，并用 $\mathcal D_{X\to Z}=\mathcal D_{X\to Y}\otimes_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}\mathcal D_{Y\to Z}$。  
   *为什么*：复合双模的分解是命题 4.1.7，逐点成立，故可作为层的等同使用。
2. 对 $\varphi$ 用投影公式的 $\mathcal D$-模关键形式：$R\varphi_\bullet(V^\bullet)\otimes^L_{\mathcal D_Y}\mathcal D_{Y\to Z}=R\varphi_\bullet\bigl(V^\bullet\otimes^L_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}\mathcal D_{Y\to Z}\bigr)$。  
   *为什么*：这正是引理 4.4.5；其证明把双模看作 $\mathcal D_Y\otimes_k\psi^{-1}\mathcal D_Z^{\mathrm{opp}}$-模层，从而化到命题 4.4.2。
3. 由张量积的结合律，$V^\bullet\otimes^L_{\mathcal D_X}\mathcal D_{X\to Z}\cong(V^\bullet\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y})\otimes^L_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}\mathcal D_{Y\to Z}$。  
   *为什么*：第 1 步的分解把 $\mathcal D_{X\to Z}$ 写成两段张量，导出张量积的结合律适用。
4. 于是 $\psi_+(\varphi_+V^\bullet)=R\psi_\bullet R\varphi_\bullet\bigl(V^\bullet\otimes^L_{\mathcal D_X}\mathcal D_{X\to Z}\bigr)=(\psi\circ\varphi)_+V^\bullet$。  
   *为什么*：第 2、3 步给出两个 $R\varphi_\bullet$ 与张量积的交换，$R\psi_\bullet\circ R\varphi_\bullet=R(\psi\circ\varphi)_\bullet$ 是 $\mathcal O$-模直像的复合。

*出处*：定理 4.5.3 / 原书 §5，p.112–113


## 易错点

- $\varphi_+$ 作用在右 $\mathcal D_X$-模上；对左模须先转成转置双模 $\mathcal D_{Y\leftarrow X}$（讲义 §2 的 $F_+$），否则张量的一侧会错。
- 不能把 $\varphi_+$ 写成 $\mathcal O$-模直像：$\varphi_\bullet$ 只给 $\mathcal O_Y$-模，取 $\mathcal D_Y$-结构必须经 $\mathcal D_{X\to Y}$ 并导出化（$R\varphi_\bullet$ 不可省）。
- 导出性不可省：一般态射下 $H^p\varphi_+$ 未必为零；只有开包含、仿射态射与闭浸入等情形才有正合性结论（注 4.5.2、命题 4.5.5、定理 4.6.4）。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§5 直像函子，p.111-112-113-114（PDF p.117-118-119-120），`源码/chapters/chap4.tex:624-764（定理 4.5.3、命题 4.5.5）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§11 直像，p.47-48（PDF p.53-54），`源码/chapters/chap1.tex:1662-1789（$F_+(M)=\mathcal D_{Y\leftarrow X}\otimes_{\mathcal D_X}M$、命题 11.2）`

## 核验

状态：`external-confirmed`（2026-11-19）
- nLab：https://ncatlab.org/nlab/show/D-module — 该页「Six operations yoga」一节称对（凝聚、完整）$\mathcal D$-模的 pull-push 有六运算 yoga，即直像（推回）作为 $\mathcal D$-模的运算是存在且成体系的；支持卡中「$\varphi_+$ 是 $\mathcal D$-模层面的直像运算」这一断言。卡内显式公式 $\varphi_+=R\varphi_\bullet(V\otimes^L\mathcal D_{X\to Y})$ 与定理 4.5.3 属讲义 §5，不在该页。
- nLab：https://ncatlab.org/nlab/show/six+operations — 该页把「$(f_!\dashv f^!)$」与直像的函子性（$f\mapsto f_!$ 构成 2-函子）列为六运算公理，并列出基变换相容条件；支持卡中「直像与逆像成伴随、直像的复合与基变换相容」这一框架断言。

## 关联

- `dmod/concept/bimodule-dx-to-y`
- `dmod/concept/projection-formula`
- `dmod/concept/direct-image-of-immersion`
