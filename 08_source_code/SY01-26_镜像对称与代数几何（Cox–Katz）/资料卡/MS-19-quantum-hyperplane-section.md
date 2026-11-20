---
id: MS-19
zh: 量子超平面截面原理
en: quantum hyperplane section principle
aliases: [QHSP, 量子超平面截面猜想, quantum hyperplane section theorem]
layer: L1
prereqs: [MS-04, MS-18]
sources:
  - "A 级：Cox–Katz 1999, §11.2.2, PDF p.387–389（印刷 p.364–366）：原理的提出与设定、向量丛 V_βk 与正合列、J_V（原书式 (11.52)）与 Ī_V 的定义、deg q 的次数约定、猜想 11.2.7、P^n 情形与定理 11.2.2 的等价性"
  - "A 级：Cox–Katz 1999, §11.2.1, PDF p.379–386（印刷 p.356–363）：式 (11.38) 的 I_V、定理 11.2.2、命题 11.2.1、命题 11.2.3、五次簇与 Fano 超曲面计算"
  - "A 级：Cox–Katz 1999, §2.6.2, PDF p.49（印刷 p.26）：镜像定理的证明将使用本原理（等变上同调的局部化公式）"
  - "A 级：Cox–Katz 1999, §12.4, PDF p.428（印刷 p.405）：[BCFKvS1] 的阶乘技巧自述为本原理的朴素版本"
  - "A 级原始文献：Givental 1996（alg-geom/9612001，提出）；Kim 1998（alg-geom/9712008，正式表述并证明广义旗流形情形）；Batyrev–Ciocan-Fontanine–Kim–van Straten 1998（Nuclear Phys. B514, 640–666）；Morrison–Plesser 1995（Nuclear Phys. B440, 279–354，量子限制公式）；Tjøtta 1998（math/9802037）"
  - "B 级：本书 §11.1.5 凸丛定义（PDF p.372）；nLab 条目「quantum cohomology」「Gromov–Witten invariant」（索引级，无本原理专条，待核）"
status: draft
review:
  drafter: agent-233
  reviewer: lead
  blindtest: pending
glossary_refs: ["SY01-24 #19 镜像映射", "SY01-24 #31 稳定映射", "SY01-24 #32 虚拟基本类", "SY01-24 #18 单值变换（本书作「单值性」）"]
symbols_refs: ['$\overline I_{\mathcal V}$', '$J_{\mathcal V}$', '$\mathcal V_{\beta,k}$', "$\\mathcal V'_{\\beta,k,i}$", '$q^\beta$', '$\deg q_i$', '$\hbar$']
updated: 2026-11-20
---

# MS-19 量子超平面截面原理

## 1. 一句话
用环境空间上的超几何级数猜测完全交子簇的镜像定理。

## 2. 为什么需要它
- 第 2 章已预告：镜像定理的证明要用本原理（PDF p.49）——原理把「环境空间 $Y$ 上稳定映射模空间的等变交理论」与「子簇 $X$ 的亏格零 GW 不变量」焊接起来，否则第 11 章只剩逐个算例。
- 没有它就不知道一般凸簇 $Y$ 的镜像定理「应当是什么」：只要知道式 (11.55) 的右端，本原理立刻给出 $Y$ 中完全交的镜像猜想（PDF p.389）。Givental 的 $\mathbb P^n$ 结果能推广到广义旗流形（Kim2）、并被用于 Grassmann 簇（BCFKvS1），正是把本原理当作桥梁（PDF p.389）。
- 在 $\mathbb P^n$ 情形它与定理 11.2.2 等价（PDF p.389），所以不是额外假设：一方面它是镜像定理的坐标变换版，另一方面为定理 11.2.2 提供「$I_{\mathcal V}$ 用等变局部化算、再与 $J_{\mathcal V}$ 比较」的证明路线。
- 具体计算也靠它：[BCFKvS1] 的「阶乘技巧」自述是本原理的朴素版本，用于算 Grassmann 簇中 Calabi–Yau 完全交三维簇的瞬子数（PDF p.428）。

## 3. 定义（全假设）
（背景）设 $Y$ 为光滑代数簇，$X\subset Y$ 为完全交，即向量丛 $\mathcal V=\bigoplus_{i=1}^{\ell}\mathcal L_i$ 的一个截面 $s$ 的零点集。设每个 $\mathcal L_i$ 是**凸线丛**：对所有无标记亏格零稳定映射 $f:C\to Y$ 有
$$H^1(C,f^*\mathcal L_i)=0 .$$
这里的「凸」与 §11.1.5 的用法相同（PDF p.387；$\mathbb P^n$ 上凸丛的完整定义见 PDF p.372）。$\overline M_{0,k}(Y,\beta)$ 记稳定映射的粗模空间（其底层的代数叠记为 $\overline{\mathcal M}_{0,k}(Y,\beta)$，见 PDF p.356 的说明）。

（假设，逐条写出）
1. $Y$ 为**凸簇**：书中在使用时落实为 $\overline M_{0,2}(Y,\beta)$ 的虚拟基本类就是通常基本类（与 PDF p.381 对 $\mathbb P^n$ 的说明同理；一般定义本书未展开，见 §11-T4）。
2. $\mathcal V$ 的每个 $\mathcal L_i$ 凸（上一条），于是 $H^0(C,f^*\mathcal V)$ 在模空间上成为向量丛。
3. $Y$ 的 Kähler 锥是由类 $T_1,\dots,T_r$ 生成的**单纯锥**；$T_i$ 是 $H^2(Y)$ 的一组基（用于定义 $q_i$ 的次数，PDF p.388）。
4. 记 $\beta\in H_2(Y,\mathbb Z)$，$M(Y)\subset H_2(Y,\mathbb Z)$ 为有效曲线类半群；$q_i=e^{t_i}$，$\delta=\sum_{i=1}^r t_iT_i$，$q^\beta=e^{\int_\beta\delta}$，$\hbar$ 为形式变量。

（构造，PDF p.387）对 $k\ge0$ 令 $\mathcal V_{\beta,k}$ 为 $\overline M_{0,k}(Y,\beta)$ 上的向量丛，纤维为 $H^0(C,f^*\mathcal V)$；$\pi_k$ 忘掉第 $k$ 个标记点，则 $\pi_k^*\mathcal V_{\beta,k-1}=\mathcal V_{\beta,k}$。对 $1\le i\le k$，令 $\mathcal V'_{\beta,k,i}$ 为「在第 $i$ 个标记点消失」的截面所成的丛，有正合列
$$0\longrightarrow\mathcal V'_{\beta,k,i}\longrightarrow\mathcal V_{\beta,k}\longrightarrow e_i^*\mathcal V\longrightarrow0 .$$

（定义一：$J_{\mathcal V}$，原书式 (11.52)，PDF p.388）$e_1$ 为赋值映射，$e_{1!}(1/(\hbar-c))$ 为下降类的符号记法（同式 (11.44)），
$$J_{\mathcal V}=e^{(t_0+\delta)/\hbar}\operatorname{Euler}(\mathcal V)\left(1+\sum_{\beta\neq0}q^\beta e_{1!}\Big(\frac{\operatorname{Euler}(\mathcal V'_{\beta,2,1})}{\hbar-c}\Big)\right).$$

（定义二：$\overline I_{\mathcal V}$，PDF p.388）令 $\mathcal L_j(\beta)=\int_\beta c_1(\mathcal L_j)$，
$$\overline I_{\mathcal V}=e^{(t_0+\delta)/\hbar}\operatorname{Euler}(\mathcal V)\left(1+\sum_{0\neq\beta\in M(Y)}q^\beta\prod_{j=1}^{\ell}\frac{\prod_{m=-\infty}^{\mathcal L_j(\beta)}(c_1(\mathcal L_j)+m\hbar)}{\prod_{m=-\infty}^{0}(c_1(\mathcal L_j)+m\hbar)}\,e_{1!}\Big(\frac1{\hbar-c}\Big)\right),$$
乘积中除有限项外全部约去（同 §5.5.3，PDF p.388）。

（定义三：$q_i$ 的次数，PDF p.388）用
$$c_1(Y)-c_1(\mathcal V)=\sum_{i=1}^r(\deg q_i)T_i$$
定义 $\deg q_i$；当 $Y=\mathbb P^n$、$\mathcal V=\bigoplus_i\mathcal O(a_i)$ 时 $\deg q=n+1-\sum_i a_i$。

（原理/猜想 11.2.7，PDF p.388）设 $Y$ 凸且所有 $i$ 有 $\deg q_i\ge0$。则存在**唯一**的加权齐次三角变量变换
$$t_0\longmapsto t_0+f_0(q)\hbar+h(q),\qquad t_i\longmapsto t_i+f_i(q),$$
其中 $h,f_0,\dots,f_r$ 是无常数项的加权齐次幂级数，$\deg f_0=\deg f_i=0$、$\deg h=1$，使得变换后 $\overline I_{\mathcal V}$ 与 $J_{\mathcal V}$ 相等。

**本书用法**：本书把它按猜想陈述，并明说「在一个尚未获证的一般情形中陈述此原理」（PDF p.387），$\mathbb P^n$ 情形已由定理 11.2.2 验证（PDF p.389）；术语「超平面截面」是历史名，$X$ 可为任意完全交，不限于超曲面（见 §7-误解 3）。

## 4. 最小例子（能算出）
取 $Y=\mathbb P^4$、$\mathcal V=\mathcal O_{\mathbb P^4}(5)$、$X$ 为五次三维簇、$\hbar=1$。此时 $\operatorname{Euler}(\mathcal V)=5H$，式 (11.38)（PDF p.379）给出
$$I_{\mathcal V}=5H\,e^{t_0+t_1H}\sum_{d\ge0}q^d\,\frac{\prod_{m=1}^{5d}(5H+m)}{\prod_{m=1}^{d}(H+m)^5},\qquad q=e^{t_1}.$$
**第 1 步（$d=1$ 的项）**：分子
$$\prod_{m=1}^{5}(5H+m)=120+1370H+5625H^2+10625H^3,$$
其中 $120=5!$，$1370=120\cdot5\big(1+\frac12+\frac13+\frac14+\frac15\big)=120\cdot5\cdot\frac{137}{60}$；分母 $(H+1)^5=1+5H+10H^2+10H^3$，其逆为 $1-5H+15H^2-35H^3$。相乘得
$$\frac{\prod_{m=1}^{5}(5H+m)}{(H+1)^5}=120+770H+575H^2-1150H^3,$$
验算：$1370-120\cdot5=770$；$5625-5\cdot1370+15\cdot120=575$；$10625-5\cdot5625+15\cdot1370-35\cdot120=-1150$。

**第 2 步（读出 $y_i$）**：与 PDF p.385 的写法 $I_{\mathcal V}=e^{t_0/\hbar}5H\big(y_0+y_1\frac H\hbar+y_2\frac{H^2}{\hbar^2}+y_3\frac{H^3}{\hbar^3}\big)$ 比较（$t_1=\log q$），由 $e^{t_1H}$ 的展开得
$$y_0=1+120q+\cdots,\quad y_1=y_0t_1+770q+\cdots,\quad y_2=y_0\frac{t_1^2}{2}+q\big(770t_1+575\big)+\cdots.$$

**第 3 步（镜像映射）**：$s=\frac{y_1}{y_0}=t_1+770q+\cdots$（PDF p.385）。令 $A=\frac{y_2}{y_0}$，代入 $t_1=s-770q+\cdots$：
$$A=\frac{t_1^2}{2}+q(770t_1+575)+\cdots=\frac{s^2}{2}-770sq+q(770s+575)+\cdots=\frac{s^2}{2}+575q+\cdots,$$
一次项 $770sq$ 恰相消，故 $A''=1+575q+\cdots$（$'=d/ds$）。

**第 4 步（结果）**：由 $I_{\mathcal V}/y_0=5H\big(1+sH+A\frac{H^2}{\hbar^2}+B\frac{H^3}{\hbar^3}\big)$（$B=y_3/y_0$）得 $(I_{\mathcal V}/y_0)''=5A''H^3+5B''H^4$。书中（PDF p.386）把它整理为
$$\Big(\frac{I_{\mathcal V}}{y_0}\Big)''=(5+2875q+\cdots)(H^3+sH^4)=Y\,(H^3+sH^4),$$
比较 $H^3$ 系数得 $Y=5A''=5+2875q+\cdots$，其中 $2875=5\cdot575$，正是五次三维簇的归一化 Yukawa 耦合 $Y=\langle H,H,H\rangle$ 的 $q$ 系数（PDF p.386；$2875$ 同时是五次三维簇上直线数 $n_1$，因为相对不变量 $K_1=\int_{\overline M_{0,0}(\mathbb P^4,1)}\operatorname{Euler}(\mathcal V_d)=n_1$，PDF p.356）。这就是 queue 所指的对照：**环境空间的相对 GW 数** $K_d$ 经镜像映射变成**子簇 $X$ 的 GW 数**；$d=1$ 时 $f=\log y_0$、$h=0$、$g=y_1/y_0-t_1$ 的镜像变换显式可算（PDF p.385）。

## 5. 关键性质（3–6 条，带出处）
| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | $\mathcal V=0$ 时 $J_{\mathcal V}=J_Y$，本原理是 $Y$ 自身镜像定理的推广 | PDF p.388 | 此时 $X=Y$ |
| 2 | $Y=\mathbb P^n$ 时用 (11.55) 得 $\overline I_{\mathcal V}=I_{\mathcal V}$（即式 (11.38)） | PDF p.388–389 | 需命题 11.2.1 |
| 3 | $\mathbb P^n$ 情形：本原理 $\Longleftrightarrow$ 定理 11.2.2 | PDF p.389 | 故不是额外假设 |
| 4 | $\deg q_i$ 由 $c_1(Y)-c_1(\mathcal V)$ 定，$\mathbb P^n$ 时 $=n+1-\sum a_i$；猜想要求 $\ge0$ | PDF p.388 | 反典范 nef 的类比 |
| 5 | 已证情形：$\mathbb P^n$（定理 11.2.2）、广义旗流形（Kim2）、Grassmann 流形与完全旗流形中 CY 完全交（BCFKvS1；书 PDF p.389 如此表述，论文本身只算 Grassmann，旗流形在同伴文 math/9803108）、二次曲线网簇 $N$（determinantal nets of conics，dim 6；Tjøtta） | PDF p.389 | 一般情形仍未证 |
| 6 | $\dim X\ge3$ 时 $J_{\mathcal V}=i_!(J_X)$；偶数维 $X$ 只能看到 $H^*(\mathcal V)=i^*H^*(Y)$ 部分 | 命题 11.2.3, PDF p.382–384 | 见 §7-误解 2 |

## 6. 推导流程（D1…Dn）
**D1（设定与凸性）** 取凸 $Y$、凸线丛 $\mathcal L_i$、完全交 $X=Z(s)$；凸性给出 $H^1(C,f^*\mathcal L_i)=0$。依据：PDF p.387；凸丛定义 PDF p.372。
**D2（造丛与正合列）** 由 $H^0$ 得 $\mathcal V_{\beta,k}$，由消失截面得 $\mathcal V'_{\beta,k,i}$ 与 $0\to\mathcal V'\to\mathcal V_{\beta,k}\to e_i^*\mathcal V\to0$。依据：PDF p.387。
**D3（定义 $J_{\mathcal V}$）** 用 $\operatorname{Euler}(\mathcal V'_{\beta,2,1})$ 与 $e_{1!}(1/(\hbar-c))$ 写下降类求和；$Y$ 凸保证虚拟基本类=通常基本类，故这是通常交数。依据：式 (11.52), PDF p.388；p.381。
**D4（定义 $\overline I_{\mathcal V}$）** 把 $J_{\mathcal V}$ 中的 $\operatorname{Euler}(\mathcal V'_{\beta,2,1})$ 换成超几何乘积 $\prod_j\prod_m(c_1(\mathcal L_j)+m\hbar)$ 之比，其余下降类折成 $e_{1!}(1/(\hbar-c))$。依据：PDF p.388；乘积约去见 §5.5.3。
**D5（定次数）** 用 $c_1(Y)-c_1(\mathcal V)=\sum(\deg q_i)T_i$ 定义加权次数，使 $\overline I_{\mathcal V}$ 加权齐次。依据：PDF p.388。
**D6（陈述原理）** 断言 $\overline I_{\mathcal V}$ 与 $J_{\mathcal V}$ 经唯一加权齐次三角变换相等（猜想 11.2.7）。依据：PDF p.388。
**D7（$\mathbb P^n$ 验证）** 命题 11.2.1 给 $I_{\mathbb P^n}=J_{\mathbb P^n}$（PDF p.380）；比较 (11.53)、(11.54) 得 (11.55) $e_{1!}(1/(\hbar-c))=1/\prod_{m=1}^d(H+m\hbar)^{n+1}$（PDF p.388–389）；代入 $\overline I_{\mathcal V}$ 并注意 $\mathcal L_j(\beta)=a_jd$，得 $\overline I_{\mathcal V}=I_{\mathcal V}$。依据：PDF p.389。
**D8（等价性）** 故 $\mathbb P^n$ 情形本原理与定理 11.2.2 等价。依据：PDF p.389。
**D9（一般 $Y$ 的用法）** 一旦知道凸 $Y$ 对应的 (11.55) 右端，就得到 $Y$ 中完全交的镜像定理「应是什么」。依据：PDF p.389。
**D10（检验与应用）** 五次簇：$(I_{\mathcal V}/y_0)''=Y(H^3+sH^4)$ 恢复 $Y=5+2875q+\cdots$（PDF p.385–386）；Fano 超曲面（$\ell<n$，此时 $f=g=h=0$）：小量子上同调关系 $H^n=q\ell(\ell H)^{\ell-1}$（推论 11.2.6, PDF p.387）；[BCFKvS1] 用「阶乘技巧」算 Grassmann 簇中 CY 完全交的瞬子数（PDF p.428）。

## 7. 常见误解与反例（≥2）
**误解 1：本原理是定理。** 错在把 Kim 的旗流形结果当成一般情形。本书明说在尚未获证的一般情形中陈述它（PDF p.387），陈述为猜想 11.2.7（PDF p.388）；已证的只有 $\mathbb P^n$（定理 11.2.2）、广义旗流形（Kim2）等（PDF p.389）。
**误解 2：$J_{\mathcal V}$ 给出 $X$ 的全部亏格零 GW 不变量。** 反例：$X$ 为偶数维完全交时，$J_{\mathcal V}$ 取值于 $H^*(\mathbb P^n)$，只反映 $H^*(\mathcal V)=i^*H^*(\mathbb P^n)$ 的像，$H_0^{2m}(X)$ 中的本原部分完全丢失（PDF p.384）。只有 $\dim X\ge3$ 才有 $J_{\mathcal V}=i_!(J_X)$（命题 11.2.3, PDF p.382–383）。
**误解 3：名中的「超平面截面」要求 $X$ 是超平面。** 「超平面截面」是历史名，源自 [MP1] 把线性 $\sigma$ 模型关联函数限制到反典范超曲面的量子限制公式（PDF p.387）；本原理对任意凸线丛的完全交成立，且与 [MP1] 的公式精神相近但范围更广。去掉凸性后 $\mathcal V_{\beta,k}$ 未必是丛，$J_{\mathcal V}$ 的定义失去前提（PDF p.387）。
**误解 4：$\overline I_{\mathcal V}=J_{\mathcal V}$ 可直接逐项比较。** 一般情形须先作唯一加权齐次三角变换（含 $f_0,f_i,h$），且要求 $Y$ 凸、$\deg q_i\ge0$（PDF p.388）。边界情形：五次簇的 $g=y_1/y_0-t_1\neq0$（$f=\log y_0$、$h=0$，PDF p.385）；而 Fano 超曲面 $\ell<n$ 时 $f=g=h=0$，才是逐项相等（PDF p.382）。

## 8. 在文献中的坐标
| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999 | §11.2.2, PDF p.387–389（印刷 p.364–366） | 本卡主文献：提出、设定、$J_{\mathcal V}$/$\overline I_{\mathcal V}$、猜想 11.2.7、$\mathbb P^n$ 验证与等价性 |
| Cox–Katz 1999 | §11.2.1, PDF p.379–386（印刷 p.356–363） | 定理 11.2.2、命题 11.2.1、命题 11.2.3、五次簇与 Fano 超曲面计算（本原理的证据与主要应用） |
| Cox–Katz 1999 | §2.6.2, PDF p.49（印刷 p.26） | 预告镜像定理的证明将用本原理（等变上同调的局部化） |
| Cox–Katz 1999 | §12.4, PDF p.428（印刷 p.405） | [BCFKvS1] 的阶乘技巧 = 本原理的朴素版本 |
| SY01-24（Siebert 讲义术语表） | 成品 §一，共 70 条（原书印刷 p.7–106） | **冲突**：无本原理、$I$ 函数、$J$ 函数、量子限制公式词条（全表检索 0 命中，属术语缺口）；且 #18「单值变换」、#21「叠」、#54「多胞体」、#58「反身多胞体」与本书「单值性/代数叠/多胞形/自反多胞形」不一致（_冲突表 T1/T3/T5/T6，本书口径优先） |
| SY01-25 资料卡 04 | §一 核心术语（原书印刷 p.17 附近）；§二 文献 34 条 | **冲突**：该卡把 $q\to0$ 记为「大复结构极限」（B 模型侧，$\epsilon\to0$ 为大辛结构极限）；本书本原理的 $q^\beta=e^{\int_\beta\delta}$ 是 A 模型 Kähler 参数的大半径极限（$t\to i\infty$）。同写 $q\to0$ 而模型/坐标不同（_冲突表 U3）→ 见 §11-C2；该卡亦无本原理词条 |
| Givental 1996（[Givental3]） | 预印本，alg-geom/9612001 | 提出量子超平面截面原理（PDF p.387 引） |
| Kim 1998（[Kim2]） | 预印本，alg-geom/9712008 | 正式表述本原理，证明广义旗流形情形（PDF p.387, 389） |
| Batyrev–Ciocan-Fontanine–Kim–van Straten 1998（[BCFKvS1]） | Nuclear Phys. B514 (1998), 640–666；alg-geom/9710022 | Grassmann 簇与完全旗流形中 CY 完全交三维簇的虚有理曲线数；引入阶乘技巧（PDF p.389, 428） |
| Morrison–Plesser 1995（[MP1]） | Nuclear Phys. B440 (1995), 279–354；hep-th/9412236 | 反典范超曲面的量子限制公式：与本原理精神相近、范围更窄（PDF p.387） |
| Tjøtta 1998（[Tjotta]） | 预印本，math/9802037 | 二次曲线网簇（determinantal nets of conics，dim $N=6$）上的可验证结果（PDF p.389）。**注意**：书 PDF p.389 原文作 "varieties of nets of quadrics"，与 [Tjotta] 实际对象（nets of *conics*）不符，属原文误引；卡片按论文实际对象订正 |
| B 级：nLab / 教材索引 | nLab「quantum cohomology」「Gromov–Witten invariant」；本书 §11.1.5（PDF p.372） | 索引级背景（凸丛、稳定映射、虚拟基本类）；无本原理专条（待核） |

## 9. 前置与后继
- 前置：MS-04（量子上同调：提供 $M(Y)$、$q^\beta$、$\operatorname{Euler}$ 类与虚拟基本类的语言）；MS-18（Frobenius 流形与 Dubrovin 联络：$J$ 函数的量子微分方程/势表示，是证明定理 11.2.2 时把本原理落地的工具）。
- 后继：MS-21（规范线性 σ 模型与相：§12.4 用本原理的朴素版本算 Grassmann 簇中 CY 完全交的瞬子数，PDF p.428）；MS-23（nef 分拆与 Batyrev 构造：环面完全交的镜像定理与本原理共用「$I$ 函数 $\leftrightarrow$ $J$ 函数」机制，PDF p.405 起）。

## 10. 形式化接口（Lean 可 sorry）
```lean
-- 只给签名与关键假设，允许 sorry；依据：Cox–Katz §11.2.2（PDF p.387–389）
variable (Y : Scheme) [Smooth Y] [IsProjective Y]
variable (V : LocallyFreeSheaf Y)      -- V = ⊕ L_i，每个 L_i 凸：∀ f : C → Y, H¹(C, f*L_i) = 0
variable (β : H2 Y)                    -- β ∈ H₂(Y, ℤ)

-- 稳定映射模空间上的向量丛及其正合列
noncomputable def Vk (k : ℕ) : VectorBundle (MBar 0 k Y β) := sorry    -- 𝒱_{β,k}
noncomputable def V' (k : ℕ) (i : Fin k) : VectorBundle (MBar 0 k Y β) := sorry

-- 取值于 H*(Y) 的形式函数
noncomputable def IbarV : FormalSeries (HStar Y) := sorry              -- \overline I_𝒱
noncomputable def JV : FormalSeries (HStar Y) := sorry                 -- J_𝒱

-- 猜想 11.2.7：唯一加权齐次三角变换后两者相等（书中一般情形未证）
theorem quantum_hyperplane_section_principle
    (hconv : Convex Y) (hdeg : ∀ i, 0 ≤ degQ i) :
    ∃ (f₀ h : FormalSeries (HStar Y)) (f : Fin r → FormalSeries (HStar Y)),
      IsTriangularWeightedHomogeneous f₀ h f ∧
      changeVars f₀ h f IbarV = JV := by
  sorry
```

## 11. 待核清单
- [ ] **C1（术语级）** SY01-24 术语表无「量子超平面截面原理 / $I$ 函数 / $J$ 函数 / 量子限制公式」词条（全表 0 命中），SY01-25 卡 04 亦无 → 术语缺口；是否补收由 lead 定。术语冲突按 _冲突表 T1/T3/T5/T6 统一为「单值性/代数叠/多胞形/自反多胞形」。
- [ ] **C2（坐标级）** SY01-25 卡 04 §一 把 $q\to0$ 记为「大复结构极限」（B 模型侧）；本书本原理的 $q^\beta=e^{\int_\beta\delta}$ 是 A 模型 Kähler 参数的大半径极限（$t\to i\infty$）。二者同趋 0 但模型/坐标不同，换算按 _冲突表 U3 交由 MS-06 给出（其 $q$ 归一化 $c_1=-1$ 一处亦待核）。
- [ ] **T1（位置）** _queue.md 记本卡「第 8 章 §8.5」，与实际不符：原理在 §11.2.2（PDF p.387–389）；§8.5 是 A 模型联络/量子微分方程（PDF p.268 起），只是证明入口。待 lead 校正 queue。
- [ ] **T2（编号）** 英文原书 PDF p.388 OCR 作「Proposition 11.2.2, which asserts $I_{\mathbb P^n}=J_{\mathbb P^n}$」，但同书 PDF p.380、p.382、p.389 均作命题 11.2.1；中译 §11.2 第一个命题环境（line 1114）按共享计数器应为 11.2.1。疑原书笔误或 OCR 误识，待核印刷页 p.365（PDF p.388）。
- [ ] **T3（公式）** 英文 PDF p.388 作 $c_1(X)-c_1(\mathcal V)=\sum(\deg q_i)T_i$，中译 line 1489 作 $c_1(Y)-c_1(\mathcal V)$；只有后者与 $\mathbb P^n$ 时 $\deg q=n+1-\sum a_i$ 一致，故中译应为正；待核原书印刷（PDF p.388）确认是否 OCR 误读。
- [ ] **T4（凸簇定义）** 本书只给「凸线丛」（$H^1=0$，引 §11.1.5, PDF p.372）与「$\mathbb P^n$ 为凸」，未给一般「凸簇」的正式定义；使用时援引「虚拟基本类=通常基本类」（PDF p.381）。一般定义是否要求 $H^1(C,f^*T_Y)=0$，待核。
- [ ] **T5（$y_i$ 归一化）** §4 中 $y_2$ 的 $q^1$ 系数 $575$ 由 $S_1=120+770H+575H^2-1150H^3$ 与 $e^{t_1H}$ 乘出，须与 §11.1（PDF p.356–357）用 Frobenius 法定义的 $y_i$（含 log 解约定）对齐；$2875=5\cdot575$ 已自行核算，但 $H^4$ 部分（$B=y_3/y_0$）未逐步展开，仅依书中 p.386 结论。
- [ ] **T6（术语判据）** 英文 "quantum hyperplane section principle" 的「hyperplane」是历史名；是否在术语表另立「量子限制公式」条（与 [MP1] 区分）待 lead 定。
- **核验（2026-11-20）**：本卡经 `_核验记录.md` 核验，修正 1 处（详见该文件 ✗ 清单与证据链接）；其余待核条目保留。
