# 第 9 章 通读笔记：Cogdell, *Analytic Theory of L-Functions for $\mathrm{GL}_n$*

底本 pp. 197–228（PDF 200–231），页图 `work/pages/ch09/p0200.png`–`p0231.png`（mutool 按真实 PDF 页号命名）。本章另有长文版本 Cogdell [1]，正文自述为「提要」（synopsis）。

## 三句话主旨

1. $\mathrm{GL}_n$ 的 $L$ 函数有两条进路：一是 Hecke 式的积分表示（把 $L$ 函数写成尖点形式与 Whittaker 函数/Eisenstein 级数的积分），二是 Eisenstein 级数 Fourier 系数的解析（Langlands–Shahidi）。本章只走第一条，并用它把整体 $L$ 函数的解析性质归约到局部因子的解析性质。
2. 技术枢纽有三件：尖点形式的 Fourier 展开（定理 1.1）、Whittaker 模型的唯一性（定理 1.2，局部与整体）、以及把 $\mathrm{GL}_n$ 的尖点形式「投影」到棒状子群 $\mathrm{P}_{m+1}$ 上以制造可展开的积分（$\mathbb{P}^n_m$）。
3. 局部侧用分数理想 $\mathcal{I}(\pi,\pi')\subset\mathbb{C}(q^{-s})$ 定义 $L(s,\pi\times\pi')$，用 $\gamma$ 因子与 $\varepsilon$ 因子陈述局部函数方程；整体侧由此得到亚纯延拓、竖直带有界、函数方程与极点位置，最后以逆定理（Hecke 判据的 $\mathrm{GL}_n$ 版本）收束：$L(s,\Pi\times\pi')$ 对足够多的扭 $\pi'$「好」，就迫使 $\Pi$ 拟自守。

## 逐节内容地图

- **引言（pp. 197–198）**：Hecke 学派 → Jacquet–Langlands $\mathrm{GL}_2$ → JPSS 与 Jacquet–Shalika 的 $\mathrm{GL}_n$ 长系列；逆定理的谱系（$\mathrm{GL}_2$ Jacquet–Langlands，$\mathrm{GL}_3$ JPSS，$\mathrm{GL}_n$ CKPS [4]）；Godement–Jacquet 的主 $L$ 函数（[15, 20]，本章不取）；Eisenstein 进路（Langlands [29]，Shahidi [35–41]，[38] 证两进路同归）。

- **§1 Fourier 展开（pp. 198–202）**
  - §1.1：$f(\tau+1)=f(\tau)$ 给 $f(\tau)=\sum_{n\ge1}a_ne^{2\pi in\tau}$；$\mathrm{GL}_2(\mathbb{A})$ 上 $W_{\varphi,\psi}(g)=\int_{k\backslash\mathbb{A}}\varphi\bigl(\binom{1\ x}{0\ 1}g\bigr)\psi^{-1}(x)\,dx$，$\varphi(g)=\sum_\psi W_{\varphi,\psi}(g)$；以 $\psi_\gamma(x)=\psi(\gamma x)$ 重排得 $\varphi(g)=W_{\varphi,\psi_0}(g)+\sum_{\gamma\in k^\times}W_\varphi\bigl(\mathrm{diag}(\gamma,1)g\bigr)$，尖点性杀掉 $\psi_0$ 项。
  - $\mathrm{GL}_n$ 的 $\mathrm{N}_n$ 非交换，Piatetski-Shapiro [31] 与 Shalika [42] 各自解决：$\psi(n)=\psi(x_{1,2}+\cdots+x_{n-1,n})$，$W_\varphi(g)=\int_{\mathrm{N}_n(k)\backslash\mathrm{N}_n(\mathbb{A})}\varphi(ng)\psi^{-1}(n)\,dn$（紧支集上绝对一致收敛）。
  - **定理 1.1**（Fourier 展开）：$\varphi(g)=\sum_{\gamma\in\mathrm{N}_{n-1}(k)\backslash\mathrm{GL}_{n-1}(k)}W_\varphi\bigl(\binom{\gamma\ }{0\ 1}g\bigr)$，绝对收敛且在紧集上一致。
  - 证明用**棒状子群** $\mathrm{P}_n=\mathrm{GL}_{n-1}\ltimes \mathrm{Y}_n$（$\mathrm{Y}_n=\{(\begin{smallmatrix}I_{n-1}&y\\0&1\end{smallmatrix})\}\cong k^{n-1}$）：先限制到 $\mathrm{P}_n$ 上对 $n$ 归纳，再把 $\varphi_g(p)=\varphi(pg)$ 当作 $\mathrm{P}_n(\mathbb{A})$ 上的紧族。
  - §1.2：$\mathcal{W}(\pi,\psi)=\{W_\varphi\}$，$\varphi\mapsto W_\varphi$ 缠结 $V_\pi$ 与右平移表示；局部情形同理定义 $\mathrm{Ind}_{\mathrm{N}_n}^{\mathrm{GL}_n}(\psi_v)$；Whittaker 泛函 $\Lambda_v$ 与模型相互转换（Frobenius 互反：$\mathrm{Hom}_{\mathrm{N}_n}\cong\mathrm{Hom}_{\mathrm{GL}_n}$）。
  - **定理 1.2**（Gelfand–Kazhdan [14] 非阿基米德；Shalika [42] 阿基米德）：$\psi_v$-Whittaker 泛函空间至多一维，故模型若存在则唯一。有模型者称**一般**（generic，非退化）；$\pi_v$ 一般 $\iff$ 对偶 $\widetilde{\pi}_v\cong\pi^\iota$ 一般，$\mathcal{W}(\widetilde{\pi},\psi^{-1})=\{\widetilde{W}(g)=W(w_n{}^tg^{-1})\}$。
  - 整体：$\pi=\otimes'\pi_v$ 给连续嵌入 $V_{\pi_v}\hookrightarrow V_\pi$，$\Lambda=\otimes'\Lambda_v$，$W_\xi(g)=\prod_vW_{\xi_v}(g_v)$；$\Lambda(\varphi)=W_\varphi(e)$，故 $\varphi$ 由 $W_\varphi$ 完全决定 → **重数一定理**（Piatetski-Shapiro [32]、Shalika [42]）。

- **§2 Euler 积分表示（pp. 202–211）**
  - 引子：$L(s,f)=\sum a_nn^{-s}$，$\Lambda(s,f)=(2\pi)^{-s}\Gamma(s)L(s,f)=\int_0^\infty f(iy)y^sd^\times y$，$\tau\mapsto-1/\tau$ 给 $\Lambda(s,f)=(-1)^{k/2}\Lambda(k-s,f)$，Hecke 本征函数给 $L(s,f)=\prod_p(1-a_pp^{-s}+p^{k-1-2s})^{-1}$。需要的不止 $L(s,\pi)$，还有扭 $L(s,\pi\times\pi')$（$\pi'$ 属 $\mathrm{GL}_m$，$m<n$）。
  - §2.1（$\mathrm{GL}_2$）：$I(s;\varphi,\chi)=\int_{k^\times\backslash\mathbb{A}^\times}\varphi\bigl(\binom{a\ }{1}\bigr)\chi(a)|a|^{s-1/2}d^\times a$，整函数、竖带有界，$\widetilde{\varphi}(g)=\varphi({}^tg^{-1})$ 给 $I(s;\varphi,\chi)=I(1-s;\widetilde{\varphi},\chi^{-1})$；展开后 $I=\int_{\mathbb{A}^\times}W_\varphi(\mathrm{diag}(a,1))\chi(a)|a|^{s-1/2}d^\times a$，Euler 化为 $\Psi_v(s;W_{\varphi_v},\chi_v)$。
  - §2.2（$\mathrm{GL}_n\times\mathrm{GL}_m$，$m<n$）：朴素的 $\int_{\mathrm{GL}_m(k)\backslash\mathrm{GL}_m(\mathbb{A})}\varphi\binom{h\ }{I_{n-m}}\varphi'(h)|\det h|^{s-(n-m)/2}dh$ 只有 $m=n-1$ 时 Euler 化，因为「把 $\varphi$ 限制到 $\mathrm{GL}_m$ 太粗暴」。补救：$\mathrm{Y}_{n,m}$（分拆 $(m+1,1,\dots,1)$ 的单幂根），**投影算子**
    $\mathbb{P}^n_m\varphi(p)=|\det p|^{-(n-m-1)/2}\int_{\mathrm{Y}_{n,m}(k)\backslash\mathrm{Y}_{n,m}(\mathbb{A})}\varphi\bigl(y\binom{p\ }{I_{n-m}}\bigr)\psi^{-1}(y)dy$，
    把 $\varphi$ 送到 $\mathrm{P}_{m+1}(\mathbb{A})$ 上的尖点函数；其 Fourier 展开（对 $\gamma\in\mathrm{N}_m(k)\backslash\mathrm{GL}_m(k)$ 求和）使 $I(s;\varphi,\varphi')$ 得以展开为 $\int_{\mathrm{N}_m(\mathbb{A})\backslash\mathrm{GL}_m(\mathbb{A})}W_\varphi\binom{h\ }{I_{n-m}}W'_{\varphi'}(h)|\det h|^{s-(n-m)/2}dh$。
  - **定理 2.1**：$I(s;\varphi,\varphi')$ 整、竖带有界，函数方程 $I(s;\varphi,\varphi')=\widetilde{I}(1-s;\widetilde{\varphi},\widetilde{\varphi}')$，且 Euler 化 $I=\prod_v\Psi_v$。函数方程右端的展开引入 $w_{n,m}=\mathrm{diag}(I_m,w_{n-m})$、右平移 $\rho$ 与 $\widetilde{\Psi}(s;W,W')=\Psi_{n-m-1}$，故右端仍是 Euler 乘积。
  - §2.3（$\mathrm{GL}_n\times\mathrm{GL}_n$）：Rankin [33]、Selberg [34]；$\int\varphi\overline{\varphi'}|\det g|^s$ 只是 $L^2$ 内积，须引入第三函数——Eisenstein 级数。$F(g,\Phi;s,\eta)=|\det g|^s\int_{\mathbb{A}^\times}\Phi(ae_ng)|a|^{ns}\eta(a)d^\times a$ 是 $\mathrm{P}'_n=\mathrm{Z}_n\mathrm{P}_n$ 上 $\delta_{P'_n}^{s-1/2}\eta$ 的平滑截面；$E(g,\Phi;s,\eta)=\sum_{\gamma\in\mathrm{P}'_n(k)\backslash\mathrm{GL}_n(k)}F(\gamma g,\Phi;s,\eta)$（$\mathrm{Re}(s)>1$ 绝对收敛）。
  - Theta 级数 $\Theta_\Phi(a,g)=\sum_{\xi\in k^n}\Phi(a\xi g)$，$\Theta'_\Phi=\Theta_\Phi-\Phi(0)$；Poisson 求和给 $E$ 的解析性质：$\mathbb{C}$ 上亚纯、仅 $\eta$ 非分歧且 $\eta(a)=|a|^{in\sigma}$ 时在 $s=-i\sigma,1-i\sigma$ 有单极点、竖带有界、$E(g,\Phi;s,\eta)=E(g^\iota,\widehat{\Phi};1-s,\eta^{-1})$。
  - $I(s;\varphi,\varphi',\Phi)=\int_{\mathrm{Z}_n(\mathbb{A})\mathrm{GL}_n(k)\backslash\mathrm{GL}_n(\mathbb{A})}\varphi\varphi'E\,dg$，函数方程 $I(s;\varphi,\varphi',\Phi)=I(1-s;\widetilde{\varphi},\widetilde{\varphi}',\widehat{\Phi})$；留数给 $\mathrm{GL}_n(\mathbb{A})$-不变配对，非零仅当 $\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}$，位置 $s=-i\sigma$ 与 $s=1-i\sigma$。
  - **定理 2.2**：$m=n$ 时 $I(s;\varphi,\varphi',\Phi)$ 亚纯、竖带（离极点）有界、极点至多单且如上、满足函数方程与 Euler 乘积。

- **§3 局部 $L$ 函数（pp. 211–218）**
  - §3.1 非阿基米德：$k$、环 $\mathfrak{o}$、素理想 $\mathfrak{p}$、一致化子 $\varpi$、$q=|\mathfrak{o}/\mathfrak{p}|=|\varpi|^{-1}$。置 $\Psi_j$（$0\le j\le n-m-1$，中间夹 $M_{j,m}(k)$ 的积分），$\Psi=\Psi_0$、$\widetilde{\Psi}=\Psi_{n-m-1}$。
  - Whittaker 函数的渐近：Iwasawa 分解 + $\mathrm{A}_n(k)$ 上单根 $\alpha_i(a)=a_i/a_{i+1}$，存在有限函数集 $X(\pi)=\{\chi_i\}$ 与 Schwartz–Bruhat 函数 $\phi_i$ 使 $W(a)=\sum_{\chi_i\in X(\pi)}\chi_i(a)\phi_i(\alpha_1(a),\dots,\alpha_{n-1}(a))$；有限函数即平移张成有限维空间者，来自 Jacquet 模 $\mathcal{W}(\pi,\psi)/(\pi(n)W-W)$。
  - 三条推论：收敛域（酉时 $\mathrm{Re}(s)\ge1$，缓增时 $>0$）；每个积分是 $q^{-s}$ 的有理函数；有只依赖 $X(\pi),X(\pi')$ 的公分母。故 $\mathcal{I}_j(\pi,\pi')$ 与 $j$ 无关，记 $\mathcal{I}(\pi,\pi')$，它是 $\mathbb{C}[q^s,q^{-s}]$ 的分数理想，主理想整环故有单一生成元，归一化为 $P_{\pi,\pi'}(q^{-s})^{-1}$，$P(0)=1$。
  - **定义**：$L(s,\pi\times\pi')=P_{\pi,\pi'}(q^{-s})^{-1}$；$L(s,\pi)=L(s,\pi\times\mathbf{1})$；与 $\psi$ 无关；$L(s,\pi\times\chi)=L(s,\pi\otimes\chi)$（$\pi\otimes\chi(g)\xi=\chi(\det g)\pi(g)\xi$）。**定理 3.1**：局部积分族构成分数理想，其生成元即 $L(s,\pi\times\pi')$。
  - 等价刻画（最小性）：$L(s,\pi\times\pi')$ 是使 $\Psi/L$（或 $\Psi(\cdot,\Phi)/L$）对一切 $W,W',\Phi$ 整、形如 $P(q^{-s})^{-1}$、$P(0)=1$ 的最低次函数；因 $L$ 属该理想，可写成局部积分的有限线性组合——整体理论要用。
  - **定理 3.2**（局部函数方程）：存在 $\gamma(s,\pi\times\pi',\psi)\in\mathbb{C}(q^{-s})$，使 $\widetilde{\Psi}(1-s;\rho(w_{n,m})\widetilde{W},\widetilde{W}')=\omega'(-1)^{n-1}\gamma\Psi(s;W,W')$（$m<n$），$\Psi(1-s;\widetilde{W},\widetilde{W}',\widehat{\Phi})=\omega'(-1)^{n-1}\gamma\Psi(s;W,W',\Phi)$（$m=n$）。
  - $\varepsilon(s,\pi\times\pi',\psi)=\gamma L(s,\pi\times\pi')/L(1-s,\widetilde{\pi}\times\widetilde{\pi}')$，归一化函数方程即把 $\gamma$ 换成 $\varepsilon$、两侧同除 $L$。$\varepsilon=cq^{-fs}$，$f(\pi)\ge0$，$f(\pi)=0\iff$ 无分歧，$f(\pi)$ 即导子。
  - 无分歧情形：$\pi\cong\mathrm{Ind}(\mu_1\otimes\cdots\otimes\mu_n)$，Satake 参数 $A_\pi=\mathrm{diag}(\mu_i(\varpi))$，Shintani [43] 的显式 Whittaker 函数 $W_\circ$ 给**定理 3.3**：$L(s,\pi\times\pi')=\det(1-q^{-s}A_\pi\otimes A_{\pi'})^{-1}$（$m<n$ 时该式等于 $\Psi(s;W_\circ,W_\circ')$；$m=n$ 时等于 $\Psi(s;W_\circ,W_\circ',\Phi_\circ)$），且 $\varepsilon\equiv1$。
  - **定理 3.4**：$\pi,\pi'$ 均为（酉）超尖点时，$m<n$ 给 $L\equiv1$，$m=n$ 时 $L(s,\pi\times\pi')=\prod(1-\alpha q^{-s})^{-1}$，乘积取遍满足 $\widetilde{\pi}\cong\pi'\otimes|\det|^{s_0}$ 的 $\alpha=q^{s_0}$。
  - 一般情形靠 Bernstein–Zelevinsky [49]：一般表示都是超尖点抛物诱导的指定成分，按 [23] 用诱导数据的 Whittaker 函数、或按 [8] 用导数与拟不变配对算。
  - $\gamma$ 因子的两条定理式结论（p. 216）：**乘性**（$\pi=\mathrm{Ind}(\pi_1\otimes\pi_2)$ 时 $\gamma$ 与 $L^{-1}$ 的可除性）与**稳定性**（同中心特征的两个一般表示被足够分歧的 $\eta$ 扭后 $\gamma$ 相同、$L\equiv1$）。
  - §3.2 阿基米德：局部 Langlands 对应已就位（Langlands 分类 [30]），于是 $\pi\mapsto\rho_\pi$（Weil 群 $W_k$ 的 $n$ 维半单表示），Jacquet–Shalika [27] **定义** $L(s,\pi\times\pi')=L(s,\rho_\pi\otimes\rho_{\pi'})$、$\varepsilon$ 同理（Artin–Weil 因子 [47]），再置 $\gamma=\varepsilon L(1-s,\widetilde{\pi}\times\widetilde{\pi}')/L(s,\pi\times\pi')$。
  - 定义 $\mathcal{M}(\pi\times\pi')$：使 $P(s)L$ 在竖带 $S[a,b]$ 全纯的多项式 $P$ 都有 $P\phi$ 在 $S[a,b]$ 有界的亚纯函数 $\phi$。**定理 3.5**：局部积分延拓为 $\mathcal{M}$ 中函数，比值 $e_j,e$ 整且竖带有界（这顺带确定了 $L$ 的极点）。**定理 3.6**：局部函数方程，左端指标移动为 $\Psi_{n-m-j-1}$。
  - 所缺是「最小性」；补救是扩大积分空间：$\widehat{\Lambda}=\Lambda\otimes\Lambda'$ 延拓到完备张量积 $V_{\pi\widehat{\otimes}\pi'}$，得 $\mathcal{W}(\pi\widehat{\otimes}\pi',\psi)$，$\Psi_j(s;W)$、$\Psi(s;W,\Phi)$ 照写；仍有 $\mathcal{I}(\pi,\pi')\subset\mathcal{M}(\pi\times\pi')$，[27] 证明等号。$m=n-1$ 或 $m=n$ 时 Stade [44, 45] 与 Jacquet–Shalika（见 [9]）给出只用 $K$-有限函数的有限线性组合。

- **§4 整体 $L$ 函数（pp. 218–222）**
  - 形式定义 $L(s,\pi\times\pi')=\prod_vL(s,\pi_v\times\pi'_v)$、$\varepsilon(s,\pi\times\pi')=\prod_v\varepsilon(\cdot,\psi_v)$；$\mathrm{Re}(s)\gg0$ 绝对收敛；$v\notin S$ 时 $\varepsilon_v\equiv1$ 故 $\varepsilon$ 是有限乘积；$\varepsilon$ 与 $\psi$ 无关（[5, 引理 2.1]）。
  - §4.1 **定理 4.1**：亚纯延拓、竖带（离极点）有界、函数方程 $L(s,\pi\times\pi')=\varepsilon(s,\pi\times\pi')L(1-s,\widetilde{\pi}\times\widetilde{\pi}')$。证明：由 $I=\bigl(\prod_{v\in S}e_v\bigr)L$ 与 $I$ 的已知解析性反转出 $L$ 的解析性（$m<n$ 与 $m=n$ 两式）；函数方程由 $I(s)=\widetilde{I}(1-s)$、局部函数方程与 $\prod_{v\in S}\omega'_v(-1)^{n-1}\varepsilon_v=\varepsilon$ 拼出。
  - 有界性：$m=n-1$ 或 $n$ 时 Stade 与 Jacquet–Shalika 给整体 $L=\sum I(\cdot;\varphi_i,\varphi'_i)$（或带 $\Phi_i$），故有界性继承。$m<n-1$ 时 $v\in S_\infty$ 只知道 $L(s,\pi_v\times\pi'_v)$ 是 $\mathcal{W}(\pi_v\widehat{\otimes}\pi'_v,\psi_v)$ 中单个或有限个函数的积分，须把整体理论重做在 $V_\pi\widehat{\otimes}V_{\pi'}$ 上——原书明言「看不出障碍，但未做」。另一条路（Eisenstein 常数项与 Fourier 系数）Gelbart–Shahidi [12] 已证一大类有界性。
  - §4.2 **定理 4.2**：$m<n$ 时整；$m=n$ 时至多单极点，且 $\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}$（$\sigma$ 实）时在 $s=-i\sigma,1-i\sigma$。两条观察：$L(s,\pi\times\widetilde{\pi})$ 在 $s=0,1$ 有单极点；$L(s,\pi\times\widetilde{\pi}')$ 在 $s=1$ 有极点 $\iff\pi\cong\pi'$。由此得**强重数一**（[31]、[25]）：两个尖点表示若几乎处处同构则相等。

- **§5 逆定理（pp. 222–225）**
  - 回顾 Hecke [17]：由 $D(s)=\sum a_nn^{-s}$ 的整延拓、有限阶、与权 $k$ 模形式相同的函数方程，经 Mellin 逆变换 $f(iy)=\frac{1}{2\pi i}\int_{2-i\infty}^{2+i\infty}(2\pi)^{-s}\Gamma(s)D(s)y^sds$ 重构模形式，并反推 $\tau\mapsto-1/\tau$ 的变换律。
  - 一般框架：$\Pi$ 为 $\mathrm{GL}_n(\mathbb{A})$ 的不可约容许（设酉且一般）表示，形式地置 $L(s,\Pi)=\prod L(s,\Pi_v)$、$\varepsilon(s,\Pi,\psi)=\prod\varepsilon(\cdot,\psi_v)$；两条假设：$L$ 在某半平面收敛、中心特征 $\omega_\Pi$ 自守（$k^\times$ 上不变），于是 $\varepsilon$ 与 $\psi$ 无关。
  - $\mathcal{A}(m)$、$\mathcal{A}_0(m)$（尖点）、$T(m)=\bigcup_{d=1}^m\mathcal{A}_0(d)$、$T(S;m)$（$v\notin S$ 处无分歧者）；$\pi'$ 尖点、$m<n$ 时同样形式定义 $L(s,\Pi\times\pi')$、$\varepsilon(s,\Pi\times\pi')$。
  - **「好」（nice）**的定义（三条：$L(s,\Pi\times\pi')$ 与 $L(s,\widetilde{\Pi}\times\widetilde{\pi}')$ 整、竖带有界、标准函数方程）。
  - **定理 5.1**（[5, 4]）：$S$ 有限，若对一切 $\pi'\in T(S;n-1)$ 都「好」，则 $\Pi$ 拟自守：存在自守 $\Pi'$ 使 $v\notin S$ 处 $\Pi_v\cong\Pi'_v$；$S$ 空时 $\Pi$ 实为尖点自守。**定理 5.2**：把 $T(S;n-1)$ 换成 $T(S;n-2)$ 仍成立（更强，证明更细）。
  - **观察**：以充分分歧的 $\eta$ 扭，若对所有 $\pi'\in\mathcal{T}\otimes\eta$ 都「好」（$\mathcal{T}$ 为 5.1 或 5.2 的扭集），则同样拟自守——因 $L(s,\Pi\times(\pi'\otimes\eta))=L(s,(\Pi\otimes\eta)\times\pi')$。
  - **定理 5.3**：非空 $S\supset S_\infty$ 且 $\mathfrak{o}_S$ 类数为一，若对一切 $\pi'\in T_S(n-1)$（$v\notin S$ 处无分歧）都「好」，则 $\Pi$ 拟自守，且 $v\in S$ 与 $v\notin S$ 两侧的 $\Pi_v,\Pi'_v$ 均无分歧。
  - 讨论：类数限制（$k=\mathbb{Q}$ 时可取 $S=S_\infty$，得「level 1」扭的逆定理；实用上取 $S$ 与 $\Pi$ 的分歧位点集 $S_\Pi$ 不交）；$S$ 空时的证明沿 Hecke–Weil–Jacquet–Langlands 路线（积分表示 + Fourier 展开 + Mellin 逆变换 + 弱形式谱理论），限制扭之后须以局部条件补偿（5.1、5.2 有限多个，5.3 无限多个），靠同余子群生成与弱/强逼近绕过。

## 体裁

综述兼讲义（synopsis of [1]），无证明细节，只有「证明的思路」一句带过。全章 15 个编号定理（1.1、1.2、2.1、2.2、3.1–3.6、4.1、4.2、5.1–5.3）加两条无编号定理式陈述（重数一、强重数一）与一条「观察」。第一人称复数为主（「我们」），偶有 "Either by analogy with Tate's thesis..." 式的作者口吻，译文保留「我们」。句子长、从句多，已按中文习惯拆句，每句控制在 60–70 字内。

## 术语处理（本章新增/定夺）

| 英文 | 译名 | 说明 |
| --- | --- | --- |
| cuspidal automorphic representation | 尖点自守表示 | 库内既有 |
| Whittaker model / functional | Whittaker 模型 / 泛函 | 保留人名 |
| multiplicity one / strong multiplicity one | 重数一 / 强重数一 | |
| generic / nondegenerate | 一般的 / 非退化的 | 两词同义，译文并列 |
| mirabolic subgroup | 棒状子群 | 首次出现加英文 |
| gauge estimate | 规范估计 | 首次出现加英文 |
| tempered | 缓增 | |
| finite function | 有限函数 | 平移张成有限维 |
| conductor | 导子 | $f(\pi)$ |
| unramified twist | 无分歧扭 | |
| fractional ideal | 分数理想 | $\mathbb{C}[q^s,q^{-s}]$ 的理想 |
| quasi-automorphic | 拟自守的 | quasiamorphic |
| nice | 好的 | 原文斜体，随文加引号 |
| Eisenstein series constant term | 常数项 | |
| Theta series | Theta 级数 | |
| essentially bounded in vertical strips | 竖直带有界 | 原文 "bounded in vertical strips" |

## 风险点（均已逐条回页图核对）

1. **定理 1.1 的求和指标**是 $\gamma\in\mathrm{N}_{n-1}(k)\backslash\mathrm{GL}_{n-1}(k)$（不是 $\mathrm{N}_n$），p. 200 图可核；证明最后一步用 $\varphi_g(1)$ 的展开再右乘 $g$。
2. **$\mathbb{P}^n_m$ 的归一化因子**是 $|\det p|^{-(n-m-1)/2}$，指数里是 $n-m-1$ 而非 $n-m$，p. 205 图可核；这与后面 $s-(n-m)/2$ 的指数配套。
3. **$W'_{\varphi'}$ 的 $\psi$ 指数**：p. 206 写作 $\int\varphi'(nh)\psi(n)dn$（正号），但同页称其为 $\psi^{-1}$-Whittaker 函数；照录，译注说明这是 $\varphi'$ 与 $\varphi$ 用相反特征的约定。
4. **$w_{n,m}=\mathrm{diag}(I_m,w_{n-m})$** 与 $\rho$（右平移）的定义在 p. 207；$\widetilde{\Psi}=\Psi_{n-m-1}$ 的指标移动在定理 3.6 中再次出现（$\Psi_{n-m-j-1}$）。
5. **定理 3.3 的三行分段**：原书用大括号把 $m<n$ 与 $m=n$ 两种情形并写在一个 $=$ 之后，译文用 cases 环境重现。
6. **定理 3.4 的乘积**：「over all $\alpha=q^{s_0}$ with $\widetilde{\pi}\cong\pi'\otimes|\det|^{s_0}$」措辞不规范（点集只有一个元素或无元素），译文照译并出注说明空积为 1。
7. **$\mathcal{M}(\pi\times\pi')$ 的定义**用多项式 $P$ 与竖带 $S[a,b]$ 的量化，p. 217 图可核；「$\phi L^{-1}$ 整」是推论而非定义。
8. **定理 5.1/5.2 的扭集**分别是 $T(S;n-1)$ 与 $T(S;n-2)$，差一阶，p. 224 图可核。
9. **$\mathfrak{o}_S$ 类数为一**的条件在定理 5.3，p. 225；$k=\mathbb{Q}$ 时 $S=S_\infty$ 满足。
10. **公式排版**：$\Psi_j$ 的 $M_{j,m}(k)$ 双重积分、$\Psi(s;W,\Phi)$ 的完备张量积版本、$E(g,\Phi;s,\eta)$ 的三行分段，均在编译中避免 overfull（最长者已拆为两行）。

## 底本笔误（正文照录，章末译注汇总 (a)–(g)）

| 页 | 原文 | 应为 |
| --- | --- | --- |
| 201 | for all $n\in N_k(k_v)$ | $N_n(k_v)$ |
| 210 | Hence a residues can be nonzero | the residues |
| 211 | $q$ 称 residue degree | 剩余域基数（$q=|\mathfrak{o}/\mathfrak{p}|$） |
| 212 | $\widehat{\Phi}(x)=\int_{\mathbb{A}^\times}\Phi(y)\psi(y{}^tx)dy$ | 积分域 $\mathbb{A}^n$ |
| 213 | the representation of $\mathrm{GL}_n(\mathbb{A})$ | $\mathrm{GL}_n(k)$（局部一节） |
| 214 | except for a finite number **if** exceptional values | of |
| 218 | $\Psi(s;W,\Phi)=\int\cdots dh$ | $dg$ |

另：p. 212 的 $\delta(s)$ 写作 $\eta(a)=|a|^{in\sigma}$，指数中的 $n$ 来历不明（若 $\eta$ 是 $\mathrm{GL}_1$ 的特征应为 $i\sigma$）；原书如此，照录。

## 译注清单（15 条，均为 A 类：原书或经典文献）

| # | 位置 | 主题 |
| --- | --- | --- |
| 1 | 引言 | Hecke 逆定理的逻辑形状与解析归一化 |
| 2 | §1.1 | Gelfand–Kazhdan–Shalika：$\mathrm{N}_n$ 非交换，以 Whittaker 函数替换加法特征展开 |
| 3 | §1.2 | Whittaker 模型唯一性何以是整章枢纽（整体→局部对接） |
| 4 | §2.1 | $|a|^{s-1/2}$ 归一化的来历（否则对应 $L(s+1/2,\cdot)$ 的平移） |
| 5 | §2.2 | 投影算子 $\mathbb{P}^n_m$ 的作用与归一化 |
| 6 | §3.1 | 有限函数三条推论：分母有界、$X(\pi)$ 即 Jacquet 模的权 |
| 7 | §3.1 | 用分数理想定义局部 $L$ 因子（生成元、$P(0)=1$） |
| 8 | §3.1 | 定理 3.3 的 Satake 显式，$n=m=1$ 时退回局部 zeta 因子 |
| 9 | §3.2 | 阿基米德侧直接搬 Artin–Weil 因子，再回验局部积分 |
| 10 | §4.1 | 整体函数方程的推导：局部 $\gamma$ 与 $L$ 相消，只剩 $\varepsilon$ |
| 11 | §4.1 | $m<n-1$ 的阿基米德有界性缺口（须绕道 Gelbart–Shahidi） |
| 12 | §4.2 | 以 $s=1$ 极点判别 $\pi\cong\pi'$（Rankin–Selberg 的经典应用） |
| 13 | §5 | 逆定理与正定理方向相反：把解析性质当作公理反推自守性 |
| 14 | §5 | 类数条件：$S=S_\infty$ 时只剩 level 1 扭，类数为一保证扭足够多 |
| 15 | 章末 | 底本笔误一览 (a)–(g) |

## 未解疑点

1. $\delta(s)$ 中 $\eta(a)=|a|^{in\sigma}$ 的 $n$：若按局部 $\mathrm{GL}_1$ 特征理解应为 $|a|^{i\sigma}$；原书整体归一化里确实带 $n$（$|\det g|^s$ 与 $|a|^{ns}$ 配对），但此处 $\eta$ 是伊代尔类特征，$n$ 的来源无旁证。已照录，未改。

（其余原书可疑处均已在页图上核实为原文如此，并收入笔误表或译注，不另计。）

## 编译自测

隔离编译（只含 ch00_titlepage、ch00_preface、ch09，保留 `\setcounter{chapter}{8}`）：xelatex 三遍，exit=0，`!` 0 处，undefined 0，Missing character 0，Overfull 0，Underfull 2（首页 vbox 与一处段落 badness，可忽略），27 页。整书编译会被兄弟 agent 正在写的 ch08 等文件中断，与本文件无关。
