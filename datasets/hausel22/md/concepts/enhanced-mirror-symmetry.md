# 增强镜像对称

> `hausel22/concept/enhanced-mirror-symmetry` · 轨道 C · 增强镜像对称与膜 · 状态 dev

> **先自测**：为什么普通的同调镜像对称不够用？

## 一句话

增强镜像对称 = 同调镜像对称 + 超 Kähler 膜的匹配 + Wilson 算子与 Hecke 算子的交换，三项都来自四维 $S$ 对偶。

## 定义

原文的定义是：同调镜像对称 $\mathscr{S}:D^b(\M_\DR)\simeq Fuk(\M^\vee_\DR)$，再加上两项额外结构——镜像对称下超 Kähler 膜的匹配，以及 Wilson 算子与 Hecke 算子的交换——合起来称为增强镜像对称。它们超出 Kontsevich 的通常同调镜像对称，来源是 $S$ 对偶的超对称来源与四维来源。

**记号**：$\mathscr{S}$；超 Kähler 膜；Wilson 算子 $\mathscr{W}^\mu$；Hecke 算子 $\mathscr{H}^\mu$。

## 要点（为什么需要它）

1. 三项缺一不可：只有 HMS 说不出膜怎么匹配，只有膜匹配说不出线算子怎么作用。
2. 「增强」的来源是四维：普通 HMS 只来自两个二维 $\sigma$ 模型之间的等价，没有超 Kähler 与线算子这两层。
3. 增强镜像对称是本文的纲领性对象：§3 全部内容（非常稳定、重数代数、Lagrange 闭包、几何 Satake）都是它在一个具体点上的检验。
4. 它可以被看成几何 Langlands 对应的「镜像版本」：Hecke 特征层在 $\G^\vee$ 侧，Wilson 算子在 $\G$ 侧，$\mathscr{S}$ 交换两者。

## 核心公式

$$
$$\mathscr{S}:D^b(\M_\DR)\simeq Fuk(\M^\vee_\DR)\quad+\quad\text{brane matching}\quad+\quad\mathscr{W}^\mu\circ\mathscr{S}=\mathscr{S}\circ\mathscr{H}^\mu$$
$$

## 定理与证明（或缺口）

### 增强镜像对称的三项结构

增强镜像对称由 (i) HMS 等价 $\mathscr{S}$；(ii) 超 Kähler 膜在 $\mathscr{S}$ 下的匹配（$(B,A,A)\leftrightarrow(B,B,B)$ 等）；(iii) 线算子的交换 $\mathscr{W}^\mu\circ\mathscr{S}=\mathscr{S}\circ\mathscr{H}^\mu$ 三部分组成。

> 证明状态：**sketch**。原文的三项是归纳式的定义，不是定理；每一项的严格陈述都还需要各自的证明。

出处：`A p.2235`

## 常见误解

- 把「增强镜像对称」当成「更强的 HMS」：它是加了结构的 HMS，不是把 HMS 的结论加强。
- 以为三项中任意两项就够：膜匹配与线算子交换分别对应不同的物理来源，缺一项就不是原文的定义。
- 把 Wilson 算子放在 $\G^\vee$ 侧：Wilson 算子作用在 $\M_\DR$（$\G$ 侧），Hecke 作用在 $\G^\vee$ 侧，见式 (3.12) 的方向。
- 把增强镜像对称与几何 Langlands 对应等同：前者是后者在 Hitchin 模空间上的「镜像化」表述，两者是同一现象的两面，不是同一条命题。

## 相关卡

[Kapustin–Witten 的 $S$ 对偶纲领](../concepts/kapustin-witten-duality.md) · [同调镜像对称](../concepts/homology-mirror-symmetry.md) · [几何 Langlands 的经典极限 $\mathscr{S}$](../concepts/classical-limit-langlands.md) · [经典极限 $\mathscr{S}$ 与算子的交换](../derivations/s-intertwines-operators.md)

## 出处（印刷页）

- A p.2235（A p.2235）
- A p.2235（A p.2235）

> 说明：A=原文 §2.5 末段的三项定义与 §3 首段的纲领性说明；B=把三项各自对应的物理来源拆开；C=「§3 是它在一个具体点上的检验」是我们对 §3 首段的归纳。最没把握处：原文对「膜匹配」只给了 $(B,A,A)\leftrightarrow(B,B,B)$ 一个例子，没有完整清单。
