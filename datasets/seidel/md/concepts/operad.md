# 操作子（operad）

> `seidel/concept/operad` ｜ track A ｜ draft

**一句话**：用「n 元运算的合成法则」编码代数结构的语言；A∞ 操作子是结合操作子的 dg 分辨，其代数的 μ^d 正对应分辨的胞腔。

**自测**：为什么把结合律放松到「只差同伦」，需要换一个操作子，而不是在结合代数里再添几条高阶关系？

## 定义

操作子 $\mathcal O$ 是一族链复形 $\mathcal O(n)$（$n\ge0$），每个带对称群 $S_n$ 的右作用，配有单位 $\mathbf 1\in\mathcal O(1)$ 与合成映射
$$\gamma:\mathcal O(k)\otimes\mathcal O(n_1)\otimes\cdots\otimes\mathcal O(n_k)\longrightarrow\mathcal O(n_1+\cdots+n_k),$$
把 $k$ 元运算的每个输入替换成一个 $n_i$ 元运算，并要求 $\gamma$ 满足结合律、单位律与 $S_n$-等变性。一个 $\mathcal O$-代数是一个链复形 $A$ 连同一族映射 $\mathcal O(n)\otimes A^{\otimes n}\to A$，与 $\gamma$ 及单位相容。直观上 $\mathcal O(n)$ 是「$n$ 元运算的模板空间」，$\gamma$ 是「把模板接成一棵树」的法则；$\mathcal O$-代数就是把这些模板实现为 $A$ 上真正的多重线性运算。
需要它的理由：Fukaya 范畴的圆盘计数只在同伦意义下结合，严格的结合代数（$\mathrm{Ass}$-代数）装不下这些数据。把 $\mathrm{Ass}$ 换成一个 dg 分辨 $\mathcal A_\infty\to\mathrm{Ass}$，$\mathcal A_\infty$-代数便自动带上一串高阶运算 $\mu^d$，其二次关系恰是 $\partial^2=0$ 的展开——这就是 A∞ 代数。原书 p.7 明说不使用操作子语言，但命题 1.12 中按分拆求和的递归公式，就是「把分辨搬到范畴上」的显式版本。

记号：$\mathcal O(n)$ 的次数指内部次数，$\gamma$ 的次数为 $0$；非对称版本 $\mathrm{Ass}(n)=\mathbb K$，对称版本 $\mathrm{Ass}(n)=\mathbb K[S_n]$。

## 要点

- 合成 $\gamma$ 是「代入」而不是「相乘」：$\mathcal O(k)$ 的一个 $k$ 元运算吞掉 $k$ 个运算，得到 $\sum_i n_i$ 元运算；它与 $S_n$-作用、单位一起满足结合律与单位律。
- A∞ 操作子是 $\mathrm{Ass}$ 的 dg 分辨：非对称版本里 $\mathcal A_\infty(n)=C_*(K_n)$（$K_n$ 为 $n$ 个输入的结合多面体，$\dim K_n=n-2$，$n\ge2$）可缩，$\mathcal A_\infty\to\mathrm{Ass}$ 逐项为拟同构，故 $\mathcal A_\infty$-代数正是 A∞ 代数。
- $\mu^d$ 是最高维胞腔的像，$\deg\mu^d=2-d$；A∞ 关系是「$\partial$ 把最高维胞腔展成低维面」再经结构映射得到的等式，实质是 $\partial^2=0$ 与链映射相容。
- 分辨只在操作子拟同构意义下唯一：associahedron、brace、树操作子给出同一个同伦论，但公式与符号不同，不能混用。
- Fukaya 范畴需要它，是因为伪全纯圆盘模空间的边界分层恰是低维模空间的乘积，这正是操作子合成律的几何原型；计数给出的 $\mu^d$ 满足二次关系，就是「边界算子的像为零」。
- 原书刻意不用这套语言（p.7）：它把操作子的树形求和展开成分拆求和（式 (1.18)），以便逐项核对符号。

## 公式

$$\gamma:\mathcal O(k)\otimes\mathcal O(n_1)\otimes\cdots\otimes\mathcal O(n_k)\longrightarrow\mathcal O(n_1+\cdots+n_k)$$
$$\mathcal A_\infty(n)=C_*(K_n)\simeq\mathbb K\ (n\ge1),\qquad \mathcal A_\infty\longrightarrow\mathrm{Ass}\ \text{逐项拟同构}$$
$$\sum_{r+s+t=d}(-1)^{\star_r}\mu^{r+1+t}(a_d,\ldots,a_{r+s+1},\mu^s(a_{r+s},\ldots,a_{r+1}),a_r,\ldots,a_1)=0,\qquad \star_r=|a_1|+\cdots+|a_r|-r$$

## 定理与证明

### A∞ 操作子的代数满足 A∞ 关系

设 $\mathcal A_\infty$ 是结合操作子 $\mathrm{Ass}$ 的一个 dg 分辨（操作子拟同构 $\mathcal A_\infty\to\mathrm{Ass}$），$(A,\{\mu^d\}_{d\ge1})$ 是 $\mathcal A_\infty$-代数，其中 $\mu^d$ 是最高维胞腔 $[K_d]\in\mathcal A_\infty(d)$ 在结构映射 $\Phi:\mathcal A_\infty\to\mathcal E\mathrm{nd}_A$ 下的像。则 $\deg\mu^d=2-d$，且 $\{\mu^d\}$ 满足 A∞ 关系；反之，任一 A∞ 代数都来自某个 $\mathcal A_\infty$-代数结构。

（sketch；来源：原书 p.17 式 (1.18)、p.19 注 1.15）

1. 令 $\mu^d:=\Phi([K_d])$。$[K_d]$ 是 $\mathcal A_\infty(d)$ 的最高维胞腔，$\deg[K_d]=d-2$，而 $\Phi$ 是保次数的操作子态射，故 $\deg\mu^d=-(d-2)=2-d$。  
   为什么：$\mathcal A_\infty(d)$ 的最高维胞腔维数为 $d-2$；$\mathcal E\mathrm{nd}_A(d)=\mathrm{Hom}(A^{\otimes d},A)$ 按内次数计，$\Phi$ 的次数为 $0$。
2. $\Phi$ 是链映射，故 $\Phi(\partial[K_d])=\partial_{\mathcal E\mathrm{nd}}(\mu^d)=[d_A,\mu^d]$，即与 $d_A$ 的分次交换子。  
   为什么：操作子态射按定义与微分交换；自同态操作子的微分正是与 $d_A$ 的分次交换子。
3. 把 $\partial[K_d]$ 按操作子合成展开成 $\sum\pm[K_{r+1+t}]\circ([K_s]\otimes\mathrm{id}^{\otimes\cdots})$，再用 $\Phi$ 作用，得到 $\sum\pm\mu^{r+1+t}(\ldots,\mu^s(\ldots),\ldots)$，其中 $r+s+t=d$。  
   为什么：associahedron 的余维一面正是「一段连续输入先结合、其余保持」的树形复合，每个面对应一个三元组 $(r,s,t)$。
4. 比较步骤 2、3 的两式并把 $[d_A,\mu^d]$ 移到同一侧，即得 A∞ 关系。  
   为什么：移项后恰为 $\sum_{r+s+t=d}(-1)^{r+st}\mu^{r+1+t}(\ldots,\mu^s(\ldots),\ldots)=0$；符号来自 Koszul 规则与 $\mathcal A_\infty(d)$ 的 $S_d$-作用。

缺口：反向（由 A∞ 结构构造 $\mathcal A_\infty$-代数）需要把 $\mu^d$ 沿 associahedron 的胞腔分层、按树形复合扩张，并核对面映射的相容性；原书未展开这一步，本卡只证正向。正向中「逐维展开得到全部 $(r,s,t)$ 项」的符号核对依赖具体分辨模型（此处取 Stasheff 模型），不同模型的符号约定不同。

## 易错点

- $\mathcal O(n)$ 不是 $n$ 元运算本身，而是参数化它们的链复形；运算要经结构映射 $\mathcal O(n)\otimes A^{\otimes n}\to A$ 才落到 $A$ 上。
- 合成方向易写反：$\gamma$ 从 $\mathcal O(k)\otimes\prod_i\mathcal O(n_i)$ 到 $\mathcal O(\sum_i n_i)$（代入），不是反向的「拆分」。
- 非对称与对称约定不能混用：非对称版 $\mathrm{Ass}(n)=\mathbb K$、$\mathcal A_\infty(n)$ 可缩；对称版 $\mathrm{Ass}(n)=\mathbb K[S_n]$ 不可缩，分辨与符号都随之改变。
- 分辨只在操作子拟同构意义下唯一；把某个具体模型（associahedron、brace、树）的公式当成「定义」，换模型时必然出错。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§1 引言，p.7–7（原书 p.7）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§1(i)，p.17–17（原书 p.17）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§1 注 1.15，p.19–19（原书 p.19）

关联：`seidel/concept/a-infinity-algebra`、`seidel/concept/a-infinity-category`、`seidel/deriv/mu-d-grading`

来源说明：原书 p.7（明说不用 operad 语言）、p.17 式 (1.18)（树形递归）、p.19 注 1.15（操作子的余纤维性）；译者注 A01-05。外部核实：nLab “operad”（https://ncatlab.org/nlab/show/operad，2026-11-19 访问）称 operad 是「a bunch of abstract operations of arbitrarily many arguments … equipped with a notion of how to compose these」；nLab “A-infinity-algebra”（https://ncatlab.org/nlab/show/A-infinity-algebra）称 A∞ 操作子是 Ass 的分解、其代数正是 A∞ 代数。
