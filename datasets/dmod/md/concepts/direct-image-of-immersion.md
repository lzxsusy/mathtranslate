---
id: dmod/concept/direct-image-of-immersion
type: concept
track: D
---

# 浸入的直像

> 对闭光滑子簇 $i:Y\hookrightarrow X$，$\mathcal D_{Y\to X}$ 局部自由，$i_+$ 可由 $\mathcal O$-模直像张量相对双模写出；特征簇沿法向多一个自由锥。

**问题**：闭浸入的直像为什么能写成「$\mathcal O$-模直像 $\otimes$ 相对双模」，其特征簇与完整性又如何变化？

## 定义

设 $i:Y\hookrightarrow X$ 是光滑簇的光滑闭子簇，$n=\dim X$、$m=\dim Y$。$\mathcal D_{Y\to X}$ 是局部自由 $\mathcal D_Y$-模（命题 4.6.1）。定理 4.6.4 断言 $H^0\circ i_+\circ D\colon V\mapsto i_\bullet(V\otimes_{\mathcal D_Y}\mathcal D_{Y\to X})$ 左正合且 $i_+$ 是它的右导出函子，并且 $\operatorname{supp}(H^0(i_+D(V)))$ 是 $\operatorname{supp}(V)$ 在 $X$ 中的闭包。闭光滑情形 $H^0\circ i_+\circ D$ 正合（4.6.6），此后滥用记号写 $i_+(V)=i_\bullet(V\otimes_{\mathcal D_Y}\mathcal D_{Y\to X})$。

*记号*：$i:Y\hookrightarrow X$：光滑闭浸入，$n=\dim X$、$m=\dim Y$；$D$：把右 $\mathcal D$-模转成左 $\mathcal D$-模的转置函子；$\mathcal D_{Y\to X}$：相对双模；$p_X:T^*X\to X$、$p_Y:T^*Y\to Y$：投影；$\operatorname{holdef}_x(V)=\dim_{p_X^{-1}(x)}\operatorname{Ch}(V)-\dim_xX$。

## 要点

- $\mathcal D_{Y\to X}$ 在适应坐标系 $(f_1,\dots,f_n;D_1,\dots,D_n)$ 下以 $\{D^I\mid I\in\{0\}\times\mathbb Z_+^{n-m}\}$ 为自由左 $\mathcal D_Y$-模的基（引理 4.6.3）；$I(U\cap Y)=(f_{m+1},\dots,f_n)$，$D_1,\dots,D_m$ 保持该理想（引理 4.6.2）。
- 定理 4.6.4：$H^0\circ i_+\circ D$ 左正合，$i_+$ 是其右导出函子，且 $\operatorname{supp}(H^0(i_+D(V)))=\overline{\operatorname{supp}(V)}$（在 $X$ 中取闭包）。
- 闭光滑子簇时 $H^0\circ i_+\circ D$ 正合（4.6.6），$i_+$ 保持凝聚（命题 4.6.7），故可用 $i_\bullet(V\otimes_{\mathcal D_Y}\mathcal D_{Y\to X})$ 直接计算。
- 特征簇（定理 4.6.8）：$\operatorname{Ch}(i_+V)=\{(x,\omega)\in T^*X\mid (x,p_x(\omega))\in\operatorname{Ch}(V)\}$，纤维维数加 $\operatorname{codim}_xY$；完整缺陷 $\operatorname{holdef}$ 沿 $i$ 不变（推论 4.6.9）。

## 关键公式

- $i_+(V)=i_\bullet\bigl(V\otimes_{\mathcal D_Y}\mathcal D_{Y\to X}\bigr)$
- $\mathcal D_{Y\to X}=\bigoplus_{I}\mathcal D_Y\,D^I,\qquad I\in\{0\}\times\mathbb Z_+^{n-m}$
- $\operatorname{Ch}(i_+V)=\{(x,\omega)\in T^*X\mid (x,p_x(\omega))\in\operatorname{Ch}(V)\}$
- $\dim_{p_X^{-1}(x)}\operatorname{Ch}(i_+V)=\dim_{p_Y^{-1}(x)}\operatorname{Ch}(V)+\operatorname{codim}_xY$

## 定理与证明

### 定理 4.6.8（浸入直像的特征簇）（完整）

设 $V$ 是 $Y$ 上的有限生成左 $\mathcal D_Y$-模，则 $\operatorname{Ch}(i_+V)=\{(x,\omega)\in T^*X\mid (x,p_x(\omega))\in\operatorname{Ch}(V)\}$，且 $\dim_{p_X^{-1}(x)}\operatorname{Ch}(i_+V)=\dim_{p_Y^{-1}(x)}\operatorname{Ch}(V)+\operatorname{codim}_xY$。

1. 问题局部：可化到 $x\in Y$ 的小邻域，此时 $Y$ 由 $f_{m+1}=\dots=f_n=0$ 定义，且 $\mathcal D_{Y\to X}$ 是以 $D^I$（$I\in\{0\}\times\mathbb Z_+^{n-m}$）为基的自由左 $\mathcal D_Y$-模。  
   *为什么*：引理 4.6.2、4.6.3 给出适应坐标与该基，特征簇的计算与紧支集无关，故可局部化。
2. 取 $V$ 的好滤过，给 $\Gamma(X,i_+V)$ 配滤过 $F_p=\bigoplus_{s+|I|\le p}F_sV\otimes D^I$。  
   *为什么*：$i_+$ 局部就是 $V\otimes_{\mathcal D_Y}\mathcal D_{Y\to X}$，自由基使直和分解成立，且该滤过是好滤过。
3. 分次化得 $\operatorname{Gr}(i_+V)\cong\operatorname{Gr}V\otimes_kk[\xi_{m+1},\dots,\xi_n]$，其中 $\xi_j$ 是 $D_{m+j}$ 的符号。  
   *为什么*：$\operatorname{Gr}\mathcal D_{Y\to X}$ 在法向由 $D^I$ 的符号生成，正是多项式环 $k[\xi_{m+1},\dots,\xi_n]$，而 $\operatorname{Gr}$ 对张量积与直和相容。
4. 设 $B$ 是 $\operatorname{Gr}V$ 的零化子理想，则 $\operatorname{Gr}(i_+V)$ 的零化子是 $B\otimes_kk[\xi_{m+1},\dots,\xi_n]$，其零点集为 $\operatorname{Ch}(V)\times k^{n-m}$（放在 $T^*X$ 的对应点 $(x,\omega)$ 上）。  
   *为什么*：多项式环上的零化子张量后零点集就是原零点集与仿射空间的积，这是 $\operatorname{Spec}$ 层面的直积。
5. 把第 4 步的集合写回 $X$：$(x,\omega)\in\operatorname{Ch}(i_+V)$ 当且仅当 $(x,p_x(\omega))\in\operatorname{Ch}(V)$；纤维维数等式随之成立，$\operatorname{holdef}$ 不变。  
   *为什么*：第 4 步只见法向坐标，收回 $X$ 时法向维数 $\operatorname{codim}_xY=n-m$ 加到原纤维维数上。

*出处*：定理 4.6.8 / 原书 §6，p.116–118


## 易错点

- $i_+$ 与 $\mathcal O$-模直像 $i_\bullet$ 不是同一个函子：$i_\bullet$ 只给 $\mathcal O_X$-模，$\mathcal D_X$-结构来自再张量 $\mathcal D_{Y\to X}$。
- 特征簇公式不是把 $\operatorname{Ch}(V)$ 原样搬进 $T^*X$：底点经 $i$，余切向量须落在 $p_x$ 的纤维里，法向坐标可任意，这才会多出 $\operatorname{codim}$ 维。
- 正合性只在闭光滑或仿射浸入时成立；一般浸入必须回到定理 4.6.4 的导出版本 $H^0\circ i_+\circ D$，不能默认 $i_+$ 正合。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§6 浸入的直像，p.115-116-117-118（PDF p.121-122-123-124），`源码/chapters/chap4.tex:766-989（定理 4.6.4、定理 4.6.8）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§11 直像（仿射情形），p.47-48（PDF p.53-54），`源码/chapters/chap1.tex:1711-1723（命题 11.3）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/direct-image-functor`
- `dmod/concept/standard-filtration-of-dx-to-y`
- `dmod/concept/characteristic-variety`
