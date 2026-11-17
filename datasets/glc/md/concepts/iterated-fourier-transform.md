---
id: glc/concept/iterated-fourier-transform
type: concept
track: C
---

# 沿 mirabolic 子群的迭代 Fourier 变换

> V(K)^⊥ 上 L_1(K) 只有两条轨道（开轨道与 {0}），Fourier 变换据此分解 C^∞(Q_1(K)\G(𝔸))，逐次降秩后只剩一般位置 Whittaker 系数。

**问题**：L_1(K) 在 V(K)^⊥ 上的两条轨道各给出分解中的哪一个因子？

## 定义

在迭代证明中使用 mirabolic 子群 $Q_1=L_1\ltimes V$，其中 $L_1\simeq\operatorname{GL}_{n-1}$，而不使用完整的极大抛物子群。$V(K)\backslash V(\mathbb{A})$ 上的 Fourier 变换使用 $V(K)^\perp=\operatorname{Ch}(V(\mathbb{A})/V(K))$，其中 $\operatorname{Ch}(-)$ 是特征标群（Pontryagin 对偶）。$L_1(K)$ 在 $V(K)^\perp$ 上的作用有两个轨道：(1) 经过非零特征标 $\eta_{n-1}$ 的开轨道，其稳定子是较小的 mirabolic 子群 $Q'_1(K)\subset\operatorname{GL}_{n-1}(K)$；(2) 闭轨道 $\{0\}$，其稳定子为 $L_1(K)$。

*记号*：$Q_1=L_1\ltimes V$，$L_1\simeq\operatorname{GL}_{n-1}$，$V$ 为其标准表示；$\operatorname{Ch}(-)$ 只在全书此节出现，指特征标群；$\eta_{n-1}$ 是非零特征标的代表。

## 要点

- Fourier 变换给出的分解：$C^\infty(Q_1(K)\backslash G(\mathbb{A}))\simeq C^\infty((Q'_1(K)\ltimes V(\mathbb{A}),\eta_{n-1})\backslash G(\mathbb{A}))\times C^\infty(L_1(K)\ltimes V(\mathbb{A})\backslash G(\mathbb{A}))$。
- 若 $n\ge3$，则 $Q'_1=L'_1\ltimes V'$ 是 $\operatorname{GL}_{n-1}$ 中的 mirabolic 子群；第一个因子又是秩 $n-1$ 的 Whittaker 型空间，因为 $Q'_1(\mathbb{A})$ 作用在 $C^\infty((V(\mathbb{A}),\eta_{n-1})\backslash G(\mathbb{A}))$ 上。
- 第二个因子包含在 $C^\infty(Q'_1(K)\ltimes V(\mathbb{A})\backslash G(\mathbb{A}))$ 中，并被尖点性消去；迭代这种降低秩的 Fourier 变换后，只剩下一般位置 Whittaker 系数。
- 对极大抛物子群 $Q$，范畴类比是到粘合的扩展 Whittaker 范畴的全忠实函子 $D(\operatorname{Bun}_G^{Q\text{-gen}})\hookrightarrow\sum_{P\supset B}D(\operatorname{Bun}_G^{Z_M\text{-gen},\mathrm{Wh}_P})$；由 $P$ 标记的部分将特征标 $\Psi_P$ 与 $Z_M(K)$ 约化的退化系数几何化。

## 关键公式

- $V(K)^\perp=\operatorname{Ch}(V(\mathbb{A})/V(K))$
- $C^\infty(Q_1(K)\backslash G(\mathbb{A}))\simeq C^\infty((Q'_1(K)\ltimes V(\mathbb{A}),\eta_{n-1})\backslash G(\mathbb{A}))\times C^\infty(L_1(K)\ltimes V(\mathbb{A})\backslash G(\mathbb{A}))$
- $D(\operatorname{Bun}_G^{Q\text{-gen}})\hookrightarrow\sum_{P\supset B}D(\operatorname{Bun}_G^{Z_M\text{-gen},\mathrm{Wh}_P})$

## 定理与证明

### Fourier 变换给出的分解与降秩（要点（有缺口））

由 $L_1(K)$ 在 $V(K)^\perp$ 上只有两条轨道，Fourier 变换给出 $C^\infty(Q_1(K)\backslash G(\mathbb{A}))\simeq C^\infty((Q'_1(K)\ltimes V(\mathbb{A}),\eta_{n-1})\backslash G(\mathbb{A}))\times C^\infty(L_1(K)\ltimes V(\mathbb{A})\backslash G(\mathbb{A}))$；第二个因子被尖点性消去，迭代后只剩一般位置 Whittaker 系数。

1. 分类 $L_1(K)$ 在 $V(K)^\perp$ 上的轨道：开轨道（稳定子 $Q'_1$）与闭轨道 $\{0\}$（稳定子 $L_1$）。  
   *为什么*：讲义直接陈述轨道分类，未给证明。
2. 沿两条轨道作 Fourier 变换，得到两个因子的直积。  
   *为什么*：讲义用「因此」一笔带过，未逐项验证。
3. 说明第二个因子含于 $C^\infty(Q'_1(K)\ltimes V(\mathbb{A})\backslash G(\mathbb{A}))$，被尖点性消去。  
   *为什么*：讲义只作断言。

> 缺口：讲义由两条轨道「因此」直接写出分解，未逐项验证 Fourier 变换在开、闭轨道上的作用；轨道分类本身也未证明。证明的完整版本见 [FGKV98] 的 mirabolic 迭代。

*出处*：§3.9（原书 p.24–25）


## 易错点

- $V(K)^\perp$ 是特征标群 $\operatorname{Ch}(V(\mathbb{A})/V(K))$，不是 $V(\mathbb{A})$ 中的正交补空间；当成子空间就看不出 $L_1(K)$ 为什么在其上有轨道。
- 第二个因子被消去靠的是「包含在 $C^\infty(Q'_1(K)\ltimes V(\mathbb{A})\backslash G(\mathbb{A}))$ 中」这一步外加尖点性，不是 Fourier 变换本身给出的。
- $Q'_1$ 是 $\operatorname{GL}_{n-1}$ 中的 mirabolic 子群（由 $\eta_{n-1}$ 给出），不是原 $Q_1$；两者所在群不同，不要混用。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§3.9 沿 mirabolic 子群迭代 Fourier 变换，p.24-25（PDF p.24-25），`源码/chapters/ch03.tex:164-194（§3.9）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/affine+Grassmannian — V(K)^⊥=Ch(V(A)/V(K))；两条轨道（开轨道/闭轨道）；Fourier 分解 C^∞(Q_1(K)\G(A))≃…
- Gai18：https://arxiv.org/abs/1811.02468 — D(Bun_G^{Q-gen})↪Σ_P D(Bun_G^{Z_M-gen,Wh_P})

## 关联

- `glc/concept/degenerate-whittaker-characters`
- `glc/concept/coherent-compactification`
