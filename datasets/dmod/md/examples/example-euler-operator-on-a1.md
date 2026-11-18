---
id: dmod/example/example-euler-operator-on-a1
type: example
track: H
---

# $\mathbb A^1$ 上 Euler 算子 $z\partial-\alpha$ 的 $\mathcal D$-模

> $M_\alpha$ 的谱为 $\alpha+\mathbb Z$，特征簇是两条坐标轴；$\alpha\notin\mathbb Z$ 时不可约，$\alpha\in\mathbb Z$ 时可约。

**问题**：$M_\alpha=\mathcal D(1)/\mathcal D(1)(z\partial-\alpha)$ 何时不可约？它的谱、特征簇与合成因子分别是什么？

## 设定

取 $X=\mathbb A^1$，$\mathcal D=\mathcal D(1)=k[z,\partial]$，$E=z\partial$，$M_\alpha=\mathcal D/\mathcal D(E-\alpha)$（$\alpha\in k$）。算子族 $\{z^pE^q,\ \partial^pE^q;p,q\in\mathbb Z_+\}$ 是 $\mathcal D$ 的 $k$-基，理想 $\mathcal D(E-\alpha)$ 由 $(z^pE^q(E-\alpha),\ \partial^pE^q(E-\alpha))$ 张成，故 $M_\alpha$ 由 $z^p$、$\partial^p$（$p\in\mathbb Z_+$）的陪集张成。记 $\mathcal O_1=\mathcal D/\mathcal D(\partial)$、$\Delta_1=\mathcal D/\mathcal D(z)$。

## 计算

1. 算交换关系：$[E,z]=z\partial z-z^2\partial=z$，$[E,\partial]=z\partial^2-\partial z\partial=-\partial$，故 $Ez=z(E+1)$、$E\partial=\partial(E-1)$。  
   *为什么*：由 $E=z\partial$ 与 $[\partial,z]=1$ 直接计算；这两式决定 $E$ 在生成元上的作用。
2. 求谱：$z^n$ 的陪集是 $E$ 的属于特征值 $\alpha+n$ 的特征向量，$\partial^n$ 的陪集属于 $\alpha-n$，故 $\operatorname{Spec}(E)=\{\alpha+n;n\in\mathbb Z\}$，每个特征值重数 $1$。  
   *为什么*：把 $E$ 移到 $z^n$ 右侧得 $Ez^n=z^n(E+n)$，在 $M_\alpha$ 上 $E=\alpha$；同理 $E\partial^n=\partial^n(E-n)$。
3. $\alpha\notin\mathbb Z$：$z$ 把特征值 $\alpha+n$ 的特征空间同构地送到 $\alpha+n+1$，归纳构造 $z^{\alpha+n}$ 使 $Ez^{\alpha+n}=(\alpha+n)z^{\alpha+n}$、$zz^{\alpha+n}=z^{\alpha+n+1}$、$\partial z^{\alpha+n}=(\alpha+n)z^{\alpha+n-1}$；它们构成基，故 $M_\alpha$ 不可约，且 $M_\alpha\cong M_{\alpha+p}$（$p\in\mathbb Z$）。  
   *为什么*：特征值互不相同使 $z$ 既是满射又是单射；任一非零子模含特征向量从而含某个 $z^{\alpha+p}$，再由 $z$ 的作用含全部基向量。
4. $\alpha\in\mathbb Z$：设 $n=-\alpha>0$，可选取 $v_m$ 使 $zv_m=v_{m+1}$、$\partial v_m=mv_{m-1}$；$v_m$（$m\ge0$）张成子模 $N_{-n}\cong\mathcal O_1$，商 $M_{-n}/N_{-n}\cong\Delta_1$，正合列 $0\to\mathcal O_1\to M_{-n}\to\Delta_1\to0$ 不分裂；对 $n\ge0$ 有 $M_n\cong M_0$ 与不分裂的 $0\to\Delta_1\to M_n\to\mathcal O_1\to0$。  
   *为什么*：$zv_{-1}\in N_{-n}$ 使商中 $z\delta=0$，且 $\delta^{(m)}=\partial^m\delta$ 与 $v_{-(m+1)}$ 成比例、$z\delta^{(m)}=-m\delta^{(m-1)}$，正是 $\Delta_1$ 的结构。
5. 算特征簇：$\operatorname{Ch}(M_\alpha)=\operatorname{Ch}(\mathcal O_1)\cup\operatorname{Ch}(\Delta_1)=\{z=0\}\cup\{\xi=0\}$，维数 $1$，故 $M_\alpha$ 完整。  
   *为什么*：用短正合列与定理 5.1.1 证明中的特征簇并集公式；$\operatorname{Ch}(\mathcal O_1)=k\times\{0\}$、$\operatorname{Ch}(\Delta_1)=\{0\}\times k$。

## 结果

$M_\alpha$ 对一切 $\alpha\in k$ 都是完整 $\mathcal D(1)$-模，特征簇为 $k^2$ 中 $\{z=0\}\cup\{\xi=0\}$。$\alpha\notin\mathbb Z$ 时 $M_\alpha$ 不可约，基为 $z^{\alpha+n}$（$n\in\mathbb Z$），且 $M_\alpha\cong M_{\alpha+p}$（$p\in\mathbb Z$）。$\alpha\in\mathbb Z$ 时 $M_\alpha$ 可约：$M_{-n}$（$n>0$）有 $0\to\mathcal O_1\to M_{-n}\to\Delta_1\to0$，$M_n$（$n\ge0$）同构于 $M_0$ 并有 $0\to\Delta_1\to M_n\to\mathcal O_1\to0$，两者都不分裂。$\alpha\notin\mathbb Z$ 时模不可约而特征簇可约，$M_0$ 可约而特征簇相同：特征簇不能决定模。

## 核对

逐条代回核对：(1) 在 $\alpha\notin\mathbb Z$ 的基上，$Ez^{\alpha+n}=(\alpha+n)z^{\alpha+n}$、$zz^{\alpha+n}=z^{\alpha+n+1}$、$\partial z^{\alpha+n}=(\alpha+n)z^{\alpha+n-1}$ 满足 $[E,z]=z$ 与 $[\partial,z]=1$，故 $\mathcal D\to M_\alpha$ 的核恰为 $\mathcal D(E-\alpha)$。(2) 滤过 $F_pM_\alpha=\langle z^{\alpha+n};|n|\le p\rangle$ 的维数为 $2p+1$，由 I §8 的判别（8.4）知 $M_\alpha$ 完整，与 $\operatorname{Ch}(M_\alpha)$ 的维数 $1$ 一致。(3) $M_\alpha\cong M_{\alpha+p}$ 与 $\alpha'-\alpha\notin\mathbb Z$ 时不同构，由谱 $\{\alpha+n\}$ 与 $\{\alpha'+n\}$ 是否相同区分。

**相关概念卡**：dmod/concept/d-module-on-affine-line、dmod/concept/irreducible-holonomic-classification

## 易错点

- $\alpha$ 与 $\alpha+p$（$p\in\mathbb Z$）给出同构的模；$\alpha'-\alpha\notin\mathbb Z$ 时谱不同，模不同构，不要把同构范围放大到所有 $\alpha$。
- $\alpha\notin\mathbb Z$ 时 $M_\alpha$ 不可约，但其特征簇是两条直线之并（可约的簇）：特征簇可约不蕴含模可约。
- 所有 $M_\alpha$ 的特征簇相同，但 $\alpha\notin\mathbb Z$ 时模不可约、$M_0$ 可约：特征簇相同不蕴含模同构，不能用 $\operatorname{Ch}$ 代替模本身。
- $E$ 在 $M_\alpha$ 上取特征值 $\alpha+n$，只在 $M_\alpha$ 中 $E$ 才可当作纯量 $\alpha$ 处理；在 $\mathcal D$ 上 $E$ 不是纯量。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），I §8 完整模，例，p.34-35（PDF p.40-41），`源码/chapters/chap1.tex:1221-1270（$M_\alpha$ 的完整计算）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》中译本（校订批注本），V §1 完整 D-模，p.133（PDF p.139），`源码/chapters/chap5.tex:14-31（定理 5.1.1：特征簇的并）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/d-module-on-affine-line`
- `dmod/concept/irreducible-holonomic-classification`
- `dmod/example/example-d-module-on-projective-space`
