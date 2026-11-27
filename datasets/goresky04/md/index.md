# Goresky《为物理学家讲述的朗兰兹猜想》（goresky04）资料卡索引

共 22 张：概念卡 18 张、推导卡 4 张。


## 轨道 A · 域与 Galois 侧


**概念卡**

- [平展上同调与 Galois 作用](concepts/etale-cohomology.md) —— 对定义在 $\bbF_p$ 上的簇 $Y$，$H^i_{\et}(Y,\Ql)$ 是有限维 $\Ql$ 向量空间，带 $\Gal(\Qbar/\bbQ)$ 的连续作用；于是几何给出 Galois 表示。
- [Frobenius 元素与局部因子](concepts/frobenius-element.md) —— 在非分歧素数 $p$ 处，Galois 表示经过 $\Gal(\overline{\bbF}_p/\bbF_p)$ 分解，后者的生成元在表示中的像就是 $\Fr_p$；它的特征多项式定义了局部因子。
- [域的分类：数域、$p$ 进域、函数域](concepts/global-and-local-fields.md) —— 猜想原本写在 $\bbQ$ 上，但同一句话在数域、$p$ 进域、函数域上各有版本；本文先把「域」这一层列清楚，才谈得上推广。
- [代数簇的 $\zeta$ 函数与 Deligne 的四个结论](concepts/zeta-function-of-variety.md) —— $\zeta(Y,s)$ 把每个素数处 Frobenius 在 $H^i_{\et}$ 上的特征值打包成一个欧拉乘积；Deligne 证明它有理性、函数方程，且零点满足 Riemann 假设。

**推导卡**

- [从 Frobenius 特征值造出局部因子与欧拉乘积](derivations/local-zeta-factor.md) —— 把 $\Fr_p$ 的特征多项式取倒数得到 $\zeta_p(\rho,t)$，再把各素数处的 $\zeta_p(\rho,p^{-s})$ 乘起来就得到 $L(\rho,s)$；这一步是整篇文章「逐素数比较」的技术基础。

## 轨道 B · 自守侧


**概念卡**

- [平代环与限制直积](concepts/adele-ring.md) —— 平代环 $\bbA_\bbQ=\bbR\times\prod_p'\bbQ_p$ 是把所有完备化一次收进来的环；它使「对所有素数同时成立」的陈述可以写成一个整体对象上的陈述。
- [自守形式与自守表示](concepts/automorphic-representation.md) —— 自守形式是 $\GL(n,\bbQ)Z(\bbA)\backslash\GL(n,\bbA)$ 上满足增长与 $K$-有限条件的函数；自守表示是它在 $\GL(n,\bbA)$ 右正则作用下的不可约成分，尖点条件对应 $L^2_0$ 部分。
- [Hecke 特征形式与 Fourier 系数](concepts/hecke-eigenform.md) —— 若一个尖点形式是所有 $T_p$ 的共同特征向量，则它的 Fourier 系数 $a_n$ 与特征值 $\lambda_n$ 满足 $a_n=\lambda_n a_1$；于是「Hecke 特征值」就成了一串可比较的数。
- [Hecke 对应与 Hecke 算子](concepts/hecke-operator.md) —— 每个 $g\in\GL(2,\bbQ)$ 给出一个双陪集 $\Gamma g\Gamma$，它定义模曲线之间的对应，作用在函数上就是 Hecke 算子 $T_g=s_*t^*$。
- [经典模形式](concepts/modular-form-classical.md) —— $\SL(2,\bbZ)$ 的权 $k$ 模形式是上半平面上的全纯函数，在 $\SL(2,\bbZ)$ 作用下按 $k$ 次自守因子变换；尖点形式是其中在尖点处取零的那些。

**推导卡**

- [从模形式到平代环上的自守形式（(6.1.1)）](derivations/adelic-equivalence.md) —— 把 $\SL(2,\bbZ)\backslash\he$ 写成 $\GL(2,\bbQ)Z(\bbA)\backslash\GL(2,\bbA)/\sO(2)K_{\mathrm f}$，模形式就变成平代环上的函数；这一步把古典对象交给整体表示论处理。

## 轨道 C · 对应与障碍


**概念卡**

- [Eichler–Shimura：$n=2$ 情形猜想的证明](concepts/eichler-shimura-theorem.md) —— 模曲线 $X$ 的平展上同调 $H^1_{\et}(X,\Ql)$ 分解为 Eisenstein 部分与尖点部分，尖点部分正好给出与 Hecke 特征形式对应的 $2$ 维 Galois 表示——这就是 $n=2$ 的朗兰兹对应。
- [$n\ge3$ 的障碍：Shimura 簇不存在](concepts/obstruction-n-ge-3.md) —— 对 $n\ge3$，对应的 Shimura 簇不存在，模空间那一侧整个失效；原文说「这是本领域最大的谜团之一」。
- [Satake 参数：非分歧局部表示的指纹](concepts/satake-parameter.md) —— 非分歧局部表示 $\pi_p$ 由球 Hecke 代数 $H_p$ 的一个特征（即 $n$ 个数的无序组 $\alpha_1,\dots,\alpha_n$）唯一确定；这组数就是 Satake 参数，也等于 $T_p$ 的特征值。
- [Shimura 簇：$n=2$ 的几何载体](concepts/shimura-variety.md) —— Shimura 簇是带水平结构的阿贝尔簇的模空间；对 $n=2$ 它就是一维的模曲线，所以有上同调可用；$n\ge3$ 时对应的空间不再是簇。

**推导卡**

- [$n=2$：上同调分解给出 Galois 表示（(7.1.1)）](derivations/eichler-shimura-decomposition.md) —— 抛物上同调 $H^1_P(X,E_k;\bbQ)\otimes\bbC$ 分解为 $S_k\oplus\overline{S_k}$，每个尖点特征形式贡献一个 $2$ 维 Galois 表示，这就是 $n=2$ 的对应。
- [把 Hecke 特征值对上 Frobenius 特征值](derivations/hecke-to-frobenius.md) —— 在非分歧素数 $p$ 处，自守侧的 Satake 参数 $\alpha_1,\dots,\alpha_n$ 与 Galois 侧 $\Fr_p$ 的特征值 $\beta_1,\dots,\beta_n$ 逐一相等，于是两个局部因子相等、两个 $L$ 函数相等。

## 轨道 D · 几何侧与展望


**概念卡**

- [对偶群与 $L$-群](concepts/dual-group.md) —— 对偶群 $G^\vee$ 由 $G$ 的根数据（把根与余根互换）决定；加上 Galois 作用得到 $L$-群 ${}^{L}G$，它是朗兰兹对应里「左侧」的群。
- [函子性：换群的那条路](concepts/functoriality.md) —— 若两个群的对偶群之间有同态 ${}^{L}H\to{}^{L}G$，则 $H$ 的自守表示应当「转移」为 $G$ 的自守表示；这是朗兰兹猜想的主干推广。
- [几何朗兰兹：把猜想搬到曲线上](concepts/geometric-langlands.md) —— 把 $\bbQ$ 换成曲线 $C$ 的函数域，把「Galois 表示」换成 $C$ 上的 $G$-丛与局部系统，把「自守表示」换成 $\Bun_G$ 上的层，得到几何版的对应。

## 轨道 总览


**概念卡**

- [朗兰兹猜想（$\GL(n,\bbQ)$ 版）的陈述](concepts/langlands-conjecture-statement.md) —— 对每个 $n$，$\Gal(\Qbar/\bbQ)$ 的「漂亮」$n$ 维表示与 $\GL(n,\bbA_\bbQ)$ 的「漂亮」自守表示应当一一对应，且 Frobenius 特征值对上 Hecke 特征值。
- [两侧的地图：Galois 侧与自守侧各有什么](concepts/two-sides-map.md) —— 左侧是平展上同调给出的 Galois 表示（数据是 Frobenius 特征值），右侧是模形式与自守表示（数据是 Hecke 特征值）；本文按「域—左侧—右侧—对照—推广」五步搭桥。
