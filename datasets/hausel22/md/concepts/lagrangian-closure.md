# 拉格朗日闭包 $\overline{\overline{W^+_\calE}}$

> `hausel22/concept/lagrangian-closure` · 轨道 E · 仿射 Grassmannian 与重数代数 · 状态 dev

> **先自测**：为什么普通的 Zariski 闭包不够，要另造一个「闭包」？

## 一句话

拉格朗日闭包是包含该上行流的最小闭上行流之并，即按 BB 分解取商后的闭包；定理 3.18 把它算成不大于 $\mu$ 的流的并。

## 定义

对 $\calE\in\M^{s\T}$，$W^+_\calE$ 的拉格朗日闭包 $\overline{\overline{W^+_\calE}}$ 定义为包含 $W^+_\calE$ 的最小闭的上行流之并；换言之，它就是按 BB 分解所取商空间中的闭包。定理 3.18：设 $\mu\in P^+$、$c\in C$，假定 $\calE_{\delta^\mu_c}\in\M^{s\T}$，则 $\overline{\overline{W^+_{\calE_{\delta^\mu_c}}}}=\coprod_{\mu\ge\lambda\in P^+}W^+_{\delta^\lambda_c}$。

**记号**：$\overline{\overline{W^+_\calE}}$；BB 分解；$\delta^\lambda_c$；支配序。

## 要点（为什么需要它）

1. 它的定义是「流之并」而不是「点集的闭包」：这正是与 Zariski 闭包的区别，也是双上划线的用意。
2. 在 BB 分解下，$X$ 是各流的局部闭并，商掉 $\T$-作用后每个流收缩成一个点，闭包就变成「向下所有流」的并。
3. 定理 3.18 的指标是支配序：并取遍 $\mu\ge\lambda$，也就是「不比 $\mu$ 大」的所有权。
4. 猜想 3.19 说：$\rho_\mu(\bE_c)$ 的镜像的支集恰是 $\overline{\overline{W^+_{\delta^\mu_c}}}$，重数自由时镜像是它的结构层。

## 核心公式

$$
$$\overline{\overline{W^+_\calE}}:=\text{包含 }W^+_\calE\text{ 的最小闭上行流之并}$$$$\overline{\overline{W^+_{\calE_{\delta^\mu_c}}}}=\coprod_{\mu\ge\lambda\in P^+}W^+_{\delta^\lambda_c}$$
$$

$$
$$\overline{\overline{W^+_{\calE_{\delta^\mu_c}}}}=\coprod_{\mu\ge\lambda\in P^+}W^+_{\delta^\lambda_c}$$
$$

## 定理与证明（或缺口）

### 拉格朗日闭包的显式形式（定理 3.18）

在 $\calE_{\delta^\mu_c}\in\M^{s\T}$ 的假设下，$\overline{\overline{W^+_{\calE_{\delta^\mu_c}}}}=\coprod_{\mu\ge\lambda\in P^+}W^+_{\delta^\lambda_c}$。

> 证明状态：**sketch**。原文说「利用 (3.8) 与 (3.4) 可以推出」，未给细节。

出处：`A p.2244`

## 常见误解

- 双上划线不是装饰：它区别于 Zariski 闭包，Zariski 闭包会多出与别的流相交的部分，不再是「拉格朗日」的并。
- 定理 3.18 的并是「闭的上行流之并」中最小者，不是任意并；写成 $\bigcup_{\lambda\le\mu}$ 时要说明取的是闭包。
- 不要把 $\overline{\overline{W^+}}$ 与 $\overline{W^+}$ 混用：前者按 BB 取商，后者是 Zariski 闭包，两者一般不同。
- 定理 3.18 要求 $\calE_{\delta^\mu_c}\in\M^{s\T}$；对非光滑点或非 $\T$-不动点，这个描述不成立。

## 相关卡

[非常稳定 Higgs 丛](../concepts/very-stable-higgs-bundle.md) · [仿射 Grassmannian $\Gr$](../concepts/affine-grassmannian.md) · [经典极限 $\mathscr{S}$ 与算子的交换](../derivations/s-intertwines-operators.md)

## 出处（印刷页）

- A p.2244（A p.2244）

> 说明：A=原文 §3.3.1 的定义（定义 3.17）与定理 3.18；B=把「BB 商掉后闭包 = 向下流的并」讲清楚；C=与 Zariski 闭包的对比是我们补的。最没把握处：原文对「按 BB 分解取商」的商空间未作严格定义，此处按「各流收缩成点」的直觉表述。
