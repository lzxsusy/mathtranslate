# Białynicki–Birula 分解与上行流

> `hausel22/concept/bialynicki-birula-attraction` · 轨道 D · 幂零锥上的等变重数 · 状态 dev

> **先自测**：为什么需要「半射影」这个条件才能作 BB 分解？

## 一句话

在 $\T=\C^\times$ 的半射影作用下，簇按「沿 $\lambda\to0$ 的极限点」分解成上行流，按「沿 $\lambda\to\infty$ 的极限」给出芯。

## 定义

设 $\T=\C^\times$ 作用在有限型既约分离概形 $X$ 上。称作用半射影（semiprojective），若：(1) 作用是线性的，即存在 $X\hookrightarrow\P^N$ 的局部闭 $\T$-等变嵌入且 $\T$ 在 $\P^N$ 上线性；(2) 不动点子簇 $X^\T$ 是 proper 的（从而射影）；(3) 对一切 $x\in X$，$\lim_{\lambda\to0}\lambda\cdot x$ 存在。对 $\alpha\in X^\T$ 定义上行流 $W^+_\alpha:=\{x\mid\lim_{\lambda\to0}\lambda x=\alpha\}$、下行流 $W^-_\alpha:=\{x\mid\lim_{\lambda\to\infty}\lambda x=\alpha\}$，则有 BB 分解 $X=\coprod_{\alpha\in X^\T}W^+_\alpha$，并称 $\calC:=\coprod_{\alpha\in X^\T}W^-_\alpha$ 为 $X$ 的芯。

**记号**：$\T=\C^\times$；$X^\T$；$W^\pm_\alpha$；$\calC$；半射影。

## 要点（为什么需要它）

1. 第 (3) 条是核心：$\lambda\to0$ 的极限必须存在，BB 分解才成立；没有它，流可以「跑到无穷远」。
2. 第 (2) 条保证 $X^\T$ 有限且每个流有紧的「源」；配合第 (1) 条的线性化才能用 Białynicki–Birula 的原始定理。
3. Hitchin 系统的 $\T$ 作用 $\lambda:(E,\Phi)\mapsto(E,\lambda\Phi)$ 满足这三条：$h$ 是 $\T$-等变的且权全为正，故 $\M$ 半射影。
4. 芯 $\calC$ 在 $\M$ 上的原像就是幂零锥 $h^{-1}(0)_{red}$：下行流的并恰好是「$\Phi$ 幂零」的那部分。
5. 定理 3.1 说：在光滑轨迹上，$W^\pm_\alpha\cong T^\pm_\alpha X$ 是局部闭子簇；当辛形式齐次度为 1 时，$W^+_\alpha$ 与 $\calC$ 都是拉格朗日的。

## 核心公式

$$
$$X=\coprod_{\alpha\in X^\T}W^+_\alpha,\qquad \calC=\coprod_{\alpha\in X^\T}W^-_\alpha$$$$W^+_\alpha=\{x\mid \lim_{\lambda\to 0}\lambda\cdot x=\alpha\}$$
$$

$$
$$W^+_\alpha=\{x\mid \lim_{\lambda\to 0}\lambda\cdot x=\alpha\}$$
$$

## 定理与证明（或缺口）

### BB 分解的几何性质（定理 3.1）

设 $\alpha\in(X^s)^\T$ 是光滑轨迹上的不动点，则 $W^\pm_\alpha\subset X$ 是局部闭子簇，且作为 $\T$-簇 $W^\pm_\alpha\cong T^\pm_\alpha X$；若 $\omega\in\Omega^2(X^s)$ 是齐次度为 1 的辛形式，则 $W^+_\alpha$ 与芯 $\calC$ 都是拉格朗日子簇。

> 证明状态：**sketch**。原文引用 Białynicki–Birula 原文与 [HH, Prop 2.1, 2.10]，未给证明。

出处：`A p.2236`

## 常见误解

- 上行流与下行流的定义方向极易写反：$W^+$ 是 $\lambda\to0$ 的极限，$W^-$ 是 $\lambda\to\infty$ 的极限。
- BB 分解要求「$\lambda\to0$ 的极限存在」；对非半射影的作用，这个分解不成立，不能默认它可用。
- 芯 $\calC$ 不是「最小的流」，而是全部下行流之并；在 $\M$ 上它就是幂零锥（取既约结构）。
- 定理 3.1 只在光滑轨迹 $(X^s)^\T$ 上成立；在奇点处 $W^\pm_\alpha$ 未必是簇、也未必同构于切空间。

## 相关卡

[非常稳定 Higgs 丛](../concepts/very-stable-higgs-bundle.md) · [等变重数 $m_\calE(t)$](../concepts/equivariant-multiplicity.md) · [Hitchin 系统](../concepts/hitchin-system.md)

## 出处（印刷页）

- A p.2236（A p.2236）
- A p.2236（A p.2236 eq (3.1)）

> 说明：A=原文 §3.1.1 的半射影三条件、流的定义与定理 3.1 的陈述；B=把「为什么需要这三条」逐条解释；C=「芯的原像是幂零锥」按 §3.1.2 末的原文补。最没把握处：定理 3.1 第三步（辛形式齐次度 1 ⇒ 拉格朗日）的原文证明在 [HH]，此处只能给思路。
