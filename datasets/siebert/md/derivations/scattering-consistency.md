# 为什么壁结构必须满足所有余维的相容性

> `siebert/deriv/scattering-consistency` ｜ track E ｜ draft

**目标**：说明壁结构的相容性为什么必须在所有余维上成立：把「局部粘合」与「绕接合部一周」的差别算出来（例 5.6 的 $g=(1+wy)^{-1}x$），指出不相容会导致同一几何对象沿不同路径得到不同的环面模型、$\mathcal X^\circ$ 的余极限不存在，从而重构出的族不自洽；并给出 Kontsevich–Soibelman 的逐阶插入修正（式 5.65–5.66）。

**自测**：为什么「余维零和余维一都粘好了」还不够，绕接合部走一圈到底会坏在哪里？

## 前提

- $A=\CC[t]/(t^{k+1})$，$k$ 固定；初始数据 $(B,\mathscr P,\varphi)$ 与壁板函数 $f_\rho\in A[\Lambda_\rho]$（式 5.31、5.52）。
- 壁结构 $\mathscr S$：余维零的壁带 $f_{\mathfrak p}=1+c_mz^m$（$c_m\equiv0\bmod t$，$m$ 为传播方向），余维一的壁板取 $f_{\mathfrak p}=f_\rho$；壁穿越 $\Theta_{\mathfrak p}(z^m)=f_{\mathfrak p}^{\langle n_{\mathfrak p},m\rangle}z^m$，且 $\Theta_{\mathfrak p}\equiv\id\pmod t$（式 5.54–5.55）。
- 腔室 $\mathfrak u\subseteq\sigma$ 是 $B\setminus\bigcup\mathfrak p$ 的连通分支的闭包（可细分使凸），$R_{\mathfrak u}=R_\sigma=A[\Lambda_\sigma]$；余维一的 $e\subset\mathfrak u$ 给 $R_e=A[\Lambda_e][z_+,z_-]/(z_+z_--f_et^{\kappa_\rho})$（式 5.69）。
- 接合部（joins）：传播中的壁沿余维二的多面体子集相交所得的交线（例 5.6、图 5.58）。

## 步骤

1. **余维零与余维一的相容只给出局部粘合：对每个腔室 $\mathfrak u$ 与相邻的壁板 $e$，$\Theta_{\mathfrak p}$ 与局部化 $R_e\to R_{\mathfrak u}$ 使 $\Spec R_{\mathfrak u}$ 与 $\Spec R_e$ 能粘成 $\mathcal X^\circ$ 的局部片（式 5.68）。**  
   为什么：余维零的壁参与定义壁穿越，余维一的壁板提供 $z_+z_-=f_et^{\kappa_\rho}$ 的局部方程；两者都只涉及「一个腔室 + 一面壁」，所以只保证局部片，不保证绕一圈的闭合。  
   锚点：原书 p.91（式 5.68–5.69）（证据 A）

2. **但壁会沿接合部相交：在接合部附近有多个腔室与多面壁，从一点到另一点可绕接合部走不同的路径，穿壁的顺序与方向不唯一。**  
   为什么：接合部是余维二的交集，它的补在局部被壁分成多个扇形区域；沿小圆周绕接合部一周必然按顺序穿过这些壁，而沿另一条路径则顺序不同——两条路径的复合之差就是「不一致」。  
   锚点：原书 p.90（例 5.6 与图 5.58）（证据 A）

3. **例 5.6 的具体计算：设四面壁的函数使依次穿过给出 $x\mapsto(1+w)x\mapsto(1+(1+y)^{-1}w)x\mapsto\cdots$，四次复合化简为 $g=(1+wy)^{-1}x$（式 5.59–5.63）。**  
   为什么：每一步都是 $\Theta_{\mathfrak p}(x)=(1+u)x$ 型（$u$ 为某个单项式），复合就是这些因子相乘；(1+w)(1+(1+y)^{-1}w)(1+(1+(1+w)y)^{-1}w)(1+(1+(1+(1+y)w)y)^{-1}(1+y)w)$ 逐项约简后只剩 $(1+wy)^{-1}$——系数 $(1+wy)^{-1}\ne1$，说明复合不是恒等。  
   锚点：原书 p.90–91（式 5.59–5.63）（证据 A）

4. **所以必须在右上方对角线方向插入一面函数为 $1+wy$ 的壁（式 5.64）：把它再复合上去，$(1+wy)^{-1}\cdot(1+wy)=1$，复合才回到恒等。**  
   为什么：这一步是「散射」的字面含义：初始数据里没有这面壁，是相容性强制把它「射」出来的；讲义强调「无论从哪个单项式开始，该修正都有效」，说明这个插入不是碰巧。  
   锚点：原书 p.91（式 5.64）（证据 A）

5. **一般原理（Kontsevich–Soibelman）：把所有真壁函数取成 $\equiv1\pmod t$，并要求绕接合部逆时针一周的复合 $\Theta=\Theta_{\mathfrak p_1}\cdots\Theta_{\mathfrak p_r}\equiv\id\pmod{t^k}$；则按出射方向插入函数 $1+ct^{k+1}z^m$ 的壁可使 $\prod\Theta_{\mathfrak p}\equiv\id\pmod{t^{k+1}}$，且插入在壁结构等价意义下唯一（式 5.65–5.66）。**  
   为什么：「$\equiv\id\pmod{t^k}$」给出归纳起点；首个非零偏差必为 $1+ct^{k+1}z^m$ 形，插入一面壁恰好抵消它，故可逐阶推进。$k\to\infty$ 时得到无穷多面壁的极限，就是相容壁结构。  
   锚点：原书 p.91（式 5.65–5.66）（证据 A）

6. **为什么不相容就「族不自洽」：$\mathcal X^\circ=\varinjlim\{\Spec R_e,\Spec R_{\mathfrak u}\}$ 的余极限要求同一对象沿不同路径的像相同；若绕接合部的复合 $\Theta\ne\id$，则沿两条路径到达同一腔室时坐标差一个非平凡自同构，余极限或者不存在、或者只能作为 stack 存在，中心纤维的粘合也就依赖路径。**  
   为什么：余极限的万有性只认「所有道路给出相同的态射」；$\Theta\ne\id$ 意味着两条道路的合成不同，故不存在同时接受两者的对象。此时重构出的族在接合部附近没有统一的方程，$X_0=\bigcup P(\sigma)$ 的粘合会在该处出错——这正是「必须所有余维相容」的实质。  
   锚点：原书 p.91–92（式 5.68 与 Def 5.5）（证据 B）

7. **等价表述（Def 5.5）：$\mathscr S$ 相容，当且仅当局部对折线求和总能给出良定义的函数；折线在接合部附近的展开正是沿不同路径穿壁的复合，故「折线求和良定义」与「绕所有接合部复合为恒等」是同一件事。**  
   为什么：折线的每一段由 $\Theta_{\mathfrak p}$ 展开后选一项得到；若两条折线（对应两条路径）给出不同的末项系数，求和就不唯一。反之相容时逐项相同，求和与路径无关（式 5.73 的良定性）。  
   锚点：原书 p.92（Def 5.5、式 5.72–5.73）（证据 B）

## 结果

壁结构的相容性必须是「所有余维」的整体条件：余维零、一的粘合只给出局部片；绕接合部（余维二）一周的复合一般不等于恒等（例 5.6 给出 $(1+wy)^{-1}$），其偏差由散射插入新壁逐阶抵消（K–S 式 5.65–5.66，且在等价意义下唯一）。相容等价于「局部折线求和良定义」（Def 5.5），也等价于 $\mathcal X^\circ$ 的余极限存在；只有相容才能由定理 5.7 得到 $\mathcal X\supset\mathcal X^\circ$ 与 $X_0=\bigcup P(\sigma)$。

## 缺口

- 式 5.65、5.66 的模次在中文译文里比英文原文抬了一阶（译文 $t^{k+1}$、$t^{k+2}$，原文 $t^k$、$t^{k+1}$）；本卡按原文记，引用译文时需注意。
- 「插入在壁结构等价的意义下唯一」讲义只给结论，未证；严格证明需要先定义「壁结构的等价」，讲义没有定义。
- 式 5.59 的长式在讲义里只算了四面壁的情形；一般接合部上壁的数目与相对位置决定复合的复杂度，讲义未给一般公式。
- 讲义在 §5.7 只说「相容壁结构的存在性见文献 [16]（散射归纳构造）」并要求 $f_{\rho,v}=f_\rho$ 在余维二处「局部刚性」，但「局部刚性」的确切含义与验证方法未展开。
- Def 5.5 的「局部」没有量化（在多大多区域内求和）；严格陈述需要指定腔室与邻域，讲义从略。

## 易错点

- 「相容」不是「每个壁单独自洽」：单面壁的 $\Theta_{\mathfrak p}$ 总是自同构（因 $f_{\mathfrak p}\equiv1\bmod t$），问题只出在绕接合部的复合上。
- 绕一圈的复合与穿越方向有关：把 $\Theta_{\mathfrak p}$ 写成反向会得到 $\Theta^{-1}$，复合变成 $(1+wy)$ 而不是 $(1+wy)^{-1}$，插入的壁函数也随之相反。
- 例 5.6 的修正壁（函数 $1+wy$）不在初始数据里，是相容性强制产生的；把它当作「额外的假设」会误解散射的意思。
- 「所有余维」不等于「无穷多条件都要手算」：K–S 的逐阶插入把问题化归为「每阶一个单项式」，这正是可计算的原因。
- 与 nLab 的 wall crossing（BPS 稳定墙）无关；这里的「穿越」是环面模型之间的坐标变换，不是稳定性条件的变化。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §5.2 例 5.6（接合部、式 5.58–5.64）与 K–S 观察（式 5.65–5.66），p.90–91（原书 p.90–91）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §5.3 构造 $\mathcal X^\circ$（式 5.67–5.69），p.91–91（原书 p.91）
- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 5 章 §5.4 折线与 Def 5.5（相容性），p.92–92（原书 p.92）

关联：`siebert/concept/wall-structure`、`siebert/concept/broken-line`、`siebert/concept/theta-function`、`siebert/deriv/mumford-degeneration`、`siebert/deriv/dwork-a1`、`siebert/concept/batyrev-mirror-construction`

来源说明：原书 p.88–92：§4.1 不含散射的说明与式 5.43（p.88）、§4.1.1 传播（式 5.45–5.48，p.88–89）、§4.1.2 离开余维一的壁（式 5.49–5.51，p.89）、§5.2 壁穿越与例 5.5–5.6（p.90–91）、K–S 式 5.65–5.66（p.91）、§5.3–5.4 的 $\mathcal X^\circ$ 与 Def 5.5（p.91–92）。第 6 步的余极限论证是按余极限的万有性补出的（讲义只说「若相容则可构造」）。外部核对：Kontsevich–Soibelman, Affine structures and non-Archimedean analytic spaces（arXiv:math/0406564）§2 的 wall crossing 与 consistency；Gross–Siebert, From real affine geometry to complex geometry（arXiv:math/0703822）§2–§3；Gross–Siebert, The canonical wall structure and intrinsic mirror symmetry（arXiv:2105.02502）。nLab 无 scattering diagram 条目（站内检索 0 结果）。
