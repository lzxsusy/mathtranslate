# 环面簇

> `siebert/concept/toric-variety` ｜ track D ｜ draft

**一句话**：仿射环面簇 = Spec k[σ^∨∩M]；把锥粘成扇就得到整体环面簇，锥的面与轨道闭包一一对应。

**自测**：为什么环面簇的组合数据（扇）能完全决定它的几何？

## 定义

仿射环面簇是 $X=\Spec k[\sigma^\vee\cap M]$，其中 $\sigma\subset N_\RR$ 是有理多面尖锥、$M=\Hom(N,\ZZ)$、$\sigma^\vee$ 为对偶锥（Def 4.4）。整体情形：扇 $\Sigma$ 是有理多面尖锥的集合，对取面封闭且两两交为共同面（Def 4.7），令\n$$X(\Sigma)=\varinjlim_{\sigma\in\Sigma}U_\sigma,\qquad U_\sigma=\Spec k[\sigma^\vee\cap M],$$\n沿 $U_{\sigma\cap\sigma'}\hookrightarrow U_\sigma,U_{\sigma'}$ 粘合（4.49），得环面簇。

记号：$M\cong\ZZ^d$、$N=\Hom(M,\ZZ)$；$T_N=\Spec k[M]\cong\GG_m^d$ 是稠密环面；$U_\sigma=\Spec k[\sigma^\vee\cap M]$；$|\Sigma|=\bigcup\sigma$ 是扇的支撑。

## 要点

- 仿射情形：$k[\sigma^\vee\cap M]$ 由 Gordan 引理有限生成（Prop 4.2），且是正规整环；$T_N=\Spec k[M]\subset X$ 是开嵌入。
- 环面理想由二项式 $x^a-x^b$（$\sum a_im_i=\sum b_im_i$）生成（Prop 4.3）：这使环面簇的组合与代数方程直接挂钩。
- 面 $\leftrightarrow$ 开子概形：$\tau\subseteq\sigma$ 时 $U_\tau=\Spec k[\tau^\vee\cap M]\hookrightarrow U_\sigma$ 是基本开子概形（Prop 4.5）。
- 轨道–闭包对应：$\tau\in\Sigma$ 给出闭子簇 $X(\Sigma_\tau)\subset X(\Sigma)$，维数 $d-\dim\tau$（4.63–4.64），它是子环面 $T_\tau$ 的轨道闭包；一维锥（射线）对应环面除子（p.68）。
- 整体性质：$|\Sigma|=N_\RR$（完备）$\iff$ $X(\Sigma)$ 固有；$X(\Sigma)$ 拟紧 $\iff$ $\Sigma$ 有限（Prop 4.8）；Thm 4.10 环面簇范畴 $\cong$ 有限扇范畴。

## 公式

$$X=\Spec k[\sigma^\vee\cap M],\qquad T_N=\Spec k[M]\hookrightarrow X$$
$$X(\Sigma)=\varinjlim_{\sigma\in\Sigma}U_\sigma,\qquad U_{\sigma\cap\sigma'}\hookrightarrow U_\sigma,\ U_{\sigma'}$$
$$\dim X(\Sigma_\tau)=d-\dim\tau,\qquad \tau\in\Sigma\ \text{为射线}\ \longleftrightarrow\ \text{环面除子}$$

## 定理与证明

### Prop 4.2：Gordan 引理

若 $C\subset N_\RR$ 是有理多面尖锥，则 $C\cap M$ 是有限生成的幺半群，从而 $k[C\cap M]$ 是有限生成 $k$ 代数。

（complete；来源：原书 p.60–61（Prop 4.2））

1. 取 $C$ 的极射线生成元 $m_1,\ldots,m_r\in M$，令 $K=\{\sum t_im_i:0\le t_i\le1\}$，则 $K$ 紧。  
   为什么：尖锥由有限条极射线张成，用它们造一个有界的基本域。
2. $K\cap M$ 是紧集里的离散集，故有限，记其元素为 $m_{r+1},\ldots,m_s$。  
   为什么：格点在紧集里只能有有限多个。
3. 任一 $m\in C\cap M$ 写成 $m=\sum_i\lfloor t_i\rfloor m_i+u$，其中 $u\in K\cap M$，故 $m$ 由 $m_1,\ldots,m_s$ 生成。  
   为什么：$\lfloor t_i\rfloor\ge0$ 是整数、$u$ 是基本域里的格点，这就给出有限生成。

### Prop 4.8：拟紧当且仅当扇有限

$X(\Sigma)$ 拟紧 $\iff$ $\\Sigma$ 是有限扇。

（complete；来源：原书 p.69（Prop 4.8、例 4.14））

1. $\Sigma$ 有限时 $X(\Sigma)$ 是有限个仿射簇 $U_\sigma$ 的并，故拟紧。  
   为什么：有限并的拟紧性是显然的。
2. 反之，$\bigcup_{\dim\tau=1}X(\Sigma_\tau)$ 只有有限个不可约分支（拟紧性），故一维锥只有有限多个；有限个一维锥张成的扇必有限。  
   为什么：每个不可约分支含一个环面除子，对应一条射线；分支有限 $\Rightarrow$ 射线有限。

## 易错点

- $\sigma$ 必须是尖锥（$\sigma\cap(-\sigma)=\{0\}$）：否则 $U_\sigma$ 含环面子群，不是环面簇（Def 4.4 的『尖』不能省）。
- 扇的两两交必须是共同面，不只是交集非空；否则 $U_{\sigma\cap\sigma'}$ 的粘合不成立，$X(\Sigma)$ 不是概形。
- 维数配对是 $\dim\tau+\dim(\tau^\perp\cap\sigma^\vee)=d$，不是 $\dim\tau+\dim\tau^\vee=d$（后者会得到 $2d$）。
- 『完备 $\iff$ 固有』只在有限扇时等价；例 4.14 的无穷扇给出非拟紧、非固有的环面簇。
- 射线对应的是环面除子（$T_N$ 不变除子），不是任意除子；$\mathrm{Cl}(X)$ 与环面除子群的关系还要看 $\Sigma$ 的几何（第 25 节起）。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §5 仿射环面簇，p.61–62（原书 p.61–62）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §10 整体化：扇，p.65–66（原书 p.65–66）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §13 环面分层，p.68–69（原书 p.68–69）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 4 章 §22 环面簇的范畴，p.73–73（原书 p.73）

关联：`siebert/concept/local-mirror-symmetry`、`siebert/concept/mirror-symmetry`、`siebert/concept/calabi-yau-manifold`

来源说明：原书 p.59–65（Def 4.1–4.7、Prop 4.2–4.5：锥、幺半群环、Gordan 引理、仿射环面簇、扇）、p.68–69（射线↔环面除子、Prop 4.8）、p.73（Def 4.11、Thm 4.10）。nLab「toric variety」（last revised 2024-07-29）核过术语与扇–多面体对应；Stacks Project 无环面几何章节。
