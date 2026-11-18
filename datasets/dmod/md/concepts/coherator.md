---
id: dmod/concept/coherator
type: concept
track: C
---

# 凝聚化函子（coherator）$Q_X$

> 遗忘函子 $\mathcal M_{qc}(\mathcal O_X)\to\mathcal M(\mathcal O_X)$ 有右伴随 $Q_X$，仿射时 $Q_X(W)=\widetilde{\Gamma(X,W)}$，它左正合。

**问题**：整体截面只在拟凝聚模上表现良好，如何构造一个右伴随把任意 $\mathcal O_X$-模「凝聚化」，代价又是什么？

## 定义

设 $X$ 是特征零代数闭域 $k$ 上的代数簇，$\operatorname{For}:\mathcal M_{qc}(\mathcal O_X)\to\mathcal M(\mathcal O_X)$ 是遗忘函子。引理 4.1 断言它有右伴随 $Q_X:\mathcal M(\mathcal O_X)\to\mathcal M_{qc}(\mathcal O_X)$，即对任意拟凝聚 $V$ 与任意 $W$ 有 $\operatorname{Hom}_{\mathcal O_X}(V,W)=\operatorname{Hom}_{\mathcal O_X}(V,Q_X(W))$。函子 $Q_X$ 称为凝聚化函子（coherator）。仿射时 $Q_X(W)=\widetilde{\Gamma(X,W)}=\mathcal O_X\otimes_{R(X)}\Gamma(X,W)$；一般情形由仿射开覆盖上的 Čech 分解取核得到。

*记号*：$\operatorname{For}$：遗忘函子；$Q_X$：其右伴随；$\widetilde M=\mathcal O_X\otimes_{R(X)}M$：$R(X)$-模的局部化；$i:U\to X$：开浸入。

## 要点

- $Q_X$ 是遗忘函子的右伴随（引理 4.1）：它把任意 $\mathcal O_X$-模换成拟凝聚模而不改变到拟凝聚模的态射。
- 仿射时 $Q_X(W)=\widetilde{\Gamma(X,W)}$，因为 $\Gamma$ 与局部化在该情形互逆。
- 四条基本性质（命题 4.2）：左正合；把入射映为入射；$Q_X\circ\operatorname{For}\cong\mathrm{id}$；$Q_X\circ i_*\cong i_*\circ Q_U$。
- 仿射时 $R^pQ_X(W)=\widetilde{H^p(X,W)}$（引理 4.4），故 $Q_X$ 不是正合函子。
- 拟凝聚 $\mathcal O_X$-模对 $Q_X$ 无环（命题 4.6），且 $\operatorname{Ext}^\bullet_{\mathcal M_{qc}}=\operatorname{Ext}^\bullet_{\mathcal M}$（定理 4.7）。

## 关键公式

- $\operatorname{Hom}_{\mathcal O_X}(V,W)=\operatorname{Hom}_{\mathcal O_X}(V,Q_X(W))$
- $Q_X(W)=\widetilde{\Gamma(X,W)}\quad(X\ \text{仿射})$
- $R^pQ_X(W)=\widetilde{H^p(X,W)}$
- $Q_X\circ\operatorname{For}\cong\operatorname{id}$

## 定理与证明

### 引理 4.1（遗忘函子有右伴随）（完整）

从 $\mathcal M_{qc}(\mathcal O_X)$ 到 $\mathcal M(\mathcal O_X)$ 的遗忘函子 $\operatorname{For}$ 有右伴随函子 $Q_X:\mathcal M(\mathcal O_X)\to\mathcal M_{qc}(\mathcal O_X)$。

1. 仿射情形：$\Gamma$ 与局部化 $\widetilde{\ }$ 互逆，故 $\operatorname{Hom}_{\mathcal O_X}(V,W)=\operatorname{Hom}_{\mathcal O_X}(\widetilde{\Gamma(X,V)},W)=\operatorname{Hom}_{R(X)}(\Gamma(X,V),\Gamma(X,W))$，此时 $Q_X(W)=\widetilde{\Gamma(X,W)}$。  
   *为什么*：张量-同态伴随把 $\mathcal O_X$-线性同态换成 $R(X)$-线性同态，于是 $W$ 只需以 $\Gamma(X,W)$ 出现。
2. 开仿射子集 $i:U\to X$：$\operatorname{Hom}_{\mathcal O_X}(V,i_*W)=\operatorname{Hom}_{\mathcal O_U}(V|_U,W)=\operatorname{Hom}_{\mathcal O_X}(V,i_*Q_U(W))$，故 $Q_X\circ i_*\cong i_*\circ Q_U$。  
   *为什么*：直像与限制互为伴随，且开浸入的直像保持拟凝聚性。
3. 一般 $X$：取仿射开覆盖 $(U_i)$，用 Čech 分解 $0\to W\to\bigoplus_i f_{i*}(W|_{U_i})\to\bigoplus_{i<j}f_{ij*}(W|_{U_i\cap U_j})$ 与前一步的相容性，把第一个微分「凝聚化」为 $\delta:\bigoplus_i f_{i*}(Q_{U_i}(W|_{U_i}))\to\bigoplus_{i<j}f_{ij*}(Q_{U_i\cap U_j}(W|_{U_i\cap U_j}))$。  
   *为什么*：局部已构造好的 $Q_{U_i}$ 通过 Čech 分解的分量相容性可以整体化。
4. 令 $Q(W)=\ker\delta$，它拟凝聚；由 $\operatorname{Hom}(V,-)$ 的左正合性得 $\operatorname{Hom}_{\mathcal O_X}(V,W)=\operatorname{Hom}_{\mathcal O_X}(V,Q(W))$，故 $Q_X$ 是右伴随。  
   *为什么*：核在同态群上给出正合列的左端，左正合性保证所需同构。

*出处*：引理 4.1 / chap3.tex:337-374

### 命题 4.2（$Q_X$ 的基本性质）（要点（有缺口））

函子 $Q_X$ 满足：(i) 左正合；(ii) 把 $\mathcal M(\mathcal O_X)$ 中的入射对象映为 $\mathcal M_{qc}(\mathcal O_X)$ 中的入射对象；(iii) $Q_X\circ\operatorname{For}\cong\mathrm{id}$；(iv) 对开子簇 $i:U\to X$ 有 $Q_X\circ i_*\cong i_*\circ Q_U$。

1. (i) 是任意右伴随函子的性质；(ii) 是正合函子之右伴随的性质。  
   *为什么*：右伴随左正合、正合函子的右伴随保入射，都是伴随对的一般事实。
2. (iii) 由 $Q_X$ 的定义直接得到。  
   *为什么*：拟凝聚模已经凝聚，$Q_X$ 在它上面只需作为恒等出现。

> 缺口：(iv) 的证明见 chap3.tex:393-397（用开浸入的直像与限制的伴随关系），本卡从略。

*出处*：命题 4.2 / chap3.tex:378-397


## 易错点

- $Q_X$ 不是正合的：仿射时 $R^pQ_X(W)=\widetilde{H^p(X,W)}$，$p>0$ 时一般不为零，故不能用 $Q_X$ 直接做消解。
- 无环性只在拟凝聚模上成立（命题 4.6）；对一般 $\mathcal O_X$-模要用引理 4.5 的条件 (V)，不能默认 $Q_X$ 无环。
- $Q_X\circ\operatorname{For}\cong\mathrm{id}$ 是「拟凝聚一侧」的同构；反向 $\operatorname{For}\circ Q_X\cong\mathrm{id}$ 一般不成立。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 III 章 §4 Coherentor（凝聚化函子），p.86（PDF p.92），`源码/chapters/chap3.tex:337-385（引理 4.1 与命题 4.2）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本，第 III 章 §4 译者注，p.89（PDF p.95），`源码/chapters/chap3.tex:488-490（译者注：coherator 的动机）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/coherent-d-module`
- `dmod/concept/quasi-coherent-d-module`
