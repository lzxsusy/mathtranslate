---
id: glc/concept/fourier-tower
type: concept
track: D
---

# Fourier 塔：F_k 的递归

> 逐层先作 j_{k,!} 延拓再作相对 Fourier 变换得到 F_k；F_n 在 Bun'_n∩C'_n 上等于 Aut'_E。

**问题**：F_{k+1} 为什么要先取 j_{k,!} 再作相对 Fourier 变换？

## 定义

归纳定义 $F_k$。首先
\[
F_1:=q_1^*\mathcal{L}_E[\text{移位}](\text{扭曲}),
\]
其中 $q_1:C'_1\to\operatorname{Tor}$ 取 $\mathcal{O}_X=\Omega_X^0\hookrightarrow M_1$ 的商。若 $j_k:C'_k\hookrightarrow\overline{C}'_k$ 为开嵌入，则
\[
F_{k+1}:=\mathsf{F}_{\overline{C}'_k/C_k}(j_{k,!}F_k)|_{\mathcal{E}_{k+1}^{\ne0}}.
\]
这里 $\mathcal{E}_{k+1}^{\ne0}$ 是中间项属于 $C_{k+1}$ 且典范截面 $\Omega_X^k\to M_{k+1}$ 在一般点单射的开部分。不会造成混淆时，借助从扩张类到中间项的遗忘映射，将这一限制看作 $C'_{k+1}$ 上的层。函子 $\mathsf{F}_{\overline{C}'_k/C_k}$ 是 $C_k$ 上两个对偶向量丛之间的 Fourier–Deligne 变换。

*记号*：讲义原文用 [移位]（扭曲）作占位记号，具体移位与扭转按相对维数取（与 §5.2 的 $[r](r/2)$ 归一化同型）；$\mathcal{E}_{k+1}$ 见「开子叠 C_k 与三个条件」一张卡。

## 要点

- 递归以逐层的 $!$-延拓 $j_{k,!}F_k$ 为输入，再做相对 Fourier 变换。
- $\mathcal{E}_{k+1}^{\ne0}$ 的选取保证下一步的截面在一般点单射，从而落在 $C'_{k+1}$ 上。
- 相对 Fourier 变换是逐纤维做的：$\mathcal{E}_{k+1}$ 与 $\overline{C}'_k$ 都是 $C_k$ 上的向量丛，$C_k$ 本身不动。
- $F_n$ 用紧化 Whittaker 叠 $Q_n$ 计算，允许目标落在 $\operatorname{Coh}_n$ 而非 $\operatorname{Bun}_n$。

## 关键公式

- $F_1=q_1^*\mathcal{L}_E[\text{移位}](\text{扭曲})$
- $F_{k+1}=\mathsf{F}_{\overline{C}'_k/C_k}(j_{k,!}F_k)|_{\mathcal{E}_{k+1}^{\ne0}}$
- $F_n|_{\operatorname{Bun}'_n\cap C'_n}=\operatorname{Aut}'_E|_{\operatorname{Bun}'_n\cap C'_n}$

## 定理与证明

### $F_n$ 与初步自守层的等同（要点（有缺口））

在 $\operatorname{Bun}'_n\cap C'_n$ 上，结果是初步的自守层：
\[
F_n|_{\operatorname{Bun}'_n\cap C'_n}=\operatorname{Aut}'_E|_{\operatorname{Bun}'_n\cap C'_n}.
\]
更一般地，$F_n$ 由紧化 Whittaker 叠
\[
Q_n=\left\{\begin{array}{l}0=M_0\subset M_1\subset\cdots\subset M_n,\quad M_i/M_{i-1}\simeq\Omega_X^{n-i},\\ M_n\hookrightarrow M,\quad M\in C_n,\ \operatorname{coker}(M_n\hookrightarrow M)\ \text{torsion}\end{array}\right\}
\]
计算，它取代未紧化的 Whittaker 叠；由于必须保留挠缺陷，允许目标属于 $\operatorname{Coh}_n$，而不仅属于 $\operatorname{Bun}_n$。

1. $F_1$ 从 $q_1^*\mathcal{L}_E$ 起步，与 §5.1 中 $\operatorname{Aut}'_E$ 的构造使用同一个挠商。  
   *为什么*：两者都以 $\mathcal{L}_E$ 沿 $q_1$ 的拉回为输入。
2. 每一步先取 $j_{k,!}$ 延拓，再作相对 Fourier 变换，层级由 $\mathcal{E}_{k+1}$ 从 $k$ 推到 $k+1$。  
   *为什么*：$\overline{C}'_k\to C_k$ 的对偶向量丛正是 $\mathcal{E}_{k+1}$。
3. 到 $k=n$ 时把 $F_n$ 限制到 $\operatorname{Bun}'_n\cap C'_n$，即得 $\operatorname{Aut}'_E$。  
   *为什么*：这是讲义对递归终点的陈述。

> 缺口：讲义只陈述这一等同（并说明 $F_n$ 由 $Q_n$ 计算），未在此处证明；它把 §5.1 的 $\operatorname{Aut}'_E$ 定义与 Fourier 递归对接起来。

*出处*：§6.1 开子叠 C_k 上的 Fourier 塔（未编号陈述）/ 原书 p.36–37


## 易错点

- 先取 $j_{k,!}$ 再变换，是为了让结果只落在 $\mathcal{E}_{k+1}^{\ne0}$ 上：缺了 $!$-延拓，支撑会伸到有挠缺陷的边界上。
- $\mathcal{E}_{k+1}$ 与 $\overline{C}'_k$ 是 $C_k$ 上的对偶向量丛，变换的移位与扭转按相对维数取，而不是按 $X$ 的维数。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§6.1 开子叠 C_k 上的 Fourier 塔，p.36-37（PDF p.36-37），`源码/chapters/ch06.tex:24-38（§6.1 F_k 递归与 Q_n）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Fourier-Mukai+transform — 页面给出 Φ(A) := (p_Y)_*(E⊗p_X^*A)：Fourier–Mukai 变换是沿对应核 E 的『拉回—张量—推前』积分变换、可相对基做，与卡里『F 是 C_k 上两个对偶向量丛之间的相对 Fourier 变换、逐纤维做』的构造形式一致；但页面只讨论 QCoh 上的 Fourier–Mukai，不含 Fourier–Deligne 的移位/扭转归一化，也不含 F_1=q_1^*L_E、F_n=Aut'_E 与 Q_n 的紧化表述。

## 关联

- `glc/concept/opens-c-k-conditions`
- `glc/concept/fourier-deligne-transform`
- `glc/concept/cleanness-theorem`
