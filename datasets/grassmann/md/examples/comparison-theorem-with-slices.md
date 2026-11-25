# 与切片解消的比较定理

> `grassmann/example/comparison-theorem-with-slices` · 轨道 5 · BD Grassmannian 与辛纽结同调 · 状态 draft

> **这张卡练什么**：两个同构要「与方图相容」，这句话比「两个簇同构」多出了什么信息？

## 一句话

取 $G=SL_m$、$\lambda_i=\omega_{\pi_i}$，则本章的开卷积/奇异格拉斯曼与切片解消 $\widetilde{S}_{m,k}^\pi\to S_{m,k}^\pi$ 同构，且两个方图交换：框架就是 Manolescu 的构造。

## 背景定义

**比较定理（定理 4.1）**：存在同构 ${}_0\widetilde{\Gr}_{\mathbb{C}^n}^{\underline{\lambda}}\cong\widetilde{S}_{m,k}^\pi$ 与 ${}_0\Gr_{\mathbb{C}^{\underline{\lambda}}}^{\underline{\lambda}}\cong S_{m,k}^\pi$，它们与以下两个方图相容：$\mathbb{C}^n$ 上的两个族分别同构，且底映射 $\mathbb{C}^n\to\mathbb{C}^{\underline{\lambda}}=\mathbb{C}^\pi$ 在两种语言里是同一条。

## 设定

取 $G=SL_m$，故 $G^\vee=PGL_m$，微小权记为 $\omega_1,\dots,\omega_{m-1}$。取 $\underline{\lambda}=(\lambda_1,\dots,\lambda_n)$ 使 $\sum\lambda_i$ 落在根格、每个 $\lambda_i$ 微小，并令 $\pi_i\in\{1,\dots,m-1\}$ 满足 $\lambda_i=\omega_{\pi_i}$。则 $N:=\pi_1+\dots+\pi_n$ 被 $m$ 整除，记 $N=mk$。此时 $\Sigma_{\underline{\lambda}}=\Sigma_\pi$ 且 $\mathbb{C}^{\underline{\lambda}}=\mathbb{C}^\pi$，其中 $\mathbb{C}^{\underline{\lambda}}$ 是 $\mathbb{P}^{1^{\underline{\lambda}}}$ 中所有点都落在 $\mathbb{C}$ 里的子簇。要比较的两个族是 ${}_0\widetilde{\Gr}_{\mathbb{C}^n}^{\underline{\lambda}}\to\mathbb{C}^n$、${}_0\Gr_{\mathbb{C}^{\underline{\lambda}}}^{\underline{\lambda}}\to\mathbb{C}^{\underline{\lambda}}$ 与 $\widetilde{S}_{m,k}^\pi\to\mathbb{C}^n$、$S_{m,k}^\pi\to\mathbb{C}^\pi$。

## 计算

把两边都化到同一个中间空间 ${}_0\mathcal{L}^{\underline{\lambda}}$ 上：它由链 $L_0=\mathbb{C}[z]^m\supset L_1\supset\dots\supset L_n$ 组成，每个 $L_i$ 是秩 $m$ 的自由 $\mathbb{C}[z]$-子模，$\dim(L_{i-1}/L_i)=\pi_i$，$z$ 在 $L_{i-1}/L_i$ 上作标量，且 $[e_1],\dots,[e_m],[ze_1],\dots,[z^{k-1}e_m]$ 是 $\mathbb{C}[z]^m/L_n$ 的一组基。(1) 几何侧：$\mathbb{P}^1$ 上两个 $PGL_m$-丛在 $x\neq\infty$ 外同构、在 $x$ 处型 $\omega_j$，等价于存在秩 $m$ 向量丛 $V_1,V_2$ 使 $L_2=\Gamma(\mathbb{C},V_2)\subset L_1=\Gamma(\mathbb{C},V_1)$、$\dim(L_1/L_2)=j$ 且 $(z-x)L_1\subset L_2$；逐点这样做就得到 $\widetilde{\Gr}_{\mathbb{C}^n}^{\underline{\lambda}}\to\mathcal{L}^{\underline{\lambda}}$，再把「$P$ 平凡」翻成「$L_n=z^k\mathbb{C}[z]^m$」即得 ${}_0$ 版本。(2) 代数侧：给定 $(L_0,\dots,L_n)\in{}_0\mathcal{L}^{\underline{\lambda}}$，令 $Y$ 为 $z$ 在 $L_0/L_n$ 上的作用，并把 $L_0/L_n$ 用优选基认同为 $\mathbb{C}^N$；链 $L_n/L_n\subset L_{n-1}/L_n\subset\dots\subset L_0/L_n$ 给出 $\mathbb{C}^N$ 中一条型为 $\pi$ 的旗 $W_\bullet$，$Y$ 保持每项且在相邻商上作标量，故 $(Y,W_\bullet)\in\widetilde{\mathfrak{gl}}_N^\pi$；又 $Y[z^i e_j]=[z^{i+1}e_j]$（$0\le i\le k-2$）给出 $Y\in S_{m,k}$，即 $(Y,W_\bullet)\in\widetilde{S}_{m,k}^\pi$。两条合起来给出 ${}_0\widetilde{\Gr}_{\mathbb{C}^n}^{\underline{\lambda}}\cong\widetilde{S}_{m,k}^\pi$；把 $\mathbb{C}^n$ 商成 $\mathbb{C}^{\underline{\lambda}}=\mathbb{C}^\pi$ 得 ${}_0\Gr_{\mathbb{C}^{\underline{\lambda}}}^{\underline{\lambda}}\cong S_{m,k}^\pi$，且两个方图（上方同构与下方 $\mathbb{C}^n\to\mathbb{C}^{\underline{\lambda}}$、$\mathbb{C}^n\to\mathbb{C}^\pi$ 的交换性）都由「记 $Y$ 的标量即记 $x_i$」自动成立。

## 要点

- 定理把「框架」与「已知构造」钉在一起：$m=2$ 时回到 Seidel–Smith，一般 $m$ 且 $\pi=(1^k,(m-1)^k)$ 时回到 Manolescu 的二分构型空间。
- 同构的桥是同一个中间空间 ${}_0\mathcal{L}^{\underline{\lambda}}$：几何侧把它读成 Hecke 修正的链，代数侧把它读成「$z$ 在 $L_0/L_n$ 上的矩阵 + 优选基给出的旗」。
- 「与方图相容」比簇同构强：它保证纤维逐点对应，因而中间上同调的计算可以直接从切片一侧搬过来。
- 定理的证明在章内只是梗概（作者自述），关键的那句「$[e_1],\dots,[z^{k-1}e_m]$ 是基 $\iff V\cong\mathcal{O}(k)^{\oplus m}$」没有展开。

## 关键公式

$$
{}_0\widetilde{\Gr}_{\mathbb{C}^n}^{\underline{\lambda}}\cong\widetilde{S}_{m,k}^\pi,\qquad {}_0\Gr_{\mathbb{C}^{\underline{\lambda}}}^{\underline{\lambda}}\cong S_{m,k}^\pi
$$

$$
Y[z^i e_j]=[z^{i+1}e_j]\quad(0\le i\le k-2)\ \Longrightarrow\ Y\in S_{m,k}
$$

$$
\dim(L_{i-1}/L_i)=\pi_i,\qquad N=\pi_1+\dots+\pi_n=mk
$$

## 相关定理

- **定理 4.1（比较定理，Mirković–Vybornov / Ngô）**：设 $G=SL_m$、$\lambda_i=\omega_{\pi_i}$、$N=\sum\pi_i=mk$。则存在同构 ${}_0\widetilde{\Gr}_{\mathbb{C}^n}^{\underline{\lambda}}\cong\widetilde{S}_{m,k}^\pi$ 与 ${}_0\Gr_{\mathbb{C}^{\underline{\lambda}}}^{\underline{\lambda}}\cong S_{m,k}^\pi$，且它们与 $\mathbb{C}^n\to\mathbb{C}^{\underline{\lambda}}$、$\mathbb{C}^n\to\mathbb{C}^\pi$ 的两个方图相容。

## 易错点

- 容易把定理读成「两个纤维化同构」：定理只给 $\mathbb{C}^n$ 与其商 $\mathbb{C}^\pi$ 上的同构并保证方图交换，$\mathbb{P}^1$ 上其余点的对应要靠单值性沿路径搬运，不能逐点直接比较。
- 容易把 $\pi$ 与 $\underline{\lambda}$ 当成两套无关数据：$\pi_i$ 就是 $\lambda_i=\omega_{\pi_i}$ 的下标，$N=\sum\pi_i$ 必须被 $m$ 整除才能让 $P_n$ 平凡（这正是 $\sum\lambda_i$ 落在根格的算术形式）。

## 用到哪些概念

- [部分 Grothendieck 解消与幂零切片](../concepts/partial-grothendieck-resolution-and-nilpotent-slice.md)
- [几何 Satake 对应](../concepts/geometric-satake-correspondence.md)
- [整体奇异格拉斯曼流形](../concepts/global-singular-grassmannian.md)

## 相关卡

- [部分 Grothendieck 解消与幂零切片](../concepts/partial-grothendieck-resolution-and-nilpotent-slice.md)
- [$SL_2$ 两点碰撞的最小例子](../examples/sl2-two-point-collision.md)
- [整体奇异格拉斯曼流形](../concepts/global-singular-grassmannian.md)
- [部分消奇异](../concepts/partial-desingularization.md)

## 出处

- ch5 §4.3 定理 4.1（比较定理）；中译 p.91（英文 PDF p.100），源码 `chapters/ch05.tex:405`
