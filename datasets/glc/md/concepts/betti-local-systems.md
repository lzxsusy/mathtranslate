---
id: glc/concept/betti-local-systems
type: concept
track: F
---

# Betti 局部系统与 de Rham 局部系统

> 谱参数在 de Rham 侧是带联络的挠子，在 Betti 侧是 $\operatorname{Map}(X^{\mathrm{top}},B\check G)$；后者只依赖 $X(\mathbb C)$ 的拓扑。

**问题**：同一个曲线 $X$ 的 de Rham 谱叠与 Betti 谱叠，为什么在代数意义上并不相同？

## 定义

在 de Rham 情形，谱参数是 de Rham 局部系统：
$$\operatorname{LocSys}^{\mathrm{dR}}_{\check G}(X)=\operatorname{Conn}_{\check G}(X):=\{(E_{\check G},\nabla)\mid E_{\check G}\text{ 为 }\check G\text{-挠子},\ \nabla\text{ 为联络}\}.$$
在 Betti 情形，谱参数是 Betti 局部系统：
$$\operatorname{LocSys}^{\mathrm{Betti}}_{\check G}(X):=\operatorname{Map}(X^{\mathrm{top}},B\check G).$$
选定基点 $x\in X(\mathbb C)$ 后，刚性化 Betti 模空间的经典截断为
$$\operatorname{LocSys}^{\mathrm{Betti},\mathrm{rig},\mathrm{cl}}_{\check G,x}(X)\simeq\operatorname{Hom}(\pi_1(X(\mathbb C),x),\check G),$$
未刚性化的经典叠通过取共轭作用的商得到。

*记号*：$\check G$ 为 $G$ 的 Langlands 对偶群；$X^{\mathrm{top}}$ 是 $X(\mathbb C)$ 的拓扑空间；$B\check G$ 是分类叠；上标 $\mathrm{rig}$ 表示刚性化（选定基点并平凡化纤维），$\mathrm{cl}$ 表示经典截断。

## 要点

- de Rham 叠依赖复代数曲线 $X$，而 Betti 叠只依赖 $X(\mathbb C)$ 的拓扑。
- 刚性化截断 $\operatorname{Hom}(\pi_1(X(\mathbb C),x),\check G)$ 只是经典层面的描述；未刚性化时还要对共轭作用取商。
- 这个描述只是第一近似：范畴 Langlands 中使用的 Betti 模空间是导出的，其切复形由 $X(\mathbb C)$ 上以伴随局部系统为系数的上链控制。

## 关键公式

- $$\operatorname{LocSys}^{\mathrm{dR}}_{\check G}(X)=\operatorname{Conn}_{\check G}(X):=\{(E_{\check G},\nabla)\mid E_{\check G}\text{ 为 }\check G\text{-挠子},\ \nabla\text{ 为联络}\}$$
- $$\operatorname{LocSys}^{\mathrm{Betti}}_{\check G}(X):=\operatorname{Map}(X^{\mathrm{top}},B\check G)$$
- $$\operatorname{LocSys}^{\mathrm{Betti},\mathrm{rig},\mathrm{cl}}_{\check G,x}(X)\simeq\operatorname{Hom}(\pi_1(X(\mathbb C),x),\check G)$$

## 易错点

- 不能把刚性化截断当成 Betti 叠本身：$\operatorname{Hom}(\pi_1,\check G)$ 只在选定基点后描述经典截断，未刚性化要取共轭商，而范畴 Langlands 用的还是导出叠。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§11.2 Betti 局部系统与 de Rham 局部系统，p.57（PDF p.57），`源码/chapters/ch11.tex:25-42（两类局部系统的定义，§11.2）`

## 核验

状态：`external-confirmed`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/local+system — 页面：local system 即 locally constant sheaf；连通空间上『local systems are equivalently representations of the fundamental group π_1(X,x_0)』（等价于 fundamental groupoid 的函子）；并指出平坦向量丛/联络与局部系统在 Riemann–Hilbert 下对应。对应卡里 LocSys^dR_Ĝ(X)=Conn_Ĝ(X)={(E_Ĝ,∇)}，以及刚性化后 LocSys^{Betti,rig,cl}_Ĝ,x(X)≃Hom(π_1(X(C),x),Ĝ)。
- arXiv：https://arxiv.org/abs/1606.08523 — L253：『Loc_{G^∨}(S)=[S,BG^∨] which we understand as a derived stack』——正是卡里 LocSys^Betti_Ĝ(X):=Map(X^top,BĜ)（BZN16 记 [S,BG^∨]，S 为 X 的底拓扑曲面）；同文 §2.2.3 给出 Loc_{GL_1}(E,0)≃Spec C[π_1(Jac(E,0))]≃C^××C^×，即刚性化后由 π_1 的表示算出的实例。

## 关联

- `glc/concept/derham-betti-elliptic-mismatch`
- `glc/concept/betti-spectral-stack`
