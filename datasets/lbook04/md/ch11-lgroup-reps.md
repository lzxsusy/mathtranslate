# L 群的表示与一般 $G$ 的 Langlands 猜想

> `lbook04/concept/ch11-lgroup-reps` · 轨 G GL_n 的 Langlands 纲领 · 状态 reviewed · 核验 source-only

**问题：** 为什么同一个 $L$ 包里的所有表示无法用 $L$ 函数区分？

**一句话：** 一般 $G$ 的局部猜想用容许同态 $\phi:W'_k\to{}^LG$ 参数化 $L$ 包；取 $r:{}^LG\to\mathrm{GL}_n(\mathbb{C})$ 便有 $L(s,\pi,r)=L(s,r\circ\phi)$，整体逐位点相乘，只有 $\mathrm{GL}_n$ 有完整理论。

**别名：** `L 函数 L(s,π,r)`、`容许同态`、`L 包`、`局部 Langlands 猜想`、`部分 L 函数`

## 定义

对一般约化群 $G$，局部 Langlands 猜想的 Galois 侧是容许同态 $\phi:W'_k\to{}^LG$，满足 (i) 在 $\mathcal{G}_k$ 上方块交换；(ii) 连续，$\phi(\mathbb{G}_a)$ 幂幺，半单映半单；(iii) 若 $\phi(W'_k)$ 落在真抛物子群的 Levi 中，则该抛物子群相干。模去 ${}^LG^0$ 的内自同构得 $\Phi(G)$。猜想说存在满射 $\mathcal{A}(G)\to\Phi(G)$，纤维有限（即 $L$ 包 $\mathcal{A}_\phi$），并满足五条性质：中心特征 $=\omega_\phi$；扭相容；模中心平方可积当且仅当 $\phi(W'_k)$ 不含于真 Levi；缓增当且仅当 $\phi(W_k)$ 有界；与 $\eta:H\to G$ 相容。$L$ 函数需要 $r:{}^LG\to\mathrm{GL}_n(\mathbb{C})$（连续、在 ${}^LG^0$ 上复解析），定义 2.1 置 $L(s,\pi,r)=L(s,r\circ\phi)$、$\varepsilon$ 同理。整体则用 $\mathcal{L}_k$ 代替 $W'_k$，定义 2.2 把局部因子相乘；几乎处处 $\varepsilon=1$、$L$ 因子次数由 $\dim r$ 界定，故乘积有意义；完整 $L$ 函数需要所有位点的局部 LL，只有 $\mathrm{GL}_n$ 已知，一般 $G$ 只能先谈部分 $L$ 函数 $L^S$。

**记号：** $W'_k$：局部 Weil–Deligne 群（阿基米德处取 $W_k$）；$\Phi(G)$：容许同态模内自同构之集；$\mathcal{A}_\phi(G)$：$L$ 包；$\omega_\phi$：中心特征；$r:{}^LG\to\mathrm{GL}_n(\mathbb{C})$：$L$ 群的表示；$\iota_v:{}^LG_v\to{}^LG$：局部–整体嵌入。

## 要点

- 容许同态的三条件是逐字可查的定义：方块交换；$\phi(\mathbb{G}_a)$ 幂幺且半单映半单；真 Levi 的相干性。
- $L$ 包内所有 $\pi$ 共享同一个 $\phi$，因此 $L(s,\pi,r)$ 与 $\varepsilon(s,\pi,r)$ 在包内不可区分——这正是「$L$ 包」得名的原因。
- $r$ 不必是嵌入：Jiang–Soudry 用 $r:\mathrm{Sp}_{2n}(\mathbb{C})\hookrightarrow\mathrm{GL}_{2n}(\mathbb{C})$ 把 $\mathrm{SO}_{2n+1}$ 的 $L$ 函数写成 $\mathrm{GL}_{2n}$ 的 Rankin–Selberg 因子。
- 部分 $L$ 函数 $L^S$ 总有定义（Langlands 已证其 Euler 乘积在半平面绝对收敛），逆定理只需在 $L^S$ 上操作。

## 公式

$$
\phi:W'_k\to{}^LG,\qquad \mathcal{A}(G)=\bigsqcup_{\phi\in\Phi(G)}\mathcal{A}_\phi(G)
$$

$$
L(s,\pi,r)=L(s,r\circ\phi),\qquad \varepsilon(s,\pi,r,\psi)=\varepsilon(s,r\circ\phi,\psi)
$$

$$
L(s,\pi,r)=\prod_v L(s,r\circ\iota_v\circ\phi_v)
$$

## 定理与证明

**局部 Langlands 猜想（一般 $G$）**　存在满射 $\mathcal{A}(G)\to\Phi(G)$，纤维有限，并满足中心特征、扭相容、平方可积、缓增、与 $\eta:H\to G$ 相容五条性质。

*出处：译文 §2.1*

**定义 2.1 / 2.2（$L$ 函数）**　$L(s,\pi,r)=L(s,r\circ\phi)$；整体 $L(s,\pi,r)=\prod_v L(s,r\circ\iota_v\circ\phi_v)$，$\varepsilon$ 同理。

*出处：译文 §2.1–2.2*

## 易错点

- 把 $\Phi$ 当根系：§1 的 $\Phi(G,T)$ 是根系，§2 起 $\Phi(G)$ 是容许同态集；原书 p. 254 明说这是两个东西。
- 以为 $\phi$ 落在真 Levi 仍可平方可积：条件 (iii) 的相干性正是排除这种 $\phi$。
- 把 $r\circ\phi$ 与 $\phi$ 混用：$L$ 函数依赖 $r$ 的选择，换 $r$ 就换 $L$ 函数（这正是函子性的入口）。

## 批注

**〔含糊点拨〕为什么用容许同态而不是同态**　$W'_k$ 不是复 Lie 群，$\phi$ 的「代数性」必须用幂幺与半单性来代替；条件 (ii) 就是把「复解析」翻译成 $W'_k$ 的语言。§2.1 的译注解释了这一点，并强调 (iii) 用 $W'_k$、(iv) 用 $W_k$，不可统一。

## 相关

[[ch11-dual-group]]、[[ch11-functoriality]]、[[ch10-local-langlands]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§2，原书 pp. 254–257（PDF pp. 256–259）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch11.tex:187-393`
