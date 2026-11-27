# 超尖点支撑与 Steinberg 表示 St_n

> `yao17/concept/supercuspidal-support` · 轨道 分类与不变量 · 状态 dev

> **先自测**：超尖点支撑为什么是「唯一无序组」？Steinberg 表示是怎么作为一个段诱导的唯一不可约商出现的？

## 一句话

超尖点支撑是 Q 与 Z 共有的唯一无序超尖点组；取 Δ=[|·|^{(1−n)/2},…,|·|^{(n−1)/2}] 时 Z(Δ)=triv、Q(Δ)=St_n（自对偶）。

## 定义

对 $\pi\cong Q(\Delta_1,\dots,\Delta_r)$，$\Delta_i=\Delta(\pi_i,m_i)$，超尖点支撑是（无序）集合 $\Supp(\pi)=\{\pi_i(j)\}_{i=1..r,\ j=0..m_i-1}$。Zelevinsky 注：$\Supp(\pi)$ 是唯一的无序组 $\sigma_1,\dots,\sigma_s$，使 $Q(\Delta_1,\dots,\Delta_r)$ 与 $Z(\Delta_1,\dots,\Delta_r)$ 都是 $\sigma_1\times\dots\times\sigma_s$ 的子商。取 $\Delta=\Delta(|\cdot|^{(1-n)/2},n)=[|\cdot|^{(1-n)/2},|\cdot|^{(3-n)/2},\dots,|\cdot|^{(n-1)/2}]$，则 $\pi(\Delta)=|\cdot|^{(1-n)/2}\times\dots\times|\cdot|^{(n-1)/2}=\{B\backslash G\ \text{上的光滑函数}\}$，$Z(\Delta)=\mathrm{triv}$（常函数），$Q(\Delta)=:\St_n$ 称（标准）Steinberg 表示，自对偶 $\St_n^\vee=\St_n$。

**记号**：模特征标在 $B$ 上：$x=\mathrm{Diag}(x_1,\dots,x_n)$ 时 $\delta(x)=|x_1^{n-1}x_3^{n-3}\cdots x_n^{1-n}|$；这里 $\pi_T=|\cdot|^{(1-n)/2}\otimes\dots\otimes|\cdot|^{(n-1)/2}=\delta^{-1/2}$。

## 要点（为什么需要它）

1. 支撑的定义只用到 $Q(\Delta_i)$ 的段的成员，与排列无关；Zelevinsky 注的力道在于：$Q$ 侧与 $Z$ 侧（商与子）诱导出同一个无序组，故支撑是 $\pi$ 的内在不变量，而不是某个分解的附属物。
2. $\St_n$ 的构造是「把 $\delta^{-1/2}$ 当成 $T$ 上的特征标诱导上去」：此时 $\pi(\Delta)$ 就是 $(B\backslash G)$ 上的光滑函数空间（未正规化诱导 = 右平移作用），常函数给出唯一不可约子 $\mathrm{triv}$，商即 $\St_n$。
3. $n=2$ 时给出短正合列 $0\to\mathrm{triv}\to|\cdot|^{-1/2}\times|\cdot|^{1/2}\to\St_2\to0$；反过来 $|\cdot|^{1/2}\times|\cdot|^{-1/2}$ 的短正合列是 $0\to\St_2\to\cdot\to\mathrm{triv}\to0$——两个顺序给出相反的「子/商」，这正是 (∗) 与 linked 的几何内容。
4. $\St_n$ 自对偶（$\St_n^\vee=\St_n$）在 $\GL_2$ 情形对应 $\Sp_2$ 的 WD 表示，在一般 $n$ 对应 $\Sp_n$——Steinberg 是「最非半单」的不可约表示，其 $N$ 的幂零指数恰为 $n$。

## 核心公式

$$
$\Supp(\pi)=\{\pi_i(j)\}_{i=1..r,\ j=0..m_i-1}\quad(\text{无序})$$\Delta(|\cdot|^{(1-n)/2},n)=[|\cdot|^{(1-n)/2},|\cdot|^{(3-n)/2},\dots,|\cdot|^{(n-1)/2}]$$Z(\Delta)=\mathrm{triv},\qquad Q(\Delta)=\St_n,\qquad \St_n^\vee=\St_n$$0\to\mathrm{triv}\to|\cdot|^{-1/2}\times|\cdot|^{1/2}\to\St_2\to0\ (n=2)$
$$

$$
$\Delta(|\cdot|^{(1-n)/2},n)=[|\cdot|^{(1-n)/2},|\cdot|^{(3-n)/2},\dots,|\cdot|^{(n-1)/2}]$
$$

$$
$Z(\Delta)=\mathrm{triv},\qquad Q(\Delta)=\St_n,\qquad \St_n^\vee=\St_n$
$$

$$
$0\to\mathrm{triv}\to|\cdot|^{-1/2}\times|\cdot|^{1/2}\to\St_2\to0\ (n=2)$
$$

## 常见误解

- 支撑里的 $\pi_i(j)$ 含 $j=0$ 到 $m_i-1$ 共 $m_i$ 项，容易只写 $m_i-1$ 项（底本 p.25 的排版也只写到 $j=1,\dots,m_i-1$，实为漏了 $j=0$，见下条）。
- $\St_n$ 不是 $\pi(\Delta)$ 本身而是它的不可约商；$\pi(\Delta)$ 的长度为 $2^{n-1}$，只有 $n=2$ 时才只有两个 Jordan–Hölder 因子。

## 相关卡

[Zelevinsky 段 Δ(π,m)、linked/precedes 与 (∗) 条件](../concepts/zelevinsky-segment.md) · [定理 3.1：Bernstein–Zelevinsky 对 GL_n 容许表示的七条分类](../concepts/bz-classification.md) · [本质 L^r、平方可积、缓增：定理 3.2、3.3 与推论 3.4](../concepts/square-integrable-tempered.md) · [GL₂ 的四类表示如何对应到 Weil–Deligne 表示](../derivations/gl2-llc-cases.md)

## 出处（印刷页）

- A p.25–26（A p.26）

> 说明：支撑定义与 Zelevinsky 注取自 p.25；Steinberg 的构造、δ 公式、$\mathrm{triv}$/$\St_2$ 两条短正合列取自 p.25–p.26。第一条 pitfalls 中「底本写作 $j=1,\dots,m_i-1$」是转录所见，与我们按定义补的 $j=0$ 不一致，已在译本作译注。
