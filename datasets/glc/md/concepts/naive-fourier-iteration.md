---
id: glc/concept/naive-fourier-iteration
type: concept
track: D
---

# GL_n 的朴素 Fourier 迭代

> 对一般 n 逐层作 Fourier 变换的朴素递归 F_k；只把中间叠限制到 Bun_k 会漏掉挠余核缺陷层。

**问题**：为什么不能把朴素递归中的所有中间叠 Coh_k 都限制到 Bun_k？

## 定义

对一般 $n$，希望迭代前面的 Fourier 变换。令 $\operatorname{Coh}_k$ 为秩 $k$ 凝聚层的叠，并定义
\[
\operatorname{Coh}_k^+:=\{(M_k,\ s:\Omega_X^{k-1}\to M_k)\},\qquad \operatorname{Coh}'_k\subset\operatorname{Coh}_k^+
\]
为 $s$ 在一般点单射的开轨迹。若 $s$ 在一般点单射，则 $\operatorname{coker}(s)$ 的秩为 $k-1$，所以 $\operatorname{Coh}'_k$ 映到 $\operatorname{Coh}_{k-1}$。递归从沿商映射 $q_1:\operatorname{Coh}'_1\to\operatorname{Tor}$ 的拉回开始：
\[
F_1:=q_1^*\mathcal{L}_E,
\]
并朴素地置
\[
F_{k+1}:=\mathsf{F}(j_{k,!}F_k)|_{\operatorname{Coh}'_{k+1}},\qquad j_k:\operatorname{Coh}'_k\hookrightarrow\operatorname{Coh}_k^+,
\]
其中将 $\operatorname{Coh}'_{k+1}$ 看作 $\operatorname{Coh}_k$ 上 Serre 对偶扩张丛的开子叠。最后，$F_n$ 限制到 $\operatorname{Bun}'_n$ 后，就是 $\operatorname{Aut}'_E$ 的 Fourier 描述。

*记号*：$q_1$ 取 $\mathcal{O}_X=\Omega_X^0\hookrightarrow M_1$ 的商；$\mathsf{F}$ 是 §5.2 的 Fourier–Deligne 变换。

## 要点

- 递归的起点 $F_1=q_1^*\mathcal{L}_E$ 通过挠商 $q_1$ 与第 4 章的 $\mathcal{L}_E$ 相连。
- 每作一次 Fourier 变换，层级从 $k$ 推到 $k+1$，这来自 $\operatorname{Coh}_k$ 上的 Serre 对偶扩张丛。
- 中间开子叠不能取 $\operatorname{Bun}_k$：否则只能看到紧化 Whittaker 叠中中间商为向量丛的部分。
- 正确的开子叠 $C_k\subset\operatorname{Coh}_k$ 必须比 $\operatorname{Bun}_k$ 更大（最终定义推迟到 §5.6–§6.1）。

## 关键公式

- $F_1=q_1^*\mathcal{L}_E$
- $F_{k+1}=\mathsf{F}(j_{k,!}F_k)|_{\operatorname{Coh}'_{k+1}}$

## 定理与证明

### 朴素迭代的缺陷（要点（有缺口））

不能简单地把所有中间的 $\operatorname{Coh}_k$ 限制到 $\operatorname{Bun}_k$：若对 $k<n$ 有 $C_k\subset\operatorname{Bun}_k$，则该构造只能看到紧化 Whittaker 叠中间商为向量丛的部分，会漏掉某些 $M_k\to M$ 具有挠余核的缺陷层；因此正确的开子叠 $C_k\subset\operatorname{Coh}_k$ 必须比 $\operatorname{Bun}_k$ 更大。

1. 若取 $C_k\subset\operatorname{Bun}_k$，递归只能覆盖中间商均为向量丛的那些旗。  
   *为什么*：$\operatorname{Bun}_k$ 按定义只含向量丛。
2. 挠余核的 $M_k\to M$ 落在补集中，构造看不到这些缺陷层。  
   *为什么*：$\operatorname{Coh}_k$ 比 $\operatorname{Bun}_k$ 多出的正是含挠部分的层。
3. 故需把 $C_k$ 取得比 $\operatorname{Bun}_k$ 更大。  
   *为什么*：这是引入 §5.6 两个条件与第 6 章三条条件的动机。

> 缺口：讲义只给出这一理由（漏掉挠余核缺陷层），没有给形式证明；$C_k$ 的最终定义被推迟到 §5.6–§6.1。

*出处*：§5.5 GL_n 的朴素迭代（未编号陈述）/ 原书 p.34–35


## 易错点

- 「朴素」指尚未取正确的开子叠 $C_k$；只把 $\operatorname{Coh}_k$ 换成 $\operatorname{Bun}_k$ 会丢掉有挠余核的 $M_k\to M$。
- $\operatorname{Coh}'_k$ 与 $\operatorname{Coh}_k^+$ 不同：前者要求 $s$ 在一般点单射，后者不要求。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§5.5 GL_n 的朴素迭代，p.34-35（PDF p.34-35），`源码/chapters/ch05.tex:76-86（§5.5 朴素迭代与缺陷）`

## 核验

状态：`source-only`（2026-11-18）
- Katz–Laumon 1985 (KL85)：https://pmihes.centre-mersenne.org/item/10.1007/BF02698808.pdf — KL85 gives the single Fourier–Deligne transform F; the iteration F_{k+1}=F(j_{k,!}F_k)|_{Coh'_{k+1}} and the torsion-defect analysis are book-specific.

## 关联

- `glc/concept/fourier-deligne-transform`
- `glc/concept/normalized-degree`
- `glc/concept/fourier-tower`
