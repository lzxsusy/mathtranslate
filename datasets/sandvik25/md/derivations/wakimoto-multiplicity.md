# Wakimoto 滤链的重数如何变成 $\dim V_\lambda$

> `sandvik25/deriv/wakimoto-multiplicity` · 轨道 C · Iwahori–Whittaker 侧 · 状态 dev · 4 步

> **要回答的问题**：两个重数公式长得一样，凭什么说后者是前者的推论？

## 一句话

定理 2.5.3 说 $Z(\mathrm{Sat}(V))$ 的 Wakimoto 滤链里 $\mathbb W_\lambda$ 的重数是 $V$ 的 $\lambda$-权维数；定理 4.5.1 说平均之后 $\Delta^{\mathrm{IW}}_\lambda$ 与 $\nabla^{\mathrm{IW}}_\lambda$ 的重数也是 $\dim V_\lambda$——中间差一个 $\mathrm{Av}^{\mathrm{IW}}$ 保持重数的论证。

## 目标

把 §2.5 的 Wakimoto 重数公式沿 $\mathrm{Av}^{\mathrm{IW}}$ 搬运到 §4.5 的 IW 标准/余标准重数公式。

## 前提

- 定理 2.5.3：$[Z(\mathcal F):\mathbb W_\lambda]=\dim(\mathrm{Sat}^{-1}(\mathcal F))_\lambda$。
- 定理 4.4.1 证明中的 (6)：$\mathrm{Av}^{\mathrm{IW}}(\Delta_w)\cong\Delta^{\mathrm{IW}}_\lambda$、$\mathrm{Av}^{\mathrm{IW}}(\nabla_w)\cong\nabla^{\mathrm{IW}}_\lambda$，$\lambda$ 由 $W\cdot w=W\cdot w_\lambda$ 定。
- 定理 4.5.1 要证：$(Z^{\mathrm{IW}}(V):\Delta^{\mathrm{IW}}_\lambda)=(Z^{\mathrm{IW}}(V):\nabla^{\mathrm{IW}}_\lambda)=\dim V_\lambda$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 取 $Z(\mathrm{Sat}(V))$ 的一条 Wakimoto 滤链：每一层商是 $\mathbb W_{\lambda_i}$，出现次数由定理 2.5.3 给出 $=\dim V_{\lambda_i}$。 | 这是重数信息的出发点；滤链存在性由定理 2.5.3(1)。 | `A p.5` | A·原文明确写了 |
| 2 | 把 $\mathrm{Av}^{\mathrm{IW}}$ 作用到整条滤链上：它是反常 $t$-正合的加法函子，故把 $0\to\mathcal F_{i-1}\to\mathcal F_i\to\mathbb W_{\lambda_i}\to0$ 送到 IW 中的短正合列，商为 $\mathrm{Av}^{\mathrm{IW}}(\mathbb W_{\lambda_i})$。 | $t$-正合性是定理 4.4.1(1)，正是它保证「滤链的商」在平均后仍是商。 | `A p.10` | A·原文明确写了 |
| 3 | 由式 (6)，$\mathrm{Av}^{\mathrm{IW}}(\mathbb W_{\lambda_i})$ 在 $K_0$ 中等于 $\Delta^{\mathrm{IW}}_{\lambda_i}$（原文在 (7) 之后明说「$\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$ 与 $\Delta^{\mathrm{IW}}_\lambda$ 不同构，但在 $K_0$ 中相等」）。 | 重数是 $K_0$ 层面的量，所以「不同构但同类」足够；若要倾斜性则需更强，那由定理 4.5.1 另证。 | `A p.11–12` | A·原文明确写了 |
| 4 | 于是 $Z^{\mathrm{IW}}(V)$ 的滤链商在 $K_0$ 中给出重数 $\dim V_\lambda$；再用 $\nabla$ 侧同法（(6) 的第二式）得余标准重数相同，二者相等即得倾斜性所需的平衡。 | 标准重数 = 余标准重数是最高权范畴中倾斜的刻画。 | `A p.11` | A·原文明确写了 |

## 结论

IW 侧重数公式 = 把 §2.5 的 Wakimoto 重数沿 $t$-正合的 $\mathrm{Av}^{\mathrm{IW}}$ 推到 $K_0$，再用式 (6) 把 $\mathbb W_\lambda$ 换成 $\Delta^{\mathrm{IW}}_\lambda$。

## 缺口

- 「$\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$ 与 $\Delta^{\mathrm{IW}}_\lambda$ 在 $K_0$ 中相等」原文只用一句带过，未给证明。
- 定理 4.5.1 本身的证明（尤其拟极小情形）原文只给三步梗概，本推导用的是它的结论而非重证。

## 最容易讲错的地方

- 不能由 $K_0$ 中同类推出滤链商同构：滤链需要的是对象层面的短正合列，这正是为什么要先有 $t$-正合性。
- $\lambda_i$ 是 Wakimoto 侧下标，$\lambda$ 是 IW 侧下标，两者按同一个 $X^\vee$ 对齐——若在 $T$ 与 $T^\vee$ 之间取了对偶，重数会整体平移。

## 相关卡

[中心层的 Wakimoto 滤链（定理 2.5.3）](../concepts/wakimoto-filtration.md) · [中心层的 IW 像是倾斜层（定理 4.5.1）](../concepts/central-tilting.md) · [IW 平均函子 $\mathrm{Av}^{\mathrm{IW}}$（定理 4.4.1）](../concepts/iw-averaging.md)

## 出处（印刷页）

- A p.5–12（A p.11）

> 说明：重数公式在 p.5（定理 2.5.3），$K_0$ 的说明在 p.12，平均函子的 $t$-正合性在 p.10。
