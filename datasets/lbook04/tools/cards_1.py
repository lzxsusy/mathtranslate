# -*- coding: utf-8 -*-
"""lbook04 资料卡数据（一）：第 1–4 章（L 轨 ch1、ch2、ch4；M 轨 ch3）。"""

from base import card, src


CARDS_1 = [
    card("all-map", "O", "全书地图：从 L 函数到几何朗兰兹",
         ["chapter map", "阅读路线"],
         "十二章沿一条主线：先把 L 函数从 Riemann zeta 推广到 Artin 与椭圆曲线，再把自守形式升到 adele 与 GL_n，最终在 Langlands 猜想与对偶群处收束，以几何朗兰兹作结。",
         "这本书的十二章应当按什么顺序读，各章之间靠什么概念相连？",
         "全书可分成四段：第 1–5 章讲 L 函数（Riemann、Dirichlet、Dedekind、Hecke、Artin、椭圆曲线）；第 3、7 章讲自守形式从经典模形式到 adele 表示的升级；第 6、8 章讲 Tate 论文与谱理论/迹公式这套解析机器；第 9–11 章把一切搬到 GL_n 并陈述 Langlands 猜想与函子性；第 12 章是几何版本。",
         "章节编号沿用原书；第 12 章为 Gaitsgory 的几何朗兰兹导论。",
         ["前五章是同一问题的五次推广：zeta → Dirichlet L → Dedekind zeta → Hecke L → Artin L。",
          "第 6 章的 Tate 论文把 L 函数的函数方程化归为局部 zeta 积分的计算，是全书技术转折点。",
          "第 9–11 章的三部曲（解析理论、Langlands 猜想、对偶群与函子性）构成纲领的现代陈述。",
          "第 12 章把数域换成函数域、把 Galois 表示换成 lisse 层，得到几何朗兰兹。"],
         ["L(s,\\chi)=\\sum_{n\\ge 1}\\chi(n)n^{-s}", "\\zeta_K(s)=\\prod_{\\mathfrak p}(1-N\\mathfrak p^{-s})^{-1}"],
         ["把第 12 章当作全书的特例会误解它：几何朗兰兹是平行理论，不是第 9–11 章的推论。",
          "各章作者不同，记号并不完全统一（如 GL_n 的 L 函数在 ch9 与 ch10 的归一化差一个移位），跨章引用时须回到该章定义。"],
         [{"type": "背景直觉", "title": "为什么按这个顺序读", "text": "若只为几何朗兰兹，最短路径是 ch6（Tate 局部理论）→ ch9（GL_n 解析理论）→ ch12；ch1–5 提供动机，ch7–8 提供自守表示与迹公式的语言，ch10–11 是纲领的完整陈述。"}],
         ["ch1-zeta-euler", "ch6-local-zeta", "ch9-godement-jacquet"],
         [src(1, "全书", [1, 281], "ch01.tex:1-40", section="导论")]),

    card(
        "ch1-zeta-euler", "L",
        "Riemann zeta 与 Euler 乘积",
        ["Riemann zeta function", "Euler product", "ζ(s) 的 Euler 乘积"],
        "$\\zeta(s)=\\prod_p(1-p^{-s})^{-1}$ 把唯一分解写成局部因子；Riemann 把 $s$ 看成复变量，用完备化 $\\Lambda$ 得到对称的函数方程。",
        "Euler 乘积为什么比「$\\zeta(s)$ 的级数定义」更强，它究竟把素数的什么信息编码进来了？",
        "Euler 1737 年用调和级数发散重新证明了素数无穷多，并得到 $\\sum_{p\\le X}1/p=\\log\\log X+O(1)$。Riemann 1859 年的贡献不是乘积而是「把 $s$ 看成复变量」：他定义 $\\Lambda(s)=\\pi^{-s/2}\\Gamma(s/2)\\zeta(s)$，证明 $\\Lambda(s)=\\Lambda(1-s)$，算出 $\\zeta(0)=-1/2$ 并指出平凡零点 $s=-2n$。Euler 乘积在 $\\operatorname{Re}(s)>1$ 时绝对收敛，因此在该半平面给出 $\\zeta(s)\\ne0$；这正是后来素数定理证明的起点之一。书中 §2 还给出显式公式 (2.5)：素数幂上的 von Mangoldt 和等于极点主项、临界带零点求和与一条竖线上的阿基米德积分三项之和。",
        "$\\zeta(s)$：Riemann zeta 函数；$p$：素数；$\\Lambda(s)$：完备化 zeta；$\\Gamma$：伽马函数；$\\rho$：非平凡零点；$\\Lambda(n)$：von Mangoldt 函数（第 2 章起用）。",
        [
            "Euler 乘积是唯一分解定理的解析形式：每个素数 $p$ 贡献因子 $(1-p^{-s})^{-1}$，乘开即得全部 $n^{-s}$。",
            "Riemann 的贡献在于「复变量 + 函数方程 + 零点」：他把一个收敛性问题变成了整函数/亚纯函数的对称性问题。",
            "$\\operatorname{Re}(s)>1$ 时乘积绝对收敛，故 $\\zeta(s)\\ne0$；这是 Euler 乘积给出的定性信息，也是第 2 章无零点区域的出发点。",
        ],
        [
            "\\zeta(s)=\\prod_{p}\\bigl(1-p^{-s}\\bigr)^{-1}=\\sum_{n\\ge1}n^{-s},\\qquad \\operatorname{Re}(s)>1",
            "\\Lambda(s)=\\pi^{-s/2}\\Gamma\\bigl(\\tfrac{s}{2}\\bigr)\\zeta(s),\\qquad \\Lambda(s)=\\Lambda(1-s)",
            "\\Lambda(n)=\\begin{cases}\\log p, & n=p^{k},\\\\ 0, & \\text{其他}\\end{cases}",
        ],
        [
            "把 $\\Lambda(s)$ 当成整函数：$\\Lambda$ 在 $s=0,1$ 各有一个单极点；整函数是 $\\xi(s)=\\tfrac12 s(s-1)\\Lambda(s)$，且 $\\xi(0)=\\xi(1)=\\tfrac12$。引用「Riemann 的函数方程」时要先声明用的是 $\\Lambda$ 还是 $\\xi$。",
            "以为 Euler 乘积自动给出解析延拓：乘积只在 $\\operatorname{Re}(s)>1$ 收敛，跨过这条线要靠 theta 函数与 Poisson 求和（第 2 章 §2）。",
        ],
        [
            {"type": "易错预警", "title": "Λ 还是 ξ", "text": "中译注本 §2 的批注特别指出：$\\Lambda(s)$ 仍带两个极点，Riemann 1859 原文用的是 $\\xi(s)=\\tfrac12 s(s-1)\\Lambda(s)$。若把「$\\Lambda(s)=\\Lambda(1-s)$」直接说成「$\\zeta$ 的函数方程」，会漏掉极点与对称轴 $s=1/2$ 的平移。"},
            {"type": "背景直觉", "title": "Euler 因子是局部数据", "text": "书中脚注提醒：在数域上，Euler 因子 $L_{\\mathfrak p}(s)$ 这份数据比乘积 $\\prod_{\\mathfrak p}L_{\\mathfrak p}(s)$ 更强——即使乘积定义了一个全纯函数（例如第 5 节的部分 zeta），单个因子的信息仍可能丢失。这就是「局部-整体原则」在 L 函数上的雏形。"},
        ],
        ["ch1-dirichlet-char", "ch1-gamma-factor"],
        [
            src(1, "§2", [1, 2], "ch01.tex:17-35"),
            src(1, "§2", [3, 4], "ch01.tex:43-70"),
        ],
        theorems=[
            {
                "name": "命题 2.1（显式公式 (2.5)）",
                "statement": "设 $\\varphi$ 为 $]0,+\\infty[$ 上具紧支集的 $C^\\infty$ 函数，$\\hat\\varphi(s)=\\int_0^{+\\infty}\\varphi(x)x^{s-1}dx$，$\\psi(x)=\\varphi(x^{-1})/x$。则 $\\sum_p\\sum_{k\\ge1}(\\log p)(\\varphi(p^k)+\\psi(p^k))=\\int_0^{+\\infty}\\varphi(x)dx-\\sum_{\\zeta(\\rho)=0,\\,0<\\operatorname{Re}\\rho<1}\\hat\\varphi(\\rho)+\\frac{1}{2\\pi i}\\int_{(-1/2)}\\bigl(\\tfrac12\\frac{\\Gamma'}{\\Gamma}(\\tfrac{s}{2})-\\tfrac12\\frac{\\Gamma'}{\\Gamma}(\\tfrac{1-s}{2})\\bigr)\\hat\\varphi(s)ds$。",
                "proof": {
                    "steps": [
                        "对 $\\Lambda'/\\Lambda$ 用 Mellin 反演，把 $\\sum\\Lambda(n)\\varphi(n)$ 写成围道积分。",
                        "把围道移到 $\\operatorname{Re}(s)=-1/2$，途中拣出 $s=1$ 的极点（给 $\\int\\varphi$）与临界带内的零点（给 $-\\sum\\hat\\varphi(\\rho)$）。",
                        "用 $\\Lambda(s)=\\Lambda(1-s)$ 把 $1-s$ 的部分化回 $s$，两个 $\\Gamma'/\\Gamma$ 各得系数 $1/2$。",
                    ],
                    "gap_note": "书中只给公式与三项来源的说明，未逐行重排围道；第 2 章命题 3.5 才给出一般 Hecke 情形的证明梗概。",
                },
                "source": "ch01.tex:74-100（§2，命题 2.1）",
            }
        ],
    ),
    card(
        "ch1-dirichlet-char", "L",
        "Dirichlet 特征与 Dirichlet L 函数",
        ["Dirichlet character", "Dirichlet L-function", "导子与本原特征"],
        "模 $q$ 的特征把 $(\\mathbb Z/q\\mathbb Z)^\\times$ 的群同态延拓到 $\\mathbb Z$ 上；$L(\\chi,s)$ 的解析性质由本原特征与导子决定，非主特征在 $s=1$ 不为零即得 Dirichlet 定理。",
        "为什么 Dirichlet 定理（算术级数中的素数）等价于非主特征满足 $L(\\chi,1)\\ne0$？",
        "设 $\\tilde\\chi:(\\mathbb Z/q\\mathbb Z)^\\times\\to\\mathbb C^\\times$ 为群同态，令 $\\chi(n)=\\tilde\\chi(n \\bmod q)$（若 $(n,q)=1$）而 $(n,q)\\ne1$ 时 $\\chi(n)=0$。$\\chi$ 完全乘性，故 $L(\\chi,s)=\\sum\\chi(n)n^{-s}=\\prod_p(1-\\chi(p)p^{-s})^{-1}$。用 $(\\mathbb Z/q\\mathbb Z)^\\times$ 上的正交关系，可把「$p\\equiv a$」的指示函数写成 $\\frac{1}{\\varphi(q)}\\sum_\\chi\\overline\\chi(a)\\chi(p)$；再对 $\\log L(\\chi,s)$ 在 $s=1$ 附近展开，主项为 $\\frac{1}{\\varphi(q)}\\log\\frac{1}{s-1}$，非主特征的贡献若有 $1/\\varphi(q)$ 量级的负项就会抵消主项——故 Dirichlet 定理归结为 $L(\\chi,1)\\ne0$（$\\chi_4$ 给出 $\\pi/4$ 的经典例子）。函数方程只对本原特征干净：任一 $\\chi$ 由唯一本原 $\\tilde\\chi$ 诱导，$L(\\chi,s)$ 与 $L(\\tilde\\chi,s)$ 差有限个 Euler 因子 (3.1)。",
        "$q$：模（导子的倍数）；$\\tilde q$：导子（本原特征的模）；$\\varphi$：Euler 函数；$\\tau(\\chi)$：Gauss 和；$\\varepsilon(\\chi)$：根数；$\\Lambda(\\chi,s)$：完备化 L 函数。",
        [
            "$\\chi$ 在 $(x,q)\\ne1$ 处取 $0$ 不是疏忽：这让 $p\\mid q$ 处的 Euler 因子退化为 $1$，从而 $L(\\chi,s)$ 与 $\\zeta(s)$ 只差有限个因子。",
            "本原特征才满足干净的函数方程；非本原 $\\chi$ 由唯一本原 $\\tilde\\chi$ 诱导，二者相差有限乘积 (3.1)。",
            "Dirichlet 定理的解析核心是「$L(\\chi,1)\\ne0$」：$\\log L$ 展开中主项由 $p\\equiv1$ 的素数的 $1/p$ 给出，其余类由正交关系合成。",
        ],
        [
            "L(\\chi,s)=\\sum_{n\\ge1}\\chi(n)n^{-s}=\\prod_{p}\\bigl(1-\\chi(p)p^{-s}\\bigr)^{-1}",
            "\\Lambda(\\chi,s)=\\varepsilon(\\chi)\\,q^{1/2-s}\\,\\Lambda(\\overline{\\chi},1-s),\\qquad \\varepsilon(\\chi)=\\begin{cases}\\tau(\\chi)/\\sqrt{q}, & \\chi(-1)=1,\\\\ -i\\,\\tau(\\chi)/\\sqrt{q}, & \\chi(-1)=-1.\\end{cases}",
            "L(\\chi,s)=L(\\tilde\\chi,s)\\prod_{p\\mid q/\\tilde q}\\bigl(1-\\chi(p)p^{-s}\\bigr)",
        ],
        [
            "$\\varepsilon(\\chi)$ 的两个分支由 $\\chi(-1)=\\pm1$ 决定；统一写法是 $\\varepsilon(\\chi)=\\tau(\\chi)/(i^a\\sqrt q)$，$a\\in\\{0,1\\}$ 由 $\\chi(-1)=(-1)^a$ 定。$\\sqrt q$ 与 $|\\tau(\\chi)|=\\sqrt q$ 只对本原特征成立，非本原时要换成导子 $\\tilde q$。",
            "(3.1) 的乘积下标是 $p\\mid q/\\tilde q$，不是 $p\\mid q$：被剔除的正是「多余」的那些素因子。",
        ],
        [
            {"type": "易错预警", "title": "模还是导子", "text": "$\\chi$ 的模 $q$ 不唯一（可乘素因子的幂提升），本原的 $\\tilde q$ 才唯一；函数方程里出现的是 $\\tilde q$ 而不是任意一个模。书中 §3 正是用这一点说明「先验未知的导子会以这种方式出现」。"},
            {"type": "背景直觉", "title": "Gauss 和是伽马因子的有限域类比", "text": "$\\tau(\\chi)=\\sum_{x\\bmod q}\\chi(x)e(x/q)$ 是加法特征与乘法特征的配对；书里把它称作 $\\Gamma$ 因子的某种有限域类比，根数 $\\varepsilon$ 因此是「阿基米德因子之外」的整体不变量。"},
        ],
        ["ch1-zeta-euler", "ch1-gamma-factor", "ch4-artin-hecke"],
        [
            src(1, "§3", [4, 5], "ch01.tex:112-150"),
            src(1, "§3", [5, 7], "ch01.tex:155-201"),
        ],
        theorems=[
            {
                "name": "定理 3.1（算术级数中的素数）",
                "statement": "设 $(a,q)=1$，则有无穷多素数 $p\\equiv a\\pmod q$，且 $\\sum_{p\\le X,\\,p\\equiv a}\\frac{1}{p}=\\frac{1}{\\varphi(q)}\\log\\log X+O(1)$。",
                "proof": {
                    "steps": [
                        "用正交关系把 $1_{p\\equiv a}$ 写成 $\\frac{1}{\\varphi(q)}\\sum_\\chi\\overline\\chi(a)\\chi(p)$。",
                        "对每个 $\\chi$ 展开 $\\log L(\\chi,s)$，$s\\to1^+$；主特征给 $\\log\\frac{1}{s-1}$ 的主项。",
                        "$\\chi\\ne\\chi_0$ 时 $L(\\chi,1)\\ne0$，故其对数在 $s=1$ 有界，不抵消主项。",
                    ],
                    "gap_note": "书中只陈述定理；$L(\\chi,1)\\ne0$ 的证明（尤其实特征情形）要到本章后段与第 2 章才补，那里用的是类数公式与零点排斥。",
                },
                "source": "ch01.tex:112-150（§3，定理 3.1）",
            }
        ],
    ),
    card(
        "ch1-dedekind-zeta", "L",
        "Dedekind zeta 与 Hecke L 函数",
        ["Dedekind zeta function", "Hecke L-function", "射线类群"],
        "$\\zeta_K(s)=\\sum_{\\mathfrak a}(N\\mathfrak a)^{-s}$ 的 Euler 因子记录素理想分裂型；Hecke 特征把 Dirichlet 特征搬到射线类群上，其 L 函数以 $|D|N\\mathfrak m$ 为导子。",
        "Dedekind zeta 的系数 $r_K(n)$ 如何读出素数在 $K$ 中的分裂方式，Hecke L 函数又为什么必须引入射线类群？",
        "$\\zeta_K(s)=\\sum_{\\mathfrak a\\ne0}(N\\mathfrak a)^{-s}$ 对 $\\operatorname{Re}(s)>1$ 绝对收敛并有 Euler 乘积；写成 Dirichlet 级数 $\\zeta_K(s)=\\sum r_K(n)n^{-s}$ 后，$r_K(p)$ 编码 $p$ 的分裂型：$r_K(p)=d$ 当且仅当 $p$ 完全分裂；$r_K(p)=1$ 则可能是完全分歧也可能是惰性（只有一个次数 $d$ 的素理想）。完备化 $\\Lambda_K$ 满足 $\\Lambda_K(s)=|D|^{1/2-s}\\Lambda_K(1-s)$，根数恒为 $+1$，判别式的位置「正如 Dirichlet L 函数中的导子」；留数由类数公式 (4.2) 给出。Hecke 的推广是：取模 $\\mathfrak m$、射线类群 $H_{\\mathfrak m}=I_{\\mathfrak m}/P_{\\mathfrak m}$，特征 $\\chi$ 经权 $\\xi_\\infty$ 与 $\\chi((\\alpha))=\\xi_\\infty(\\alpha)$ 相容，于是 $L(\\chi,s)=\\prod_{\\mathfrak p}(1-\\chi(\\mathfrak p)(N\\mathfrak p)^{-s})^{-1}$。$K=\\mathbb Q$ 时回到 Dirichlet（例 5.6），$\\mathfrak m=1$、$\\xi_\\infty=1$ 时回到理想类群特征（例 5.5）。",
        "$K$：数域；$\\mathcal O_K$：整数环；$\\mathfrak a,\\mathfrak p$：整理想/素理想；$N\\mathfrak a$：绝对范数；$D$：判别式；$r_1,r_2$：实/复嵌入个数；$h$：类数；$R$：调节子；$\\mathfrak m$：模；$H_{\\mathfrak m}$：射线类群；$\\xi_\\infty$：无穷位权。",
        [
            "$\\zeta_K$ 是「$K$ 中素数分布」的生成函数：$r_K(p)$ 数出 $p$ 上方素理想的个数与次数，完全分裂、惰性、分歧三种情形在系数上可区分。",
            "$h>1$ 时 Hecke 特征不能只看元素，必须看理想/射线类群；这正是 Hecke L 比 Dirichlet L 多出来的结构。",
            "(4.3) 的根数恒为 $+1$，因为 $\\zeta_K$ 来自平凡表示；一般 Hecke L 的根数 $\\varepsilon(\\chi)$ 才可能非平凡，且底数从 $|D|$ 变成 $|D|N\\mathfrak m$。",
        ],
        [
            "\\zeta_K(s)=\\sum_{\\mathfrak a\\ne0}\\frac{1}{(N\\mathfrak a)^{s}}=\\prod_{\\mathfrak p}\\bigl(1-(N\\mathfrak p)^{-s}\\bigr)^{-1}",
            "\\Lambda_K(s)=|D|^{1/2-s}\\Lambda_K(1-s),\\qquad \\Lambda_K(s)=\\pi^{-r_1s/2}(2\\pi)^{-r_2s}\\Gamma(s/2)^{r_1}\\Gamma(s)^{r_2}\\zeta_K(s)",
            "L(\\chi,s)=\\prod_{\\mathfrak p}\\bigl(1-\\chi(\\mathfrak p)(N\\mathfrak p)^{-s}\\bigr)^{-1},\\qquad \\Lambda(\\chi,s)=\\varepsilon(\\chi)\\,(|D|N\\mathfrak m)^{1/2-s}\\,\\Lambda(\\overline\\chi,1-s)",
        ],
        [
            "把 (4.3) 的根数也写成 $\\varepsilon$：$\\zeta_K$ 的根数恒为 $+1$；只有 Hecke L 的 (5.4) 里才出现 $\\varepsilon(\\chi)(|D|N\\mathfrak m)^{1/2-s}$。",
            "$r_K(p)=1$ 不能直接判为惰性：完全分歧也只有一个素理想；要区分得看 $r_K(p^k)$ 的整组数据（$e$、$f$、$g$ 的组合）。",
        ],
        [
            {"type": "易错预警", "title": "判别式的位置", "text": "书中明说判别式在 (4.3) 中的位置「正如 Dirichlet L 函数中的导子」，这把 $|D|$ 与 $q$ 放在同一角色。但 $|D|$ 只由 $K$ 决定，不是可选的「模」；真正的模是 $\\mathfrak m$，两者在 (5.4) 中才合并成 $|D|N\\mathfrak m$。"},
            {"type": "背景直觉", "title": "类数公式是特殊值原理的原型", "text": "(4.2) $\\operatorname{Res}_{s=1}\\zeta_K=\\frac{2^{r_1}(2\\pi)^{r_2}hR}{w\\sqrt{|D|}}$ 用整体不变量表达 $\\zeta_K$ 在 $s=1$ 的留数。书中把它与 Deligne 的特殊值框架、BSD 猜想并置：椭圆曲线 L 在中心点的导数对应 regulator，是同一个原理的算术几何版本。"},
        ],
        ["ch1-zeta-euler", "ch1-cft-entry", "ch4-artin-hecke"],
        [
            src(1, "§4", [7, 9], "ch01.tex:213-235"),
            src(1, "§4", [10, 12], "ch01.tex:278-300"),
            src(1, "§5", [13, 16], "ch01.tex:433-465"),
        ],
    ),
    card(
        "ch1-gamma-factor", "L",
        "函数方程与 gamma 因子",
        ["gamma factor", "完备化 L 函数", "阿基米德 Euler 因子"],
        "$\\Gamma$ 因子是补齐阿基米德位的局部因子：它使 $\\Lambda(s)=\\Lambda(1-s)$ 对称；Tate 论文才把它解释为 $\\mathbb Q$ 的阿基米德 Euler 因子。",
        "伽马因子为什么必须出现在函数方程里，它在局部-整体原则下到底是什么？",
        "$\\zeta$ 的完备化是 $\\Lambda(s)=\\pi^{-s/2}\\Gamma(s/2)\\zeta(s)$，函数方程 $\\Lambda(s)=\\Lambda(1-s)$。Dirichlet 情形要分偶奇：$\\chi(-1)=1$ 时 $\\Lambda(\\chi,s)=\\pi^{-s/2}\\Gamma(s/2)L(\\chi,s)$；$\\chi(-1)=-1$ 时用 $\\pi^{-(s+1)/2}\\Gamma((s+1)/2)$。Dedekind 情形按 $r_1,r_2$ 出 $\\Gamma(s/2)^{r_1}\\Gamma(s)^{r_2}$，判别式 $|D|$ 只进 $s\\mapsto1-s$ 的平移因子。Kowalski 在 §2 提醒：1859 年时伽马因子的出现「并未被很好理解」，是 Tate 的论文才把它澄清为 $\\mathbb Q$（或一般数域）在阿基米德位处的 Euler 因子；第 4 章把同一件事写成 $\\Gamma_{\\mathbb R},\\Gamma_{\\mathbb C}$，并用 $n_\\pm$ 把 $s$ 与 $s+1$ 分配下去。",
        "$\\Gamma_{\\mathbb R}(s)=\\pi^{-s/2}\\Gamma(s/2)$：实位因子；$\\Gamma_{\\mathbb C}(s)=2(2\\pi)^{-s}\\Gamma(s)$：复位因子；$n_\\pm(\\chi,v)$：实/复位上 $s$ 与 $s+1$ 的重数；$\\varepsilon$：根数。",
        [
            "$\\Gamma$ 因子不是「修正项」，而是与 $p$ 处 $(1-p^{-s})^{-1}$ 并列的局部因子，只不过所在的位是阿基米德位。",
            "偶/奇特征用不同的 $\\Gamma$：$\\chi(-1)=1$ 用 $\\Gamma(s/2)$，$\\chi(-1)=-1$ 用 $\\Gamma((s+1)/2)$，对应 $\\chi_\\infty$ 在 $\\mathbb R^\\times$ 上的两个分量。",
            "函数方程的对称轴由 $\\Gamma$ 因子与导子共同决定：$\\zeta$ 的轴是 $s=1/2$，权/导子会把轴移动（模形式是 $s=k/2$）。",
        ],
        [
            "\\Lambda(s)=\\pi^{-s/2}\\Gamma(s/2)\\zeta(s)=\\Lambda(1-s)",
            "\\Lambda(\\chi,s)=\\pi^{-(s+1)/2}\\Gamma\\bigl((s+1)/2\\bigr)L(\\chi,s)\\qquad(\\chi(-1)=-1)",
            "\\Gamma_{\\mathbb R}(s)=\\pi^{-s/2}\\Gamma(s/2),\\qquad \\Gamma_{\\mathbb C}(s)=\\Gamma_{\\mathbb R}(s)\\Gamma_{\\mathbb R}(s+1)=2(2\\pi)^{-s}\\Gamma(s)",
        ],
        [
            "把 $\\Gamma$ 因子只当成「为了让函数方程好看」的凑数：它在 Tate 的局部理论里有独立来源（$\\mathbb R^\\times$ 上的 zeta 积分），可以事先算出，而不是事后拼凑。",
            "偶/奇两套 $\\Lambda$ 混用：$\\chi(-1)=-1$ 时若仍写 $\\pi^{-s/2}\\Gamma(s/2)$，函数方程会差一个平移，$s\\leftrightarrow1-s$ 不再对称。",
        ],
        [
            {"type": "含糊点拨", "title": "Γ 因子地位的演变", "text": "书中 §2 说函数方程「当时并未被很好理解」，直到 Tate 才澄清 $\\Gamma$ 因子是 $\\mathbb Q$ 的阿基米德 Euler 因子；第 4 章 (4.1) 把它写成 $\\Gamma_{\\mathbb R},\\Gamma_{\\mathbb C}$，正是同一件事的一般形式。读第 1 章时不要把「de facto 地位」误当成「概念上已解释」。"},
            {"type": "背景直觉", "title": "Hodge 理论预测局部因子", "text": "de Shalit 在 §4.1 说，如今 Hodge 理论的一般原理能预测阿基米德 Euler 因子的正确形状——即便解析延拓与函数方程仍然未知。这把「猜函数方程」变成了「算局部因子」，是 Langlands 纲领把局部问题整体化的一个例子。"},
        ],
        ["ch1-zeta-euler", "ch1-dirichlet-char", "ch2-explicit-formula"],
        [
            src(1, "§2", [3, 4], "ch01.tex:43-70"),
            src(1, "§3", [5, 6], "ch01.tex:170-201"),
        ],
    ),
    card(
        "ch1-cft-entry", "L",
        "解析延拓与类域论入口",
        ["Kronecker–Weber", "交换扩张的 L 分解", "ζ_E=∏L(ρ,s)"],
        "交换扩张 $E/K$ 的 zeta 分解为 Galois 特征 L 函数之积；把每个 $L(\\rho,s)$ 认成一维 Hecke L 函数，就是类域论的 L 函数表述。",
        "为什么 $\\zeta_E(s)=\\prod_{\\rho\\in\\widehat G}L(\\rho,s)$ 的「形式计算」能看成类域论的入口，而不是普通的因式分解？",
        "设 $E/K$ 为有限交换 Galois 扩张，群 $G$，$\\mathfrak p$ 为 $K$ 的素理想，$\\sigma_{\\mathfrak p}$ 为 Frobenius 元。则 $\\zeta_E(s)=\\prod_{\\rho\\in\\widehat G}L(\\rho,s)$，其中 $L(\\rho,s)=\\prod_{\\mathfrak p}(1-\\rho(\\sigma_{\\mathfrak p})(N\\mathfrak p)^{-s})^{-1}$，分歧的 $\\mathfrak p$ 用 $V^{I_{\\mathfrak p}}$ 上的作用处理。这个等式本身只是「按 $G$ 的特征分解」：完全分裂时两边的 $\\mathfrak p$-因子都是 $d$ 个 $(1-q^{-s})^{-1}$。真正的困难在解析延拓——单个 $L(\\rho,s)$ 的 Dirichlet 系数没有明显的部分和有界性（书中脚注 5 提出这个问题）。类域论的内容正是：把 Galois 侧的一维 $L(\\rho,s)$ 认成 Hecke/Dirichlet 侧的 $L(\\chi,s)$。书中定理 5.2（Kronecker–Weber 的 L 函数形式）与定理 5.9（Artin）给出 $L(\\rho,s)=L(\\chi,s)$ 及局部等式 $\\rho(\\sigma_{\\mathfrak p})=\\chi(\\mathfrak p)$；注 5.10 说明导子 $\\mathfrak f(\\rho)$ 与权 $\\xi_\\infty(\\rho)$ 可只用 $\\rho$ 定义；注 5.11 给出 $|D|=\\prod_\\chi q_\\chi$。",
        "$E/K$：交换 Galois 扩张；$G$：Galois 群；$\\widehat G$：复特征群；$\\sigma_{\\mathfrak p}$：Frobenius 元；$I_{\\mathfrak p}$：惯性群；$\\mathfrak f(\\rho)$：导子；$q_\\chi$：特征 $\\chi$ 的导子；$H_{\\mathfrak m}$：射线类群。",
        [
            "(5.1) 的证明只是「按 $G$ 的特征分解」：$\\zeta_E$ 的每个 $\\mathfrak p$-因子是 $d$ 个 $(1-q^{-s})^{-1}$，右边 $d$ 个特征各贡献一个。",
            "真正的困难在解析延拓：Artin L 的 Dirichlet 系数没有明显的部分和有界性，这正是第 4 章用 Brauer 诱导解决的问题。",
            "交换情形定理 5.9 说 $L(\\rho,s)=L(\\chi,s)$ 且局部相等；这把「Galois 侧的 L」与「Hecke 侧的 L」逐位对齐，是类域论的解析表述。",
        ],
        [
            "\\zeta_E(s)=\\prod_{\\rho\\in\\widehat G}L(\\rho,s),\\qquad L(\\rho,s)=\\prod_{\\mathfrak p}\\bigl(1-\\rho(\\sigma_{\\mathfrak p})(N\\mathfrak p)^{-s}\\bigr)^{-1}",
            "L(\\rho,s)=L(\\chi,s),\\qquad \\rho(\\sigma_{\\mathfrak p})=\\chi(\\mathfrak p)\\quad(\\dim\\rho=1)",
            "|D|=\\prod_{\\chi}q_{\\chi}",
        ],
        [
            "把 (5.1) 当成「$\\zeta_E$ 的解析延拓」：它只是形式分解；每个 $L(\\rho,s)$ 的解析延拓在交换情形由 Hecke 定理 5.8 给出，非交换情形要靠 Artin/Brauer（第 4 章）。",
            "忽略惯性群：$\\mathfrak p$ 分歧时 $\\rho(\\sigma_{\\mathfrak p})$ 无定义，必须取 $V^{I_{\\mathfrak p}}$ 上的作用；书中 (5.1) 下方明确写出这一点。",
        ],
        [
            {"type": "易错预警", "title": "导子不是判别式", "text": "注 5.11 给出 $|D|=\\prod_\\chi q_\\chi$：判别式是各特征导子之积，而不是某一个导子。对 $E=\\mathbb Q(\\mu_\\ell)$，$\\ell-1$ 个特征中 $\\ell-2$ 个导子为 $\\ell$、一个导子为 $1$，于是 $|D|=\\ell^{\\ell-2}$；$\\ell=3,5$ 可直接验算。"},
            {"type": "背景直觉", "title": "Weil 式证明的类比", "text": "注 5.4 把 Kronecker–Weber 的 L 函数证明与模性猜想（Wiles）相提并论：都是「先证 L 函数相等，再用它推出域/曲线相等」。这是本书反复出现的「互反」母题：解析侧的等式反过来决定算术侧的对象。"},
        ],
        ["ch1-dedekind-zeta", "ch4-artin-hecke", "ch4-induction"],
        [
            src(1, "§5", [12, 14], "ch01.tex:378-400"),
            src(1, "§5", [15, 17], "ch01.tex:484-516"),
        ],
        theorems=[
            {
                "name": "定理 5.9（Artin，交换情形）",
                "statement": "设 $E/K$ 为有限交换扩张，$\\rho:G\\to\\mathbb C^\\times$ 为 Galois 特征。则存在 $K$ 的唯一本原 Hecke 特征 $\\chi$（模 $\\mathfrak m$），使 $L(\\rho,s)=L(\\chi,s)$；且 Euler 乘积的 $\\mathfrak p$-分量对一切素理想 $\\mathfrak p$ 相等，即 $\\rho(\\sigma_{\\mathfrak p})=\\chi(\\mathfrak p)$（对与 $\\mathfrak m$ 互素的 $\\mathfrak p$）。",
                "proof": {
                    "steps": [
                        "由类域论，$\\rho$ 对应 $K$ 的一个射线类特征 $\\chi$；逐位比较 $\\mathfrak p$-Euler 因子即可。",
                        "导子与权由 $\\rho$ 的分歧与无穷位行为决定（注 5.10），故 $\\chi$ 唯一。",
                    ],
                    "gap_note": "书中把类域论作为已知工具引用，未证明存在性；脚注 6 提醒：$K\\ne\\mathbb Q$ 时「局部相等」强于「整体 L 相等」。",
                },
                "source": "ch01.tex:504-516（§5，定理 5.9）",
            }
        ],
    ),
    card(
        "ch2-euler-vonstaudt", "L",
        "Euler 乘积与 von Staudt",
        ["von Staudt–Clausen", "Bernoulli 数", "L 函数的极点"],
        "L 函数的极点总由 $\\zeta$ 的极点解释；Serre 观察到 $\\zeta(1-k)=-b_k/k$，而 von Staudt–Clausen 定理把 $b_k$ 分母的素数写成 $p-1\\mid k$。",
        "为什么说 L 函数在 $s=1$ 的极点「只能来自 zeta」，模 $p$ 的极点又为何仍由调和级数解释？",
        "第 2 章 §5 讨论「零碎内容，包括极点」。酉归一化之后，$s=1$ 是 L 函数唯一可能的极点，而且总由 $\\zeta$ 的单极点解释：书中举出 $L(f,s)=\\zeta(s)^kL(f_1,s)$ 的三种来源——Dedekind zeta、Rankin–Selberg（对称平方）、Artin（Brauer 诱导），极点的阶数等于平凡表示的重数。这条原则的算术影子是 Serre 的观察：$\\zeta(1-k)=-b_k/k$（(5.1)），于是负整数处的值与 Bernoulli 数挂钩；von Staudt–Clausen 定理给出 $b_k$ 分母的素数分解，从而「模 $p$ 的极点」仍由调和级数 $\\sum1/n$ 解释。书中还提到 Tate 猜想与 Leopoldt 的 $p$ 进 zeta，把这条线索延伸到 $p$ 进世界。",
        "$b_k$：Bernoulli 数；$\\zeta(1-k)$：负整数处的 zeta 值；$p-1\\mid k$：von Staudt–Clausen 的整除条件；$L(f,s)=\\zeta(s)^kL(f_1,s)$：极点分解。",
        [
            "「极点来自 $\\zeta$」是结构性的：只要 L 函数来自自守表示（或 Artin 表示），极点就由平凡表示的重数决定，而平凡表示的 L 就是 $\\zeta$。",
            "von Staudt–Clausen 把 Bernoulli 数分母的算术（$p-1\\mid k$）暴露出来，这正是模 $p$ 极点的来源：分母含 $p$ 当且仅当 $p-1\\mid k$。",
            "书中的 $p-1\\mid2k$ 与随后同余式 $x^{k-1}\\equiv x^{-1}\\pmod p$ 不自洽；标准定理是 $p-1\\mid k$（$k$ 偶），中译注本已出译注。",
        ],
        [
            "\\zeta(1-k)=-\\frac{b_k}{k}\\qquad(k\\ge1)",
            "\\operatorname{denom}(b_k)=\\prod_{p-1\\mid k}p\\qquad(k\\ \\text{偶})",
            "L(f,s)=\\zeta(s)^{k}L(f_1,s)",
        ],
        [
            "把「极点阶数 = 平凡表示重数」当成对所有 Dirichlet 级数成立：它要求 L 来自自守表示或 Artin 表示；一般的 Dirichlet 级数没有这个性质。",
            "照抄书中的 $p-1\\mid2k$：von Staudt–Clausen 的标准形式是 $p-1\\mid k$（$k$ 偶数）；书中同余式只在 $p-1\\mid k$ 时成立。",
        ],
        [
            {"type": "易错预警", "title": "von Staudt 的整除条件", "text": "中译注本在 §5 出注：原书「$p-1\\mid2k$」与随后的同余不自洽，正确的充分必要条件是 $p-1\\mid k$；译文照录并出译注给出标准形式。引用时务必用 $p-1\\mid k$，否则 $p=5$、$k=2$ 之类的例子会立刻矛盾。"},
            {"type": "背景直觉", "title": "调和级数是唯一真正发散的级数", "text": "书中这句话的意思是：正系数 Dirichlet 级数在收敛边界处若有极点，其发散必须由 $\\sum1/n$ 提供；Landau 定理把「正系数 ⇒ 实轴上有奇点」严格化。所以「极点来自 $\\zeta$」并不是巧合，而是正系数与 Euler 乘积共同强制的。"},
        ],
        ["ch2-nonvanishing", "ch1-zeta-euler"],
        [
            src(2, "§5", [36, 37], "ch02.tex:498-529"),
        ],
    ),
    card(
        "ch2-nonvanishing", "L",
        "非主特征 L 函数的非 vanishing",
        ["L(χ,1)≠0", "Landau–Siegel 零点", "Siegel 定理"],
        "Dirichlet 定理归结为 $L(\\chi,1)\\ne0$；实特征情形靠类数公式与 Siegel 下界 $L(\\chi,1)\\gg_\\varepsilon q^{-\\varepsilon}$，但 Siegel 的方法非实效。",
        "非主特征的 $L(\\chi,1)$ 为什么可能接近 $0$，Landau–Siegel 零点又如何阻碍实效下界？",
        "Dirichlet 定理等价于：每个非主特征都满足 $L(\\chi,1)\\ne0$。非实特征容易处理：若 $L(\\chi,1)=0$，则 $L(\\overline\\chi,1)=0$，乘积 $\\zeta(s)L(\\chi,s)L(\\overline\\chi,s)$ 在 $s=1$ 有高于一阶的零点，与 $\\zeta$ 的单极点矛盾。实特征没有这种配对，只能借助类数公式：$L(\\chi,1)$ 小对应虚二次域类数小。定理 3.2 给出无零点区域 $\\sigma>1-c_1/\\log(T^d|D|N\\mathfrak m)$，至多允许一个单重实零点 $\\beta_1$，且只在二次（实）特征时出现，称为 Landau–Siegel 零点。Siegel 的 $L(\\chi,1)\\gg_\\varepsilon q^{-\\varepsilon}$ 是非实效的：常数 $C(\\varepsilon)$ 无法算出。机制是二分法：若存在极小 $L(\\chi,1)$ 的特征 $\\chi_1$，用它靠近 $1$ 的实零点排斥其他零点；若不存在，结论平凡。",
        "$\\beta_1$：可能的 Landau–Siegel 实零点；$\\delta^*(\\mathfrak m)$：其存在性指示；$\\gg_\\varepsilon$：常数依赖 $\\varepsilon$ 而不可算；$h(K)$：类数；$q$：导子。",
        [
            "非实特征用 $L(\\chi,1)L(\\overline\\chi,1)$ 的乘积论证；实特征没有配对，只能靠类数公式与零点排斥。",
            "Siegel 的非实效性来自「不知道 $\\beta_1$ 是否存在」：反证法只能在「若存在则……」的二分法里给出常数，无法判定哪一支成立。",
            "无零点区域与 $L(\\chi,1)\\ne0$ 是两件事：定理 3.2 允许一个 $\\beta_1<1$，它不影响 $s=1$ 处的非零性，但破坏有效的零点排斥。",
        ],
        [
            "L(\\chi,1)\\gg_\\varepsilon q^{-\\varepsilon}\\qquad(\\text{Siegel，非实效})",
            "L(\\chi,1)\\gg\\frac{1}{\\log q},\\qquad h(K)\\gg\\frac{\\sqrt q}{\\log q}\\qquad(\\text{GRH 蕴涵})",
            "\\sigma>1-\\frac{c_1}{\\log(T^d|D|N\\mathfrak m)}\\ \\Longrightarrow\\ L(\\chi,s)\\ne0\\ \\text{（至多一个实零点 }\\beta_1\\text{）}",
        ],
        [
            "把 Siegel 的 $\\gg_\\varepsilon q^{-\\varepsilon}$ 当成可计算的下界：常数 $C(\\varepsilon)$ 无法算出，这是数论中著名的非实效性，与 Thue–Siegel 定理同源。",
            "混淆「无零点区域」与「$L(\\chi,1)\\ne0$」：定理 3.2 允许 $\\beta_1<1$，它不影响 $s=1$ 处的非零性，但使零点排斥论证失去统一常数。",
        ],
        [
            {"type": "易错预警", "title": "β₁ 只在二次（实）特征", "text": "定理 3.2 说那个可能的单重实零点只可能在 $\\chi$ 为二次（实）特征时出现；不要把它安到复特征上。书中还固定 $c_1$ 之后才定义 $\\delta^*(\\mathfrak m)$，因为「是否存在」本身依赖这个常数。"},
            {"type": "背景直觉", "title": "Siegel 二分法", "text": "书中例 3.3 说明：若存在靠近 $1$ 的实零点，类数就小；若不存在，就得到统一的下界。两条路各给一半，故称二分法；正因为无法判定哪一支成立，结论里的常数不可计算。"},
        ],
        ["ch2-goldfeld", "ch1-dirichlet-char", "ch2-euler-vonstaudt"],
        [
            src(2, "§3", [26, 27], "ch02.tex:245-260"),
            src(2, "§3", [27, 29], "ch02.tex:261-300"),
        ],
    ),
    card(
        "ch2-goldfeld", "L",
        "Goldfeld 的椭圆曲线中心零点论证",
        ["Goldfeld 定理", "Gross–Zagier", "中心零点"],
        "Goldfeld 用椭圆曲线 L 在中心点的三阶零点（Gross–Zagier）作杠杆，把 Siegel 的非实效下界改进为实效的 $\\log q/(\\sqrt q\\log\\log q)$。",
        "为什么椭圆曲线中心点的三阶零点，能反过来给出类数/Dirichlet L 的实效下界？",
        "Siegel 的下界非实效，Goldfeld 的定理是目前唯一已知的实效改进。它的杠杆不是「假设存在坏特征」，而是一个真正有实零点的 L 函数：Gross–Zagier 定理给出秩 $1$ 椭圆曲线在其中心点的单零点；对秩 $3$ 的曲线（例如导子 $5077$ 的那条）可算出中心零点恰为三阶，这正是论证所需。这些零点在本章的酉归一化下位于中心点 $s=1/2$（椭圆曲线的经典归一化把它记作 $s=1$），与 $s=1$ 相距 $1/2$，故「排斥力」弱，结果只比平凡界多一个对数因子：$L(\\chi,1)\\gg\\log q/(\\sqrt q\\log\\log q)$，常数已由 Oesterlé 算出。",
        "$E$：椭圆曲线；$L(E,s)$：其 L 函数；$\\operatorname{rank}E$：Mordell–Weil 秩；导子 $5077$：书中用作三阶零点的例子；$s=1/2$：酉归一化的中心点。",
        [
            "Gross–Zagier：秩 $1$ 椭圆曲线的 L 在中心有单零点，且导数与 Heegner 点的高度有关；这是「解析秩 = 代数秩」的第一个一般情形。",
            "Goldfeld 的杠杆是「三阶」而非「一阶」：中心零点阶数越高，排斥实零点的力量越强；但中心点距 $s=1$ 只有 $1/2$，故只多出一个 $\\log$ 因子。",
            "书中的归一化要留意：第 2 章的 $L(\\chi,s)$ 的算术位置是 $s=1$（$\\zeta$ 的极点），而椭圆曲线 L 的中心是 $s=1/2$（酉归一化）。",
        ],
        [
            "L(E,s)\\ \\text{在 }s=1/2\\text{ 有单零点}\\qquad(\\operatorname{rank}E=1,\\ \\text{Gross--Zagier})",
            "L(E,s)\\ \\text{在 }s=1/2\\text{ 有三阶零点}\\qquad(E:\\ \\text{导子 }5077)",
            "L(\\chi,1)\\gg\\frac{\\log q}{\\sqrt q\\,\\log\\log q}\\qquad(\\text{Goldfeld，实效})",
        ],
        [
            "把 Gross–Zagier 当成「所有椭圆曲线」：它给的是秩 $1$ 情形的单零点；三阶零点是另一个（秩 $3$）例子，书中用导子 $5077$ 的曲线。",
            "把 $s=1/2$ 与 $s=1$ 混用：第 2 章的 $L(\\chi,s)$ 的算术关注点是 $s=1$（$\\zeta$ 的极点所在），椭圆曲线 L 的中心在 $s=1/2$（酉归一化；经典归一化记作 $s=1$）。书中明说两者相距 $1/2$，这使 Goldfeld 的结论只多一个对数因子。",
        ],
        [
            {"type": "背景直觉", "title": "为什么三阶零点更强", "text": "若 $L(E,s)$ 在中心有三阶零点，则对每个 $\\chi$ 的 twist，中心附近被迫有零点；函数方程把这些零点「反射」到 $\\chi$ 的 L 函数在 $1$ 附近，从而排斥 $\\beta_1$。阶数越高，排斥区间越宽，但仍只到 $1-O(1/\\log q)$。"},
            {"type": "含糊点拨", "title": "只多一个对数因子", "text": "书中说 Goldfeld 的下界比 Siegel 的 $q^{-\\varepsilon}$ 弱（多 $\\log$ 因子），原因是中心点 $1/2$ 与 $1$ 的距离固定为 $1/2$，twist 的导子只能把零点推到 $1-O(1/\\log q)$ 处，无法更远。这是「杠杆位置」而非「杠杆长度」的限制。"},
        ],
        ["ch2-nonvanishing", "ch2-explicit-formula", "ch1-dedekind-zeta"],
        [
            src(2, "§3", [29, 31], "ch02.tex:271-300"),
        ],
    ),
    card(
        "ch2-explicit-formula", "L",
        "L 函数的零点与显式公式",
        ["显式公式", "零点计数", "Hadamard 乘积"],
        "显式公式把素数幂上的 von Mangoldt 和写成极点主项、零点求和与阿基米德积分三项；零点计数 $N(\\chi;T)$ 的主项来自 $\\Gamma$ 因子。",
        "显式公式为什么能把「素数的分布」与「L 函数零点的位置」精确地等同起来？",
        "命题 3.1 给出零点计数：$N(\\chi;T)=\\frac{T}{2\\pi}\\log\\frac{T^d|D|N\\mathfrak m}{(2\\pi e)^d}+O(\\log(T^d|D|N\\mathfrak m))$，且 $\\sum_\\rho|\\rho|^{-1-\\varepsilon}$ 绝对收敛。证明用 Cauchy 定理在矩形上积分 $\\Lambda'/\\Lambda$，主要贡献来自 $\\Gamma$ 因子，其余由 Hadamard 乘积控制。$\\operatorname{Re}(s)=1$ 上无零点（1896 年 Hadamard 与 de la Vallée Poussin）是无零点区域与素理想定理的关键。命题 3.5 的显式公式 (3.6) 把 $\\sum_{\\mathfrak a}\\Lambda(\\mathfrak a)(\\chi(\\mathfrak a)\\varphi(N\\mathfrak a)+\\overline\\chi(\\mathfrak a)\\psi(N\\mathfrak a))$ 写成 $(\\log|D|N\\mathfrak m)\\varphi(1)+\\delta(\\chi)\\int\\varphi-\\sum_{L(\\chi,\\rho)=0}\\hat\\varphi(\\rho)$ 再加阿基米德积分与 $s=0$ 的留数；检验函数取光滑紧支集时各项绝对收敛，公式是恒等式而非极限。",
        "$N(\\chi;T)$：虚部在 $[-T,T]$ 内的零点数；$\\Lambda(\\mathfrak a)$：von Mangoldt 函数；$\\varphi,\\hat\\varphi$：检验函数与其 Mellin 变换；$\\psi(x)=\\varphi(x^{-1})/x$；$\\delta(\\chi)$：$\\chi$ 平凡时为 $1$，否则为 $0$。",
        [
            "显式公式是「素数 $\\leftrightarrow$ 零点」的精确字典：左边是素数幂上的和，右边是极点主项、零点项与阿基米德项。",
            "主项来自 $s=1$ 的极点（仅 $\\chi$ 平凡时）与 $\\log|D|N\\mathfrak m$；零点项逐项对应非平凡零点；阿基米德项吸收 $\\Gamma'/\\Gamma$。",
            "零点计数的主项 $\\frac{T}{2\\pi}\\log(T^d|D|N\\mathfrak m)$ 中 $1/2\\pi$ 与 $d\\log T$ 都来自 $\\Gamma$ 因子——「零点密度由无穷处的局部因子控制」。",
        ],
        [
            "N(\\chi;T)=\\frac{T}{2\\pi}\\log\\frac{T^d|D|N\\mathfrak m}{(2\\pi e)^d}+O\\bigl(\\log(T^d|D|N\\mathfrak m)\\bigr)",
            "\\sum_{\\mathfrak a}\\Lambda(\\mathfrak a)\\bigl(\\chi(\\mathfrak a)\\varphi(N\\mathfrak a)+\\overline\\chi(\\mathfrak a)\\psi(N\\mathfrak a)\\bigr)=(\\log|D|N\\mathfrak m)\\varphi(1)+\\delta(\\chi)\\int_0^{\\infty}\\varphi-\\sum_{L(\\chi,\\rho)=0}\\hat\\varphi(\\rho)+\\cdots",
            "\\Lambda(\\chi,s)=e^{a+bs}\\prod_{\\rho}\\bigl(1-\\frac{s}{\\rho}\\bigr)e^{s/\\rho}\\qquad(\\chi\\ne1)",
        ],
        [
            "照抄书中 (3.6) 的下标 $\\zeta(\\rho)=0$：应为 $L(\\chi,\\rho)=0$，否则会漏掉全部 $L(\\chi,s)$ 的零点（中译注本已出译注）。",
            "忽略 $\\delta(\\chi)$ 项：只有 $\\chi$ 平凡时才有 $\\int\\varphi$ 项（对应 $\\zeta$ 在 $s=1$ 的极点）；非平凡时该项为零。",
        ],
        [
            {"type": "易错预警", "title": "ζ(ρ) 是笔误", "text": "中译注本在 (3.6) 后出注：影印作 $\\zeta(\\rho)=0$，是照抄第 1 章 (2.5) 未改符号；一般情形必须写 $L(\\chi,\\rho)=0$。同一段的伽马项与 $-L'/L$ 都写明取自 $L(\\chi,\\cdot)$，可见下标确是排印疏漏。"},
            {"type": "背景直觉", "title": "为什么零点计数主项来自 Γ", "text": "用 Cauchy 定理在矩形上积分 $\\Lambda'/\\Lambda$，主要贡献来自 $\\Gamma'/\\Gamma$（Stirling 公式给 $T\\log T$），而 $L'/L$ 的贡献被 Hadamard 乘积控制为 $O(\\log)$。这就是「零点密度由阿基米德因子决定」的机制，也是显式公式里 $\\log|D|N\\mathfrak m$ 出现的原因。"},
        ],
        ["ch2-nonvanishing", "ch1-gamma-factor", "ch2-goldfeld"],
        [
            src(2, "§3", [26, 27], "ch02.tex:231-261"),
            src(2, "§3", [30, 32], "ch02.tex:332-360"),
        ],
    ),
    card(
        "ch2-hecke-gross", "L",
        "Hecke L 与 Gross 的类比",
        ["Gross 的类比", "Hecke L 函数", "中心零点与特殊值"],
        "Hecke L 把 Dirichlet L 搬到数域与射线类群；Gross–Zagier 型「中心导数 = 算术不变量」的类比，把 Hecke L 与椭圆曲线 L 的中心零点并置。",
        "Hecke L 与椭圆曲线 L 的函数方程结构相似，为什么中心点的零点能承载算术信息？",
        "Hecke L 的函数方程 (5.4) $\\Lambda(\\chi,s)=\\varepsilon(\\chi)(|D|N\\mathfrak m)^{1/2-s}\\Lambda(\\overline\\chi,1-s)$ 与椭圆曲线 L 的函数方程形状相同：都是「导子 $\\times$ 完备化 $\\times$ 根数」的对称形式，函数方程的对称中心都在 $s=1/2$。差别在于算术关注点：Hecke/Dirichlet L 的关键位置是 $s=1$（$\\zeta$ 的极点与非 vanishing 的战场），而椭圆曲线 L 的中心点在酉归一化下是 $s=1/2$（经典归一化记作 $s=1$）。第 2 章 §3 的 Goldfeld 论证正是利用这一点：Gross–Zagier 给出秩 $1$ 椭圆曲线中心点的单零点，$\\chi$ 的 twist 把中心零点「反射」到 $\\chi$ 的实零点 $\\beta_1\\approx1$ 附近，从而排斥 Landau–Siegel 零点。这个「中心导数 = 算术不变量」的模式（Heegner 点高度、Petersson 范数、类数公式）就是书中反复出现的「特殊值 ↔ 算术」类比；中译注本把它与 Gross–Zagier 并提，但未把它命名为定理。",
        "$\\Lambda(\\chi,s)$：完备化 Hecke L；$\\varepsilon(\\chi)$：根数；$\\mathfrak m$：模；$|D|N\\mathfrak m$：导子；$s=1/2$：函数方程的对称中心（也是椭圆曲线 L 的酉归一化中心）；$s=1$：$\\zeta$ 的极点与 Dirichlet 非 vanishing 的位置。",
        [
            "两种 L 的局部因子形状一致（一次项、二次项），函数方程的「导子 $\\times$ 完备化 $\\times$ 根数」结构也一致；差别在算术关注点（$s=1$ 与椭圆曲线的中心）与阿基米德因子的具体形状。",
            "Gross–Zagier 是「中心导数 = 算术不变量」的第一个一般定理：秩 $1$ 时 $L'(E,1)$ 与 Heegner 点高度成正比；这给 Goldfeld 提供了真正的实零点杠杆。",
            "书中并没有把「Gross 的类比」列为一条定理；这里按上下文把它理解为「Hecke L 的特殊值/中心零点 ↔ 椭圆曲线 L 的中心导数」这一类比的统称。",
        ],
        [
            "\\Lambda(\\chi,s)=\\varepsilon(\\chi)\\,(|D|N\\mathfrak m)^{1/2-s}\\,\\Lambda(\\overline\\chi,1-s)",
            "\\Lambda(E,s)=\\varepsilon(E)\\,N^{1-s}\\,\\Lambda(E,2-s)\\qquad(\\text{权 }2\\text{ 的椭圆曲线 L})",
            "L'(E,1)\\ \\sim\\ \\hat h(P)\\qquad(\\operatorname{rank}E=1,\\ P\\in E(K)\\ \\text{Heegner 点})",
        ],
        [
            "把「极点所在 $s=1$」当成「函数方程中心」：Dirichlet/Hecke L 的函数方程中心也是 $s=1/2$，但算术关注点是 $s=1$（$\\zeta$ 的极点与非 vanishing）；椭圆曲线 L 在经典归一化下中心记作 $s=1$，酉归一化下才是 $s=1/2$。混用会把 Goldfeld 论证里「相距 $1/2$」的来源说错。",
            "把「Gross 的类比」当成书中的定理名：原书第 2 章只在 Goldfeld 段提到 Gross–Zagier，没有「Gross 类比」这一条；引用时应说明这是整理性的说法。",
        ],
        [
            {"type": "含糊点拨", "title": "类比不是定理", "text": "任务式的问题把「Hecke L 与 Gross 的类比」当成一个主题，但原书第 2 章只在 §3 的 Goldfeld 段出现 Gross–Zagier，且未命名任何「Gross 类比」。本卡按上下文把它整理为「中心导数 = 算术不变量」的类比，并在批注里标明这一点，避免把它误读成书中定理。"},
            {"type": "背景直觉", "title": "为什么中心点特殊", "text": "函数方程 $s\\leftrightarrow1-s$（或 $s\\leftrightarrow2-s$）把中心点固定下来；中心点的零点阶数在函数方程下不变，因此是「算术不变量」最自然的栖身处。BSD 猜想把中心零点的阶数等同于 Mordell–Weil 秩，Gross–Zagier 则给出阶数为 $1$ 时的定量版本。"},
        ],
        ["ch1-dedekind-zeta", "ch2-goldfeld", "ch2-nonvanishing"],
        [
            src(2, "§2", [21, 24], "ch02.tex:11-70"),
            src(2, "§3", [29, 31], "ch02.tex:281-300"),
        ],
    ),
    card(
        "ch3-three-motives", "M",
        "自守形式的三个动机",
        ["三个动机", "theta 函数", "行列式方程", "椭圆曲线不变量"],
        "Kowalski 用三条线索引入自守形式：theta 的函数方程、行列式方程解的矩、椭圆曲线模不变量；共同点是 $\\mathrm{SL}(2,\\mathbb Z)$ 的变换公式。",
        "为什么 theta 函数、行列式方程解数与椭圆曲线不变量会指向同一类对象（自守形式）？",
        "第 3 章 §2 给出三个动机。2.1 theta：$\\theta(z)=\\sum_{n\\in\\mathbb Z}e(n^2z/2)$ 满足 $\\theta(-1/z)=(-iz)^{1/2}\\theta(z)$ 与 $\\theta(z+1)=\\theta(z)$，$\\theta(2z)^k$ 的 Fourier 系数是表示数 $r_k(n)$。2.2 行列式方程的解数：对矩阵计数得矩 $I_k(T)$，四阶矩化为 Kloosterman 和。2.3 椭圆曲线的不变量：格、$\\tau'=\\gamma\\tau$、$g(z;\\gamma\\tau)=(c\\tau+d)^k g(z;\\tau)$，例 2.1 的 $\\wp$ 函数与 $G_k$ 给出 Weierstrass 系数。三条线索的共同结构是：$\\mathrm{H}$ 上的全纯函数在 $z\\mapsto z+1$ 与 $z\\mapsto-1/z$ 下有确定的变换公式；这两个变换生成 $\\mathrm{PSL}(2,\\mathbb Z)$，于是「自守性」成为一个可验证的有限条件。",
        "$\\theta$：theta 函数；$e(z)=e^{2\\pi iz}$；$r_k(n)$：$n$ 表示为 $k$ 个平方和的方法数；$I_k(T)$：矩；$\\wp$：Weierstrass 椭圆函数；$G_k$：Eisenstein 系数；$\\gamma=\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix}\\in\\mathrm{SL}(2,\\mathbb Z)$。",
        [
            "三条动机不是三个应用，而是同一变换群的三个来源：theta 的 Poisson 求和、矩阵计数的模空间、格的不变量。",
            "$\\theta$ 的 $(-iz)^{1/2}$ 是自守因子（乘子）的雏形：它不是常数，而是 $z$ 的全纯函数，换分支会改号。",
            "2.2 的矩与 2.3 的 $\\wp$ 展开都产生「Fourier 系数 $\\times$ 幂次」的结构，这正是模形式 Fourier 展开的来源。",
        ],
        [
            "\\theta(z)=\\sum_{n\\in\\mathbb Z}e\\bigl(n^2z/2\\bigr),\\qquad \\theta\\bigl(-\\tfrac1z\\bigr)=(-iz)^{1/2}\\theta(z)",
            "\\theta(2z)^k=\\sum_{n\\ge0}r_k(n)e(nz),\\qquad r_2(n)=4\\sum_{d\\mid n}\\chi_4(d)",
            "g(z;\\gamma\\tau)=(c\\tau+d)^{k}g(z;\\tau)",
        ],
        [
            "把 $\\theta(z)$ 当成权 $1/2$ 的模形式：它满足的是带分支的变换公式（乘子系），不是标量权；严格说是 $\\Gamma_0(4)$ 上的半整数权形式。",
            "忘记 $z\\mapsto z+1$ 与 $z\\mapsto-1/z$ 只是生成元：验证自守性要在整个 $\\mathrm{PSL}(2,\\mathbb Z)$（或有限指数子群）上验证，生成元足够但乘子必须相容。",
        ],
        [
            {"type": "背景直觉", "title": "为什么是 SL(2,Z)", "text": "$\\theta$ 的 $1$-周期性给 $z\\mapsto z+1$，Poisson 求和给 $z\\mapsto-1/z$；两者生成 $\\mathrm{PSL}(2,\\mathbb Z)$。任何在这两个生成元下有变换公式的全纯函数，自动对整个群有公式——这正是「自守」的定义方式，也是为什么三个动机都落到同一个群上。"},
            {"type": "含糊点拨", "title": "r_k(n) 的初等公式为何只到 8", "text": "书中说模形式理论能解释 $r_k(n)$ 公式的一般形状，并说明 $k$ 大时为何没有「初等」公式：模形式空间维数随 $k$ 增长，Eisenstein 部分与尖点部分的比例改变，$r_k(n)$ 不再由单个 Eisenstein 级数给出。"},
        ],
        ["ch3-theta-modularity", "ch3-eisenstein-cusp"],
        [
            src(3, "§2", [39, 43], "ch03.tex:13-47"),
        ],
    ),
    card(
        "ch3-theta-modularity", "M",
        "theta 函数与模性",
        ["theta 变换", "Poisson 求和", "半整数权"],
        "$\\theta$ 的函数方程由 Poisson 求和与 $e^{-\\pi x^2}$ 的自对偶得到；$\\theta(2z)^k$ 因此是模形式，把二次型的表示数变成 Fourier 系数。",
        "theta 的函数方程为什么能同时给出 $\\zeta$ 的函数方程与 $r_k(n)$ 的模性？",
        "核心分析事实只有一个：$e^{-\\pi x^2}$ 的 Fourier 变换是它自己。Poisson 求和把它变成 $\\theta(-1/z)=(-iz)^{1/2}\\theta(z)$；再加上 $\\theta(z+1)=\\theta(z)$，就得到 $\\theta$ 在 $\\mathrm{SL}(2,\\mathbb Z)$ 生成元下的变换公式。于是 $\\theta(2z)^k=\\sum r_k(n)e(nz)$ 是（半整数权）模形式，$r_2,r_4,r_6$ 的经典公式由此推出。高秩推广：对正定偶整二次型 $A$，$\\Theta(z;A)=\\sum_{m\\in\\mathbb Z^r}e(\\tfrac12{}^tmAm\\,z)$ 属于 $M_{r/2}(2N)$（例 3.6、命题 3.7）；反向的 theta 对应把模形式与二次型的表示数联系起来。第 2 章用同一套 Poisson 求和证明 $\\zeta$ 与 Dedekind zeta 的函数方程，只是把 $e^{-\\pi x^2}$ 换成 $f(x)=x^{-s}$ 的「非 Schwartz」困难用截断/伽马积分绕开。",
        "$\\theta$：Jacobi theta；$r_k(n)$：$k$ 元平方和表示数；$A$：$r\\times r$ 正定偶整对称矩阵；$N$：使 $NA^{-1}$ 整的正整数；$M_{r/2}(2N)$：权 $r/2$、level $2N$ 的模形式空间。",
        [
            "关键分析事实只有一个：$e^{-\\pi x^2}$ 的 Fourier 变换是它自己；Poisson 求和把它变成 $\\theta$ 的变换公式。",
            "$\\theta$ 是模形式但不是 $\\mathrm{SL}(2,\\mathbb Z)$ 上的标量形式：它有乘子 $(-iz)^{1/2}$，属半整数权、level 4（或 $2N$）。",
            "二次型 $A$ 的 theta 级数把「表示数」变成 Fourier 系数，因此模形式空间的有限维性给出 $r_k(n)$ 的线性关系。",
        ],
        [
            "\\theta\\bigl(-\\tfrac1z\\bigr)=(-iz)^{1/2}\\theta(z),\\qquad \\theta(z+1)=\\theta(z)",
            "\\Theta(z;A)=\\sum_{m\\in\\mathbb Z^{r}}e\\bigl(\\tfrac12\\,{}^{t}mAm\\,z\\bigr)\\in M_{r/2}(2N)",
            "\\sum_{n\\ge0}r_k(n)e(nz)=\\theta(2z)^{k}",
        ],
        [
            "把 $(-iz)^{1/2}$ 当成常数：它是 $z$ 的函数（$\\mathrm{H}$ 上的全纯分支），换分支会改变符号；这正是「乘子系」而非「标量权」的意思。",
            "以为 $\\theta$ 的模性只对二次型：$\\Theta(z;A)$ 的 level 由 $A$ 的判别式/整性条件决定（例 3.6 要求 $A$ 整、对角偶、$NA^{-1}$ 整），不是固定 $4$。",
        ],
        [
            {"type": "背景直觉", "title": "theta 对应", "text": "命题 3.7 把「偶整二次型」映到「半整数权模形式」；反过来，模形式的 Fourier 系数若来自 theta，就满足二次型的表示数恒等式。这是 Langlands 函子性（theta 提升）的经典特例，也是第 3 章 §6.3 用 theta 处理二次域的伏笔。"},
            {"type": "易错预警", "title": "权与 level", "text": "$\\Theta(z;A)$ 的权是 $r/2$（$r$ 为变量个数），level 是 $2N$；$r$ 奇时是半整数权，需要 metaplectic 的语言，不能直接套 $\\mathrm{SL}(2,\\mathbb Z)$ 的模形式定义。书中例 3.6 的条件「$A$ 整、对角偶、$NA^{-1}$ 整」正是为了保证变换公式在 $\\Gamma_0(2N)$ 上闭合。"},
        ],
        ["ch3-three-motives", "ch3-modular-l", "ch3-eisenstein-cusp"],
        [
            src(3, "§2.1", [39, 40], "ch03.tex:17-47"),
            src(3, "§3", [50, 51], "ch03.tex:359-390"),
        ],
    ),
    card(
        "ch3-eisenstein-cusp", "M",
        "Eisenstein 级数与尖点形式",
        ["Eisenstein series", "cusp form", "尖点"],
        "Eisenstein 级数是对 $\\Gamma$ 的陪集求平均得到的「连续谱」；尖点形式在 Fourier 展开中无常数项。两者构成 $M_k=S_k\\oplus E_k$。",
        "Eisenstein 级数与尖点形式在模形式空间里各自扮演什么角色，为什么必须分开？",
        "例 3.4 说明：若函数已在子群 $G_1<G$ 下不变，只需对 $G_1$ 在 $G$ 中的陪集求平均。由此得到 Poincaré 级数 $P_m$ 与 Eisenstein 级数 $E_k(z)=\\sum_{(a,b)=1}(az+b)^{-k}$；当 $m=0$ 时 $P_0$ 就是 Eisenstein 级数，$m\\ne0$ 时 $P_m$ 是尖点形式。Eisenstein 级数的 Fourier 展开（例 4.2）含 $\\zeta(1-k)$ 的常数项，一般不为零；尖点形式的常数项为零。于是 $M_k=S_k\\oplus E_k$（尖点部分与 Eisenstein 部分直和），Petersson 内积下两部分正交。Hecke 理论在 $S_k$ 上给出正交特征基（推论 5.5），这是「离散谱」；Eisenstein 级数则对应「连续谱」，在 Rankin–Selberg 积分中作为核出现。",
        "$\\Gamma_\\infty$：$\\mathrm{SL}(2,\\mathbb Z)$ 的抛物子群；$P_m$：第 $m$ 个 Poincaré 级数；$E_k$：权 $k$ Eisenstein 级数；$S_k$：尖点形式空间；$M_k$：模形式空间；$\\Delta$：权 $12$ 尖点形式。",
        [
            "Eisenstein 级数 = 由抛物子群诱导的表示对应的「连续谱」；它的 Fourier 常数项不为零，反映极点/常数项。",
            "尖点形式 = 在所有尖点处衰减的部分；它们构成有限维空间，Hecke 算子在其上有正交特征基（推论 5.5）。",
            "「尖点」不是几何点而是 $\\Gamma\\backslash\\mathrm{H}$ 的边界点；在尖点处消失等价于该尖点处 Fourier 展开的常数项为 $0$。",
        ],
        [
            "E_k(z)=\\sum_{(a,b)=1}\\frac{1}{(az+b)^{k}}=\\sum_{\\gamma\\in\\Gamma_\\infty\\backslash\\Gamma}\\gamma\\cdot z^{-k}",
            "\\Delta(z)=q\\prod_{n\\ge1}(1-q^{n})^{24}=\\sum_{n\\ge1}\\tau(n)q^{n},\\qquad q=e^{2\\pi iz}",
            "M_k=S_k\\oplus E_k",
        ],
        [
            "把「尖点形式」等同于「在 $\\infty$ 处消失」：必须在所有尖点处消失；对 $\\Gamma_0(q)$，各尖点的宽度不同，Fourier 展开要按伸缩矩阵 $\\sigma_a$ 逐点写。",
            "把 Eisenstein 级数的常数项当成 $0$：它含 $\\zeta(1-k)$（例 4.2），一般非零；这正是 Eisenstein 部分与尖点部分的判别标志。",
        ],
        [
            {"type": "易错预警", "title": "两种 q", "text": "模形式里的 $q=e^{2\\pi iz}$（局部坐标）与 level 的 $q$ 是同一个字母，书中专门出注提醒；读公式时先看 $q$ 出现在 $e(\\cdot)$ 里还是 $\\Gamma_0(q)$ 里。这个混淆在第 3 章反复出现。"},
            {"type": "背景直觉", "title": "Eisenstein = 诱导表示", "text": "例 3.4 把 Eisenstein 级数写成对陪集 $\\Gamma_\\infty\\backslash\\Gamma$ 的平均；表示论上这就是从抛物子群的平凡表示诱导。尖点形式则是「离散谱」，与 Eisenstein 的连续谱在 Petersson 内积下正交——这正是谱分解 $L^2(\\Gamma\\backslash\\mathrm{H})=L^2_{\\mathrm{cusp}}\\oplus L^2_{\\mathrm{Eis}}$ 的经典情形。"},
        ],
        ["ch3-three-motives", "ch3-hecke-operators", "ch3-modular-l"],
        [
            src(3, "§3", [43, 45], "ch03.tex:300-330"),
            src(3, "§4.2", [52, 54], "ch03.tex:455-495"),
        ],
    ),
    card(
        "ch3-hecke-operators", "M",
        "Hecke 算子与特征形式",
        ["Hecke operators", "Hecke eigenform", "Atkin–Lehner"],
        "Hecke 算子 $T(n)$ 在模形式空间上交换、自伴，因而可同时对角化；本原特征形式的 L 函数有 Euler 乘积，特征值 $\\lambda_f(p)$ 即 Euler 因子系数。",
        "Hecke 算子为什么能同时对角化，特征值又为什么恰好是 L 函数 Euler 因子的系数？",
        "§5 定义 Hecke 算子 $T(n)$（双陪集 $\\Gamma\\operatorname{diag}(n)\\Gamma$ 的作用）。引理 5.1 给出 $T(p)$ 对 Fourier 系数的作用；引理 5.2 证明 $T(m)T(n)=T(mn)$（$(m,n)=1$）与 $T(p)T(p^r)=T(p^{r+1})+p^{k-1}T(p^{r-1})$（level 1），由此得 Euler 乘积（推论 5.3）。引理 5.4 证明 $T(n)$ 在 Petersson 内积下自伴（正规），故可同时对角化；推论 5.5 给出 Hecke 形式的正交基与特征值 $\\lambda_f(n)$。定理 5.7（Atkin–Lehner）证明新空间中本原形式的重数为 $1$；推论 5.8 给出本原形式的 Euler 乘积。特征值 $\\lambda_f(n)$ 就是 $L(f,s)=\\sum\\lambda_f(n)n^{-s}$ 的系数，也是 Euler 因子 $1-\\lambda_f(p)p^{-s}+\\chi(p)p^{k-1-2s}$ 的一次项系数。",
        "$T(n)$：第 $n$ 个 Hecke 算子；$\\lambda_f(n)$：特征值；$S_k(q,\\chi)$：权 $k$、level $q$、旁特征 $\\chi$ 的尖点形式空间；$S_k(q,\\chi)^{*}$：新空间；$W$：Fricke 对合。",
        [
            "交换性来自双陪集乘法的结合律（引理 5.2），自伴性来自 Petersson 内积的不变性（引理 5.4）；两者合起来给出正交特征基。",
            "特征值 $\\lambda_f(n)$ 就是 $L(f,s)$ 的 Euler 因子系数：$T(n)f=\\lambda_f(n)f$ 与 $L(f,s)=\\sum\\lambda_f(n)n^{-s}$ 是同一件事的两面。",
            "本原形式（newform）才满足精确的 Euler 乘积；旧形式来自更低 level，Euler 因子会退化（推论 5.8 的条件）。",
        ],
        [
            "T(n)f=\\lambda_f(n)f,\\qquad L(f,s)=\\sum_{n\\ge1}\\lambda_f(n)n^{-s}=\\prod_{p}\\bigl(1-\\lambda_f(p)p^{-s}+\\chi(p)p^{k-1-2s}\\bigr)^{-1}",
            "T(p)T(p^{r})=T(p^{r+1})+p^{k-1}T(p^{r-1})\\qquad(\\text{level }1)",
            "\\langle T(n)f,g\\rangle=\\langle f,T(n)g\\rangle\\qquad(\\text{Petersson})",
        ],
        [
            "把 $T(n)$ 当成「乘以 $n$」：$T(n)$ 是双陪集上的平均（对应 $n$ 阶同源），一般不是标量；只有在特征形式上才等于 $\\lambda_f(n)$。",
            "忽略 level 与旁特征：$\\Gamma_0(q)$ 上 $T(p)$ 的定义依赖 $p\\mid q$ 与否（$p\\mid q$ 时是退化算子），Euler 因子在坏素数处不同。",
        ],
        [
            {"type": "易错预警", "title": "本原形式 vs Hecke 形式", "text": "推论 5.8 的 Euler 乘积要求 $f$ 是本原形式（newform）；一般的 Hecke 形式若来自旧空间，$L(f,s)$ 会多出有限个坏因子。书中用旧空间/新空间 $S_k(q,\\chi)^{b}$、$S_k(q,\\chi)^{*}$ 区分，读定理时先看下标。"},
            {"type": "背景直觉", "title": "重数一", "text": "定理 5.7（Atkin–Lehner）说新空间里本原形式的重数为 $1$——这是「Hecke 特征值决定形式」的算术版本，也是模形式与 Galois 表示对应的起点：给定特征值系统，模形式与 $\\ell$-进表示都被唯一确定。"},
        ],
        ["ch3-eisenstein-cusp", "ch3-modular-l", "ch3-theta-modularity"],
        [
            src(3, "§5", [57, 60], "ch03.tex:596-670"),
            src(3, "§5", [60, 62], "ch03.tex:671-760"),
        ],
    ),
    card(
        "ch3-modular-l", "M",
        "L 函数与函数方程",
        ["模形式的 L 函数", "函数方程", "Rankin–Selberg"],
        "模形式 $f$ 的 L 级数由 Fourier 系数拼成；Hecke 特征形式给出 Euler 乘积，函数方程来自 $f$ 的模性，Rankin–Selberg 给出二阶 L。",
        "模形式的 L 函数为什么必然满足函数方程，Weil 逆定理又为什么能反过来刻画模形式？",
        "§4.3 定义 $L(f,s)=\\sum a_n n^{-s}$ 与完备化 $\\Lambda(f,s)$（(4.11)–(4.14)）。命题 4.4 证明 $\\Lambda(f,s)$ 整延拓并满足函数方程 $\\Lambda(f,s)=\\varepsilon\\Lambda(\\overline f,k-s)$；推导只用 Mellin 变换 $\\Lambda(f,s)=\\int_0^{\\infty}f(iy)y^{s-1}dy$ 与 $f$ 的模性，$y\\mapsto1/y$ 把 $s$ 换成 $k-s$。§6.1 的 Weil 逆定理（定理 6.1）反向：若 $L(f,s)$ 及所有旁特征 twist 都满足函数方程，则 $f$ 是模形式。§6.2 的 Rankin–Selberg $L(f\\times g,s)$（命题 6.2）给出二阶 L，$s=1$ 的极阶判别 $f=\\overline g$，$s=k$ 的留数对应 Petersson 范数（注 6.5）。§6.3 用 theta 处理二次域（命题 6.6）：二次域的特征对应权 $1$ 全纯形式或权 $1/4$ 的 Maass 形式。",
        "$L(f,s)$：模形式 $f$ 的 L 级数；$\\Lambda(f,s)=(2\\pi)^{-s}\\Gamma(s)L(f,s)$（或带 level 的完备化）；$\\varepsilon$：根数；$L(f\\times g,s)$：Rankin–Selberg L；$S_k(q,\\chi)$：尖点形式空间。",
        [
            "函数方程来自 Mellin 变换：$\\int_0^{\\infty}f(iy)y^{s-1}dy$ 的模性把 $y\\mapsto1/y$ 变成 $s\\mapsto k-s$。",
            "Euler 乘积只在 Hecke 特征形式上成立；一般模形式的 L 级数只是 Dirichlet 级数（但仍有函数方程）。",
            "Weil 逆定理说明「函数方程 + 所有 twist」足以刻画模性；这是「L 函数决定形式」的精确版本，也是模性提升的起点。",
        ],
        [
            "\\Lambda(f,s)=\\int_0^{\\infty}f(iy)y^{s-1}\\,dy=\\varepsilon\\,\\Lambda(\\overline f,k-s)",
            "L(f\\times g,s)=\\sum_{n\\ge1}\\frac{a_nb_n}{n^{s}}\\qquad(\\text{Rankin--Selberg})",
            "\\Lambda(f\\times g,s)\\ \\text{的 }s=1\\text{ 极阶}=1\\iff f=\\overline g",
        ],
        [
            "照抄 (4.13) 的 $L(f,s)$：左端应为 $\\Lambda(f,s)$（完备化后的 L），否则函数方程两边次数不齐；中译注本已径改并出注。",
            "把 Rankin–Selberg 的极点位置记错：注 6.5 说 $s=1$ 处极阶判别 $f=\\overline g$，$s=k$ 处留数对应 Petersson 范数；书中原文把 $s=k$ 印成 $s=1$，注意区分。",
        ],
        [
            {"type": "易错预警", "title": "(4.13) 的左端", "text": "中译注本把原书 (4.13) 左端的 $L(f,s)$ 径改为 $\\Lambda(f,s)$，因为右端是 $\\varepsilon\\Lambda(\\overline f,k-s)$，两边必须是完备化 L 才能对齐；引用原书时需说明这一改动，否则会误以为函数方程对未完备化的 $L$ 成立。"},
            {"type": "背景直觉", "title": "逆定理的分量", "text": "定理 6.1 要求对所有模 $q$ 的 Dirichlet 特征 twist 都满足函数方程，缺一不可；这正是 Weil 把「函数方程」变成「模性判据」的关键——单个函数方程不足以定 $f$，所有 twist 才够。"},
        ],
        ["ch3-hecke-operators", "ch3-theta-modularity", "ch3-eisenstein-cusp"],
        [
            src(3, "§4.3", [55, 56], "ch03.tex:522-595"),
            src(3, "§6.1", [63, 65], "ch03.tex:769-829"),
        ],
        theorems=[
            {
                "name": "定理 6.1（Weil 逆定理）",
                "statement": "设 $f$ 为 $\\mathrm{H}$ 上的全纯函数，$L(f,s)=\\sum a_n n^{-s}$。若对每个模 $q$ 的 Dirichlet 特征 $\\chi$，twist $L(f\\otimes\\chi,s)$ 的完备化都满足函数方程（且 $f$ 满足适度的增长条件），则 $f$ 是 $\\Gamma_0(q)$ 上的模形式。",
                "proof": {
                    "steps": [
                        "对每个 twist 的函数方程做 Mellin 反演，得到 $f$ 在 $\\Gamma_0(q)$ 生成元下的变换公式。",
                        "所有 twist 合起来给出足够的函数方程，使 $f$ 在 $\\Gamma_0(q)$ 上自守。",
                    ],
                    "gap_note": "书中只给定理陈述与思路，未展开「所有 twist」的充分性论证；Weil 原文用的是「函数方程 + 有界性」的版本。",
                },
                "source": "ch03.tex:802-829（§6.1，定理 6.1）",
            }
        ],
    ),
    card(
        "ch4-artin-definition", "L",
        "Artin L 函数的定义",
        ["Artin L-function", "Frobenius 元", "惯性群"],
        "Artin 把 Dirichlet L 从交换群推广到任意 Galois 表示：$L(\\chi,s)=\\prod_v\\det(1-\\sigma_vq_v^{-s}\\mid V^{I_v})^{-1}$，只用惯性不变量上的 Frobenius 作用。",
        "为什么 Artin 的 L 函数必须在惯性不变量 $V^{I_v}$ 上取行列式，而不能直接用 $\\rho(\\sigma_v)$？",
        "本原 Dirichlet 特征 $\\chi\\bmod m$ 对应 $K=\\mathbb Q(\\zeta_m)$、$G\\cong(\\mathbb Z/m\\mathbb Z)^\\times$，Artin 的第一步是 (1.1) $\\chi_{\\mathrm{Gal}}(\\sigma_p)=\\chi(p)$ 与 (1.2) 的 Euler 积。1923 年他把这推广到任意复表示：设 $\\rho:G\\to\\mathrm{GL}(V)$，$\\chi$ 为其特征。对每个素位 $v$，$G_{\\bar v}/I_{\\bar v}$ 作用在 $V^{I_{\\bar v}}$ 上，故 $L_v(\\chi,s)=\\det(1-\\sigma_vq_v^{-s}\\mid V^{I_{\\bar v}})^{-1}$ 良定；对几乎所有 $v$，$V^{I_{\\bar v}}=V$，因子就等于 $\\det(1-\\rho(\\sigma_v)q_v^{-s})^{-1}$。若 $V^{I_{\\bar v}}\\ne V$，称 $v$ 在 $\\rho$ 中分歧；$\\rho$ 忠实时这与 $v$ 在 $K/k$ 中分歧一致。坏位因子「由函数方程好看这一愿望所决定」，并非任意选择。",
        "$G$：Galois 群；$\\rho$：复表示；$\\chi=\\operatorname{tr}\\rho$：特征；$V^{I_{\\bar v}}$：惯性不变量；$\\sigma_v$：Frobenius 元（定义到共轭类）；$q_v$：剩余域基数；$k$：基域。",
        [
            "关键设计是「取惯性不变量」：$v$ 分歧时 $\\sigma_v$ 在 $V$ 上无定义，但在 $V^{I_{\\bar v}}$ 上有定义，故 Euler 因子良定。",
            "对几乎所有 $v$，$V^{I_{\\bar v}}=V$，因子为 $\\det(1-\\rho(\\sigma_v)q_v^{-s})$；坏位因子由整体函数方程与导子唯一确定。",
            "$\\chi$ 是表示的特征，不是一维特征：$L(\\chi,s)$ 只依赖 $\\chi$，但定义要经过 $\\rho$ 的矩阵；同一 $\\chi$ 的不同表示给同一个 L。",
        ],
        [
            "L(\\chi,s)=\\prod_{v}L_v(\\chi,s),\\qquad L_v(\\chi,s)=\\det\\bigl(1-\\sigma_vq_v^{-s}\\mid V^{I_{\\bar v}}\\bigr)^{-1}",
            "\\chi_{\\mathrm{Gal}}(\\sigma_p)=\\chi(p)\\qquad\\bigl(K=\\mathbb Q(\\zeta_m),\\ G\\cong(\\mathbb Z/m\\mathbb Z)^{\\times}\\bigr)",
            "\\log L_v(\\chi,s)=\\sum_{n\\ge1}\\frac{1}{n}\\operatorname{tr}\\bigl(\\sigma_v^{n}\\mid V^{I_{\\bar v}}\\bigr)q_v^{-ns}",
        ],
        [
            "把 $\\sigma_v$ 当成固定的 Frobenius 自同构：它只定义到惯性子群的共轭类，换 $\\bar v$ 会换代表元；取 $V^{I_v}$ 后作用良定，这才是 (3.2) 的意义。",
            "把 $\\chi(1)$ 与 $\\dim V$ 混：$\\chi(1)=\\dim V$，出现在导子/函数方程的指数 $|d_k|^{\\chi(1)}$ 里；不同表示可以有相同维数但不同 $L$。",
        ],
        [
            {"type": "易错预警", "title": "Frobenius 的阶", "text": "书中 §3.1 说 Frobenius 是「$q$ 次幂」自同构（不动域为 $\\mathbb F_q$），不是「$q$ 阶」；原书 \"of order $q$\" 的字面容易被误读，notes 特别提醒译文作「$q$ 次幂的 Frobenius 自同构」。"},
            {"type": "背景直觉", "title": "坏因子的自由度", "text": "作者说坏 Euler 因子「由函数方程好看这一愿望所决定」——这不是循环论证，而是说局部因子被整体函数方程与导子唯一确定（Tate 的局部理论后来给出第一原理）。第 4 章 §4.1–4.2 的 $\\Gamma$ 因子与 Artin 导子正是这套「由整体反推局部」的产物。"},
        ],
        ["ch4-induction", "ch4-conductor-fe", "ch4-artin-hecke"],
        [
            src(4, "§1", [73, 74], "ch04.tex:11-30"),
            src(4, "§3.2", [75, 77], "ch04.tex:109-142"),
        ],
    ),
    card(
        "ch4-induction", "L",
        "分解与诱导",
        ["Brauer 诱导", "Frobenius 互反律", "Artin 表示"],
        "Artin L 对表示可加、对诱导有 (3.12)–(3.13) 的分解；Brauer 定理把任意特征写成单项特征整系数组合，从而把 $L(\\chi,s)$ 化成 Hecke L 的乘积。",
        "Brauer 诱导定理为什么只能给亚纯延拓，而给不了解析延拓？",
        "§3.4 列出初步性质：可加性 (3.12)、诱导 (3.13) $L(\\operatorname{Ind}_H^G\\psi,s)=L(\\psi,s)$、膨胀 (3.14)；类域论情形 (3.15) 与 $\\zeta_K(s)=\\zeta_k(s)\\prod_{\\chi\\ne1}L(\\chi,s)^{\\chi(1)}$ (3.16)。§4.4 的 Brauer 定理（定理 4.2，1947）说：有限群 $G$ 的每个特征都是单项特征 $\\operatorname{Ind}_H^G\\psi$（$\\psi$ 一维）的整系数线性组合。于是 $\\Lambda(\\chi,s)=\\prod_i\\Lambda(\\chi_i,s)^{n_i}$（(4.9)）。证明梗概（Brauer–Tate 1951）：幂零群全单项，再用 $A=\\mathbb Z[\\zeta]$ 与两条构造化到 $p$-初等子群。系数 $n_i$ 可为负，所以只得到亚纯延拓与函数方程；解析性（极点是否相消）正是 Artin 猜想。",
        "$\\operatorname{Ind}_H^G$：诱导表示；$\\psi$：$H$ 的一维特征；$n_i\\in\\mathbb Z$：Brauer 组合的整系数（可负）；$p$-初等子群：$p$-群与循环群的直积；$\\Lambda(\\chi,s)$：完备化 Artin L。",
        [
            "诱导公式 (3.13) 是「L 函数按域塔分解」的表示论版本；膨胀 (3.14) 处理非 Galois/中间域。",
            "Brauer 定理给的是虚拟特征（整系数、可能为负）的组合，因此只能得到亚纯延拓与函数方程；要解析延拓需正系数分解（Artin 猜想）。",
            "交换情形 (3.15)(3.16) 把 $\\zeta_K/\\zeta_k$ 写成 Dirichlet/Hecke L 的乘积，这是 Brauer 分解的最简单实例。",
        ],
        [
            "L(\\operatorname{Ind}_H^G\\psi,s)=L(\\psi,s),\\qquad \\Lambda(\\chi,s)=\\prod_i\\Lambda(\\chi_i,s)^{n_i}",
            "\\zeta_K(s)=\\zeta_k(s)\\prod_{\\chi\\ne1}L(\\chi,s)^{\\chi(1)}",
            "\\sum_i n_i\\operatorname{Ind}_{H_i}^G\\psi_i=\\chi\\qquad(n_i\\in\\mathbb Z)",
        ],
        [
            "把 Brauer 的整系数组合当成「正系数乘积」：$n_i$ 可以为负，故只能谈亚纯；极点/零点可能相消，解析性正是 Artin 猜想的内容。",
            "把诱导与限制搞反：$\\operatorname{Ind}_H^G$ 从 $H$ 的表示造 $G$ 的表示，$L$ 函数不变（(3.13)）；限制 $\\operatorname{Res}$ 则把 $G$ 的表示拉回 $H$，$L$ 函数会分解。",
        ],
        [
            {"type": "易错预警", "title": "诱导作用的方向", "text": "(2.4) 的诱导空间是 $\\{f:G\\to W,\\ f(hg)=\\rho(h)f(g)\\}$（左协变），而 (2.5) 的 $G$-作用是右平移 $f(g'g)$；两者方向相反但相容。notes 特别提醒不要把这两个作用混为同一个，否则 Frobenius 互反律 (2.7) 的配对会对错。"},
            {"type": "背景直觉", "title": "为什么 Brauer 够了", "text": "单项表示是一维表示的诱导，其一维情形由 Hecke/类域论给出解析延拓；Brauer 定理保证任何特征都能由这些「已知块」拼出，代价是系数可能为负。这也解释了为什么 1947 年之后 Artin L 的亚纯延拓与函数方程立刻成为定理，而解析性至今未决。"},
        ],
        ["ch4-artin-definition", "ch4-conductor-fe", "ch1-cft-entry"],
        [
            src(4, "§3.4", [78, 79], "ch04.tex:201-249"),
            src(4, "§4.4", [81, 83], "ch04.tex:311-353"),
        ],
    ),
    card(
        "ch4-conductor-fe", "L",
        "函数方程与导子",
        ["Artin 导子", "Artin 根数", "函数方程"],
        "Artin 导子 $\\mathfrak f(\\chi)=\\prod_vv^{f(\\chi,v)}$ 度量分歧，其整性由 Artin/Hasse–Arf 保证；完备化 $\\Lambda(\\chi,s)$ 满足 $\\Lambda(\\chi,1-s)=W(\\chi)\\Lambda(\\widetilde\\chi,s)$。",
        "Artin 导子的指数 $f(\\chi,v)$ 为什么取 $|G_0|^{-1}\\sum_i|G_i|\\operatorname{codim}V^{G_i}$ 这种形式，它如何进入函数方程？",
        "§4.1 定义 $\\Gamma_{\\mathbb R}(s)=\\pi^{-s/2}\\Gamma(s/2)$、$\\Gamma_{\\mathbb C}(s)=2(2\\pi)^{-s}\\Gamma(s)$，并用 $n_+(\\chi,v)=\\dim V^{G_{\\bar v}}$、$n_-(\\chi,v)=\\dim V/V^{G_{\\bar v}}$ 分配 $\\Gamma_v(s)$ 与 $\\Gamma_v(s+1)$。§4.2 定义高阶分歧群 $G_0\\supset G_1\\supset\\cdots$ 与 $f(\\chi,v)=|G_0|^{-1}\\sum_{i\\ge0}|G_i|\\operatorname{codim}V^{G_i}$，$\\mathfrak f(\\chi)=\\prod_vv^{f(\\chi,v)}$；$f$ 的整性是 Artin 的深刻定理，交换情形即局部类域论的 Hasse–Arf 定理。§4.3 定义 $\\Lambda(\\chi,s)=(|d_k|^{\\chi(1)}N\\mathfrak f(\\chi))^{s/2}\\prod_{v\\mid\\infty}L_v(\\chi,s)\\cdot L(\\chi,s)$，定理 4.1 断言其亚纯延拓并满足 $\\Lambda(\\chi,1-s)=W(\\chi)\\Lambda(\\widetilde\\chi,s)$；证明分两步：类域论处理一维，Brauer 处理一般情形。",
        "$G_i$：第 $i$ 个高阶分歧群；$f(\\chi,v)$：局部导子指数；$\\mathfrak f(\\chi)$：整体 Artin 导子；$d_k$：$k$ 的判别式；$W(\\chi)$：Artin 根数；$\\widetilde\\chi$：反偶特征；$\\Gamma_{\\mathbb R},\\Gamma_{\\mathbb C}$：阿基米德因子。",
        [
            "导子指数是分歧群上的加权平均：$|G_i|$ 递减、$\\operatorname{codim}$ 递增，加权和有限且为整数（Artin 定理）。",
            "阿基米德因子用 $n_+$、$n_-$ 把 $\\Gamma_v(s)$ 与 $\\Gamma_v(s+1)$ 分配；复位的 $G_v$ 平凡，故 $n_+=n_-=\\dim V$，回到 $\\Gamma_{\\mathbb C}^{\\dim V}$。",
            "根数 $W(\\chi)$ 是模 $1$ 复数，局部化后 $W=\\prod_vW_v$，$W_v=\\tau(\\chi_v)/\\sqrt{N\\mathfrak f_v}$（(6.5)）。",
        ],
        [
            "f(\\chi,v)=|G_0|^{-1}\\sum_{i\\ge0}|G_i|\\operatorname{codim}V^{G_i},\\qquad \\mathfrak f(\\chi)=\\prod_vv^{f(\\chi,v)}",
            "\\Lambda(\\chi,s)=\\bigl(|d_k|^{\\chi(1)}N\\mathfrak f(\\chi)\\bigr)^{s/2}\\prod_{v\\mid\\infty}L_v(\\chi,s)\\cdot L(\\chi,s)",
            "\\Lambda(\\chi,1-s)=W(\\chi)\\,\\Lambda(\\widetilde\\chi,s)",
        ],
        [
            "把 (4.2) 的 $n_-$ 当成余维：书中写 $\\dim V/V^{G_{\\bar v}}$（商空间维数），数值上等于余维，但记号不同；notes 特别提醒这一点。",
            "把 (6.1) 的分母写成 $\\sqrt{f i^\\delta}$：正确的是 $\\sqrt f\\,i^\\delta$（中译注本回页图放大核对过）。",
        ],
        [
            {"type": "易错预警", "title": "分母不是根号内相乘", "text": "(6.1) $W(\\chi)=\\tau(\\chi)/(\\sqrt f\\,i^\\delta)$，分母是 $\\sqrt f$ 乘 $i^\\delta$；若误读成 $\\sqrt{f i^\\delta}$，相位会差 $\\pi/4$。notes 记原书 p.89 的放大核对。"},
            {"type": "背景直觉", "title": "根数是局部常数之积", "text": "$W(\\chi)=\\prod_vW_v$ 是函数方程的「局部-整体」分解；每个 $W_v$ 由局部 Gauss 和给出，只有有限个 $v$ 非平凡。Langlands 1970 宣布、Deligne 1974 证明——这是局部常数理论的核心定理。"},
        ],
        ["ch4-artin-definition", "ch4-induction", "ch1-gamma-factor"],
        [
            src(4, "§4.1", [79, 80], "ch04.tex:252-274"),
            src(4, "§4.2", [80, 81], "ch04.tex:275-290"),
            src(4, "§4.3", [81], "ch04.tex:291-310"),
        ],
        theorems=[
            {
                "name": "定理 4.1（函数方程）",
                "statement": "设 $\\chi$ 为 $G$ 的特征。则 $\\Lambda(\\chi,s)$ 亚纯延拓到整个复平面，并满足 $\\Lambda(\\chi,1-s)=W(\\chi)\\Lambda(\\widetilde\\chi,s)$，其中 $W(\\chi)$ 为模 $1$ 的 Artin 根数。",
                "proof": {
                    "steps": [
                        "一维情形（交换 $G$）由类域论化为 Hecke L 的函数方程（第 1 章定理 5.8）。",
                        "一般情形用 Brauer 定理写成单项特征的整系数组合，逐项相乘；函数方程与根数在乘积下相容。",
                    ],
                    "gap_note": "书中只给两步走的框架，Brauer 定理的证明只述梗概；「亚纯」而非「整」正来自系数可能为负。",
                },
                "source": "ch04.tex:299-310（§4.3，定理 4.1）",
            }
        ],
    ),
    card(
        "ch4-artin-conjecture", "L",
        "Artin 猜想",
        ["Artin's conjecture", "整函数性", "Aramata–Brauer"],
        "Artin 猜想：不含平凡成分的不可约表示 $\\chi$，其 $L(\\chi,s)$ 在全平面解析；它蕴含 $\\zeta_K/\\zeta_k$ 全纯，并归入 Langlands 纲领。",
        "Artin 猜想为什么不能由 Brauer 定理直接推出，它与 Langlands 纲领的关系是什么？",
        "§5 的猜想 5.1：若特征 $\\chi$ 不含平凡特征成分，则 $L(\\chi,s)$ 是整函数。推论 5.2：$K/k$ 为 Galois 扩张时 $\\zeta_K/\\zeta_k$ 全纯。例 5.1（Aramata–Brauer）用增广表示把 $\\zeta_K/\\zeta_k$ 写成 $\\prod_{\\chi\\ne1}L(\\chi,s)^{\\chi(1)}$，从而在 Galois 情形给出全纯性；非 Galois 情形 $\\zeta_K/\\zeta_k$ 的全纯性仍未决。Brauer 定理只给亚纯（系数可负，极点可能相消），要得解析必须证明不相消。Artin 猜想今天已归入 Langlands 纲领：$\\chi$ 应对应 $\\mathrm{GL}_n$ 的自守表示，$L(\\chi,s)$ 应是自守 L 函数；二维情形对应权 $1$ 模形式（Deligne–Serre 正向、Weil 逆定理反向、Langlands–Tunnell 解决除二十面体外的所有类型）。",
        "$\\chi$：Galois 表示的特征；$\\zeta_K/\\zeta_k$：Dedekind zeta 之比；增广表示：$\\chi_{\\mathrm{aug}}=\\chi_{\\mathrm{reg}}-1$；强 Artin 猜想：还要求 $L$ 来自自守表示。",
        [
            "猜想只排除平凡成分：$\\chi$ 含 $1$ 时 $L$ 有 $\\zeta$ 的极点；去掉 $1$ 后应无极点。",
            "Brauer 分解给出亚纯，要得解析必须证明极点不相消；Aramata–Brauer 对 Galois 扩张给出 $\\zeta_K/\\zeta_k$ 的全纯性，但非 Galois 的整性未决。",
            "与 Langlands 的联系：$\\chi$ 应对应 $\\mathrm{GL}_n$ 的自守表示，$L(\\chi,s)$ 应是自守 L 函数，从而整/亚纯由自守表示理论给出。",
        ],
        [
            "L(\\chi,s)\\ \\text{整}\\qquad(\\chi\\ \\text{不含平凡成分})",
            "\\zeta_K(s)/\\zeta_k(s)=\\prod_{\\chi\\ne1}L(\\chi,s)^{\\chi(1)}\\ \\text{全纯}\\qquad(K/k\\ \\text{Galois})",
            "L(\\chi,s)=L(\\pi,s)\\qquad(\\text{Langlands 对应}:\\ \\chi\\leftrightarrow\\pi)",
        ],
        [
            "把「$\\chi$ 不可约」当成充分条件：不可约但含平凡成分（如 $\\chi=1$）仍有极点；条件是没有平凡成分。",
            "把强 Artin 猜想与 Artin 猜想混同：前者还要求 $L$ 来自自守表示（权 $1$ 模形式），后者只要求解析性。",
        ],
        [
            {"type": "背景直觉", "title": "为什么二维情形重要", "text": "§7 说明二维 Artin 表示对应权 $1$ 模形式：Deligne–Serre 给出正向构造，Weil 逆定理给出反向，Langlands–Tunnell 解决除二十面体外的所有类型。这是「Artin 猜想 $\\Rightarrow$ 模性」的具体通道，也是 Wiles 证明费马大定理所用方法的祖先。"},
            {"type": "含糊点拨", "title": "二十面体情形", "text": "定理 7.3 用 Tunnell 的拼写（原书作 Tunnel）。二十面体情形是唯一未被 Langlands–Tunnell 覆盖的二维射影类型，后来由 Taylor 等人的工作推进；书中把它列为「强 Artin 猜想」的开放案例。"},
        ],
        ["ch4-induction", "ch4-artin-hecke", "ch4-conductor-fe"],
        [
            src(4, "§5", [83, 84], "ch04.tex:354-370"),
            src(4, "§7", [85, 87], "ch04.tex:442-482"),
        ],
        theorems=[
            {
                "name": "猜想 5.1（Artin）",
                "statement": "设 $\\chi$ 为 $G$ 的特征，且 $\\chi$ 不含平凡特征作为成分。则 $L(\\chi,s)$ 是全平面上的整函数。",
                "proof": {
                    "steps": [
                        "$\\chi$ 写成不可约特征的整系数组合，逐项由 Brauer 定理得亚纯。",
                        "需证明在 $s=1$ 等处极点不相消——这正是猜想的内容，等价于 $\\chi$ 对应自守表示。",
                    ],
                    "gap_note": "书中明确说 Brauer 定理「只能给亚纯，不能给解析」；猜想 5.1 至今未决，只有一维（类域论）与部分二维情形已知。",
                },
                "source": "ch04.tex:356-370（§5，猜想 5.1）",
            }
        ],
    ),
    card(
        "ch4-artin-hecke", "L",
        "与 Hecke L 的关系（类域论情形）",
        ["类域论", "Hecke L 函数", "交换情形"],
        "当 $\\chi$ 是一维（交换情形），Artin L 就是 Hecke L：局部 $\\rho(\\sigma_v)=\\chi(v)$，整体 $L(\\rho,s)=L(\\chi,s)$；这正是类域论的 L 函数表述。",
        "类域论为什么恰好是 Artin L 与 Hecke L 的相等，这个相等在局部和整体分别意味着什么？",
        "设 $E/K$ 为有限交换扩张，$\\rho:G\\to\\mathbb C^\\times$ 为 Galois 特征。第 1 章定理 5.9（Artin）断言：存在 $K$ 的唯一本原 Hecke 特征 $\\chi$，使 $L(\\rho,s)=L(\\chi,s)$；更强地，Euler 乘积逐位相等，即 $\\rho(\\sigma_{\\mathfrak p})=\\chi(\\mathfrak p)$ 对一切与导子互素的 $\\mathfrak p$（脚注 6 提醒 $K\\ne\\mathbb Q$ 时局部陈述强于整体陈述）。第 4 章 §3.4 的 (3.15)(3.16) 把这写成 $\\zeta_K=\\zeta_k\\prod_{\\chi\\ne1}L(\\chi,s)^{\\chi(1)}$；§4.3 的函数方程证明「第一步用类域论」正是处理这个一维情形。高维没有逐位相等，取而代之的是 Langlands 对应：$\\rho$ 应对应 $\\mathrm{GL}_n$ 的自守表示，$L$ 函数应相等（函子性）。",
        "$\\rho$：一维 Galois 表示（特征）；$\\chi$：Hecke 特征；$\\mathfrak f(\\rho)$：导子；$\\xi_\\infty(\\rho)$：无穷位权；$\\zeta_K=\\zeta_k\\prod_{\\chi\\ne1}L(\\chi,s)^{\\chi(1)}$：交换扩张的 zeta 分解。",
        [
            "一维表示对应 Hecke 特征：类域论给出一一对应，Artin L 的 Euler 因子与 Hecke L 的逐位相等。",
            "整体相等 $L(\\rho,s)=L(\\chi,s)$ 比局部相等弱；第 1 章脚注 6 强调 $K\\ne\\mathbb Q$ 时局部陈述更强（需要逐位匹配）。",
            "高维情形没有这种相等，取而代之的是 Langlands 对应：$\\rho$ 对应 $\\mathrm{GL}_n$ 的自守表示，$L$ 函数相等（函子性）。",
        ],
        [
            "L(\\rho,s)=L(\\chi,s),\\qquad \\rho(\\sigma_v)=\\chi(v)\\qquad(\\dim\\rho=1)",
            "\\zeta_K(s)=\\zeta_k(s)\\prod_{\\chi\\ne1}L(\\chi,s)^{\\chi(1)}",
            "\\mathfrak f(\\rho)=\\mathfrak m,\\qquad \\xi_\\infty(\\rho)=\\xi_\\infty(\\chi)",
        ],
        [
            "把「类域论情形」误当成「所有一维表示都自动是 Hecke 特征」：需要 $\\chi$ 的导子/无穷位权与 $K$ 的射线类群匹配；非本原特征要先约化到本原。",
            "把局部相等与整体相等混为一谈：局部 $\\rho(\\sigma_v)=\\chi(v)$ 是对每个 $v$ 的陈述，整体 $L$ 相等是乘积的结果；书中脚注提醒 $K\\ne\\mathbb Q$ 时局部版本更强。",
        ],
        [
            {"type": "背景直觉", "title": "互反律的两种写法", "text": "第 1 章把 (4.4) $\\zeta(s)L(\\chi,s)=\\zeta_K(s)$ 称为二次互反律的重新表述；第 4 章把它推广为「一维 Artin = Hecke」。两处都是「扩域的 zeta 分解为基域上更简单 L 函数之积」——这正是本书反复出现的「互反」母题。"},
            {"type": "易错预警", "title": "Tunnell 的拼写", "text": "定理 7.3 标题作 Tunnell（J. Tunnell），原书作 Tunnel；引用时用 Tunnell，并说明原书拼写。原书还有 $|G|=p^a l$ 的小写 $l$ 与素数 $\\ell$ 字体冲突的问题，读 §4.4 时要留意。"},
        ],
        ["ch4-artin-definition", "ch1-cft-entry", "ch1-dedekind-zeta"],
        [
            src(4, "§3.4", [78, 79], "ch04.tex:215-249"),
            src(4, "§6", [83, 85], "ch04.tex:371-410"),
        ],
    ),
]
