# 从混合 Hodge 数到 $\alpha$-扭弦性 Hodge 数

> `hausel22/deriv/stringy-hodge-shift` · 轨道 B · 拓扑镜像对称与 Hodge 数 · 状态 dev · 5 步

> **要回答的问题**：$\alpha$-扭弦性 Hodge 数里的求和、移位与不变取分别从哪来？

## 一句话

把轨形按 $\Gamma$-不动点分层、每层取 $L_\alpha$-扭上同调并作费米子移位，就得到与 $\SL_n$ 侧混合 Hodge 数可比的对象。

## 目标

说明 $h_{st,\alpha}^{p,q}(\M^\vee)$ 的每一项对应轨形分层中的哪些数据，从而解释为什么它与 $h^{p,q}(\M)$ 可比。

## 前提

- $\Gamma=\Jac_C[n]$ 作用在 $\SL_n$ 侧的 $\M$ 上，$\M^\vee=\M/\Gamma$ 是轨形。
- gerbe $\alpha\in H^2(\M^\vee,\U(1))\cong H^2(\M,\U(1))^\Gamma$ 由 $\M$ 上的万有丛构造。
- $\M^\gamma$ 记 $\gamma$ 的不动点集，$F(\gamma)$ 是费米子移位。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | $\SL_n$ 侧：$h^{p,q}(\M)=h^{p,q}(H^{p+q}_c(\M))$，即取紧支上同调的混合 Hodge 分次。 | $\M$ 非紧，必须用紧支上同调才能得到有限维的混合 Hodge 结构；这是原文定义。 | `A p.2233` | A·原文明确写了 |
| 2 | $\PGL_n$ 侧：轨形按 $\Gamma$ 的每个元素 $\gamma$ 分成不动点层 $\M^\gamma$，每层取 $L_\alpha$-扭上同调 $H^{\bullet}(\M^\gamma;L_\alpha)$。 | 轨形的「上同调」是各层不动点上同调的组装；$L_\alpha$ 是 gerbe 给出的扭层，扭在哪里由 $\alpha$ 决定。 | `A p.2233` | A·原文明确写了 |
| 3 | 再取 $\Gamma$-不变部分 $(-)^\Gamma$：只有 $\Gamma$-不变的部分才是轨形本身的贡献。 | $\Gamma$ 作用在扭上同调上，不取不变部分会把同一条 $\Gamma$-轨道重复计数。 | `A p.2233` | B·原文暗示、我们补的中间步 |
| 4 | 最后作费米子移位：总次数平移 $2F(\gamma)$，Hodge 双次数各平移 $F(\gamma)$，得到 $h^{p-F(\gamma),q-F(\gamma)}(H^{p+q-2F(\gamma)}(\M^\gamma;L_\alpha)^\Gamma)$。 | $F(\gamma)$ 由 $\gamma$ 在某个 $\gamma$-不动点处切空间上的作用定义；它把「切空间上旋转的权」换算成上同调次数的平移。 | `A p.2233` | A·原文明确写了 |
| 5 | 对 $\gamma\in\Gamma$ 求和，即得 $h_{st,\alpha}^{p,q}(\M^\vee)$ 的完整定义。 | 求和遍历轨形的所有层，这正是轨形 Hodge 数的定义方式。 | `A p.2233` | A·原文明确写了 |

## 结论

$h_{st,\alpha}^{p,q}(\M^\vee)=\sum_{\gamma\in\Gamma}h^{p-F(\gamma);q-F(\gamma)}\big(H^{p+q-2F(\gamma)}(\M^\gamma;L_\alpha)^\Gamma\big)$，与 $\SL_n$ 侧的 $h^{p,q}(\M)$ 可比，猜想 2.1 断言两者相等。

## 缺口

- $F(\gamma)$ 的具体公式（特征值相位和）原文只说「由作用定义」，未写；本卡第 4 步的展开是标准写法，但严格性依赖不动点选取的无关性，原文未证。
- $L_\alpha$ 的构造只说「可以用万有丛构造」，没有给出层的定义。
- 「$\Gamma$-不变部分」与 $\alpha$-扭转的相容性（扭层上的 $\Gamma$-作用）原文未讨论。

## 最容易讲错的地方

- 把 $F(\gamma)$ 当成 $\gamma$ 的阶：它是切空间特征值的相位和，与阶无关。
- 漏掉 $\Gamma$-不变上取：轨形的 Hodge 数取不变部分，不取会重复计数。
- 把 $\alpha$ 取平凡：$\PGL_n$ 侧的 gerbe 非平凡是本质的。
- $\M$ 非紧，必须用紧支上同调；用普通上同调会得到不同的（一般不是有限维的）对象。

## 相关卡

[弦性 Hodge 数（$\alpha$-扭）](../concepts/stringy-hodge-numbers.md) · [拓扑镜像对称](../concepts/topological-mirror-symmetry.md)

## 出处（印刷页）

- A p.2233（A p.2233）

> 说明：A=原文 §2.4 的定义与费米子移位的定性说明；B=第 3、4 步的展开（不变取、移位公式）是我们按标准轨形 Hodge 理论补的；C=「为什么可比」的说明是我们的归纳。最没把握处：$F(\gamma)$ 的具体公式与 $L_\alpha$ 的构造，原文都只一笔带过。
