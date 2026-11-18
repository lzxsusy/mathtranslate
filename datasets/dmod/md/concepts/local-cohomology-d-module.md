---
id: dmod/concept/local-cohomology-d-module
type: concept
track: F
---

# $\mathcal D$-模的局部上同调 $R\Gamma_Y$

> 沿闭光滑子簇 $Y$ 的导出局部上同调 $R\Gamma_Y$ 同构于 $i_+\circ Ri^!$，其同调在阶数超过余维数时消没。

**问题**：沿闭光滑子簇取「支集落在 $Y$ 的截面」，在导出范畴里由哪个函子实现？

## 定义

设 $Y$ 是光滑簇 $X$ 的闭光滑子簇，$i:Y\to X$，$U=X-Y$，$j:U\to X$。令 $\Gamma_Y$ 为「支集在 $Y$ 的截面」函子，$R\Gamma_Y$ 为其右导出函子（由引理 4.9.1，$\Gamma_Y$ 的右同调维数 $\le\dim X+1$，故存在）。对下方有界的拟凝聚右 $\mathcal D_X$-模复形 $\mathcal V^\cdot$，在 $D(\mathcal M_R(\mathcal D_X))$ 中有可区别三角 $Rj_\bullet(\mathcal V^\cdot|_U)\to R\Gamma_Y(\mathcal V^\cdot)\to\mathcal V^\cdot\xrightarrow{+1}$；且 $R\Gamma_Y$ 作为 $D(\mathcal M^R_{qc}(\mathcal D_X))$ 上的正合函子同构于 $i_+\circ Ri^!$。

*记号*：$R\Gamma_Y$：$\Gamma_Y$ 的右导出函子；$H^p_Y(\mathcal V)=i_+(R^pi^!(\mathcal V))$：第 $p$ 阶局部上同调；$Rj_\bullet$：开浸入 $j$ 的导出直像；$\mathcal V^\cdot$：下方有界拟凝聚右 $\mathcal D_X$-模复形。

## 要点

- 可区别三角给出「开集外—支集在 $Y$—整体」的分解，且关于 $\mathcal V^\cdot$ 函子性。
- 定理 4.9.3：$R\Gamma_Y\cong i_+\circ Ri^!$ 是三角范畴层面正合函子之间的同构，不是单个模的同构。
- 定理 4.9.9：$\Gamma_Y$ 与 $i^!$ 的右同调维数都 $\le\dim X-\dim Y$，故 $H^p_Y=0$（$p>\dim X-\dim Y$）；引理 4.9.1 的 $\dim X+1$ 只是粗界。
- 支集在 $Y$ 的右 $\mathcal D_X$-模是 $\Gamma_Y$-无循环（引理 4.9.4）；支集在 $Y$ 的拟凝聚模是 $i^!$-无循环（推论 4.9.5）。
- 与代数版本的衔接：$i_+\circ i^!\cong\Gamma_{[Y]}$（定理 4.8.10），拟凝聚时 $\Gamma_{[Y]}=\Gamma_Y$（引理 4.8.11）。
- 批注给出另一种写法 $R\Gamma_Z=\operatorname{RHom}_{\mathcal D_X}(\mathcal D_{X,\infty Z},-)$；与 $\operatorname{RHom}(\mathcal O_{X,\infty Z},\cdot)$ 交换的等式只在拟凝聚时成立。

## 关键公式

- $R\Gamma_Y(\mathcal V^\cdot)\cong i_+\bigl(Ri^!(\mathcal V^\cdot)\bigr)$
- $H^p_Y(\mathcal V)=i_+\bigl(R^pi^!(\mathcal V)\bigr)$
- $H^p_Y=0\quad(p>\dim X-\dim Y)$
- $R\Gamma_Z=\operatorname{RHom}_{\mathcal D_X}(\mathcal D_{X,\infty Z},-)$

## 定理与证明

### 定理 4.9.9（局部上同调的维数界）（完整）

(i) $\Gamma_Y:\mathcal M^R_{qc}(\mathcal D_X)\to\mathcal M^R_{qc}(\mathcal D_X)$ 的右同调维数 $\le\dim X-\dim Y$；(ii) $i^!:\mathcal M^R_{qc}(\mathcal D_X)\to\mathcal M^R_{qc}(\mathcal D_Y)$ 的右同调维数 $\le\dim X-\dim Y$。

1. 对拟凝聚右 $\mathcal D_X$-模 $\mathcal V$ 与 $p\in\mathbb Z_+$ 有 $R^pi^!(\mathcal V)=i^!(H^p_Y(\mathcal V))$，故 (i) 与 (ii) 等价，只需证 (i)。  
   *为什么*：两条断言经这一等式逐阶互换，(i) 成立则 (ii) 成立，反之亦然。
2. 层的内射性是局部性质，故可设 $X$ 仿射、带坐标系 $(f_1,\dots,f_n;D_1,\dots,D_n)$、$Y$ 是 $f_{m+1},\dots,f_n$ 的公共零点集，再对余维 $n-m$ 归纳。  
   *为什么*：消没估计是局部问题；在仿射坐标下 $Y$ 由函数方程切出，才能对余维作归纳。
3. 余维 $1$（$m=n-1$）：$U=\{x:f_n(x)\ne0\}$ 是主开集，$U$ 仿射、$j$ 仿射，故 $R^pj_\bullet(\mathcal V|_U)=0$（$p\ge1$）；由长正合列 $H^{p+1}_Y(\mathcal V)$ 是 $R^pj_\bullet(\mathcal V|_U)$ 的商，得 $H^p_Y=0$（$p\ge2$）。  
   *为什么*：仿射态射没有高阶导出直像，长正合列随即给出 $p\ge2$ 的消没，即余维 $1$ 的界。
4. 一般余维：取 $Z=\{x:f_n(x)=0\}$ 与 $i_1:Y\to Z$、$i_2:Z\to X$；由归纳假设 $i_1^!,i_2^!$ 满足 (ii)，再由 $R(i\circ i_1)^!\cong Ri_1^!\circ Ri^!$（定理 4.9.8）得复合 $i^!$ 满足 (ii)。  
   *为什么*：维数界在复合下相加：$(\dim X-\dim Z)+(\dim Z-\dim Y)=\dim X-\dim Y$。

*出处*：定理 4.9.9 / 原书 §9, p.127

### 定理 4.9.3（$R\Gamma_Y\cong i_+\circ Ri^!$）（要点（有缺口））

函子 $R\Gamma_Y$ 与 $i_+\circ Ri^!$ 作为从三角范畴 $D(\mathcal M^R_{qc}(\mathcal D_X))$ 到自身的正合函子是同构的。

1. 引理 4.9.1 与引理 4.9.2 分别给出 $\Gamma_Y$ 与 $i^!$ 的右同调维数 $\le\dim X+1$，故 $R\Gamma_Y$ 与 $Ri^!$ 都存在。  
   *为什么*：维数有限是导出函子存在的根据，也是后面逐阶比较的前提。
2. 逐阶有 $H^p_Y(\mathcal V)=i_+(R^pi^!(\mathcal V))$，把两侧同调逐项对上即得函子同构 $R\Gamma_Y\cong i_+\circ Ri^!$。  
   *为什么*：两侧都是正合函子，逐阶自然同调相同即给出函子的同构。

> 缺口：讲义对定理 4.9.3 只写「由前述讨论得到」，函子层面同构的自然性与相容性未展开。

*出处*：定理 4.9.3 / 原书 §9, p.125


## 易错点

- 非导出的 $\Gamma_Y$ 只左正合；只有 $R\Gamma_Y$ 的 $H^0$ 才对应它，高阶部分必须用导出函子。
- 消没界是 $\dim X-\dim Y$（余维），不是引理 4.9.1 的 $\dim X+1$；引用时不要取粗界。
- 这不是拓扑层的 $R\Gamma_Y$，而是 $\mathcal D_X$-模的代数局部上同调；$R^pj_\bullet$ 用的是 $\mathcal D$-模直像。
- 批注中的 $\operatorname{RHom}(\mathcal O_{X,\infty Z},\cdot)$ 换位等式只在拟凝聚时成立；对一般模只能保留 $\operatorname{RHom}_{\mathcal D_X}(\mathcal D_{X,\infty Z},-)$ 的写法。
- 定理 4.9.3 的同构是函子之间的，逐项同构不足以说明自然性；引用时要连同函子性一起陈述。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§9 $\mathcal D$-模的局部上同调，p.124–125（PDF p.130–131），`源码/chapters/chap4.tex:1230-1274（定理 4.9.3）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§9 $\mathcal D$-模的局部上同调，p.127（PDF p.133），`源码/chapters/chap4.tex:1346-1365（定理 4.9.9）`

## 核验

状态：`external-confirmed`（2026-11-19）
- Stacks Project：https://stacks.math.columbia.edu/tag/0A6Y — 该引理原文：对 $K,L\in D(A)$ 有典范同构 $R\operatorname{Hom}_{A}(K^{\wedge},L^{\wedge})\to R\operatorname{Hom}_{A}(R\Gamma_{Z}(K),R\Gamma_{Z}(L))$；其证明指出局部上同调由 $C\otimes^{\mathbf{L}}-$ 给出（引 Lemma 47.9.1，tag 0A6R），导出完备化由 $R\operatorname{Hom}_{A}(C,-)$ 给出（引 More on Algebra, Lemma 15.93.10，tag 091V），即局部上同调与完备化经 $\otimes$/$\operatorname{Hom}$ 对偶。这一句支持本卡 key_points 第 6 条「$R\Gamma_{Z}$ 可以写成 $\operatorname{RHom}_{\mathcal{D}_{X}}(\mathcal{D}_{X,\infty Z},-)$ 的同类形式」这一形式对照；但它只是交换环层面的类比，既不是 $\mathcal{D}$-模局部上同调的定义来源，也不覆盖非交换情形。

## 关联

- `dmod/concept/support-localization`
- `dmod/concept/kashiwara-theorem`
- `dmod/concept/kashiwara-base-change`
