# -*- coding: utf-8 -*-
"""L1 样板：校订修正 + 6 条 Tutor Note 登记 + 8 条学生向译注。只跑一次。"""
import io, os, re

WORK = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(WORK)
F = os.path.join(ROOT, 'src', 'chapters', 'lecture01.tex')
t = io.open(F, encoding='utf-8').read()
orig_len = len(t)
LOG = []


def rep(anchor, new, tag):
    global t
    c = t.count(anchor)
    if c != 1:
        raise SystemExit('[%s] anchor count=%d: %r' % (tag, c, anchor[:60]))
    t = t.replace(anchor, new)
    LOG.append(tag)


N_PERFECT = (r'\znote{域 $F$ 称为\textbf{完美域}（perfect field），若 $F$ 上每个不可约多项式都无重根；'
             r'特征 $p>0$ 时这等价于 $F^p=F$，即 Frobenius 映射 $x\mapsto x^p$ 是满射。完美域的代数闭包与其可分闭包重合，'
             r'因此它的每个代数扩张都自动可分，这正解释了本条结论。'
             r'[来源：nLab "perfect field"，\url{https://ncatlab.org/nlab/show/perfect+field}（Last revised 2017-07-21；2026-11-14 访问）。]}')

N_SEP = (r'\znote{\textbf{可分闭包} $F^{\mathrm{sep}}$ 指 $\overline F_{\mathrm{alg}}$ 中所有在 $F$ 上可分的元素组成的子域（本文记作 $\overline F$）。'
         r'它是 $F$ 的极大可分扩张，故 $F^{\mathrm{sep}}/F$ 是 Galois 扩张；$F$ 完美时它与代数闭包重合。'
         r'数论中取可分闭包而非代数闭包作底座，是因为 $\Gal(F^{\mathrm{sep}}/F)$ 才是与类域论、Langlands 对应直接相关的绝对 Galois 群。'
         r'[来源：nLab "separable closure"，\url{https://ncatlab.org/nlab/show/separable+closure}（Last revised 2026-04-15；2026-11-14 访问）。]}')

N_KRULL = (r'\znote{具体地，把 $\Gal(L/F)$ 看作所有有限 Galois 子扩张 $L_i/F$ 对应的有限群 $\Gal(L_i/F)$ 的投影极限，'
           r'并赋以投影极限拓扑（各 $\Gal(L_i/F)$ 取离散拓扑），所得拓扑即 Krull 拓扑。此时 $\Gal(L/F)$ 是\textbf{射有限群}：'
           r'紧、Hausdorff、全不连通。正因如此，才对「闭子群」而非任意子群有中间域对应——非闭子群不对应任何中间域。'
           r'[来源：nLab "profinite group"，\url{https://ncatlab.org/nlab/show/profinite+group}（Last revised 2025-07-01；2026-11-14 访问）。]}')

N_SPLIT = (r'\znote{设 $f\in F[x]$。$f$ 在 $F$ 上的\textbf{分裂域}指这样的扩张 $E/F$：$f$ 在 $E$ 中分裂为一次因式之积，'
           r'且 $E$ 由 $F$ 与 $f$ 的全部根生成；它在 $F$-同构意义下唯一。$x^m-1$ 的根恰为全部 $m$ 次单位根，故其分裂域为 $\Q(\zeta_m)$。'
           r'[来源：nLab "splitting field"，\url{https://ncatlab.org/nlab/show/splitting+field}（Last revised 2026-06-08；2026-11-14 访问）。]}')

N_AB = (r'\znote{即\textbf{阿贝尔化} $G^{\mathrm{ab}}=G/\overline{[G,G]}$：一般群取交换子子群的闭包，使商群 Hausdorff（射有限情形下闭包不可省）。'
        r'$G$ 的一维表示与 $G^{\mathrm{ab}}$ 的一维表示一一对应，而无限 Galois 理论给出 $\Gal(\overline F/F)^{\mathrm{ab}}\cong\Gal(F^{\mathrm{ab}}/F)$，'
        r'所以 $n=1$ 的 Langlands 对应就是描述 $F^{\mathrm{ab}}$。$n\geq2$ 的表示没有这种「先取商」的化简，这正是难点所在。'
        r'[来源：nLab "abelianization"，\url{https://ncatlab.org/nlab/show/abelianization}（Last revised 2026-01-21；2026-11-14 访问）。]}')

N_PROFIN = (r'\znote{$\widehat{\Z}$ 称为 $\Z$ 的\textbf{射有限完备化}，同构于 $\varprojlim_n\Z/n\Z$；'
            r'在乘积拓扑下 $\prod_p\Z_p$ 与投影极限拓扑一致，都是紧、全不连通的射有限环。一般地，任何有限生成 $\Z$-模都有射有限完备化。'
            r'[来源：nLab "profinite group"，\url{https://ncatlab.org/nlab/show/profinite+group}（Last revised 2025-07-01；2026-11-14 访问）。]}')

N_IGP = (r'\znote{此即\textbf{逆 Galois 问题}（inverse Galois problem）：是否每个有限群都同构于 $\Q$ 的某个有限 Galois 扩张的 Galois 群？'
         r'阿贝尔情形由 Kronecker--Weber 定理肯定（即本讲定理 9）；一般情形仍未解决。已知可解群情形成立（Shafarevich），'
         r'$S_n$、$A_n$ 及大量其他群也已实现，但一般有限群情形是公开问题。'
         r'[来源：nLab "inverse Galois problem"，\url{https://ncatlab.org/nlab/show/inverse+Galois+problem}（Last revised 2023-05-27；2026-11-14 访问）。]}')

N_DIR = (r'\znote{Dirichlet $L$-级数定义为 $L(s,\chi)=\sum_{n\geq1}\chi(n)n^{-s}$，其中 $\chi$ 是模 $b$ 的 Dirichlet 特征标；'
         r'由 $L(1,\chi)\neq0$ 可推出等差数列 $\{a+kb\}$ 中素数无穷多，这就是 Dirichlet 定理的解析证明。'
         r'它也是 Langlands 纲领中 $L$ 函数的最初原型（$F=\Q$、$n=1$ 的情形）。'
         r'[来源：Ireland--Rosen, \textit{A Classical Introduction to Modern Number Theory}, 2nd ed., GTM 84, 第 16 章（本讲参考文献）；'
         r'并见 nLab "L-function"，\url{https://ncatlab.org/nlab/show/L-function}（Last revised 2024-07-07；2026-11-14 访问）。]}')

# ---------- 1. 真错修正：指数 → 阶 ----------
rep(r'它有一个指数为$m_1$的子群。',
    r'它有一个阶为$m_1$的子群。' + '\n' +
    r'% [Tutor Note: 原书 p8 作 "has a subgroup of order m_1"，旧译误作「指数」；指数为 m_1 的子群对应的是 $\Z/((p_1-1)/m_1)\Z$ 的商，与构造不符。本轮改正。]',
    'FIX: 指数→阶')

# ---------- 2. 原书笔误登记（Tutor Note，不影响排版） ----------
rep(r'容易看出$\theta$是单射，且像为整个$(\Z/m\Z)^\times$。',
    r'容易看出$\theta$是单射，且像为整个$(\Z/m\Z)^\times$。' + '\n' +
    r'% [Tutor Note: 原书 p6 将 $\theta$ 的余域写作 $\Z/m\Z$，紧接着又说其像为 $(\Z/m\Z)^\times$，前后不一致；译文按正确的 $(\Z/m\Z)^\times$ 处理。]',
    'TN: θ 余域')
rep(r'只需证明$[\Q(\zeta_m,\zeta_n):\Q]=[\Q(\zeta_m):\Q]\,[\Q(\zeta_n):\Q]$。',
    r'只需证明$[\Q(\zeta_m,\zeta_n):\Q]=[\Q(\zeta_m):\Q]\,[\Q(\zeta_n):\Q]$。' + '\n' +
    r'% [Tutor Note: 原书 p7 该恒等式右端误写作 $[\Q(\zeta_n):\Q]\cdot[\Q(\zeta_n):\Q]$（两次 $\zeta_n$）；译文按正确写法处理。]',
    'TN: 推论2.5 次数公式')
rep(r'\qquad 1\leq t<\sum_{j=1}^s a_j.\]',
    r'\qquad 1\leq t<\sum_{j=1}^s a_j.\]' + '\n' +
    r'% [Tutor Note: 原书 p8 此处下界误写作 $1\leq t\leq\sum_j m_j$，与定理中 $m_j$ 的含义不符；译文按正确的 $\sum_j a_j$ 处理。]',
    'TN: 定理6 列式')
rep(r'而$\varphi(m)=2\iff m=3,4,6$。',
    r'而$\varphi(m)=2\iff m=3,4,6$。' + '\n' +
    r'% [Tutor Note: 原书 p8 习题提示作「$m=4$ 或 $6$」，漏了 $m=3$（$\varphi(3)=2$）；译文已补正。]',
    'TN: φ(m)=2 漏 m=3')
rep(r'若$a,b\in\Z$且$(a,b)=1$，$b\ne0$，',
    r'若$a,b\in\Z$且$(a,b)=1$，$b\ne0$，' + '\n' +
    r'% [Tutor Note: 原书 p10 未声明 $b\neq0$，而 $b=0$ 时同余式无意义；译文补上。]',
    'TN: Dirichlet b≠0')

# ---------- 3. 学生向译注 ----------
rep(r'$F$都是完美域。）', r'$F$都是完美域' + N_PERFECT + r'。）', 'NOTE: 完美域')
rep(r'我们总用$\overline F$表示域$F$的可分闭包', r'我们总用$\overline F$表示域$F$的可分闭包' + N_SEP, 'NOTE: 可分闭包')
rep(r'\idx{Krull拓扑}', r'\idx{Krull拓扑}' + N_KRULL, 'NOTE: Krull拓扑')
rep(r'是$x^m-1$的分裂域', r'是$x^m-1$的分裂域' + N_SPLIT, 'NOTE: 分裂域')
rep(r'为核得到的商群。', r'为核得到的商群。' + N_AB, 'NOTE: 阿贝尔化')
rep(r'令$\widehat{\Z}:=\prod_p\Z_p$。', r'令$\widehat{\Z}:=\prod_p\Z_p$' + N_PROFIN + r'。', 'NOTE: 射有限完备化')
rep(r'然而，一旦去掉阿贝尔条件，问题便远未解决。', r'然而，一旦去掉阿贝尔条件，问题便远未解决。' + N_IGP, 'NOTE: 逆Galois问题')
rep(r'Dirichlet的证明使用了Dirichlet $L$-级数。', r'Dirichlet的证明使用了Dirichlet $L$-级数。' + N_DIR, 'NOTE: Dirichlet L-级数')

io.open(F, 'w', encoding='utf-8').write(t)
print('applied', len(LOG), 'edits;', orig_len, '->', len(t), 'chars')
for x in LOG:
    print('  ', x)
