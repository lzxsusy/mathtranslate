# ch15.tex 待注点（对照英文原 PDF p71–p75）

## 待注 ch15.tex:9（原 PDF p72）

- 原文：and the center acts by pulling functions from local opers to global opers
- 概念：临界中心 $\mathfrak z_{\mathrm{crit}}$ 在 Beilinson–Drinfeld 局部化下的作用方向。
- 读者缺什么：这句英文与紧随的交换图方向相反。图中是 $\QCoh(\Op_{\checkG}(D_x))\leftarrow\QCoh(\Op_{\checkG}(X))$，即沿限制 $\Op_{\checkG}(X)\to\Op_{\checkG}(D_x)$ 把整体 oper 上的函数拉回到局部 oper；原文措辞正好说反，读者应以图为准，否则接不上 15.1 的 $V$-生成子范畴与中心作用。
- 建议来源：原书文献 [BD91]

## 待注 ch15.tex:18（原 PDF p72）

- 原文：The spectral space in the FLE is not the space of regular opers on D, but the larger fiber product
- 概念：FLE 谱空间 $\Op^{\mathrm{unr}}_{\checkG}$ 与 $D$ 上正则 oper 空间 $\Op_{\checkG}(D)$ 的差别。
- 读者缺什么：非分歧只要求底层 $\check G$-局部系统延拓到 $D$，不要求 oper 约化在 $D$ 上正则延拓；因此谱空间取纤维积 $\Op_{\checkG}(D^\times)\times_{\LocSys_{\checkG}(D^\times)}\LocSys_{\checkG}(D)$，比 $\Op_{\checkG}(D)$ 大，后者的点还要在 $t=0$ 处满足一般位置条件。缺这一对比，就看不懂 15.2 为何要用 λ̌ 分层来度量“缺陷”。
- 建议来源：原书文献 [FG07]、[ABC24a]

## 待注 ch15.tex:44（原 PDF p73）

- 原文：Ψ(M) := C^{∞/2}(n((t)), M ⊗ kχ). This is the semi-infinite cohomology, or BRST reduction, of M.
- 概念：半无限上同调 $C^{\infty/2}(\mathfrak n((t)),-)$ 与 BRST 约化；$k_\chi$ 是加性特征标给出的一维模。
- 读者缺什么：$\infty/2$ 指半无限维数；定义 $C^{\infty/2}$ 需先取 $\mathfrak n((t))$ 在临界水平中心扩张下的真空模，再作半无限 Chevalley 上链。这正是为何 $\Psi$ 在临界水平等同于 Drinfeld–Sokolov 约化；缺这些，44 行的公式只是记号。
- 建议来源：原书文献 [FG05]、[Fre02]

## 待注 ch15.tex:59（原 PDF p73）

- 原文：κ = κ_{G,crit} + c κ_{Kil,G}, κ̌ = κ_{Ĝ,crit} + c^{-1} κ_{Kil,Ĝ}.
- 概念：量子局部 Langlands 的水平 $\kappa$ 与对偶水平 $\check\kappa$；临界水平是 $c=0$ 的边界值。
- 读者缺什么：为何对偶侧用 $c^{-1}$、Killing 形式如何归一化；以及 $c\to0$ 时 $\check G$-Whittaker 侧退化为 oper 的经典谱几何（大水平极限给出 Satake），这正是 66 行“极限等价就是 FLE”的来源。
- 建议来源：原书文献 [FG05]

## 待注 ch15.tex:88（原 PDF p74）

- 原文：The functor Poinc^spec is the push–pull transform along the correspondence which compares a global local system with its formal-disk restrictions.
- 概念：谱 Poincaré 函子（push–pull／积分变换）。
- 读者缺什么：这个对应比较“全局局部系统”与“它在形式圆盘上的限制”，推前与拉回分别沿哪一侧；配合 89 行的纤维积 $\Op_{\checkG}(X\setminus\{x\})^{\mathrm{unr}}$，才能理解它如何把整体谱参数送到局部。
- 建议来源：原书文献 [ABC24a]

## 待注 ch15.tex:101（原 PDF p75）

- 原文：KL_{G,crit,x} ⊗_{QCoh(Op^unr_{Ĝ,x})} QCoh(Op_Ĝ(X\setminus x)^unr) → DMod_crit(Bun_G)
- 概念：DG 范畴在 $\QCoh$-模上的张量积；用全局谱参数增强局部化函子。
- 读者缺什么：$\otimes_{\QCoh(\Op^{\mathrm{unr}}_{\check G,\mathbf x})}$ 不是普通张量积，而是把 $\QCoh(\Op^{\mathrm{unr}}_{\check G,\mathbf x})$-模结构推过去（即加入全局谱参数）；“示意形式”表示这里省略了 ind-完备化等技术条件。
- 建议来源：原书文献 [ABC24a]
