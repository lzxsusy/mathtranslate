# 坍缩的首项渐近：$X_q^{new}$ 逼近 $\varepsilon$-环面丛

`kshms/concept/conj-02-collapse-ma-model` · track A（CFT 与几何退化） · 原文 猜想 2

**问题**　坍缩族 $X_q^{new}$ 在 $q\to0$ 时不只是一个度量极限，它的「首项渐近」能否就是某个具体的 Ricci 平坦环面丛族？

**摘要**　猜想 1 的加强版：存在 $C>0$ 与扭 $t(q)$，使 $X_q^{new}$ 在切空间层面按 $o(1)$ 逼近环面丛 $X^{\varepsilon(q),t(q)}$（$\varepsilon(q)=C(\log|q|)^{-1}$），并整体收敛到配对 $(\bar Y,Y^{sing})$。

**别名**　Conjecture 2；leading asymptotic of the collapsed family；$q=e^{-1/\varepsilon}$ 与环面丛族的比较

## 陈述

设 $(\mathcal{X}_{mer},vol)=(X_q,vol_q)$ 是一族单参数极大退化 Calabi–Yau 流形，$X_q^{new}$ 是如前重新标度度量之后所得的族。则存在常数 $C>0$ 与函数 $t(q)$，使得凯勒流形 $X_q^{new}$ 与 $X^{\varepsilon(q),t(q)}$（其中 $\varepsilon(q)=C(\log|q|)^{-1}$）在 $q\to0$ 时按如下意义互相接近：

对任意 $\delta>0$，存在分解 $X_q=X_q^{sm}\sqcup X_q^{sing}$ 与光滑流形的嵌入
$$j_q:X_q\to p_{\varepsilon(q),t(q)}^{-1}\bigl(Y\setminus(Y^{sing})^{\delta}\bigr),$$
其中 $(Y^{sing})^{\delta}$ 是 $Y^{sing}$ 的 $\delta$-邻域，使得：

a) $(X_q,X_q^{sing})$ 在 Gromov–Hausdorff 度量下收敛到配对 $(\bar Y,Y^{sing})$。

b) $j_q$ 把切空间 $T_xX_q$ 与 $T_{j_q(x)}X^{\varepsilon(q),t(q)}$ 上的内积与复结构等同起来，误差为 $o(1)$，且对 $x\in X_q^{sm}$ 一致。

## 记号

$X^\varepsilon$：纤维为 $T_{Y,y}/\varepsilon T^{\mathbb{Z}}_{Y,y}$ 的环面丛 $p_\varepsilon:X^\varepsilon\to Y$ 的全空间，带复结构 $J_{X^\varepsilon}$ 与 Ricci 平坦凯勒度量；$X^{\varepsilon,t}$：由 $t\in H^1\bigl(Y,(T_Y/T^{\mathbb{Z}}_Y)_{discr}\bigr)$ 扭出的扭流形；$\varepsilon(q)=C(\log|q|)^{-1}$；$q=e^{-1/\varepsilon}$。

## 要点

- 这是猜想，不是定理：原文先说「粗略地说，下一个猜想断言」，再说「更精确地说，我们把它表述如下」；a)、b) 之外没有证明。
- 它与猜想 1 的关系是加强：猜想 1 只说 GH 极限存在且光滑部分是 Monge–Ampère 流形，猜想 2 进一步指定极限族就是由 $(Y,g_Y,\nabla)$ 造出的 $\varepsilon$-环面丛族，精确到扭 $t(q)$。
- 两条接近方式不同：a) 是整体度量收敛（配对 $(\bar Y,Y^{sing})$），b) 是逐点一阶接近（内积与复结构，误差 $o(1)$ 且对 $x\in X_q^{sm}$ 一致），二者不能互相替代。
- 尺度匹配 $\varepsilon(q)=C(\log|q|)^{-1}$ 把退化的对数尺度翻成纤维尺度：纤维体积 $\sim\varepsilon^n$，与体积渐近中的 $(\log|q|)^{n}$ 因子对偶。
- 嵌入 $j_q$ 的目标挖掉了 $(Y^{sing})^{\delta}$，$\delta>0$ 任意小但固定：奇点邻域不在比较范围内，这与猜想 1 中 $Y^{sing}$ 至少余维 $2$ 相呼应。

## 公式

$$\varepsilon(q)=C(\log|q|)^{-1},\qquad q=e^{-1/\varepsilon}$$

$$j_q:X_q\to p_{\varepsilon(q),t(q)}^{-1}\bigl(Y\setminus(Y^{sing})^{\delta}\bigr)$$

$$T_xX_q\ \cong\ T_{j_q(x)}X^{\varepsilon(q),t(q)}\quad(\mathrm{误差}\ o(1))$$

## 易错点

- 这是猜想，不是定理：原文在给出 a)、b) 之前明说「粗略地说」；后文只在复阿贝尔簇情形验证（注 5、§8 定理 4）。
- b) 说的是切空间上内积与复结构相差 $o(1)$，既不是 $C^0$ 意义下的度量接近，也不是等距；把它读成「$X_q$ 与 $X^\varepsilon$ 等距」会过强。
- 扭 $t(q)$ 不能省：$X^{\varepsilon,t}$ 只在 $t=0$ 时等于 $X^\varepsilon$，而 $t$ 一般随 $q$ 变化；忽略它陈述就不成立。
- 比较只对 $x\in X_q^{sm}$ 一致成立，$X_q^{sing}$ 上的行为不在 b) 的范围内（a) 只给出集合层面的收敛）。

## 相关卡

- `kshms/concept/conj-01-collapse-gh-limit`
- `kshms/concept/dfn-01-maximal-degeneration`
- `kshms/concept/dfn-02-monge-ampere-manifold`
- `kshms/remark/rmk-05-gross-wilson-k3`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §3.1（原文 p.16）；锚点 `源码/chunks/ch03.tex:160-177（猜想 2）`

> 原文 p16 §3.1；译本 p16；其前的 p16 段构造了环面丛 $X^\varepsilon\to Y$ 与扭流形 $X^{\varepsilon,t}$，为猜想提供比较对象。
