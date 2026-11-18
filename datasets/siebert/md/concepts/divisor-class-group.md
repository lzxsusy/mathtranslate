# 除子类群、Cartier 除子与 Picard 群

> `siebert/concept/divisor-class-group` ｜ track D ｜ draft

**一句话**：环面簇的 $\operatorname{Pic}$ 是分段线性函数模整体线性函数：$\varphi\in\mathrm{PL}(\Sigma)$ 给出 $T$ 不变 Cartier 除子 $\sum\varphi(v_i)D_i$，而 $\operatorname{Cl}$ 是 Weil 除子模有理等价。

**自测**：为什么环面簇的 Cartier 除子全都能写成 $\sum\varphi(v_i)D_i$，而 $\operatorname{Pic}$ 恰好是分段线性函数模掉整体线性函数？

## 定义

Cartier 除子群 $\operatorname{CaDiv}X=\Gamma(X,\mathcal K^\times/\OO_X^\times)$，在整概形上可用局部数据 $\{(U_i,f_i)\}$（要求 $f_i/f_j\in\OO_X^\times(U_i\cap U_j)$）表示，且 $\operatorname{CaDiv}X\hookrightarrow\operatorname{Div}X$。$T$ 不变 Cartier 除子对应分段线性函数：$\mathrm{PL}(\Sigma)$ 是 $|\Sigma|$ 上连续、在每个锥 $\sigma\in\Sigma$ 上等于某个 $m\in M$ 给出的线性函数的实值函数全体，映射 $\varphi\mapsto\sum_i\varphi(v_i)D_i$ 给出 $T$ 不变 Cartier 除子。

记号：$\mathrm{PL}(\Sigma)$：分段线性函数群；$\operatorname{CaDiv}^T(X_\Sigma)$：$T$ 不变 Cartier 除子；$\operatorname{Cl}X$：除子类群；$\operatorname{Pic}X$：可逆层同构类群。

## 要点

- Cartier 与 Weil 的差别在环面情形很具体（引理 4.16）：仿射环面簇 $\Spec k[\sigma^\vee\cap M]$ 上一个 $T$ 不变 Weil 除子是 Cartier 的，当且仅当它是某个 $\operatorname{div}(\chi^m)$，即主除子。所以仿射情形没有非主的不变 Cartier 除子。
- 整体情形（命题 4.17）：$\operatorname{CaDiv}^T(X_\Sigma)\simeq\mathrm{PL}(\Sigma)$。直觉是每个仿射图 $U_\sigma$ 上的除子由 $m_\sigma\in M$ 给出，相容性 $m_\sigma-m_{\sigma'}\in(\sigma\cap\sigma')^\perp$ 恰好说明这些 $m_\sigma$ 拼成一个分段线性函数。
- Picard 群（命题 4.18）：$\operatorname{Pic}(X_\Sigma)=\mathrm{PL}(\Sigma)/M=\operatorname{CaCl}X$，模掉的是整体线性函数 $\varphi\mapsto\langle m,\cdot\rangle$，因为它给出主除子 $\operatorname{div}(\chi^m)$。
- $\operatorname{Pic}(X_\Sigma)$ 离散（推论 4.19）；若 $\Sigma$ 含满维锥则无挠；此时若 $\varphi$ 来自 $M_\RR$ 中某个向量的全局线性函数，它必定来自 $M$。
- 丰的判别（命题 4.20）：有限扇、支撑凸、极大锥满维时，$\OO_X(D)$ 丰当且仅当 $\varphi$ 严格凸，即每个余维一锥处的折角 $K_\rho(\varphi)>0$。

## 公式

$\operatorname{CaDiv}^T(X_\Sigma)\simeq\mathrm{PL}(\Sigma),\qquad \varphi\longmapsto\sum_i\varphi(v_i)D_i$
$\operatorname{Pic}(X_\Sigma)=\mathrm{PL}(\Sigma)/M=\operatorname{CaCl}X$
$K_\rho(\varphi)=\varphi|_{\sigma_1}(\check d_\rho)-\varphi|_{\sigma_2}(\check d_\rho)\in\ZZ,\qquad \OO_X(D)\ \text{丰}\iff\forall\rho:\ K_\rho(\varphi)>0$

## 定理与证明

### 命题 4.17：分段线性函数与不变 Cartier 除子

映射 $\varphi\mapsto\sum_i\varphi(v_i)D_i$ 给出群同构 $\operatorname{CaDiv}^T(X_\Sigma)\simeq\mathrm{PL}(\Sigma)$。

（complete；来源：原书 p.79）

1. 取 $\varphi\in\mathrm{PL}(\Sigma)$，在每个极大锥 $\sigma$ 上有 $m_\sigma\in M$ 使 $\varphi|_\sigma=\langle m_\sigma,\cdot\rangle$ 为线性函数。  
   为什么：分段线性的定义保证每个锥上一片线性，且相邻锥上两片在公共面上取值一致。
2. 在仿射图 $U_\sigma$ 上，$\varphi$ 给出的除子是 $\operatorname{div}(\chi^{m_\sigma})$；在交 $U_\sigma\cap U_{\sigma'}=U_{\sigma\cap\sigma'}$ 上两者相差 $\chi^{m_\sigma-m_{\sigma'}}$，其在公共面外为可逆函数。  
   为什么：相容性条件 $m_\sigma-m_{\sigma'}\in(\sigma\cap\sigma')^\perp$ 保证差的因子在交上属于 $\OO^\times$，故这些局部除子拼成一个 Cartier 除子。
3. 反之由 Cartier 数据 $\{(U_\sigma,f_\sigma)\}$，在 $U_\sigma$ 上 $\operatorname{div}(f_\sigma)$ 只能由某个 $m_\sigma$ 给出（引理 4.16），相容性给出分段线性函数，两个构造互逆。  
   为什么：仿射图上不变 Cartier 除子都是主除子，所以局部数据完全由这些 $m_\sigma$ 决定。

### 命题 4.18：Picard 群

$\operatorname{Pic}(X_\Sigma)=\mathrm{PL}(\Sigma)/M=\operatorname{CaCl}X$。

（sketch；来源：原书 p.79）

1. 由命题 4.17，$T$ 不变 Cartier 除子对应 $\mathrm{PL}(\Sigma)$；模去主除子后得到 $\operatorname{CaCl}X$。  
   为什么：主除子中 $T$ 不变的那些恰是 $\operatorname{div}(\chi^m)$，对应的分段线性函数是整体线性函数 $\langle m,\cdot\rangle$。
2. 环面簇上每个可逆层都可由 $T$ 不变 Cartier 除子代表，故 $\operatorname{Pic}X=\operatorname{CaCl}X$。  
   为什么：环面作用把任意除子平均成 $T$ 不变的，等价类不变。
3. 于是 $\operatorname{Pic}(X_\Sigma)=\mathrm{PL}(\Sigma)/M$。  
   为什么：商掉的是 $m\mapsto\langle m,\cdot\rangle$ 的像，即整体线性函数。

缺口：第 2 步「每个可逆层都可由 $T$ 不变 Cartier 除子代表」在讲义里是一句话带过，未用群作用取平均或等变化函子论证。

### 命题 4.20：丰环面除子的分段线性判别

设 $\Sigma$ 是有限扇、支撑凸、极大锥均满维，$\varphi\in\mathrm{PL}(\Sigma)$，$D=\sum\varphi(v_i)D_i$。则 $\OO_X(D)$ 丰当且仅当 $\varphi$ 严格凸，即对每个 $\rho\in\Sigma[d-1]$ 有 $K_\rho(\varphi)>0$。

（sketch；来源：原书 p.80）

1. 「$\Leftarrow$」：$\varphi$ 严格凸时取 Newton 多胞体 $\Xi$，则 $X\simeq X(\Sigma_\Xi)\simeq\Proj k[C(\Xi)\cap(M\oplus\ZZ)]$ 且 $\OO_X(D)=\OO_X(1)$，故丰（事实上甚丰）。  
   为什么：把除子实现为射影坐标环的 $\OO(1)$，丰性立刻成立。
2. 「$\Rightarrow$」：对余维一锥 $\rho$，限制 $\OO_X(D)|_{X(\Sigma_\rho)}$ 的次数恰是折角 $K_\rho(\varphi)$（事实 8）。  
   为什么：曲线 $X(\Sigma_\rho)$ 上丰层次数必正，故 $K_\rho(\varphi)>0$。
3. 由事实 7，$\forall\rho:\ K_\rho(\varphi)>0$ 等价于 $\varphi$ 严格凸。  
   为什么：折角符号逐片检查，正好刻画严格凸性。

缺口：事实 7、事实 8 在讲义中只陈述未证（折角与限制次数相等），故整体标 sketch。

## 易错点

- $\operatorname{Cl}X$ 与 $\operatorname{Pic}X$ 一般不相等：环面簇上 $\operatorname{Pic}\subset\operatorname{Cl}$，等式成立需要每个 $T$ 不变 Weil 除子都 Cartier，例如 $\PP^n$；带奇点的仿射环面簇会出现 $\operatorname{Pic}=0$ 而 $\operatorname{Cl}\ne0$。
- $\mathrm{PL}(\Sigma)$ 里的「分段线性」要求函数在每个锥上由 $M$ 中向量给出，而不是 $M_\RR$：系数必须在整格上，否则 $\sum\varphi(v_i)D_i$ 不是整除子。
- 命题 4.20 要求扇有限、支撑凸、极大锥满维，缺一不可：无穷扇没有 Newton 多胞体，非凸支撑的对偶也接不上。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §23 Cartier 除子，p.79–79（原书 p.79）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §24 Picard 群，p.79–79（原书 p.79）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §25 丰环面除子，p.80–80（原书 p.80）

关联：`siebert/concept/weil-divisor-toric`、`siebert/concept/fan`、`siebert/correction/very-ample-term`、`siebert/deriv/polytope-to-fan`

来源说明：原书 p.79–80（(4.119)–(4.121)、引理 4.16、命题 4.17、命题 4.18、推论 4.19、命题 4.20）。核过 Stacks tag/01PR（丰层的定义）、0BE0（Cl 的正合列）、0C4S（$\OO_S(D)$ 与 Picard 群乘法）、0EBK（秩 1 自反层与 Cl 的关系）；nLab「ample line bundle」用于核对「丰」的含义。
