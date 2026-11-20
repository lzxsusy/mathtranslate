---
id: MS-03
zh: 五次三维簇
en: quintic threefold
aliases: [五次超曲面, quintic hypersurface, 五次 Calabi–Yau 三维簇]
layer: L0
prereqs: []
sources:
  - "Cox–Katz 1999, PDF p.38–47（Ch.2 §2.1–2.5：A 模型关联函数、镜像族、镜像映射、n_d 表）"
  - "Cox–Katz 1999, PDF p.84–85（§4.2：以自反多胞形 Δ、Δ° 重访五次三维簇）"
  - "Cox–Katz 1999, PDF p.101–111（§5.2 最大幺幂指标、§5.4 例 1 的 h^{2,1}(V°)=1）"
  - "A 级：Griffiths 1969, Ann. of Math. 90 (1969), 460–495, 498–541（Jacobian 环与 Hodge 数）"
  - "A 级：Batyrev 1994, J. Algebraic Geom. 3 (1994), 493–535（自反多胞形镜像构造）"
  - "A 级：Candelas–de la Ossa–Green–Parkes 1991, Nuclear Phys. B359 (1991), 21–74"
  - "B 级：本书 §1.4（PDF p.33–35）Calabi–Yau 簇与 Kähler 模空间定义；§5.3（PDF p.106–107）Griffiths–Dwork"
status: draft
review:
  drafter: agent-217
  reviewer: lead
  blindtest: pending
glossary_refs: [quintic threefold, quintic hypersurface, Calabi–Yau variety, Hodge number, mirror map, Picard–Fuchs equation]
symbols_refs: ["$H$", "$n_d$", "$h^{1,1}$", "$h^{2,1}$", "$\\psi$", "$x=\\psi^{-5}$", "$q$", "$\\Delta$", "$\\Delta^\\circ$"]
updated: 2026-11-20
---

# MS-03 五次三维簇

## 1. 一句话

光滑五次三维簇，是本书把镜像对称算到枚举预测的最小 Calabi–Yau 三维例子。

## 2. 为什么需要它

- **§1.4 的抽象定义需要一个落地对象。** 第 1 章 §1.4 只给了 Calabi–Yau 簇（PDF p.34）与复化 Kähler 模空间 $K_{\mathbb C}(V)/\mathrm{Aut}(V)$（PDF p.35）的一般定义，紧接着 p.35–36 便预告「下一章先仔细描述光滑五次三维簇 $V\subset\mathbb P^4$ 的镜像」。缺了 $V$，$K_{\mathbb C}(V)$ 就只是记号：五次三维簇满足 $h^{2,0}=0$、$h^{1,1}=1$，正是该定义最干净的对象。
- **全书三条战线在它身上交汇。** A/B 模型三点函数（PDF p.38、p.45–46）、Batyrev 环面镜像（§4.2 PDF p.84–85 的 $\Delta,\Delta^\circ$；§5.4 PDF p.110 的 $h^{2,1}(V^\circ)$ 公式）、Picard–Fuchs/Griffiths–Dwork（§5.3–5.4 PDF p.106–111）。缺了它，$\Delta$ 与 $\Delta^\circ$ 只是无例子的多胞形，最大幺幂指标 $\lambda^4=0$（PDF p.104）也无从算起。
- **它是唯一同时完成「预测—验证」的例子。** $n_1=2875$ 是经典计数（PDF p.46），$n_2,n_3,n_4$ 分别由 Katz2、ES1、Kontsevich2 独立算出（PDF p.46–47），镜像对称由此成为可证伪的数学命题；而镜像映射的归一化常数 $c_1=-1$ 只能靠 2875 定出（PDF p.46）。
- **它是最小可算情形。** $h^{1,1}=1$ 使镜像只有单参数复模（PDF p.40），Picard–Fuchs 是单变量 4 阶方程；换成 $\mathbb P(1,1,2,2,2)$ 后 $h^{2,1}(V^\circ)=2$，方程立刻变成偏微分方程组（PDF p.111–112）。

## 3. 定义（全假设）

**定义 3.1（光滑五次三维簇）.** 设 $k$ 为特征 0 的代数闭域，$f\in k[x_0,\dots,x_4]$ 为 5 次齐次多项式，$f\neq0$。假设 (i) $f$ 无平方因子；(ii) 光滑性（Jacobian 判据）：$\partial f/\partial x_0,\dots,\partial f/\partial x_4$ 在 $\mathbb P^4$ 中无公共零点，即 $V(f)$ 光滑。令 $V=V(f)\subset\mathbb P^4$。则 $\dim V=4-1=3$；由 $\mathbb P^4$ 的伴随公式 $K_V=\mathcal O_{\mathbb P^4}(-5)|_V\otimes\mathcal O_{\mathbb P^4}(5)|_V\cong\mathcal O_V$；由 Lefschetz 超平面定理 $b_1(V)=0$、$H^2(V,\mathbb Z)\cong H^2(\mathbb P^4,\mathbb Z)=\mathbb Z\cdot H$；并由 Kodaira 消失 $H^i(V,\mathcal O_V)=0$（$0<i<3$）。故 $V$ 满足下面的定义 3.2，是光滑 Calabi–Yau 三维簇。

**定义 3.2（Calabi–Yau 簇；本书 PDF p.34）.** $d$ 维正规紧致簇 $V$ 称 Calabi–Yau 簇，若 (i) 至多 Gorenstein 典范奇点；(ii) 对偶化层 $\widehat\Omega_V^d\cong\mathcal O_V$；(iii) $H^1(V,\mathcal O_V)=\dots=H^{d-1}(V,\mathcal O_V)=0$。若还只有 Gorenstein $\mathbb Q$-析因终端奇点，则称极小 Calabi–Yau 簇。

**定义 3.3（镜像五次族；本书 PDF p.40–41）.** 令 $G=\{(a_1,\dots,a_5)\in\mathbb Z_5^5:\sum a_i\equiv0\pmod 5\}/\mathbb Z_5$（分母为对角 $\mathbb Z_5$），$\mu=e^{2\pi i/5}$，$g\cdot(x_1,\dots,x_5)=(\mu^{a_1}x_1,\dots,\mu^{a_5}x_5)$。设
$$\bar X_\psi=\{x_1^5+x_2^5+x_3^5+x_4^5+x_5^5+\psi\,x_1x_2x_3x_4x_5=0\}\subset\mathbb P^4/G .$$
假设 $\psi^5\neq-5^5$（等价于 $\psi\neq-5\mu^i$，$0\le i\le4$），此时 $\bar X_\psi$ 是 $\mathbb P^4/G$ 中的 Calabi–Yau 轨形；其解奇异化记为 $V^\circ_\psi$（三维时解奇异化不唯一，Morrison2 给一个明确选择；不同选择复模与 B 模型关联函数相同，PDF p.40）。$\psi\mapsto\mu\psi$ 给出 $V^\circ_\psi\cong V^\circ_{\mu\psi}$，故 $\psi^5$ 与 $x=\psi^{-5}$ 良定义；奇异点 $\psi=-5\mu^i$、$\psi=\infty$ 分别对应 $x=-5^{-5}$、$x=0$（PDF p.40–41）。

**定义 3.4（大复结构极限即最大幺幂点；本书 PDF p.41、p.104）.** 单参数 Calabi–Yau 三维簇族在 $x=0$ 处的局部单值性 $T=I+N$ 满足 $N^3\neq0$、$N^4=0$（最大幺幂），且 $x=0$ 是 Picard–Fuchs 算子的正则奇点，其指标方程为 $\lambda^4=0$。等价刻画（PDF p.41）：杯积 $\smile H$ 在 $\oplus H^{p,p}(V)$ 上最大幂零（$(\smile H)^3\neq0$，$(\smile H)^4=0$），在镜像下对应单值性之对数 $N$。

**本书用法.** Cox–Katz 在 PDF p.38 直接断言「光滑五次超曲面 $V\subset\mathbb P^4$ 是 Calabi–Yau 簇」，不重证 $K_V\cong\mathcal O_V$ 与 $b_1=0$；p.25 脚注给的是「$b_1=0$、典范类平凡的光滑紧致连通三维簇」这一**光滑版**，而 p.34 的**簇版**允许 Gorenstein 典范奇点——正是为了容纳 p.40 的 $V^\circ$（轨形及其解奇异化）。与标准（光滑）定义无出入，只是放宽了奇点条件。

## 4. 最小例子（能算出）

取 Fermat 五次 $X_5=\{x_0^5+x_1^5+x_2^5+x_3^5+x_4^5=0\}\subset\mathbb P^4$；$\partial f/\partial x_i=5x_i^4$ 的公共零点只有原点，故 $X_5$ 光滑。

1. **$h^{1,1}=1$。** Lefschetz 超平面定理：$H^2(X_5,\mathbb Z)\cong H^2(\mathbb P^4,\mathbb Z)=\mathbb Z\cdot H$，故 $h^{1,1}(X_5)=1$（PDF p.40 对一般五次同样断言）。
2. **$H^3=5$。** $\int_{X_5}H^3=\deg X_5=5$，这正是 PDF p.38 式 (2.1) 中 $\langle H,H,H\rangle=5+\sum_{d\ge1}n_dd^3q^d/(1-q^d)$ 的常数项。
3. **$h^{2,1}=101$（本卡自算；书只给理论，未印此数）。** 光滑超曲面的 Griffiths 留数理论给 $H^{2,1}_{\mathrm{prim}}(X_5)\cong R_5$，其中 $R=\mathbb C[x_0,\dots,x_4]/(5x_0^4,\dots,5x_4^4)$ 为 Jacobian 环（PDF p.106–107 引 Griffiths1）。$\dim\mathbb C[x]_5=\binom{9}{4}=126$；被某个 $x_i^4$ 整除的 5 次单项式共 $5$（$x_i^5$）$+5\cdot4=20$（$x_i^4x_j$，$i\neq j$）$=25$ 个。故 $\dim R_5=126-25=101$，即 $h^{2,1}=101$。
4. **$b_3$ 与 $\chi$。** CY 三维簇的 Hodge 菱形对称性（PDF p.27–28）给 $b_3=2+2h^{2,1}=2+202=204$，$\chi=2(h^{1,1}-h^{2,1})=2(1-101)=-200$。
5. **Chern 类核对。** $c(T_{X_5})=(1+H)^5/(1+5H)|_{X_5}=1+10H^2-40H^3+\cdots$（用 $(1+5H)^{-1}=1-5H+25H^2-125H^3+\cdots$），故 $c_2\cdot H=10H^3=50$，$c_3=-40H^3=-40\cdot5=-200$，与第 4 条的 $\chi$ 一致。
6. **A 模型级数的前几项。** 一般五次三维簇含 2875 条直线，故 $n_1=2875$（PDF p.46）。代入式 (2.1)：$\langle H,H,H\rangle=5+2875q+4\,876\,875\,q^2+\cdots$，其中 $q^2$ 系数 $=2875\cdot1^3+609250\cdot2^3=2875+4\,874\,000=4\,876\,875$（$n_2=609250$ 见 PDF p.47 表）。
7. **镜像侧的 Batyrev 核对。** $\Delta^\circ$ 的整点只有 5 个顶点与原点共 6 个，代入 $h^{2,1}(V^\circ)=l(\Delta^\circ)-5-\sum_{\Gamma^\circ}l^*(\Gamma^\circ)+\sum_{\Theta^\circ}l^*(\Theta^\circ)l^*(\hat\Theta^\circ)$ 得 $6-5-0+0=1$（PDF p.110，§5.4 例 1），与 $h^{1,1}(X_5)=1$ 相符。另一方向：$\Delta\cap M$ 的点即 5 次单项式，$l(\Delta)=\binom{9}{4}=126$；5 个面各为 $5\Delta_3$，$l^*(5\Delta_3)=\binom{4}{3}=4$；$\Delta^\circ$ 各边差向量最大公约数为 1（如 $(2,1,1,1)$）故无余维 2 贡献。于是 $h^{1,1}(V^\circ)=126-5-5\cdot4=101=h^{2,1}(X_5)$。
8. **镜像映射前两项。** $q=c_1(x-770x^2+\cdots)$，由 $n_1=2875$ 定出 $c_1=-1$（PDF p.43、p.46），故 $q=-x+770x^2+\cdots$，反解 $x=-q+770q^2+\cdots$。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | $V$ 是光滑 Calabi–Yau 三维簇：$K_V\cong\mathcal O_V$、$b_1=0$、$h^{3,0}=1$ | PDF p.38（断言）、p.34（定义核对）；p.25 脚注（光滑版） | 由伴随公式与 Lefschetz 超平面定理补证 |
| 2 | $h^{1,1}=1$，$h^{2,1}=101$，$b_3=204$，$\chi=-200$ | $h^{1,1}$：PDF p.40；$h^{2,1}$：本卡 §4(3) 用 §5.3 的 Griffiths 理论；$b_3,\chi$：PDF p.27–28 | $h^{2,1}=101$ 书中未直接印出，见 §11 |
| 3 | $H^3=\deg V=5$；一般五次含 $2875$ 条直线，$n_1=2875$ | PDF p.38 式 (2.1)；p.46 | 常数项 5 与 $H^3=5$ 对应 |
| 4 | $h^{1,1}=1$ 迫使镜像只有一个复模参数：$\dim H^1(V^\circ,T_{V^\circ})=1$，$x=\psi^{-5}$ 是局部坐标 | PDF p.40–41 | 镜像族的单参数性来源 |
| 5 | $x=0$ 是大复结构极限/最大幺幂点：$N^3\neq0$、$N^4=0$，指标 $\lambda^4=0$ | PDF p.41；p.104（指标方程） | 与 $x=-5^{-5}$（幺幂但非最大，$N^2=0$）区分 |
| 6 | 枚举预言：$n_1=2875$，$n_2=609250$，$n_3=317206375$，$n_4=242467530000$，$n_5=229305888887625$ | PDF p.46–47；Katz2、ES1、Kontsevich2 | 整数性与 $5^3\mid n_d$ 仅为猜想（PDF p.47、LY1） |

## 6. 推导流程（D1…Dn）

- **D1（$V$ 是 Calabi–Yau 簇）.** 伴随公式 $K_V\cong\mathcal O_V$、Lefschetz 给 $b_1=0$，$H^i(V,\mathcal O_V)=0$，对照定义 3.2。依据：PDF p.38 断言 + p.34 定义 + p.25 脚注。
- **D2（Hodge 数与不变量）.** $H^2(V,\mathbb Z)=\mathbb Z\cdot H$ 给 $h^{1,1}=1$；Jacobian 环 $R_5$ 的维数给 $h^{2,1}=126-25=101$；再由 Hodge 菱形对称性得 $b_3=204$、$\chi=-200$。依据：PDF p.40、p.27–28、p.106–107（Griffiths）。
- **D3（A 模型）.** $H^3=5$ 与 $n_d$ 的定义（多覆盖公式 $\langle I_{0,3,d}\rangle(H,H,H)=\sum_{k\mid d}n_kk^3$）给出 $\langle H,H,H\rangle=5+\sum_d n_dd^3q^d/(1-q^d)$。依据：PDF p.38 式 (2.1)、p.39。
- **D4（构造镜像族）.** $h^{1,1}(V)=1\Rightarrow$ 镜像复模一维；Greene–Plesser 取 $V^\circ_\psi=(\bar X_\psi\subset\mathbb P^4/G)$ 的解奇异化，$x=\psi^{-5}$ 为模坐标。依据：PDF p.40–41（GPl）。
- **D5（大复结构极限）.** $x=0\Leftrightarrow q=e^{2\pi it}\to0$；$\smile H$ 在 $\oplus H^{p,p}$ 上最大幂零，镜像下 $T=I+N$ 最大幺幂；4 阶 Picard–Fuchs 算子在 $x=0$、$x=-5^{-5}$ 正则奇异，$x=0$ 处指标方程 $\lambda^4=0$。依据：PDF p.41、p.43、p.104。
- **D6（镜像映射与周期）.** 消失圈 $\gamma_0$（单值不变）与 $\gamma_1$（绕 $x=0$ 变为 $\gamma_1+\gamma_0$，$m=1$，Morrison2）给 $q=\exp\!\big(2\pi i\int_{\gamma_1}\Omega/\int_{\gamma_0}\Omega\big)=c_1(x-770x^2+\cdots)$，其中 $y_0(x)=\sum_n\frac{(5n)!}{(n!)^5}(-1)^nx^n$ 是 PF 方程唯一全纯解。依据：PDF p.42–43、p.45–46。
- **D7（镜像恒等式）.** $5+\sum_d n_dd^3q^d/(1-q^d)=\frac{5}{(1+5^5x)\,y_0(x)^2}\big(\frac{q}{x}\frac{dx}{dq}\big)^3$；用 $n_1=2875$ 令两边 $q$ 系数相等，得 $c_1=-1$。依据：PDF p.45–46。
- **D8（验证与重解释）.** 展开得 $n_1,\dots,n_5$（PDF p.46–47），与 Katz2/ES1/Kontsevich2 的独立计算一致；再按 Batyrev 用自反多胞形 $\Delta,\Delta^\circ$ 重写 $V$ 与 $V^\circ$，并用 §5.4 的公式复核 $h^{2,1}(V^\circ)=6-5=1$。依据：PDF p.47、p.84–85、p.110。

## 7. 常见误解与反例（≥2）

- **误解 1：$V$ 的镜像还是 $\mathbb P^4$ 中的五次超曲面，甚至就是 $V$ 自己。** 错。$V^\circ$ 是 $\mathbb P^4/G$ 中超曲面的解奇异化（PDF p.40），Hodge 数对调为 $h^{1,1}(V^\circ)=101$、$h^{2,1}(V^\circ)=1$；镜像族的成员 $\bar X_\psi$ 是轨形，$\psi=0$ 时 $\bar X_0=\{x_1^5+\cdots+x_5^5=0\}/G$ 甚至不是光滑流形。正确说法是：镜像 Hodge 菱形由 $h^{p,q}(V)=h^{3-p,q}(V^\circ)$ 作 45° 反射（PDF p.27–28）。
- **误解 2：$h^{1,1}=1$、$h^{2,1}=101$、$\chi$、$b_3$ 是各自独立的输入。** 错。只要知道 $h^{1,1}$ 与 $h^{2,1}$，CY 三维簇的对称性即强制 $b_3=2+2h^{2,1}=204$、$\chi=2(h^{1,1}-h^{2,1})=-200$（PDF p.27–28）；§4(5) 用 Chern 类独立算出的 $c_3=-200$ 与之一致，可作交叉验证，而不是第三个输入。
- **误解 3：$n_1=2875$ 是镜像对称算出来的。** 错。2875 是经典结果（一般五次三维簇上的直线数，PDF p.46），镜像计算拿它当边界条件反定 $c_1=-1$。并且 $n_d$ 一般不是 $d$ 次有理曲线的条数：PDF p.39 指出 $d=10$ 时 Pandharipande 发现 $n_{10}$ 因六结点五次有理曲线的二重覆盖而偏离曲线计数；Clemens 猜想（$n_d$ 等于 $d$ 次有理曲线的条数）只在 $d\le9$ 时已证（JK1，PDF p.39）。$n_d$ 的正式定义是「瞬子数」，由 $\sum_{k\mid d}n_kk^3$ 给出（PDF p.39）。
- **误解 4：三维镜像族的解奇异化唯一，所以镜像族唯一。** 错。PDF p.40 明确说三维解奇异化无典范选择，Morrison2 只给出一个明确选择；书中只承诺不同选择给出相同复模与相同 B 模型关联函数。边界情形：镜像定理（PDF p.47）的陈述不依赖这一选择，但任何具体计算必须先固定一个 $\Sigma^\circ$（PDF p.84–85）。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999（本译本） | PDF p.38–47（Ch.2）、p.84–85（§4.2）、p.101–111（§5.2/§5.4）、p.34–35（§1.4 定义） | 全书以五次三维簇为贯穿例子：A 模型 Yukawa、Greene–Plesser 镜像族、镜像映射、$n_d$ 表、Batyrev 重解释。书内页码均为 PDF 物理页（$=$ 印刷页 $+23$） |
| SY01-24（Siebert 讲义中译本）术语表 | 第 18 条（p.21，第 1 章）、§83 行说明 | **冲突（术语）**：monodromy 在 SY01-24 统一译「单值变换」（第 18 条备注「本轮由『单值化』改定」；§83 行「全书统一为『单值变换』」），本书（PDF p.41、p.104）与 _冲突表 T1 用「单值性」。本卡从本书口径，孰对不判 |
| SY01-24 术语表（续） | 第 2 条（p.7，概览） | **冲突（范围）**：SY01-24 只收「Calabi–Yau 流形」（光滑流形口径），本书 PDF p.34 的 Calabi–Yau **簇**允许 Gorenstein 典范奇点；五次族的镜像 $V^\circ$ 先是 $\mathbb P^4/G$ 中的轨形（PDF p.40），必须用簇版定义才称得上 CY，两处适用范围不同 |
| SY01-25 资料卡 04（术语文献勘误） | §一 核心术语；§二 文献；§三 勘误 | 无直接冲突：卡 04 的 25 条术语（HMS、SYZ 环面纤维化、$A_\infty$-预范畴、大复结构极限 $q\to0$ 等）针对 HMS/$A_\infty$ 语境，未收五次三维簇条目；本书不讲 $A_\infty$/Fukaya（_冲突表 U4），本卡只在「CY 三维簇/Hodge 数」层面与之相接；其「大复结构极限 $=q\to0$」与本书 PDF p.41 的 $x=0$（$q=0$）相容 |
| Candelas–de la Ossa–Green–Parkes 1991（CdGP） | Nuclear Phys. B359 (1991), 21–74 | A 级原始文献：首次由镜像对称算出五次三维簇的 $n_d$；本书 PDF p.38 明说基本沿用 CdGP 方法，p.40 指出 CdGP 用 $-5\psi$ 而非 $\psi$，p.46 指出 CdGP 亦得 $c_1=-1$ |
| Griffiths 1969 | Ann. of Math. 90 (1969), 460–495、498–541（本书 PDF p.106–107 引 Griffiths1） | A 级原始文献：留数理论与 Jacobian 环，§4(3) 的 $h^{2,1}=101$ 计算依据 |
| Batyrev 1994 | J. Algebraic Geom. 3 (1994), 493–535（本书 PDF p.84–85 引 Batyrev4） | A 级原始文献：自反多胞形对 $(\Delta,\Delta^\circ)$ 的镜像构造；§4.2 的顶点表与 §5.4 的 $h^{2,1}(V^\circ)$ 公式出处 |
| Greene–Plesser 1990 | Nuclear Phys. B338 (1990), 15–37（本书 PDF p.40 引 GPl） | A 级原始文献：$\mathbb P^4/G$ 中五次族的轨形镜像构造，定义 3.3 的出处 |

## 9. 前置与后继

- 前置：无（队列登记 `prereqs: —`）。但 §4(7) 的 Batyrev 交叉验证需先读 MS-08（扇与多胞形）、MS-09（自反多胞形）；§4(3) 的 $h^{2,1}$ 计算需 MS-10（Hodge 结构与滤过）；§6 D5 需 MS-12（单值性与最大幺幂）。
- 后继：MS-01（镜像对称）、MS-02（镜像映射，$q=c_1(x-770x^2+\cdots)$）、MS-06（Picard–Fuchs 方程）、MS-11（Hodge 结构变分，五次族的 $F^3\subset H^3$）、MS-12（单值性与最大幺幂）、MS-14（消失圈 $\gamma_0,\gamma_1$）、MS-19（量子超平面截面原理）、MS-22（锥形奇点跃迁，$b_3:204\to202$）、MS-23（nef 分拆，$\nabla_0=\{0\},\nabla_1=\Delta$）、MS-24（Berglund–Hübsch：Fermat 五次）。

## 10. 形式化接口（Lean 可 sorry）

```lean
import Mathlib.Algebra.MvPolynomial.Basic

/-- 光滑五次三维簇（§3 定义 3.1）：P^4 中的 5 次超曲面 + Jacobian 判据 -/
structure SmoothQuintic (k : Type*) [Field k] where
  f : MvPolynomial (Fin 5) k
  isHom : f.IsHomogeneous 5
  /-- 光滑：V(f) 上各偏导数无公共零点（只留命题槽，证明待补） -/
  smooth : Prop
  smooth_ok : smooth

/-- 本卡 §4 的 Hodge 数（由 Griffiths 留数理论自算，书中未直接印 101） -/
def h11 : ℕ := 1
def h21 : ℕ := 101
def b3 : ℕ := 2 + 2 * h21
def eulerChar : ℤ := 2 * ((h11 : ℤ) - (h21 : ℤ))

example : b3 = 204 := by decide
example : eulerChar = -200 := by decide

/-- 镜像族（§3 定义 3.3）：x = ψ^{-5} 为复模坐标，ψ^5 ≠ -5^5 -/
structure MirrorQuinticFamily where
  ψ : ℂ
  hψ : ψ ^ 5 ≠ -5 ^ 5
  x : ℂ

/-- A 模型三点函数 5 + Σ n_d d³ q^d/(1-q^d)（PDF p.38 式 (2.1)），暂以不透明函数占位 -/
opaque yukawaA : ℂ → ℂ
/-- B 模型侧 5/((1+5^5 x) y_0(x)^2) · ((q/x)(dx/dq))^3（PDF p.45–46） -/
opaque yukawaB : ℂ → ℂ

/-- 镜像恒等式（PDF p.45–46）：在镜像映射 x = x(q) 下两级数相等 -/
theorem mirror_identity (q : ℂ) (hq : q ≠ 0) : yukawaA q = yukawaB q := by
  sorry

/-- 最大幺幂点（§3 定义 3.4）：N^3 ≠ 0，N^4 = 0 -/
theorem quintic_MUM (N : Module.End ℚ (Fin 4 → ℚ)) :
    N ^ 3 ≠ 0 ∧ N ^ 4 = 0 := by
  sorry
```

## 11. 待核清单

- [ ] $h^{2,1}=101$、$b_3=204$、$\chi=-200$ 均由本卡自算（§4(3)(4)），书中未直接印出；第 6 章据队列 MS-22 提示出现过 $b_3=204\to202$ 的锥形奇点跃迁，页码待核。
- [ ] 式编号：「五次超曲面 4 阶方程 (2.8)」来自 _queue.md 的 MS-06 行；本次检索只在 chapter02.tex:258 找到硬编码的 (2.1)，其余用 `\eqref` 自动编号，无法确认 PF 方程确为 (2.8)。本卡一律用「§2.3 的四阶 Picard–Fuchs 方程（PDF p.43）」定位，待核后统一。
- [ ] **冲突（术语）**：SY01-24 术语表第 18 条 monodromy 译「单值变换」/§83 行说明，与本书「单值性」不一致；_冲突表 T1 已裁定「单值性」，本卡从本书口径。依据：SY01-24_术语表.md:27、:83；_冲突表 T1。
- [ ] **冲突（定义范围）**：SY01-24 第 2 条只收「Calabi–Yau 流形」（p.7 概览，无奇点版），本书 PDF p.34 的 Calabi–Yau 簇允许 Gorenstein 典范奇点；五次族的 $V^\circ$ 先为轨形、解奇异化后才成为流形（PDF p.40）。孰对不判，待 lead 复核是否需要统一为「Calabi–Yau 簇」。
- [ ] $n_d$ 的整数性、$d$ 不被 5 整除时 $5^3\mid n_d$、以及对所有 $d$ 的 $5^3\mid n_d$ 猜想（PDF p.47、LY1）在书后是否已被证明，待核。
- [ ] PDF p.39 的 Pandharipande $d=10$ 反例：只记下「$n_{10}$ 不是十次有理曲线数」的结论，具体偏差数值与原始文献出处待核。
- [ ] 队列 MS-12 行示例写「单参数族的 $T=I+N$，$N^2=0$；MUM 点」，而本书 PDF p.101–104 对五次族的 MUM 点给 $N^3\neq0$、$N^4=0$，$N^2=0$ 只出现在 $x=-5^{-5}$ 处；两者不是同一极限点，需 MS-12 卡处理（本卡按 PDF p.104 写）。
- [ ] CdGP 的 $-5\psi$ 约定（PDF p.40）与本书 $\psi$ 的换算关系书中只给一句提示，$x_{\mathrm{CdGP}}$ 与 $x=\psi^{-5}$ 的具体换算式待核。
- [ ] _冲突表 第三节维护：本卡的两条冲突未写入 _冲突表.md（本轮禁止改写既有文件），需 lead 同步登记。
