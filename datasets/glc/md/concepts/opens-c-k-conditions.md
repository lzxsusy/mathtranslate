---
id: glc/concept/opens-c-k-conditions
type: concept
track: D
---

# 开子叠 C_k 与三个条件

> C_k 需满足的三条：Ext^1 消失（保证向量丛性）、归一化次数下界、商 M_k/Ω_X^{k−1} 仍属 C_{k−1}。

**问题**：开子叠 C_k 的三条条件各自保证了什么？

## 定义

对 $1\le k\le n$，令
\[
\operatorname{Coh}_k:=\{M_k\in\operatorname{Coh}(X)\mid\operatorname{rank}(M_k)=k\}.
\]
有两个截面叠：
\[
\operatorname{Coh}'_k:=\{\Omega_X^{k-1}\to M_k\text{ 在一般点单射}\},\qquad \overline{\operatorname{Coh}}'_k:=\{\Omega_X^{k-1}\to M_k\},
\]
上横线允许截面不是单射或为零。固定开子叠 $C_k\subset\operatorname{Coh}_k$，并记
\[
C'_k:=\operatorname{Coh}'_k\times_{\operatorname{Coh}_k}C_k,\qquad \overline{C}'_k:=\overline{\operatorname{Coh}}'_k\times_{\operatorname{Coh}_k}C_k.
\]
要求这些开子叠满足以下条件：
（1） 对 $M_k\in C_k$，有 $\operatorname{Ext}^1(\Omega_X^{k-1},M_k)=0$；因此 $\overline{C}'_k\to C_k$ 是纤维为 $\operatorname{Hom}(\Omega_X^{k-1},M_k)$ 的向量丛。
（2） 若 $M_k^{\mathrm{tf}}$ 是无挠商，则
\[
\mathring{\deg}(M_k^{\mathrm{tf}})>nk(2g-2),
\]
证明使用这一归一化次数形式。
（3） 若 $M_k\in C_k$ 且 $\Omega_X^{k-1}\hookrightarrow M_k$ 在一般点单射，则 $M_k/\Omega_X^{k-1}\in C_{k-1}$。
由 Serre 对偶，$\overline{C}'_k\to C_k$ 的线性对偶的纤维为 $\operatorname{Ext}^1(M_k,\Omega_X^k)$。记这一对偶向量丛为 $\mathcal{E}_{k+1}\to C_k$；它的点是扩张类
\[
0\longrightarrow\Omega_X^k\longrightarrow M_{k+1}\longrightarrow M_k\longrightarrow0.
\]
这就是下一次 Fourier 变换从层级 $k$ 移到层级 $k+1$ 的原因。

*记号*：$g$ 为 $X$ 的亏格，$n$ 为 $E$ 的秩；上横线表示允许截面非单射或为零。

## 要点

- 条件 （1） 保证 $\overline{C}'_k\to C_k$ 是向量丛，而不是一般的扩张叠。
- 条件 （2） 用归一化次数；讲义说明证明使用的是这一形式。
- 条件 （3） 使 $M_k$ 的商 $M_k/\Omega_X^{k-1}$ 仍落在下一层的开子叠 $C_{k-1}$ 中。
- $\mathcal{E}_{k+1}$ 是 $\overline{C}'_k\to C_k$ 的线性对偶，其点是扩张类，因此 Fourier 变换把层级 $k$ 推到 $k+1$。
- §5.6 已给出条件 （1）（2）；同样的 Serre 对偶计算还给出 $\operatorname{Hom}(M_k,\Omega_X^k)=0$，所以对偶扩张叠没有自同构方向。

## 关键公式

- $\operatorname{Ext}^1(\Omega_X^{k-1},M_k)=0\ \Longrightarrow\ \overline{C}'_k\to C_k$ 是纤维 $\operatorname{Hom}(\Omega_X^{k-1},M_k)$ 的向量丛
- $\mathring{\deg}(M_k^{\mathrm{tf}})>nk(2g-2)$
- $\operatorname{Ext}^1(M_k,\Omega_X^k)$ 是 $\overline{C}'_k\to C_k$ 的线性对偶的纤维

## 易错点

- 上横线不是装饰：$\overline{C}'_k$ 允许截面为零或非单射，$C'_k$ 才是其开子叠；洁净性正是跨过补集延拓。
- 条件 （3） 的方向是 $M_k/\Omega_X^{k-1}\in C_{k-1}$，不是 $M_k\in C_{k-1}$。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§5.6 开子叠 C_k 与两个所需条件，p.35（PDF p.35），`源码/chapters/ch05.tex:87-96（§5.6 条件 （1）（2） 与对偶扩张丛）`
- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§6.1 开子叠 C_k 上的 Fourier 塔，p.36（PDF p.36），`源码/chapters/ch06.tex:3-22（§6.1 开子叠与三个条件）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Serre+functor — 页面把 Serre 函子定义为 Hom(A,B) ≅ Hom(B,S(A))^*，并给出光滑射影簇 X 上 S = (·⊗ω_X)[n]。取 n=1、A=Ω_X^{k−1}、B=M_k，即得 Hom(Ω_X^{k−1},M_k)^* ≅ Ext^1(M_k,Ω_X^{k−1}⊗ω_X) = Ext^1(M_k,Ω_X^k)，正是卡里『由 Serre 对偶，线性对偶的纤维为 Ext^1(M_k,Ω_X^k)』与 E_{k+1} 的纤维描述；同一配对也说明 Ext^1(Ω_X^{k−1},M_k)=0 与 Hom(M_k,Ω_X^k)=0 等价（即卡里 key point 那句）。

## 关联

- `glc/concept/normalized-degree`
- `glc/concept/fourier-tower`
- `glc/concept/base-case-torsion-free`
