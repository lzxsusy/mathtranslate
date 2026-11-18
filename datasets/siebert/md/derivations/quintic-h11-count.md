# 五次三维超曲面的 Hodge 数与 $h^1(\Theta_X)$ 的计算

> `siebert/deriv/quintic-h11-count` ｜ track A ｜ draft

**目标**：计算光滑五次三维超曲面 $X\subset\PP^4$ 的 $h^{1,1}(X)$、$h^{2,1}(X)$ 与 $h^1(X,\Theta_X)$，并说明后两者相等、前者等于 $1$ 的理由。

**自测**：五次三维超曲面的 Hodge 数 $1,101$ 与 $h^1(\Theta_X)=101$ 是怎样一步步算出来的，为什么三个 101 恰好相等？

## 前提

- $X=V(f)\subset\PP^4$，$f$ 为五次齐次多项式，$X$ 光滑；$\Theta_X$ 为 $X$ 的切丛，$K_X\cong\OO_X$（Calabi–Yau）。
- Euler 序列 $0\to\OO_{\PP^4}\to\OO_{\PP^4}(1)^{\oplus5}\to\Theta_{\PP^4}\to0$，以及余法序列 $0\to\OO_X(-5)\to\Omega^1_{\PP^4}|_X\to\Omega^1_X\to0$（原书 (1.9)）。
- 超曲面 $X$ 由 $H^0(\OO_{\PP^4}(5))$ 的 126 维线性系统给出，$\dim\mathrm{PGL}(5)=24$。
- $\Theta_X\cong\Omega^2_X$：三维 Calabi–Yau 有 $\Omega^3_X\cong\OO_X$，由 $\Theta_X\cong\Omega^2_X\otimes(\Omega^3_X)^{-1}$ 得。

## 步骤

1. **先做参数计数：$126-1-24=101$。$H^0(\OO(5))$ 是 126 维，模去常数倍数（射影化）与 $\mathrm{PGL}(5)$ 的作用，得到 $101$ 维的模空间，故预期 $h^{2,1}(X)=101$。**  
   为什么：五次超曲面模空间的光滑点维数等于 $h^1(\Theta_X)$（Kodaira–Spencer），而 $h^1(\Theta_X)=h^{2,1}$；参数计数给出预期值，但它是『预期』不是证明——必须独立算出上同调，才能排除稳定化子、非光滑点等因素。  
   锚点：原书 p.10（证据 A）

2. **证明 $H^1(\Theta_{\PP^4}(-5))=0$：把 Euler 序列张量 $\OO(-5)$，得 $0\to\OO(-5)\to\OO(-4)^{\oplus5}\to\Theta_{\PP^4}(-5)\to0$。由 $H^{i}(\OO(-4))=H^{i+1}(\OO(-5))=0$（$i\ge0$，Bott 公式）知 $H^1(\Theta_{\PP^4}(-5))=0$。**  
   为什么：这一步是为了给余法序列的长正合列右端封口：$H^1(\Theta_{\PP^4}(-5))=H^1(\Theta_X|_X)$ 是 $H^1(\Theta_X)$ 的右邻项，只有它为零，才能断言 $H^1(\Theta_X)$ 恰是中间映射的余核。用 Bott 的消没区间 $H^q(\PP^n,\Omega^p(k))=0$（$0<q<n$）即可。  
   锚点：原书 p.11（证据 A）

3. **数出长正合列两端：$H^0(\Theta_{\PP^4})=\CC^{24}$。由 Euler 序列 $H^0$ 段 $0\to\CC\to\CC^{25}\to H^0(\Theta_{\PP^4})\to H^1(\OO)=0$ 得 $25-1=24$。又 $H^0(\OO_X(5))=\CC^{125}$：由 $0\to\OO\to\OO(5)\to\OO_X(5)\to0$ 得 $126-1=125$。**  
   为什么：这两个数是长正合列中相邻两项的维数；$24$ 是 $\mathrm{PGL}(5)$ 的维数（$25$ 个矩阵参数减去整体标度），$125$ 是五次齐次多项式模去常数倍的维数。必须分别算准，因为余核的维数 $125-24$ 正是 $h^1(\Theta_X)$。  
   锚点：原书 p.11–12（证据 A）

4. **写出余法序列的对偶长正合列（原书 (1.12)）：$0\to H^0(\Theta_X)\to H^0(\Theta_{\PP^4}|_X)=\CC^{24}\xrightarrow{v(f)}H^0(\OO_X(5))=\CC^{125}\to H^1(\Theta_X)\to H^1(\Theta_{\PP^4}|_X)=0$。故 $H^1(\Theta_X)\cong\CC^{125}/\mathrm{im}\,v(f)\cong\CC^{101}$。**  
   为什么：长正合列把 $H^1(\Theta_X)$ 写成余核；只要像的维数是 $24$（即 $v(f)$ 单射），余核维数就是 $101$。这一步是全卡的核心：$101$ 不是数出来的，是从两个上同调群的维数差算出来的。  
   锚点：原书 p.12（证据 A）

5. **像的维数是 24：在 $\mathfrak{gl}(5)$（25 维）层面看 $\xi\mapsto\xi(f)\bmod f$，Euler 关系 $\sum x_i\partial_i f=5f$ 说明 $E=\sum x_i\partial_i$ 落在核里；核恰为 $\CC\cdot E$（否则 $f$ 在一个单参数群下不变，与 $X$ 光滑矛盾），故像为 24 维。限制到 $\mathfrak{sl}(5)=H^0(\Theta_{\PP^4})$（24 维，$E\notin\mathfrak{sl}(5)$ 因 $\mathrm{tr}\,E=5$）上核为 0，故 $v(f)$ 单射、像为 24 维。**  
   为什么：若像的维数小于 24，余核就会大于 101，与参数计数不符，必须确认。Euler 关系是这里唯一的线性关系：它把 25 维的 $\mathfrak{gl}(5)$ 压成 24 维的像，这正解释了为什么是 24 而不是 25；而在 $\mathfrak{sl}(5)$ 上，压掉 $E$ 之后一个维度也不少，所以 $v(f)$ 单射。  
   锚点：原书 p.12（证据 B）

6. **由 $\Theta_X\cong\Omega^2_X$ 得 $H^1(\Theta_X)=H^1(\Omega^2_X)=H^{2,1}(X)$，故 $h^{2,1}=101$；再由弱 Lefschetz 定理 $H^2(\PP^4,\ZZ)\cong H^2(X,\ZZ)$ 与 $(1,1)$ 定理得 $h^{1,1}=1$（$H^2(X)$ 由超平面类 $h$ 生成）。**  
   为什么：$\Theta_X\cong\Omega^2_X$ 依赖 $K_X\cong\OO_X$：这是 Calabi–Yau 条件第一次真正被用到，没有它 Dolbeault 群与 $H^1(\Theta)$ 对不上。$h^{1,1}=1$ 不能从 $b_2=1$ 直接读出（$b_2$ 还可能含 $(2,0)$ 部分），必须先由弱 Lefschetz 得 $b_2=1$，再用 $(1,1)$ 定理排除 $(2,0)$ 类。  
   锚点：原书 p.13–14（证据 A）

## 结果

$h^{2,1}(X)=h^1(X,\Theta_X)=101$，$h^{1,1}(X)=1$，$h^{3,0}=h^{0,3}=1$，故 Hodge 菱形为 $1/101\;101/1$，Euler 数 $\chi=2(1-101)=-200$（与 $c_3(X)=-200$ 一致）。

## 缺口

- 步骤 5 中『$v(f)$ 的像为 24 维』讲义只以 Euler 关系断言，未逐项验证 $\mathrm{PGL}(5)$ 的 24 维作用与 $\ker v(f)$ 的维数恰好互补（即 $\ker v(f)$ 与 Euler 向量场张成的 1 维之和为 24+1=25）。
- Bott 公式的消没区间（$H^q(\PP^n,\Omega^p(k))=0$，$0<q<n$）讲义只引用，未给证明。
- 弱 Lefschetz 定理（$H^i(\PP^n)\to H^i(X)$ 当 $i<n$ 时为同构）在讲义 §4 引用而未证；$h^{1,1}=1$ 还额外用了 $(1,1)$ 定理与『$X$ 单连通故 $\mathrm{Pic}=\mathrm{NS}$』。
- Kodaira–Spencer 映射 $H^1(\Theta_X)\to T$ 的满射性（模空间光滑、维数等于 $h^1(\Theta_X)$）讲义未证，参数计数只作旁证。

## 易错点

- $101$ 的三个来源（$h^{2,1}$、$h^1(\Theta_X)$、次数 101）相等靠的是三维 Calabi–Yau 且单连通；换到一般三维流形或非 CY 情形，$h^1(\Theta_X)\neq h^{2,1}$。
- $H^0(\Theta_{\PP^4})$ 是 24 维而不是 25 维：$H^0(\OO(1)^{\oplus5})=\CC^{25}$，但 Euler 序列的 $H^0$ 段有 1 维常数截面，故为 $25-1=24$。
- $H^0(\Theta_X)=0$ 与 $H^0(\Theta_{\PP^4}|_X)=\CC^{24}$ 不是一回事：前者说明 $X$ 没有整体向量场（CY 的 $h^{0,0}$ 性质），后者是 $\PP^4$ 的向量场限制到 $X$。
- $126$ 是 $H^0(\OO(5))$ 的维数，$126-1$ 是模去整体标度，$126-1-24$ 才模去 $\mathrm{PGL}(5)$；漏掉 $-1$ 会得 $102$，漏掉 $-24$ 会得 $125$。
- 不能由『$X$ 是超曲面』直接断言 $h^{1,1}=1$：$h^{1,1}=1$ 需要弱 Lefschetz 加 $(1,1)$ 定理，两个定理缺一不可。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §2–§4（五次三维超曲面、Hodge 菱形、Lefschetz 超平面定理），p.10–14（原书 p.10–14）

关联：`siebert/concept/hodge-diamond`、`siebert/concept/quintic-threefold`、`siebert/concept/mirror-quintic`

来源说明：原书 p.10–14（§2 的 (1.12)–(1.18)、§3 的 Hodge 菱形与 (1.28)(1.33)、§4 的 Lefschetz 定理）。参数计数 $126-1-24=101$ 与长正合列逐项核对过译本；$\chi=-200$ 与 $c_3(X)=-200$ 的一致性另行核对。
