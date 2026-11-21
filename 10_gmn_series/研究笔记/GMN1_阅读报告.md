# GMN1 阅读报告：这篇论文是怎么证明穿墙公式的

> 写给**没有读过原文**的下游 agent。目标：读完这一份，你能（a）复述全文的论证骨架；（b）知道每一步的输入与输出、哪一步是硬的、哪一步是软的；（c）在写 GMN2/3、GMW 时知道该从哪里接、该引哪个式子。
> 配套：`资料卡/00-速览.md`（一页版）、`02-论证地图.md`（D1–D10）、`03-条款索引.md`（式号→页码）。本报告是**深版**，三者不重复。
> 版本：2026-11-21，基于译本 v1.0（`成品/GMN1_四维穿墙_v1.0.pdf`，65 页）。式号与原文一致。

---

## 0. 先用三句话定位

1. **素材**：$d=4$、$\mathcal{N}=2$ 的超对称规范理论，放在 $\mathbb{R}^3\times S^1$ 上（半径 $R$）。
2. **观察**：低能有效理论是靶空间为库仑分支 $\mathcal{M}$ 的三维 sigma 模型；BPS 粒子绕 $S^1$ 缠绕，成为这个三维理论里的「瞬子」；瞬子按 $e^{-2\pi R|Z_\gamma|}$ 压低，所以**大 $R$ 展开就是瞬子展开**，其系数正是 BPS 简并度 $\Omega(\gamma;u)$。
3. **要害**：物理上度量的量子修正必须**光滑**，而 $\Omega(\gamma;u)$ 在边缘稳定墙上**跳变**。两者相容的唯一方式，是「单个 BPS 粒子的贡献跳变」被「多粒子（多瞬子）贡献的跳变」精确抵消——而这个抵消条件**逐字就是 Kontsevich–Soibelman 穿墙公式**。

所以本文不是"证明一个已知公式"那么简单，而是：**给 KS 公式一个物理来源，再用它反推出公式必须成立。**

---

## 1. 问题从哪来（§1–§2 的动机，必须理解的四件事）

### 1.1 指标 $\Omega$ 是分段常值，而且会跳

第二螺旋度超迹
$$\Omega(\gamma;u) := -\tfrac12\,\mathrm{Tr}_{\mathcal{H}_{\gamma,\mathrm{BPS}}}(-1)^{2J_3}(2J_3)^2 \tag{1.1}$$
对超多重态（hypermultiplet）取值 $+1$，对矢量多重态取 $-2$。它在 $\mathcal{M}$ 上**分段常值**，只有穿过**边缘稳定墙**（wall of marginal stability，实余维 1，其上 $Z_\gamma,Z_{\gamma'}$ 同相位）时才跳。这是「墙」这个词的全部含义：墙不是空间的墙，是**参数空间里使某个 BPS 态变成边缘稳定的轨迹**。

### 1.2 KS 公式在说什么

对每条射线 $\ell\subset\mathbb{C}^\times$，把中心荷相位落在 $\ell$ 上的电荷收集起来，按 $\arg Z_\gamma$ 的次序做乘积
$$\prod_{\gamma\in\Gamma_u\cap\ell} \mathcal{K}_\gamma^{\Omega(\gamma;u)}, \qquad \mathcal{K}_\gamma:\ X_{\gamma'}\mapsto X_{\gamma'}\bigl(1-\sigma(\gamma)X_\gamma\bigr)^{\langle\gamma',\gamma\rangle} \tag{2.16}$$
（$\sigma$ 是二次加细，见 §1.5）。当 $u$ 穿过墙时，$\Omega$ 跳变，但**每个凸扇形内所有 BPS 射线的总乘积不变**——这就是穿墙公式 (2.18)。等价说法：$\Omega$ 的跳变必须使乘积在墙两侧相等。

> 注意 $\mathcal{K}_\gamma$ 不是线性映射，是**辛同胚**（保持辛形式 $\varpi^T$ 的自同构）。这是后面整个构造的"骨架"：跳变是辛同胚，所以由它拼出来的辛形式才可能是解析的。

### 1.3 4d→3d 给了什么

$\mathbb{R}^3\times S^1$ 上的低能理论（§2.3）以 $\mathcal{M}$ 为靶空间，$\mathcal{M}$ 本身是库仑分支 $\mathcal{B}$ 上的**复环面丛**（纤维 $\mathcal{M}_u$，坐标 $\theta_{\mathrm{elec}},\theta_{\mathrm{magn}}$，周期 $2\pi$）。$R\to\infty$ 时度量的首项是**半平坦度量**
$$g^{\mathrm{sf}} = R\,(\mathrm{Im}\,\tau)_{IJ}\,da^I d\bar a^J + \frac{1}{4\pi^2R}\bigl((\mathrm{Im}\,\tau)^{-1}\bigr)^{IJ}dz_I d\bar z_J, \qquad dz_I = d\theta_{\mathrm{magn},I}-\tau_{IJ}d\theta_{\mathrm{elec}}^J \tag{2.35}$$
它在纤维上是平坦的，体积 $\mathrm{vol}(\mathcal{M}_u) = R^{-r}$，并且关于某个复结构 $J^{\mathrm{sf}}_3$ 是凯勒的——那个复结构正是 **Seiberg–Witten 环面纤维化**的复结构。

### 1.4 矛盾就在这里

$g^{\mathrm{sf}}$ 是"把瞬子全关掉"的结果。打开瞬子：每个 BPS 态贡献一项，权重是 $\Omega(\gamma;u)$。但 $\Omega$ 会跳！那 $g$ 岂不是也要跳？而 $g$ 是三维规范理论的低能度量，**物理上必须光滑**（低能有效作用量在模空间上光滑，这是 Wilsonian 有效理论的基本要求）。

**整个第一节都在铺这个矛盾，第二节开始解答：多瞬子。**

---

## 2. 工具：怎么用全纯数据造一个超凯勒度量（§3）

这一段是纯几何，与场论无关；它是全文的"机器"。**没读懂 §3，后面全是黑箱。**

### 2.1 超凯勒 $\Rightarrow$ 一整个 $\mathbb{CP}^1$ 的复结构

超凯勒流形 $(\mathcal{M},g)$ 有三个复结构 $J_1J_2=J_3$（轮换）。对任意单位向量 $a^\alpha$，$a^\alpha J_\alpha$ 仍是复结构，于是有 $S^2\cong\mathbb{CP}^1$ 的复结构族。用复参数 $\zeta$ 参数化：
$$J^{(\zeta)} = \frac{i(-\zeta+\bar\zeta)J_1-(\zeta+\bar\zeta)J_2+(1-|\zeta|^2)J_3}{1+|\zeta|^2} \tag{3.2}$$
以及全纯辛形式
$$\varpi(\zeta) = -\frac{i}{2\zeta}\omega_+ + \omega_3 - \frac{i}{2}\zeta\,\omega_-, \qquad \omega_\pm = \omega_1\pm i\omega_2. \tag{3.4}$$
**为什么是这三个系数**：$\varpi(\zeta)$ 对每个固定 $\zeta$ 都是 $J^{(\zeta)}$-全纯的辛形式，并且对 $\zeta$ 只有 $\zeta^{-1},1,\zeta$ 三阶（这是超凯勒的"三复结构"信息的精确编码）。$\varpi(\zeta)$ 被 $\mathcal{O}(2)$ 扭转（要理解 $\zeta=0,\infty$ 处得用 $\zeta$ 或 $1/\zeta$ 重标度）。

> **反过来用它**：如果你能从别的途径造出一个 $\varpi(\zeta)$ 满足「逐点非退化 + 在 $\zeta=0,\infty$ 只有单极点 + 实性 $\varpi(-1/\bar\zeta)=\overline{\varpi(\zeta)}$」，再由 $\varpi^{r+1}=0$ 提取 $\omega_3$，就得到一个超凯勒度量。§3.3 用它重造了 $g^{\mathrm{sf}}$，§5 用它造精确的 $g$。

### 2.2 扭量构造：全纯坐标 $X_\gamma$ 是"母对象"

§3.2 假设给了一族 $\mathbb{C}^\times$-值函数 $X_\gamma(u,\theta;\zeta)$（$\gamma\in\Gamma$），性质五条：

1. **乘性** $X_\gamma X_{\gamma'} = X_{\gamma+\gamma'}$；
2. **实性** $X_\gamma(\zeta) = \overline{X_{-\gamma}(-1/\bar\zeta)}$；
3. **CR 方程**：$X$ 是下面这组方程的解
$$\frac{\partial X}{\partial u^i} = \Bigl(\tfrac1\zeta A^{(-1)}_{u^i}+A^{(0)}_{u^i}\Bigr)X,\qquad \frac{\partial X}{\partial \bar u^{\bar i}} = \Bigl(A^{(0)}_{\bar u^{\bar i}}+\zeta A^{(1)}_{\bar u^{\bar i}}\Bigr)X \tag{3.5}$$
其中 $A^{(n)}$ 是沿纤维的复竖直向量场，$A^{(-1)}$ 与 $A^{(1)}$ 逐点线性无关；
4. **关于 $\zeta$ 分段全纯**（在可数条直线之外全纯）；
5. 由 $X$ 组装的
$$\varpi(\zeta) := \frac{1}{8\pi^2R}\epsilon_{ij}\frac{dX_{\gamma^i}}{X_{\gamma^i}}\wedge\frac{dX_{\gamma^j}}{X_{\gamma^j}} \tag{3.6}$$
整体定义、关于 $\zeta$ 全纯、非退化、在 $\zeta=0,\infty$ 只有单极点。

于是在 $\mathcal{Z}=\mathcal{M}\times\mathbb{CP}^1$ 上得到：复结构（由 CR 方程定义 $T^{0,1}$，可积性由 $X_\gamma$ 的存在保证）、到 $\mathbb{CP}^1$ 的全纯纤维化、纤维上的辛形式 $\varpi(\zeta)$、法丛 $\mathcal{O}(1)^{\oplus 2r}$ 的截面族、覆盖对径映射的反全纯对合 $\sigma(x,\zeta)=(x,-1/\bar\zeta)$。**这五条正是扭量空间的特征性质**（Hitchin 的定理），于是按标准配方重构出 $\mathcal{M}$ 上的超凯勒度量：由 $\varpi^{r+1}=0$ 得 $\omega_+^r\wedge\omega_3=0$，故 $\omega_3$ 是 $(1,1)$ 型，配 $J_3$ 就是凯勒度量。

> **这里的逻辑关系要记牢**：$X_\gamma$ 是"源"，$\varpi$ 是"$X$ 的二次组合"，$g$ 是"$\varpi$ 的三复结构分解"。所以**全文只需造 $X_\gamma$**。

### 2.3 半平坦情形：显式解（全文的"零阶项"）

$$X^{\mathrm{sf}}_\gamma(\zeta) := \exp\Bigl[\pi R\zeta^{-1}Z_\gamma + i\theta_\gamma + \pi R\zeta\bar Z_\gamma\Bigr] \tag{3.10}$$
代入 §2.2 的框架，得 $\omega_+^{\mathrm{sf}} = -\frac{1}{2\pi}\langle dZ,d\theta\rangle = \frac{1}{2\pi}da^I\wedge dz_I$，$\omega_3^{\mathrm{sf}}$ 正好给出 (2.35)。**这就是"瞬子为零"的基准解**，也是 §5 里 RH 问题的边界条件。

> 一个容易被忽略的点（译注 3 专门讲了）：$\varpi(\zeta)$ 在原文里出现两次"定义"——(3.4) 是从超凯勒结构给的，(3.6) 是从 $X$ 组装的。整个构造的成败就在于：**由 (3.6) 算出的 $\varpi$ 恰好满足 (3.4) 的形式**。§5.4 验证的正是这件事。

---

## 3. 先做最简单的情形：$U(1)$ + 单个超多重态（§4）

这一段是"可以手算的实验室"，全文所有猜想的形状都从这里读出来。

- 没有磁荷 BPS 态 ⇒ 沿 $\theta_{\mathrm{magn}}$ 的平移是精确等距 ⇒ 度量是 **Gibbons–Hawking 型**
  $$g = V^{-1}\Bigl(\frac{d\theta_{\mathrm{magn}}}{2\pi}+A\Bigr)^2 + V\,d\vec x^2,\qquad a = x^1+ix^2,\ \theta_{\mathrm{elec}}=2\pi R x^3,\ F=\star dV $$
- $V$ 由一圈图（Kaluza–Klein 动量求和）给出，Poisson 重求和后 $V=V^{\mathrm{sf}}+V^{\mathrm{inst}}$，其中
  $$V^{\mathrm{inst}} = \frac{q^2R}{2\pi}\sum_{n\ne0}e^{inq\theta_{\mathrm{elec}}}K_0(2\pi R|nqa|), \qquad A^{\mathrm{inst}} = -\frac{q^2R}{4\pi}\Bigl(\frac{da}{a}-\frac{d\bar a}{\bar a}\Bigr)\sum_{n\ne0}(\mathrm{sgn}\,n)e^{inq\theta_{\mathrm{elec}}}|a|K_1(2\pi R|nqa|)$$
  $K_0,K_1$ 是修正贝塞尔函数，$x\to\infty$ 时 $\sim e^{-x}$——**这就是"单瞬子修正指数压低"的第一次显形**，也是 §5.6 首阶修正 (5.16) 的模板。
- 奇点结构变了：$g^{\mathrm{sf}}$ 在 $a=0$ 有一个奇点；$g$ 把它换成 $q$ 个 $A_{q-1}$ 型锥奇点，$q=1$ 时完全光滑化。**"瞬子修正改善奇性"**是重复出现的母题。
- 单值性（§4.1 末尾）：绕 $a=0$ 一周，$\theta_{\mathrm{magn}}\to\theta_{\mathrm{magn}}+q^2\theta_{\mathrm{elec}}-q\pi$。那个 $-q\pi$ 就是**二次加细必须存在**的直接证据（Wilson 线只有在选定 $\sigma$ 后才良定义）。
- $\mathcal{X}_{\mathrm{magn}}$ 的精确解 (4.33) 是一条**积分方程**（沿两条 BPS 射线 $\ell_\pm$ 的 Cauchy 型积分）。**它就是 §5 一般积分方程 (5.13) 的原型**——对照着看，一般情形只是把"一条射线、一个电荷"换成"可数多条射线、全格点电荷"。

---

## 4. 一般情形：黎曼–希尔伯特问题（§5.1）——全文的心脏

### 4.1 五个要素

要造 $X:\mathcal{M}\to T$（$T$ 是复化辛环面，$X_\gamma$ 是 $T$ 上的坐标函数），先规定：

**(a) 渐近**：定义 $\Upsilon := X\,(X^{\mathrm{sf}})^{-1}$（注意原文的复合约定 $fg = g\circ f$，所有公式都按这个约定写），要求
$$\lim_{\zeta\to0}\Upsilon=\Upsilon_0,\qquad \lim_{\zeta\to\infty}\Upsilon=\Upsilon_\infty,\qquad \Upsilon_0=\overline{\Upsilon_\infty}. \tag{5.3}$$

**(b) 跳变**：对每条过原点的射线 $\ell$，令 $(\Gamma_u)_\ell:=\{\gamma: Z_\gamma(u)/\zeta\in\mathbb{R}_-,\ \zeta\in\ell\}$，
$$X^+ = X^- S_\ell,\qquad S_\ell := \prod_{\gamma\in(\Gamma_u)_\ell}\mathcal{K}_\gamma^{\Omega(\gamma;u)} \tag{5.7}$$
（$X^\pm$ 是沿顺/逆时针趋近 $\ell$ 的极限）。$u$ 不在墙上时 $(\Gamma_u)_\ell$ 至多一维，诸 $\mathcal{K}_\gamma$ 对易，无需指定次序。**"BPS 射线"就是 $(\Gamma_u)_\ell\ne\emptyset$ 的那些 $\ell$。**

**(c) 实性**：由 $\Omega(\gamma)=\Omega(-\gamma)$ 知若 $X$ 是解，则 $\bar X_\gamma(\zeta):=\overline{X_{-\gamma}(-1/\bar\zeta)}$ 也是解；断言 $\bar X=X$。证明只用刘维尔定理：$Y:=\bar X X^{-1}$ 无跳变故解析，两端均 $\to1$ 故 $Y=1$。

**(d) 不唯一性**：解只定到 $X\to bX$（$b$ 是 $\mathcal{M}_u$ 的微分同胚）。**这一点很重要**：它说明 RH 问题本身不编码度量，只编码"复结构 + 辛形式"的等价类；固定 $b$ 的规范要靠积分方程（§5.3 的核选择）来做。

**(e) 线性化**：若嫌"映射之间的 RH 问题"不习惯，就换成 $\mathcal{X}^*:C^\infty(T)\to C^\infty(\mathcal{M}_u)$；线性解不一定是某个 $X$ 的拉回，但"保乘法"就能保证，故函子性救场。

> **原型检查**：把 §4 的 $U(1)$ 情形对进来——$\mathcal{K}_{(0,\pm q)}$ 就是 $S_{\pm\ell}$，跳变条件 (5.7) 退化成 (4.52) 里"$\mathcal{X}_{\mathrm{elec}}$ 连续、$\mathcal{X}_{\mathrm{magn}}$ 跳变"。

### 4.2 §5.2：为什么 KS 公式 = 度量的连续性（**全文唯一不可替代的一步**）

这是本文最重要的一小节，逻辑只有五行，但必须精确复述：

1. 假设对远离墙的固定 $u$，RH 问题有解 $X$；它关于 $\zeta$ 的行为被 (5.7) 完全钉死（分段全纯 + 跳变）。
2. 问它**关于 $u$** 的行为：$u$ 依赖只来自两处——渐近条件 (5.3)（连续）和跳变处方 (5.7)（远离墙时连续）。
3. 穿墙时：设 $u_w$ 是墙上一一般点，$u\to u_w$ 时电荷 $\gamma=n\gamma_1+m\gamma_2$ 的诸 BPS 射线汇聚成一条射线 $\ell$。记跨过整组射线的**总不连续性**为
$$A = \prod^{\ccwarrow}_{\substack{\gamma=n\gamma_1+m\gamma_2\\ m>0,\,n>0}}\mathcal{K}_\gamma^{\Omega(\gamma;u)} \tag{5.10}$$
（逆时针次序，因为原文的复合约定是非标准的；§2.2 的 KS 乘积是顺时针，差别仅此。）
4. 从墙两侧取极限 $u\to u_w$：每一侧得到"跨 $\ell$ 跳变为 $A$、其余跳变照旧"的同一个 RH 问题的解。
5. 两侧极限相等 $\iff$ 它们是**同一个 RH 问题**的解 $\iff$ $A$ 在两侧相同 $\iff$ **这正是 KS 穿墙公式**。

**结论**：$\Omega$ 服从 KS 公式 $\Rightarrow$ RH 的解 $X(u,\zeta)$ 关于 $u$ 连续（除 BPS 射线外），而 $\varpi(\zeta)$ 是 $X$ 的二次组合，且 $X$ 的跳变是辛同胚（$\mathcal{K}_\gamma$ 保 $\varpi^T$）$\Rightarrow$ $\varpi(\zeta)$ 关于 $\zeta$ **解析**、关于 $u$ **光滑** $\Rightarrow$ $g$ 光滑。

> 这是全文的"等价性引擎"。请连同它的方向一起记住：**KS 公式 $\Rightarrow$ 连续性**（这里用），而**连续性 $\Rightarrow$ KS 公式**（反面：若 KS 不成立，则两侧 $A$ 不同，$X$ 必在墙上跳，$g$ 必不光滑，与物理矛盾）——后者是"物理解释"，前者才是"构造"。

### 4.3 §5.3：把 RH 问题解出来（存在性 + 大 $R$ 展开）

不能像 §4 那样写显式解（那里所有 $S_\ell$ 对易，这里不对易）。走"Cecotti–Vafa 的无穷维版本"：

- 有限维原型：$tt^*$ 方程里的 RH 问题可以改写成关于 $\Phi(\zeta)$ 的**积分方程**，$R$ 大时 $\Phi=1+\text{小}$，可迭代 $\Rightarrow$ 存在性 + 首阶修正。
- 直接照搬只适用于**线性**问题，所以要先线性化（§5.1(e)），代价是要验证"保乘法"。
- 照搬的边界条件是 $\Upsilon_0=1$，与本文需要的 $\Upsilon_0=\overline{\Upsilon_\infty}$ 不符；**改积分核**即可。

最终写出（这是在 $T_u$ 的阿贝尔群结构上写的，所以每一步都保持"是某个映射的拉回"）：
$$X_\gamma(\zeta) = X^{\mathrm{sf}}_\gamma(\zeta)\exp\Bigl[\tfrac{1}{4\pi i}\sum_\ell\int_\ell\frac{d\zeta'}{\zeta'}\frac{\zeta'+\zeta}{\zeta'-\zeta}\log\frac{X_\gamma(\zeta')}{(XS_\ell)_\gamma(\zeta')}\Bigr]$$
代入 $\mathcal{K}$ 的显式形式 $(XS_\ell)_\gamma = X_\gamma\prod_{\gamma'\in(\Gamma_u)_\ell}(1-\sigma(\gamma')X_{\gamma'})^{\Omega(\gamma';u)\langle\gamma,\gamma'\rangle}$，得**主结果 (5.13)**：
$$X_\gamma(\zeta) = X^{\mathrm{sf}}_\gamma(\zeta)\exp\Bigl[-\frac{1}{4\pi i}\sum_{\gamma'}\Omega(\gamma';u)\langle\gamma,\gamma'\rangle\int_{\ell_{\gamma'}}\frac{d\zeta'}{\zeta'}\frac{\zeta'+\zeta}{\zeta'-\zeta}\log\bigl(1-\sigma(\gamma')X_{\gamma'}(\zeta')\bigr)\Bigr] \tag{5.13}$$

三件事必须记住：

1. **(5.13) 的任何解都自动满足跳变条件与实性条件**（核的选择就是为了这个），所以"解 (5.13)" = "解 RH 问题"。
2. **它就是 TBA 方程**（附录 E）：把 $\log(1-\sigma X)$ 看成"准粒子能量的指数"，核 $\frac{\zeta'+\zeta}{\zeta'-\zeta}$ 看成散射相移。这一点在 GMN2 里会更清楚（WKB + TBA）。
3. **迭代展开 = 瞬子展开**。首阶：
   $$X_\gamma \sim X^{\mathrm{sf}}_\gamma\exp\Bigl[-\frac{1}{4\pi i}\sum_{\gamma'}\Omega(\gamma';u)\langle\gamma,\gamma'\rangle\int_{\ell_{\gamma'}}\frac{d\zeta'}{\zeta'}\frac{\zeta'+\zeta}{\zeta'-\zeta}\log\bigl(1-\sigma(\gamma')X^{\mathrm{sf}}_{\gamma'}(\zeta')\bigr)\Bigr] \tag{5.14}$$
   这就是 §4 里单瞬子修正的线性叠加；高阶项是 $\Omega$ 的多重线性式，带 $R$ 依赖，对应多瞬子。（**这就是 §1.4 那个矛盾的解答**：单粒子项跳，多粒子项也跳，两者抵消。）
4. 存在性与渐近在附录 C（$R\gg1$）。

> **技术细节别丢**：$\Upsilon_0$ 与 $\Upsilon_\infty$ 定了规范；$\sigma$（二次加细）的选择只让 $X$ 变 $(-1)^{\gamma\cdot c(\sigma,\sigma')}X_\gamma(u,\theta+c\pi;\zeta)$，故可去掉（§5.3 末"整体性问题"）。

### 4.4 §5.4–5.6：从 $X$ 到度量

- **辛形式**：$\varpi(\zeta)=\frac{1}{4\pi^2R}\mathcal{X}^*\varpi^T=\frac{1}{8\pi^2R}\epsilon_{ij}\frac{dX_{\gamma^i}}{X_{\gamma^i}}\wedge\frac{dX_{\gamma^j}}{X_{\gamma^j}}$ (5.16)。四条性质：解析（因跳变是辛同胚）、实性、$\zeta=0,\infty$ 单极点且留数 $\mathrm{Res}_{0}\varpi=\frac{i}{8\pi}\Upsilon_0^*\langle dZ,d\theta\rangle$、$R$ 大时非退化。
- **微分方程**（§5.5，本文第二重要的技术块）：因跳变 $S_\ell$ 与参数无关，$\mathcal{A}_\zeta:=\zeta\partial_\zeta X X^{-1}$、$\mathcal{A}_n:=\partial_{t^n}XX^{-1}$ 都**解析**（跳变相消），且在 $\zeta=0,\infty$ 只有单极点（因为 $\Upsilon$ 有限）。于是得到 $\mathbb{CP}^1$ 上的**平坦联络**，有非正则奇点，**斯托克斯因子正是 $S_\ell$**。完整方程组 (5.30)–(5.35)：
  $$\partial_{u^j}X=\Bigl(\tfrac1\zeta\mathcal{A}^{(-1)}_{u^j}+\mathcal{A}^{(0)}_{u^j}\Bigr)X,\quad \partial_{\bar u^{\bar j}}X=\Bigl(\mathcal{A}^{(0)}_{\bar u^{\bar j}}+\zeta\mathcal{A}^{(1)}_{\bar u^{\bar j}}\Bigr)X,$$
  $$\Lambda\partial_\Lambda X=\Bigl(\tfrac1\zeta\mathcal{A}^{(-1)}_\Lambda+\mathcal{A}^{(0)}_\Lambda\Bigr)X,\quad R\partial_R X=\Bigl(\tfrac1\zeta\mathcal{A}^{(-1)}_R+\mathcal{A}^{(0)}_R+\zeta\mathcal{A}^{(1)}_R\Bigr)X,\quad \zeta\partial_\zeta X=\Bigl(\tfrac1\zeta\mathcal{A}^{(-1)}_\zeta+\mathcal{A}^{(0)}_\zeta+\zeta\mathcal{A}^{(1)}_\zeta\Bigr)X.$$
  其数学身份：$\mathbb{CP}^1\times\mathcal{P}$ 上的平坦联络，即 $\mathbb{CP}^1$ 上联络的**等单值形变族**；斯托克斯数据由 KS 因子给出。「凸扇形内总乘积在参数变动下不变」$\Rightarrow$ 再把 $u$ 变动用上 $\Rightarrow$ **重新得到穿墙公式**（这是 §5.2 的另一种讲法，也是 §7 的出发点）。
- **Nahm 形变**：$(\mathcal{A}^{(\pm1)}_\zeta,\mathcal{A}^{(0)}_\zeta,\mathcal{A}^{(0)}_R)$ 的相容性给出 Nahm 方程的一个形变（附录 D）；作者猜测其解对一切 $R$ 正则，并说这也许能反过来限制 BPS 谱。
- **度量**：把 $\log X_\gamma$ 按 $\zeta$ 展开 $=\zeta^{-1}F_{-1}^\gamma+F_0^\gamma+\zeta F_1^\gamma+\cdots$，$F_{-1}=\pi RZ_\gamma$、$F_0=i\theta_\gamma-\frac{1}{4\pi i}\sum_{\gamma'}\Omega\langle\gamma,\gamma'\rangle\int\frac{d\zeta'}{\zeta'}\log(1-\sigma X)$、$F_1=\pi R\bar Z_\gamma-\frac{1}{2\pi i}\sum\cdots\int\frac{d\zeta'}{\zeta'^2}\log(\cdots)$，再代回 $\varpi$ 得 $\omega_+=\frac{i}{2\pi^2R}\epsilon_{ij}dF_{-1}^{\gamma^i}\wedge dF_0^{\gamma^j}$、$\omega_3=\frac{1}{8\pi^2R}\epsilon_{ij}(2dF_1^{\gamma^i}\wedge dF_{-1}^{\gamma^j}+dF_0^{\gamma^i}\wedge dF_0^{\gamma^j})$。**由这两个形式就得到 $g$**（这就是"构造"的终点）。
- **首阶修正**：$\frac{dX_\gamma}{X_\gamma}=\frac{dX^{\mathrm{sf}}_\gamma}{X^{\mathrm{sf}}_\gamma}+\mathcal{I}_\gamma+\cdots$，$\mathcal{I}_\gamma$ 含 $\frac{\sigma X^{\mathrm{sf}}}{1-\sigma X^{\mathrm{sf}}}$ 与贝塞尔型的指数压低；转成 $\varpi$ 的修正即 (5.17)/(5.18)，其中 $V^{\mathrm{inst}},A^{\mathrm{inst}}$ 与 §4 的 (4.7)/(4.10) 同型。**这就是"单瞬子 $\Omega$ 一次方"的那一项。**

### 4.5 §5.7：五条性质与"它就是物理度量"

构造出的 $g$ 满足（**这是 §5 的资格证明**）：

1. **连续**（由 KS 公式，§5.2）；
2. 若所有 BPS 粒子 $|Z|\to\infty$，则 $g\to g^{\mathrm{sf}}$（修正项指数压低）；
3. **光滑**，只有物理预期的奇点例外：在 $\mathcal{B}$ 的奇异轨迹上方（那里某 BPS 粒子变成无质量，$Z_{\gamma_i}=0$ 而 $\Omega\ne0$）；局部标度极限 $R\to\infty$ 而 $RZ_{\gamma_i}$ 有限时，RH 问题只留 $\ell_{\gamma_i}$，退化为 §4 的 $A_{q-1}$ 奇点阵列，与 3d 有效场论预期一致。**超共形点**（非局域粒子同时无质量）作者明说未分析；
4. $\mathrm{vol}(\mathcal{M}_u)=(1/R)^r$——因为 $\omega_\pm$ 在纤维上为零，$\mathrm{vol}=\frac{1}{r!}\int\varpi^r=\frac{1}{(4\pi^2R)^rr!}\int_{\mathcal{X}(\mathcal{M}_u)}(\varpi^T)^r$；
5. 关于 $J_3$，$(\mathcal{M},g)$ 与标准 SW 环面纤维化等同；等同之下 $\omega_+=\frac{1}{2\pi}da^I\wedge dz_I$（因为 $\omega_+=2i\,\mathrm{Res}_{\zeta=0}\varpi$，而渐近条件保证 $\omega_+=\Upsilon_0^*\omega_+^{\mathrm{sf}}$）。

**这五条全部与 Seiberg 1996 描述的 $\mathbb{R}^3\times S^1$ 物理度量相符**。作者的原话是：最简单的自洽图像就是"我们造的就是物理度量"；在秩 1 情形 Seiberg 曾提出这些性质（借 Yau 定理的非紧类比）**决定**了度量。

---

## 5. §7：真正的"证明"是怎么反过来的

§5 是「**造**一个度量，验证它满足 KS 公式」，逻辑上是"若 KS 成立则度量光滑"。§7 反过来：

1. 目标：直接从规范理论造出 (5.30)–(5.35) 那组方程，不去假设度量长什么样。
2. 第一步（(5.30)(5.31)，即 $u$-方向的 CR 方程）：来自约化理论的 $\mathcal{N}=4$ 超对称，几何意义是 $X(\zeta)$ 关于 $J^{(\zeta)}$ 的全纯性（附录 B 给出完整推导）。**这一步是硬的。**
3. 第二步（$\Lambda$ 方程 (5.32)(5.33)，以及有质量时的 (6.11)(6.12)）：把 $\Lambda$ 看成一个"背景"矢量多重态的标量分量，方程形式与 CR 方程完全一样——这是证明非重整化定理的标准技巧（Seiberg 1993），故可同样证。**这一步是硬的（借用已知技术）。**
4. 第三步（$R$ 与 $\zeta$ 方程 (5.34)(5.35)）：由 $d=4$ 理论的**反常 $U(1)_R$ 对称性**与**标度不变性**（即 (5.42)(5.43)）推出；物理上它们是反常 Ward 恒等式（作者说 $X_\gamma$ 可解释为 3d 拓扑场论手征环元素或 4d 线算子期望值，另文讨论）。
5. 第四步（斯托克斯因子确实是 $S_\ell$）：由 (5.34)，斯托克斯因子在 $R$ 变化下不变 $\Rightarrow$ 取 $R$ 很大 $\Rightarrow$ 那里度量修正可很好近似为**已知的单瞬子修正线性叠加**（§4 的 abelian 结果）$\Rightarrow$ 从联络转回 RH 问题，重复 §5 的论证 $\Rightarrow$ 斯托克斯因子 $=S_\ell$。
6. 于是：$\mathbb{CP}^1$ 上的联络存在、其斯托克斯因子由 $\Omega$ 给出、且随 $u$ 作等单值形变 $\Rightarrow$ **WCF**。

**结论（作者自陈）**："至少是在物理的严格性水平上"。

> 为什么这叫"证明"而不是"循环论证"？因为 §7 的输入里**没有**"度量应当具有某种形式"这一假设；它只用 $\mathcal{N}=4$ 超对称、非重整化定理、反常。而 §5 用到的"度量必光滑"是物理要求。两者汇合于同一组方程，于是 WCF 被夹住。

---

## 6. 附录各自在证明中的角色（别把它们当装饰）

| 附录 | 内容 | 在证明里的地位 |
|---|---|---|
| A（p51–55） | 用 $SU(2)$ 理论逐项验证 KS 恒等式：递推 $x_{n+1}x_{n-1}=(1-x_n)^2$、通解 $\cosh^2/\sinh^2$、无穷乘积 $K^{-1}_{0,1}K^{-1}_{1,0}K_{0,1}K_{1,1}K_{1,0}=1$、五边形型恒等式 | **唯一可以当"定理"用的部分**：可独立复算，验证 $\Omega$ 的跳变确实满足 WCF |
| B（p56–57） | $\mathcal{M}$ 上的 CR 方程 $=$ $J^{(\zeta)}$ 全纯性 | §5.5 与 §7 第一步的几何依据 |
| C（p57–61） | 积分方程 (5.13) 的存在性与 $R\to\infty$ 渐近；含有限维 $tt^*$ 情形重做 | §5.3 的"解存在"与"首阶修正"的实际来源；技术地基 |
| D（p61–62） | 把 (5.30)–(5.35) 在给定 $\zeta=0$ 渐近展开下写具体；Nahm 型三式、等单值五式 | 研究小 $R$ 行为的工具；§5.5 末的评论 |
| E（p62–66） | 积分方程 $=$ TBA：散射矩阵、准粒子能量、核 $K$ | 与 2d 可积系统的接口；GMN2 的引子 |

---

## 7. 引用强度清单（写论文/写卡片时必须分清）

- **可当定理引用**：§4 的精确 GH 度量与 $A_{q-1}$ 奇点分析；附录 A 的恒等式；附录 B 的 CR 方程推导；附录 C/D 在给定方程下的渐近估计；(2.35) 的半平坦度量与其体积/凯勒性。
- **物理论证**（不能当定理）：§5 全篇（"存在满足条件的 $X$"依赖 (5.13) 的可解性，而 (5.13) 的可解性只在 $R$ 大时论证）；§5.7 的"这就是物理度量"（五条性质 + 最简自洽图像）；§7 的 WCF 证明（作者自己加了"physical level of rigor"）。
- **明确假设**：KS 公式本身（§5.2 用它保证连续性）；$R$ 足够大；$\mathcal{M}$ 的整体性（无额外奇点）；超共形点未分析。
- **已知缺口**：$X_\gamma$ 的物理解释（作者说另文）；小 $R$ 行为（Nahm 形变解可能奇异，但作者预期这些特解对一切 $R$ 正则）；非阿贝尔推广只在 §4.7 提了"更高秩"的方向。

---

## 8. 与后续文献的接口（给 GMN2/GMN3/GMW 的读者）

1. **→ GMN2（WKB / Hitchin 系统）**：本文的 RH 问题 (5.13) 在 GMN2 里变成"WKB 曲线上的谱网络 + 穿墙"；$X_\gamma$ 变成 Fenchel–Nielsen 型坐标；(5.13) 的核 $\frac{\zeta'+\zeta}{\zeta'-\zeta}$ 与 TBA 的关系（附录 E）是 GMN2 的出发点之一。**GMN2 要读通的接口：(5.13)+(5.14) 与附录 E。**
2. **→ GMN3（Framed BPS）**：本文的 $\Omega(\gamma;u)$ 是"无 framing"的；GMN3 引入 framed BPS 态与 $\mathcal{X}$ 的线缺陷解释，正是本文 §7 末"$X_\gamma$ 是线算子期望值"那句话的展开。
3. **→ GMW（红外代数）**：本文的"BPS 粒子 = 3d 瞬子""多瞬子抵消"是 GMW 的"BPS 态 $\leftrightarrow$ 网/junction"的二维版本前身；GMW1 的导读版可以看作本文 §1 的 2d 类比。

---

## 9. 最小记号表

| 记号 | 含义 | 易混点 |
|---|---|---|
| $\mathcal{B}$（`\vm`） | 4d 库仑分支，复维 $r$ | 与 $\mathcal{M}$ 混 |
| $\mathcal{M}$（`\CM`） | 3d 模空间 = $\mathcal{B}$ 上的环面丛 | 同上 |
| $\Gamma$（`\clat`） | 电荷格，带整值辛配对 $\langle\cdot,\cdot\rangle$ | |
| $Z_\gamma(u)$ | 中心荷；$Z(u)$ 是周期向量 | |
| $\Omega(\gamma;u)$（`\degen`） | BPS 简并度（第二螺旋度超迹） | 不是"态数"，可负 |
| $\mathcal{K}_\gamma$ | KS 辛同胚 (2.16) | 非线性 |
| $X_\gamma$ | 全纯坐标，$\mathbb{C}^\times$ 值，分段全纯 | $X^{\mathrm{sf}}$ 是零阶近似 |
| $\varpi(\zeta)$（`\hsymp`） | 全纯辛形式；(3.4) 与 (3.6) 两种定义必须相等 | |
| $\Upsilon$ | $X(X^{\mathrm{sf}})^{-1}$，控制 $\zeta\to0,\infty$ 渐近 | |
| $S_\ell$ | 射线 $\ell$ 上的总跳变（KS 乘积） | 与"斯托克斯因子"同义 |
| $\sigma$ | 二次加细 $\Gamma\to\{\pm1\}$ | 不加细则 Wilson 线不良定义 |
| $g^{\mathrm{sf}}$ | 半平坦度量 (2.35) | $R\to\infty$ 的首项 |

---

## 10. 如果只有三分钟

1. 4d $\mathcal{N}=2$ 放在 $\mathbb{R}^3\times S^1$ 上，BPS 粒子 $\to$ 3d 瞬子，大 $R$ 展开的系数是 $\Omega(\gamma;u)$。
2. 度量必须光滑，$\Omega$ 会跳变 $\Rightarrow$ 单瞬子的跳变必须被多瞬子抵消 $\Rightarrow$ 这个抵消条件就是 KS 穿墙公式。
3. 技术上：用一个在 $\mathbb{CP}^1$ 上分段全纯的映射 $X_\gamma$ 把整件事编码成一个黎曼–希尔伯特问题；它的可解性 $\Leftrightarrow$ 连续性 $\Leftrightarrow$ WCF；解由 TBA 型积分方程 (5.13) 给出，大 $R$ 迭代 = 瞬子展开。
4. §7 把这个逻辑反过来，只用 $\mathcal{N}=4$ 超对称、非重整化定理、$U(1)_R$ 反常造出同一组方程，从而（在物理严格性水平上）证明 WCF。

---

*本报告由 Lead（DSH agent）撰写，2026-11-21。若与原文冲突，以原文为准；若发现本报告有误，请记入 `工程文件/work/02_疑点清单.md` 并在下一次修订中改。*
