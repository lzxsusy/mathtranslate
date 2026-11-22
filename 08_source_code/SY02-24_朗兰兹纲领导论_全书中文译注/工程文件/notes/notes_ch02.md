# 第 2 章通读笔记：E. Kowalski, *Elementary Theory of L-Functions II*

底本页码：原书 21–37 页 = PDF 29–45（共 17 个 PDF 页；章首页 p.21 不印页码）。抽取件 `ch02_raw.txt` 已改为 `===== PDF PAGE n (BOOK m) =====` 标号，覆盖 PDF 30–45（BOOK 22–37）；章首页 PDF 29（BOOK 21）不在其内，本章开头的章题、§1 三句、§2 首段、(2.1) 与命题 2.1 据页图 `work/pages/c02_p029.png` 逐字核对。
**页码口径**：页眉印刷页码 = PDF 页 − 8 = `BOOK` 标号 − 8（实测 c02_p030 页眉“22 E. Kowalski”、c02_p031 页眉“2. Elementary Theory of L-Functions II 23”，故 PDF 30 = 印刷 22）。STYLE.md 的“原书页 = PDF 页 − 2”与本 PDF 不符；第 3 章章首页为印刷 38 页（PDF 46）。

## 三句话主旨

1. 本章把第 1 章关于 L 函数解析性质的断言补上证明梗概：先用 theta 函数与 Poisson 求和给出 Dedekind zeta 以及部分 zeta 的函数方程与解析延拓。
2. 再转向零点：零点计数、无零点区域与 Landau–Siegel 零点、切博塔廖夫型素理想定理，以及显式公式。
3. 最后讨论临界带内的量级（凸性界、近似函数方程、Lindelöf 猜想），并以“极点只能来自 zeta”这一现象与 Bernoulli 数的 p 进同余收尾。

## 逐节内容地图

### §1 引言（p.21，三句）
本章一半是展开第 1 章要点并给出证明梗概，一半是 L 函数零点这一课题的综述。

### §2 Hecke L 函数的函数方程（p.21–26）
- 路线：Dedekind zeta → 部分 zeta → theta 积分 → Poisson 求和 → 函数方程 (2.5)(2.6)；参 [La, XIII-3]、Hecke 原文。特点：显式，但伽马因子的出现未获概念解释。
- (2.1) ζ_K(s)=Σ_𝔞 (N𝔞)^{-s}；命题 2.1 = **Poisson 求和公式**（$\hat f(\xi)=\int f(x)e(-\langle x,\xi\rangle)dx$）。
- 为何不能直接对 ζ(s) 取 $f(x)=x^{-s}$：非 Schwartz。
- (2.2) 按理想类拆分；命题 2.2 = 部分 zeta 的完备化、函数方程、留数 $\frac{2^{r_1}(2\pi)^{r_2}R}{w\sqrt{|D|}}$，different 的理想类 $\mathfrak{d}$。
- 注 2.3：解析延拓只靠级数 + Poisson，与 Euler 乘积无关（h>1 时部分 zeta 无 Euler 乘积）。
- 证明：伽马积分 → (2.3) theta 积分；$G_1=\{\|y\|=1\}$，$G_1/U$ 紧（单位定理）；用 $1/w$ 处理单位根。
- (2.4) Hecke theta；引理 2.4 = (2.5) 变换公式，靠 $\hat f(\xi)=|\det Q|^{-1/2}\exp(-\pi Q'(\xi))$，判别式作为行列式出现。
- 在 $t=\alpha$ 拆积分、$t\mapsto\beta/t$，得四步等式链；$\beta=|D|^{-2}$、$\alpha=1/|D|$ 得 (2.6)；因 $\beta/\alpha=\alpha$，函数方程立得。
- 例 2.5：Riemann zeta 的经典情形，$\theta(y)=y^{-1/2}\theta(y^{-1})$。
- 注 2.6：$G_1/U$ 紧、$\|y\|$ 有限、$m<+\infty$ 三者等价；可反从 (2.6) 推出 $m<\infty$（Bill Duke 告知）。

### §3 L 函数的零点、显式公式（p.26–32）
- GRH 陈述；$N(\chi;T_1,T_2)$、$N(\chi;T)$；von Mangoldt $\Lambda(\mathfrak{a})$；(3.1) 对数导数的 Dirichlet 级数。
- 命题 3.1：(3.2) 零点计数（主项来自伽马因子），(3.3) $\sum_\rho|\rho|^{-1-\varepsilon}<\infty$；证明靠 Cauchy 定理 + Hadamard 乘积。
- 关键：$\operatorname{Re}(s)=1$ 上无零点（1896，Hadamard 与 de la Vallée Poussin），方法至今几乎唯一。
- 定理 3.2：无零点区域 $1-c_1/\log(T^d|D|N\mathfrak{m})$，可能有一个单重实零点 $\beta_1$（Landau–Siegel 零点），只在二次特征时出现；$\delta^*(\mathfrak{m})$ 记号。
- 例 3.3：虚二次域类数；Siegel (3.4) 非实效；Goldfeld 的实效改进（只多一个对数因子）。
- Siegel 机制：假设特征 ↔ 靠近 $s=1$ 的实零点；Goldfeld 用中心点 $s=1/2$ 的三阶零点作杠杆，故弱得多。
- 注 3.4：该方法给出的是下界，不能指望更好；Vinogradov 指数和可略微扩大无零点区域。
- (3.5) 素理想定理的类比；Siegel–Walfisz；GRH 给 $q<\sqrt X(\log X)^{-2}$。
- p.30 段：BFI 突破 GRH 直接推论；切博塔廖夫与 Artin L 函数的困难；随机矩阵、Montgomery 对相关、Rudnick–Sarnak、Katz–Sarnak、Conrey–Soundararajan（正比例实特征无 Landau–Siegel 零点）。
- 命题 3.5：(3.6) 显式公式，证明靠 Mellin 反演 + 移线 + 函数方程 + $\hat\varphi(1-w)=\hat\psi(w)$。

### §4 临界带内 L 函数的量级（p.32–36）
- 动机：类数公式、导子方向的一致性、与零点分布的联系；“量级”兼指按 $s$ 与按导子。
- 解析延拓给出阶 $\le1$ 的整函数：$\Lambda(\chi,s)\ll\exp(|s|^{1+\varepsilon})$；$L$ 亦然。
- 平凡界：$\operatorname{Re}(s)>1+\delta$ 时 $\ll1$；$\operatorname{Re}(s)<-\delta$ 时 $\ll|s|^{(1-\sigma)/2}$。
- Phragmén–Lindelöf ⇒ 凸性；猜想 4.1 = Lindelöf（GRH 蕴涵；"近似函数方程"动机）。
- 命题 4.2：(4.1) 两段截断级数，$XY=|D|N\mathfrak{m}$；$V_s,W_s$ 是截断型核。
- 推论 4.3：凸性界 $\ell(\sigma)$（$\ell(1)=0$，$\ell(0)=1/2$），临界线上指数 $1/4+\varepsilon$。
- 振荡与平方根哲学；突破凸性界 ⇒ 深刻算术；Weyl 的 $1/6$；Burgess、Conrey–Iwaniec；Iwaniec、Sarnak 与算术量子混沌。
- 命题 4.2 的证明：$I$ 先展开成第一和，再移到 $\operatorname{Re}=-3$ 拣出 $w=0$，对余项用函数方程回到绝对收敛域。

### §5 零碎内容，包括极点（p.36–37）
- 酉归一化后 $s=1$ 是唯一可能极点，且总由 $\zeta$ 的单极点解释：$L(f,s)=\zeta(s)^kL(f_1,s)$；Dedekind、Rankin–Selberg（对称平方）、Artin（Brauer）；阶数 = 平凡表示重数；Tate 猜想。
- 极点与正系数；“调和级数是唯一真正发散的级数”。
- Serre 的观察：(5.1) 负整数取值；von Staudt–Adams 定理给分母的素数 $p-1\mid 2k$；于是模 $p$ 的“极点”仍由调和级数解释；Leopoldt 的 p 进 zeta。

## 体裁

- 综述 + 证明梗概，夹大量评注与文献指引；无习题，无形式化定理环境。
- 编号：公式 (2.1)–(2.6)、(3.1)–(3.6)、(4.1)、(5.1)；条目号 2.1–2.6、3.1–3.5、4.1–4.3；脚注 9 条。
- 作者口吻第一人称（"我们"、"我"），译文用"我们"。

## 风险点（逐条已核页图）

1. **(2.3) 之前那两行伽马积分**：抽取件指数错乱（`ys/2-dyy`），页图为 $\pi^{-s/2}\Gamma(s/2)|z|_\sigma^{-s}=\int_0^{+\infty}\exp(-\pi y|z|_\sigma^2)y^{s/2}\frac{dy}{y}$ 与 $(2\pi)^{-s}\Gamma(s)|z|_\sigma^{-s}=\int_0^{+\infty}\exp(-2\pi y|z|_\sigma^2)y^{s}\frac{dy}{y}$。
2. **p.23 双重求和第二行下标**：影印作 "$\sum_{u\in\mathcal{O}}$"（裁图确认），与上一行 "$\sum_{u\in U}$" 不一致；按上下文两层求和合并为对 $\mathcal{O}$ 中非零元的一次求和，译文排 $\sum_{z\in\mathcal{O},\,z\neq0}$ 并出译注。
3. **四步等式链**：第三、四步里的常数因子是 $|D|^{1/2}\beta^{(s-1)/2}$ 与修正项 $|D|^{-1/2}\beta^{(s-1)/2}\frac{2m}{1-s}(\beta/\alpha)^{(1-s)/2}$，逐个核对无误；抽取件把 $|D|$ 印成 `IDI`，不可照抄。
4. **(2.5) 的因子**：$\frac{1}{\sqrt{|D|}\prod_i x_i}$，且自变量是 $|D|^{-2/d}x^{-1}$（逐分量取倒数，整体缩放到判别式指数），第二个变量是理想类 $\mathfrak{d}^{-1}$。
5. **(3.6) 零点求和下标**：影印为 "$\zeta(\rho)=0,\ 0<\operatorname{Re}(\rho)<1$"（裁图确认），当为 $L(\chi,\rho)=0$；译文照排并出译注。
6. **交叉引用**：文中 "(4.5)"、"(5.3)"、"(5.4)"、"Section 5"、"Section 6"、"Proposition 2.1"、"(5.1)" 均指**第 1 章**编号（第 2 章公式自 (2.1) 起算），其中 "Proposition 2.1" 与 "(5.1)" 尤易误读，出译注。
7. **符号**：$D$ 为判别式（书中写 $|D|$）；$\mathfrak{d}$ 为 different 的理想类，$N\mathfrak{d}=|D|$；$w$ 为单位根个数；$R$ 为调节子；$H(K)$ 为理想类群；$H_{\mathfrak{m}}$ 为射线类群。
8. **脚注 9 条**全部译出（置于对应段落）；脚注 2 与脚注 8 内容重复（$\chi=1$ 时乘 $s(1-s)$），照原书各自保留。
9. **§5 的 von Staudt 句**：原文“$p-1\mid 2k$”与随后的同余 $x^{k-1}\equiv x^{-1}\pmod p$ 不自洽（正确的充分必要条件是 $p-1\mid k$）；译文照录原书，出译注给出标准形式。

## 译注清单（12 条）

1. §2 开篇：theta 证法与 Tate 论文、阿代尔语言下的伽马因子（背景直觉）。
2. 命题 2.1 后：$e(z)=e^{2\pi iz}$ 与 Fourier 变换归一化（易错预警）。
3. 命题 2.2 后：different、$N\mathfrak{d}=|D|$、对偶理想类 $(a\mathfrak{d})^{-1}$（含糊点拨）。
4. 类数有限性那段：Dirichlet 类数公式的解析形式（背景直觉）。
5. p.23 双重求和：原书下标 $\mathcal{O}$ 的排印问题（易错预警）。
6. 例 2.5 后：$\theta$ 变换与 Poisson 求和、$-1/4$ 指数的来源（背景直觉）。
7. §3 首段：全部交叉引用指向第 1 章（含糊点拨）。
8. (3.6) 后：$\zeta(\rho)=0$ 应为 $L(\chi,\rho)=0$（易错预警）。
9. Goldfeld 段后：Siegel 二分法、Gross–Zagier 与三阶零点（背景直觉）。
10. 推论 4.3 后：“近似函数方程”之名、$\ell(\sigma)$ 的凸性（含糊点拨）。
11. §5 调和级数句后：正系数级数的 Landau 定理（背景直觉）。
12. §5 同余后：von Staudt–Clausen 的标准形式与 $p-1\mid k$（易错预警）。
