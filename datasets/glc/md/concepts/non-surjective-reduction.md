---
id: glc/concept/non-surjective-reduction
type: concept
track: D
---

# 非满射情形到满射情形的归约

> 非满射情形经仿射纤维化与因子化恒等式 (s,q)_!m^*L_E≃L_E⊠L_E 归约到满射情形。

**问题**：非满射情形最后欠下的因子化恒等式说的是什么？

## 定义

假设 $M_k\to\mathcal{T}$ 不是满射，令 $\mathcal{T}'\subsetneq\mathcal{T}$ 为其像。置 $\mathring{M}_k:=\ker(M_k\to\mathcal{T}')$，并令 $M'\subset M$ 为 $\mathcal{T}'$ 在 $M\to\mathcal{T}$ 下的逆像。则数据经由一个分解图通过，从而
\[
0\longrightarrow M'/M_k\longrightarrow M/M_k\longrightarrow\mathcal{T}/\mathcal{T}'\longrightarrow0.
\]
令 $H_{\mathcal{T}}$ 和 $H_{\mathcal{T}'}$ 为相应修改纤维。映射 $H_{\mathcal{T}}\to H_{\mathcal{T}'}$ 与挠层图相容：$\operatorname{Tor}^{\mathrm{ses}}$ 分类挠层的短正合列，$m$ 记录中间项，$(s,q)$ 记录子对象与商；在当前情形它们分别是 $M/M_k$、$M'/M_k$ 与 $\mathcal{T}/\mathcal{T}'$。

*记号*：$\mathrm{pr}$ 为剩余的投影；$H_{\mathcal{T}}$、$H_{\mathcal{T}'}$ 是相应修改纤维。

## 要点

- $\mathcal{T}'$ 是 $M_k\to\mathcal{T}$ 的像，$\mathring{M}_k=\ker(M_k\to\mathcal{T}')$。
- 拉回到挠层图后，$H_{\mathcal{T}}\to H_{\mathcal{T}'}$ 是仿射空间纤维化。
- 仿射方向由诸如 $\operatorname{Ext}^1(\mathcal{T}/\mathcal{T}',\mathring{M}_k)$ 的扩张数据与相容提升 $M_k\to M'$ 控制。
- 因子化恒等式 $(s,q)_!m^*\mathcal{L}_E\simeq\mathcal{L}_E\boxtimes\mathcal{L}_E$ 把 $\mathcal{L}_E$ 沿挠商的积分拆成两段。
- 该恒等式在第 7 章证明，是洁净性证明所欠的最后一步。

## 关键公式

- $0\to M'/M_k\to M/M_k\to\mathcal{T}/\mathcal{T}'\to0$
- $\mathrm{pr}_!((s,q)_!m^*\mathcal{L}_E|_{H_{\mathcal{T}'}})=0$
- $(s,q)_!m^*\mathcal{L}_E\simeq\mathcal{L}_E\boxtimes\mathcal{L}_E$

## 定理与证明

### 非满射情形到满射情形的归约（要点（有缺口））

拉回到该图后，$H_{\mathcal{T}}\to H_{\mathcal{T}'}$ 是仿射空间纤维化，仿射方向由诸如 $\operatorname{Ext}^1(\mathcal{T}/\mathcal{T}',\mathring{M}_k)$ 的扩张数据以及在商 $\mathcal{T}'$ 上选择相容提升 $M_k\to M'$ 控制。因此忽略通常的仿射丛移位与 Tate 扭转后，通过基变换，剩余项归约为沿剩余投影 $\mathrm{pr}$ 的推前
\[
\mathrm{pr}_!\bigl((s,q)_!m^*\mathcal{L}_E|_{H_{\mathcal{T}'}}\bigr)=0.
\]
所需的命题是 $\operatorname{Tor}$ 所用商叠归一化中的因子化恒等式
\[
(s,q)_!m^*\mathcal{L}_E\simeq\mathcal{L}_E\boxtimes\mathcal{L}_E,
\]
它在第 7 章证明；该恒等式将挠商分为 $M'/M_k$ 部分与剩余的 $\mathcal{T}/\mathcal{T}'$ 部分，从而将非满射情形归约为满射情形。

1. 写 $M_k\to\mathcal{T}$ 的像 $\mathcal{T}'$，令 $M'$ 为 $\mathcal{T}'$ 的逆像，得短正合列 $0\to M'/M_k\to M/M_k\to\mathcal{T}/\mathcal{T}'\to0$。  
   *为什么*：这是把数据沿 $\mathcal{T}'$ 分解。
2. 把 $H_{\mathcal{T}}\to H_{\mathcal{T}'}$ 拉回到挠层图，验证它是仿射空间纤维化。  
   *为什么*：仿射方向由扩张数据与相容提升控制。
3. 忽略仿射丛移位与 Tate 扭转，经基变换把剩余项写成沿 $\mathrm{pr}$ 的推前 $\mathrm{pr}_!((s,q)_!m^*\mathcal{L}_E|_{H_{\mathcal{T}'}})$。  
   *为什么*：仿射纤维化上的推前只差移位与扭转。
4. 代入因子化恒等式 $(s,q)_!m^*\mathcal{L}_E\simeq\mathcal{L}_E\boxtimes\mathcal{L}_E$，把挠商拆成两段，归约到满射情形。  
   *为什么*：该恒等式在 $\operatorname{Tor}$ 所用商叠归一化下成立，并且讲义明言在第 7 章证明。

> 缺口：关键是因子化恒等式 $(s,q)_!m^*\mathcal{L}_E\simeq\mathcal{L}_E\boxtimes\mathcal{L}_E$，讲义明言它在第 7 章才证明；讲义称「在假定该命题的情况下，洁净性的证明完成」。

*出处*：§6.6 非满射情形的归约（定理 6.2.1 证明的一部分，原文未单独编号）/ 原书 p.39–40


## 易错点

- 因子化恒等式是在「$\operatorname{Tor}$ 所用商叠归一化」下的陈述；换归一化会差平移与扭转。
- $\mathcal{T}'$ 是像而不是商，$\mathcal{T}'\subsetneq\mathcal{T}$；$M'$ 是 $\mathcal{T}'$ 在 $M\to\mathcal{T}$ 下的逆像。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§6.6 非满射情形的归约，p.39-40（PDF p.39-40），`源码/chapters/ch06.tex:115-137（§6.6 非满射情形的归约）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/six+operations — 页面给出 f_! ⊣ f^! 与 Beck–Chevalley 基变换，支持卡里『拉回到图后通过基变换把剩余项化为沿 pr 的推前』的一般机制；但 H_T→H_T' 的仿射空间纤维化、Tor^{ses} 图与因子化恒等式 (s,q)_!m^*L_E ≃ L_E⊠L_E 页面均无。

## 关联

- `glc/concept/cleanness-theorem`
- `glc/concept/fiber-calculation-surjective`
- `glc/concept/induction-step-base-change`
