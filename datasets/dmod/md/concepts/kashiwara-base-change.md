---
id: dmod/concept/kashiwara-base-change
type: concept
track: F
---

# Kashiwara 基变换（闭浸入情形）

> Kashiwara 基变换把 $i^!$ 移到直像之后：闭浸入情形靠可区别三角配 $Ri^!\circ Rj_\bullet=0$ 与 $i^!\circ i_+\cong\operatorname{id}$ 两条输入。

**问题**：为什么沿闭浸入的 $i^!$ 可以与光滑态射的直像交换，靠的是哪两条输入？

## 定义

设 $i:Y\to S$ 是闭浸入、$\varphi:X\to S$ 是光滑态射，$i':\varphi^{-1}(Y)\to X$ 与 $\varphi':\varphi^{-1}(Y)\to Y$ 是限制，$U=S-Y$、$j:U\to S$、$j':\varphi^{-1}(U)\to X$。闭浸入情形的 Kashiwara 基变换断言 $$Ri^!\circ\varphi_+\cong\varphi'_+\circ Ri'^!,$$ 它是定理 4.10.2 的 $\psi^!\circ\varphi_+\cong\varphi'_+\circ\psi'^!$ 在 $\psi=i$ 时的形式。证明只用两条输入：$Ri^!\circ Rj_\bullet=0$（引理 4.9.10）与 $i^!\circ i_+\cong\operatorname{id}$（定理 4.8.10，即 Kashiwara 定理）。

*记号*：$Ri^!$：$i^!$ 的右导出函子；$Rj_\bullet$：开浸入的导出直像；$R\Gamma_{\varphi^{-1}(Y)}$：沿纤维闭子集的局部上同调；$\varphi'=\varphi|_{\varphi^{-1}(Y)}$；$[\,]$：平移。

## 要点

- 核心是可区别三角：把 $\mathcal V^\cdot$ 换成 $R\Gamma_{\varphi^{-1}(Y)}(\mathcal V^\cdot)$ 不改变 $Ri^!\varphi_+(\mathcal V^\cdot)$，因为差项落在 $Rj_\bullet$ 的像里而被 $Ri^!$ 杀掉。
- 两条输入都来自 §8–§9：引理 4.9.10（$Ri^!\circ Rj_\bullet=0$）与定理 4.8.10（$i^!\circ i_+\cong\operatorname{id}$）。
- 截断点论证把「下方有界」推广到任意拟凝聚复形，依据是所涉函子的同调维数有限。
- 推论 4.10.3（$\varphi(X)\cap\psi(Y)=\varnothing$ 时复合为 $0$）是同一机制的极端情形：纤维积为空。
- 与六函子形式的 Beck–Chevalley 同构形状一致，但这里是 $\mathcal D$-模的 $!$ 与 $+$ 函子，不是层的 $!$、$*$。

## 关键公式

- $Ri^!\circ\varphi_+\cong\varphi'_+\circ Ri'^!$
- $Ri^!\circ Rj_\bullet=0$
- $i^!\circ i_+\cong\operatorname{id}$
- $Ri^!\bigl(\varphi_+(R\Gamma_{\varphi^{-1}(Y)}(\mathcal V^\cdot))\bigr)\xrightarrow{\sim}Ri^!\bigl(\varphi_+(\mathcal V^\cdot)\bigr)$

## 定理与证明

### 定理 4.10.2 的闭浸入情形（Kashiwara 基变换）（完整）

设 $i:Y\to S$ 是闭浸入、$\varphi:X\to S$ 光滑，且 $\varphi^{-1}(Y)$ 是 $X$ 的光滑闭子簇。则在 $D(\mathcal M_{qc}(\mathcal D_X))$ 上有 $Ri^!\circ\varphi_+\cong\varphi'_+\circ Ri'^!$。

1. 取可区别三角 $Rj'_\bullet(\mathcal V^\cdot|_{\varphi^{-1}(U)})\to R\Gamma_{\varphi^{-1}(Y)}(\mathcal V^\cdot)\to\mathcal V^\cdot$，依次施导出函子 $\varphi_+$ 与 $Ri^!$。  
   *为什么*：把 $\mathcal V^\cdot$ 与它沿纤维闭子集的局部化用三角联系起来，只需比较两端。
2. 首项化为 $\varphi_+(Rj'_\bullet(\mathcal V^\cdot|_{\varphi^{-1}(U)}))=Rj_\bullet(\varphi_+(\mathcal V^\cdot)|_U)$（用 $\varphi\circ j'=j\circ\varphi''$），再由引理 4.9.10 得 $Ri^!$ 在其上为 $0$；于是 $Ri^!(\varphi_+(R\Gamma_{\varphi^{-1}(Y)}(\mathcal V^\cdot)))\to Ri^!(\varphi_+(\mathcal V^\cdot))$ 是同构。  
   *为什么*：差项被杀掉，两端因此在该同构下可以互换，这正是基变换的全部内容。
3. 对左边用 $\Gamma_{\varphi^{-1}(Y)}=i'_+\circ Ri'^!$ 与 $i^!\circ i_+\cong\operatorname{id}$ 化简：$Ri^!(i_+(\varphi'_+(Ri'^!(\mathcal V^\cdot))))=\varphi'_+(Ri'^!(\mathcal V^\cdot))$。  
   *为什么*：这里用到 Kashiwara 定理：$i^!$ 是 $i_+$ 的拟逆，故 $i^!\circ i_+$ 可以消去。
4. 由所涉函子同调维数有限，截断点论证把上述同构从下方有界复形推广到任意拟凝聚复形。  
   *为什么*：维数有限使复形可以逐段截断比较，从而去掉下方有界假设。

*出处*：定理 4.10.2（闭浸入情形）/ 原书 §10, p.130–132

### 推论 4.10.3（不相交时复合为零）（要点（有缺口））

设 $X,Y,Z$ 是光滑代数簇，$\varphi:X\to Z$、$\psi:Y\to Z$ 是态射且 $\varphi(X)\cap\psi(Y)=\varnothing$。则在 $D(\mathcal M_{qc}(\mathcal D_X))$ 上 $\psi^!\circ\varphi_+=0$。

1. 将 $\psi^!\circ\varphi_+$ 经基变换改写为 $\varphi'_+\circ\psi'^!$，此时纤维积 $X\times_ZY=\varnothing$。  
   *为什么*：不相交正是纤维积为空的情形，基变换把复合搬到空纤维积上。
2. 空纤维积上直像与 $!$-函子都取零对象，故复合为 $0$。  
   *为什么*：两端都定义在空簇上，函子作用的结果只能是零对象。

> 缺口：讲义只给出推论陈述，未单独证明；本卡按定理 4.10.2 的空纤维积情形复原，未写出空簇上函子取值的技术细节。

*出处*：推论 4.10.3 / 原书 §10, p.132


## 易错点

- 闭浸入情形的结论是 $Ri^!\circ\varphi_+\cong\varphi'_+\circ Ri'^!$，其中的 $i^!$ 必须取导出函子；未导出的 $i^!$ 不右正合。
- 截断点论证依赖「所涉函子同调维数有限」，去掉它只能得到下方有界复形上的同构。
- 不要与层论六函子的 $!$、$*$ 混为一谈：$\varphi_+$ 是 $\mathcal D$-模直像，不是层直像。
- 若 $\varphi$ 非光滑，$\varphi_+$ 与 $!$-函子的性质都会变，基变换公式失效；本卡的光滑性由 $\varphi$ 与 $\varphi'$ 承担。
- 定理 4.10.2 的投影情形另需 $[-\dim S]$ 平移，与本卡的闭浸入情形不能混用同一个公式。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§10 基变换（定理 4.10.2 的证明），p.130–132（PDF p.136–138），`源码/chapters/chap4.tex:1473-1537（定理 4.10.2、推论 4.10.3）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/base-change-for-d-modules`
- `dmod/concept/kashiwara-theorem`
- `dmod/concept/local-cohomology-d-module`
