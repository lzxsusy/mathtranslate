# 余切栈 T*Bun_G 的哈密顿约化与整体幂零锥

- **id**：`bdh/concept/tstar-bun-hamiltonian-reduction`
- **类型**：concept
- **位置**：§1.2
- **问题**：为什么 $T^{*}\operatorname{Bun}_G$ 可以由 $T^{*}S$ 的哈密顿约化得到，而零纤维 $\operatorname{Nilp}$ 的维数只有 $\dim\operatorname{Bun}_G$？

> 对商栈 $K\backslash S$，其余切栈是 $K\backslash\mu^{-1}(0)$，其象征与算子代数层由不变式给出（式 (8)(9)）；$\operatorname{Bun}_G$ 的零纤维 $\operatorname{Nilp}:=p^{-1}(0)$ 满足 $\dim\operatorname{Nilp}=\dim\operatorname{Bun}_G$（式 (38)），因而是迷向的，$g>1$ 时还是 Lagrange 的。

## 定义

1.2.1 的一般原理：设 $\mathcal{Y}=K\backslash S$，$S$ 光滑、$K$ 作用，$\mu:T^{*}S\to\mathfrak{k}^{*}$ 为动量映射，$\mathfrak{k}:=\operatorname{Lie}K$，则余切栈是哈密顿约化 $T^{*}\mathcal{Y}=K\backslash\mu^{-1}(0)$。函数与算子在其上取 $K$-不变式：式 (8) 给出 $\Gamma(\mathcal{Y},P_{\mathcal{Y}})=\Gamma(S,\tilde{P}_S/I_S^{cl})^{\pi_0(K)}$，$I_S^{cl}:=(\operatorname{Sym}\Theta_S)\mathfrak{k}$；式 (9) 给出 $\Gamma(\mathcal{Y},D_{\mathcal{Y}})=\Gamma(S,\tilde{D}_S/I_S)^{\pi_0(K)}$，$I_S:=\mathcal{D}_S\cdot\mathfrak{k}$。在 $\mathcal{Y}=\operatorname{Bun}_G$ 上，Hitchin 纤维化 $p$ 的零纤维 $\operatorname{Nilp}:=p^{-1}(0)$ 称为整体幂零锥（global nilpotent cone）[La87][La88]：它是满足 $\eta\in H^{0}(X,\mathfrak{g}^{*}_{\mathcal{F}}\otimes\omega_X)$ 为幂零的 Higgs 对的模栈。式 (38) 说 $\dim\operatorname{Nilp}=\dim\operatorname{Bun}_G$；2.10.2 证明 $\operatorname{Nilp}$ 是迷向的，$g>1$ 时是 Lagrange 的。

**记号**：$\mathcal{Y}=K\backslash S$：商栈；$\mu:T^{*}S\to\mathfrak{k}^{*}$：动量映射，$\mathfrak{k}:=\operatorname{Lie}K$、$\pi_0(K)$：$K$ 的连通分支群；不变式取 $\pi_0(K)$，因为 $K$ 本身可缩或连通部分已由李代数作用吸收、$\operatorname{Nilp}:=p^{-1}(0)$：整体幂零锥；$p$：Hitchin 纤维化、迷向 / Lagrange：对光滑辛簇的子概形（或光滑代数栈的子栈）而言，切空间在辛形式下全迷向 / 再加维数等于一半

## 关键点

- 1.2.1 把「余切栈」与「哈密顿约化」等同起来：$T^{*}\mathcal{Y}=K\backslash\mu^{-1}(0)$。这不是把 $T^{*}S$ 商掉，而是先取零水平集 $\mu^{-1}(0)$ 再商 $K$（ch01.tex:83）。
- 整体截面层面，式 (8) 与式 (9) 都只取 $\pi_0(K)$-不变式：象征代数与算子代数在商栈上都由不变式给出，这解释了为什么 §1.1 的构造在商栈上仍能落地（ch01.tex:85-91）。
- $\mathcal{Y}=\operatorname{Bun}_G$ 时，$p$ 的零纤维就是整体幂零锥：$\eta$ 幂零的那些 Higgs 对。它由 Laumon [La87][La88] 引入，是 Hitchin 纤维化最奇异的纤维（ch02.tex:1238-1248）。
- 式 (38)：$\dim\operatorname{Nilp}=\dim\operatorname{Bun}_G$。总空间 $T^{*}\operatorname{Bun}_G$ 是 $2\dim\operatorname{Bun}_G$ 维，零纤维却只有一半维数——这正是「完全可积」的几何表现（ch02.tex:1251-1253）。
- 2.10.1 反过来用式 (38) 证 $\operatorname{Bun}_G$ 良：取满足 $\dim U\le 2\dim\operatorname{Bun}_G$ 的最大开子栈 $U$，由 $p^{-1}(0)\subset U$ 与 $U$ 的 $\mathbb{G}_m$-不变性得 $U=T^{*}\operatorname{Bun}_G$，于是 $\dim T^{*}\operatorname{Bun}_G\le 2\dim\operatorname{Bun}_G$，$T^{*}\operatorname{Bun}_G$ 是纯维数 $2\dim\operatorname{Bun}_G$ 的局部完全交（ch02.tex:1267-1289）。
- 2.10.2：$\operatorname{Nilp}$ 是迷向的；$g>1$ 时 Faltings–Ginzburg 证明它是 Lagrange 的，$g=0,1$ 时同样 Lagrange（见 2.10.4）。$\mathbb{G}_m$-不变的 Lagrange 子簇必是余法丛之并（ch02.tex:1298-1299、1322-1325）。
- 这条路线与 2.2.4 相互印证：(38) 不只给维数，还给 2.2.4(iii) 的平坦性与纤维纯维数，是把几何与可积系统连起来的枢纽。

## 公式

```latex
T^{*}\mathcal{Y}=K\backslash\mu^{-1}(0),\qquad \mu:T^{*}S\to\mathfrak{k}^{*},\quad \mathfrak{k}:=\operatorname{Lie}K
```
```latex
\Gamma(\mathcal{Y},P_{\mathcal{Y}})=\Gamma(S,\tilde{P}_S/I_S^{cl})^{\pi_0(K)},\qquad I_S^{cl}:=(\operatorname{Sym}\Theta_S)\mathfrak{k}
```
```latex
\Gamma(\mathcal{Y},D_{\mathcal{Y}})=\Gamma(S,\tilde{D}_S/I_S)^{\pi_0(K)},\qquad I_S:=\mathcal{D}_S\cdot\mathfrak{k}
```
```latex
\operatorname{Nilp}:=p^{-1}(0)
```
```latex
\dim\operatorname{Nilp}=\dim\operatorname{Bun}_G
```
```latex
\dim T^{*}\operatorname{Bun}_G\le 2\dim\operatorname{Bun}_G
```

## 定理

式 (38)（ch02.tex:1251-1253，p.48）：$\dim\operatorname{Nilp}=\dim\operatorname{Bun}_G$。

2.10.1（ch02.tex:1267-1289，p.48）：由式 (38) 证明 2.2.4(iii)，并证明 $\operatorname{Bun}_G$ 在 1.1.1 意义下良，$T^{*}\operatorname{Bun}_G$ 是纯维数 $2\dim\operatorname{Bun}_G$ 的局部完全交。

2.10.2（ch02.tex:1298-1299，p.49）：$\operatorname{Nilp}$ 是迷向的；$g>1$ 时是 Lagrange 的（$g=0,1$ 时见 2.10.4）。

## 常见错误

- 把 $T^{*}\mathcal{Y}=K\backslash\mu^{-1}(0)$ 理解成「$T^{*}S$ 对 $K$ 取商」：必须先取零水平集 $\mu^{-1}(0)$ 再商，只商 $T^{*}S$ 得到的是不同的对象，维数会差出 $2\dim K$。
- 把式 (8)(9) 的不变式写成对 $K$ 取不变：式子里写的是 $\pi_0(K)$，因为李代数作用已被 $I_S^{cl}$、$I_S$ 商掉，剩下的是连通分支群的作用（ch01.tex:87、91）。
- 把式 (38) 的 $\dim\operatorname{Nilp}=\dim\operatorname{Bun}_G$ 与 $\dim T^{*}\operatorname{Bun}_G=2\dim\operatorname{Bun}_G$ 混为一谈：前者是奇异零纤维的维数，后者是对总空间取的（且只在良栈时为等式，一般只是上界 $\le 2\dim\operatorname{Bun}_G$）。
- $g>1$ 的条件：2.10.2 的 Lagrange 结论在 $g>1$ 时由 Faltings–Ginzburg 给出；$g=0,1$ 要另行处理（2.10.4），引用时不能默认对一切 $g$ 成立（ch02.tex:1314-1321）。
- 把「迷向」当成「Lagrange」：迷向只要求切空间在辛形式下全迷向，Lagrange 还要求维数恰为一半；$\operatorname{Nilp}$ 的维数由式 (38) 给出，正是补上这一半的关键。

## 批注

### 背景直觉：为什么商栈的余切是哈密顿约化

对 $\mathcal{Y}=K\backslash S$，$S$ 上的函数在 $\mathcal{Y}$ 上要 $K$-不变；但余切方向里，沿 $K$ 轨道方向的对偶分量应由动量映射的零水平集来「钉住」：给定 $\mathcal{Y}$ 上的余切向量，把它提升到 $S$，只有落在 $\mu^{-1}(0)$ 上的那些才不会在 $K$ 作用后改变。这就是 $T^{*}\mathcal{Y}=K\backslash\mu^{-1}(0)$ 的来源，也是 1.1.1 末尾说「$\mathcal{Y}=K\backslash S$ 时 $T^{*}\mathcal{Y}$ 由 $T^{*}S$ 经哈密顿约化得到」的意思。

### 含糊点拨：幂零锥为什么只有一半维数

Hitchin 纤维化把 $2\dim\operatorname{Bun}_G$ 维的余切栈映到 $\dim\operatorname{Bun}_G$ 维的底；一般纤维是 $\dim\operatorname{Bun}_G$ 维的阿贝尔簇（2.2.4(iv)），而零纤维 $\operatorname{Nilp}$ 虽奇异，维数却仍是 $\dim\operatorname{Bun}_G$（式 (38)）。换句话说，零纤维不比一般纤维「大」，只是形状退化：一般纤维是环面，零纤维是幂零 Higgs 场构成的奇异簇，两者维数相同而几何不同。

### 易错预警：「整体」幂零锥的「整体」二字

$\operatorname{Nilp}$ 的「整体」不是指 $T^{*}\operatorname{Bun}_G$ 整体，而是指 $\eta$ 作为 $X$ 上整体的 Higgs 场（而非某点处的形式幂级数）逐点取值都幂零。逐点的幂零条件只涉及 $\mathfrak{g}^{*}_{\mathcal{F}}\otimes\omega_X$ 的纤维，但「对所有 $x\in X$ 同时成立」是一个整体条件，这正是它能用 Laumon 的整体构造刻画（并给出式 (38)）的原因。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §1.2.1；印刷页 [10] / PDF 页 [10]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch01.tex:83-92`
- 1.2.1 起于 p.10：`\SourcePage{10}` 在 ch01.tex:83（行内），下一处 `\SourcePage{11}` 在 ch01.tex:108，故 $T^{*}\mathcal{Y}=K\backslash\mu^{-1}(0)$ 与式 (8)(9) 都在印刷页 10，与 PDF 页 10 对应。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §2.10；印刷页 [47, 48, 49] / PDF 页 [47, 48, 49]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch02.tex:1236-1299`
- §2.10 起于 p.47（`\SourcePage{47}` 在 ch02.tex:1193）；`\SourcePage{48}` 在 ch02.tex:1248，式 (38) 与 2.10.1 在 p.48；`\SourcePage{49}` 在 ch02.tex:1291，定理 2.10.2 与注在 p.49。印刷页 = PDF 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
