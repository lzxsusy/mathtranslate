# A∞-范畴

> `functoriality/concept/a-infinity-category` ｜ track A ｜ draft

**一句话**：A∞-范畴是一族运算 μ_r（r≥1），μ₁ 是微分、μ₂ 只在 μ₃ 给出的同伦下结合，全部由 A∞ 方程统一控制；它是 dg-范畴的同伦松弛。

**自测**：A∞-范畴比 dg-范畴多了什么，为什么 Fukaya 范畴必须用 A∞ 而不是 dg？

## 定义

设 $\mathbf K$ 是域。$\mathbf K$-线性 $\Ainf$-范畴由对象集与分次 $\mathbf K$-向量空间 $\hom(X,Y)$ 组成，并配运算 $\mu_r:\CF^*(L^0,L^1)\otimes\cdots\otimes\CF^*(L^{r-1},L^r)\longrightarrow\CF^{*-2+r}(L^0,L^r)$（式(18)，这里写出 Fukaya 情形；一般情形把 $\CF^*$ 换成 $\hom$），满足 A∞ 方程（式(19)）：对每个 $r\ge1$，$\sum\pm\mu_{r-a+1}(x_1,\ldots,x_{i-1},\mu_a(x_i,\ldots,x_{i+a-1}),x_{i+a},\ldots,x_r)=0$。

记号：$\mu_r$ 的次数为 $2-r$：$\mu_1$ 次数 1（微分）、$\mu_2$ 次数 0（乘法）、$r\ge3$ 时为负；$\mu_1$ 也可归入目标范畴（链复形范畴）的结构。

## 要点

- $\mu_2$ 只在 $\mu_3$ 给出的链同伦下结合（式(21)），故 A∞-范畴是「带高阶同伦修正的 dg-范畴」；严格结合律被同伦意义下的结合律取代。
- 次数约定 $2-r$ 决定结构：$\mu_1$ 升次 1、$\mu_2$ 保次、高阶运算降次；这也是 $\mu_1$ 与其余运算「不同类」的原因。
- Fukaya 范畴的 $\mu_r$ 由 $(r+1)$-边形计数给出，高阶运算不可省：即使只关心 $\HF^*$，$\mu_3$ 等也会影响同调层面的乘法。
- 操作子表述：A∞-范畴等价于胞腔链操作子 $(C_*^{\mathrm{cell}}(K_r))_{r\ge1}$ 上的范畴（命题 thm:2.20），这解释了 A∞ 方程的来源。

## 公式

$$\mu_r:\CF^*(L^0,L^1)\otimes\cdots\otimes\CF^*(L^{r-1},L^r)\longrightarrow\CF^{*-2+r}(L^0,L^r),$$
$$\sum_{\substack{1\le a\le r\\1\le i\le r-a+1}}\pm\mu_{r-a+1} \bigl(x_1,\ldots,x_{i-1},\mu_a(x_i,\ldots,x_{i+a-1}),x_{i+a},\ldots,x_r\bigr)=0 \quad\forall r\ge1.$$
$$\begin{aligned} &\mu_2(\mu_2(x,y),z)-\mu_2(x,\mu_2(y,z))\\ &\quad=\pm\mu_3(\mu_1(x),y,z)\pm\mu_3(x,\mu_1(y),z)\\ &\qquad\quad\pm\mu_3(x,y,\mu_1(z))\pm\mu_1(\mu_3(x,y,z)). \end{aligned}$$

## 定理与证明

### 前几个 A∞ 方程的含义

r=1 的方程是 μ₁²=0；r=2 的方程说明 μ₂ 关于 μ₁ 是链映射；r=3 的方程说明结合律的失败由 μ₃ 控制（式(21)）。

（sketch；来源：原书 p.10 §2.2）

1. 在式(19) 中取 $r=1$：求和只剩 $\mu_1(\mu_1(x_1))=0$。  
   为什么：$a$ 只能取 1、$i$ 只能取 1，故得微分条件。
2. 取 $r=2$：得 $\mu_1\mu_2\pm\mu_2(\mu_1\otimes\id)\pm\mu_2(\id\otimes\mu_1)=0$，即 $\mu_2$ 是链映射。  
   为什么：这正是「乘法与微分相容」的链级表述。
3. 取 $r=3$：得结合律的差等于 $\mu_1\mu_3$ 加 $\mu_3$ 与 $\mu_1$ 的复合项，即式(21)。  
   为什么：结合律的失败被 $\mu_3$ 精确补偿；$\mu_3$ 不存在时退化为 dg-范畴。

缺口：原文用文字解释前几个方程（p.10），未逐项验证符号与次数；本卡补出对应关系，符号约定以式(19) 为准。

### A∞-范畴是胞腔链操作子上的范畴（命题 thm:2.20）

K-线性 A∞-范畴与操作子 C_*^cell(K)（由结合多面体的胞腔链组成）上的范畴等价。

（sketch；来源：原书 p.13 §2.3）

1. 把 $\mu_1$ 取为态射复形上的微分，$r\ge2$ 的 $\mu_r$ 取为把基本类 $[K_r]$ 代入操作子复合所得的结果。  
   为什么：操作子上的范畴只给抽象复合，代入基本类才得到具体的 $r$ 元运算。
2. 利用 $\varphi_r$ 是链映射（式(27)）与结合多面体 $K_r$ 的递归结构，把 $\partial[K_r]$ 的边界分解翻译成插入求和，整理即得 A∞ 方程（式(29)）。  
   为什么：A∞ 方程就是操作子相容性的展开，不需要额外验证。

缺口：原文在 §2.3 给出逆向方向的完整构造与验证（命题 thm:2.20 的证明）；本卡只重述两个关键步骤，正向方向从略。

## 易错点

- 把 A∞-范畴当成 dg-范畴：忽略 $\\mu_3$ 会丢掉结合律的同伦修正，同调层面的乘法也可能算错。
- 次数记错：$\\mu_r$ 的次数是 $2-r$，不是 $1-r$ 也不是 $0$；这直接决定分次平移与符号。
- 以为 A∞ 方程是「额外要求」：它等价于操作子相容性（§2.3），是边界配边为零的代数翻译，不是人为公理。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§2.2，p.9–10（原书 p.9–10 §2.2）

关联：`functoriality/concept/fukaya-category`、`functoriality/concept/operad`、`functoriality/deriv/fukaya-ainf-structure`

来源说明：原书 p.9–10 §2.2（A∞-范畴定义、式(18)、(19)、(21) 与前几个方程的解释）；公式逐字取自中译本 chapter2.tex 的 eq:18、eq:19、eq:21。
