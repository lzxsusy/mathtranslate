# 对偶群与根数据

> `lbook04/concept/ch11-dual-group` · 轨 G GL_n 的 Langlands 纲领 · 状态 reviewed · 核验 source-only

**问题：** 为什么 ${}^LG$ 只决定内型与准分裂形式，而不能决定同一内型中的具体群？

**一句话：** 由 $(X,\Phi,\Delta)$ 的对偶 $(X^\vee,\Phi^\vee,\Delta^\vee)$ 造出 ${}^LG^0$，再让 $\mathcal{G}_k$ 经 $\mu$ 作用其上，得 ${}^LG={}^LG^0\rtimes\mathcal{G}_k$；它只分辨到内型，却完全决定准分裂形式。

**别名：** `L 群`、`根数据`、`Chevalley 定理`、`内型`、`pinning`

## 定义

设 $G$ 连通约化、$T\subset B$ 为极大环面与 Borel，$X=X^*(T)$、$\Phi=\Phi(G,T)$、$\Delta$ 为单根。对偶根数据把 $X$ 换成 $X^\vee=X_*$、$\Phi$ 换成 $\Phi^\vee$、$\Delta$ 换成 $\Delta^\vee$，得 $\Psi(G)=(X,\Phi,X^\vee,\Phi^\vee)$ 与基根数据 $\Psi_0(G)=(X,\Delta,X^\vee,\Delta^\vee)$。Chevalley 定理（定理 1.1）说 $\Psi(G)$ 在同构意义下决定 $G$；$\mathrm{Aut}(G)$ 由 $\mathrm{Int}(G)$ 与 $\mathrm{Aut}(\Psi_0(G))$ 组成，钉住 $(G,B,T,\{x_\alpha\})$ 就把分裂钉死。对偶化 $\Psi_0(G)^\vee=(X^\vee,\Delta^\vee,X,\Delta)$ 定义 ${}^LG^0$，再让 $\mathcal{G}_k$ 通过 $\mu:\mathcal{G}_k\to\mathrm{Aut}({}^LG^0)$ 作用，定义 1.1 给出 ${}^LG={}^LG^0\rtimes\mathcal{G}_k$。${}^LG$ 只分辨到内型：内型之间 ${}^LG$ 同构，而准分裂形式被 ${}^LG$ 完全决定，机制是 $H^1(k,G^{\mathrm{ad}})$ 与 $\mathrm{Out}(G)$。表 1 给出 $\mathrm{GL}_n\mapsto\mathrm{GL}_n(\mathbb{C})$、$\mathrm{SO}_{2n+1}\mapsto\mathrm{Sp}_{2n}(\mathbb{C})$、$\mathrm{Sp}_{2n}\mapsto\mathrm{SO}_{2n+1}(\mathbb{C})$、$\mathrm{SO}_{2n}\mapsto\mathrm{SO}_{2n}(\mathbb{C})$：$B_n$ 与 $C_n$ 互换，伴随与单连通互换。

**记号：** $X=X^*(T)$：特征格；$X^\vee=X_*(T)$：余特征格；$\Phi$：根系；$\Delta$：单根基；$\Psi(G)$：根数据；$\Psi_0(G)$：基根数据；${}^LG^0$：对偶群的连通分量；$\mu$：$\mathcal{G}_k$ 在 ${}^LG^0$ 上的作用。

## 要点

- 对偶化的次序是 $(X^\vee,\Delta^\vee,X,\Delta)$，不是逐项照抄 $(X,\Delta,X^\vee,\Delta^\vee)$；这是原书 p. 253 首行的写法，译注已核。
- 内型共享同一个 ${}^LG$，但 $\Phi(G')$ 只是 $\Phi(G)$ 的子集；准分裂形式的容许同态集最大。
- ${}^LG$ 有三种形式：Galois ${}^LG^0\rtimes\mathcal{G}_k$、Weil ${}^LG^0\rtimes W_k$、Weil–Deligne ${}^LG^0\rtimes W'_k$；本书主要用 Galois 形式。
- 表 1 的对偶是「特征格 $\leftrightarrow$ 余特征格」的直接后果，故 $\mathrm{SO}_{2n+1}$ 与 $\mathrm{Sp}_{2n}$ 互换。

## 公式

$$
\Psi(G)=(X,\Phi,X^\vee,\Phi^\vee),\qquad \Psi_0(G)=(X,\Delta,X^\vee,\Delta^\vee)
$$

$$
\Psi_0(G)^\vee=(X^\vee,\Delta^\vee,X,\Delta)
$$

$$
{}^LG={}^LG^0\rtimes\mathcal{G}_k
$$

## 定理与证明

**定理 1.1（Chevalley）**　根数据 $\Psi(G)$ 在同构意义下决定连通约化群 $G$。

*出处：译文 §1*

**定义 1.1（L 群）**　${}^L(G_{/k})={}^LG={}^LG^0\rtimes\mathcal{G}_k$，其中 $\mathcal{G}_k$ 经 $\mu$ 作用在 ${}^LG^0$ 上。

*出处：译文 §1*

## 易错点

- 把 ${}^LG$ 写成直积 ${}^LG^0\times\mathcal{G}_k$：原书误排为 $\times$，正确是半直积 $\rtimes$（译注已改）。
- 以为 ${}^LG$ 决定 $G$：它只决定内型与准分裂形式，不决定同一内型中的具体 $G$。

## 批注

**〔易错预警〕splitting 的双关**　英文 splitting 既指「分裂」也指「钉住」；原书用 pinning 强调 $(G,B,T,\{x_\alpha\})$ 这组数据把 Borel 与根向量钉死，从而 $\mathrm{Aut}(G)\to\mathrm{Aut}(\Psi_0(G))$ 可分裂。§1 的译注解释了为什么需要根向量而不只是 $(B,T)$。

## 相关

[[ch11-lgroup-reps]]、[[ch11-functoriality]]、[[ch10-local-langlands]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§1，原书 pp. 252–253（PDF pp. 254–255）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch11.tex:52-184`
