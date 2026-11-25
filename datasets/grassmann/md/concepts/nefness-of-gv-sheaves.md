# $GV$-层的 nef 性

> `grassmann/concept/nefness-of-gv-sheaves` · 轨道 8 · 阿贝尔簇上的正则性 · 状态 draft

> **先自测**：为什么一个只满足上同调支集余维下界的层，反而必然是 nef 的？

## 一句话

阿贝尔簇上每个 $GV$-层都是 nef 的：先用同源归约到主极化，再把充裕性翻译成 $\mathbb Q$-扭曲层并让分母趋于无穷；这条定理把一般消没直接变成半正性。

## 定义

对 $\mathbb Q$-除子 $D$ 与凝聚层 $\mathcal F$，记 $\mathcal F\langle D\rangle:=\mathcal F\otimes\mathcal O_X(\lfloor D\rfloor)$。设 $\Theta$ 是 $X$ 上的主极化。称 $\mathcal F$ **nef**，如果对每个有理数 $\varepsilon>0$，层 $\mathcal F\langle\varepsilon\Theta\rangle$ 都是充裕的（等价地：对每个充裕除子 $A$ 与每个 $\varepsilon>0$，$\mathcal F\langle\varepsilon A\rangle$ 充裕）。定理 4.1 断言：若 $\mathcal F$ 是 $GV$-层，则 $\mathcal F$ 是 nef 的。

**记号约定**：$\langle\cdot\rangle$ 是 $\mathbb Q$-扭曲（只取整数部分，故不必要求 $D$ 为整除子）；充裕 = ample；nef 与充裕在有限同源下的拉回与下推都保持；$\phi_m\colon X\to X$ 是乘 $m$ 映射。

## 要点（为什么需要它）

- 第一步是归约：任一充裕除子 $A$ 都可写成主极化 $L$ 沿某同源 $\widehat\psi\colon\widehat X\to\widehat Y$ 的拉回，而 $GV$ 性与 nef 性都在有限同源下保持，故只需证主极化情形。
- 主极化时 $\mathcal O(-m\Theta)$ 在 $\widehat X$ 上满足 $IT_g$，其 Fourier 变换在 $X$ 上局部自由且满足 $IT_0$；于是 $\mathcal F\otimes\widehat{\mathcal O(-m\Theta)}\otimes\alpha$ 的高次上同调对一切 $\alpha$ 为零。
- 用 $\phi_m^*\widehat{\mathcal O(-m\Theta)}\cong\bigoplus_r\mathcal O(m\Theta)$ 把上式拉回，得 $\phi_m^*\mathcal F\otimes\mathcal O(m\Theta)$ 满足 $IT_0$，从而 $M$-正则，从而（Debarre）充裕。
- 因为 $\phi_m^*\Theta\equiv m^2\Theta$，充裕性沿 $\phi_m$ 下传为 $\mathcal F\langle\frac1m\Theta\rangle$ 充裕；对每个 $\varepsilon$ 取 $m>1/\varepsilon$，令 $m\to\infty$ 得 nef。
- 推论 4.2：对任意 $a\colon Y\to X$（$X$ 为阿贝尔簇），直像层 $R^ja_*\omega_Y$ 全是 nef——这是本章在圈外被引用最多的一条。

## 关键公式

$$
\mathcal F\langle D\rangle:=\mathcal F\otimes\mathcal O_X(\lfloor D\rfloor)
$$

$$
\phi_m^*\widehat{\mathcal O(-m\Theta)}\cong\bigoplus\nolimits_r\mathcal O(m\Theta)
$$

$$
\phi_m^*\Theta\equiv m^2\Theta\ \Longrightarrow\ \phi_m^*\bigl(\mathcal F\langle\tfrac1m\Theta\rangle\bigr)=\phi_m^*\mathcal F\otimes\mathcal O(m\Theta)
$$

## 定理与证明（或缺口）

### 定理 4.1（$GV$-层的 nef 性）

设 $X$ 是阿贝尔簇，$\mathcal F$ 是 $X$ 上的 $GV$-层，则 $\mathcal F$ 是 nef 的。

**证明状态：完整**

1. 归约到主极化：取同源 $\psi\colon X'\to X$ 与 $X'$ 上的主极化 $L$，使 $\psi^*A\equiv L$；由定理 2.3 与 Fourier–Mukai 变换和同源的交换性（[Muk1] 3.4），$\psi^*\mathcal F$ 仍是 $GV$。若 $\psi^*\mathcal F$ 已证 nef，则 $\mathcal F$ 也 nef。
   - *为什么*：nef 是『$\mathbb Q$-扭曲后充裕』的性质，而充裕与 nef 在有限同源下可上下来回。
2. 主极化情形：$\mathcal O(-m\Theta)$ 在 $\widehat X$ 上满足 $IT_g$，故由定理 2.3 与命题 3.1，对 $m\gg0$ 与任意 $\alpha$ 有 $H^i\bigl(\mathcal F\otimes\widehat{\mathcal O(-m\Theta)}\otimes\alpha\bigr)=0\ (i>0)$；再用 $\phi_m^*\widehat{\mathcal O(-m\Theta)}\cong\bigoplus_r\mathcal O(m\Theta)$ 得 $\phi_m^*\mathcal F\otimes\mathcal O(m\Theta)$ 满足 $IT_0$，故 $M$-正则，故（Debarre [De2] Cor 3.2）充裕。
   - *为什么*：$IT_0$ 是 $M$-正则的最强形式（所有 $V^i$ 都空），Debarre 的定理把 $IT_0$ 提升为充裕。
3. 由 $\phi_m^*\Theta\equiv m^2\Theta$ 得 $\phi_m^*(\mathcal F\langle\frac1m\Theta\rangle)=\phi_m^*\mathcal F\otimes\mathcal O(m\Theta)$ 充裕；$\phi_m$ 有限平坦，迹映射 $\operatorname{tr}\colon\phi_{m*}\mathcal O\to\mathcal O$ 分裂，故充裕性可下传，$\mathcal F\langle\frac1m\Theta\rangle$ 充裕。对每个 $\varepsilon>0$ 取 $m>1/\varepsilon$，令 $m\to\infty$ 得 nef。
   - *为什么*：$\frac1m\Theta\le\varepsilon\Theta$ 对 $m>1/\varepsilon$ 成立，而 nef 只要求任意小的 $\varepsilon$ 扭曲都充裕。


出处：中译 p.140，定理 4.1 与推论 4.2（chapters/ch08.tex:223）

## 易错点

- 别把 $[g]$ 读成张量因子：原文把移位写成 $\mathbf R\widehat{\mathcal S}(\mathbf R\Delta\mathcal F)[g]$，$[g]$ 是整个复形的移位；真正起作用的是 $GV$ 给出的 $\dim\operatorname{Supp}R^k\widehat{\mathcal S}\mathcal F\le g-k$。
- $\mathcal O(-m\Theta)$ 在主极化下满足的是 $IT_g$ 而不是 $IT_0$：它只有一个非零上同调群，位置在第 $g$ 次，所以变换回来时要在 $X$ 上先取一次移位。
- 充裕性沿有限态射下传要挟迹映射的分裂（笔记补 2），不能对一般满射断言；这正是 §4 必须走同源而不是任意满射的原因。

## 相关卡

- [$GV$-层](../concepts/gv-sheaf.md)
- [$M$-正则层](../concepts/m-regular-sheaf.md)
- [连续整体生成](../concepts/continuously-globally-generated.md)

## 出处

- ch8 §4 $GV$-层的 nef 性；中译 p.140（英文 PDF p.156），源码 `chapters/ch08.tex:223`
