---
id: MS-09
zh: 自反多胞形
en: reflexive polytope
aliases: [自反多胞形, 反身多胞体, 反身多胞形]
layer: L1
prereqs: [MS-08]
sources:
  - "A 级：Cox–Katz 1999, p.069–070（PDF p.069–070，印刷 p.46–47）§3.5：定义 3.5.3、引理 3.5.4、命题 3.5.5、引理 3.5.6、有限性段落"
  - "A 级：Cox–Katz 1999, p.057–058（PDF p.057–058）§3.2：法扇、极多胞形、支撑函数；p.076–087 §4.1–§4.3：定义 4.1.1、引理 4.1.2、命题 4.1.3、定理 4.1.4、五次例、nef 分拆"
  - "A 级：Batyrev 1994, J. Algebraic Geom. 3 (1994) 493–535（书内 [Batyrev4]，arXiv alg-geom/9310003；定理号待核）；Kreuzer–Skarke 1997, Comm. Math. Phys. 185 (1997) 495–508（书内 [KS3]，hep-th/9512204）"
  - "B 级：SY01-24 第 5 章 §5.1.1（p.81–83）定义 5.1、例 5.1–5.2、反例 3、命题 5.1；Fulton 1993 §5.3（书 p.077 所引 [Fulton3]，页码待核）"
status: draft
review:
  drafter: agent-225
  reviewer: lead
  blindtest: pending
glossary_refs: [SY01-24 术语表 第 54 条「多胞体」p.73, SY01-24 术语表 第 58 条「反身多胞体」p.81, _冲突表 T5、T6]
symbols_refs: ['$M$', '$N$', '$\Delta$', '$\Delta^\circ$', '$v_\Gamma$', '$\Gamma$', '$l(k\Delta)$', '$l^*(k\Delta)$', '$\Sigma$', '$X_\Sigma$', '$V^\circ$', '$\mathbb P_\Delta$']
updated: 2026-11-20
---

# MS-09 自反多胞形

## 1. 一句话

刻面都贴在与原点相距一格的支撑超平面上的整多胞形，是 Batyrev 镜像对的原料。

## 2. 为什么需要它

- **把 Fano 环面簇翻译成多胞形。** 本书 p.069 指出：Fano 环面簇上的丰沛除子 $-K_X$ 确定一个多胞形 $\Delta$，Batyrev 发现「极多胞形也是整的」那一类 $\Delta$ 恰好刻画 Fano 性（命题 3.5.5）。第 4 章开篇原话是「Batyrev 的构造关键地使用了第 3.5 节介绍的自反多胞形」（p.076）。
- **给出成对的多胞形，从而给出成对的 Calabi–Yau 族。** 自反是 $\Delta$ 与 $\Delta^\circ$ 的对称性质（引理 3.5.4，p.069）：同一份数据 $\Delta$ 同时给出 $\mathbb P_\Delta$ 与 $\mathbb P_{\Delta^\circ}$，两者的反典范超曲面族互为 Batyrev 镜像（p.079）。
- **可计算、可列表。** 固定维数、模去幺模变换后自反多胞形只有有限多个（p.070）；Hodge 数有格点计数公式（p.080–082），五次三维簇的镜像族就是从 $\Delta^\circ$ 数出 6 个单项式得到的（p.084–085）。p.083 还记载：7555 个加权射影空间超曲面例子经 [CdK] 核查，其 Newton 多胞形确实都是自反的。

## 3. 定义（全假设）

**3.1 背景与记号**（p.057–058）。设 $(M,N)$ 为互相对偶的自由 $\mathbb Z$-模，$M\cong\mathbb Z^n$，$N=\operatorname{Hom}(M,\mathbb Z)$；$M_{\mathbb R}=M\otimes\mathbb R$，$N_{\mathbb R}=N\otimes\mathbb R$，$\langle\cdot,\cdot\rangle$ 为配对。整多胞形指顶点在 $M$（或 $N$）中的多胞形；「$n$ 维」在本卡一律指满维，故 $\operatorname{Int}\Delta\neq\varnothing$。刻面指 $n-1$ 维面。本书只在 $0$ 是内点时定义极多胞形（p.057）：$\Delta^\circ=\{v\in N_{\mathbb R}:\langle m,v\rangle\ge-1\ \text{对一切}\ m\in\Delta\}$；此时 $0\in\operatorname{Int}\Delta^\circ$、$(\Delta^\circ)^\circ=\Delta$，且 $\Delta$ 的 $i$ 维面 $F$ 对应 $\Delta^\circ$ 的 $(n-1-i)$ 维面 $F^\circ$，在 $F,F^\circ$ 上 $\langle m,v\rangle=-1$。又记 $l(k\Delta)=|k\Delta\cap M|$，$l^*(k\Delta)$ 为 $k\Delta$ 中不在任何刻面上的格点数（p.058）；$\Sigma_\Delta$ 为 $\Delta$ 的法扇（p.057）。

**3.2 定义（定义 3.5.3，p.069）。** 设 $\Delta\subset M_{\mathbb R}\cong\mathbb R^n$ 是 $n$ 维整多胞形。称 $\Delta$ 为**自反的**，若

- $(i)$ $\Delta$ 的每个刻面 $\Gamma$ 都位于形如 $\{m\in M_{\mathbb R}:\langle m,v_\Gamma\rangle=-1\}$ 的支撑仿射超平面上，其中 $v_\Gamma\in N$；
- $(ii)$ $\operatorname{Int}(\Delta)\cap M=\{0\}$。

**3.3 必须交代的假设与等价形式。**

- 满维假设不可省：$(ii)$ 只保证「唯一的内部格点是 $0$」，是满维使 $\operatorname{Int}\Delta\neq\varnothing$，两者合起来才给出 $0\in\operatorname{Int}\Delta$，也才有极多胞形可用。
- $(i)$ 中的 $v_\Gamma$ 由 $\Gamma$ 唯一决定且自动本原：若 $v_\Gamma=d w$（$d>1$），则 $\langle m,w\rangle=-1/d\notin\mathbb Z$ 与 $m\in M$ 矛盾；若 $v_\Gamma'$ 也满足，则 $v_\Gamma'-v_\Gamma\perp\Gamma$ 的方向空间，故 $v_\Gamma'=(1+\lambda)v_\Gamma$，代回得 $\lambda=0$。
- 在 $0\in\operatorname{Int}\Delta$ 下，$(i)$ 等价于「$\Delta$ 的每个刻面格高为 $1$」，也等价于「$\Delta^\circ$ 是整多胞形、顶点正是各 $v_\Gamma$」（p.058 把这批多胞形直接描述为「极多胞形也是整的」）。因此 $\Delta$ 自反 $\iff$ $\Delta$ 与 $\Delta^\circ$ 都是整多胞形且 $0\in\operatorname{Int}\Delta$；这是 SY01-24 定义 5.1 的等价表述，差别只在记号约定（见 §8 冲突 C3）。
- $(ii)$ 不可弱化为「$0\in\operatorname{Int}\Delta$」，必须是「唯一内部格点」；等价地 $l^*(\Delta)=1$（p.082 明用此式）。

**3.4 本书用法。** Cox–Katz 用定义 3.5.3（p.069）这个「刻面方程取 $-1$、法向 $v_\Gamma\in N$、唯一内部格点」的版本，而不把「$\Delta^\circ$ 也整」写进定义。好处是它与支撑函数 $\phi_\Delta(v)=\min_{m\in\Delta}\langle m,v\rangle$ 及法扇 $\Sigma_\Delta$ 直接咬合（p.058、p.070 命题 3.5.5 的证明）；两种写法在满维格多胞形上等价，本书没有出入。

## 4. 最小例子（能算出）

**4.1 一维（热身）。** $n=1$，$M=\mathbb Z$，$\Delta=[-1,1]$。两个刻面 $m=\pm1$，取 $v_\Gamma=\pm1\in N=\mathbb Z$，方程 $\langle m,v\rangle=\pm m=-1$ 成立，格高均为 $1$；$\operatorname{Int}\Delta\cap\mathbb Z=\{0\}$。故 $\Delta$ 自反；$\Delta^\circ=\{v:|v|\le1\}=[-1,1]=\Delta$，$l(\Delta)=l(\Delta^\circ)=3$。注意此时 $\Delta=\Delta^\circ$，说明自反**不**要求 $\Delta\ne\Delta^\circ$。

**4.2 二维正方形（SY01-24 例 5.2，p.81 的同一例子）。** $\Delta=[-1,1]^2$，$M=\mathbb Z^2$。四个刻面 $x=\pm1$、$y=\pm1$，法向 $(\pm1,0),(0,\pm1)\in N$，方程取 $-1$，格高 $1$；$\operatorname{Int}\Delta\cap\mathbb Z^2=\{(0,0)\}$，故自反。极多胞形：$\langle m,v\rangle\ge-1$ 对一切 $\max|m_i|\le1$ 成立 $\iff|v_1|+|v_2|\le1$，即 $\Delta^\circ=\operatorname{conv}\{(1,0),(-1,0),(0,1),(0,-1)\}$（旋转 $45^\circ$ 的菱形，面积 $2$，而 $\Delta$ 的面积 $4$），并且 $(\Delta^\circ)^\circ=\Delta$。逐项：$l(\Delta)=9$，$l(\Delta^\circ)=5$，两边的边都无内部格点，故 $\sum_\Gamma l^*(\Gamma)=\sum_{\Gamma^\circ}l^*(\Gamma^\circ)=0$；又 $l^*(2\Delta)=l(\Delta)=9$，正是 p.082「$l^*(2\Delta)=l(\Delta)$ 来自自反性」的检验。

**4.3 二维 $\mathbb P^2$ 三角形：把 p.084 的顶点族降到 $n=2$。** 取 $\Delta=\operatorname{conv}\{(-1,-1),(2,-1),(-1,2)\}$（即 $=(-1,-1)+3\Delta_2$）。三个刻面 $x=-1$、$y=-1$、$x+y=1$ 的格高都是 $1$（法向 $(1,0),(0,1),(-1,-1)$，右端 $-1$）；内部格点只有 $(0,0)$，故自反。数格点：$l(\Delta)=\#\{(m_1,m_2)\in\mathbb Z^2:m_i\ge-1,\ m_1+m_2\le1\}=\#\{(a,b)\ge0:a+b\le3\}=\binom52=10$。极多胞形 $\Delta^\circ=\operatorname{conv}\{(1,0),(0,1),(-1,-1)\}$，$l(\Delta^\circ)=4$（3 顶点 $+$ 原点；三边本原，无余格点）。三条边各有 $2$ 个内部格点，故 $\sum_\Gamma l^*(\Gamma)=6$；$\Delta^\circ$ 三边本原，故 $\sum_{\Gamma^\circ}l^*(\Gamma^\circ)=0$。结论：$\Delta$ 与 $\Delta^\circ$ 都自反，但 $l(\Delta)=10\ne4=l(\Delta^\circ)$，因此二者**不是**幺模等价的格多胞形（GL$_2(\mathbb Z)$ 保格点计数）——这组数就是 §7 反例 2 的来源，也是 p.080 那些公式中的量在低维的对照。

**4.4 五次三维簇（书内主例，p.084–085）。** $M=\mathbb Z^4$，$\Delta=\operatorname{conv}\{(-1,-1,-1,-1),(4,-1,-1,-1),(-1,4,-1,-1),(-1,-1,4,-1),(-1,-1,-1,4)\}$，即 $\Delta=\{-1\le m_i,\ \sum_i m_i\le1\}$。

1. 自反性：五个刻面是 $m_i=-1$（$i=1,\dots,4$，法向 $e_i$）与 $\sum_i m_i=1$（法向 $-u$，$u=(1,1,1,1)$），右端全为 $-1$，格高 $1$；内部格点只有 $0$。
2. $\Delta^\circ=\operatorname{conv}\{e_1,e_2,e_3,e_4,-u\}$（书 p.084 顶点表）；注意 $\{v_\Gamma\}$ 恰是这些顶点，印证 p.076「因 $\Delta$ 自反，法扇的一维锥生成元就是 $\Delta^\circ$ 的顶点」。
3. $l(\Delta)$：令 $n_i=m_i+1\ge0$，则 $\sum n_i\le5$，故 $l(\Delta)=\binom94=126$——正好是 $x_0,\dots,x_4$ 的五次单项式个数，与书「$\Delta$ 是五次多项式的 Newton 多胞形」一致。
4. $l(\Delta^\circ)$：解 $\sum_i v_i\le1$ 与 $5v_i-\sum_jv_j\ge-1$（$i=1..4$），分类得 $v\in\{0,e_1,e_2,e_3,e_4,-u\}$，故 $l(\Delta^\circ)=6$；书 p.085 说镜像族方程中的单项式「对应于 $\Delta^\circ$ 中的整点，即原点与各顶点」，正是 $6$ 个。
5. 刻面格点数：$m_1=-1$ 的刻面内部点满足 $m_1=-1$、$m_j\ge0$、$\sum_{j\ge2}m_j\le1$，共 $4$ 个；四个这样的刻面共 $16$；$\sum m_i=1$ 的刻面内部点满足 $m_i+1\ge1$、$\sum(m_i+1)=5$，共 $\binom43=4$ 个。故 $\sum_\Gamma l^*(\Gamma)=20$。$\Delta^\circ$ 的五个刻面都是无内点的四面体（$3$-单纯形），故 $\sum_{\Gamma^\circ}l^*(\Gamma^\circ)=0$。
6. Hodge 数：由 p.080 的 $h^{1,1}_{\mathrm{toric}}=l(\Delta^\circ)-n-1-\sum_{\Gamma^\circ}l^*(\Gamma^\circ)$ 得 $6-4-1-0=1$；由 $h^{n-2,1}_{\mathrm{poly}}=l(\Delta)-n-1-\sum_\Gamma l^*(\Gamma)$ 得 $126-4-1-20=101$。完整公式的修正项（p.081–082）在例中为零：$\Delta^\circ$ 的余维 2 面全是无内点三角形，而 $\Delta^\circ$ 的十条边都本原（向量如 $e_i+u=(2,1,1,1)$ 或 $e_j-e_i$，$\gcd=1$），故对偶面 $l^*=0$，乘积为零（$h^{1,1}$ 的修正项由前者为零，$h^{2,1}$ 的修正项由后者为零）。于是 $h^{1,1}(V)=1,\ h^{2,1}(V)=101$；交换 $\Delta\leftrightarrow\Delta^\circ$ 得镜像族 $h^{1,1}(V^\circ)=101,\ h^{2,1}(V^\circ)=1$，与定理 4.1.4 及已知的五次数值一致。
7. 另两项核对：顶点向量（取四个）构成矩阵 $5I_4-J_4$，$\det=5^3(5-4)=125$，与书 p.084「生成指数 $125$ 的子格 $M_1$」相符；又 $\operatorname{vol}(\Delta)=5^4/4!=625/24$，引理 4.1.2(iii) 的 $(-K)^4=4!\operatorname{vol}(\Delta)=625=5^4$ 成立。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | $\Delta$ 自反 $\iff$ $\Delta^\circ$ 自反；且 $(\Delta^\circ)^\circ=\Delta$ | p.057；p.069 引理 3.5.4 | 自反是「成对」性质，Batyrev 构造依赖于此 |
| 2 | $\Delta$ 自反 $\iff$ $\mathbb P_\Delta$ 是 Fano 簇且 $\Delta$ 是 $-K_{\mathbb P_\Delta}$ 对应的多胞形 | p.069–070 命题 3.5.5 | 证明要点：$\phi_\Delta(v_\Gamma)=-1$，故 $\sum_\rho D_\rho=-K$ 丰沛 |
| 3 | 自反 $\Rightarrow$ $l^*(\Delta)=1$ 且 $l^*(2\Delta)=l(\Delta)$ | p.082 | 用来把 Danilov–Khovanskii 公式化简为 p.080 的 $h^{n-2,1}_{\mathrm{poly}}$ 式 |
| 4 | 固定 $n$，模幺模变换自反多胞形只有有限多个 | p.070（[Batyrev4]） | 本书只断言有限性；计数 $16$、$4319$ 的出处见 §8 的 C6（B 级），四维数量同处 |
| 5 | 射影细分 $\Sigma$：$X_\Sigma$ 是 Gorenstein 轨形，$\Delta$ 是 $-K_{X_\Sigma}$ 的多胞形，$-K$ 半丰沛且大，$(-K)^n=n!\operatorname{vol}(\Delta)$，$f:X_\Sigma\to\mathbb P_\Delta$ 保典范；极大时 $X_\Sigma$ 终端 | p.076–077 定义 4.1.1、引理 4.1.2 | 关键式 $K_{X'}=g^*K_X-(\langle m,v'\rangle+1)D'$ |
| 6 | 一般成员 $\overline V\in|-K_{\mathbb P_\Delta}|$ 是 $(n-1)$ 维 Calabi–Yau；且 $h^{1,1}(V)=h^{n-2,1}(V^\circ)$、$h^{n-2,1}(V)=h^{1,1}(V^\circ)$ | p.078 命题 4.1.3；p.080 定理 4.1.4（编号见 §11） | 完整 Hodge 公式见 p.080–082，修正项由余维 2 面对偶给出 |

## 6. 推导流程（D1…Dn）

- **D1（输入）** 取 $n$ 维整多胞形 $\Delta\subset M_{\mathbb R}$，先确认 $0\in\operatorname{Int}\Delta$（$(ii)$ 与满维性会保证）。依据：p.057 极多胞形的定义前提。
- **D2（验证刻面条件）** 对每个刻面 $\Gamma$ 找 $v_\Gamma\in N$ 使 $\Gamma\subset\{\langle\cdot,v_\Gamma\rangle=-1\}$。依据：p.069 定义 3.5.3(i)；$v_\Gamma$ 本原且唯一，见 §3.3。
- **D3（读出对偶）** 由 $\{v_\Gamma\}$ 得 $\Delta^\circ=\operatorname{conv}\{v_\Gamma\}$ 是格多胞形，$(\Delta^\circ)^\circ=\Delta$。依据：p.057–058 极多胞形与面-面对应；p.076 的「一维锥生成元 $=$ $\Delta^\circ$ 顶点」。
- **D4（验证唯一内点）** 检查 $\operatorname{Int}\Delta\cap M=\{0\}$，即 $l^*(\Delta)=1$。依据：p.069 定义 3.5.3(ii)；p.082。
- **D5（得到 Fano 性）** 支撑函数 $\phi_\Delta(v)=\min_{m\in\Delta}\langle m,v\rangle$ 在 $v_\Gamma$ 上取 $-1$，故 $\sum_\rho D_\rho=-K_{\mathbb P_\Delta}$ 是丰沛 Cartier 除子，$\mathbb P_\Delta$ 是 Fano；逆向同理。依据：p.058 支撑函数、p.070 命题 3.5.5 证明。
- **D6（细分、去奇点）** 取射影细分 $\Sigma$：$\Sigma$ 细化 $\Sigma_\Delta$、$\Sigma(1)\subset\Delta^\circ\cap N-\{0\}$（极大取等号）；得 $X_\Sigma$ 是 Gorenstein 轨形、$-K$ 半丰沛大、$f$ 保典范。依据：p.076–077 定义 4.1.1、引理 4.1.2 及式 $K_{X'}=g^*K_X-(\langle m,v'\rangle+1)D'$。
- **D7（取超曲面）** 由 Bertini 型论证，一般成员 $V\in|-K_{X_\Sigma}|$ 是 $(n-1)$ 维 Calabi–Yau 轨形，极大时极小。依据：p.078 命题 4.1.3。
- **D8（镜像侧）** 由 D3 或引理 3.5.4，$\Delta^\circ$ 也自反；对 $\Delta^\circ$ 重复 D5–D7 得 $V^\circ$，称 $^\circ$ 为 $V$ 的 Batyrev 镜像。依据：p.079 §4.1.2。
- **D9（数 Hodge 数）** 由 $\Sigma(1)=\Delta^\circ\cap N-\{0\}$ 与 $D_i'$ 的关系得 $h^{1,1}_{\mathrm{toric}}=l(\Delta^\circ)-n-1-\sum_{\Gamma^\circ}l^*(\Gamma^\circ)$；由 $L(\Delta)$ 参数化形变并扣除 $\dim\operatorname{Aut}(X_\Sigma)=n+\sum_\Gamma l^*(\Gamma)$ 得 $h^{n-2,1}_{\mathrm{poly}}=l(\Delta)-n-1-\sum_\Gamma l^*(\Gamma)$。依据：p.080–081。
- **D10（补修正项）** 与 $V$ 交可约的除子由 $\Delta^\circ$ 的余维 2 面控制，得完整公式；交换 $\Delta\leftrightarrow\Delta^\circ$ 即得定理 4.1.4。依据：p.081–082（Batyrev4、AGM1）。

## 7. 常见误解与反例

- **误解 1：自反就是关于原点中心对称。** 反例：§4.3 的 $\Delta=\operatorname{conv}\{(-1,-1),(2,-1),(-1,2)\}$ 自反，但 $-\Delta\ne\Delta$（$-\Delta$ 的顶点是 $(1,1),(-2,1),(1,-2)$）；正方形 $[-1,1]^2$ 才是中心对称的。自反是「刻面到原点等距一格」，不是「对径封闭」。
- **误解 2：自反意味着 $\Delta$ 与 $\Delta^\circ$ 同构（自对偶）。** 反例：同一 $\Delta=\operatorname{conv}\{(-1,-1),(2,-1),(-1,2)\}$ 有 $l(\Delta)=10$、$l(\Delta^\circ)=4$，GL$_2(\mathbb Z)$ 保格点数，故 $\Delta\not\cong\Delta^\circ$；连 $[-1,1]^2$ 也有 $(\Delta^\circ)$ 面积 $2\ne4$。极对偶总满足 $(\Delta^\circ)^\circ=\Delta$（p.057），但「对偶回自己」与「同构于对偶」是两回事。
- **误解 3：只要 $\Delta$ 有唯一内格点，平移一下就能自反。** 自反性对原点位置敏感：$\Delta=[-1,1]^2$ 自反，而平移 $\Delta'=([0,2]\times[-1,1])$ 的唯一内格点是 $(1,0)$，$0$ 落在刻面 $x=0$ 上（格高 $0$），另两刻面 $x=2$ 格高 $2$——两条都失败。书外对照：SY01-24 反例 3（p.81）的 $\operatorname{conv}\{(-1,-1),(-1,0),(1,0),(0,2)\}$ 同病：$0$ 在刻面 $y=0$ 上，另两刻面格高 $2$。
- **误解 4：Batyrev 构造给出的「镜像对称」是已证的定理。** 书 p.079 明言：虽然 Batyrev 镜像构造适用于**任意维数**的自反多胞形，「这个猜想只适用于 $V$ 与 $V^\circ$ 为三维簇的情形，此时 $\Delta$ 是四维的」；已证的是 Hodge 数关系（p.080），镜像对称本身（族级同构）仍未证明。另注意引理 3.5.6（p.070）：$X=\mathbb P(q_0,\dots,q_n)$ 是 Fano $\iff$ 每个 $q_i\mid\sum_jq_j$——不是所有加权射影空间都 Fano，故对应的反典范多胞形未必自反。
- **误解 5：自反多胞形只有 16 个，所以镜像对称的例子很少。** 16 只是二维的数；三维 $4319$ 个、四维 $473800776$ 个（SY01-24 p.81，见 §8 冲突 C6），而每个自反多胞形还给出多个极大射影细分，进而给出多个镜像族（书中 §4.1.4，p.083–084 讨论多重镜像：同一侧不同的极大射影细分给出不同的镜像族）。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999（本书） | p.069–070 §3.5 | 定义 3.5.3；引理 3.5.4（对偶封闭）；命题 3.5.5（Fano 判据）；引理 3.5.6（加权射影空间）；有限性与四维分类的现状 |
| Cox–Katz 1999（本书） | p.076–082 §4.1 | 定义 4.1.1（射影细分）、引理 4.1.2、命题 4.1.3（CY 超曲面）、定理 4.1.4 及其证明（Hodge 数公式与修正项） |
| Cox–Katz 1999（本书） | p.083–085 §4.1.4–§4.2；p.086–087 §4.3 | 7555 个加权射影空间例子的自反性核查；五次族的完整计算；nef 分拆与自反 Gorenstein 锥（$\Delta=\Delta_1+\cdots+\Delta_k$ 仍自反，Borisov1） |
| SY01-24（Siebert 讲义中译本） | 第 5 章 §5.1.1，p.81–83：定义 5.1、例 5.1–5.2、反例 3、命题 5.1–5.2、定义 5.3 | 同一概念的独立讲法。**冲突 C3**：它以「$0$ 在内部」为假设、把条件写成「侧面到原点的整仿射距离为 $1$」，并把「$\Xi$ 与 $\Xi^\circ$ 都是格多胞形」显式写成等价表述；本书未显式列 $0\in\operatorname{Int}$、未写等价形式，且法向符号取 $-\!1$。逐条等价（见 §3.3），仅记号差 $v\mapsto-v$（建议并入 _冲突表 T9）。另 **冲突 C4**：它以「侧面」指余维 $1$ 面，本书用「刻面」。**冲突 C1/C2**（术语）已由 _冲突表 T5/T6 裁定为「多胞形/自反多胞形」。**冲突 C5**：SY01-24 叫「MPCP 细分」，本书叫「极大射影细分」，命题 5.2 与引理 4.1.2 四性质逐条相同。**冲突 C6**：p.81 给了 $16/4319/473800776$ 三个计数而未给文献（图 5.1 引自 [ref1]），本书 p.070 只写四维分类「正在尝试」 |
| SY01-25 资料卡 04-术语文献勘误.md | 卡 04「一、核心术语」（25 条速查，全表见译本附录 A）与「二、文献」（34 条） | 全文件及该目录 grep「多胞/reflexive/自反/反身」均 $0$ 命中：**无**自反多胞形条目，无定义冲突。仅在同形字层面相关：卡 04 收「sector 扇区」，与本书「扇 fan」不同词（MS-08 C6，建议 _冲突表 T10） |
| Batyrev 1994（书内 [Batyrev4]） | J. Algebraic Geom. 3 (1994) 493–535；arXiv alg-geom/9310003。§/定理号待核 | 自反多胞形的概念来源、对偶镜像构造、Hodge 数公式与修正项 |
| Kreuzer–Skarke 1997（书内 [KS3]） | Comm. Math. Phys. 185 (1997) 495–508；hep-th/9512204 | 自反多胞形分类；本书 p.070 引它说明四维分类的工作 |

注：书内页码一律为 PDF 物理页（$=\backslash$SourcePage$\{N\}$，印刷页 $+23$）；外部文献用原书页码或定理号。

## 9. 前置与后继

- 前置：MS-08（法扇、极多胞形、$l(k\Delta)$ 与 $l^*(k\Delta)$、支撑函数；本卡 §3.1 的记号全部取自它，先读它才能读定义 3.5.3 的「刻面方程」与「法扇一维锥生成元」）。
- 后继：MS-06、MS-22、MS-23（_queue.md 中把 MS-09 列为前置的卡片；MS-23 行写的「第 4 章 §4.5」与实际 §4.3（p.086–087）不符，见 §11 待核 Q7）。本卡 $\Delta$、$\Delta^\circ$、射影细分、Hodge 数公式是 Batyrev 构造、环面完全交、Gorenstein 锥各卡的直接输入。
- 术语协调：正文一律用「多胞形、自反多胞形、刻面、极大射影细分、扇」；引 SY01-24 原话时保留其「多胞体、反身多胞体、侧面、MPCP 细分」并加注。

## 10. 形式化接口（Lean 可 sorry）

```lean
-- M, N：互对偶的自由 ℤ-模；M_ℝ = M ⊗ ℝ；⟨·,·⟩：配对（代码中略去 ℝ-线性延拓细节）。
structure LatticePair where
  M : Type
  N : Type
  pairing : M → N → ℤ   -- 需满足 ℤ-双线性与非退化

structure LatticePolytope (P : LatticePair) (n : ℕ) where
  carrier : Set (P.M →₀ ℝ)          -- M_ℝ 中的子集
  vertices : Finset (P.M →₀ ℝ)       -- 顶点在 M 中
  isFullDim : True                   -- 满维：Int Δ ≠ ∅
  facets : Finset (Set (P.M →₀ ℝ))

def polar (P : LatticePair) (Δ : LatticePolytope P n) : Set (P.N →₀ ℝ) :=
  {v | ∀ m ∈ Δ.carrier, P.pairing m v ≥ -1}

/-- 定义 3.5.3（书 p.069）：刻面方程取 -1 + 唯一内部格点。 -/
def IsReflexive (P : LatticePair) (Δ : LatticePolytope P n) : Prop :=
  (∀ Γ ∈ Δ.facets, ∃ vΓ : P.N, ∀ m ∈ Γ, P.pairing m vΓ = -1) ∧
  (interior Δ.carrier ∩ latticePoints P.M = {0})

/-- 引理 3.5.4（书 p.069）：自反 ⟺ 极多胞形自反。 -/
theorem reflexive_iff_polar_reflexive (P : LatticePair) (Δ : LatticePolytope P n) :
    IsReflexive P Δ ↔ IsReflexive P (polarPolytope P Δ) := by sorry

/-- 命题 3.5.5（书 p.069–070）：Δ 自反 ⟺ ℙ_Δ 是 Fano 且 Δ 是反典范多胞形。 -/
theorem reflexive_iff_fano (P : LatticePair) (Δ : LatticePolytope P n) :
    IsReflexive P Δ ↔ IsFano (P_delta P Δ) ∧ antiCanonicalPolytope (P_delta P Δ) = Δ := by sorry

/-- 定理 4.1.4（书 p.080）：Batyrev 镜像对的 Hodge 数交换。 -/
theorem batyrev_hodge_dual (Δ : LatticePolytope P 4) (h : IsReflexive P Δ) :
    h11 (CYHypersurface Δ) = h21 (BatyrevMirror Δ) ∧
    h21 (CYHypersurface Δ) = h11 (BatyrevMirror Δ) := by sorry
```

## 11. 待核清单

- [ ] **C1（术语，已裁）** SY01-24 术语表第 54 条把 polytope 译为「多胞体」，本书用「多胞形」；_冲突表 T5 已裁定「多胞形」，正文照此执行。
- [ ] **C2（术语，已裁）** SY01-24 术语表第 58 条把 reflexive polytope 译为「反身多胞体」，本书用「自反多胞形」；_冲突表 T6 已裁定「自反多胞形」，正文照此执行。
- [ ] **C3（定义表述，待核）** SY01-24 定义 5.1（p.81）显式假设「$0$ 在内部」、把 (ii) 写成「每个侧面到原点的整仿射距离均为 $1$」并给出等价表述「$\Xi$ 与 $\Xi^\circ$ 都是格多胞形」；本书定义 3.5.3 不显式列 $0\in\operatorname{Int}$、不写等价形式，且法向取 $-1$。两者逐条等价（论证见 §3.3），差异属记号与行文；请 lead 决定是否并入 T9（极多胞形符号约定）。
- [ ] **C4（术语，待核）** SY01-24 用「侧面」指余维 1 面，本书用「刻面」；MS-08 已建议编入 _冲突表 T8，本卡沿用，待 lead 分配。
- [ ] **C5（术语，待核）** SY01-24 定义 5.3 的「MPCP 细分」（极大、射影、保典范、部分细分）与本书「极大射影细分」（定义 4.1.1）实质同一对象，命题 5.2 与引理 4.1.2 四性质逐条相同；两书命名不同，编号待 lead 分配。
- [ ] **C6（计数，待核）** SY01-24 p.81 给出「二维 16 个、三维 4319 个、四维 473800776 个」且未标文献（图 5.1 引自 [ref1]）；本书 p.070（1999 年）只说「人们正在尝试分类所有四维自反多胞形」。四维数字应是 Kreuzer–Skarke 2000 年结果（书内未收，待补 A 级出处）；不作对错判断，只记差异。
- [ ] Q1 定理 4.1.4 的编号：tex 中该定理为不带显式编号的 `theorem` 环境，按 §3.5 的共享计数器（定义 4.1.1、引理 4.1.2、命题 4.1.3）推断为 4.1.4；页码 p.080 确定，编号待核。
- [ ] Q2 书内公式编号（如 $h^{1,1}$ 与 $h^{n-2,1}$ 的完整式）未能与排版对核，正文一律改用页码引用（p.080–082）。
- [ ] Q3 Batyrev 1994 的定理号未核（本卡只引书内页码与「[Batyrev4]」）。
- [ ] Q4 [KS3] 与「四维分类工作」的对应关系待核（书 p.070 与 p.083 的引用语境不同）。
- [ ] Q5 7555 个例子的来源 [CdK] 完整书目待核（书 p.083、p.255 相关条目）。
- [ ] Q6 §4.4 第 6 条「修正项为零」由本卡独立数出（$\Delta^\circ$ 各边本原、余维 2 面 $l^*=0$），书中未逐项写出；如审核需要，可补一条脚注式论证。
- [ ] Q7 MS-23 的 _queue.md 位置「第 4 章 §4.5」与实际 §4.3（nef 分拆，p.086–087）不符，属跨卡待核。
- [ ] Q8 SY01-25 资料卡 04 无自反多胞形条目（已全目录检索确认），若日后补收，需回填 §8 的 SY01-25 行。

非空则 status ≠ frozen。
