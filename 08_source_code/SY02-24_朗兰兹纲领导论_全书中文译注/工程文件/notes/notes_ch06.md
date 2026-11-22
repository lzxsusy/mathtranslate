# 第 6 章 通读笔记

Stephen S. Kudla, *Tate's Thesis*
原书印刷页 109–131（章末参考文献止于印刷页 131），页图 `work/pages/c06_p114.png`–`c06_p134.png`，另加 `work/tmp_ch06/nxt_p135.png`–`nxt_p136.png`。

## 页码核对（2026-11-23 已按主编订正）

- 实测页眉：**印刷页 = PDF 页 − 5**（`c06_p115.png` 印 110、`c06_p116.png` 印 111、`c06_p133.png` 印 128、`c06_p134.png` 印 129）。
- 旧 `ch06_raw.txt` 按「原书页 = PDF 页 − 2」贴标签，故只到 PDF 134（印刷页 129）便中断，缺练习后半与 REFERENCES。
- 现 `work/en/ch06_raw.txt` 已重抽，标签改为 `===== PDF PAGE n (BOOK m) =====`，共 23 页：**PDF 114–136 = 印刷页 109–131**；章题页 PDF 114，REFERENCES 止于 PDF 136。
- 译文据此逐页复校：开头即章题（无第 5 章残文），中段 23 页逐页对照，末尾 [1]–[14] 齐全。页图为 `work/pages/c06_p114.png`–`work/pages/c06_p134.png`，PDF 135、136 用 `work/tmp_ch06/nxt_p135.png`、`nxt_p136.png`。
- PDF 111–113（印 106–108）是第 5 章 de Shalit 的结尾与参考文献，不属本章。

## 三句话主旨

1. Tate 论文用 Chevalley 的阿代尔／伊代尔上的交换调和分析，统一处理任意数域上任意 Hecke 特征 $\chi$ 的 $L(s,\chi)$ 的解析延拓与函数方程，取代了 Hecke 靠 Grössencharakter 硬算的经典方法。
2. 技术上把局部 $L$ 因子实现为「一维本征分布空间的两组自然基之间的比例常数」：局部唯一性定理（定理 3.4，$\dim S'(\omega)=1$）给出 $z(s,\omega)=L(s,\omega)z_o(s,\omega)$，整体张量积再把它升为 $\Lambda(s,\omega)$ 的比例常数。
3. 整体函数方程由三件事拼成：比例关系 (4.3)、局部函数方程 (3.23)、以及 Poisson 求和给出的整体恒等式 $\widehat{z(1-s,\omega^{-1})}=z(s,\omega)$（定理 4.3）；$\epsilon$ 因子整体化后与加法特征 $\psi$ 的选取无关。

## 逐节内容地图

**引言（印 109）** 交代 Tate 论文出处（Cassels–Fröhlich 1967 第 XV 章）、Hecke 的 Grössencharakter、交换调和分析相对经典方法的进步；说明本章两目标（统一处理 $L(s,\chi)$；在最简单情形引入阿代尔群表示论）；指出 $G=\mathrm{GL}(1)$ 是现代自守表示论的起点。末尾给参考文献评注：Weil [13, VII]、Bump [2, 3.1]、[5]、[9]、Valenza–Ramakrishnan [11]；声明本章大体沿 Weil 1966 Bourbaki 报告 [12, 14] 的路子，强调 Tate 原文只隐含的「等变分布」。脚注 *：2001 年 3 月耶路撒冷希伯来大学暑期学校两次讲演的扩写；脚注 1：Tate 在论文中及 [3, XV] 末有历史评注。

**§1 阿代尔、伊代尔与 Dirichlet 特征（印 109–112）**
- 经典 Dirichlet 特征 $\underline\chi_N:\mathbb Z\to\mathbb C$（在 $\mathbb Z/N\mathbb Z$ 上延拓 0 再拉回）、$\chi_N:(\mathbb Z/N\mathbb Z)^\times\to\mathbb C^\times$、$N\mid M$ 时的 $\mathrm{pr}_{M,N}$ 拉回、$\underline\chi_M$。
- 逆向极限 $\widehat{\mathbb Z}^\times=\varprojlim(\mathbb Z/N\mathbb Z)^\times$（脚注 2 给显式定义，紧、全不连通）；导子 $N_0$ 是最小使 $\chi$ 在 $\mathrm{pr}_{N_0}$ 的核上平凡者；本原／非本原特征；与 $\mathrm{GL}(2)$ 新形式的类比。
- $p$ 进基本事实：$\mathbb Z_p$、$\mathbb Z_p^\times$、$\mathbb Q_p$；阿代尔环 $\mathbb A=\mathbb R\times\prod'_p\mathbb Q_p$（脚注 3：几乎全部分量在 $\mathbb Z_p$）；伊代尔群 $\mathbb A^\times=\prod'_v\mathbb Q_v^\times$；(1.1) $\mathbb A^\times\simeq\mathbb Q^\times\times\mathbb R^\times_+\times\widehat{\mathbb Z}^\times$，$x=\alpha tu$。
- 由 $\chi$ 造 $\omega(\alpha tu)=\chi(u)$；最一般的拟特征为 $\omega\cdot|\ |^s$（脚注 4：取值在 $\mathbb C^1$ 才叫特征）；Dirichlet 特征恰是有限阶拟特征。
- $(\mathbb Z/N\mathbb Z)^\times=\prod_p(\mathbb Z/p^n\mathbb Z)^\times$、$\chi_N=\otimes_p(\chi_N)_p$、$\chi=\otimes_p\chi_p$；(1.2) $\omega=\otimes_v\omega_v$；$i_v$ 嵌入。
- 练习 (i) 奇特征给出 $\omega_\infty(x)=\operatorname{sgn}(x)=x/|x|$；(ii) 求 $\omega_p(p)$，$p\nmid N$ 与 $p\mid N$ 两种情形。

**§2 拟特征的 $L$ 函数（印 112–114）**
- 一般数域 $k$（脚注 5：函数域情形从略）：$\mathcal O,\mathcal O_v,\mathcal P_v,\varpi_v,\mathbb F_v,q_v,\operatorname{ord}_v,|x|_v=q_v^{-\operatorname{ord}_v(x)},\mathcal O_v^\times$；$\mathcal O_v^\times\times\mathbb Z\simeq k_v^\times$；阿基米德位 $|x|_v$ 为通常绝对值（$\mathbb C$ 情形为其平方）；限制乘积 $\mathbb A,\mathbb A^\times$；绝对值 $|\ |_\mathbb A$，乘积公式。
- 定义 2.1：拟特征＝Hecke 特征＝$\mathbb A^\times\to\mathbb C^\times$ 的连续复特征、在 $k^\times$ 上平凡；$\omega=\otimes_v\omega_v$。
- 定义 2.2：非阿基米德位无分歧＝在 $\mathcal O_v^\times$ 上平凡，故 $\omega_v(x)=t_v^{\operatorname{ord}_v(x)}$；整体无分歧；$S(\omega)$（脚注 6：阿基米德位无「无分歧」概念）。
- 定义 2.3：(EP) $L^S(s,\omega)=\prod_{v\notin S}(1-t_v(\omega)q_v^{-s})^{-1}$；局部因子 $L_v(s,\omega_v)=(1-t_v(\omega)q_v^{-s})^{-1}$；$L^S(s,\omega)=L^S(0,\omega\omega_s)$；$\mathrm{Re}(s)>1$ 绝对收敛。
- 两大目标：补全局部因子、证亚纯延拓与函数方程；手段是把局部 $L$ 因子读成「一维分布空间两组自然基」的比例常数。

**§3 局部理论（印 114–125）**
- 固定位 $v$，$F=k_v$；$dx$、$d^\times x$，$d(ax)=|a|dx$，$d^\times x=\mu|x|^{-1}dx$；$\omega_s(x)=|x|^s$；非阿基米德时 $\omega_s$ 只依赖 $s+\frac{2\pi i}{\log q}\mathbb Z$。
- $S(F)$（Schwartz–Bruhat）、$S(F)'$（缓增分布）。例 (i) 非阿基米德：紧支且在 $\mathcal P^r$ 陪集上常值；此时 $S(F)'$ 是全部 $\mathbb C$-线性泛函。例 (ii) $\mathbb R/\mathbb C$：通常 Schwartz 空间，Fréchet（脚注 7 引 Friedlander [4]、非阿基米德引 [1]）。
- 作用 $r(a)f(x)=f(xa)$、$\langle r'(a)\lambda,f\rangle=\langle\lambda,r(a^{-1})f\rangle$；定义 3.1：$S'(\omega)=\{\lambda: r'(a)\lambda=\omega(a)\lambda\}$。
- 几何分析：$F=\{0\}\cup F^\times$ 两条轨道；$C_c^\infty(F^\times)\hookrightarrow S(F)$ 对偶给正合列 (3.1)，取 $\omega$-本征空间得 (3.2)。
- 引理 3.2：$C_c^\infty(F^\times)'(\omega)$ 一维，由 $\omega(x)d^\times x$ 张成。
- 引理 3.3：支在 0 的分布。(i) 非阿基米德 $S(F)'_0=\mathbb C\delta_0\subset S'(\omega_0)$，$\omega\ne\omega_0$ 时为 0；(ii) $\mathbb R$：$S(F)'_0=\bigoplus_{k\ge0}\mathbb C D^k\delta_0$，$D=\frac{d}{dx}$，$\omega(x)=x^{-k}$；(iii) $\mathbb C$：$D=\frac{\partial}{\partial x}$、$\bar D=\frac{\partial}{\partial\bar x}$，$\bigoplus_{k,l}\mathbb C D^k\bar D^l\delta_0$，$\omega(x)=x^{-k}\bar x^{-l}$。脚注 8：阿基米德情形只给 $F^\times$-有限分布。
- 定理 3.4：$\dim S'(\omega)=1$。两条 Remarks：$S'(\omega)_0=0$ 时只欠存在性；$S'(\omega)_0\ne0$ 时须证 $\omega(x)d^\times x$ 不能延拓。例：分歧 $\omega$ 时 $S'(\omega\omega_s)_0=0$；无分歧时维数上界 2 或 1，视 $tq^{-s}=1$。
- zeta 积分 (3.3)：$\mathrm{Re}(s)>0$ 绝对收敛，$f\mapsto z(s,\omega;f)$ 给出非零 $z(s,\omega)\in S'(\omega\omega_s)$。
- 无分歧局部理论：(3.4) $\tau=[1]-[\varpi^{-1}]$ 杀掉支集；(3.5) $z_o(s,\omega)$；Re$(s)>0$ 中的计算给出 $(1-tq^{-s})z(s,\omega;f)$，即 (3.6) $z(s,\omega)=L(s,\omega)z_o(s,\omega)$；归一化 $\mathrm{vol}(\mathcal O^\times)=1$，(3.7) $f^o$＝$\mathcal O$ 的示性函数；(3.8) $\langle z_o(s,\omega),f^o\rangle=1$。
- 注（$L$ 因子即「最大公分母」）：(3.9) $z(s,\omega;f)/L(s,\omega)=\langle z_o(s,\omega),f\rangle$ 整，且对每个 $s$ 有 $f=f^o$ 使其非零。
- 补完无分歧情形的定理 3.4：(3.10)(3.11) 正合列；(3.12) $\lambda_0$；(3.13) 算出 $c=-1$；(3.14) 二维表示矩阵。
- 分歧局部理论：导子 $c(\omega)$ 最小使 $\omega$ 在 $1+\mathcal P^c$ 上平凡；$\int_{F^\times-\mathcal P^n}$ 当 $n$ 大时与 $n$ 无关，给出整延拓与 (3.15) $z_o(s,\omega):=z(s,\omega)$；(3.16) $L_v(s,\omega)=1$；(3.17) $f^o$；$\langle z_o,f^o\rangle=1$；gcd 性质 (3.9) 仍成立。
- 阿基米德情形：极点是 $f$ 在 0 的整条 Taylor 级数所致（引 [2, Prop 3.1.7]）。(3.18) $\mathbb R$：$\omega(x)=x^{-a}$、$a=0,1$；(3.19) $L(s,\omega)=\pi^{-s/2}\Gamma(s/2)$；(3.20) $\mathbb C$：$\omega(x)=x^{-a}\bar x^{-b}$、$\min(a,b)=0$；(3.21) $L(s,\omega)=(2\pi)^{1-s}\Gamma(s)$。
- 命题 3.5：$z_o=L^{-1}z$ 整、处处为基；$f^o=f_a$ 或 $f_{a,b}$ 时 $\langle z_o,f^o\rangle=1$；测度约定（$\mathbb C$ 上 $|x|=x\bar x$，$dx$ 为 Lebesgue 测度的两倍）。
- 注：(3.22) $\operatorname{Res}_{s=-r}z(s,\omega)=c_rD^r\delta_0$（$\mathbb R$，$r\equiv a\bmod 2$）；Laurent 常数项给出 $x^{-r}d^\times x$ 到 $S(F)$ 的延拓，但不属于 $S'(\omega\omega_{-r})$；$\mathbb C$ 情形留数在 $S'(\omega\omega_{-r})$ 中，是 $D^{a+r}\bar D^{b+r}\delta_0$ 的非零倍。
- Fourier 变换：非平凡加法特征 $\psi$；$\widehat F=\operatorname{Hom}_{cont}(F,\mathbb C^1)$，$F\simeq\widehat F$，$y\mapsto(x\mapsto\psi(xy))$；非阿基米德导子 $\nu(\psi)$ 为最大使 $\psi$ 在 $\mathcal P^{-\nu}$ 上平凡者；$\hat f(x)=\int f(y)\psi(xy)dy$；自对偶测度使反演为 $\hat{\hat f}(x)=f(-x)$；分布 Fourier 变换 $\langle\hat\lambda,f\rangle=\langle\lambda,\hat f\rangle$。
- 引理 3.6：$\lambda\in S'(\omega)\Rightarrow\hat\lambda\in S'(\omega^{-1}\omega_1)$，$\omega_1(x)=|x|$；证明「An exercise!」。
- 推论 3.7（局部函数方程）：(3.23) $\widehat{z_o(1-s,\omega^{-1})}=\epsilon(s,\omega,\psi)z_o(s,\omega)$，$\epsilon$ 为局部 epsilon 因子。
- 注：改写为 (3.24)(3.25)，比例常数 (3.26) 即局部伽马因子 $\gamma$；(3.27) 用 $f^o$ 配对得 $\epsilon$ 的表达式；(3.28) $\epsilon(s,\omega\omega_t,\psi)=\epsilon(s+t,\omega,\psi)$；(3.29) $\epsilon(s,\omega,\psi_\beta)=|\beta|^{s-\frac12}\omega(\beta)\epsilon(s,\omega,\psi)$。
- 命题 3.8：显式 $\epsilon$。(i) 无分歧 $\epsilon=\omega(\varpi^\nu)q^{(\frac12-s)\nu}$；(ii) 分歧 $\epsilon=\omega(\varpi^{\nu+c})q^{(\frac12-s)(\nu+c)}\mathfrak g(\omega,\psi)$，高斯和 $\mathfrak g=q^{\frac12(\nu+c)}\int_{\mathcal O^\times}\omega^{-1}(y)\psi(\varpi^{-\nu-c}y)dy$；(iii) $\mathbb R$：$\epsilon=i^a$；(iv) $\mathbb C$：$\epsilon=i^{\max(a,b)}$。
- 证明：(3.30) 标准 $\psi$（$e(x)$／$e(x+\bar x)$）；(3.31) $\widehat{f^o}(x)=\mathfrak g q^{-\frac12(\nu+c)}\overline{f^o(\varpi^{\nu+c}x)}$；(3.32) 高斯和定义式；(3.33)(3.34) 用 $D^a_x$ 与 $(2\pi i)^{-a}$ 算 Fourier 变换。

**§4 整体理论（印 125–128）**
- $S(\A)$：可分解函数 $f=\otimes_vf_v$（几乎处处 $f_v=f_v^o$），$f(x)=\prod_vf_v(x_v)$，有限线性组合稠密。
- 引理 4.1：局部分布之张量积，正反两向。
- 伊代尔群作用；$S'(\omega)=\otimes_vS'_v(\omega_v)$；定理 4.2：$\dim S'(\omega)=1$，$S'(\omega\omega_s)$ 由 $z_o(s,\omega)=\otimes_vz_o(s,\omega_v)$ 张成。
- 整体 zeta 积分 (4.1)(4.2)；收敛性等价于 $L^S(s,\omega)$ 绝对收敛，即 $\mathrm{Re}(s)>1$；(4.3) $z=\Lambda z_o$；(4.4) $\Lambda(s,\omega)=\prod_vL_v(s,\omega)$；(4.5)。
- Fourier 变换与整体函数方程：整体加法特征 $\psi$（在 $k$ 上平凡），$\psi=\prod_v\psi_v$，导子 $\nu_v$；整体 Fourier 变换与局部相容，$\hat f=\otimes_v\hat f_v$；自对偶测度。
- 定理 4.3：$z(s,\omega)$ 亚纯延拓且 (4.3 之前) $\widehat{z(1-s,\omega^{-1})}=z(s,\omega)$。
- 由 (4.3) 得 $\Lambda$ 的延拓；局部函数方程（原文误引为 (3.13)，实为 (3.23)）；(4.6) 整体 $\epsilon$；(4.7)；$\psi$ 可略去的理由（(3.29)、$\psi_\beta$、乘积公式）；(4.8)(4.9)；推论 4.4 $\Lambda(s,\omega)=\epsilon(s,\omega)\Lambda(1-s,\omega^{-1})$。
- 收尾：定理 4.3 归结为 Riemann 的 Poisson 求和论证，细节见 Tate 论文 pp. 339–341、Weil [13, pp. 121–124]、Bump [2, pp. 267–270]。

**§5 例子（印 129–130）**
- (5.1) $\mathfrak m=\prod_v\mathfrak p_v^{c_v(\omega)}$；$\chi(\mathfrak p_v)=\omega_v(\varpi_v)$ 定义 $I_\mathfrak m$ 上的特征。
- (5.2) $k^\times_\mathfrak m=\{\alpha\equiv1\bmod\mathfrak m\}$，$P_\mathfrak m$；(5.3) $\chi((\alpha))=\omega_\infty(\alpha)^{-1}$；$\omega_\infty$ 为阿基米德部分；(5.4) $\omega_\infty(\epsilon)=1$。
- 反向：由经典 Hecke 特征 $\chi$ 复原 $\omega$；弱逼近定理 [3]；导子与 $\mathrm{ord}_v(\mathfrak m)$ 的关系。脚注 9：Hecke 所谓 Grössencharakter 即 $\chi$ 依赖于阿基米德位上的「量」（Grössen）$\alpha_v$。
- $\omega_\infty=1$：$\mathfrak m=\mathcal O_k$ 给理想类群 $H=I/P$ 的特征；一般 $\mathfrak m$ 给射线类群 $H_\mathfrak m=I_\mathfrak m/P_\mathfrak m$ 的特征；$\omega=1$ 给 Dedekind zeta，详见 [13, VII §6、§7]。
- 练习：$k=\mathbb Q(\sqrt5)$，$\epsilon=\frac{1+\sqrt5}{2}$，$\mathcal O_k^\times=\{\pm1\}\times\{\epsilon^n\}$。(i) $\mathfrak m=\mathcal O_k$ 时 $\omega_\infty(x_1,x_2)=|x_1/x_2|^{-i\pi/\log\epsilon}$ 在 $\mathcal O_k^\times$ 上平凡，$\chi((\alpha))=\omega_\infty(\alpha)^{-1}=|\alpha/\alpha'|^{i\pi/\log\epsilon}$；(ii) $\mathfrak m=(\sqrt5)=\mathfrak p_5$ 时 $k^\times_\mathfrak m\cap\mathcal O_k^\times$ 由 $-\epsilon^2$ 生成；(iii) 定出满足 (5.3) 的全部 $\omega_\infty$，两个例子见 (5.4)（原书重复使用编号 (5.4)）；(iv) 求 $\omega_5$：$\mathcal O_5^\times/(1+\mathcal P_5)\simeq\mathbb F_5^\times$，$\varpi_5=\sqrt5$，$\omega_5(\sqrt5)=1$、$\omega_5(\epsilon)=i$；(v) 定出经典 Hecke 特征 $\chi$；(vi) 写出对应 Hecke $L$ 级数与函数方程。

**REFERENCES（印 130–131）** [1] Bernstein–Zelevinski；[2] Bump；[3] Cassels–Fröhlich；[4] Friedlander；[5] Gelbart 1975；[6] Gelbart 1984；[7] Hecke；[8] Kowalski（本书内）；[9] Lang；[10] Tate 论文；[11] Valenza–Ramakrishnan；[12] Weil Bourbaki；[13] Weil《Basic Number Theory》；[14] Weil《Collected Papers》。

## 体裁

讲义式综述：定义—引理—定理—注，证明多半只给思路或直接推给 Tate 原文与 Weil、Bump。公式密度极高，且原书用「局部→整体」的固定套路：先证一维唯一性，再把 $L$ 因子读成基变换常数。译注应补足被跳过的关键计算（$\tau$ 杀支集、$c=-1$、$\epsilon$ 的三个显式公式、$\psi$ 无关性），并点明归一化与交叉引用错误，不宜展开完整证明。

## 公式/记号风险点

1. **页码**：见上「页码核对」。旧 raw 标签偏大 3；现 `work/en/ch06_raw.txt` 已按真实边界重抽（PDF 114–136 = 印刷 109–131），译文与之一致。
2. **(3.2) 无尾零**：原书 $0\to S'(\omega)_0\to S'(\omega)\to C_c^\infty(F^\times)'(\omega)$ 后没有 $\to0$（(3.1) 有），照排，不补。
3. **(3.14) 的基序**：矩阵 $\begin{pmatrix}1&-\operatorname{ord}(x)\\&1\end{pmatrix}$ 是相对有序基 $(\delta_0,\lambda_0)$ 写的；若按原文叙述顺序 $(\lambda_0,\delta_0)$，应为下三角。译文照排并出注。
4. **(3.23)、(4.7)、(4.8) 的宽帽**：$\widehat{z_o(1-s,\omega^{-1})}$ 是分布的 Fourier 变换，帽号覆盖整个 $z_o(\cdot)$，不是只盖 $z_o$；漏掉会与 $z_o$ 本身混淆。
5. **(3.32) 与 p. 129 无编号式重复**：同一高斯和公式原书排了两遍（p. 129 无编号，p. 130 编号 (3.32)）；照排。
6. **原文交叉引用错误两处**：(a) p. 128「local functional equations have the form (3.13)」应为 (3.23)；(b) 同页「given explicitly in Proposition 3.7」应为命题 3.8。译文照排并出注。
7. **(3.27) 的 $\widehat{f^o}$**：帽号覆盖 $f^o$ 整体（$f^o$ 的上标 0 不是帽号的一部分）。
8. **(3.22) 的 $D^r$**：$\mathbb R$ 情形的 $D$ 是 $\frac{d}{dx}$；$\mathbb C$ 情形用 $D=\frac{\partial}{\partial x}$、$\bar D=\frac{\partial}{\partial\bar x}$，留数是 $D^{a+r}\bar D^{b+r}\delta_0$ 的非零倍，指数是 $a+r$、$b+r$ 而非 $r$。
9. **$\mathbb C$ 上的 $|x|$**：$|z|_{\mathbb C}=z\bar z$（通常绝对值的平方），故 (3.30) 的自对偶测度与 $\mathbb R$ 情形不同；(3.21) 的 $(2\pi)^{1-s}\Gamma(s)$ 依赖于该约定。
10. **(5.4) 编号重复**：印 129 的 $\omega_\infty(\epsilon)=1$ 与印 130 练习 (iii) 末尾的两个 $\omega_\infty$ 都标 (5.4)。译文两处都保留 (5.4)，出注说明。
11. **(1.1) 的 $\simeq$ 是宽松写法**：分解不唯一，$\mathbb Q^\times\cap\widehat{\mathbb Z}^\times=\{\pm1\}$ 给出 $(\alpha,u)$ 的 $\pm$ 二义性，故 $\omega(\alpha tu)=\chi(u)$ 只对偶特征良定义；奇特征须补 $\operatorname{sgn}$，正是练习 (i) 的由来。出注。
12. **$\omega_s$ 的周期**：非阿基米德时 $\omega_{s+\frac{2\pi i}{\log q}}=\omega_s$，故「$s$ 可省去」一语（$L^S(s,\omega)=L^S(0,\omega\omega_s)$）须按此理解。
13. **$S(F)'$ 在非阿基米德情形＝全部线性泛函**：因为 $S(F)$ 是有限维空间的正向极限、取最细局部凸拓扑，连续性与线性等价；不可与阿基米德情形（Fréchet 空间的对偶）混为一谈。
14. **$f^o$ 的两义**：无分歧时 $f^o$ 是 $\mathcal O$ 的示性函数 (3.7)；分歧时是 (3.17) 的 $\omega(x)^{-1}\mathbf 1_{\mathcal O^\times}$；阿基米德时是命题 3.5 的 $f_a$／$f_{a,b}$。同一记号三种含义，随情形切换。
15. **练习 (iii) 的两行公式**：$\operatorname{sgn}(x_1)|x_1/x_2|^{-i\pi/(4\log\epsilon)}$ 与 $|x_1/x_2|^{-i\pi/(2\log\epsilon)}$，指数分母分别是 $4\log\epsilon$ 与 $2\log\epsilon$，易混。

## 交付核对（写完后补记）

- `src/chapters/ch06.tex`：895 行，5 个 `\section`、11 个 `\subsection*`、51 个 `\tag`、12 条 `annote`。
- 编译：`work/tmp_ch06/build/test.tex`（复制 main.tex 全部 preamble 与 annote、`\ob` 定义，`\input{../../../src/chapters/ch06}`）连跑 3 遍，共 20 页，0 error、0 undefined、0 Overfull。
- 目视抽查页：`t_p01`（章题、作者 `*` 注、脚注 1）、`t_p07`（引理 3.3 的直和与 `D^k\delta_0`）、`t_p10`（(3.13) 长链、(3.14) 的 pmatrix 及其后译注）、`t_p13`（命题 3.8 与高斯和）、`t_p15`（引理 4.1 的乘积分布）、`t_p20`（参考文献 [6]–[14]）。
- 与主编订正的对应：原以为正文止于 PDF 134，实为 PDF 114–136 = 印刷 109–131，故原「补译的印刷页 130–131」本就在章内，保留；三条带页码的译注来源改写成「原书 p.~120（PDF 125）」式，同时给出印刷页与真实 PDF 页。
- 留待主编决定的一点：全书统一用 chapter.section 编号，节标题显示「6.1–6.5」，而原书节号是 1–5、公式号也按 1–5 编（译文照原书编号，正文「第 5 节」等字样未改）。
