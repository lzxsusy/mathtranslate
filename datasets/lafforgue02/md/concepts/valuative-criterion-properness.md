# 紧合性的赋值判据

> `lafforgue02/concept/valuative-criterion-properness` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：赋值判据把「紧合」这个几何条件换成了哪一道具体的代数题？

## 一句话

要证 $\ol{\Cht}^{\,r,d,\overline p\le p}$ 在 $X\times X$ 上紧合，只需对每个离散赋值环 $A$ 验证：任意 $K_A$-点都能延拓为 $A$-点；这一步把问题化成构造一个迭代 $\varphi$-格。

## 定义

设 $A$ 为离散赋值环，$K_A=\mathrm{Frac}(A)$，$\kappa_A$ 为剩余域，$\pi_A$ 为一致化子。$\ol{\Cht}^{\,r,d,\overline p\le p}\to X\times X$ 满足紧合性的赋值判据，指：对任意 $A$ 与任意使下图交换的 $K_A$-点，都存在 $A$-点延拓之。验证时的几何载体是正则曲面 $X\otimes A$，其特殊纤维是 $X\otimes\kappa_A$、一般纤维是 $X\otimes K_A$。

**记号**：$A_X$ 为 $X\otimes A$ 在某个点处的局部环；$\kappa_{A_X}$、$K_{A_X}$ 为其剩余域与分式域。

## 要点（为什么需要它）

1. 判据的内容是「延拓」：给定 $K_A$-点（一般纤维上的 chtouca），要造出 $A$-点（整族），等价于把一般纤维上的迭代 $\varphi$-格的特殊化算出来。
2. 这一步把几何问题彻底代数化：剩下的只是「在 $V$ 中找格 $M$ 使 $\varphi(M)\subset M$ 且 $[M:\varphi(M)]$ 受控」。
3. 第 V 章验证判据，第 VI 章给出构造；两章的衔接点是「满足截断多边形条件的格恰有一个」。
4. 判据只对够凸的 $p$ 成立，故「足够凸」这一条件在此处真正被用到。

## 核心公式

$$
$X\otimes A$，特殊纤维 $X\otimes\kappa_A$，一般纤维 $X\otimes K_A$$\varphi(M)\subset M$，$[M:\varphi(M)]=\deg$ 受 $p$ 控制$\ol{\Cht}^{\,r,d,\overline p\le p}\to X\times X$ 紧合 $\iff$ 赋值判据成立
$$

$$
$\varphi(M)\subset M$，$[M:\varphi(M)]=\deg$ 受 $p$ 控制
$$

$$
$\ol{\Cht}^{\,r,d,\overline p\le p}\to X\times X$ 紧合 $\iff$ 赋值判据成立
$$

## 定理与证明（或缺口）

### 赋值判据的验证

对每个离散赋值环 $A$、每个 $K_A$-点，存在 $A$-点延拓；故 $\ol{\Cht}^{\,r,d,\overline p\le p}\to X\times X$ 紧合。

> 证明状态：**sketch**。讲义只给归约与结论，构造的存在性归给第 VI 章，而第 VI 章本身也只给关键引理与序列构造，完整细节在 [Lafforgue 1998]。

出处：`A p.34`

## 常见误解

- 赋值判据要求对**所有**离散赋值环验证，不是只对 $X$ 的局部环；漏掉「任意 $A$」是把判据降格成特例。
- 紧合性在此指在 $X\times X$ 上紧合；叠本身不分离的 fourre-tout 不满足判据，只有切出的开子叠才验证。

## 相关卡

[fourre-tout（不分离的「杂物袋」叠）](../concepts/fourre-tout.md) · [迭代 $\varphi$-格](../concepts/iterated-phi-lattice.md) · [用赋值判据把紧合性化归为构造一个 $\varphi$-格](../derivations/properness-by-valuative-criterion.md)

## 出处（印刷页）

- A p.34–35（A p.34）

> 说明：判据的陈述与归约取第 V 章 p.34–35；曲面 $X\otimes A$ 的图解在 p.35。最后一步「唯一性」取 p.45。
