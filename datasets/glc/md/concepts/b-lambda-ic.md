---
id: glc/concept/b-lambda-ic
type: concept
track: C
---

# 局部 IC 层 $B_{\lambda,x}$（定义 4.8.1）与仿射 Grassmann 簇的比较

> $B_{\lambda,x}:=\operatorname{IC}_{\overline{\operatorname{Tor}_x^\lambda}}$ 与 Schubert 层 $A_\lambda$ 差光滑拉回与移位 $[dn]$。

**问题**：局部 IC 层 $B_{\lambda,x}$ 如何定义，它与仿射 Grassmann 簇上的 Schubert 层 $A_\lambda$ 通过光滑拉回如何对应？

## 定义

对分拆 $\lambda\vdash d$，定义 $B_{\lambda,x}:=\operatorname{IC}_{\overline{\operatorname{Tor}_x^\lambda}}$。与仿射 Grassmann 簇的关系如下：令 $\operatorname{Gr}_{n,x}^{d,\mathrm{mod}}$ 为次数 $d$ 的正修改轨迹（其点是 $\mathcal{O}_x^n$ 的长度 $d$ 商的轨迹，不应与正则幂零轨迹混淆），$f:\operatorname{Gr}_{n,x}^{d,\mathrm{mod}}\to\operatorname{Tor}_x^d$ 为将修改映为其商挠层的映射；它的像是最多可由 $n$ 个元素生成的挠层所构成的开子叠，在这一像上 $f$ 光滑、相对维数为 $nd$。对 $|\lambda|=d$ 且 $\ell(\lambda)\le n$，令 $\operatorname{Gr}_{n,x}^\lambda$ 为型 $\lambda$ 的 Schubert 分层，置 $A_\lambda:=\operatorname{IC}_{\overline{\operatorname{Gr}_{n,x}^\lambda}}$。采用 IC 包括反常上同调移位但不包括 Tate 扭转的约定，光滑拉回给出 $f^*B_{\lambda,x}\simeq A_\lambda[-dn]$，等价地 $f^*B_{\lambda,x}[dn]\simeq A_\lambda$。

*记号*：$\overline{\operatorname{Tor}_x^\lambda}$ 为局部层的闭包；$\operatorname{Gr}_{n,x}$ 为 $\operatorname{GL}_n$ 在 $x$ 处的仿射 Grassmann 簇；$\operatorname{Gr}_{n,x}^{d,\mathrm{mod}}$ 为次数 $d$ 正修改轨迹；$\ell(\lambda)$ 为分拆长度。

## 要点

- $B_{\lambda,x}$ 是幂零轨道（局部层）闭包上的 IC 层，定义本身只用到 $\operatorname{Tor}_x^\lambda$ 与其闭包，属局部构造。
- $f$ 把 $\mathcal{O}_x^n$ 的长度 $d$ 商送到该商作为挠层；像不是整个 $\operatorname{Tor}_x^d$，而是「最多 $n$ 个元素生成」的开子叠，讲义指出 $f$ 在该像上光滑、相对维数为 $nd$。
- 两个 IC 的差别只是移位：约定 IC 含反常上同调移位、不含 Tate 扭转；$f$ 光滑且相对维数 $nd$，故光滑拉回把 $\operatorname{IC}$ 搬成 $\operatorname{IC}$ 再移位 $-dn$。
- 局部 Laumon 公式里的 Tate 因子 $-n(\lambda)$ 不属于这个比较，它属于 Whittaker／Casselman–Shalika 归一化；因此 $B_{\lambda,x}$ 与 $A_\lambda$ 的对应里没有 $n(\lambda)$，只有 $dn$。

## 关键公式

- $B_{\lambda,x}:=\operatorname{IC}_{\overline{\operatorname{Tor}_x^\lambda}}$
- $f:\operatorname{Gr}_{n,x}^{d,\mathrm{mod}}\longrightarrow\operatorname{Tor}_x^d$
- $A_\lambda:=\operatorname{IC}_{\overline{\operatorname{Gr}_{n,x}^\lambda}}$
- $f^*B_{\lambda,x}\simeq A_\lambda[-dn]\qquad\Longleftrightarrow\qquad f^*B_{\lambda,x}[dn]\simeq A_\lambda$
- $\dim\operatorname{Gr}_{n,x}^{d,\mathrm{mod}}-\dim\operatorname{Tor}_x^d=nd$

## 定理与证明

### 光滑拉回比较 $f^*B_{\lambda,x}\simeq A_\lambda[-dn]$（要点（有缺口））

在 $f$ 的像（最多 $n$ 个元素生成的挠层所构成的开子叠）上，$f$ 光滑、相对维数为 $nd$；采用 IC 含反常上同调移位但不含 Tate 扭转的约定，有 $f^*B_{\lambda,x}\simeq A_\lambda[-dn]$，等价地 $f^*B_{\lambda,x}[dn]\simeq A_\lambda$。

1. 用 $\mathcal{O}_x^n$ 的长度 $d$ 商刻画 $\operatorname{Gr}_{n,x}^{d,\mathrm{mod}}$，并把它映到商挠层。  
   *为什么*：这是 $f$ 的定义；讲义强调该记号不应与正则幂零轨迹混淆。
2. 确定像为「最多 $n$ 个元素生成」的开子叠，并在其上验证 $f$ 光滑、相对维数 $nd$。  
   *为什么*：光滑性与相对维数由修改的自由度计出，讲义直接陈述。
3. 对光滑映射按相对维数作 IC 拉回：$f^*\operatorname{IC}= \operatorname{IC}[-dn]$，把 $B_{\lambda,x}$ 送到 $A_\lambda$。  
   *为什么*：这是 IC 沿光滑映射拉回的标准行为，讲义只列结论并声明所用约定。

> 缺口：讲义只陈述像的开性、$f$ 的光滑性与相对维数 $nd$，以及拉回同构，未给证明；IC 的约定（含移位、不含 Tate 扭转）也是作为约定引入的。

*出处*：§4.8 定义 4.8.1（原书 p.30）、§4.10（原书 p.31）


## 易错点

- 移位是 $dn$，不是 $n(\lambda)$：$n(\lambda)=\sum_i(i-1)\lambda_i$ 属 Whittaker／Casselman–Shalika 归一化，不在这个光滑拉回比较里出现。
- $\operatorname{Gr}_{n,x}^{d,\mathrm{mod}}$ 是「长度 $d$ 商」的轨迹，不是正则幂零轨迹；讲义专门提醒这一记号易混。
- $f$ 的像只是开子叠（最多 $n$ 个元素生成的挠层），不是整个 $\operatorname{Tor}_x^d$；在该像之外不能直接用这个拉回比较。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§4.8 定义 4.8.1；§4.10 与仿射 Grassmann 簇的关系，p.30-31（PDF p.30-31），`源码/chapters/ch04.tex:143-146,160-169（§4.8 定义 4.8.1、§4.10）`

## 核验

状态：`external-confirmed`（2026-11-18）
- FGKV98：https://arxiv.org/abs/alg-geom/9703022 — 卡里『B_{λ,x} := IC_{closure of Tor_x^λ}』对应原文『B_{λ,x} denote the intersection cohomology sheaf associated to the constant sheaf on the stratum Coh^λ_{n,m}(x)』；卡里『叠 Tor_x^d 维数 −d』对应原文 dimension −m 的说明。
- GPR20：https://arxiv.org/abs/2002.12480 — 卡里『B_{λ,x} 是幂零轨道闭包上的 IC 层、按分拆 λ 编号』对应原文『each pair (O,L) corresponds to a simple perverse sheaf IC(O,L) on N』与式 (2.3)。
- nLab：https://ncatlab.org/nlab/show/perverse+sheaf — 卡里『IC 层是分层闭包的中间延拓』的规范性由该页确认：『simple objects are the intersection cohomology sheaves (with that perversity) of closures of strata』。
- nLab：https://ncatlab.org/nlab/show/affine+Grassmannian — 卡里 §4.10 的 Gr_{n,x} 作为仿射 Grassmann 簇（lattice / GL_n(K)/GL_n(O) 的 ind-scheme）由该页定义确认。

## 关联

- `glc/concept/torsion-stratification`
- `glc/concept/local-laumon-formula`
- `glc/concept/local-factorization`
