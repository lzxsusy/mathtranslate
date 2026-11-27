# 常数项证明中的 $BH^1$ 应为 $BH^0$

- id：`raskin_glc/correction/bh1-vs-bh0`
- 类型：correction　轨道：B　状态：dev
- 一句话：命题 2.1.5 的证明说 $q_d$ 的纤维是 $BH^1(X,L)$，又说 $H^1(X,L)$ 可缩；但 $d>2g-2$ 时 $H^1=0$，正确纤维是 $R\Gamma(X,L)[1]\simeq H^0(X,L)[1]$，即 $BH^0(X,L)$。把 $H^1$ 与 $H^0$ 混为一谈会让读者以为扩张空间平凡，实际上扩张仍有 $H^0$ 的自同构。

**问题**：为什么 $BH^1$ 与 $BH^0$ 的差别不影响 $q_{d,*}$ 是等价这一结论？

## 位置

§2.1，命题 2.1.5 的证明，原文 p.6（译文 p.8）

## 原文

> the fiber of $q_d$ at a point $L\in\Bun^d_{\Gm}$ can be identified with the classifying stack $BH^1(X,L)$.

## 应为

> the fiber is the vector stack $R\Gamma(X,L)[1]\simeq H^0(X,L)[1]$ for $d>2g-2$, i.e. $BH^0(X,L)$.

## 理由

对 $0\to L\to\cE\to\cO\to0$，自同构群为 $\Hom(\cO,L)=H^0(X,L)$，所以分类叠的连通分量由 $H^0$ 给出；用 $\Ext^1(\cO,L)=H^1(X,L)$ 描述的是扩张的切空间，不是纤维的群。$d>2g-2$ 时 $H^1(X,L)=0$，故 $R\Gamma(X,L)[1]\simeq H^0(X,L)[1]$。$BH^1$ 若按字面理解则为 $B0=\mathrm{pt}$，这会把「扩张空间」误读成单点；原文脚注 1 写的 $R\Gamma(X,L)[1]$ 才是正确的一般陈述。结论仍对：$H^0$ 是向量空间，$\Shv(BH^0)\simeq\Vect$，故 $q_{d,*}$ 仍是等价。

## 说明

译文正文照录 $BH^1$ 并保留「$H^1$ 可缩」的原文措辞，脚注给出 $BH^0$ 与 $R\Gamma[1]$ 两种正确写法；这是「照录原文 + 批注」而非静默改字。

## 出处

- Sam Raskin (lecturer), Lin Chen (notes), Notes for ``Geometric Langlands for Projective Curves'', July 07--11, 2025, 18 pp.，§2.1，命题 2.1.5 的证明，pp. 6；`源码/sections/s02-cusp.tex:L65-L80（正文与译注）`
  > the fiber of qd at a point L ∈Bund Gm can be identified1 the classifying stack BH1(X,L).

## 相关卡

- `raskin_glc/concept/cuspidal-sheaf`
- `raskin_glc/derivation/cuspidal-vanishing`

## 核验（partial，2026-11-27）

- 底本脚注 1（A） / 命题 2.1.5 的脚注：`supports` — 对任意 d，纤维可典范地等同于向量叠 RΓ(X,L)[1]；d>2g-2 时它等于 H^0[1]=BH^0。
- Drinfeld–Gaitsgory, Geometric constant term functor(s), Selecta Math. 22 (2016) / §2：`supports` — 常数项函子的纤维计算与第二伴随的框架；支持「纤维是 RΓ[1] 型向量叠」而不是 BH^1。
- 标准事实 Ext^1(O,L)=H^1(X,L) / 扩张的分类：`supports` — H^1 描述扩张的切空间；H^0 描述自同构群，故纤维的分类叠由 H^0 给出。

结论「q_{d,*} 为等价」不变；错的是纤维的群，不是证明的走向。
