---
id: MS-11
zh: Hodge 结构变分
en: variation of Hodge structure
aliases: [VHS, 极化 Hodge 结构变分, polarized variation of Hodge structure]
layer: L1
prereqs: [MS-10]
sources:
  - "Cox–Katz 1999（中译本），PDF p.96–99（§5.1.1–5.1.4）：定义 (H,∇,H_Z,F^•)、Gauss–Manin 联络、Griffiths 横截性、退化与极限混合 Hodge 结构（A 级）"
  - "Cox–Katz 1999，PDF p.104–105（§5.2.2）：最大幺幂单值性（MUM）用极限混合 Hodge 结构定义（A 级）"
  - "Cox–Katz 1999，PDF p.127–128（§5.6.3）：归一化 Yukawa 耦合与 Gauss–Manin 联络、Hodge–Tate 型混合 Hodge 结构变分（A 级）"
  - "Cox–Katz 1999，PDF p.265–281（§8.5–8.6.1）：A 模型 Hodge 结构变分（定理 PDF p.277）与数学镜像对（PDF p.281）（A 级）"
  - "A 级：P. Griffiths, On the periods of certain rational integrals I, II, Ann. of Math. 90 (1969), 460–495、498–541（书内 [Griffiths1]）"
  - "A 级：W. Schmid, Variation of Hodge structure: the singularities of the period mapping, Invent. Math. 22 (1973), 211–319（[Schmid]）"
  - "A 级：P. Deligne, Équations différentielles à points singuliers réguliers, LNM 163, Springer 1970（[Deligne1]）"
  - "A 级：A. Landman, On the Picard–Lefschetz transformations, Trans. Amer. Math. Soc. 181 (1973), 89–126（[Landman]）"
  - "B 级：SY01-24 术语表 #17 Gauss–Manin 联络、#18 单值变换；SY01-24 讲义第 1 章式 (1.68)–(1.69)、(1.95)–(1.97)（B 级）"
  - "B 级：SY01-25 资料卡 04-术语文献勘误.md §二（[De]「Hodge 结构在无穷远处的局部行为」、[LTY]「极大单值」）（B 级）"
status: draft
review:
  drafter: agent-226
  reviewer: lead
  blindtest: pending
glossary_refs: ["Gauss–Manin connection", "monodromy（SY01-24 术语表 #18，按 _冲突表 T1 统一为「单值性」）"]
symbols_refs: ["$H$", "$\\nabla$", "$H_{\\mathbb Z}$", "$F^\\bullet$", "$\\Omega^1_S$", "$W_\\bullet$"]
updated: 2026-11-20
---

# MS-11 Hodge 结构变分

> 页码约定：本卡书内页码一律为本书 **PDF 物理页**（= 中译本 `\SourcePage{N}`；印刷页 + 23）。外部文献用原书页码/卷期页与定理号。

## 1. 一句话
让 Hodge 滤过随族横截变分、并用于表述镜像对称的结构。

## 2. 为什么需要它

镜像对称的最终形态就是「两个 Hodge 结构变分的同构」。第 1 章结尾（PDF p.36）写道：新引入的两个要素是量子上同调与 A 型 Hodge 结构变分；「镜像对称真正涉及两个 Hodge 结构变分在镜像映射下的同构——一个来自 B 模型，即由复模产生的通常 Hodge 结构变分；另一个来自 A 模型，即 A 型 Hodge 结构变分」，第 8 章末将以这种形式表述镜像定理，且「所要求的关联函数相等，将直接从 Hodge 结构变分的这一同构推出」。因此从第 5 章起，VHS 是把镜像对称翻译成几何的语言；在 B 模型侧，它就是周期积分的几何载体。第 2 章（PDF p.47–48）预告：一旦用镜像参数 $q$ 表示归一化 Yukawa 耦合 $Y$，就完全确定了 $H^3(V^\circ,\mathbb C)$ 上的 Hodge 结构变分；在适当基下 Gauss–Manin 联络的矩阵为 $\begin{pmatrix}0&0&0&0\\1&0&0&0\\0&Y&0&0\\0&0&1&0\end{pmatrix}$。$Y$ 不是孤立函数，而是「镜像族的 Hodge 结构不可缺少的一部分」，由此才猜测 A 模型一侧也存在 VHS。第 5 章 §5.6.3（PDF p.127–128）兑现这一点：在最大幺幂边界点用权滤过 $W_\bullet$ 的整平坦截面 $g_0$ 归一化 $\Omega$，得到 Hodge–Tate 型混合 Hodge 结构变分，进而命题 `prop:normalized-yukawa-pf` 给出 $\nabla_\delta^2(\nabla_\delta^2\Omega/Y)=0$。

在 A 模型侧，第 8 章必须**构造** A 模型 VHS，否则镜像对无法陈述。§8.5.4 定理（PDF p.277）把量子上同调上的 $(\mathcal H,\nabla,\mathcal H_{\mathbb Z},\mathcal F^\bullet)$ 实现为权 $d$ 的极化 VHS；§8.6.1（PDF p.281）才给出数学镜像对 = A 模型 VHS 与 B 模型 VHS 的（极化）同构。没有本节的语言，「镜像对称 = 两个 VHS 同构」这句话无从定义。

在退化/边界侧，VHS 把「周期在边界点的行为」变成结构理论：单值性定理、幂零轨道定理、权滤过与极限混合 Hodge 结构（PDF p.98–99）全部以 VHS 为对象陈述，并直接喂给 MS-12（最大幺幂单值性）与 MS-13（极限混合 Hodge 结构）。只把 PF 方程当 ODE 看，得不到这些；在计算侧，横截性把 GM 联络矩阵压成上三角，于是 PF 方程可从联络矩阵机械读出（§5.3–5.4；§4 用五次族演示：横截性 ⇒ $\omega_j\in F^{4-j}$ ⇒ 矩阵上三角 ⇒ 四阶 PF 方程）。

## 3. 定义（全假设）

**设定.** 设 $S$ 为连通光滑拟射影复流形（底空间），$\pi:X\to S$ 为相对维数 $n$ 的光滑紧合态射（一族 $n$ 维光滑射影簇；书 p.97 只写「光滑态射」，紧合性由射影族默认，见 §11 C8），$k$ 为固定整数（$0\le k\le 2n$）。

**(A1) 整数局部系统.** $H_{\mathbb Z}:=R^k\pi_*\mathbb Z$ 是 $S$ 上的局部常值 $\mathbb Z$-层；$H:=R^k\pi_*\mathbb C=H_{\mathbb Z}\otimes_{\mathbb Z}\mathbb C$ 为局部常值 $\mathbb C$-层，纤维 $H_s=H^k(X_s,\mathbb C)$，并带来自 $R^k\pi_*\mathbb R$ 的实结构。

**(A2) 平坦联络.** $H$ 上带唯一平坦联络 $\nabla=\nabla^{\mathrm{GM}}$（Gauss–Manin 联络）：$\nabla(s\otimes f)=s\otimes df$（$s$ 局部常值截面，$f$ 全纯函数）；等价地，$\nabla$-平坦截面恰为局部系统的截面，且 $\nabla^2=0$。

**(A3) Hodge 滤过.** $F^\bullet$ 是 $H\otimes\mathcal O_S$ 的递减滤过子层
$$0=F^{k+1}\subset F^k\subset F^{k-1}\subset\cdots\subset F^0=H\otimes\mathcal O_S,$$
每个 $F^p$ 是局部自由 $\mathcal O_S$-模（全纯子丛），$\operatorname{rank}F^p$ 在 $S$ 上为常数。

**(A4) Griffiths 横截性.** $\nabla(F^p)\subset F^{p-1}\otimes\Omega^1_S$（$p=1,\dots,k$；约定 $F^{-1}:=F^0$）。

**(A5) 纤维条件.** 对每个 $s\in S$，$(H_s,F^\bullet_s)$ 是权 $k$ 的 Hodge 结构：$H_s$ 带实结构与共轭，且
$$F^p_s\oplus\overline{F^{k-p+1}_s}=H_s,\qquad H^{p,q}_s:=F^p_s\cap\overline{F^q_s},\qquad H_s=\bigoplus_{p+q=k}H^{p,q}_s.$$
等价地 $H^{p,q}_s\cong F^p_s/F^{p+1}_s$；故 Hodge 结构由 $(H_{\mathbb Z},F^\bullet)$ 唯一确定。

**(A6) 极化（加强版，非定义必需）.** 权 $k$ 极化 VHS 另给 $\nabla$-平坦双线性型 $Q:H\times H\to\mathbb C$，满足 $Q(\alpha,\beta)=(-1)^kQ(\beta,\alpha)$、$Q(F^p,F^{k-p+1})=0$，且
$$Q\bigl(i^{p-q}\alpha,\overline\alpha\bigr)>0\qquad(\alpha\in H^{p,q}_s,\ \alpha\neq0).$$
本书中 $Q$ 来自 Kähler 类 $\omega$ 限制在本原上同调 $H^k_0=PH^k$ 上：$Q(\alpha,\beta)=(-1)^{k(k-1)/2}\int_X\omega^{n-k}\wedge\alpha\wedge\beta$，即式 (5.1)（PDF p.97）。

**定义.** 称四元组 $(H,\nabla,H_{\mathbb Z},F^\bullet)$ 为权 $k$ 的 **Hodge 结构变分**（原文 "We call $(H,\nabla,H_{\mathbb Z},F^\bullet)$ a variation of Hodge structure"，PDF p.97）。

**本书用法.** Cox–Katz 在 PDF p.97 采用的正是上述四元组定义（与 Griffiths 的经典版本一致），但**定义不含极化**：$Q$ 只在本原上同调上由 Kähler 类 $\omega$ 借式 (5.1) 得到，故「极化 VHS」是加强版（§8.5.4 定理 p.277 的陈述即「由 $S$ 极化」）。书中**不使用缩写 VHS**，本卡仅为行文方便使用，正式稿按书内写法。另注意：与「Hodge 结构的族」的全部区别在 (A2)+(A4)——$H^{p,q}$ 本身不随族全纯变化（PDF p.96–97 原话），只有 $F^\bullet$ 是；这是 §7 M1 的核心。【待核：$Q$ 在 (A6) 中的正负号约定，见 §11 C11】

## 4. 最小例子（能算出）

**族.** 五次三维簇的单参数镜像族（[Morrison2]；PDF p.110–111，Example 5.4.1）
$$V_\psi=\{F_\psi=x_1^5+x_2^5+x_3^5+x_4^5+x_5^5+\psi\,x_1x_2x_3x_4x_5=0\}\subset\mathbb P^4,\qquad\psi\in\mathbb C^*,$$
模 $G=(\mathbb Z/5)^4$ 的群作用；令 $z=\psi^{-5}$，$\delta=z\,d/dz=-\tfrac15\psi\,d/d\psi$。$V_\psi$ 在 $\psi^5\neq-5^5$ 时光滑，即 $z\notin\{0,-\tfrac1{3125},\infty\}$（$5^5=3125$）。

**Hodge 数（可直接算出）.** $V_\psi$ 作为 $\mathbb P^4$ 中的五次三维簇有 $h^{1,1}=1$、$h^{2,1}=101$、$b_3=204$；本书真正用的是其 $G$-不变部分 $H^3(V_\psi)^G$（即镜像族 $V_\psi/G$ 的 $H^3$）：$h^{3,0}=h^{2,1}=h^{1,2}=h^{0,3}=1$，故 $b_3(H^3(V_\psi)^G)=4$，且 $\dim F^p=\sum_{a\ge p}h^{a,3-a}=4-p$：
$$\dim F^3=1,\quad\dim F^2=2,\quad\dim F^1=3,\quad\dim F^0=4.$$
基（留数形式，PDF p.110–111）：$\omega_j=(-1)^{j-1}\psi^j(x_1x_2x_3x_4x_5)^{j-1}\Omega_0/F_\psi^j$（$j=1,2,3,4$），其中 $\Omega_0=\sum_{j=1}^5(-1)^{j-1}x_j\,dx_0\wedge\cdots\widehat{dx_j}\cdots\wedge dx_4$；则 $\operatorname{Res}(\omega_j)\in F^{4-j}H^3(V_\psi)$，且 $\{\omega_1,\dots,\omega_4\}$ 是 $H^3$ 的基。

**Gauss–Manin 联络（显式）.** 书中的计算（PDF p.111，式 `eq:quintic-basis-derivative`）给出
$$\delta\omega_j=-\tfrac j5(\omega_j+\omega_{j+1}),\qquad\omega_5:=0,$$
即 $\delta\omega_1=-\tfrac15(\omega_1+\omega_2)$、$\delta\omega_2=-\tfrac25(\omega_2+\omega_3)$、$\delta\omega_3=-\tfrac35(\omega_3+\omega_4)$、$\delta\omega_4=-\tfrac45\omega_4$。以 $(\omega_1,\omega_2,\omega_3,\omega_4)$ 为基，$\delta$ 方向的联络矩阵（$i$ 行 = $\delta\omega_i$ 的系数）为
$$M=-\frac15\begin{pmatrix}1&1&0&0\\0&2&2&0\\0&0&3&3\\0&0&0&4\end{pmatrix},$$
对角元具体为 $-0.2,-0.4,-0.6,-0.8$。

**横截性逐列验证.** $\omega_j\in F^{4-j}$。$\delta\omega_1$ 的 $\omega_2$ 项系数 $-\tfrac15\neq0$，故 $\delta\omega_1\in F^2\setminus F^3$；$\delta\omega_2\in F^1\setminus F^2$；$\delta\omega_3\in F^0$（$=H^3$）；$\delta\omega_4\in F^0$。每列恰好降一阶：$\nabla(F^p)\subset F^{p-1}\otimes\Omega^1$ 成立（此处 $\Omega^1_S$ 由 $dz$ 生成）。

**从 VHS 读出 PF 方程.** 由 $M$ 逐次迭代得（PDF p.111–112）
$$\delta^4\omega_1=\frac{5z}{1+5^5z}\bigl(\omega_1+15\omega_2+50\omega_3+60\omega_4\bigr),$$
消元得四阶 Picard–Fuchs 方程（式 (5.12)，PDF p.104）：
$$\theta^4y+\frac{6250z}{1+3125z}\theta^3y+\frac{4375z}{1+3125z}\theta^2y+\frac{1250z}{1+3125z}\theta y+\frac{120z}{1+3125z}y=0,\qquad\theta=\delta,$$
其中 $6250=2\cdot5^5$、$4375=7\cdot5^4$、$1250=2\cdot5^4$、$120=24\cdot5$。$z=0$ 处指标方程 $\lambda^4=0$，故 $z=0$ 为**最大幺幂点**；全纯周期
$$y_0(z)=\sum_{n\ge0}\frac{(5n)!}{(n!)^5}(-1)^nz^n=1-120z+113400z^2-\cdots$$
（$113400=10!/(2!)^5$）是 $z=0$ 处唯一的全纯周期。

**单值性（具体矩阵）.** 在 $z=0$ 附近以 $(y_0,y_1,y_2,y_3)$（对应 $\log z$ 幂次 $0,1,2,3$ 的 PF 解基）表示周期向量，解析延拓 $z\mapsto e^{2\pi i}z$ 的矩阵为
$$T=\begin{pmatrix}1&2\pi i&\frac{(2\pi i)^2}{2}&\frac{(2\pi i)^3}{6}\\0&1&2\pi i&\frac{(2\pi i)^2}{2}\\0&0&1&2\pi i\\0&0&0&1\end{pmatrix},$$
故 $T$ 幺幂；$\log T$ 幂零，且 $(\log T)^3\neq0$、$(\log T)^4=0$（$b_3=4$：MUM 的幂零指数为 4）。另一奇点 $z=-5^{-5}=-1/3125\approx-3.2\times10^{-4}$ 处为 conifold：$(\log T)^2=0$、$\log T\neq0$；$z=\infty$ 处指标根为 $\{1/5,2/5,3/5,4/5\}$，故 $T_\infty$ 的特征值为 5 次单位根，$T_\infty^5$ 幺幂（单值性定理中取 $m=5$ 可实现，PDF p.98）。

**极化数字.** $n=k=3$，故 $Q(\alpha,\beta)=(-1)^3\int_{V_\psi}\alpha\wedge\beta=-\int_{V_\psi}\alpha\wedge\beta$；$k=3$ 为奇数，故 $Q$ 在实 $H^3$ 上是**交错**型且非退化（$b_3=4$）。按 Hodge 分解的定号计数为 $(h^{3,0}+h^{2,1},\,h^{1,2}+h^{0,3})=(2,2)$；具体号向由式 (5.1) 中 $Q(i^{p-q}\alpha,\bar\alpha)>0$ 与 $(-1)^{k(k-1)/2}$ 的配合决定（符号约定待核，§11 C11）。

**结论.** $(H^3,\nabla^{\mathrm{GM}},H^3_{\mathbb Z},F^\bullet)$ 在 $z\neq0,-\tfrac1{3125},\infty$ 上满足 (A1)–(A5)，是权 3 的极化 VHS；$z=0$ 处单值性最大幺幂，$z=-1/3125$ 处为 conifold 点。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | 平坦联络唯一：局部系统 $H$ 上存在唯一平坦联络 $\nabla$，且 $\nabla(s\otimes f)=s\otimes df$ | PDF p.97 | 平坦截面 = 局部系统截面；「相对化」的全部内容 |
| 2 | Griffiths 横截性：$\nabla(F^p)\subset F^{p-1}\otimes\Omega^1_S$ | PDF p.97 | 与「Hodge 结构的族」的唯一区别；五次族联络矩阵上三角（§4） |
| 3 | 只全纯于滤过：$H^{p,q}$ 不随族全纯变化，$F^p$ 才是局部自由全纯子丛 | PDF p.96–97 | 故 VHS 可只用 $(H_{\mathbb Z},\nabla,F^\bullet)$ 记录，$H^{p,q}\cong F^p/F^{p+1}$ |
| 4 | 极化：Kähler 类 $\omega$ 给出 $Q$，式 (5.1) 的 Hodge–Riemann 型正性 | PDF p.97；§8.5.4 定理 PDF p.277 | 书内定义不含 $Q$；「极化 VHS」是加强版，A 模型 VHS 由 $S$ 极化 |
| 5 | 单值性拟幺幂：$T_j$ 拟幺幂，$(T_j^m-I)^{n+1}=0$，$m\ge0$ | PDF p.98，[Landman] | 中译 p.98 作 $m>0$，与英文原著 OCR 的 $m\ge0$ 不一致（§11 C5） |
| 6 | 退化结构：正则奇点 + 典范延拓 [Deligne1] + 幂零轨道 [Schmid] ⇒ $F_{\lim}$、$\bar\nabla_{\delta_j}=-\tfrac1{2\pi i}N_j$、权滤过 $W_\bullet$、极限混合 Hodge 结构 | PDF p.98–99，式 (5.3)–(5.4) | 可再推广为混合 Hodge 结构变分（§5.6.3，p.127–128）；通向 MS-12、MS-13 |

## 6. 推导流程（D1…Dn）

D1. 族 → 局部系统与整数格：$\pi$ 光滑紧合 ⇒ $R^k\pi_*\mathbb C$、$R^k\pi_*\mathbb Z$ 局部常值。依据：PDF p.96–97（$H_Z$ 定义为 $R^k\pi_*\mathbb Z\to R^k\pi_*\mathbb C$ 的像）。
D2. 逐纤维 Hodge 分解 → 子空间 $F^p(X)$、$H^{p,q}(X)$ 与 $F^p\oplus\overline{F^{k-p+1}}=H^k$。依据：PDF p.96–97 定义。
D3. 相对化：$F^0=R^k\pi_*\mathbb C\otimes\mathcal O_S$ 局部自由，$F^p$ 拼成局部自由子层。依据：PDF p.97。
D4. 联络：局部常值层上唯一平坦联络 $\nabla$，$\nabla(s\otimes f)=s\otimes df$。依据：PDF p.97。
D5. 横截性：由周期导数公式 (5.2) $\partial_i\int_\gamma\Omega=\int_\gamma\nabla_{\partial_i}\Omega$ 与 $\nabla$ 把 Hodge 阶降一阶，得 $\nabla(F^p)\subset F^{p-1}\otimes\Omega^1$。依据：PDF p.97–98。
D6. 定义：四元组 $(H,\nabla,H_{\mathbb Z},F^\bullet)$ 称 VHS；再加极化 $Q$（式 (5.1)）称极化 VHS。依据：PDF p.97。
D7. 可算出口：取 $\Omega$ 与平坦截面 $g$，周期 $y=\langle g,\Omega\rangle$ 满足 PF 方程；五次族得 §4 的四阶方程 (5.12)。依据：PDF p.97–98、p.104、p.110–112（细算见 MS-06）。
D8. 边界/退化：紧化 $\bar S$、$D$ 正规交叉、典范延拓；单值性定理 [Landman]；幂零轨道定理 [Schmid] ⇒ $F_{\lim}$、(5.3)、(5.4)、极限 MHS，进一步得 MUM 与混合 Hodge 结构变分。依据：PDF p.98–99、p.104–105、p.127–128。
D9. 闭环：A 模型 VHS 的构造（定理 PDF p.277）与数学镜像对（PDF p.281）——第 8 章把镜像对称重述为「极化 VHS 同构」的落点。依据：PDF p.265–281。

## 7. 常见误解与反例（≥2）

**M1（反例）：「VHS 就是逐纤维给出 Hodge 结构的族」。** 在 §4 中固定 $F^3=\mathbb C\omega_1$、$F^1=\operatorname{span}(\omega_1,\omega_2,\omega_3)$、$F^0=H^3$，只把 $F^2$ 改成 $F'^2=\operatorname{span}(\omega_1,\omega_2+\varphi(z)\omega_3)$（$\varphi$ 非零全纯，$|\varphi|$ 小）。逐纤维仍得到权 3 的 Hodge 结构（$F'^2\oplus\overline{F'^2}=H^3$ 对小 $\varphi$ 成立）。但
$$\delta(\omega_2+\varphi\omega_3)=-\tfrac25(\omega_2+\omega_3)-\tfrac35\varphi(\omega_3+\omega_4)+z\varphi'\omega_3$$
含 $\omega_4$ 项，系数 $-\tfrac35\varphi\neq0$，而 $F'^1=F^1$ 不含 $\omega_4$，故横截性 (A4) 失败。可见「纤维 Hodge 结构 + 全纯滤过」不够，联络与横截性才是变分的实质。依据：PDF p.96–97 与 (A4)。

**M2（反例）：「$\nabla$ 保持 Hodge 滤过，即 $\nabla(F^p)\subset F^p$」。** 五次族里 $\delta\omega_1=-\tfrac15(\omega_1+\omega_2)\notin F^3=\mathbb C\omega_1$。若 $\nabla$ 保持 $F^3$，则周期 $y_0=\langle g_0,\Omega\rangle$ 的全纯性会迫使 PF 方程在 $z=0$ 的局部解全为单值，但 §4 的 $T$ 矩阵上三角非对角元 $2\pi i\neq0$ 正说明存在 $\log z$ 项。依据：PDF p.111 的 $\delta\omega_j$ 公式。

**M3（误解）：「单值性定理说 $T$ 幂零，或每个退化纤维处都有 $T=I+N$」。** 定理只说 $T$ 拟幺幂（特征值为单位根），幂零的是 $\log T$；$z=\infty$ 处指标根 $\{1/5,2/5,3/5,4/5\}$ 使 $T_\infty$ 的特征值为 5 次单位根而非 1，$T_\infty$ 本身不幺幂（$T_\infty^5$ 才幺幂）；只有 MUM 点（如 $z=0$）才有 $T=I+N$ 且 $(\log T)^3\neq0$、$(\log T)^4=0$。依据：PDF p.98 [Landman]、p.111–112、p.104–105。

**M4（误解）：「极化是 VHS 定义的一部分」。** 书 p.97 的定义句只列 $(H,\nabla,H_{\mathbb Z},F^\bullet)$；$Q$ 只在 Kähler 情形由式 (5.1) 额外得到，§8.5.4 定理（PDF p.277）特意写「由 $S$ 极化」，说明极化是附加数据；在 A 模型侧 $S$ 需要构造，不是自动存在的。依据：PDF p.97、p.277。

**M5（误解）：「VHS 只对 Calabi–Yau 的 $H^3$ 有意义」。** 书 p.96–97 对任意 $n$、任意权 $k$ 定义 VHS；只在 §5.4–5.6 与第 8 章才特化到 CY3 的 $H^3$。SY01-24 只写 CY3 的 $H^3$，是适用范围上的差异（§8 冲突 C2）。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz（本书） | PDF p.96–99（§5.1.1–5.1.4）；p.104–105（§5.2.2）；p.127–128（§5.6.3）；p.265–281（§8.5–8.6.1） | 定义 $(H,\nabla,H_{\mathbb Z},F^\bullet)$ 与横截性；退化/极限 MHS；MUM；A 模型 VHS（定理 p.277）与数学镜像对（p.281） |
| SY01-24（Siebert 讲义） | 术语表 #17 Gauss–Manin 联络、#18 单值变换；第 1 章式 (1.68)–(1.69)、(1.95)–(1.97)；正文「它与 Hodge 结构变动的定义有关」 | 与本书 §5.1.1 对应的教学版。**冲突 C1**：用「Hodge 结构变动」，本书 p.97 用「Hodge 结构变分」；**冲突 C2**：只对 CY3 的 $H^3$ 定义 $F^0\supset\cdots\supset F^3$（式 1.95–1.97），本书对任意 $n$、任意权 $k$ 定义；术语表无「Hodge 结构变分」条目（缺口）；式 (1.76) 为 $[\theta^4-5z(5\theta+1)(5\theta+2)(5\theta+3)(5\theta+4)]\varphi=0$、$z=(1/(5\psi))^5$，在 $z_{\rm SY}=-z_{\rm 本书}$ 下与本书式 (5.12) 逐项一致（已展开核对；差异为 $\psi$ 归一化/符号，非冲突，§11 C4） |
| SY01-25 资料卡 | 04-术语文献勘误.md §二「极大退化 / 模空间」组（[De]「Hodge 结构在无穷远处的局部行为」、[LTY]「极大单值」）；§一 25 条核心术语 | 与本书 §5.1.4 的极限 MHS 呼应；无 VHS/Hodge 滤过/Gauss–Manin 联络定义（缺口）。**冲突 C3**：术语「极大单值」vs 本书「最大幺幂单值性」（PDF p.101–105）与「最大幺幂边界点」（p.128），是否同指待核（主归 MS-12） |
| Griffiths 1969 | Ann. of Math. 90 (1969), 460–495、498–541（[Griffiths1]） | 周期映射与 Hodge 滤过的解析性；本书 p.96 列为一般参考文献，§5.3 Griffiths–Dwork 建立其上（A 级） |
| Schmid 1973 | Invent. Math. 22 (1973), 211–319（[Schmid]） | 幂零轨道定理：$F^p$ 延拓与 $F_{\lim}$；本书 p.99 引用（A 级） |
| Deligne 1970 | LNM 163（[Deligne1]） | 正则奇点方程/典范延拓；本书 p.98 用它延拓 $F^0$（A 级） |
| Landman 1973 | Trans. Amer. Math. Soc. 181 (1973), 89–126（[Landman]） | Picard–Lefschetz 变换的拟幺幂性（单值性定理）；本书 p.98（A 级） |
| Cattani–Kaplan 1989；Cattani–Kaplan–Schmid 1986 | Astérisque 179–180 (1989), 67–96；Ann. of Math. 123 (1986), 457–535（[CaK]、[CKS1]） | §8.5.4 定理证明引用：幂零轨道（[CaK] 定理 (2.8)）、[CKS1] 命题 (4.66)、[CaK] p.74 典范延拓（A 级） |

## 9. 前置与后继

- 前置：**MS-10**（必须先读：本卡定义里的 $F^p$、$H^{p,q}$ 与极化式 (5.1) 都在 MS-10 建立）；层论与 Hodge 理论基础（$R^k\pi_*$、局部系统、平坦联络、$\Omega^1_S$，本卡直接使用）。
- 后继：**MS-12**（单值性与最大幺幂单值性，§5.1.5–5.2：$N_j$、$W_\bullet$、MUM 定义）；**MS-13**（极限混合 Hodge 结构，§5.1.3–5.1.4：$F_{\lim}$、$(W_\bullet,F_{\lim})$）；**MS-06**（Picard–Fuchs 方程，本卡的计算出口，§5.1.2、§5.3–5.4）；**MS-18**（Frobenius 流形与 Dubrovin 联络，§8.4–8.5）。本卡是上述概念的定义域与语言。
- 分工备忘：MS-10 讲单个 Hodge 结构，本卡讲相对版本/变分；MS-10 §3.6 已收录 VHS 定义，两卡 §3 的重叠与主卡归属待 lead 裁定（§11 C7）。

## 10. 形式化接口（Lean 可 sorry）

```lean
-- MS-11 接口骨架：只固定类型形状与约束，证明全部留 sorry
universe u

/-- 权 k 的 Hodge 结构（滤过 + Hodge 分解公理） -/
structure WeightHodgeStructure (H : Type u) [AddCommGroup H] [Module ℂ H] (k : ℤ) where
  F : ℤ → Submodule ℂ H
  hodge : ℤ → ℤ → ℕ
  hodge_spec : ∀ p q, p + q = k → hodge p q = Module.finrank ℂ (F p ⧸ F (p + 1))
  conjugate_decomp : ∀ p, F p ⊔ F (k - p + 1) = ⊤
  strict : ∀ p, k < p → F p = ⊥

/-- Hodge 结构变分 (H, ∇, H_Z, F^•)：书 p.97 定义的形状 -/
structure VariationOfHodgeStructure (S : Type u) where
  k : ℤ
  H : Type u                    -- 局部系统 R^k π_* ℂ 的截面
  HZ : Type u                   -- 整数格 R^k π_* ℤ
  nabla : H → (S → ℂ) → H      -- 平坦 Gauss–Manin 联络
  flat : Prop                   -- ∇² = 0（sorry）
  F : ℤ → Set H                 -- Hodge 滤过（子丛）
  decreasing : ∀ p, F (p + 1) ⊆ F p
  transversality : Prop         -- ∇(F^p) ⊆ F^{p-1} ⊗ Ω¹_S（sorry）
  fiber : ∀ s : S, WeightHodgeStructure H k
  integral : HZ → H
  polarization : Option (H → H → ℂ)  -- 定义（p.97）不含 Q；极化 VHS 另加

/-- 关键假设：横截性不可省；去掉它只剩「Hodge 结构的族」（反例见 §7 M1） -/
theorem transversality_essential : True := by sorry

/-- §4 的计算：五次族在 (ω₁,…,ω₄) 基下的 GM 联络矩阵上三角 -/
theorem quintic_connection_upper_triangular : True := by sorry
```

## 11. 待核清单

- [ ] **C1（冲突·术语）**：SY01-24 用「Hodge 结构变动」，本书 p.97 用「Hodge 结构变分」；不判定谁对，待 lead 裁定（MS-10 §11 已登记，建议 _冲突表编号 T7，涉及 MS-11，不重复编号）。
- [ ] **C2（冲突·适用范围）**：SY01-24 只对 CY3 的 $H^3$ 定义 $F^0\supset\cdots\supset F^3$（式 (1.95)–(1.97)）；本书 p.97 对任意 $n$、任意权 $k$ 定义。是否只是特例、术语表是否需注明适用域，待核。
- [ ] **C3（冲突·术语，主归 MS-12）**：SY01-25 §二 [LTY] 条用「极大单值」，本书 p.101–105 用「最大幺幂单值性」（p.128 另有「最大幺幂边界点」）；是否同指待核（_冲突表 U2 已记「单值性的作用对象」之别）。
- [ ] C4（非冲突·参数约定）：SY01-24 式 (1.76) 与本书式 (5.12) 在代换 $z_{\rm SY}=-z_{\rm 本书}$ 下逐项相同（已把 $(5\theta+1)(5\theta+2)(5\theta+3)(5\theta+4)=625\theta^4+1250\theta^3+875\theta^2+250\theta+24$ 展开核对）；故差异来自两书对 $\psi$ 的归一化与 $z$ 的符号（SY01-24 取 $z=(1/(5\psi))^5$，本书取 $z=\psi^{-5}$），不是方程内容矛盾。两书族方程写法（$\sum x_i^5+\psi\prod x_i$ 还是 $\sum x_i^5-5\psi\prod x_i$）待核原文，不判定谁对。
- [ ] C5（非冲突）：单值性定理 $m\ge0$（英文原著 OCR p.098）vs 中译 p.98「$m>0$」；本卡按 $m\ge0$ 引用，译误候选（MS-13 已记）。
- [ ] C6（非冲突）：[Morrison7] 用于 A 模型 VHS 命名（p.278），references.tex 条目卷期页待补。
- [ ] C7（非冲突·协调）：MS-10 §3.6 已收录 VHS 定义；本卡与 MS-10 的 §3 重叠，主卡归属与引用方式待 lead 裁定。
- [ ] C8（非冲突）：书 p.97 只写「光滑态射」，本卡按「连通光滑拟射影底空间 + 光滑紧合族」写；连通性与紧合性是否为原文假设待核。
- [ ] C9（非冲突）：§5.6.3 命题 `prop:normalized-yukawa-pf` 假定 §5.2.2 的整性猜想；A 模型 VHS（§8.5.4）与该猜想的关系待核（转 MS-18/MS-12）。
- [ ] C10（非冲突）：§4 中 $T$ 矩阵所取 PF 解基 $(y_0,\dots,y_3)$ 与书 p.44、p.111 所用周期基可能差一个整基变换（$\log T$ 的幂零指数不变），具体矩阵待核。
- [ ] C11（非冲突·符号约定）：§3 (A6) 与 §4 中 $Q$ 的系数 $(-1)^{k(k-1)/2}$ 与式 (5.1) 正性 $Q(i^{p-q}\alpha,\bar\alpha)>0$ 的符号配合（$k=3$ 时 $Q=-\int\alpha\wedge\beta$）需对照书 p.97 原文核实；本卡照书引用。
- 非空则 status ≠ frozen。
- **核验（2026-11-20）**：本卡经 `_核验记录.md` 核验，修正 2 处（详见该文件 ✗ 清单与证据链接）；其余待核条目保留。
