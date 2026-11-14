# 逐节抽查记录与通读评注

**方法**：以原 PDF 逐页渲染图（140 dpi）与文字层为底本，对每章抽取公式密集页，
将译本公式与原图**逐符号**对照（上下标、希腊字母、花体、粗体、括号、分式结构、求和/积分上下限）。
对可疑处用 4–5 倍放大裁切复核。以下记录抽查要点与结论。

---

## 一、逐章抽查

### 第 1 章 引言（PDF p.2–6）
- 作用量 $S:\mathcal{E}\to\mathbf{k}$、Yang–Mills $F=\dd A+\frac12[A,A]$、
  Chern–Simons $\int_M\operatorname{Tr}(\frac12A\wedge\dd A+\frac16A\wedge[A,A])$、路径积分
  $\langle O\rangle\propto\int_{\mathcal{E}}\ee^{\frac{\ii}{\hbar}S}O$：与 p.2–3 原图一致。
- TQM 例 1.2 的 $H_\bullet(\R-\{0\})=\Z_{\mathrm{left}}\oplus\Z_{\mathrm{right}}$、
  2d 手征 OPE $A(z)B(w)=\sum_n(A_{(n)}B)(w)/(z-w)^{n+1}$：与 p.5–6 原图一致。
- 结论：无公式转录错误；原文 "quanatum"、"an fundamental role" 两处笔误已在批注指出。

### 第 2 章 上同调与积分（PDF p.7–14）
- 抽查：上链复形与 $H^n(C^{*},d)$、de Rham 复形、Stokes 定理、Poincaré 引理、
  Cartan 公式 $\mathcal{L}_V=\dd\iota_V+\iota_V\dd$、内积与 Lie 导数的定义（p.9–13）；
  Gauss 定理（例 2.5，p.9）。
- 对照结果：分式、上下标（$d_{n-1},d_n,d_{n+1}$；$\Omega^{p}$）无误；
  原文 $d_nd_{n+1}=0$、$\partial_t^{*}(\alpha)$、$\iota_V(\dd x^{i_1})\wedge\dd x^{i_2}\cdots$
  等疑误按"照录+批注"处理（详见 `review_原文疑误.md` 第 2 章）。

### 第 3 章 经典场论（PDF p.15–22）
- 抽查：Euler–Lagrange 方程、Noether 定理的两种推导、Hamilton 方程
  $\dot q=\partial_pH$、$\dot p=-\partial_qH$、Maxwell 方程组的 2-形式写法
  $\dd F=0$、$\dd(*F)=*J$ 与分量形式（p.19–21）。
- 对照结果：$\dd F=0$、$\dd(*F)=*J$、$A=-\phi\,\dd t+\vec A\cdot\dd\vec x$ 均无误；
  p.19 的 $\partial_qH\dot q$ 漏写 $H$、p.20 例 3.11 的符号疑误已批注。

### 第 4 章 对称性的代数方面（PDF p.23–30）
- 抽查：Chevalley–Eilenberg 微分 $d_{\mathrm{CE}}c^\alpha=\frac12f^\alpha_{\beta\gamma}c^\beta c^\gamma$、
  $d_{\mathrm{CE}}^2=0$ 的证明（图证明）、DGLA 定义中的 Koszul 符号
  $[a,b]=-(-1)^{|a||b|}[b,a]$、$L_\infty$ 关系 $\sum\pm\ell_n=0$、$\deg\ell_n=2-n$。
- 对照结果：$\frac12$ 因子、$(-1)^{|a||b|}$ 符号、$W[n]$ 平移与 $\bigwedge^m(V[1])\cong\mathrm{Sym}^m(V)[m]$
  等均与原图一致；例 4.11 的指标问题已批注。

### 第 5 章 微扰展开（PDF p.31–47）
- 抽查：Gaussian 积分（含 $\det Q$、$(2\pi\hbar)^{n/2}$ 因子）、Wick 定理的框式公式
  $\langle x^{i_1}\cdots x^{i_{2m}}\rangle_x=\hbar^m\sum_{\sigma\in P(2m)}\prod(Q^{-1})^{\sigma(2j-1)\sigma(2j)}$、
  两点/四点函数、Feynman 图公理（顶点、边、$\omega_\Gamma$、$|\Aut(\Gamma)|$）、
  命题 5.10（图展开公式）、Green 函数 $G=\frac12\operatorname{sgn}(t_1-t_2)$、
  热核正则化 $P^L_\varepsilon=\int_\varepsilon^L Q^*\ee^{-t\Delta}\,\dd t$、抵消项 $\hbar\lambda^2\log\epsilon/\pi^2$。
- 对照结果：Wick 定理框式公式、$1/|\Aut(\Gamma)|$ 因子、$\Theta$ 图的赋值、单圈抵消项
  $\hbar\lambda^2\log\varepsilon/\pi^2$ 均确认；原文 $(A^{-1})^{ij}$、$2s/2m$、$\gamma/\Gamma$、
  $(2\pi t)^2$（疑应为 $(4\pi t)^2$）等已批注。
- 说明：例 5.2/5.3 的配对图嵌在公式行内，译本以"公式 + 图形裁切"并列呈现，数学内容不减。

### 第 6 章 BRST–BV 形式（PDF p.48–60）
- 抽查：Faddeev–Popov 切片、$\mathcal{O}(V/G)=\mathcal{O}(V)^G$、BRST 复形
  $(\wedge^{\bullet}\mathfrak{g}^\vee\otimes\mathcal{O}(V),d_{\mathrm{CE}})$、
  多向量场 $\mathrm{PV}(M)=\Gamma(M,\wedge^{\bullet}TM)$、$\Gamma:\mathrm{PV}^k\to\Omega^{n-k}$、
  BV 算子 $\Delta$、BV 括号 $\{a,b\}=\Delta(ab)-(\Delta a)b-(-1)^{|a|}a\Delta b$、
  CME/QME、形变–障碍（$\hbar^1$ 阶与 $\hbar^{>1}$ 阶、$H^1(\mathcal{O}_{loc},Q+\{I_0,-\})$）。
- 对照结果：$\Delta$ 的符号与归一化、$\{S_0,S_0\}=0\Leftrightarrow\delta^2=0$、
  变量对照表（$c^\alpha,x^i,\theta_i,e_\alpha$ 的次数 $1,0,-1,-2$）均确认；
  p.49、p.51、p.54、p.55 的疑误/记号不一致已批注。

### 第 7 章 BV 量子化的有效理论（PDF p.61–70）
- 抽查：$(-1)$-平移辛结构、Poisson 核 $K_0=\omega^{-1}$、$K_P=K_0+Q(P)$、
  $\Delta_P$、链同伦 $K_0=K_r+Q(P_r)$、Costello 有效解三条件（有效 QME、同伦 RG 流、
  渐近局部性）、热核 $K_r=\ee^{-r\Delta}$、$P_\varepsilon^L$、UV 有限理论。
- 对照结果：$K_0=K_r+QP_r$、$P_r=\int_0^rQ^*\ee^{-t\Delta}\dd t$、
  $\ee^{I[r']/\hbar}=\ee^{\hbar\partial_{P^{r'}_r}}\ee^{I[r]/\hbar}$ 等均逐符号核对无误；
  $\Delta_K$ 的 $\hat\alpha_i/\hat\alpha_j$ 笔误已批注。

### 第 8 章 因子化代数（PDF p.71–76）
- 抽查：预因子化代数的相容性图、$F(\varnothing)$ 交换性、$\mathcal{A}^{fact}(U)=\operatorname{colim}_{K}A^{\otimes K}$、
  因子化代数/余层条件、Čech 复形、Weiss 覆盖。
- 对照结果：相容性交换图、$\bigotimes_i F(U_i)\to F(V)$、$H^\bullet$ 与余层表述均无误；
  例 8.2 的 $a_k/a_\alpha$、命题 8.7 的 $\{x_1,\dots,x_k\}$ 等已批注。

### 第 9 章 拓扑量子力学（PDF p.77–92）
- 抽查：星积公理、Moyal 公式 $(f*g)(x)=f(x)\ee^{\frac{\mathrm{i}\hbar}{2}(\overleftarrow{\partial_x}\overrightarrow{\partial_p}-\overleftarrow{\partial_p}\overrightarrow{\partial_x})}g(x)$、
  Weyl 丛与 Fedosov 联络、Fedosov 方程、代数指标定理
  $\operatorname{Tr}(1)=\int_X\ee^{-\omega_\hbar/\hbar}\widehat A(X)$、
  万有迹映射 $\widetilde{\operatorname{Tr}}$、定理 9.20
  $[\widetilde{\operatorname{Tr}}(1)]=u^n\ee^{-R_3/(u\hbar)}\widehat A(\mathfrak{sp}_{2n})_u$、
  Gelfand–Fuks 下降映射 $\Omega^{\bullet}(X,\operatorname{Hom}_{\mathbb{K}}(CC^{per}_\bullet(\mathcal{W}(X)),\mathbb{K}))$。
- 对照结果：Moyal 指数的 $\frac{\mathrm{i}\hbar}{2}$、$\widehat A$ 类、$u^{-p/2}$ 幂次、
  $\omega_\hbar=-\omega_0+\hbar\omega_1+\cdots$ 均确认；$C^\infty(x)$、Moayl、$e^{\pm\omega_\hbar/\hbar}$
  符号差异等已批注。

### 第 10 章 二维手征量子场论（PDF p.93–101）
- 抽查：顶点代数公理（态–场对应、真空、OPE、平移）、$\beta\gamma$/$bc$ 系统、
  Dijkgraaf 手征形变 $S=\int_{E_\tau}\frac12\partial\phi\bar\partial\phi+\frac1{3!}\int_{E_\tau}\frac{\dd^2z}{\operatorname{Im}\tau}(\partial_z\phi)^3$、
  正则化积分与 UV 有限性、手征链复形、2d→1d 约化、定理 10.12（全纯反常方程）
  $\partial_Y\fint_{E^n_\tau}\Phi=\fint_{E^n_\tau}\partial_Y\Phi-\sum_{i<j}\fint_{E^{n-1}_\tau}\operatorname{Res}_{z_i=z_j}((z_i-z_j)\Phi)$。
- 对照结果：OPE 的 $(z-w)^{n+1}$ 约定、$\fint$ 记号、全纯反常方程的留数项均确认；
  真空公理/局域性下标/$\operatorname{Conf}_n$ 等 5 处疑误已批注。

### 参考文献（PDF p.101–103）
- 41 条逐条照录（作者、标题、期刊、卷期、页码、年份），编号 [1]–[41] 连续；
  原文缺连字符处（[21]、[34]、[35]、[25]）照录并加注。

---

## 二、通读理解与学术评注（"先读懂再评论"）

1. **全书的组织逻辑**：作者以"可观测量代数"为主线——第 1 章以因子化乘积点题，
   第 2 章补上同调/积分语言，第 3–5 章把经典场论、对称性代数化、微扰展开依次铺开，
   第 6–7 章进入 BV 形式与 Costello 同伦重整化，第 8 章把微扰 QFT 的代数结构抽象为
   因子化代数，第 9–10 章给出两个可完全算出的模型（拓扑量子力学、二维手征 QFT）。
   这条线索与 Costello–Gwilliam 学派的标准叙述一致，但本书更强调"先算例、后公理"的
   教学路径。

2. **BV 形式的核心机制**：第 6–7 章真正的技术枢纽是"用链同伦替换 Poisson 核"
   （$K_0=K_r+Q(P_r)$）。作者在 $(-1)$-平移辛几何的框架下把"量子化 = 构造 BV 算子 $\Delta$"
   解释为"将奇 Poisson 核正则化为光滑核"，这与传统 Faddeev–Popov/BV 的坐标表述互补；
   批注中特别提示 $\Delta$ 的符号与 $\Omega$ 的归一化是全篇最易错处。

3. **因子化代数的地位**：第 8 章把"开集上的可观测量如何相乘"公理化。作者只给出
   预因子化代数/因子化代数与层–余层对偶的骨架，未展开 Weiss 覆盖的细节；批注中补充了
   "余层条件 = 局部到整体的同伦粘合"这一要点，并指出与微扰重整化的接口（Costello 的
   有效作用量给出因子化代数）——这正是全书第 6–8 章串联起来的地方。

4. **两个可解模型的意义**：第 9 章的拓扑量子力学把 BV 量子化化为 Moyal 星积与
   Fedosov 联络，指标定理成为"配分函数的半经典精确计算"；第 10 章的二维手征 QFT 把
   顶点代数、正则化积分与全纯反常统一在 BV 框架下，定理 10.12 的全纯反常方程是
   第 9 章指标定理的"带参数版本"。这两章是全书理论框架的验证与落脚点。

5. **作为"速成讲义"的局限**：作者明言笔记"hastily prepared"，多处证明留作练习
   （如 $d_{\mathrm{CE}}^2=0$、命题 6.13、命题 10.9 等）。译本以批注指出省略论证的实质
   （Jacobi 恒等式、椭圆正则性、轨道–稳定子计数、Atiyah–Singer 指标定理、Borcherds
   顶点代数公理等），不擅自补写，以便教授按原书核对。
