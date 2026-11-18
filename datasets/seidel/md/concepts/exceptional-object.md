# 例外对象与例外集

> `seidel/concept/exceptional-object` ｜ track A ｜ draft

**一句话**：自同态只有单位元、其余 $\hom(E,E[i])$ 全为零的对象；一列这样的对象若彼此只有单向态射，就构成例外集。

**自测**：什么样的对象可以充当「单胞」，把一个三角范畴拆成有限层、从而得到显式的 Postnikov 分解？

## 定义

设 $\A$ 是 $c$-有限（对任意 $Y_0,Y_1$，$\Hom_{H(\A)}(Y_0,Y_1)$ 有限维）的三角化 $A_\infty$ 范畴。对象 $E$ 称例外对象，若
$$\Hom_{H(\A)}(E,E)=\K\cdot[e_E],\qquad \Hom_{H(\A)}(E,E[i])=0\quad(i\neq0).$$
有限有序族 $\Y=(Y_1,\ldots,Y_m)$ 称例外集，若 (i) 每个 $Y_k$ 都是例外对象；(ii) $k>l$ 时 $\Hom_{H(\A)}(Y_k,Y_l)=0$。若该族还按 §3j 的意义生成 $\A$，称满例外集。
例外性把 $E$ 的整个自同态代数压成 $\K$：没有高阶自同态，也没有平移后的自同态。这正是「单胞」的代数版本——每层只贡献一个 $\K$。
满例外集使任意对象都能沿该族作有限阶梯式分解：逐次扭转 $T_{Y_1}\cdots T_{Y_m}$ 把它打到零（引理 5.13），反向读出即得 Postnikov 分解 (5.23)。

记号：$\Hom_{H(\A)}$ 记 $H^0(\A)$ 的 hom 空间；$\Y=(Y_1,\dots,Y_m)$ 的顺序是数据的一部分；满例外集也称 full exceptional collection。

## 要点

- 例外集是「有序」的：$k>l\Rightarrow\Hom(Y_k,Y_l)=0$ 的单向性让族里的对象像单胞一样逐层搭建，顺序不能随手改。
- 满例外集 ⇒ 任意 $X$ 的逐次扭转为零（引理 5.13）：$T_{Y_1}\cdots T_{Y_m}(X)\cong0$，这是最干净的判别法。
- 该证明同时给出显式 Postnikov 分解 (5.23)，其中 $Z_k=\Hom_{H(\A)}(Y_k,X_k)$；分解的层数与族长相同，故「满」是本质条件。
- 经典例子：$\mathbb P^n$ 的导出范畴由 $\mathcal O,\mathcal O(1),\ldots,\mathcal O(n)$ 满例外生成；这也解释了半正交分解的来源。
- 变异在例外集上作用：基本变异 $U_k=T_{Y_k}Y_{k+1}$、$U_{k+1}=Y_k$ 仍是例外集，辫关系成立，群 $\Z^m\rtimes\mathrm{Br}_m$ 作用于长度 $m$ 的例外集同构类。

## 公式

$$\Hom(E,E)=\K,\qquad \Hom(E,E[i])=0\quad(i\neq0)$$
$$k>l\ \Longrightarrow\ \Hom_{H(\A)}(Y_k,Y_l)=0,\qquad \Hom(Y_k,Y_k)=\K\cdot[e_{Y_k}]$$
$$T_{Y_1}\cdots T_{Y_m}(X)\cong0\qquad(\Y\ \text{满例外集},\ \forall X)$$
$$Z_k=\Hom_{H(\A)}(Y_k,X_k)$$

## 定理与证明

### 引理 5.13（满例外集使逐次扭转为零）

设 $\Y=(Y_1,\ldots,Y_m)$ 是 $c$-有限三角化 $A_\infty$ 范畴 $\A$ 的满例外集。则对任意 $X$，在 $H^0(\A)$ 中有同构 $T_{Y_1}\cdots T_{Y_m}(X)\cong0$。

（complete；来源：原书 p.76 引理 5.13）

1. 令 $X_m=X$，$X_{k-1}=T_{Y_k}(X_k)$，逐层考察 $\Hom(Y_k,X_k)$。  
   为什么：扭转 $T_{Y_k}$ 由沿 $Y_k$ 的锥构成，只改动 $\Hom(Y_k,-)$ 方向的分量，故可逐层控制。
2. 先取 $X=Y_l$。对 $k>l$ 有 $\Hom(Y_k,Y_l)=0$，由扭转的显式公式 (5.4) 得 $X_{k-1}\cong X_k\cong\cdots\cong X$。  
   为什么：当 $\Hom(Y_k,-)=0$ 时锥退化，扭转在该对象上是恒等，逐层都不动它。
3. 第 $l$ 步把 $Y_l\xrightarrow{[e_{Y_l}]}X_l\cong Y_l$ 三角化，得 $X_{l-1}\cong\Cone(e_{Y_l})\cong0$。  
   为什么：以单位元作锥：$e_{Y_l}$ 是同构，其锥同调为零。
4. 于是 $k<l$ 的 $X_k$ 全为零（$T_{Y_k}$ 把零送到零），特别 $T_{Y_1}\cdots T_{Y_m}(Y_l)\cong0$。  
   为什么：函子保持零对象与同构，故一旦某层归零，后续层都为零。
5. 对一般 $X$：$F=T_{Y_1}\cdots T_{Y_m}$ 是 $A_\infty$ 函子，由推论 3.9 保持正合三角并与平移交换；它在生成族 $Y_k$ 上为零，故在任意 $X$ 上为零。  
   为什么：生成性把「在生成元上为零」提升为「处处为零」：任何 $X$ 由 $Y_k$ 经有限次锥与平移得到，而 $F$ 保持这些构造。

缺口：原书对「在生成元上为零 ⇒ 处处为零」用得很快；严格说需对 $X$ 的构造长度作归纳，或在 $H^0$ 中把 $F$ 视为三角函子再引用生成性。

### 满例外集给出半正交分解

若 $\Y=(Y_1,\ldots,Y_m)$ 是 $H^0(\A)$ 的满例外集，则 $H^0(\A)=\langle Y_1,\ldots,Y_m\rangle$ 是半正交分解：每个 $\langle Y_k\rangle$ 由单个例外对象生成，且 $k>l$ 时 $\Hom(Y_k,Y_l[*])=0$。

（sketch；来源：原书 p.75–76 §5i）

1. 每个 $Y_k$ 例外的条件下，$\langle Y_k\rangle$ 是极小的三角子范畴，只含 $Y_k$ 的有限次平移与锥。  
   为什么：$\Hom(Y_k,Y_k)=\K$ 使 $Y_k$ 没有非平凡直和项，任何由它生成的对象都是它的若干次平移的锥。
2. $k>l$ 时 $\Hom(Y_k,Y_l[*])=0$：例外性给出 $i\neq0$ 时 $\Hom(Y_k,Y_k[i])=0$，单向性给出 $i=0$ 时为零，两者合起来就是所有阶为零。  
   为什么：前者是例外对象的定义，后者是例外集的 (ii)，只需把 $[i]$ 的平移吸收进下标。
3. 满性把 $\Y$ 生成的三角子范畴等于 $H^0(\A)$，于是得到分解。  
   为什么：半正交分解的定义就是「单向的三角子范畴族生成整个范畴」。

缺口：原书在 §5i 之后讨论变异时才明确使用半正交分解的语言；这里按 Bondal 的术语重述，$\langle\cdot\rangle$ 指三角生成，未讨论可容许性。

## 易错点

- 「例外」是对 $H^0$ 说的：$\Hom(E,E)=\K$ 只约束上同调层面的自同态，$E$ 的链层自同态可以有很多（高阶运算仍可非零）。
- 顺序是数据：把例外集反序一般不再是例外集，因为 $k>l$ 的单向性会全部反过来。
- 满例外集比「生成」强得多：只生成还不够，还要求每层恰好一个对象且只有 $\K$ 个自同态；残缺的族做不出 Postnikov 分解。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§5i，p.75–75（原书 p.75 §5i）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§5i，p.76–76（原书 p.76 §5i）

关联：`seidel/concept/split-generation`、`seidel/concept/exact-triangle`、`seidel/concept/karoubi-envelope`、`seidel/concept/twisted-complex`

来源说明：原书 p.75 定义、p.76 引理 5.13 及其证明（(5.23) 的 Postnikov 分解）；译者注 A03-12（nLab exceptional collection，B 级）。
