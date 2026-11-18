# A_m 型奇点与 Milnor 纤维

> `seidel/concept/a-m-singularity` ｜ track C ｜ draft

**一句话**：由 $x_0^{m+1}+x_1^2+\cdots+x_n^2$ 的 Milnor 纤维得到的 Lefschetz 纤维化：消失圈按 $A_m$ 箭图相交，其 Fukaya 范畴由箭图代数与 length filtration 显式算出。

**自测**：$A_m$ 型奇点的 Milnor 纤维里，消失圈为什么排成一条 $A_m$ 箭图？

## 定义

取 $\Psi(x)=p(x_0)+x_1^2+\cdots+x_n^2:\C^{n+1}\to\C$，其中 $p$ 是次数 $m+1$ 的多项式且临界点非退化。对正则值 $w$，Milnor 纤维
$$X^n_m=\Psi^{-1}(w)$$
是仿射 $n$ 维光滑超曲面，典范丛平凡，配以 $\C^{n+1}$ 的平坦 Kähler 形式与二次体积形式。$p$ 一般时 $\Psi$ 是 Lefschetz 纤维化，其消失圈 $V_1,\dots,V_m$ 满足：对 $i\ne j$，
$$|V_i\cap V_j|=\begin{cases}1,&|i-j|=1,\\0,&|i-j|\ge2.\end{cases}$$
再取 $\varphi(x)=x_0$，则 $\varphi$ 的纤维 $\cong T^*S^{n-1}$，每个消失圈都是零截面，任意连接两临界值的路径都是匹配路径。

记号：$m\ge2$，$n\ge1$；$V_i\cong S^{n-1}$；$F^n_m\subset F(X^n_m)$ 是由 $V^{\#}_1,\dots,V^{\#}_m$ 生成的全 A∞ 子范畴。

## 要点

- 消失圈的相交数只由下标差决定：相邻相交一点、相隔至少 2 则不相交，正是 $A_m$ 箭图 $1\to2\to\cdots\to m$ 的边（式 20.1–20.2）。
- 路径代数模去三条关系 $(i+2,i+1,i)=0$、$(i-2,i-1,i)=0$、$(i,i+1,i)+(i,i-1,i)=0$ 得 $A^n_m$，且 $A^n_m\cong H(F^n_m)$；$m=2$ 时三条关系全落空，需补「长度三路径为零」，$A_2^n$ 为 6 维（注 A12-09）。
- $\tau=\tau_{V_1}\cdots\tau_{V_m}$ 是 $X$ 的辛自同构，即 $A_m$ 型超曲面奇点的单值；加权齐次性给出 $\tau^{2m+2}(L^{\#})\simeq S^{(4-2n)(m+1)-4}L^{\#}$，位移量恒非零，故 $V^{\#}_j$ split-generate：$\Pi\,\mathrm{Tw}\,F(X^n_m)\simeq\Pi\,\mathrm{Tw}\,F^n_m$（式 20.3）。
- $n\ge2$ 时用双纤维化 $(\Psi,\varphi)$：纤维是 $T^*S^{n-1}$，零截面的 A∞-代数在同调上是 $K e\oplus K f$（式 20.4），有向模型 $B^\to$ 为 $m+1$ 份 $S^{n-1}$（式 20.5），$C_j=\mathrm{Cone}(e_{j,j-1})$（20.6）。
- length filtration：给 $e_{ji}$ 长度 0、$f_{ji}$ 长度 2，引入降长度 1 的形式运算 $\Lambda$ 与齐次加法完备化 $\dagger^{\mathrm{ho}}B^\to$（20.7）；用命题 1.12 消 $\mu^1$ 且保持双分次后，$d>2$ 的 $\mu^d_A$ 必为零，故 $F$ 形式（formal）。
- 与 §20 的 length filtration 的关系：次数分次无法表达 $\mathrm{Cone}(e_{j,j-1})$ 的长度 $j$，必须再加 length grading 才能把 $C_j$ 写成齐次扭曲复形（注 A12-11）。

## 公式

$$\Psi(x)=p(x_0)+x_1^2+\cdots+x_n^2,\qquad X^n_m=\Psi^{-1}(w)$$
$$|V_i\cap V_j|=\begin{cases}1,&|i-j|=1,\\0,&|i-j|\ge2\end{cases}\quad(i\ne j)$$
$$A^n_m\cong H(F^n_m),\qquad \Pi\,\mathrm{Tw}\,F(X^n_m)\simeq\Pi\,\mathrm{Tw}\,F^n_m$$
$$\mu^2(e,e)=e,\quad\mu^2(e,f)=(-1)^{n-1}f,\quad\mu^2(f,e)=f$$
$$\tau^{2m+2}(L^{\#})\simeq S^{(4-2n)(m+1)-4}L^{\#}$$

## 定理与证明

### A_m 箭图与 H(F^n_m) 的计算

对一般的 $p$ 与合适的消失圈分次，$A^n_m\cong H(F^n_m)$，其中 $A^n_m$ 是 $A_m$ 箭图路径代数模去三条关系。

（sketch；来源：原书 p.304–305 §20a）

1. 由 (20.1)，$V_i,V_{i+1}$ 横截相交于唯一一点，$|i-j|\ge2$ 时 $V_i\cap V_j=\emptyset$。  
   为什么：消失圈的相交模式由 $A_m$ 型临界值的排列决定。
2. $HF(V_i,V_j)$ 由交点生成：相邻时两条（次数 0 与 $n$），对角时 $H^*(S^{n-1})$ 两条（$e,f$），其余为零。  
   为什么：横截交点的 Floer 复形以交点为生成元，次数由 Maslov 指标给出（注 A12-08）。
3. 复合由 $A_m$ 箭图的路径给出，三条关系来自 $\mu^2$ 的显式计算。  
   为什么：路径代数关系逐条对应 Floer 复形中的消去。
4. 故 $A^n_m\cong H(F^n_m)$。  
   为什么：生成元与关系逐一匹配。

缺口：原书只列结论并指向 [85]；这里给出生成元与关系对应的路线。

### 定理：n≥2 时 F^n_m 形式

设 $n\ge2$、$\mathrm{char}\,K\ne2$。则 $F^n_m$ 形式：存在保持双分次的 A∞-结构 $A$，使 $d>2$ 的 $\mu^d_A$ 全为零，且 $A$ 与 $F^n_m$ 拟同构。

（sketch；来源：原书 p.306–307 §20b）

1. 把 $B^\to$ 按长度分次：$e_{ji}$ 长度 0，$f_{ji}$ 长度 2，并引入降长度 1 的 $\Lambda$。  
   为什么：需要长度分次才能表达 $C_j$ 的长度 $j$。
2. 在齐次扭曲复形范畴 $\mathrm{Tw}^{\mathrm{ho}}B^\to$ 中，$C_j=\Lambda^j\mathrm{Cone}(e_{j,j-1})$ 是齐次对象，其全子范畴与 $F$ 拟同构（命题 18.21）。  
   为什么：命题 18.21 把 $C_j$ 识别为 $V_j$。
3. 用命题 1.12 消 $\mu^1$，操作保持双分次。  
   为什么：消 $\mu^1$ 的同伦只依赖分次，长度分次给出额外约束。
4. 双分次下 $d>2$ 的 $\mu^d_A$ 无可用次数，故全为零，$F$ 形式。  
   为什么：次数与长度同时守恒，高阶项无处可去。

缺口：原书用「inspection shows」跳过逐项检查；完整验证需展开 $\mu^d$ 的次数—长度双重守恒。

### 单值公式（式 20.3）

$\tau=\tau_{V_1}\cdots\tau_{V_m}$ 满足 $\tau^{2m+2}(L^{\#})\simeq S^{(4-2n)(m+1)-4}L^{\#}$，位移量非零；故 $V^{\#}_j$ split-generate $F(X^n_m)$。

（sketch；来源：原书 p.305 §20a）

1. 奇点加权齐次，$\tau$ 的幂可由 $\C^*$-作用显式算出。  
   为什么：加权齐次性把单值化为单项式变换。
2. 分次 Dehn 扭转的平移量按权重累加，得指数 $(4-2n)(m+1)-4$。  
   为什么：每次 $\tau_{V_j}$ 贡献固定平移，$2m+2$ 次后总指数可加。
3. 位移非零，故由命题 19.7 的同款论证，$V^{\#}_j$ split-generate。  
   为什么：非零分次平移排除真子范畴。

缺口：原书指向 [125, §4c] 的显式计算。

## 易错点

- 式 (20.1) 只对 $i\ne j$ 说相交数；$|V_i\cap V_i|$ 无意义，不要代入 $i=j$。
- $A_2^n$ 不是「三条关系自动成立」就完事：$m=2$ 时三条关系全落空，必须额外加「长度三路径为零」，否则维数不对（注 A12-09；$A_2^n$ 为 6 维）。
- 式 (20.4) 中 $\mu^2(e,f)=(-1)^{n-1}f$ 不是笔误；它等价于 $\mu^2(e,f)=(-1)^{|f|}\mu^2(f,e)$ 的符号约定（注 A12-10）。
- length grading 不是可有可无的装饰：只用次数分次无法把 $\mathrm{Cone}(e_{j,j-1})$ 的长度 $j$ 表达出来，也就无法做形式性论证（注 A12-11）。
- $n=1$（曲面情形）不在本卡「$n\ge2$ 形式性」的范围内：原书 §20c 另作处理，且要求 $\mathrm{char}\,K=0$。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§20a，p.304–305（原书 p.304 §20a）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§20b，p.305–307（原书 p.305 §20b）

关联：`seidel/concept/vanishing-cycle`、`seidel/concept/lefschetz-fibration`、`seidel/concept/thimble`、`seidel/concept/matching-cycle`、`seidel/deriv/directed-dg`、`seidel/deriv/mu-d-grading`

来源说明：据原书 §20a–20b（p.304–307）转述；译者注 A12-08、A12-09、A12-10、A12-11；外部参考 nLab「ADE singularity」与 Seidel《More about vanishing cycles and mutation》（arXiv:math/0010032）。
