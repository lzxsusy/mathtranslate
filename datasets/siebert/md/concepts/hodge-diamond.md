# Hodge 菱形

> `siebert/concept/hodge-diamond` ｜ track A ｜ draft

**一句话**：把 $h^{i,j}=\dim H^j(X,\Omega_X^i)$ 排成菱形，Serre 对偶与复共轭给出两重对称；五次超曲面的中间两行是 $1/101,101/1$。

**自测**：为什么五次超曲面的 Hodge 菱形只由 $h^{1,1}$ 与 $h^{2,1}$ 两个数决定，而这两个数又分别来自哪里？

## 定义

设 $X$ 为 $n$ 维紧 Kähler 流形。Dolbeault 上同调 $H^{i,j}_{\bar\partial}=H^j(X,\Omega_X^i)$，$h^{i,j}=\dim_{\CC}H^{i,j}$。Hodge 分解 $H^k(X,\CC)=\bigoplus_{i+j=k}H^{i,j}$ 给出 $b_k=\sum_{i+j=k}h^{i,j}$；Serre 对偶给出 $h^{i,j}=h^{n-i,n-j}$，复共轭给出 $h^{i,j}=h^{j,i}$。把 $h^{i,j}$ 按 $i$ 为行、$j$ 为列排成菱形，即 Hodge 菱形。Calabi–Yau $n$ 维流形满足 $h^{n,0}=1$、$b_1=0$；$n=3$ 时 $h^{3,0}=h^{0,3}=1$、$h^{1,0}=h^{0,1}=0$，故菱形由 $h^{1,1}$ 与 $h^{2,1}$ 两个数决定。五次超曲面的有趣部分是 $h^{3,0}=1$、$h^{2,1}=h^{1,2}=101$、$h^{1,1}=1$；其镜像的 Hodge 菱形把 $1$ 与 $101$ 对调。

记号：$h^{i,j}$：$H^j(X,\Omega_X^i)$ 的维数；$\Omega_X^i=\wedge^i\Omega_X^1$；$\Theta_X$：全纯切丛；$\mathrm{Def}(X)$：复结构形变空间；$\PP^4$ 为复射影空间。

## 要点

- 两重对称：Serre 对偶是中心对称 $h^{i,j}=h^{n-i,n-j}$，复共轭是左右对称 $h^{i,j}=h^{j,i}$；两者合起来只需算菱形的一个扇形。
- 对 Calabi–Yau 三维流形，$K_X\cong\O_X$ 给出 $\Theta_X\cong\Omega_X^2$，于是 $H^1(X,\Theta_X)=H^1(X,\Omega_X^2)=H^{2,1}$；复结构形变的维数因此恰好是 $h^{2,1}$（Kodaira–Spencer）。
- $h^{1,1}=1$ 来自弱 Lefschetz：$H^2(\PP^4,\ZZ)\to H^2(X,\ZZ)$ 是同构，故 $\mathrm{NS}(X)=\ZZ\cdot h$；Calabi–Yau 流形上 $\mathrm{Pic}=\mathrm{NS}$，所以 $h^{1,1}=1$。
- $h^{2,1}=101$ 来自 $h^1(\Theta_X)=101$：参数计数 $126-1-24$ 与长正合列 $0\to\CC^{24}\to\CC^{125}\to H^1(\Theta_X)\to0$ 两条路线给出同一个数。
- 镜像对称交换 $h^{1,1}$ 与 $h^{2,1}$：五次超曲面的 $1/101$ 变成镜像五次超曲面的 $101/1$；这是检验镜像构造是否正确的判据，不是算错。

## 公式

$$h^{i,j}=h^{j,i}=h^{n-i,n-j},\qquad H^k(X,\CC)=\bigoplus_{i+j=k}H^{i,j}_{\bar\partial}$$
$$h^{3,0}=1,\qquad h^{2,1}=h^{1,2}=101,\qquad h^{1,1}=1$$
$$H^1(X,\Theta_X)\cong H^{n-1,1}(X)\ \Longrightarrow\ \dim\mathrm{Def}(X)=h^{2,1}$$

## 定理与证明

### 五次超曲面的 Hodge 菱形

设 $X=\{f=0\}\subset\PP^4$ 为光滑五次超曲面。则 $h^{1,1}(X)=1$，$h^{2,1}(X)=h^{1,2}(X)=101$，$h^{3,0}(X)=h^{0,3}(X)=1$，其余 $h^{i,j}$ 为 $0$ 或由 Serre 对偶给出。

（sketch；来源：原书 p.11–14）

1. $h^{3,0}=1$：$\Omega=\mathrm{Res}_X(\widetilde\Omega/f)$ 是全纯、处处非零的三形式，故 $H^0(X,K_X)=\CC\cdot\Omega$。  
   为什么：Calabi–Yau 流形的 $K_X$ 平凡，$h^{n,0}=1$ 是定义性质；留数构造给出这个非零截面。
2. $h^{1,1}=1$：弱 Lefschetz 给 $H^2(\PP^4,\ZZ)\cong H^2(X,\ZZ)=\ZZ\cdot h$，$(1,1)$ 类定理给 $\mathrm{NS}(X)=H^2(X,\ZZ)\cap H^{1,1}$，故 $h^{1,1}=1$。  
   为什么：对 $k=2<n=3$， Lefschetz 超平面定理把 $\PP^4$ 的上同调同构地拉回到 $X$；$\PP^4$ 的 $H^2$ 秩为 1。
3. $h^{2,1}=101$：对 $0\to\Theta_X\to\Theta_{\PP^4}|_X\to\O_X(5)\to0$ 取长正合列，得 $H^1(\Theta_X)\cong\CC^{125}/\CC^{24}$，维数 $101$；再由 $\Theta_X\cong\Omega_X^2$ 得 $H^{2,1}=101$。  
   为什么：$H^0(\Theta_{\PP^4}|_X)=\CC^{24}$（$\PP^4$ 的无穷小自同构），$H^0(\O_X(5))=\CC^{125}$（$126$ 个五次多项式除以整体标度），两者的余核就是 $H^1(\Theta_X)$。

缺口：本卡只列骨架；$H^0(\Theta_{\PP^4}|_X)\to H^0(\O_X(5))$ 的像为 24 维、以及 Bott 消没的细节，见 quintic-h11-count 卡。

## 易错点

- Hodge 菱形的对称是 Serre 对偶加复共轭，不是任意对称；$h^{3,0}=h^{0,3}=1$ 这种外圈只在 Calabi–Yau（更一般地，$K_X$ 平凡）时成立。
- $H^1(X,\Theta_X)=H^{n-1,1}$ 用了 $K_X\cong\O_X$；对一般流形 $H^1(\Theta_X)$ 不是 Hodge 分解的一项，不能这样读。
- $h^{1,1}=1$ 不能从『$X$ 是一个超曲面所以只有一个除子』直接读出：要先用 Lefschetz 定理确定 $H^2$ 的秩，再用 $(1,1)$ 类定理与 $\mathrm{Pic}=\mathrm{NS}$。
- $h^{2,1}=101$ 与 $\dim\mathrm{Def}(X)=101$ 是同一件事，但 $126-1-24$ 只是参数计数；只有在 $X$ 光滑、形变无阻碍时才等于 $h^1(\Theta_X)$。
- 镜像的 Hodge 菱形是 $101/1,1/101$，不是把原菱形『旋转』任意角度；交换的是 $h^{1,1}$ 与 $h^{2,1}$ 这一对。

## 参考与关联

- Siebert, Mirror Symmetry (lectures, Fall 2019; notes by Jackson Van Dyke)，第 1 章 §3 Hodge 菱形，p.11–14（原书 p.11–14）

关联：`siebert/deriv/quintic-h11-count`、`siebert/concept/mirror-quintic`、`siebert/concept/calabi-yau-manifold`

来源说明：原书 p.11–14（1.26–1.33 的 Hodge 菱形、Dolbeault 上同调、$(1,1)$ 类 Lefschetz 与弱 Lefschetz）。nLab「Hodge theory」（last revised 2023-10-18）核过 Hodge 分解与 Serre 对偶的表述；nLab「Calabi-Yau manifold」（2026-01-06）核过 $h^{n,0}=1$ 与 $K_X\cong\O_X$。
