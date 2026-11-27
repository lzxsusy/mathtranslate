# Bernstein 分量、惯性等价与定理 4.2 的直积分解

> `yao17/concept/bernstein-decomposition` · 轨道 惯性 Langlands 与类型 · 状态 dev

> **先自测**：Bernstein 分量按什么划分？为什么它的定义既要用超尖点 ς 又要允许非分歧扭转 η？

## 一句话

Rep^∞_n 直积分解为各 Bernstein 分量 R(L,ς)；分量相等 ⇔ 惯性等价，Bernstein 中心就是 (L,ς) 的惯性等价类。

## 定义

设 $L\subset\GL_n(K)$ 是 Levi，$P$ 是以为 $L$ 为 Levi 因子的抛物，$\varsigma$ 是 $L$ 的不可约超尖点表示。Bernstein 分量 $R(L,\varsigma)=R(L,\varsigma)(\GL_n(K))\subset\Rep^\infty_n$ 是由所有「其每个不可约子商都是某个 $I_L^{\GL_n}(\varsigma\otimes\eta)$ 的子商」的 $\pi$ 构成的全子范畴，$\eta$ 跑遍 $L$ 的非分歧特征标，$I_L^{\GL_n}:=\Ind_P^{\GL_n(K)}\circ j^\ast$ 是正规化抛物诱导。引理 4.1：$R(L_1,\varsigma_1)=R(L_2,\varsigma_2)$ $\iff$ 二者惯性等价：存在 $L_2$ 的非分歧特征标 $\eta$ 与 $g\in\GL_n(K)$ 使 $gL_1g^{-1}=L_2$、$g\varsigma_1=\varsigma_2\eta$。定义 Bernstein 中心 $\mathcal B=\mathcal B(\GL_n(K)):=\{(L,\varsigma)\}/\text{惯性等价}$。定理 4.2：$\Rep^\infty_n=\prod_{(L,\varsigma)\in\mathcal B}R(L,\varsigma)$。

**记号**：$j\colon P\to L$ 是到 Levi 商的映射；$\varsigma\otimes\eta$ 通过 $j^\ast$ 拉回成 $P$ 的表示；底本注：判断 $\pi$ 落在哪个分量，只需看它的超尖点支撑。

## 要点（为什么需要它）

1. 分量的定义用「$\varsigma\otimes\eta$（$\eta$ 非分歧）诱导出的所有子商」，而不是「$\varsigma$ 本身」：这一步把「同一个超尖点表示沿 $|\det|$ 的整数次幂」全部并进一个分量，否则 $\varsigma$ 与 $\varsigma(1)$ 会落在不同分量里。
2. 引理 4.1 的两个条件缺一不可：只要求 $gL_1g^{-1}=L_2$ 会漏掉 $\varsigma$ 的非分歧扭转，只要求 $\varsigma$ 相等会漏掉共轭。惯性等价正是这两个作用的商。
3. 定理 4.2 是「直积」而非「直和」：每个分量 $R(L,\varsigma)$ 里可以有任意长的诱导表示，但不同分量之间没有非零同态——这是 Bernstein 分解最有力的地方。
4. $\GL_2$ 的三类分量（底本例）恰好对上超尖点支撑的三种形状：$\{\pi\}$（超尖点自己）、$\{\chi,\chi\}$（$\St_2(\chi)$ 型）、$\{\chi_1,\chi_2\}$（$\chi_1\chi_2^{-1}$ 分歧的主序列）。

## 核心公式

$$
$R(L,\varsigma)=\big\{\pi:\ \text{每个不可约子商都是 }I_L^{\GL_n}(\varsigma\otimes\eta)\ \text{的子商},\ \eta\ \text{非分歧}\big\}$$R(L_1,\varsigma_1)=R(L_2,\varsigma_2)\iff \exists\eta,\ g:\ gL_1g^{-1}=L_2,\ g\varsigma_1=\varsigma_2\eta$$\Rep^\infty_n=\prod_{(L,\varsigma)\in\mathcal B}R(L,\varsigma)$
$$

$$
$R(L_1,\varsigma_1)=R(L_2,\varsigma_2)\iff \exists\eta,\ g:\ gL_1g^{-1}=L_2,\ g\varsigma_1=\varsigma_2\eta$
$$

$$
$\Rep^\infty_n=\prod_{(L,\varsigma)\in\mathcal B}R(L,\varsigma)$
$$

## 定理与证明（或缺口）

### 定理 4.2（Bernstein 分解）

光滑表示范畴按 Bernstein 中心直积分解：$\Rep^\infty_n=\prod_{(L,\varsigma)\in\mathcal B}R(L,\varsigma)$。

> 证明状态：**cited**。底本只陈述（§4.1.4 的「Proof of the Bernstein decomposition」只有标题、正文空缺），引理 4.1 亦只陈述。

出处：`A §4.1.1 p.32`

## 常见误解

- 「$R(L,\varsigma)$ 里的不可约表示都是 $I_L(\varsigma\otimes\eta)$ 的子商」不是「都是它的商」：既有子也有商，故 $Q$ 侧与 $Z$ 侧的表示可以同分量。
- Bernstein 中心是集合 $\mathcal B$，不是环；名字里的「中心」来自它与 Bernstein 中心的代数对象（$\mathcal Z$）的对应，底本未展开。

## 相关卡

[惯性对应：Bernstein 中心 ↔ Weil–Deligne 惯性类型（引理 4.3–4.5）](../concepts/inertial-correspondence.md) · [超尖点支撑与 Steinberg 表示 St_n](../concepts/supercuspidal-support.md) · [定理 3.1：Bernstein–Zelevinsky 对 GL_n 容许表示的七条分类](../concepts/bz-classification.md)

## 出处（印刷页）

- A p.32–33（A p.32）

> 说明：分量定义、引理 4.1、Bernstein 中心与定理 4.2 取自 p.32；$\GL_2$ 三类分量与支撑对应取自 p.32–p.33；「直积而非直和」的解读是我们的判断。
