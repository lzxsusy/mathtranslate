# Gaitsgory–Rozenblyum 2014（cdm14）资料卡索引

共 35 张：概念卡 27 张、推导卡 8 张。


## 轨道 A · de Rham 预栈与晶体定义


**概念卡**

- [经典形式光滑的预栈](concepts/classically-formally-smooth.md) —— 每个测试映射 $S\to Y$ 都能在 $S$ 的既约化上、沿幂零方向自由延伸的预栈；此时 $Y_{\mathrm{dR}}$ 由 Čech 神经算出。
- [de Rham 预栈 $X_{\mathrm{dR}}$](concepts/dr-prestack.md) —— 把测试环先约化成既约经典环、再取 $X$ 的预栈；它记的是 $X$ 的「无穷小邻域」信息。
- [局部几乎有限型（laft）与 $Y_{\mathrm{dR}}$ 的正性](concepts/laft-and-dr.md) —— $\PreStk_{\mathrm{laft}}$ 是收敛、且各截断局部有限型的预栈；$\mathrm{dR}$ 把它留在其中并变成经典的。

**推导卡**

- [dR 与极限交换、左 Kan 延拓表述](derivations/dr-kan.md) —— 从逐对象定义直接读出 dR 保极限，再把左 Kan 延拓写成逐对象余极限。

## 轨道 B · 左/右晶体、IndCoh 与 Kashiwara


**概念卡**

- [Kashiwara 引理：闭浸入上的晶体即开补上为零的晶体](concepts/kashiwara.md) —— 闭浸入 $i:X\hookrightarrow Z$ 上，$\Crys(X)$ 等价于 $\Crys(Z)$ 中在开补 $Z^\circ$ 上为零的对象。
- [左晶体：$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$](concepts/left-crystal.md) —— 左晶体就是 de Rham 预栈上的拟凝聚层；它由「对每个 $S\to Y_{\mathrm{dR}}$ 给一个 $\QCoh(S)$ 中的对象」的下降数据描述。
- [右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](concepts/right-crystal.md) —— 右晶体是 de Rham 预栈上的归纳凝聚层，用 $f^!$ 作拉回；它比左晶体多了 $t$-结构与推前的函子性。
- [$\Upsilon$：左晶体与右晶体的比较](concepts/upsilon-comparison.md) —— $\Upsilon_S(F)=F\otimes\omega_S$ 把 $\QCoh$ 送到 $\IndCoh$，逐层拼起来给出 $\Crys^l(Y)\to\Crys^r(Y)$，并且是等价。

**推导卡**

- [命题 2.5.6 的证明：把 $\Crys^r(Z)_X$ 算成形完备化](derivations/kashiwara-equiv.md) —— 把 $\Crys^r(X)$ 写成 $\IndCoh(S^\wedge)$ 的极限，把 $\Crys^r(Z)_X$ 写成 $\ker(j_S^!)$ 的极限，再用形式完备化的 $\IndCoh$ 描述把两者对上。
- [命题 2.4.4 的证明：逐层 $\Upsilon$ 拼成全化上的等价](derivations/upsilon-equiv.md) —— 把一般 $Y$ 化到「仿射 $X$ 在光滑 $Z$ 中的形式完备化」，两边都用 Čech 全化，逐层用光滑情形的 $\Upsilon$ 等价。

## 轨道 C · 下降性质与归纳函子


**概念卡**

- [晶体满足 h-下降](concepts/h-descent.md) —— $\Crys^r$ 把 h-拓扑（Zariski + 固有满）的覆盖送到全化极限；特别地满足 fppf 下降。
- [左晶体的归纳函子与最终余连接假设](concepts/induction-left.md) —— 左晶体一般不能写成 $\QCoh$ 的全化；只有最终余连接的 DG 概形才成立，此时可借 $\Upsilon$ 定义 $\ind^l_X$。
- [右晶体的归纳函子 $\ind^r_X$](concepts/induction-right.md) —— $\oblv^r_X$ 有左伴随 $\ind^r_X:\IndCoh(X)\to\Crys^r(X)$，它把 $\IndCoh(X)$ 张成 $\Crys^r(X)$，并给出单子性。
- [无穷小群胚 $X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$](concepts/infinitesimal-groupoid.md) —— $X\to X_{\mathrm{dR}}$ 的 Čech 神经给出群胚 $X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$，它的每一项是主对角线的形式完备化。

**推导卡**

- [h-下降的证明：双单纯对象与两次全化](derivations/h-descent-proof.md) —— 把固有满覆盖 $S'\to S$ 与其 de Rham 版本拼成双单纯对象，两个方向各用一次命题 3.1.3，再比较全化。
- [命题 3.3.2 的证明：全化 + Barr–Beck–Lurie](derivations/right-induction.md) —— 先用命题 3.1.3 把 $\Crys^r(X)$ 写成全化，再用 [Lu2] 的单子性判据与 [GR1] 的基变换把伴随对认出来。

## 轨道 D · 晶体上的 t-结构


**概念卡**

- [$\Crys^r(X)$ 是其心上的导出范畴](concepts/abelian-heart.md) —— 仿射 DG 概形 $X$ 上，$\Crys^r(X)$ 等价于其 $t$-结构心上的（有界）导出范畴。
- [粗糙归纳与 Gorenstein 条件](concepts/coarse-induction.md) —— 把 $\IndCoh$ 先左完备化到 $\QCoh$，得到「粗糙」的归纳/遗忘函子；$\oblv^r$ 穿过 $\QCoh$ 当且仅当 $X$ 是 Gorenstein。
- [ind-概形上的右 $t$-结构](concepts/indscheme-t-structure.md) —— 把 ind-概形 $X=\mathrm{colim}\,X_\alpha$ 上的右 $t$-结构逐 $\alpha$ 定义，并用闭浸入的 $t$-正合性把它与形式完备化对齐。
- [$\Crys^r(X)$ 的左完备性](concepts/left-completeness.md) —— 右 $t$-结构下 $\Crys^r(X)$ 左完备；拟紧时 $\Crys(X)$ 在左 $t$-结构下也左完备。
- [左 $t$-结构：把 $\QCoh$ 的 $t$-结构搬到 $\Crys^l$](concepts/left-t-structure.md) —— $\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$ 用 $\QCoh$ 的典范 $t$-结构；$\oblv^l$ 右 $t$-正合。
- [左右 $t$-结构相差一个维数平移](concepts/left-vs-right-shift.md) —— 光滑 $n$ 维时，$\Crys^l$ 的左 $t$-结构与 $\Crys^r$ 的右 $t$-结构相差 $[-n]$；一般拟紧情形差有界幅度。
- [右 $t$-结构：晶体上的「那个」$t$-结构](concepts/right-t-structure.md) —— 用 $\oblv^r_X$ 把 $\IndCoh(X)$ 的 $t$-结构拉回，定义 $\Crys^r(X)$ 的右 $t$-结构；$\ind^r$ 与 $i_{\mathrm{dR},*}$ 都是 $t$-正合的。

**推导卡**

- [命题 4.2.11：$\oblv^r$ 的 $t$-正合性与有界幅度](derivations/right-t-exact.md) —— 光滑时用无穷小邻域把群胚写成 $\mathrm{colim}\,X_n$、$p_s\circ i_n$ 有限平坦；一般情形用闭浸入光滑 $Z$ 与 $i^!$ 的有界性。

## 轨道 E · 与 D-模的关系


**概念卡**

- [晶体与 D-模：经典等价](concepts/crystals-vs-dmodules.md) —— 经典有限型 $X$ 上，右晶体范畴等价于右 D-模的导出范畴，左晶体等价于左 D-模；等价与遗忘函子相容。
- [核 $D^l_X$ 与微分算子层 $\mathrm{Diff}_X$](concepts/diff-operators.md) —— 光滑经典 $X$ 上，$D^l_X$ 是 $\mathrm{Diff}_X$ 的代数推广：卷积对应复合，$D^l_X\to\mathrm{Diff}_X$ 是代数同构。
- [积分变换与核 $D^r_X$](concepts/integral-transform.md) —— $\IndCoh$ 自对偶把连续函子写成 $X\times Y$ 上的核；$\oblv^r\circ\ind^r$ 的核是 $D^r_X=(\widehat\Delta_X)_*\omega_{X\times_{X_{\mathrm{dR}}}X}$。

**推导卡**

- [§5.5 的证明：晶体 = D-模的六步](derivations/cdm-equiv.md) —— Zariski 下降 → Kashiwara 到光滑仿射 → 左右化 → 心上的范畴 → 单子比较，最后用 $D^l_X\simeq\mathrm{Diff}_X$ 收口。

## 轨道 F · 扭化


**概念卡**

- [$\mathbb G_m$-gerbe 与 $\mathbf{Ge}_{\mathbb G_m}$](concepts/gm-gerbe.md) —— $\mathbb G_m$-gerbe 是 $\mathbf{pt}/\mathbb G_m$ 的 torsor 预层；三种「局部平凡」版本分别由 $B^{\mathrm{et}}$、$B^{\mathrm{Zar}}$、$B^{\mathrm{naive}}$ 表示。
- [扭化的 Picard 群胚：$\mathrm{Tw}(Y)\simeq\tau^{\le2}(H_{\mathrm{dR}}\times_H *)[2]$](concepts/twist-picard.md) —— $\mathrm{Tw}(Y)$ 是 $\tau^{\le2}(H_{\mathrm{dR}}(Y)\times_{H(Y)}*)[2]$；光滑经典 $X$ 上化为 $\tau^{\le2}\Gamma(X,\Omega^1\to\Omega^{2,\mathrm{cl}})[2]$。
- [扭化 $\mathrm{Tw}(Y)$](concepts/twisting.md) —— $\mathrm{Tw}(Y)$ 是「在 $Y_{\mathrm{dR}}$ 上的 gerbe，加上在 $Y$ 上的平凡化」；线丛 $L$ 给出例子 $T(L)$。

**推导卡**

- [命题 6.4.2：三种扭化版本在仿射上逐点相等](derivations/twist-three.md) —— 只在 $S\in\DGSch_{\mathrm{aff}}$ 上算：把核写成纤维积，再用引理 6.3.10 与指数映射把三个版本对齐。

## 轨道 G · 扭晶体


**概念卡**

- [扭晶体：$\Crys^{T,l}$ 与 $\Crys^{T,r}$](concepts/twisted-crystals.md) —— 固定 $T\in\mathrm{Tw}(Y)$，把 $\QCoh/\IndCoh$ 换成 $T$-扭版本，得到 $\Crys^{T,l}(Y)$、$\Crys^{T,r}(Y)$，两者仍由 $\Upsilon$ 等价。
- [扭晶体上的两个 $t$-结构](concepts/twisted-t-structure.md) —— 扭情形同样有左/右两个 $t$-结构；$\ind^{T,r}$ $t$-正合，$\oblv^{T,r}$ 有界，且 $\Crys^{T,r}(X)$ 左完备。

## 轨道 总览


**概念卡**

- [全书总览：晶体是 de Rham 预栈上的层](concepts/overview.md) —— 把晶体定义为 de Rham 预栈上的（归纳）凝聚层，在导出代数几何里重建左/右 D-模、t-结构与扭化。
