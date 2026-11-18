---
id: dmod/concept/six-operations
type: concept
track: D
---

# D-模的六种运算

> 直像、逆像与外张量、导出张量、导出 Hom、支集截面合称六运算；逆像是直像的右伴随且只能导出化，相容性由 Beck–Chevalley 保证。

**问题**：六种运算各自的角色是什么，$f^+$ 为什么只能作为导出函子出现，运算之间的相容性由哪条公理保证？

## 定义

在光滑簇及其态射的范畴上，D-模的导出范畴带有六种运算：对态射 $f:X\to Y$ 的直像 $f_+$ 与逆像 $f^+$、外张量积 $\boxtimes$、导出张量积 $\otimes^L$、导出 Hom $R\mathcal{H}om$、以及支集落在闭子概形 $Z$ 中的截面 $R\Gamma_Z$。讲义把 $f_+$ 的两套等价定义并列：经转置双模 $\mathcal D_{Y\leftarrow X}$ 作张量，或经相对双模 $\mathcal D_{X\to Y}$ 作转移；$f^+$ 是 $f_+$ 的右伴随，且只能作为导出函子定义。运算之间的相容性即 Beck–Chevalley 型基变换：对拉回方块有 $(p_2)_!\circ(p_1)^*\cong g^*\circ f_!$，配合投影公式构成完整的六运算形式化。

*记号*：$f_+$：本讲义的直像记号（nLab 公理写作 $f_!$）；$f^+$：其右伴随（nLab 写作 $f^!$）；$\boxtimes$：外张量积；$\otimes^L$：导出张量积；$R\mathcal{H}om$：导出内 Hom；$R\Gamma_Z$：支集在 $Z$ 中的截面；$p_1,p_2$：拉回方块的两个投影。

## 要点

- 六种运算的清单：$f_+$、$f^+$、$\boxtimes$、$\otimes^L$、$R\mathcal{H}om$、$R\Gamma_Z$（见 chap4.tex 第 215–217 行的校订批注）。
- $f_+$ 的两套等价定义：经 $\mathcal D_{Y\leftarrow X}=\mathcal D_Y\otimes_{f^{-1}\mathcal D_X}f^{-1}\mathcal D_X$ 作张量，或经 $\mathcal D_{X\to Y}$ 作转移；仿射情形前者写成 $F_+(M)=\mathcal D_{Y\leftarrow X}\otimes_{\mathcal D_X}M$。
- $f^+$ 是 $f_+$ 的右伴随，且只能作导出函子：非导出层面 $\varphi^+$ 不正合，伴随关系与基变换都只在导出范畴中成立。
- 相容性为 Beck–Chevalley：$(p_2)_!\circ(p_1)^*\cong g^*\circ f_!$（对拉回方块），与投影公式一起构成六运算的公理体系。

## 关键公式

- $f_+\colon D(M_R(\mathcal D_X))\to D(M_R(\mathcal D_Y)),\qquad f_+(V)=Rf_\bullet\bigl(V\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y}\bigr)$
- $f^+(V)=\mathcal D_{X\to Y}\otimes^L_{f^{-1}\mathcal D_Y}f^{-1}V$
- $(p_2)_!\circ(p_1)^*\cong g^*\circ f_!$
- $\mathcal D_{Y\leftarrow X}=\mathcal D_Y\otimes_{f^{-1}\mathcal D_X}f^{-1}\mathcal D_X\quad\text{（批注记法）}$

## 定理与证明

### 六运算的相容性（Beck–Chevalley 基变换）（要点（有缺口））

对拉回方块（$f$ 分离），有自然同构 $(p_2)_!\circ(p_1)^*\cong g^*\circ f_!$；与投影公式、$f_!\dashv f^!$ 的伴随一起，六种运算满足 Grothendieck 六运算公理。

1. 把 $f_+$ 写成 $Rf_\bullet(-\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y})$，把逆像写成 $\mathcal D_{X\to Y}\otimes^L_{f^{-1}\mathcal D_Y}f^{-1}(-)$，两者共用同一个相对双模。  
   *为什么*：这是 §5 与 §3 的定义：直像与逆像都由 $\mathcal D_{X\to Y}$ 表达，故基变换的两边可以在同一个双模上比较。
2. 对拉回方块用投影公式（引理 4.4.5 的形式）把张量积从直像内搬到直像外，再比较两边的双模分解。  
   *为什么*：投影公式允许把 $\mathcal D_{Y\to Z}$ 一类的底模张量进出直像，这正是基变换所需的搬移。

> 缺口：讲义只在第 215–217 行的校订批注中声明该形式化并指出对应 nLab 的 six operations 公理，正文未给出 Beck–Chevalley 的证明；完整证明属 Bernstein 的六运算理论（nLab 该页亦仅列公理与文献），故此处记为 sketch。

*出处*：chap4.tex 第 215–217 行批注 / 原书 §1–§2，p.99–108

### 定理 4.5.3（直像与复合相容）（完整）

对态射 $X\xrightarrow{\varphi}Y\xrightarrow{\psi}Z$，有 $\psi_+\circ\varphi_+\cong(\psi\circ\varphi)_+$；且直像可对目标局部化计算。

1. 按定义展开左边：$\psi_+\circ\varphi_+(V^\bullet)=R\psi_\bullet\bigl(R\varphi_\bullet(V^\bullet\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y})\otimes^L_{\mathcal D_Y}\mathcal D_{Y\to Z}\bigr)$。  
   *为什么*：直像的定义 $\varphi_+(V^\bullet)=R\varphi_\bullet(V^\bullet\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y})$ 逐层代入，外层再用 $\psi$ 的直像。
2. 用投影公式（引理 4.4.5）把 $\otimes^L_{\mathcal D_Y}\mathcal D_{Y\to Z}$ 搬入 $R\varphi_\bullet$ 之内：得 $R\psi_\bullet R\varphi_\bullet\bigl(V^\bullet\otimes^L_{\mathcal D_X}\mathcal D_{X\to Y}\otimes^L_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}\mathcal D_{Y\to Z}\bigr)$，其中两个 $\mathcal D_Y$-张量由 $\mathcal D_{X\to Y}$ 的右 $\varphi^{-1}\mathcal D_Y$-作用合并为一个。  
   *为什么*：引理 4.4.5 恰是「底模张量可进出直像」的形式；合并张量只需把 $\mathcal D_{Y\to Z}$ 拉回成 $\varphi^{-1}\mathcal D_Y$-模。
3. 由双模的复合公式 $\mathcal D_{X\to Y}\otimes_{\varphi^{-1}\mathcal D_Y}\varphi^{-1}\mathcal D_{Y\to Z}=\mathcal D_{X\to Z}$（命题 4.1.7）与 Leray 型等式 $R(\psi\circ\varphi)_\bullet=R\psi_\bullet R\varphi_\bullet$，第 2 步的结果就是 $(\psi\circ\varphi)_+(V^\bullet)$。  
   *为什么*：复合双模把中间的双模消去，剩下的正是复合态射的直像定义；直像的复合性即导出函子的复合。

*出处*：定理 4.5.3 / 原书 §5，p.111–113


## 易错点

- 不能用非导出的 $\varphi^+$ 顶替 $f^+$：非导出层面不正合，伴随与基变换都只在导出范畴成立。
- 记号要与 nLab 对齐：本讲义用 $f_+$、$f^+$，nLab 公理用 $f_!$、$f^!$；$f^+$ 是 $f_+$ 的右伴随，不要按「$f^!=f^\ast$」的习惯把它当成拉回。
- $\boxtimes$ 与 $\otimes^L$ 是两个不同运算：前者跨两个簇、$M\boxtimes N=M\otimes_kN$，后者在同一簇上导出化；六运算清单缺一不可。
- $R\Gamma_Z$ 与 $\otimes^L$ 的角色不同：前者是支集限制，不能与直像 $f_+$ 混为「推前」的两种写法。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§1 六运算批注（校订批注），p.99-100-101-102（PDF p.105-106-107-108），`源码/chapters/chap4.tex:211-217（六运算批注；命题 4.1.7 给出双模复合）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§5 直像与复合，p.111-112-113-114（PDF p.117-118-119-120），`源码/chapters/chap4.tex:624-674（定理 4.5.3）`

## 核验

状态：`external-confirmed`（2026-11-19）
- nLab：https://ncatlab.org/nlab/show/six+operations — 该页 Idea 段逐条列出六运算：$(f^\ast\dashv f_\ast)$ 与 $(f_!\dashv f^!)$ 两对伴随、张量/内 Hom 伴随 $((-)\otimes X\dashv[X,-])$，并把「Beck–Chevalley condition (base change formulas)」写成 $g^\ast\circ f_!\simeq(p_2)_!\circ(p_1)^\ast$；与卡中「六运算清单、$f^+\dashv f_+$ 的伴随位置、Beck–Chevalley 基变换」逐条对应（本讲义记 $f_+$、$f^+$ 分别对应该页的 $f_!$、$f^!$）。
- nLab：https://ncatlab.org/nlab/show/D-module — 该页「Six operations yoga」一节称「Discussion of six operations yoga for pull-push of (coherent, holonomic) D-modules is in (Bernstein, around p. 18)」，并称在 D-模上定义六运算的最有效方式是由 $\Omega$-模经 Koszul 对偶转移；支持卡中「D-模上确有六种运算且直像/逆像是其中两族」这一断言。

## 关联

- `dmod/concept/direct-image-functor`
- `dmod/concept/inverse-image-functor`
- `dmod/concept/projection-formula`
