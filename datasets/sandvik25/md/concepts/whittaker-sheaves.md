# Whittaker 层与 $(H,\chi^*\mathcal L_{\mathrm{AS}})$-等变范畴

> `sandvik25/concept/whittaker-sheaves` · 轨道 C · Iwahori–Whittaker 侧 · 状态 dev

> **先自测**：Whittaker 层的「等式 $a^*\mathcal F\cong\chi^*\mathcal L_{\mathrm{AS}}\boxtimes\mathcal F$」为什么只是直观而非定义？

## 一句话

固定 $\chi\colon H\to\mathbb G_m$ 与 $\mathbb G_a$ 上的 Artin–Schreier 局部系统 $\mathcal L_{\mathrm{AS}}$，把 $\chi^*\mathcal L_{\mathrm{AS}}$ 当作 $H$ 的乘法局部系统，得等变导出范畴；其对象常被上同调消没死死约束。

## 定义

设 $X$ 是代数群 $H$ 作用的 $H$-簇，$a\colon H\times X\to X$ 为作用映射，固定同态 $\chi\colon H\to\mathbb G_m$。取 $\mathbb G_a$ 上的 Artin–Schreier 局部系统 $\mathcal L_{\mathrm{AS}}$，则 $\chi^*\mathcal L_{\mathrm{AS}}$ 是 $H$ 上的乘法局部系统。定义 $(H,\chi^*\mathcal L_{\mathrm{AS}})$-等变可构造层导出范畴 $\mathcal D^b_c(H\backslash^{\chi^*\mathcal L_{\mathrm{AS}}}X)$。

**记号**：$\mathcal L_{\mathrm{AS}}$ 由 $x\mapsto x^p-x$ 的伽罗瓦覆盖中取一个直和项、使 $\mathbb Z/p$ 以 $[n]\mapsto\zeta^n$ 作用得到（$\zeta$ 为本原 $p$ 次单位根）。

## 要点（为什么需要它）

1. 等变性在这里是「乘性局部系统」意义的：$a^*\mathcal F\cong\chi^*\mathcal L_{\mathrm{AS}}\boxtimes\mathcal F$，比通常的 $H$-等变多了个扭曲。
2. 原文脚注 13 明确说这个等式「直观但不精确」：精确定义要纳入乘性映射 $H^k\times X\to X$ 的高阶余herence 关系（引 [Gai2]）。
3. 关键的消没 $H^\bullet(\mathbb G_a,\mathcal L_{\mathrm{AS}})\cong H^\bullet_c(\mathbb G_a,\mathcal L_{\mathrm{AS}})=0$：这正是 Whittaker 层「被约束得很紧」的来源。
4. 例 4.1.1 是最小模型：$\mathbb G_a$ 作用 $\mathbb P^1$，点轨道太小无法承载 Whittaker 层，于是 $\mathcal D^b_c(\mathbb G_a\backslash^\chi\mathbb P^1)\cong\mathcal D^b_c(\mathbb G_a\backslash^\chi\mathbb A^1)\cong\mathcal D^b(\mathbb Q_\ell\text{-mod})$（由 $0$ 处取茎给出）。
5. 这一节只是「热身」：真正的 IW 范畴把一个具体的 $I_u^+\to\mathbb G_a$ 代进去。

## 核心公式

$$
$a^*\mathcal F\cong\chi^*\mathcal L_{\mathrm{AS}}\boxtimes\mathcal F$$H^\bullet(\mathbb G_a,\mathcal L_{\mathrm{AS}})\cong H^\bullet_c(\mathbb G_a,\mathcal L_{\mathrm{AS}})=0$
$$

$$
$H^\bullet(\mathbb G_a,\mathcal L_{\mathrm{AS}})\cong H^\bullet_c(\mathbb G_a,\mathcal L_{\mathrm{AS}})=0$
$$

## 定理与证明（或缺口）

### 例 4.1.1（$\mathbb P^1$ 上的最小模型）

$\mathbb G_a$ 以 $t\cdot[x:y]=[x+yt:y]$ 作用 $\mathbb P^1$，则 $\mathcal D^b_c(\mathbb G_a\backslash^\chi\mathbb P^1)\cong\mathcal D^b_c(\mathbb G_a\backslash^\chi\mathbb A^1)\cong\mathcal D^b(\mathbb Q_\ell\text{-mod})$。

> 证明状态：**sketch**。两步都未给细节。

出处：`A p.9`

## 常见误解

- 把 $\chi^*\mathcal L_{\mathrm{AS}}$ 当成常局部系统：它是秩一但**非平凡**的，正是 Whittaker 扭曲的全部来源。
- 忽略「必须换到 étale 设置」（注 4.0.1）：Betti 情形下的 Whittaker 层需要 Krillov 模型，超出本文范围。

## 相关卡

[Iwahori–Whittaker 范畴 $\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$](../concepts/iw-category.md) · [IW 反常层的最高权结构（命题 4.3.1）](../concepts/iw-highest-weight.md)

## 出处（印刷页）

- A p.9（A p.9）

> 说明：§4.1 全在 p.9；$\mathcal L_{\mathrm{AS}}$ 的具体构造见脚注 12。
