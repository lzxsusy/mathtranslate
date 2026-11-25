# 配对的留数公式

> `grassmann/concept/residue-formula-for-pairings` · 轨道 4 · 奇异模空间的相交配对 · 状态 draft

> **先自测**：留数映射为什么不是亚纯函数在 0 处的通常留数，而要绕道 Fourier 变换来定义？

## 一句话

把模空间上的相交配对写成不动点集上的留数之和：留数是亚纯函数 Fourier 变换在零点的值，周期性再把求和压成 1/(1−e^X)。

## 定义

设 $T$ 是紧 Lie 群，$\beta_j\in\mathfrak{t}^*$ 是它的权，$\bar\beta=\{\beta_1,\dots,\beta_n\}$，定义 $\mathfrak{t}$ 上的亚纯函数
$$h_{\bar\beta}(X)=\frac{1}{\prod_j\beta_j(X)}.$$
**留数映射** $\mathrm{Res}$ 定义为这类函数的 Fourier 变换在 $\xi=0$ 处的值：$\mathrm{Res}(f)=(\mathcal{F}f)(0)$，其中 $\mathcal{F}h_{\bar\beta}$ 是 $\mathbb{C}^n$ 上的 Lebesgue 测度在 $(y_1,\dots,y_n)\mapsto\sum_j\beta_jy_j$ 下到 $\mathfrak{t}^*$ 的前推。取 $\tilde\mu$ 的小正则值 $\epsilon$，则
$$\frac{1}{n!}\int_{\mu^{-1}(\epsilon)^s/T}\kappa_M^{T,\epsilon}(\eta e^{\bar\omega}\mathcal{D})=\mathrm{Res}\Big(\sum_F e^{\langle\mu(F),X\rangle}\int_F\frac{\eta e^{\omega}\mathcal{D}^2}{e_F}\Big),$$
其中 $F$ 跑遍 $T$-不动点集的连通分支，$e_F$ 是 $F$ 的法丛关于变量 $X$ 的等变 Euler 类。

**记号约定**：$X\in\mathfrak{t}$；$\mu(F)$ 是不动点分支的矩映射值；$e_F=e_T(N_F)$；$\mathrm{Res}$ 靠极化定符号：选锥 $\Lambda\subset\mathfrak{t}$ 使所有 $\beta_j(X)>0$（$X\in\Lambda$）后取定。

## 要点（为什么需要它）

- 留数不是通常留数：$h_{\bar\beta}$ 在 $0$ 处是极点，通常留数或为零或发散；$\mathrm{Res}$ 是 Guillemin–Lerman–Sternberg 用 Fourier 变换的赋值，可以非零。
- $S^2$ 例子把公式兑现：两个不动点 $\mu(F_\pm)=\pm1$、$e_{F_\pm}=\pm X$，求和给 $(e^X-e^{-X})/X=2\sinh X/X$，其 Fourier 变换是 $[-1,1]$ 的特征函数，正是 $S^2$ 在矩映射下的像。
- 定理 6.1 是本公式的「差分」形式：两个正则值处的配对之差等于夹在中间的不动点的留数之和，穿墙项 $B$ 正是这样算的。
- 周期性（$\mu^{-1}(a)\cong\mu^{-1}(a+1)$，对 $K=SU(n)$ 在 $M^{\mathrm{ext}}$ 上成立）把定理 6.1 的求和写成显式的 $\sum_F\mathrm{Res}\,e^{\mu(F)X}\eta(X)/(e_F(X)(1-e^X))$。
- 公式里的 $\mathcal{D}^2$ 与左端的 $\mathcal{D}^1$ 不匹配，正文未交代来源（批注 6），这是本章最需要外部核对的一处。

## 关键公式

$$
h_{\bar\beta}(X)=\frac{1}{\prod_j\beta_j(X)},\qquad \mathrm{Res}(f)=(\mathcal{F}f)(0)
$$

$$
\frac{1}{n!}\int_{\mu^{-1}(\epsilon)^s/T}\kappa_M^{T,\epsilon}(\eta e^{\bar\omega}\mathcal{D})=\mathrm{Res}\Big(\sum_F e^{\langle\mu(F),X\rangle}\int_F\frac{\eta e^{\omega}\mathcal{D}^2}{e_F}\Big)
$$

$$
h(X)=\frac{e^X-e^{-X}}{X}=2\frac{\sinh X}{X}\quad (S^2\ \text{例})
$$

## 定理与证明（或缺口）

### Guillemin–Kalkman；Martin：两个正则值处的配对之差（定理 6.1）

若 $a,b$ 是圆周作用矩映射 $\mu$ 的正则值且 $a<b$，则
$$\int_{\mu^{-1}(a)/T}\kappa_M^{T,a}(\eta e^{\bar\omega})-\int_{\mu^{-1}(b)/T}\kappa_M^{T,b}(\eta e^{\bar\omega})=\sum_{F\mid a<\mu(F)<b}\mathrm{Res}\int_F\frac{e^{\mu(F)X}\eta e^{\omega}}{e_F(X)},$$
其中 $F$ 跑遍圆周作用不动点集的连通分支。

**证明状态：只引出处，原书不重证**


出处：中译 p.79（§6 定理 6.1，引 Guillemin–Kalkman, J. Reine Angew. Math. 470 (1996)；Martin）

## 易错点

- 把 $\mathrm{Res}$ 当成 $\mathrm{Res}_{X=0}$ 的通常留数：$h_{\bar\beta}$ 在 $0$ 处是极点，通常留数给不出 $\int_{S^2}e^{\omega+\mu X}$ 这种光滑函数的值，必须走 Fourier 变换。
- 忘了极化定符号：不选锥 $\Lambda$ 使 $\beta_j(X)>0$，$\mathrm{Res}$ 会整体差一个符号，$S^2$ 例子里 $h_+-h_-$ 就会变成 $-\chi_{[-1,1]}$。
- 把 $e_F$ 写成普通 Euler 类：必须是等变的 $e_T(N_F)=c_1(N_F)+\mathrm{wt}$，丢掉权就丢掉全部 $Y$ 依赖，留数算不出来。

## 相关卡

- [Kirwan 映射与正根类](../concepts/kirwan-map-and-class-d.md)
- [M(2,0) 的穿墙项](../examples/wall-crossing-term-m20.md)
- [α-稳定凝聚系](../concepts/alpha-stable-coherent-system.md)

## 出处

- ch4 §6 式 (10) 与定理 6.1；中译 p.79（英文 PDF p.85），源码 `chapters/ch04.tex:266`
