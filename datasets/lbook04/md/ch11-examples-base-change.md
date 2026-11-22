# 函子性的 Galois 例子：基变换、自守诱导、内型

> `lbook04/concept/ch11-examples-base-change` · 轨 G GL_n 的 Langlands 纲领 · 状态 reviewed · 核验 source-only

**问题：** 基变换与自守诱导都是「换域」，为什么方向相反、技术手段也不同？

**一句话：** 基变换用 $W_K\subset W_k$ 的限制把 $H(k)$ 的表示送到 $H(K)$；自守诱导反向使用 $R_{K/k}\mathrm{GL}_n\to\mathrm{GL}_{dn}$；内型提升则是 ${}^LH={}^LG$ 的恒等，三者由扭迹公式或逆定理解决。

**别名：** `基变换`、`自守诱导`、`内型提升`、`迹公式`、`R_{K/k}`

## 定义

Galois 理论的一组例子来自 $W_K\subset W_k$。基变换：取 $G=R_{K/k}H$（Weil 限制），$G(k)=H(K)$，$L$ 同态 ${}^LH={}^LH^0\times\mathcal{G}_k\to(\prod_{\mathcal{G}_K\backslash\mathcal{G}_k}{}^LH^0)\rtimes\mathcal{G}_k={}^LG$ 在局部就是限制映射（把 $W'_K$ 看成 $W'_k$ 的开子群）。已解决：$H=\mathrm{GL}_n$、$K/k$ 可解（$n=2$ 是 Langlands，一般 $n$ 是 Arthur–Clozel，用扭迹公式）；$H=\mathrm{GL}_2$、$K/k$ 非正规三次是 Jacquet–Piatetski-Shapiro–Shalika 用逆定理做的。自守诱导方向相反：$H=R_{K/k}\mathrm{GL}_n$、$G=\mathrm{GL}_{dn}$，把 $K$ 上的表示送到 $k$ 上；$n=2$ 是 Jacquet–Langlands，$n=1$ 是 Kazhdan，一般情形 Arthur–Clozel、Henniart–Herb。内型提升则是 ${}^LH={}^LG$ 的恒等：Jacquet–Langlands $D^\times\to\mathrm{GL}_2$、Rogawski、Deligne–Kazhdan–Vignéras。

**记号：** $K/k$：$d$ 次有限扩张；$R_{K/k}$：Weil 纯量限制；$G(k)=H(K)$；$\mathcal{G}_K\backslash\mathcal{G}_k$：双陪集，对应 $\mathrm{Hom}_k(K,\bar k)$；$D$：$\mathrm{GL}_2$ 的四元数除代数。

## 要点

- 指标集 $\mathcal{G}_K\backslash\mathcal{G}_k$ 与 $\mathrm{Hom}_k(K,\bar k)$ 一一对应，$d$ 次扩张有 $d$ 个元素；这就是 $\prod{}^LH^0$ 出现 $d$ 次的原因。
- 基变换 $k\to K$ 与自守诱导 $K\to k$ 方向相反，不要混。
- 内型之间 ${}^LH={}^LG$，故函子性在这里退化为「同一 $L$ 群下的转移」，但仍是非平凡的表示论。
- 迹公式路线（Arthur–Clozel）与逆定理路线（JPSS）是两条独立的技术路径；前者对可解扩张最有效，后者能处理非正规三次扩张。

## 公式

$$
{}^LH={}^LH^0\times\mathcal{G}_k\longrightarrow\Bigl(\prod_{\mathcal{G}_K\backslash\mathcal{G}_k}{}^LH^0\Bigr)\rtimes\mathcal{G}_k={}^LG
$$

$$
\#(\mathcal{G}_K\backslash\mathcal{G}_k)=[K:k]=d
$$

## 易错点

- 把基变换与自守诱导的方向搞反：基变换从 $k$ 到 $K$（$H(k)\to H(K)$），自守诱导从 $K$ 到 $k$。
- 把内型提升当成不同 ${}^LG$ 之间的同态：内型共享同一个 ${}^LG$，同态是恒等。
- 以为基变换总能解：只对 $H=\mathrm{GL}_n$ 且 $K/k$ 可解（或 $H=\mathrm{GL}_2$ 的三次非正规情形）已知。

## 批注

**〔背景直觉〕为什么基变换能用迹公式**　比较 $H(\mathbb{A}_k)$ 与 $H(\mathbb{A}_K)$ 的（扭）迹公式：几何侧由 $\kappa$-轨道给出，稳定化后两侧的轨道匹配就是基变换。这条路线不构造 $L$ 函数，只用表示的存在性，故对可解扩张最有效。

## 相关

[[ch11-functoriality]]、[[ch11-examples-sym-power]]、[[ch11-dual-group]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§4.1，原书 pp. 260–262（PDF pp. 262–264）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch11.tex:545-628`
