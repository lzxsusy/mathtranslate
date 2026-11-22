# -*- coding: utf-8 -*-
"""lbook04 资料卡数据（三）：第 9–11 章，GL_n 的 Langlands 纲领（轨 G）。

对应 Bernstein–Gelbart 编《朗兰兹纲领导论》中译注本：
  ch9  Cogdell, GL_n 的 L 函数解析理论       pp. 197–228
  ch10 Cogdell, GL_n 的 Langlands 猜想       pp. 229–249
  ch11 Cogdell, 对偶群与 Langlands 函子性    pp. 251–268
行号一律以 08_source_code/.../源码/chapters/chNN.tex 的实际行号为准。
"""

from base import card, src


CARDS_3 = [

    # =====================================================================
    # 第 9 章  GL_n 的 L 函数解析理论
    # =====================================================================
    card(
        "ch9-automorphic-representation",
        "G",
        r"$\mathrm{GL}_n$ 自守表示的解析理论",
        ["解析理论", "尖点自守表示", "Fourier 展开", "Whittaker 模型"],
        r"把 $\mathrm{GL}_n(\mathbb{A})$ 的尖点自守表示当作解析对象：用非交换 $N_n$ 上的 Whittaker 积分做 Fourier 展开，再由 Whittaker 泛函的唯一性得到整体 Euler 乘积与重数一。",
        r"为什么 $\mathrm{GL}_n$（$n\ge3$）的 Fourier 展开要沿棒状子群 $P_n$ 归纳，而不能像 $\mathrm{GL}_2$ 那样直接对 $N_n$ 积分？",
        r"本章的自守表示指 $\mathrm{GL}_n(\mathbb{A})$ 的光滑表示：每个局部分量 $K_v$-有限（阿基米德处不要求 $K_\infty$-有限），中心特征酉，且作为函数是尖点的——对每个单幂根群 $U$，$\int_{U(k)\backslash U(\mathbb{A})}\varphi(ug)\,du\equiv0$。尖点性给出速降，这是后面所有积分绝对收敛的根据。展开的技巧在于 $N_n$ 非交换（$n\ge3$）：取 $\psi(n)=\psi(x_{1,2}+\cdots+x_{n-1,n})$，定义 $W_\varphi(g)=\int_{N_n(k)\backslash N_n(\mathbb{A})}\varphi(ng)\psi^{-1}(n)\,dn$，则 $\varphi$ 可按 $\mathrm{GL}_{n-1}(k)$ 的双陪集展开为 Whittaker 函数之和（定理 1.1）。局部地，$\psi_v$-Whittaker 泛函至多一维（定理 1.2，Gelfand–Kazhdan 与 Shalika），这使整体 Whittaker 函数成为局部 Whittaker 函数之积 $W_\xi(g)=\prod_v W_{\xi_v}(g_v)$，Euler 积分才能逐位点分解，重数一定理也随之落地。",
        r"$\pi$：$\mathrm{GL}_n(\mathbb{A})$ 的不可约自守表示；$\psi$：$k\backslash\mathbb{A}$ 的非平凡加法特征；$N_n$：上三角单幂根群；$P_n=\mathrm{GL}_{n-1}\ltimes Y_n$：棒状子群（mirabolic），$Y_n\cong k^{n-1}$；$W_\varphi$：$\varphi$ 的 $\psi$-Whittaker 函数；$X(\pi)$：$\pi$ 的 Whittaker 渐近指数有限集。",
        [
            r"尖点性用单幂根积分定义，不依赖 $K_\infty$ 有限；它同时给出速降，是整套解析理论的入口。",
            r"$n\ge3$ 时 $N_n$ 非交换，Fourier 展开的归纳载体是棒状子群 $P_n$，而 $P_n\backslash\mathrm{GL}_n\cong k^n\setminus\{0\}$ 仍是齐性空间，展开并未变复杂。",
            r"Whittaker 泛函的唯一性（定理 1.2）是整章枢纽：它把整体的 $W$ 拆成局部的 $W_v$ 之积，Euler 乘积才可能。",
            r"由此得到重数一定理；强重数一则在 §4 用 $L$ 函数在 $s=1$ 的极点重述（定理 4.2 后的观察）。",
        ],
        [
            r"W_\varphi(g)=\int_{N_n(k)\backslash N_n(\mathbb{A})}\varphi(ng)\,\psi^{-1}(n)\,dn",
            r"\varphi(g)=\sum_{\gamma\in N_{n-1}(k)\backslash\mathrm{GL}_{n-1}(k)}W_\varphi\left(\begin{pmatrix}\gamma&0\\0&1\end{pmatrix}g\right)",
            r"W_\xi(g)=\prod_v W_{\xi_v}(g_v)",
        ],
        [
            r"把 $N_n$ 当成交换群：$n\ge3$ 时 $\psi$ 不是沿整个 $N_n$ 的「好」特征标，诱导必须从棒状子群 $P_n$ 出发；这就是定理 1.1 的求和跑遍 $N_{n-1}(k)\backslash\mathrm{GL}_{n-1}(k)$ 的原因。",
            r"把「光滑」误读为「$K_\infty$ 有限」：本章只要求局部 $K_v$-有限，阿基米德分量允许无限维 $K_\infty$-等型。",
        ],
        [
            {"type": "背景直觉", "title": "非交换 $N_n$ 反而好用", "text": r"若 $N_n$ 交换（如 $\mathrm{GL}_2$），Fourier 展开就是 $k$ 上的通常 Fourier 变换；$n\ge3$ 时 $N_n$ 非交换，但逐单根特征 $\psi$ 的稳定化子恰是 $P_n$，而 $P_n\backslash\mathrm{GL}_n\cong k^n\setminus\{0\}$，展开只是换到 $P_n$ 上做。§1.1 末的译注专门交代了 Gelfand–Kazhdan 与 Shalika 两条来源。"},
        ],
        ["ch9-godement-jacquet", "ch9-local-l-functions", "ch9-functional-equation"],
        [src(9, "§1", [198, 202], "ch09.tex:49-294")],
        theorems=[
            {"name": "定理 1.1（Fourier 展开）", "statement": r"$\varphi(g)=\sum_{\gamma\in N_{n-1}(k)\backslash\mathrm{GL}_{n-1}(k)}W_\varphi\big((\gamma,0;0,1)g\big)$，绝对收敛且在每个紧集上一致。", "source": "译文 §1.1"},
            {"name": "定理 1.2（Whittaker 泛函唯一性）", "statement": r"$\psi_v$-Whittaker 泛函空间至多一维（非阿基米德：Gelfand–Kazhdan；阿基米德：Shalika）。", "source": "译文 §1.2"},
        ],
    ),

    card(
        "ch9-godement-jacquet",
        "G",
        r"Godement–Jacquet 积分与主 $L$ 函数的位置",
        ["Godement–Jacquet zeta 积分", "主 L 函数", "L(s,π)", "Hecke 积分"],
        r"本章不展开 Godement–Jacquet 的矩阵系数积分，只把主 $L$ 函数 $L(s,\pi)$ 作为 $m=1$ 的 Rankin–Selberg 特例纳入统一框架：$L(s,\pi)=L(s,\pi\times\mathbf{1})$。",
        r"既然 Godement–Jacquet 积分已经定义了 $L(s,\pi)$，本章为什么还要另建一套 $\mathrm{GL}_n\times\mathrm{GL}_m$ 的积分？",
        r"Godement–Jacquet 的 zeta 积分是 $\mathrm{GL}_n$ 上主 $L$ 函数的标准来源：取 $\pi$ 的矩阵系数 $\beta$（或 Schwartz 函数），在 $\mathrm{GL}_n(k)Z_n(\mathbb{A})\backslash\mathrm{GL}_n(\mathbb{A})$ 上作 $Z(s)=\int\beta(g)|\det g|^s\,dg$，这些积分张成同一个分数理想，归一化生成元即 $L(s,\pi)$，配上 $\varepsilon(s,\pi,\psi)$ 便有函数方程。本章章首明确不重复这套构造（只管 $\pi\times\pi'$ 的 Rankin–Selberg 族），而把它当作 $m=1$ 的端点：$\pi'=\mathbf{1}$ 时记 $L(s,\pi)=L(s,\pi\times\mathbf{1})$（§3.1 定义处）。仍值得单独记一张卡，因为本章所有局部因子都由 Whittaker 积分定义，Godement–Jacquet 走的是矩阵系数路线，二者给出同一个 $L$ 函数正是「积分表示不唯一、$L$ 函数唯一」的第一个实例；第 10 章 §2 又直接用 Godement–Jacquet 理论给 $\mathrm{GL}_n$ 的 $L$ 函数作定义，所以这张卡是第 9、10 章之间的接口。",
        r"$\pi\in\mathcal{A}_n(k)$：$\mathrm{GL}_n(k)$ 的不可约容许表示（整体时指自守表示）；$\beta$：$\pi$ 的矩阵系数；$Z(s)$：zeta 积分；$f$：$\mathrm{GL}_2$ 的尖点形式，$\Lambda(s,f)$ 为其完备 $L$ 函数。",
        [
            r"本章的统一定义是「先有积分族、再取分数理想的生成元」，因此单个积分（有分歧时）并不等于 $L$ 函数，Godement–Jacquet 与 Rankin–Selberg 只是两族不同的积分。",
            r"$m=1$ 时 $\pi'=\mathbf{1}$，Rankin–Selberg 积分退化为对单个尖点形式的 Mellin 型积分；$n=1$ 时即 Hecke 的 $\Lambda(s,f)$，这就是「主 $L$ 函数是特例」的字面含义。",
            r"第 10 章 §2 用 Godement–Jacquet 理论 [24] 直接定义 $\mathrm{GL}_n$ 的 $L(s,\pi)$ 与 $\varepsilon(s,\pi,\psi)$，第 9 章则把同一对象作为 $\pi\times\mathbf{1}$ 处理；两处必须对得上。",
        ],
        [
            r"\Lambda(s,f)=(2\pi)^{-s}\Gamma(s)L(s,f)=\int_0^\infty f(iy)y^s\,d^\times y",
            r"L(s,\pi)=L(s,\pi\times\mathbf{1})",
        ],
        [
            r"把 $L(s,\pi\times\widetilde{\pi})$ 当作 $L(s,\pi)$ 的平方：它是对偶对的 Rankin–Selberg $L$ 函数，在 $s=1$ 有极点（内积的留数），不是主 $L$ 函数。",
            r"以为 Godement–Jacquet 与 Rankin–Selberg 给出两套不同的局部因子：它们只是同一个局部 $L$ 函数的两个积分表示。",
        ],
        [
            {"type": "背景直觉", "title": "为什么主 $L$ 函数反而是特例", "text": r"$\mathrm{GL}_2$ 的 $\Lambda(s,f)=\int_0^\infty f(iy)y^s\,d^\times y$ 是 Mellin 变换，$n=1$ 时就是 Hecke 的局部 zeta 积分；Godement–Jacquet 把「矩阵系数 × $|\det|^s$」推广到任意 $n$。本章取 $\pi'=\mathbf{1}$ 便退回这一端点，所以它虽未展开，却始终在框架之内。"},
        ],
        ["ch9-automorphic-representation", "ch9-local-l-functions", "ch10-local-langlands"],
        [
            src(9, "§0", [197, 197], "ch09.tex:37-39"),
            src(9, "§2", [202, 203], "ch09.tex:296-319"),
        ],
    ),

    card(
        "ch9-local-l-functions",
        "G",
        r"局部 $L$ 函数：分数理想与生成元",
        ["局部 L 因子", "分数理想", "Satake 参数", "Whittaker 积分"],
        r"非阿基米德局部域上，Whittaker 积分张成 $\mathbb{C}[q^s,q^{-s}]$ 的分数理想，其归一化生成元就是 $L(s,\pi\times\pi')$；无分歧时化为 $\det(1-q^{-s}A_\pi\otimes A_{\pi'})^{-1}$。",
        r"为什么局部 $L$ 函数要用「一族积分的生成元」来定义，而不能直接取某一个积分？",
        r"§3.1 的出发点是 $\Psi_j$ 一族积分：对 $\pi\in\mathcal{A}_n(k)$、$\pi'\in\mathcal{A}_m(k)$（酉、一般），在 $N_m(k)\backslash\mathrm{GL}_m(k)$ 上对 $W$、$W'$ 与矩阵坐标积分，$j=0,\dots,n-m-1$。三条推论先用 Whittaker 渐近 $W(a)=\sum_{X(\pi)}\chi_i(a)\phi_i(\alpha_1(a),\dots)$ 把收敛域（酉时 $\mathrm{Re}\,s\ge1$）、有理性（$q^{-s}$ 的有理函数）与公分母（只依赖 $X(\pi),X(\pi')$）固定下来，于是这些积分张成 $\mathbb{C}[q^s,q^{-s}]$ 的一个分数理想 $I(\pi,\pi')$。主理想整环中每个非零分数理想有唯一归一化生成元（$P(0)=1$），定义 $L(s,\pi\times\pi')=P_{\pi,\pi'}(q^{-s})^{-1}$；定理 3.1 断言这个生成元就是 $L$ 函数，最小性（$\Psi/L$ 整，891–901）说明 $L$ 由理想中函数的极点唯一确定。无分歧时 Shintani 显式 Whittaker 函数给出 $A_\pi=\mathrm{diag}(\mu_1(\varpi),\dots,\mu_n(\varpi))$ 与定理 3.3 的行列式公式；有分歧时单个积分只是 $L$ 的有理倍数，所以「取积分」与「取生成元」绝不能混。",
        r"$k$：非阿基米德局部域，$\mathfrak{o}$、$\mathfrak{p}$、$\varpi$、$q=|\mathfrak{o}/\mathfrak{p}|=|\varpi|^{-1}$；$\pi,\pi'$：酉、一般（generic）的不可约容许表示；$\Psi_j$：第 $j$ 个局部积分；$X(\pi)$：Whittaker 渐近的指数集；$A_\pi$：Satake 参数对角矩阵。",
        [
            r"三条推论（收敛域、有理性、公分母）是分数理想定义的前提；没有它们，$I(\pi,\pi')$ 只是形式记号。",
            r"$L$ 由理想定义而非由某个积分定义：有分歧时 $\Psi$ 只是 $L$ 的有理倍数，单个积分并不等于 $L$。",
            r"归一化 $P(0)=1$ 让生成元唯一，从而 $\varepsilon$ 是单项式 $cq^{-f(\pi)s}$，$f(\pi)$ 就是导子。",
            r"无分歧情形定理 3.3 把 $L$ 写成 $\det(I-q^{-s}A_\pi\otimes A_{\pi'})^{-1}$，并可取 $W_o(e)=1$ 的显式 Whittaker 函数验证；这也是第 10 章 Satake 参数的解析出处。",
        ],
        [
            r"I(\pi,\pi')=\Bigl\{\sum_i\Psi(s;W_i,W_i')\Bigr\}\subset\mathbb{C}[q^s,q^{-s}]",
            r"L(s,\pi\times\pi')=P_{\pi,\pi'}(q^{-s})^{-1},\qquad P_{\pi,\pi'}(0)=1",
            r"L(s,\pi\times\pi')=\det\bigl(I-q^{-s}A_\pi\otimes A_{\pi'}\bigr)^{-1}\qquad(\pi,\pi'\ \text{无分歧})",
        ],
        [
            r"把 $\Psi(s;W,W')$ 直接当作 $L$：它只是理想中的一个元素；只有 $\pi,\pi'$ 都无分歧且取 $W_o$ 时才恰好相等（定理 3.3）。",
            r"忘记 $\pi,\pi'$ 需一般（generic）：没有 Whittaker 模型，$\Psi_j$ 无从定义；§1.2 已说明 GL_n 上一般性的位置。",
        ],
        [
            {"type": "含糊点拨", "title": "分数理想不是商", "text": r"$I(\pi,\pi')$ 是 $\mathbb{C}[q^s,q^{-s}]$ 的分数理想，不是两个函数之商；两个不同的积分族可以生成同一个理想——这正是「换积分表示不换 $L$ 函数」的技术含义。§3.1 末的译注特别提醒：初学者常把「理想相等」误读成「函数相等」。"},
        ],
        ["ch9-godement-jacquet", "ch9-functional-equation", "ch9-automorphic-representation"],
        [src(9, "§3.1", [211, 215], "ch09.tex:796-1031")],
        theorems=[
            {"name": "定理 3.1（局部 $L$ 因子的定义）", "statement": r"局部积分族构成分数理想 $I(\pi,\pi')$，其归一化生成元即 $L(s,\pi\times\pi')$。", "source": "译文 §3.1"},
            {"name": "定理 3.3（无分歧情形）", "statement": r"若 $\pi,\pi'$ 无分歧，则 $L(s,\pi\times\pi')=\det(1-q^{-s}A_\pi\otimes A_{\pi'})^{-1}$，且 $\varepsilon\equiv1$。", "source": "译文 §3.1"},
        ],
    ),

    card(
        "ch9-functional-equation",
        "G",
        r"函数方程与 $\varepsilon$ 因子",
        ["局部函数方程", "gamma 因子", "epsilon 因子", "导子"],
        r"局部积分满足带 $\gamma$ 因子的函数方程，除以 $L$ 后剩下单项式 $\varepsilon=cq^{-f(\pi)s}$；把各局部方程相乘，$\gamma$ 与 $L$ 相消，即得整体函数方程。",
        r"整体函数方程里的 $\varepsilon$ 因子为什么是有限乘积，而不是无限乘积？",
        r"局部函数方程（定理 3.2）对 $m<n$ 写成 $\widetilde{\Psi}(1-s;\rho(w_{n,m})\widetilde{W},\widetilde{W}')=\omega'(-1)^{n-1}\gamma(s,\pi\times\pi',\psi)\Psi(s;W,W')$，对 $m=n$ 则多带一个 $\widehat{\Phi}$。$\gamma$ 是 $q^{-s}$ 的有理函数，依赖 $\psi$；把 $L$ 除掉，定义 $\varepsilon=\gamma L(s,\pi\times\pi')/L(1-s,\widetilde{\pi}\times\widetilde{\pi}')$，则 $\varepsilon$ 是单项式 $cq^{-f(\pi)s}$，且归一化后的函数方程只含 $L$ 与 $\varepsilon$（955–968）。整体层面（§4）把各局部 $\varepsilon_v$ 相乘：除有限个分歧位点外 $\varepsilon_v\equiv1$，故 $\varepsilon$ 是有限乘积；再把局部函数方程逐位点相乘，每个 $\gamma_v$ 与 $L_v$ 相消，只剩 $\prod\varepsilon_v$，得到定理 4.1 的 $L(s,\pi\times\pi')=\varepsilon(s,\pi\times\pi')L(1-s,\widetilde{\pi}\times\widetilde{\pi}')$。1016–1031 的超尖点情形与 1033–1059 的 $\gamma$ 乘性、稳定性，是把这个机制推广到一般表示的工具。",
        r"$\gamma(s,\pi\times\pi',\psi)$：局部积分方程的系数；$\varepsilon(s,\pi\times\pi',\psi)$：去掉 $L$ 后的不变量；$f(\pi)$：导子（conductor），非负整数，$f(\pi)=0$ 当且仅当 $\pi$ 无分歧；$\omega'$：$\pi'$ 的中心特征；$w_{n,m}=\mathrm{diag}(I_m,w_{n-m})$。",
        [
            r"$\gamma$ 依赖加法特征 $\psi$，$\varepsilon$ 与 $L$ 的比值不依赖；换 $\psi$ 只把 $\gamma$ 乘一个一次因子。",
            r"$\varepsilon$ 的单项式性是归一化 $P(0)=1$ 的直接后果；$f(\pi)$ 就是导子，$f(\pi)=0$ 刻画无分歧。",
            r"整体函数方程的证明是纯形式相乘：每个 $v$ 的局部方程中 $\gamma_v$ 与 $L_v$ 相消，只剩 $\prod_v\varepsilon_v$；$\omega'_v(-1)^{n-1}$ 只在分歧的非阿基米德位点可能为 $-1$，不改变 $\varepsilon$ 的形状。",
            r"超尖点情形 $L\equiv1$（$m<n$）或 $L$ 是显式几何级数之积（$m=n$，定理 3.4），是检验公式的最简例子。",
        ],
        [
            r"\widetilde{\Psi}(1-s;\rho(w_{n,m})\widetilde{W},\widetilde{W}')=\omega'(-1)^{n-1}\gamma(s,\pi\times\pi',\psi)\,\Psi(s;W,W')",
            r"\varepsilon(s,\pi\times\pi',\psi)=\gamma(s,\pi\times\pi',\psi)\,\frac{L(s,\pi\times\pi')}{L(1-s,\widetilde{\pi}\times\widetilde{\pi}')}",
            r"L(s,\pi\times\pi')=\varepsilon(s,\pi\times\pi')\,L(1-s,\widetilde{\pi}\times\widetilde{\pi}')",
        ],
        [
            r"把对偶表示写成复共轭：$\widetilde{\pi}$ 是 contragredient，$\ell$ 进情形还须先取 $\overline{\mathbb{Q}}_\ell$ 对偶再经 $\iota$ 与复表示比较；函数方程右边必须是 $\widetilde{\pi}\times\widetilde{\pi}'$。",
            r"把整体 $\varepsilon$ 写成无限乘积：几乎处处 $\varepsilon_v\equiv1$，它实际上是有限乘积（1205–1206）。",
        ],
        [
            {"type": "易错预警", "title": r"$\gamma$ 与 $\varepsilon$ 的分工", "text": r"$\gamma$ 是局部积分方程的系数，本身依赖 $\psi$ 且不是单项式；$\varepsilon$ 才是去掉 $L$ 之后的不变量。文献里常把两者混称，读公式时先看它是否带 $L$ 的比值。"},
        ],
        ["ch9-local-l-functions", "ch9-automorphic-representation", "ch9-langlands-spectral"],
        [
            src(9, "§3.2", [215, 218], "ch09.tex:934-1130"),
            src(9, "§4", [218, 222], "ch09.tex:1182-1303"),
        ],
        theorems=[
            {"name": "定理 3.2（局部函数方程）", "statement": r"存在 $\gamma(s,\pi\times\pi',\psi)\in\mathbb{C}(q^{-s})$ 使 $\widetilde{\Psi}(1-s;\rho(w_{n,m})\widetilde{W},\widetilde{W}')=\omega'(-1)^{n-1}\gamma(s,\pi\times\pi',\psi)\Psi(s;W,W')$。", "source": "译文 §3.2"},
            {"name": "定理 4.1（整体函数方程）", "statement": r"$L(s,\pi\times\pi')$ 亚纯延拓、竖带有界，且 $L(s,\pi\times\pi')=\varepsilon(s,\pi\times\pi')L(1-s,\widetilde{\pi}\times\widetilde{\pi}')$。", "source": "译文 §4"},
        ],
    ),

    card(
        "ch9-langlands-spectral",
        "G",
        r"Langlands 谱问题：Eisenstein 级数与逆定理",
        ["Eisenstein 级数", "谱理论", "逆定理", "留数配对"],
        r"$m=n$ 的积分需要第三函数——由 Schwartz 函数造的 Eisenstein 级数；其留数给出不变配对与非零性条件，逆定理则把「好」的扭 $L$ 函数反解为自守性。",
        r"为什么 $m=n$ 的 Rankin–Selberg 积分必须引入 Eisenstein 级数，而不能直接用两个尖点形式的 $L^2$ 内积？",
        r"$m=n$ 时 $\int_{\mathrm{GL}_n(k)\backslash\mathrm{GL}_n(\mathbb{A})}\varphi\varphi'|\det g|^s\,dg$ 本质是 $L^2$ 内积，只在 $s$ 的特定值收敛，不能定义 $L$ 函数（608–617），但它的留数会以「内积」的形式重新出现。正确的做法是引入第三函数：取 $\Phi\in\mathcal{S}(\mathbb{A}^n)$、酉 idèle 类特征 $\eta$，令 $F(g,\Phi;s,\eta)=|\det g|^s\int_{\mathbb{A}^\times}\Phi(ae_ng)|a|^{ns}\eta(a)\,d^\times a$，再对 $P'_n(k)\backslash\mathrm{GL}_n(k)$（$P'_n=Z_nP_n$，分拆 $(n-1,1)$）求和得 Eisenstein 级数 $E$。用 Poisson 求和（通过 Theta 级数 $\Theta_\Phi(a,g)=\sum_{\xi\in k^n}\Phi(a\xi g)$）证 $E$ 亚纯、竖带有界、满足 $E(g,\Phi;s,\eta)=E(g^\iota,\widehat{\Phi};1-s,\eta^{-1})$，极点只可能在 $s=-i\sigma,1-i\sigma$。于是三重积分 $I(s;\varphi,\varphi',\Phi)$ 的留数给出 $\mathrm{GL}_n(\mathbb{A})$-不变配对；配对非零迫使 $\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}$，这就是定理 2.2。§5 的逆定理把同一机制反过来用：先假定一切扭 $L$ 函数「好」（整、竖带有界、标准函数方程），反解 Whittaker 函数，证明 $\Pi$ 拟自守——这正是 Hecke 逆定理在 $\mathrm{GL}_n$ 上的推广。",
        r"$P_n$：棒状子群，$P_n\backslash\mathrm{GL}_n\cong k^n\setminus\{0\}$；$P'_n=Z_nP_n$：分拆 $(n-1,1)$ 的抛物子群；$\eta$：酉 idèle 类特征；$\Theta_\Phi$：Theta 级数；$\mathcal{T}(S;m)=\bigcup_{d=1}^m\mathcal{A}_0^S(d)$：用 $S$ 外无分歧的尖点表示作扭的集合。",
        [
            r"$F$ 是 $\mathrm{Ind}_{P'_n}^{\mathrm{GL}_n}(\delta^{s-1/2}\eta)$ 的光滑截面，$E$ 是它的级数；两者不可混。",
            r"Poisson 求和（Theta 表示）是解析延拓与函数方程的唯一入口；没有它，$E$ 只在 $\mathrm{Re}\,s>1$ 收敛。",
            r"留数非零 $\Rightarrow$ 存在 $\mathrm{GL}_n(\mathbb{A})$-不变配对 $\Rightarrow$ $\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}$；反过来该条件也保证 $s=1$ 处有极点（定理 4.2 后的两条观察）。",
            r"逆定理只需 $\pi'$ 跑遍 $\mathcal{T}(S;n-1)$（定理 5.1）；用 $\mathcal{T}(S;n-2)$ 可减弱假设（定理 5.2），类数一时还有 5.3 的细化。",
        ],
        [
            r"F(g,\Phi;s,\eta)=|\det g|^s\int_{\mathbb{A}^\times}\Phi(ae_ng)|a|^{ns}\eta(a)\,d^\times a",
            r"E(g,\Phi;s,\eta)=\sum_{\gamma\in P'_n(k)\backslash\mathrm{GL}_n(k)}F(\gamma g,\Phi;s,\eta)",
            r"E(g,\Phi;s,\eta)=E(g^\iota,\widehat{\Phi};1-s,\eta^{-1})",
            r"\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}",
        ],
        [
            r"把 Eisenstein 级数的解析性质当成「显然」：没有 Poisson 求和就得不到函数方程，$E$ 只在右半平面有定义。",
            r"以为「好」只要函数方程：逆定理要求整性、竖带有界、标准函数方程三条同时成立，缺一不可。",
            r"把 §2.3 的留数配对与 §2.2 的 $P_n$ 投影混淆：前者作用于两个尖点形式（三重积分），后者作用于一个函数再与另一个配对。",
        ],
        [
            {"type": "背景直觉", "title": "谱理论为什么在这里出现", "text": r"$m=n$ 时 $L^2$ 内积本身就是 $L$ 函数在 $s=1$ 的留数，无法提供新信息；Eisenstein 级数把「两两配对」提升为「三重积分」，其留数才携带 $\pi$ 与 $\pi'$ 的耦合。§5 末尾把这套论证称为 Langlands 谱理论的弱形式。"},
        ],
        ["ch9-functional-equation", "ch9-automorphic-representation", "ch9-godement-jacquet"],
        [
            src(9, "§2.3", [206, 211], "ch09.tex:601-784"),
            src(9, "§5", [222, 225], "ch09.tex:1406-1588"),
        ],
        theorems=[
            {"name": "定理 2.2（$m=n$ 的积分）", "statement": r"$I(s;\varphi,\varphi',\Phi)$ 亚纯、竖带有界；极点全为单极点，且仅当 $\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}$ 时在 $s=-i\sigma,1-i\sigma$ 出现；满足函数方程，可分解时等于 Euler 乘积。", "source": "译文 §2.3"},
            {"name": "定理 5.1（逆定理）", "statement": r"若 $\Pi$ 对一切 $\pi'\in\mathcal{T}(S;n-1)$ 都「好」，则 $\Pi$ 拟自守；$S=\varnothing$ 时 $\Pi$ 本身是尖点自守表示。", "source": "译文 §5"},
        ],
    ),

    # =====================================================================
    # 第 10 章  GL_n 的 Langlands 猜想
    # =====================================================================
    card(
        "ch10-weil-deligne",
        "G",
        r"Weil–Deligne 群与 Frobenius 半单化",
        ["W'_k", "Frobenius 半单化", "局部 L 因子", "(rho,N) 表示"],
        r"局部 Weil–Deligne 群 $W'_k=W_k\rtimes\mathbb{G}_a$ 的表示等价于 $(\rho,N)$，且 $\rho(w)N\rho(w)^{-1}=\|w\|N$；半单化后局部因子只看 $(\ker N)^{\rho(I)}$ 上的 $\det(1-t\rho(\Phi))$。",
        r"为什么局部 $L$ 因子要用 $(\ker N)^{\rho(I)}$ 而不是惯性不变子空间 $V^I$？",
        r"局部 Langlands 猜想的 Galois 侧不是 $\mathcal{G}_k$ 而是 Weil–Deligne 群 $W'_k=W_k\rtimes\mathbb{G}_a$（Deligne）。$W'_k$ 的表示与「$(\rho,N)$：$\rho$ 是 $W_k$ 的表示，$N$ 幂幺，且 $\rho(w)N\rho(w)^{-1}=\|w\|N$」等价；不可约时 $N=0$，故 Frobenius 半单表示就是 $W_k$ 的半单表示。一般情形取唯一的幂幺 $u$ 使 $\rho u^{-v}$ 半单，半单化 $\rho'_{\mathrm{ss}}=(\rho u^{-v},N)$；局部因子定义为 $Z(t,V)=\det(1-t\rho(\Phi)|_{V_N^I})^{-1}$，其中 $V_N^I=(\ker N)^{\rho(I)}$，再令 $L(s,\rho')=Z(q^{-s},\rho')$。阿基米德域没有 $W'_k$（没有 $\mathbb{G}_a$ 部分），约定 $W'_k=W_k$；$W_{\mathbb{R}}$ 是 $\mathbb{C}^\times$ 与 $j\mathbb{C}^\times$ 的并，$jcj^{-1}=\bar c$、$j^2=-1$，它不是 $\mathbb{C}^\times\times\mathbb{Z}/2$ 的直积。",
        r"$W_k$：Weil 群；$I$：惯性群；$\Phi$：几何 Frobenius；$\|\cdot\|$：$\|w\|=q^{-v(w)}$，$v$ 为赋值；$\rho,N$：$W'_k$ 表示的半单部分与幂幺部分；$u$：唯一的幂幺元素使 $\rho u^{-v}$ 半单；$Z(t,V)$：局部 zeta 函数。",
        [
            r"交叉项必须是 $x_1+\|w_1\|x_2$：若写成 $x_1+x_2$，结合律失效（§1 的译注专门验算过）。",
            r"半单化只改 $\rho$，不改 $N$；不可约表示自动 $N=0$，此时「Frobenius 半单」与「$\rho$ 半单」一致。",
            r"局部因子只取 $(\ker N)^{\rho(I)}$ 上 $\Phi$ 的作用；$N\ne0$ 时若误用 $V^I$ 会多出因子（Steinberg 例 $\omega\otimes\mathrm{Sp}(2)$）。",
            r"整体 $L(s,\rho)=\prod_vL(s,\rho_v)$、$\varepsilon(s,\rho)=\prod_v\varepsilon(s,\rho_v,\psi_v)$，三条良好性质与 Artin $L$ 函数一致。",
        ],
        [
            r"(w_1,x_1)(w_2,x_2)=(w_1w_2,\;x_1+\|w_1\|x_2)",
            r"\rho(w)N\rho(w)^{-1}=\|w\|N",
            r"Z(t,V)=\det\bigl(1-t\rho(\Phi)\big|_{V_N^I}\bigr)^{-1},\qquad V_N^I=(\ker N)^{\rho(I)}",
            r"L(s,\rho')=Z(q^{-s},\rho')",
        ],
        [
            r"把 $V_N^I$ 写成 $V^I$：$N\ne0$ 时 $(\ker N)^{\rho(I)}$ 严格小于 $V^{\rho(I)}$，局部因子会多算。",
            r"把 $W_{\mathbb{R}}$ 当成 $\mathbb{C}^\times\times\mathrm{Gal}(\mathbb{C}/\mathbb{R})$ 的直积：正合列 $1\to\mathbb{C}^\times\to W_{\mathbb{R}}\to\mathrm{Gal}\to1$ 不分裂，$j$ 的作用是共轭。",
        ],
        [
            {"type": "易错预警", "title": r"两个 $\Phi$", "text": r"本章的 $\Phi$ 是几何 Frobenius；第 11 章的 $\Phi(G)$ 是容许同态集。原书在 p. 254 专门提醒不要把两者混读，中译注也在第 11 章 §2 再次点明。"},
        ],
        ["ch10-local-langlands", "ch10-global-function-field", "ch9-functional-equation"],
        [src(10, "§1", [230, 233], "ch10.tex:55-204")],
        theorems=[
            {"name": "局部因子的定义", "statement": r"$L(s,\rho')=Z(q^{-s},\rho')$，$Z(t,V)=\det(1-t\rho(\Phi)|_{V_N^I})^{-1}$；$N=0$ 时 $\varepsilon$ 即 Artin–Weil 因子。", "source": "译文 §1"},
        ],
    ),

    card(
        "ch10-local-langlands",
        "G",
        r"局部 Langlands 猜想：两种表述",
        ["局部对应", "猜想 I", "猜想 II", "L 包", "Frobenius 半单表示"],
        r"猜想 I 断言 Frobenius 半单的 $n$ 维 $W'_k$ 表示与 $\mathrm{GL}_n(k)$ 的不可约容许表示一一对应；猜想 II 追加归一化与 $L/\varepsilon$ 匹配，把几何 Frobenius 与一致化子对齐。",
        r"猜想 I 与猜想 II 的差别究竟在哪里，为什么需要两次陈述？",
        r"局部猜想 I：存在双射 $\mathrm{Rep}_n(W'_k)\leftrightarrow\mathcal{A}_n(k)$，$\rho\mapsto\pi_\rho$，满足 (i) $n=1$ 时即局部类域论；(ii) 中心特征与 $\det$ 对应；(iii) 扭相容 $\rho_{\pi\otimes\chi}=\rho\otimes\chi$；(iv) $\pi_\rho$ 平方可积当且仅当 $\rho(W'_k)$ 不在任何真 Levi 中；(v) 缓增当且仅当 $\rho(W_k)$ 有界；(vi) 与 $H(k)\to\mathrm{GL}_n(k)$ 相容。猜想 II 换成 $\mathcal{A}_n(k)\to\mathrm{Rep}_n(W'_k)$，追加归一化 (i) 一致化子 $\leftrightarrow$ 几何 Frobenius，以及 (ii) $L(s,\rho_\pi\otimes\rho_{\pi'})=L(s,\pi\times\pi')$、$\varepsilon$ 同。$\mathrm{GL}_n$ 时容许同态 $\Phi(\mathrm{GL}_n)$ 就是 Frobenius 半单的 $n$ 维复表示，故两个猜想在「集合层面」等价，差别只在 $L/\varepsilon$ 是否逐项相等——而这正是与第 9 章解析理论对接的地方。",
        r"$\mathcal{A}_n(k)$：$\mathrm{GL}_n(k)$ 的不可约容许表示（整体时指自守表示）；$\mathrm{Rep}_n(W'_k)$：$W'_k$ 的 $n$ 维 Frobenius 半单表示；$\Phi$：几何 Frobenius；$\omega^s$：$\omega^s(w)=\|w\|^{-s}$；$\rho_\pi$：$\pi$ 的参数。",
        [
            r"(iv) 必须用 $\rho(W'_k)$ 而不是 $\rho(W_k)$：Steinberg 表示的 $\rho(W_k)$ 像落在对角环面（真 Levi），但 $W'_k$ 的像含 $N$，Zariski 闭包不落在真 Levi。",
            r"猜想 II 的归一化是定标点：把几何 Frobenius 与一致化子对齐；若改用算术 Frobenius，整体要扭 $\omega^s$，定理 3.2/3.3 的陈述都得改写。",
            r"(vi) 与函子性直接相关：它保证扭、诱导等操作与对应相容，也是第 11 章函子性预言的局部依据。",
            r"$\mathrm{GL}_2$ 情形 Deligne 已完整证明；一般 $n$ 见定理 3.2（正特征，LRS）与定理 3.3（特征零，Harris–Taylor、Henniart）。",
        ],
        [
            r"\mathrm{Rep}_n(W'_k)\;\longleftrightarrow\;\mathcal{A}_n(k)",
            r"L(s,\rho_\pi\otimes\rho_{\pi'})=L(s,\pi\times\pi')",
            r"\pi_\rho\ \text{平方可积}\iff\rho(W'_k)\not\subset M(k)\quad(\text{任意真 Levi }M)",
        ],
        [
            r"把 (iv) 的判据套在 $\rho(W_k)$ 上：会误判 Steinberg 表示不是平方可积。",
            r"把猜想 I 与 II 当成同一个猜想：I 只要求集合双射与定性性质，II 还要求与解析定义的 $L/\varepsilon$ 因子逐点相等。",
        ],
        [
            {"type": "背景直觉", "title": "两种解读", "text": r"同一猜想既可读作「非 Abel 类域论」（$n=1$ 的推广），也可读作「$\mathcal{A}_n(k)$ 的算术分类」；前者强调 $W'_k\to\mathrm{GL}_n(\mathbb{C})$ 的像，后者强调每个 $\pi$ 都有 Frobenius 半单参数。原书把这两种读法并列，中译注在 §3 末作了区分。"},
        ],
        ["ch10-weil-deligne", "ch10-henniart", "ch11-lgroup-reps"],
        [src(10, "§3", [234, 237], "ch10.tex:290-371")],
        theorems=[
            {"name": "猜想 I", "statement": r"存在双射 $\mathrm{Rep}_n(W'_k)\leftrightarrow\mathcal{A}_n(k)$ 满足 (i)–(vi)，其中 (iv) 用 $\rho(W'_k)$ 判平方可积、(v) 用 $\rho(W_k)$ 判缓增。", "source": "译文 §3"},
            {"name": "局部猜想 II", "statement": r"存在双射 $\mathcal{A}_n(k)\to\mathrm{Rep}_n(W'_k)$，归一化使一致化子对应几何 Frobenius，并使 $L(s,\rho_\pi\otimes\rho_{\pi'})=L(s,\pi\times\pi')$、$\varepsilon$ 逐项相等。", "source": "译文 §3"},
        ],
    ),

    card(
        "ch10-henniart",
        "G",
        r"局部对应的四步约化与 Henniart 的结果",
        ["局部逆定理", "数值局部 Langlands", "Henniart", "Harris–Taylor", "LRS"],
        r"证明局部 LL 分四步：$L$ 函数在 $s=0$ 的极点给单射，导子指数做数值比对，$\varepsilon$ 因子逆定理给唯一性，LRS、Harris–Taylor 或 Henniart 给存在性。",
        r"为什么「数值局部 Langlands」与「$\varepsilon$ 因子逆定理」两步合起来就能把对应逼成唯一的？",
        r"局部对应的证明被拆成四步。(1) 单射：由 $L(s,\rho\otimes\rho')$ 在 $s=0$ 有极点当且仅当 $\rho'\cong\widetilde{\rho}$，以及 $\pi$ 侧对应的极点判据，任何满足猜想 II (ii) 的对应自动单射。(2) 数值：Artin 导子指数 $a(\rho)$ 与 JPSS 导子 $f(\pi)$ 相等，且每个 $(m,\mu)$ 层的表示个数相等，$|\mathrm{Rep}_n^0(\mathcal{G}_k)_{m,\mu}|=|\mathcal{A}_n^0(k)_{m,\mu}|$（Henniart 1988）；这一步只给「数个数」，不给映射。(3) 唯一性：$\varepsilon$ 因子逆定理——若对一切 $1\le m\le n-1$ 与 $\tau\in\mathcal{A}_m^0(k)$ 有 $\varepsilon(s,\pi\times\tau,\psi)=\varepsilon(s,\pi'\times\tau,\psi)$，则 $\pi\cong\pi'$；此时相应扭 $L$ 函数恒 $1$，故只需比对 $\varepsilon$。(4) 存在性：LRS 在正特征用 $\mathcal{D}$-椭圆模空间的上同调；Harris–Taylor 在特征零用 Kottwitz 酉群的简单 Shimura 簇，得到 $\pi\otimes JL(\pi)\otimes\rho_\pi$ 作用于 $\mathrm{GL}_n(k)\times D_n^\times(k)\times W_k$；Henniart 用 Brauer 归纳把 $\rho$ 写成单项表示之和，经局部类域论提升与整体自守诱导，证明更短但无几何实现。",
        r"$a(\rho)$：Artin 导子指数；$f(\pi)$：JPSS 导子指数；$\mathcal{A}_n^0(k)$：超尖点表示集；$\mathcal{D}$：$\mathrm{GL}_n$ 上的中心除代数；$JL$：局部 Jacquet–Langlands 对应；$\iota$：$\overline{\mathbb{Q}}_\ell\to\mathbb{C}$。",
        [
            r"四步分工：单射与唯一性把「已知的 $L/\varepsilon$」用足，数值步把「未知的对应」数清楚，存在性才是真正的构造。",
            r"数值 LL 的计数按 $(m,\mu)$ 分层，$m$ 是导子指数、$\mu$ 与中心特征的幂零部分有关；层的划分必须与两边各自的定义一致。",
            r"Harris–Taylor 的构造同时给出局部 LL 与局部 Jacquet–Langlands：$\pi$、$JL(\pi)$、$\rho_\pi$ 出现在同一个上同调里。",
            r"Henniart 的 Brauer 归纳路线依赖 $n=1$（局部类域论）与整体自守诱导的弱情形，是「解析化」的证明，不含几何实现。",
        ],
        [
            r"L(s,\rho\otimes\rho')\ \text{在}\ s=0\ \text{有极点}\iff\rho'\cong\widetilde{\rho}",
            r"a(\rho)=f(\pi)",
            r"\varepsilon(s,\pi\times\tau,\psi)=\varepsilon(s,\pi'\times\tau,\psi)\ \ (\forall\,1\le m\le n-1,\ \tau\in\mathcal{A}_m^0(k))\ \Longrightarrow\ \pi\cong\pi'",
        ],
        [
            r"把数值相等当成对应存在：它只保证两边计数相同，不给出映射。",
            r"把「扭 $L$ 恒 $1$」误解为「所有扭都消失」：消失的是 $L$，$\varepsilon$ 仍在，且其单项式性使逐位点比对成为可能。",
            r"原书 p. 237 两处 Henniart 引文编号 $[28]$ 与 $[30]$ 互换：1988 数值 LL 是 $[28]$，2000 简化证明是 $[30]$。",
        ],
        [
            {"type": "含糊点拨", "title": "为什么 $\varepsilon$ 逆定理够用", "text": r"对应若存在，扭 $L$ 函数 $L(s,\pi\times\tau)$ 对一切 $\tau$ 都由第 9 章的解析理论已知，比对 $\varepsilon$ 就等价于比对整个局部因子。Piatetski-Shapiro 的逆定理正是这个逻辑的局部版。"},
        ],
        ["ch10-local-langlands", "ch9-functional-equation", "ch10-global-function-field"],
        [src(10, "§3.2", [237, 240], "ch10.tex:395-539")],
        theorems=[
            {"name": "定理 3.2（正特征）", "statement": r"存在双射 $\mathcal{A}_n^0(k)_f\to\mathrm{Rep}_n^0(\mathcal{G}_k)$，$\pi\mapsto\rho_\pi$，满足 (i)–(v)（LRS）。", "source": "译文 §3.2"},
            {"name": "定理 3.3（特征零）", "statement": r"同一双射在特征零成立（Harris–Taylor；Henniart）。", "source": "译文 §3.2"},
        ],
    ),

    card(
        "ch10-global-function-field",
        "G",
        r"整体 Langlands 猜想（函数域）：Satake 参数与特征值",
        ["整体对应", "Satake 参数", "shtuka", "Lafforgue", "Ramanujan–Petersson"],
        r"函数域上整体对应由「几乎所有点的 Hecke 特征值 = Frobenius 特征值」唯一确定；Lafforgue 用 shtuka 上同调实现，$L$ 函数相等与特征值相等等价。",
        r"为什么整体对应只需比较几乎所有点的特征值，而不必逐点指定？",
        r"函数域上，整体对应是一个双射 $\mathcal{A}_n^0(k;\overline{\mathbb{Q}}_\ell)_f\to\mathrm{Rep}_n^0(\mathcal{G}_k;\overline{\mathbb{Q}}_\ell)_f$，性质 (i)–(vi) 中最关键的是与局部对应的相容性。给定 $\pi$，几乎所有点 $x$ 处 $\pi_x$ 无分歧，有 Satake 类 $A_{\pi_x}$（共轭类）与 Hecke 特征值 $z_1(\pi_x),\dots,z_n(\pi_x)$；给定 $\rho$，同样有 Frobenius 共轭类 $\rho(\Phi_x)$ 与特征值 $z_i(\rho_x)$。整体猜想断言这两组数几乎处处相等；Chebotarev 保证 Frobenius 共轭类决定 $\rho$，强重数一保证 Hecke 特征值决定 $\pi$。定理 4.1 把这件事凝成「存在唯一双射使 $\{z_i(\pi_x)\}=\{z_i(\rho_{\pi,x})\}$ 对几乎所有 $x$ 成立」，等价于 $L^S(s,\pi)=L^S(s,\rho_\pi)$；定理 4.2（Piatetski-Shapiro–Deligne 归纳）说明只需几乎所有 $x$ 即可。Lafforgue 的证明用 shtuka：双陪集 $\mathrm{GL}_n(k)\backslash\mathrm{GL}_n(\mathbb{A})/\mathrm{GL}_n(\mathcal{O})$ 只参数化秩 $n$ 向量丛，而 shtuka 叠 $\mathcal{V}$ 的 Frobenius 两腿让 Hecke 对应几何化；在 $H^*_c(\bar k\otimes_k\mathcal{V};\overline{\mathbb{Q}}_\ell)$ 上，几何 Grothendieck–Lefschetz 与 Arthur–Selberg 迹公式给出 $\pi\otimes\rho_\pi\otimes\widetilde{\rho}_\pi$。",
        r"$x$：$k$ 的位点；$A_{\pi_x}$：Satake 类；$z_i(\pi_x)$：Hecke 特征值；$\Phi_x$：$x$ 处的几何 Frobenius；$z_i(\rho_x)$：Frobenius 特征值；$S(\pi)$、$S(\rho)$：分歧位点集；$\mathcal{V}$：shtuka 叠。",
        [
            r"Satake 参数是局部–整体的接口：$A_{\pi_x}$ 的特征值是 Hecke 算子 $T_x$ 的特征值，$\rho(\Phi_x)$ 的特征值是 Frobenius 的特征值，猜想说二者相等。",
            r"定理 4.1 的等价形式是 $L^S(s,\pi)=L^S(s,\rho_\pi)$；由局部因子决定特征值，函数方程与 $\varepsilon$ 的局部分解再把分歧集 $S(\pi)=S(\rho_\pi)$ 升级。",
            r"定理 4.3 是 Ramanujan–Petersson：$|z_i(\pi_x)|=1$；定理 4.4 是 Deligne 的权 $0$ 纯性，二者都由几何/上同调方法给出，是「纯性 ⇒ Ramanujan」的现代形式。",
            r"特征 $p$ 的证明不经过模空间，而经过 shtuka 的上同调；这是几何 Langlands 的起点。",
        ],
        [
            r"\{z_i(\pi_x)\}=\{z_i(\rho_{\pi,x})\}\quad\text{对几乎所有 }x",
            r"L^S(s,\pi)=L^S(s,\rho_\pi)",
            r"\det\bigl(1-t\rho_\pi(\Phi_x)\bigr)^{-1}=\prod_{i=1}^{n}(1-z_i(\pi_x)t)^{-1}",
        ],
        [
            r"把双陪集当成本质：$\mathrm{GL}_n(k)\backslash\mathrm{GL}_n(\mathbb{A})/\mathrm{GL}_n(\mathcal{O})$ 只给出向量丛的同构类，Hecke 算子的几何化需要 shtuka 的 Frobenius 结构。",
            r"以为需要「所有 $x$」：定理 4.2 说明几乎所有即可，剩下的由函数方程与 $\varepsilon$ 的局部分解补上。",
            r"把 $z_i(\pi_x)$ 与 $z_i(\rho_x)$ 逐一下标对齐：它们只在集合意义下相等，单个特征值的配对依赖 Satake 参数的选择。",
        ],
        [
            {"type": "背景直觉", "title": "为什么是 shtuka 而不是模空间", "text": r"数域上用 Shimura 簇，因为 $\mathrm{GL}_n$ 在数域上没有自然模空间（原书 §4.2 明说）；函数域上向量丛的模叠给出几何对象，shtuka 的 Frobenius 把 Hecke 算子变成对应上的推前，于是迹公式可以在上同调上算。"},
        ],
        ["ch10-local-langlands", "ch10-global-number-field", "ch10-weil-deligne"],
        [src(10, "§4.1", [241, 244], "ch10.tex:566-740")],
        theorems=[
            {"name": "定理 4.1（整体对应）", "statement": r"存在唯一双射使 $\{z_i(\pi_x)\}=\{z_i(\rho_{\pi,x})\}$ 对几乎所有 $x$ 成立，等价于 $L^S(s,\pi)=L^S(s,\rho_\pi)$。", "source": "译文 §4.1"},
            {"name": "定理 4.2（只需几乎所有点）", "statement": r"Piatetski-Shapiro–Deligne 归纳：只需几乎所有 $x$ 的特征值相等即可。", "source": "译文 §4.1"},
        ],
    ),

    card(
        "ch10-global-number-field",
        "G",
        r"数域上的整体猜想与已知结果",
        ["Langlands 群 L_k", "Galois 型尖点", "Wiles", "Clozel"],
        r"数域上没有整体 $W'_k$，Langlands 群 $\mathcal{L}_k$ 以正合列 $1\to\mathcal{L}_k^0\to\mathcal{L}_k\to\mathcal{G}_k\to1$ 代替；三类对应分别配 $\mathcal{G}_k$、$\mathcal{M}_k$、$\mathcal{L}_k$，已知结果集中在 $n=2$ 与全实域。",
        r"数域上为什么不能像函数域那样用上同调统一构造整体对应？",
        r"数域上没有整体 $W'_k$：Frobenius 只有共轭类，没有单个元素。Langlands 因此引入 $\mathcal{L}_k$，期望有正合列 $1\to\mathcal{L}_k^0\to\mathcal{L}_k\to\mathcal{G}_k\to1$，并把整体参数 $\phi:\mathcal{L}_k\to{}^LG$ 的局部化 $\iota_v\circ\phi_v$ 与局部参数相容。三类对应分别是：(i) $\mathcal{G}_k$ 的 $n$ 维不可约表示 $\leftrightarrow$ Galois 型尖点表示（限制 $\pi_\infty$）；(ii) 动机 Galois 群 $\mathcal{M}_k$ 的表示 $\leftrightarrow$ 代数尖点表示；(iii) $\mathcal{L}_k$ 的表示 $\leftrightarrow$ 全部尖点表示。已知结果大多在 (i)：Deligne 对 $n=2$、$k=\mathbb{Q}$、权 $\ge2$ 的全纯新形式；Deligne–Serre 权 $1$；全实域的 Rogawski–Tunnell、Ohta、Carayol、Wiles、Taylor、Blasius–Rogawski；虚二次域的 Harris–Soudry–Taylor、Taylor；Clozel 对一般 $n$ 的全实域。反方向有 Langlands–Tunnell（强 Artin 猜想，$n=2$）、Wiles（椭圆曲线模性）与 Breuil–Conrad–Diamond–Taylor。障碍的根源是 $\mathrm{GL}_n$ 在数域上没有自然的模问题，故自守→Galois 方向只能逐例做。",
        r"$\mathcal{L}_k$：猜想中的 Langlands 群；$\mathcal{L}_k^0$：其连通分量（猜想对象）；$\mathcal{M}_k$：动机 Galois 群；$\mathcal{G}_k$：绝对 Galois 群；$\pi_\infty$：阿基米德分量。",
        [
            r"$\mathcal{L}_k$ 是猜想对象，不是 $W'_k$ 的整体版；正合列中的 $\mathcal{L}_k^0$ 正是需要构造的部分。",
            r"三类对应按「Galois 侧目标」分层：$\mathcal{G}_k$（最小，Galois 型尖点）、$\mathcal{M}_k$（动机，代数尖点）、$\mathcal{L}_k$（全部尖点）。",
            r"数域上 $\mathrm{GL}_n$ 没有自然模问题，故不能像函数域那样用 shtuka 的上同调统一处理；这是整体理论至今零散的根本原因。",
            r"$n=2$、$k=\mathbb{Q}$ 是唯一完整的情形；$n\ge3$ 只对全实域等特殊域有结果（Clozel 及其后续）。",
        ],
        [
            r"1\to\mathcal{L}_k^0\to\mathcal{L}_k\to\mathcal{G}_k\to1",
        ],
        [
            r"把 $\mathcal{L}_k$ 与 $W'_k$ 等同：$\mathcal{L}_k$ 更大，且其结构本身是猜想的一部分。",
            r"把「Galois 型尖点」当成全部尖点：还有 $\mathcal{M}_k$ 与 $\mathcal{L}_k$ 两档，分别对应代数尖点与全部尖点。",
        ],
        [
            {"type": "含糊点拨", "title": "局部–整体相容怎么写", "text": r"整体参数 $\phi$ 的局部化是 $\phi_v=\iota_v\circ\phi$，其中 $\iota_v:{}^LG_v\to{}^LG$ 由 $\mathcal{G}_{k_v}\subset\mathcal{G}_k$ 给出；没有这条相容性，整体 $L$ 函数无法写成 Euler 乘积。第 11 章定义 2.2 正是这样写的。"},
        ],
        ["ch10-global-function-field", "ch11-dual-group", "ch10-local-langlands"],
        [src(10, "§4.2", [245, 246], "ch10.tex:742-807")],
    ),

    # =====================================================================
    # 第 11 章  对偶群与 Langlands 函子性
    # =====================================================================
    card(
        "ch11-dual-group",
        "G",
        r"对偶群与根数据",
        ["L 群", "根数据", "Chevalley 定理", "内型", "pinning"],
        r"由 $(X,\Phi,\Delta)$ 的对偶 $(X^\vee,\Phi^\vee,\Delta^\vee)$ 造出 ${}^LG^0$，再让 $\mathcal{G}_k$ 经 $\mu$ 作用其上，得 ${}^LG={}^LG^0\rtimes\mathcal{G}_k$；它只分辨到内型，却完全决定准分裂形式。",
        r"为什么 ${}^LG$ 只决定内型与准分裂形式，而不能决定同一内型中的具体群？",
        r"设 $G$ 连通约化、$T\subset B$ 为极大环面与 Borel，$X=X^*(T)$、$\Phi=\Phi(G,T)$、$\Delta$ 为单根。对偶根数据把 $X$ 换成 $X^\vee=X_*$、$\Phi$ 换成 $\Phi^\vee$、$\Delta$ 换成 $\Delta^\vee$，得 $\Psi(G)=(X,\Phi,X^\vee,\Phi^\vee)$ 与基根数据 $\Psi_0(G)=(X,\Delta,X^\vee,\Delta^\vee)$。Chevalley 定理（定理 1.1）说 $\Psi(G)$ 在同构意义下决定 $G$；$\mathrm{Aut}(G)$ 由 $\mathrm{Int}(G)$ 与 $\mathrm{Aut}(\Psi_0(G))$ 组成，钉住 $(G,B,T,\{x_\alpha\})$ 就把分裂钉死。对偶化 $\Psi_0(G)^\vee=(X^\vee,\Delta^\vee,X,\Delta)$ 定义 ${}^LG^0$，再让 $\mathcal{G}_k$ 通过 $\mu:\mathcal{G}_k\to\mathrm{Aut}({}^LG^0)$ 作用，定义 1.1 给出 ${}^LG={}^LG^0\rtimes\mathcal{G}_k$。${}^LG$ 只分辨到内型：内型之间 ${}^LG$ 同构，而准分裂形式被 ${}^LG$ 完全决定，机制是 $H^1(k,G^{\mathrm{ad}})$ 与 $\mathrm{Out}(G)$。表 1 给出 $\mathrm{GL}_n\mapsto\mathrm{GL}_n(\mathbb{C})$、$\mathrm{SO}_{2n+1}\mapsto\mathrm{Sp}_{2n}(\mathbb{C})$、$\mathrm{Sp}_{2n}\mapsto\mathrm{SO}_{2n+1}(\mathbb{C})$、$\mathrm{SO}_{2n}\mapsto\mathrm{SO}_{2n}(\mathbb{C})$：$B_n$ 与 $C_n$ 互换，伴随与单连通互换。",
        r"$X=X^*(T)$：特征格；$X^\vee=X_*(T)$：余特征格；$\Phi$：根系；$\Delta$：单根基；$\Psi(G)$：根数据；$\Psi_0(G)$：基根数据；${}^LG^0$：对偶群的连通分量；$\mu$：$\mathcal{G}_k$ 在 ${}^LG^0$ 上的作用。",
        [
            r"对偶化的次序是 $(X^\vee,\Delta^\vee,X,\Delta)$，不是逐项照抄 $(X,\Delta,X^\vee,\Delta^\vee)$；这是原书 p. 253 首行的写法，译注已核。",
            r"内型共享同一个 ${}^LG$，但 $\Phi(G')$ 只是 $\Phi(G)$ 的子集；准分裂形式的容许同态集最大。",
            r"${}^LG$ 有三种形式：Galois ${}^LG^0\rtimes\mathcal{G}_k$、Weil ${}^LG^0\rtimes W_k$、Weil–Deligne ${}^LG^0\rtimes W'_k$；本书主要用 Galois 形式。",
            r"表 1 的对偶是「特征格 $\leftrightarrow$ 余特征格」的直接后果，故 $\mathrm{SO}_{2n+1}$ 与 $\mathrm{Sp}_{2n}$ 互换。",
        ],
        [
            r"\Psi(G)=(X,\Phi,X^\vee,\Phi^\vee),\qquad \Psi_0(G)=(X,\Delta,X^\vee,\Delta^\vee)",
            r"\Psi_0(G)^\vee=(X^\vee,\Delta^\vee,X,\Delta)",
            r"{}^LG={}^LG^0\rtimes\mathcal{G}_k",
        ],
        [
            r"把 ${}^LG$ 写成直积 ${}^LG^0\times\mathcal{G}_k$：原书误排为 $\times$，正确是半直积 $\rtimes$（译注已改）。",
            r"以为 ${}^LG$ 决定 $G$：它只决定内型与准分裂形式，不决定同一内型中的具体 $G$。",
        ],
        [
            {"type": "易错预警", "title": "splitting 的双关", "text": r"英文 splitting 既指「分裂」也指「钉住」；原书用 pinning 强调 $(G,B,T,\{x_\alpha\})$ 这组数据把 Borel 与根向量钉死，从而 $\mathrm{Aut}(G)\to\mathrm{Aut}(\Psi_0(G))$ 可分裂。§1 的译注解释了为什么需要根向量而不只是 $(B,T)$。"},
        ],
        ["ch11-lgroup-reps", "ch11-functoriality", "ch10-local-langlands"],
        [src(11, "§1", [252, 253], "ch11.tex:52-184")],
        theorems=[
            {"name": "定理 1.1（Chevalley）", "statement": r"根数据 $\Psi(G)$ 在同构意义下决定连通约化群 $G$。", "source": "译文 §1"},
            {"name": "定义 1.1（L 群）", "statement": r"${}^L(G_{/k})={}^LG={}^LG^0\rtimes\mathcal{G}_k$，其中 $\mathcal{G}_k$ 经 $\mu$ 作用在 ${}^LG^0$ 上。", "source": "译文 §1"},
        ],
    ),

    card(
        "ch11-lgroup-reps",
        "G",
        r"L 群的表示与一般 $G$ 的 Langlands 猜想",
        ["L 函数 L(s,π,r)", "容许同态", "L 包", "局部 Langlands 猜想", "部分 L 函数"],
        r"一般 $G$ 的局部猜想用容许同态 $\phi:W'_k\to{}^LG$ 参数化 $L$ 包；取 $r:{}^LG\to\mathrm{GL}_n(\mathbb{C})$ 便有 $L(s,\pi,r)=L(s,r\circ\phi)$，整体逐位点相乘，只有 $\mathrm{GL}_n$ 有完整理论。",
        r"为什么同一个 $L$ 包里的所有表示无法用 $L$ 函数区分？",
        r"对一般约化群 $G$，局部 Langlands 猜想的 Galois 侧是容许同态 $\phi:W'_k\to{}^LG$，满足 (i) 在 $\mathcal{G}_k$ 上方块交换；(ii) 连续，$\phi(\mathbb{G}_a)$ 幂幺，半单映半单；(iii) 若 $\phi(W'_k)$ 落在真抛物子群的 Levi 中，则该抛物子群相干。模去 ${}^LG^0$ 的内自同构得 $\Phi(G)$。猜想说存在满射 $\mathcal{A}(G)\to\Phi(G)$，纤维有限（即 $L$ 包 $\mathcal{A}_\phi$），并满足五条性质：中心特征 $=\omega_\phi$；扭相容；模中心平方可积当且仅当 $\phi(W'_k)$ 不含于真 Levi；缓增当且仅当 $\phi(W_k)$ 有界；与 $\eta:H\to G$ 相容。$L$ 函数需要 $r:{}^LG\to\mathrm{GL}_n(\mathbb{C})$（连续、在 ${}^LG^0$ 上复解析），定义 2.1 置 $L(s,\pi,r)=L(s,r\circ\phi)$、$\varepsilon$ 同理。整体则用 $\mathcal{L}_k$ 代替 $W'_k$，定义 2.2 把局部因子相乘；几乎处处 $\varepsilon=1$、$L$ 因子次数由 $\dim r$ 界定，故乘积有意义；完整 $L$ 函数需要所有位点的局部 LL，只有 $\mathrm{GL}_n$ 已知，一般 $G$ 只能先谈部分 $L$ 函数 $L^S$。",
        r"$W'_k$：局部 Weil–Deligne 群（阿基米德处取 $W_k$）；$\Phi(G)$：容许同态模内自同构之集；$\mathcal{A}_\phi(G)$：$L$ 包；$\omega_\phi$：中心特征；$r:{}^LG\to\mathrm{GL}_n(\mathbb{C})$：$L$ 群的表示；$\iota_v:{}^LG_v\to{}^LG$：局部–整体嵌入。",
        [
            r"容许同态的三条件是逐字可查的定义：方块交换；$\phi(\mathbb{G}_a)$ 幂幺且半单映半单；真 Levi 的相干性。",
            r"$L$ 包内所有 $\pi$ 共享同一个 $\phi$，因此 $L(s,\pi,r)$ 与 $\varepsilon(s,\pi,r)$ 在包内不可区分——这正是「$L$ 包」得名的原因。",
            r"$r$ 不必是嵌入：Jiang–Soudry 用 $r:\mathrm{Sp}_{2n}(\mathbb{C})\hookrightarrow\mathrm{GL}_{2n}(\mathbb{C})$ 把 $\mathrm{SO}_{2n+1}$ 的 $L$ 函数写成 $\mathrm{GL}_{2n}$ 的 Rankin–Selberg 因子。",
            r"部分 $L$ 函数 $L^S$ 总有定义（Langlands 已证其 Euler 乘积在半平面绝对收敛），逆定理只需在 $L^S$ 上操作。",
        ],
        [
            r"\phi:W'_k\to{}^LG,\qquad \mathcal{A}(G)=\bigsqcup_{\phi\in\Phi(G)}\mathcal{A}_\phi(G)",
            r"L(s,\pi,r)=L(s,r\circ\phi),\qquad \varepsilon(s,\pi,r,\psi)=\varepsilon(s,r\circ\phi,\psi)",
            r"L(s,\pi,r)=\prod_v L(s,r\circ\iota_v\circ\phi_v)",
        ],
        [
            r"把 $\Phi$ 当根系：§1 的 $\Phi(G,T)$ 是根系，§2 起 $\Phi(G)$ 是容许同态集；原书 p. 254 明说这是两个东西。",
            r"以为 $\phi$ 落在真 Levi 仍可平方可积：条件 (iii) 的相干性正是排除这种 $\phi$。",
            r"把 $r\circ\phi$ 与 $\phi$ 混用：$L$ 函数依赖 $r$ 的选择，换 $r$ 就换 $L$ 函数（这正是函子性的入口）。",
        ],
        [
            {"type": "含糊点拨", "title": "为什么用容许同态而不是同态", "text": r"$W'_k$ 不是复 Lie 群，$\phi$ 的「代数性」必须用幂幺与半单性来代替；条件 (ii) 就是把「复解析」翻译成 $W'_k$ 的语言。§2.1 的译注解释了这一点，并强调 (iii) 用 $W'_k$、(iv) 用 $W_k$，不可统一。"},
        ],
        ["ch11-dual-group", "ch11-functoriality", "ch10-local-langlands"],
        [src(11, "§2", [254, 257], "ch11.tex:187-393")],
        theorems=[
            {"name": "局部 Langlands 猜想（一般 $G$）", "statement": r"存在满射 $\mathcal{A}(G)\to\Phi(G)$，纤维有限，并满足中心特征、扭相容、平方可积、缓增、与 $\eta:H\to G$ 相容五条性质。", "source": "译文 §2.1"},
            {"name": "定义 2.1 / 2.2（$L$ 函数）", "statement": r"$L(s,\pi,r)=L(s,r\circ\phi)$；整体 $L(s,\pi,r)=\prod_v L(s,r\circ\iota_v\circ\phi_v)$，$\varepsilon$ 同理。", "source": "译文 §2.1–2.2"},
        ],
    ),

    card(
        "ch11-functoriality",
        "G",
        r"Langlands 函子性：L 同态与提升",
        ["函子性原则", "L 同态", "弱提升", "强提升", "自然无分歧提升"],
        r"$L$ 同态 $u:{}^LH\to{}^LG$ 把 $H$ 的参数复合成 $G$ 的参数，于是 $H$ 的表示被提升为 $G$ 的；弱提升只要求几乎所有有限位点匹配，其唯一性来自 $\mathrm{GL}_N$ 的强重数一。",
        r"函子性提升为什么只能先得到「弱」提升，而弱提升又为什么足以确定整体表示？",
        r"$L$ 同态是 $u:{}^LH\to{}^LG$，满足 (i) 在 $\mathcal{G}_k$ 上交换（方块交换）、(ii) 连续、(iii) 在 ${}^LH^0$ 上是复解析同态。若 $G$ 准分裂，则 $\phi\mapsto u\circ\phi$ 给出 $\Phi(u):\Phi(H)\to\Phi(G)$；整体时对每个 $v$ 还有局部 $u_v$。函子性原则说：每个 $L$ 同态都联系着从 $H$ 的容许（局部）/自守（整体）表示到 $G$ 的容许/自守表示的转移或提升。局部情形直接令 $\phi'=u\circ\phi$，$\phi'$ 参数化的 $L$ 包就是提升；三种已理解情形是阿基米德任意 $H,G$ 准分裂、非阿基米德 $\mathrm{GL}_m\to\mathrm{GL}_n$、以及无分歧的自然提升。整体用定义 3.1：弱提升要求所有阿基米德位点与几乎所有有限位点局部提升，强提升要求所有位点。提升的直接后果是 $L^S(s,\pi,r\circ u)=L^S(s,\Pi,r)$ 与 $\varepsilon$ 的相应等式（$S$ 为不知道如何局部提升的有限位点集）。弱提升的存在性由逆定理给出，唯一性由 $\mathrm{GL}_N$ 的强重数一：两个自守表示若几乎处处相同则整体相同。",
        r"$u:{}^LH\to{}^LG$：$L$ 同态；$\Phi(u)$：诱导的容许同态映射；$\mathcal{A}_\phi(H)$：$H$ 的 $L$ 包；$\Pi$：$\pi$ 的提升；$S$：未做局部提升的有限位点集。",
        [
            r"$G$ 必须准分裂：否则 $u\circ\phi$ 可能落在 $\Phi(G)$ 之外，提升无从谈起（§3 的译注）。",
            r"弱/强的差别只在有限多个位点，但弱提升一旦存在就由强重数一唯一确定——这是典型群反推局部参数的关键。",
            r"局部函子性在三种情形已完全理解；整体函子性一般只能得到弱提升。",
            r"提升不只给表示，还给 $L$ 函数与 $\varepsilon$ 的等式；后者是逆定理方法的输入。",
        ],
        [
            r"u:{}^LH\to{}^LG,\qquad \phi\mapsto u\circ\phi",
            r"L^S(s,\pi,r\circ u)=L^S(s,\Pi,r),\qquad \varepsilon^S(s,\pi,r\circ u,\psi)=\varepsilon^S(s,\Pi,r,\psi)",
        ],
        [
            r"把弱提升当成「差一个表示」：它差的是有限多个位点的局部分量，但强重数一使整体表示唯一。",
            r"忘记 $G$ 准分裂：定义 3.1 与函子性原则都只对准分裂的 $G$ 陈述。",
            r"把 $L$ 包层面的提升当成单值映射：提升到的是一整个 $L$ 包，具体选哪个元素需要额外信息。",
        ],
        [
            {"type": "含糊点拨", "title": "为什么用部分 $L$ 函数", "text": r"完整 $L$ 函数要求所有位点的局部 LL，只有 $\mathrm{GL}_n$ 已知；而弱提升本来也只承诺几乎所有位点，所以 $L^S$ 上的等式才是可证的。有限多个缺失因子可由 $\varepsilon$ 的局部分解与函数方程补上。"},
        ],
        ["ch11-lgroup-reps", "ch11-examples-base-change", "ch11-examples-sym-power"],
        [src(11, "§3", [257, 259], "ch11.tex:395-521")],
        theorems=[
            {"name": "函子性原则", "statement": r"$k$ 局部（或整体），$H,G$ 连通约化、$G$ 准分裂，则每个 $L$ 同态 $u:{}^LH\to{}^LG$ 对应一个从 $H$ 的容许（自守）表示到 $G$ 的容许（自守）表示的转移或提升。", "source": "译文 §3"},
            {"name": "定义 3.1（弱/强提升）", "statement": r"弱提升：所有阿基米德位点及几乎所有有限位点 $\Pi_v$ 是 $\pi_v$ 的局部提升；强提升：所有位点。", "source": "译文 §3.2"},
        ],
    ),

    card(
        "ch11-examples-base-change",
        "G",
        r"函子性的 Galois 例子：基变换、自守诱导、内型",
        ["基变换", "自守诱导", "内型提升", "迹公式", "R_{K/k}"],
        r"基变换用 $W_K\subset W_k$ 的限制把 $H(k)$ 的表示送到 $H(K)$；自守诱导反向使用 $R_{K/k}\mathrm{GL}_n\to\mathrm{GL}_{dn}$；内型提升则是 ${}^LH={}^LG$ 的恒等，三者由扭迹公式或逆定理解决。",
        r"基变换与自守诱导都是「换域」，为什么方向相反、技术手段也不同？",
        r"Galois 理论的一组例子来自 $W_K\subset W_k$。基变换：取 $G=R_{K/k}H$（Weil 限制），$G(k)=H(K)$，$L$ 同态 ${}^LH={}^LH^0\times\mathcal{G}_k\to(\prod_{\mathcal{G}_K\backslash\mathcal{G}_k}{}^LH^0)\rtimes\mathcal{G}_k={}^LG$ 在局部就是限制映射（把 $W'_K$ 看成 $W'_k$ 的开子群）。已解决：$H=\mathrm{GL}_n$、$K/k$ 可解（$n=2$ 是 Langlands，一般 $n$ 是 Arthur–Clozel，用扭迹公式）；$H=\mathrm{GL}_2$、$K/k$ 非正规三次是 Jacquet–Piatetski-Shapiro–Shalika 用逆定理做的。自守诱导方向相反：$H=R_{K/k}\mathrm{GL}_n$、$G=\mathrm{GL}_{dn}$，把 $K$ 上的表示送到 $k$ 上；$n=2$ 是 Jacquet–Langlands，$n=1$ 是 Kazhdan，一般情形 Arthur–Clozel、Henniart–Herb。内型提升则是 ${}^LH={}^LG$ 的恒等：Jacquet–Langlands $D^\times\to\mathrm{GL}_2$、Rogawski、Deligne–Kazhdan–Vignéras。",
        r"$K/k$：$d$ 次有限扩张；$R_{K/k}$：Weil 纯量限制；$G(k)=H(K)$；$\mathcal{G}_K\backslash\mathcal{G}_k$：双陪集，对应 $\mathrm{Hom}_k(K,\bar k)$；$D$：$\mathrm{GL}_2$ 的四元数除代数。",
        [
            r"指标集 $\mathcal{G}_K\backslash\mathcal{G}_k$ 与 $\mathrm{Hom}_k(K,\bar k)$ 一一对应，$d$ 次扩张有 $d$ 个元素；这就是 $\prod{}^LH^0$ 出现 $d$ 次的原因。",
            r"基变换 $k\to K$ 与自守诱导 $K\to k$ 方向相反，不要混。",
            r"内型之间 ${}^LH={}^LG$，故函子性在这里退化为「同一 $L$ 群下的转移」，但仍是非平凡的表示论。",
            r"迹公式路线（Arthur–Clozel）与逆定理路线（JPSS）是两条独立的技术路径；前者对可解扩张最有效，后者能处理非正规三次扩张。",
        ],
        [
            r"{}^LH={}^LH^0\times\mathcal{G}_k\longrightarrow\Bigl(\prod_{\mathcal{G}_K\backslash\mathcal{G}_k}{}^LH^0\Bigr)\rtimes\mathcal{G}_k={}^LG",
            r"\#(\mathcal{G}_K\backslash\mathcal{G}_k)=[K:k]=d",
        ],
        [
            r"把基变换与自守诱导的方向搞反：基变换从 $k$ 到 $K$（$H(k)\to H(K)$），自守诱导从 $K$ 到 $k$。",
            r"把内型提升当成不同 ${}^LG$ 之间的同态：内型共享同一个 ${}^LG$，同态是恒等。",
            r"以为基变换总能解：只对 $H=\mathrm{GL}_n$ 且 $K/k$ 可解（或 $H=\mathrm{GL}_2$ 的三次非正规情形）已知。",
        ],
        [
            {"type": "背景直觉", "title": "为什么基变换能用迹公式", "text": r"比较 $H(\mathbb{A}_k)$ 与 $H(\mathbb{A}_K)$ 的（扭）迹公式：几何侧由 $\kappa$-轨道给出，稳定化后两侧的轨道匹配就是基变换。这条路线不构造 $L$ 函数，只用表示的存在性，故对可解扩张最有效。"},
        ],
        ["ch11-functoriality", "ch11-examples-sym-power", "ch11-dual-group"],
        [src(11, "§4.1", [260, 262], "ch11.tex:545-628")],
    ),

    card(
        "ch11-examples-sym-power",
        "G",
        r"群论例子：张量积、对称幂与典型群",
        ["对称幂提升", "张量积提升", "Ramanujan 猜想", "典型群", "逆定理方法"],
        r"到 $\mathrm{GL}_N$ 的提升（张量积、$\mathrm{sym}^n$、典型群）都用 $\mathrm{GL}_N$ 逆定理：逐位点造局部提升、证扭 $L$ 函数匹配、再反解自守性；全 $n$ 的 $\mathrm{sym}^n$ 将推出 $\mathrm{GL}_2$ 的 Ramanujan 猜想。",
        r"为什么「所有对称幂提升」能推出 Ramanujan 猜想，而单个 $\mathrm{sym}^n$ 不能？",
        r"群论例子都取 $H$ 分裂、$G=\mathrm{GL}_N$。张量积：$H=\mathrm{GL}_m\times\mathrm{GL}_n$、$G=\mathrm{GL}_{mn}$，$L$ 同态由 $\otimes:\mathrm{GL}_m(\mathbb{C})\times\mathrm{GL}_n(\mathbb{C})\to\mathrm{GL}_{mn}(\mathbb{C})$ 延拓。对称幂：$H=\mathrm{GL}_2$、$G=\mathrm{GL}_{n+1}$，$L$ 同态由 $\mathrm{sym}^n:\mathrm{GL}_2(\mathbb{C})\to\mathrm{GL}_{n+1}(\mathbb{C})$ 延拓；$\mathrm{sym}^2$（$\mathrm{GL}_2\to\mathrm{GL}_3$）是 Gelbart–Jacquet，$\mathrm{sym}^3$（$\to\mathrm{GL}_4$）是 Kim–Shahidi，$\mathrm{sym}^4$（$\to\mathrm{GL}_5$）是 Kim；全 $n$ 的对称幂函子性将推出 $\mathrm{GL}_2$ 的 Ramanujan 猜想。典型群：$\mathrm{SO}_{2n+1}\to\mathrm{GL}_{2n}$（${}^LH^0=\mathrm{Sp}_{2n}(\mathbb{C})$）、$\mathrm{Sp}_{2n}\to\mathrm{GL}_{2n+1}$、$\mathrm{SO}_{2n}\to\mathrm{GL}_{2n}$，嵌入取标准表示。方法统一：逐位点用局部函子性造 $\Pi_v$，得局部 $L$ 因子等式 $L(s,\pi_v,r_v)=L(s,\Pi_v,\iota_v)$，再证整体 $L(s,\pi,r)=L(s,\Pi,\iota)$ 与扭 $L(s,\pi\times\pi',r\otimes\iota)=L(s,\Pi\times\pi')$；用 Langlands–Shahidi 方法控制扭 $L$ 函数的解析性质，最后套 $\mathrm{GL}_N$ 逆定理得 $\Pi$ 自守。典型群的次生问题是有限位点集 $S$ 上不知正确的局部提升，须取任意提升并用高度分歧的 $\eta$ 扭，靠 $\gamma$ 因子稳定性强行匹配。",
        r"$\mathrm{sym}^n$：$n$ 次对称幂，$\mathrm{GL}_2(\mathbb{C})\to\mathrm{GL}_{n+1}(\mathbb{C})$；$\Pi$：提升后的自守表示；$\iota:{}^LG\to\mathrm{GL}_N(\mathbb{C})$：$L$ 群的表示（常取投影或标准表示）；$r=u^0$：$H$ 侧的标准表示；$\eta$：高度分歧的 idèle 类特征。",
        [
            r"Ramakrishnan（$\mathrm{GL}_2\times\mathrm{GL}_2\to\mathrm{GL}_4$）需 $\mathrm{GL}_1$、$\mathrm{GL}_2$ 的扭，控制的是 Rankin 三重积；Kim–Shahidi（$\mathrm{GL}_2\times\mathrm{GL}_3\to\mathrm{GL}_6$）需 $m=1,2,3,4$，用到 $\mathrm{GL}_5$、$\mathrm{Spin}_{10}$、$E_6$、$E_7$ 上 Eisenstein 级数的系数。",
            r"$\mathrm{sym}^2$ 只需 $\mathrm{GL}_3$ 逆定理与 $\mathrm{GL}_1$ 扭，Gelbart–Jacquet 用 Shimura 积分；$\mathrm{sym}^3$、$\mathrm{sym}^4$ 由张量积提升与外平方推出。",
            r"典型群：CKPS 证弱提升，Ginzburg–Rallis–Soudry 证其为强提升并刻画像，Jiang–Soudry 由此反推局部 LL。",
            r"$\gamma$ 因子稳定性（Shahidi：局部系数 = Bessel 函数的 Mellin 变换）是「以扭代知」的技术基础。",
        ],
        [
            r"\otimes:\mathrm{GL}_m(\mathbb{C})\times\mathrm{GL}_n(\mathbb{C})\to\mathrm{GL}_{mn}(\mathbb{C})",
            r"\mathrm{sym}^n:\mathrm{GL}_2(\mathbb{C})\to\mathrm{GL}_{n+1}(\mathbb{C})",
            r"L(s,\Pi)=L(s,\pi,\mathrm{sym}^2)",
        ],
        [
            r"把 $\mathrm{sym}^n$ 的目标写成 $\mathrm{GL}_n$：$\mathrm{GL}_2(\mathbb{C})$ 的 $n$ 次对称幂是 $n+1$ 维，目标是 $\mathrm{GL}_{n+1}$。",
            r"以为典型群与对称幂用同一套方法：典型群有「有限 $S$ 上不知局部提升」的次生问题，需要高度分歧 $\eta$ 扭与 $\gamma$ 稳定性补偿。",
            r"把弱提升的「几乎所有位点」当成完整结论：$\mathrm{SO}_{2n+1}$ 情形还要 GRS 的强提升定理才能确定 $S$ 处的分量。",
        ],
        [
            {"type": "背景直觉", "title": r"对称幂 $\Rightarrow$ Ramanujan", "text": r"设 $\pi$ 的无分歧参数为 $\mathrm{diag}(\alpha,\beta)$，则 $\mathrm{sym}^n\pi$ 的参数是 $\alpha^n,\alpha^{n-1}\beta,\dots,\beta^n$。若所有 $\mathrm{sym}^n\pi$ 都自守，则 $L(s,\mathrm{sym}^n\pi)$ 在 $\mathrm{Re}\,s>1$ 绝对收敛，比较 Euler 因子得 $|\alpha|,|\beta|\le1$；中心特征给 $|\alpha\beta|=1$，故 $|\alpha|=|\beta|=1$。这就是原书说「全 $n$ 对称幂是通往 Ramanujan 的最短路线」的意思。"},
        ],
        ["ch11-functoriality", "ch11-examples-base-change", "ch9-functional-equation"],
        [src(11, "§4.2", [262, 265], "ch11.tex:629-856")],
        theorems=[
            {"name": "Ramakrishnan / Kim–Shahidi", "statement": r"$\mathrm{GL}_2\times\mathrm{GL}_2\to\mathrm{GL}_4$ 与 $\mathrm{GL}_2\times\mathrm{GL}_3\to\mathrm{GL}_6$ 的整体张量积提升成立（用 $\mathrm{GL}_N$ 逆定理）。", "source": "译文 §4.2"},
            {"name": "对称幂", "statement": r"$\mathrm{sym}^2$（Gelbart–Jacquet）、$\mathrm{sym}^3$（Kim–Shahidi）、$\mathrm{sym}^4$（Kim）的整体提升成立；全 $n$ 将推出 $\mathrm{GL}_2$ 的 Ramanujan 猜想。", "source": "译文 §4.2"},
        ],
    ),
]
