# 一般（generic）表示、Whittaker 模型与定理 3.6

> `yao17/concept/generic-whittaker` · 轨道 分类与不变量 · 状态 dev

> **先自测**：θ_ψ 是怎么从加性特征标 ψ 造出来的？为什么「段两两不 linked」正好刻画 generic？

## 一句话

generic 指 π|U_n 上有非零的 θ_ψ-同态；Zelevinsky 定理说它等价于段两两不 linked，故缓增必 generic。

## 定义

取 $K$ 的非平凡加性拟特征标 $\psi$，$n(\psi)$ 为使 $\psi(\varpi^{-n}\mathcal O_K)=1$ 的最大整数。$U_n\subset\GL_n(K)$ 是严格上三角群，定义一维表示 $\theta_\psi(u_{ij})=\psi(u_{12}+\dots+u_{n-1,n})$。不可约容许 $\pi$ 称一般（generic），若 $\Hom_{U_n}(\pi|_{U_n},\theta_\psi)\neq0$。取非零 $\lambda\in\Hom_{U_n}(\pi|_{U_n},\theta_\psi)$，Whittaker 模型 $W_\psi=\{f\colon G\to\mathbb C: f(ug)=\theta_\psi(u)f(g)\}$，$G$ 右平移作用，$v\mapsto(g\mapsto\lambda(\pi(g)v))$ 是单 $G$-同态，像记 $W_{\pi,\psi}$。

**记号**：$\theta_\psi$ 是 $U_n$ 的特征标，沿「主对角线之上第一条」求和；引理 3.5：(1) generic 性与 $\psi$ 选取无关；(2) $\pi$ generic $\iff$ $\pi^\vee$ generic；(3) 任意拟特征标扭转保持 generic。

## 要点（为什么需要它）

1. 定理 3.6（Zelevinsky）：$Q(\Delta_1,\dots,\Delta_r)$ generic $\iff$ 任两段不 linked $\iff$ $\pi=Q(\Delta_1)\times\dots\times Q(\Delta_r)$——最后一步用定理 3.1(5)。于是推论 3.4 可重述为「每个不可约（本质）缓增表示都是 generic」。
2. Whittaker 模型的构造是「把 $\lambda$ 卷进右平移」：$v\mapsto(g\mapsto\lambda(\pi(g)v))$ 自动满足 $f(ug)=\theta_\psi(u)f(g)$，且由 $\pi$ 不可约与 $\lambda\neq0$ 保证单射。底本特意点明像与 $\pi$ 同构。
3. generic 在整体应用里是主力：Shalika 注说数域上不可约容许尖点自守表示 $\pi=\otimes'_v\pi_v$ 的每个局部分量都 generic——这正是局部理论要单独发展 generic 的原因。
4. 底本脚注 11 说 $\epsilon$ 因子的定义要靠 Whittaker 模型（「Much more to be added in second draft」），故 §3.6 的 $\epsilon$ 在底本里其实留了缺口：只有 JPPS 公式而无 Whittaker 侧的定义。

## 核心公式

$$
$\theta_\psi(u_{ij})=\psi(u_{12}+\dots+u_{n-1,n})$$\pi\ \text{generic}\iff \Hom_{U_n}(\pi|_{U_n},\theta_\psi)\neq0$$v\mapsto\big(g\mapsto\lambda(\pi(g)v)\big)\colon V\hookrightarrow W_\psi$$Q(\Delta_1,\dots,\Delta_r)\ \text{generic}\iff \Delta_i,\Delta_j\ \text{不 linked}\ (i\neq j)$
$$

$$
$\pi\ \text{generic}\iff \Hom_{U_n}(\pi|_{U_n},\theta_\psi)\neq0$
$$

$$
$v\mapsto\big(g\mapsto\lambda(\pi(g)v)\big)\colon V\hookrightarrow W_\psi$
$$

$$
$Q(\Delta_1,\dots,\Delta_r)\ \text{generic}\iff \Delta_i,\Delta_j\ \text{不 linked}\ (i\neq j)$
$$

## 定理与证明（或缺口）

### 定理 3.6（Zelevinsky）

$\pi=Q(\Delta_1,\dots,\Delta_r)$ generic $\iff$ 任两段不 linked $\iff$ $\pi=Q(\Delta_1)\times\dots\times Q(\Delta_r)$。

> 证明状态：**cited**。底本只陈述，并引定理 3.1(5) 完成第二个「当且仅当」；Whittaker 侧的计算未写。

出处：`A §3.2.3 p.28`

### 引理 3.5

(1) generic 性与 $\psi$ 的选取无关；(2) $\pi$ generic $\iff$ $\pi^\vee$ generic；(3) 拟特征标扭转保持 generic。

> 证明状态：**cited**。底本只列三条，未给证明。

出处：`A §3.2.3 p.28`

## 常见误解

- generic 是「$\pi|_{U_n}$ 上有 $\theta_\psi$-同态」，不是「$\pi$ 有一维 $U_n$-固定向量」；$\theta_\psi$ 非平凡，两者完全不同。
- 定理 3.6 的等价要求段两两不 linked，而不是「段两两不同」：$\Delta$ 与 $\Delta'$ linked 时 $Q(\Delta)\times Q(\Delta')$ 可约，$\pi$ 只能取 $Q(\Delta,\Delta')$。

## 相关卡

[本质 L^r、平方可积、缓增：定理 3.2、3.3 与推论 3.4](../concepts/square-integrable-tempered.md) · [定理 3.1：Bernstein–Zelevinsky 对 GL_n 容许表示的七条分类](../concepts/bz-classification.md) · [定理 2.14：超尖点、本质平方可积、一般表示在对应下的像](../concepts/llc-finer-properties.md) · [惯性对应：Bernstein 中心 ↔ Weil–Deligne 惯性类型（引理 4.3–4.5）](../concepts/inertial-correspondence.md)

## 出处（印刷页）

- A p.28（A p.28）

> 说明：θ_ψ、generic 与 Whittaker 模型的定义、引理 3.5、定理 3.6 与 Shalika 注取自 p.28；「脚注 11 说 §3.6 留了缺口」是据同页脚注的观察。
