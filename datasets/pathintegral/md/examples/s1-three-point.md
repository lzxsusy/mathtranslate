# $S^1$ 上的三点关联

> `pi/example/s1-three-point` · 轨道 E · 微扰与代数结构 · 状态 draft

> **这张卡练什么**：三个因子、两对收缩时，为什么 $\hbar^2$ 项恰好消失而 $\hbar$ 一次项的系数是 $\frac16$？

## 一句话

三点关联 $\langle x\otimes xp\otimes p\rangle$：三项一阶收缩合成 $\frac{\mathrm{i}\hbar}{6}xp$，二阶项被反号对称性消掉，结果是 $x^2p^2+\frac{\mathrm{i}\hbar}{6}xp$。

## 设定

取 $f_0=x$、$f_1=xp$、$f_2=p\in A=\mathbb{R}[x,p]$。按定义 2.8.12（$m=2$）写三点关联：$\langle f_0\otimes f_1\otimes f_2\rangle_{S^1}=2!\int_{\mathrm{Cyc}_3(S^1)}\mathrm{d}\theta_0\mathrm{d}\theta_1\mathrm{d}\theta_2\,\bigl\langle f_0(\theta_0)f_1(\theta_1)f_2(\theta_2)\bigr\rangle$，其中期望按威克定理展开：每个 $\mathrm{i}\hbar G_{ij}$ 把第 $i$ 槽的 $\partial_x$ 与第 $j$ 槽的 $\partial_p$ 配成一对（$G_{ij}=G(\theta_i,\theta_j)$，$i=j$ 时为零）。

## 计算

**第 1 步**：按威克定理，一阶项来自三种配对 $(0,1)$、$(1,2)$、$(0,2)$；对 $f_0=x$、$f_1=xp$、$f_2=p$，每种配对都消掉两个导数、剩下一个 $xp$：$(0,1)$ 给 $(\partial_x x)(\partial_p xp)\cdot p=xp$，$(1,2)$ 给 $x\cdot(\partial_x xp)(\partial_p p)=xp$，$(0,2)$ 给 $(\partial_x x)\cdot xp\cdot(\partial_p p)=xp$。

> 为什么：三个因子各含一个 $x$ 或 $p$，一阶收缩只能落在两个因子上，剩下的那个因子提供另一个字母——三项都恰好合成 $xp$，这就是它们能并成一项的原因。

**第 2 步**：一阶总和为 $2!(\mathrm{i}\hbar)\int_{\mathrm{Cyc}_3}(G_{01}+G_{12}+G_{02})\,xp$；取规范序 $(\theta_0,\theta_1,\theta_2)=(1,\theta_1,\theta_2)$，$\mathrm{Cyc}_3$ 上的积分为 $\int_{1\ge\theta_1\ge\theta_2\ge0}\mathrm{d}\theta_1\mathrm{d}\theta_2$。

> 为什么：循环序区域的标准形是把 $\theta_0$ 钉在 $1$；$2!$ 来自定义 2.8.12 的归一化，不是配对重数。

**第 3 步**：用 $g$ 的周期性与命题 2.8.11：$G_{01}=g(\theta_1-1)=g(\theta_1)=\theta_1-\frac12$；$G_{12}=g(\theta_2-\theta_1)=\frac12-(\theta_1-\theta_2)$（因 $\theta_2-\theta_1<0$）；$G_{02}=g(\theta_2-1)=\theta_2-\frac12$。三者相加 $=2\theta_2-\frac12$。

> 为什么：$\theta_2-\theta_1$ 落在 $(-1,0)$，必须用周期的另一段 $g(\theta)=\theta+\frac12$ 来读，写成 $\frac12-(\theta_1-\theta_2)$ 才与书上一致；相加后 $\theta_1$ 消掉，只剩对 $\theta_2$ 的单变量积分。

**第 4 步**：算一阶积分：$\int_{1\ge\theta_1\ge\theta_2\ge0}(2\theta_2-\frac12)\mathrm{d}\theta_1\mathrm{d}\theta_2=\int_0^1(1-\theta_2)(2\theta_2-\frac12)\mathrm{d}\theta_2=\frac1{12}$，故贡献 $2\mathrm{i}\hbar\cdot\frac1{12}xp=\frac{\mathrm{i}\hbar}{6}xp$。

> 为什么：内层对 $\theta_1$ 的积分长度是 $1-\theta_2$；$\int_0^1(2\theta_2-\frac12-2\theta_2^2+\frac{\theta_2}{2})\mathrm{d}\theta_2=1-\frac12-\frac23+\frac14=\frac1{12}$。

**第 5 步**：二阶项：两个 $\mathrm{i}\hbar G$ 的配对中只有 $(0,1)$ 与 $(1,2)$ 的组合非零（$\partial_p$ 与 $\partial_x$ 必须落在相邻槽上），积分 $\int_0^1(\theta_1-\frac12)\bigl(\frac{\theta_1}{2}-\frac{\theta_1^2}{2}\bigr)\mathrm{d}\theta_1=0$，故 $\hbar^2$ 项消失。

> 为什么：被积函数是「关于 $\theta_1=\frac12$ 反号的因子」乘「关于 $\theta_1=\frac12$ 对称的因子」，整段积分为零；这一步不做，就会凭空多出一个 $\hbar^2$ 修正。

## 结果

$\langle x\otimes xp\otimes p\rangle_{S^1}=x^2p^2+\frac{\mathrm{i}\hbar}{6}xp$（书中结果一致）。

## 复核

① 一阶积分复算：$\int_0^1(1-\theta)(2\theta-\frac12)\mathrm{d}\theta=\int_0^1(-2\theta^2+\frac52\theta-\frac12)\mathrm{d}\theta=-\frac23+\frac54-\frac12=\frac1{12}$ ✓。② 二阶积分复算：被积式 $=\frac12(\theta-\frac12)\theta(1-\theta)$ 关于 $\theta=\frac12$ 反号，积分为零 ✓。③ 循环对称：把 $1$ 换到另一槽重算，一阶括号变为 $2\theta_1-2\theta_2-\frac12$，其三角形积分 $\int_0^1(\theta_1^2-\frac{\theta_1}{2})\mathrm{d}\theta_1=\frac1{12}$，与前面一致，说明关联在循环置换下不变 ✓。④ $\hbar\to0$ 回到 $x^2p^2$，与定义 2.8.12 的经典极限一致。

## 易错点

- 不要漏 $2!$：$m=2$ 时定义 2.8.12 的归一化因子是 $2!$，它把「三种配对」之外的重数一次算进，漏掉会得到 $\frac{\mathrm{i}\hbar}{12}xp$。
- $G_{12}=g(\theta_2-\theta_1)$ 里的宗量是负的，必须用 $g(\theta)=\theta+\frac12$（$\theta\in(-1,0)$）那一段；误写成 $\theta_2-\theta_1-\frac12$ 会把三项和算成别的值。
- 二阶项不是「天然为零」：它由被积函数的反号对称性消掉，换一个关联或换一种规范序时可能不为零，必须逐项验算。

## 用到哪些概念

- [$S^1$ 上的传播子与关联函数](../concepts/s1-correlators.md)
- [威克定理与高斯矩的配对](../concepts/wick-theorem.md)

## 相关卡

- [$S^1$ 上的两点关联](../examples/s1-two-point.md)

## 出处

- §2.8.4 例 2.8.14（三点关联），p.155（PDF p.156），源码 `ch02c.tex:1025-1044`
