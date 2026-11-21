# GL_n-oper：完全滤链与无处为零象征的 n 阶算子

- **id**：`bdh/concept/gln-oper-complete-filtration`
- **类型**：concept
- **位置**：§3.1
- **问题**：为什么一条「完全滤链 + 联络把每一片推进下一片」的数据，会与一个象征处处非零的 $n$ 阶微分算子完全等价？

> $\mathrm{GL}_n$-oper 是带联络的 $\mathcal O_X$-模 $\mathcal E$ 连同完全滤链 $\mathcal E=\mathcal E_n\supset\cdots\supset\mathcal E_0=0$，使各 $\operatorname{gr}_i\mathcal E$ 可逆、$\nabla(\mathcal E_i)\subset\mathcal E_{i+1}\otimes\omega_X$ 且相邻分次片间为同构。

## 定义

$\mathrm{GL}_n$-oper 可以看作 $\mathcal O_X$-模 $\mathcal E$，带联络 $\nabla:\mathcal E\to\mathcal E\otimes\omega_X$ 与滤链 $\mathcal E=\mathcal E_n\supset\mathcal E_{n-1}\supset\cdots\supset\mathcal E_0=0$，使得：(i) 层 $\operatorname{gr}_i\mathcal E=\mathcal E_i/\mathcal E_{i-1}$（$n\ge i\ge1$）可逆；(ii) $\nabla(\mathcal E_i)\subset\mathcal E_{i+1}\otimes\omega_X$，且对 $n-1\ge i\ge1$，由 $\nabla$ 诱导的态射 $\operatorname{gr}_i\mathcal E\to\operatorname{gr}_{i+1}\mathcal E\otimes\omega_X$ 是同构。条件 (i) 就是「完全」：每片商都是线丛，故 $\mathcal E$ 秩 $n$、滤链长 $n$。反过来，设 $\mathcal A,\mathcal B$ 是可逆 $\mathcal O_X$-模，$\partial:\mathcal A\to\mathcal B$ 是 $n$ 阶微分算子，其象征 $\sigma(\partial)\in\Gamma(X,\mathcal B\otimes\mathcal A^{\otimes(-1)}\otimes\Theta_X^{\otimes n})$ 无处为零。把 $\partial$ 看作 $\mathcal B\otimes\mathcal D_X\otimes\mathcal A^{\otimes(-1)}$ 的截面，令 $I\subset\mathcal D_X\otimes\mathcal A^{\otimes(-1)}$ 为其像生成的 $\mathcal D_X$-子模，$\mathcal E:=\mathcal D_X\otimes\mathcal A^{\otimes(-1)}/I$，$\mathcal E_i$ 为算子阶滤链诱导的滤链，则 $(\mathcal E,\{\mathcal E_i\},\nabla)$ 是 $\mathrm{GL}_n$-oper。这一构造给出 $\mathrm{GL}_n$-oper 的群胚与数据 $\partial:\mathcal A\to\mathcal B$ 的群胚之间的等价；逆函子把 $(\mathcal E,\{\mathcal E_i\},\nabla)$ 送到算子 $\partial:\mathcal A\to\mathcal B$，其中 $\mathcal A:=\mathcal E_1^{\otimes(-1)}$、$\mathcal B:=\omega_X\otimes(\mathcal E/\mathcal E_{n-1})^{\otimes(-1)}$。取 $n=2$ 并加自伴条件即得 Sturm–Liouville 算子，此时 $\mathcal A$ 自动是 $\omega_X^{\otimes(-1)}$ 的平方根。

**记号**：$\mathcal E_i$：滤链的第 $i$ 片（$\mathcal E_n=\mathcal E$，$\mathcal E_0=0$）；$\operatorname{gr}_i\mathcal E=\mathcal E_i/\mathcal E_{i-1}$、$\mathcal D_X$：$X$ 上的微分算子层；$\mathcal D_X^{(k)}$：阶数 $\le k$ 的算子子层、$\sigma(\partial)$：$n$ 阶算子 $\partial$ 的象征，取值于 $\mathcal B\otimes\mathcal A^{\otimes(-1)}\otimes\Theta_X^{\otimes n}$、$\Theta_X$：切层，$\Theta_X\cong\omega_X^{\otimes(-1)}$、$\omega_X$：典范丛；$\Theta_X^{\otimes n}\cong\omega_X^{\otimes(-n)}$，故象征无处为零等价于 $\mathcal B\cong\mathcal A\otimes\omega_X^{\otimes n}$

## 关键点

- 条件 (i) 是「完全」两字的全部内容：$\operatorname{gr}_i\mathcal E$ 都是可逆层，于是 $\mathcal E_i$ 的秩逐片加一，滤链无法再细分也无法缩短；等价地 $\mathcal E$ 由 $n$ 条线丛按 $\omega_X$ 的幂次逐级粘成。
- 条件 (ii) 的指标 $i=n$ 是平凡的（它只说 $\nabla$ 保持 $\mathcal E=\mathcal E_n$），实质内容是 $1\le i\le n-1$：联络把第 $i$ 片推进第 $i+1$ 片，且相邻分次片之间的诱导映射是同构，这使 $\mathcal E_1$ 与 $\mathcal E/\mathcal E_{n-1}$ 通过 $\omega_X^{\otimes(n-1)}$ 相互决定。
- 该定义与「$n$ 阶算子」一一对应：正向由 $\partial\mapsto\mathcal D_X\otimes\mathcal A^{\otimes(-1)}/I$ 给出，逆向由 $\mathcal A=\mathcal E_1^{\otimes(-1)}$、$\mathcal B=\omega_X\otimes(\mathcal E/\mathcal E_{n-1})^{\otimes(-1)}$ 给出；两个方向都保持群胚（同构意义下）。
- 象征无处为零正是条件 (ii) 的算子版：$\sigma(\partial)$ 是 $\mathcal B\otimes\mathcal A^{\otimes(-1)}\otimes\omega_X^{\otimes(-n)}$ 的处处非零截面，故 $\mathcal B\cong\mathcal A\otimes\omega_X^{\otimes n}$；反过来这一同构保证各 $\operatorname{gr}_i\mathcal E\to\operatorname{gr}_{i+1}\mathcal E\otimes\omega_X$ 是同构。
- $\mathrm{SL}_2$ 情形：oper 等价于 Sturm–Liouville 算子（象征非零的自伴二阶算子）。带同构 $\mathcal M^{\otimes2}\cong\mathcal O_X$ 的线丛 $\mathcal M$ 有典范联络，用 $\mathcal M$ 扭得到等价类；自然映射 $\operatorname{Op}_{\mathrm{SL}_2}(X)\to\operatorname{Op}_{\mathfrak{sl}_2}(X)$ 把这些等价类与 $\operatorname{Op}_{\mathfrak{sl}_2}(X)$ 等同（§3.1.7 又说 $\operatorname{Op}_{\mathfrak{sl}_2}$ 是 $\omega_X^{\otimes2}$-torsor）。

## 公式

```latex
\mathcal{E}=\mathcal{E}_n\supset\mathcal{E}_{n-1}\supset\cdots\supset\mathcal{E}_0=0,\qquad \operatorname{gr}_i\mathcal{E}=\mathcal{E}_i/\mathcal{E}_{i-1}
```
```latex
\nabla(\mathcal{E}_i)\subset\mathcal{E}_{i+1}\otimes\omega_X,\qquad \operatorname{gr}_i\mathcal{E}\xrightarrow{\ \sim\ }\operatorname{gr}_{i+1}\mathcal{E}\otimes\omega_X\quad(n-1\ge i\ge1)
```
```latex
\sigma(\partial)\in\Gamma(X,\mathcal{B}\otimes\mathcal{A}^{\otimes(-1)}\otimes\Theta_X^{\otimes n})
```
```latex
\mathcal{E}:=\mathcal{D}_X\otimes\mathcal{A}^{\otimes(-1)}/I,\qquad \mathcal{A}:=\mathcal{E}_1^{\otimes(-1)},\qquad \mathcal{B}:=\omega_X\otimes(\mathcal{E}/\mathcal{E}_{n-1})^{\otimes(-1)}
```

## 常见错误

- 把滤链方向写反：原文是降链 $\mathcal E=\mathcal E_n\supset\cdots\supset\mathcal E_0=0$，$\mathcal E_1$ 是最小非零片。若把 $\mathcal E_1$ 当成最大片，逆函子的 $\mathcal A=\mathcal E_1^{\otimes(-1)}$ 与 $\mathcal B=\omega_X\otimes(\mathcal E/\mathcal E_{n-1})^{\otimes(-1)}$ 就会同时取错，$n$ 阶算子会退化成 $1$ 阶。
- 把 $\nabla(\mathcal E_i)\subset\mathcal E_{i+1}\otimes\omega_X$ 误读为「$\nabla$ 保持滤链」：它恰恰把每一片推进下一片（shift by one），这是 oper 型横截性；写成 $\nabla(\mathcal E_i)\subset\mathcal E_i\otimes\omega_X$ 就只剩「带旗的平坦丛」，与 §3.1.6 的算子对应完全断裂。
- 把 $\mathrm{SL}_2$-oper 与 $\mathfrak{sl}_2$-oper 当成同一集合：二者差一个 $\mathcal M$（$\mathcal M^{\otimes2}\cong\mathcal O_X$）的扭，$\operatorname{Op}_{\mathrm{SL}_2}(X)\to\operatorname{Op}_{\mathfrak{sl}_2}(X)$ 只把等价类等同；且 $\operatorname{Op}_{\mathfrak{sl}_2}$ 是 $\omega_X^{\otimes2}$-torsor（§3.1.7），不是集合。
- 以为任意完全滤链都给出 oper：还必须满足相邻分次片同构，这一条等价于象征非零。只有滤链而无同构，得到的 $\partial$ 象征可能有零点，不再是 $n$ 阶椭圆型（处处非零主部）的算子。

## 批注

### 易错预警：象征的这一格决定 A 与 B 的关系

$\Theta_X^{\otimes n}\cong\omega_X^{\otimes(-n)}$，故 $\sigma(\partial)\in\Gamma(X,\mathcal B\otimes\mathcal A^{\otimes(-1)}\otimes\omega_X^{\otimes(-n)})$。「无处为零」意味着这个线丛被平凡化，即 $\mathcal B\cong\mathcal A\otimes\omega_X^{\otimes n}$。代入 $\mathrm{SL}_2$ 的 $n=2$、$\mathcal B=\omega_X\otimes\mathcal A^{\otimes(-1)}$，立刻得到 $\mathcal A^{\otimes2}\cong\omega_X^{\otimes(-1)}$——这正是源码 §3.1.6 末「$\mathcal A$ 自动是 $\omega_X^{\otimes(-1)}$ 的平方根」的算法来源，漏掉 $\Theta_X$ 与 $\omega_X$ 的换算就推不出来。

### 含糊点拨：A、B 不是独立的两条线丛

逆函子取 $\mathcal A=\mathcal E_1^{\otimes(-1)}$、$\mathcal B=\omega_X\otimes(\mathcal E/\mathcal E_{n-1})^{\otimes(-1)}$，看似两个独立选择，其实中间由相邻同构串联：$\operatorname{gr}_i\mathcal E\xrightarrow{\sim}\operatorname{gr}_{i+1}\mathcal E\otimes\omega_X$ 逐级迭代给出 $\mathcal E_1\xrightarrow{\sim}(\mathcal E/\mathcal E_{n-1})\otimes\omega_X^{\otimes(n-1)}$。源码在推导 $\partial$ 时正是用这个同构把 $\omega_X^{\otimes(-n)}\otimes\mathcal E_1$ 改写成 $\mathcal B^{\otimes(-1)}$，从而把正合列的分裂读成算子。

### 背景直觉：为什么「完全」二字必须保留

若只要求滤链的商是凝聚层而非线丛，$\mathcal E$ 的秩就不会逐片加一，$\mathcal D_X^{(n-1)}\otimes\mathcal E_1\to\mathcal E$ 也不再是同构，$\partial$ 的阶数便无从定义。完全性保证 $\mathcal E$ 恰由 $n$ 条线丛堆成，使 $\operatorname{gr}$ 的每一片正好是一维权空间——这与 §3.1.1 的 $\operatorname{gr}^{-1}\mathfrak g=\bigoplus\mathfrak g^{\alpha}$ 是同一现象在 $\mathrm{GL}_n$ 上的显式化：oper 就是「滤链每片掉一维」的联络。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §3.1.6；印刷页 [62, 63] / PDF 页 [62, 63]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch03.tex:43-58`
- 定义与 (i)(ii) 在 p.62，算子的构造跨到 p.63；本书 PDF 页 = 印刷页。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
