# 本质 L^r、平方可积、缓增：定理 3.2、3.3 与推论 3.4

> `yao17/concept/square-integrable-tempered` · 轨道 分类与不变量 · 状态 dev

> **先自测**：«平方可积» 与 «缓增» 在段语言下各自长什么样？为什么定理 3.2 里要额外看 ρ((m−1)/2) 的中心特征标？

## 一句话

本质平方可积 ⇔ π=Q(Δ) 单段；缓增 ⇔ 每段都平方可积；两者之间还有本质 L^{2+ε} 的连续层级。

## 定义

令 $G^0=\{g\in\GL_n(K):|\det g|_K=1\}$。(1) 容许 $\pi$ 称本质 $L^r$，若对任意 $v,\lambda$，矩阵系数 $c_{v,\lambda}$ 在 $G^0$ 上 $L^r$（即 $\int_{G^0}|c_{v,\lambda}|^r dg$ 收敛）；(2) 若再加中心特征标 $\omega_\pi$ 酉，称 $L^r$；(3) 本质平方可积 = 本质 $L^2$，平方可积 = $L^2$；本质缓增 = 对一切 $\epsilon>0$ 本质 $L^{2+\epsilon}$，缓增再加 $\omega_\pi$ 酉。定理 3.2（Zelevinsky）：(1) 不可约容许 $\pi$ 本质平方可积 $\iff$ $\pi\cong Q(\Delta)$（单个段）；(2) 此 $Q(\Delta)$ 平方可积 $\iff$ $Q(\Delta)=\Delta(\sigma,m)$ 时 $\rho(\tfrac{m-1}{2})$ 的中心特征标酉。定理 3.3：$\pi=Q(\Delta_1,\dots,\Delta_r)$ 缓增 $\iff$ 每个 $Q(\Delta_i)$ 平方可积。

**记号**：层级：$\text{超尖点}\subset\text{平方可积}\subset\text{缓增}\subset\text{一般}\subset\text{容许}$；推论 3.4 与定理 3.6 把「缓增」与「一般且每段中心特征标酉」对上。

## 要点（为什么需要它）

1. 定理 3.2(1) 把「平方可积」变成纯组合条件：$\pi$ 只由一个段诱导（于是 $\Supp(\pi)$ 是单一超尖点的阶梯），而定理 3.2(2) 的 $\rho(\frac{m-1}{2})$ 是校正项，确保中心特征标酉——这正是「本质」与「非本质」的差别。
2. 定理 3.3 说缓增性是「逐段」的：$Q(\Delta_1,\dots,\Delta_r)$ 缓增 $\iff$ 每个 $Q(\Delta_i)$ 平方可积；配合定理 3.1(5)，推论 3.4 进一步得到任两段不 linked，故 $\pi\cong Q(\Delta_1)\times\dots\times Q(\Delta_r)$ 本身不可约。
3. 「本质」只是中心特征标不酉；Casselman 80' 的注说任一光滑表示可乘一个正实值拟特征标把中心特征标变酉，故本质 $L^r$ 与 $L^r$ 的差别在 $\GL_n$ 情形是可控的。
4. 底本 Remark 指出反向的困难：用 Zelevinsky 段去分类「本质缓增」似乎不容易（因为本质缓增的真条件是对所有 $\epsilon>0$ 的本质 $L^{2+\epsilon}$），可见这条层级在中间地带并不干净。

## 核心公式

$$
$\int_{G^0}|c_{v,\lambda}(g)|^r\,dg<\infty\quad(\text{本质 }L^r)$$\pi\ \text{本质平方可积}\iff \pi\cong Q(\Delta)\ (\text{单个段})$$\pi=Q(\Delta_1,\dots,\Delta_r)\ \text{缓增}\iff Q(\Delta_i)\ \text{平方可积}\ \forall i$$\text{缓增}\ \Longrightarrow\ \pi\cong Q(\Delta_1)\times\dots\times Q(\Delta_r)\ (\text{无 linked})$
$$

$$
$\pi\ \text{本质平方可积}\iff \pi\cong Q(\Delta)\ (\text{单个段})$
$$

$$
$\pi=Q(\Delta_1,\dots,\Delta_r)\ \text{缓增}\iff Q(\Delta_i)\ \text{平方可积}\ \forall i$
$$

$$
$\text{缓增}\ \Longrightarrow\ \pi\cong Q(\Delta_1)\times\dots\times Q(\Delta_r)\ (\text{无 linked})$
$$

## 定理与证明（或缺口）

### 定理 3.2（Zelevinsky）

不可约容许 $\pi$ 本质平方可积 $\iff$ $\pi\cong Q(\Delta)$ 为单个段；$Q(\Delta(\sigma,m))$ 平方可积 $\iff$ $\sigma(\frac{m-1}{2})$ 的中心特征标酉。

> 证明状态：**cited**。底本只陈述，未给证明；它依赖 Casselman 的矩阵系数判据与段诱导的显式计算。

出处：`A §3.2.1 p.27`

### 定理 3.3（Zelevinsky）

$Q(\Delta_1,\dots,\Delta_r)$ 缓增 $\iff$ 每个 $Q(\Delta_i)$ 平方可积。

> 证明状态：**cited**。底本只陈述；推论 3.4 的证明被给出，但其论证只用到「$\sigma$ 有酉中心特征标时 $\omega_\sigma(s)$ 对非零 $s$ 不酉」这一事实。

出处：`A §3.2.2 p.27`

## 常见误解

- 本质平方可积（essential）与平方可积差一个中心特征标的酉性；底本在定理 3.2(2) 用 $\rho(\frac{m-1}{2})$ 显式写出这个校正，漏掉会误判。
- 「缓增 + 一般」并不等价于「缓增」：定理 3.6 的另一半需要每段中心特征标酉，底本 Remark 已点明这个差别。

## 相关卡

[超尖点支撑与 Steinberg 表示 St_n](../concepts/supercuspidal-support.md) · [一般（generic）表示、Whittaker 模型与定理 3.6](../concepts/generic-whittaker.md) · [定理 2.14：超尖点、本质平方可积、一般表示在对应下的像](../concepts/llc-finer-properties.md)

## 出处（印刷页）

- A p.27（A p.27）

> 说明：本质 $L^r$/$L^r$/本质缓增的定义、定理 3.2/3.3 与推论 3.4 取自 p.27；「本质与平方可积只差中心特征标」是我们的解读。
