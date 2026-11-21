# Pfaffian 线丛：det RΓ 的 (Z/2)-分次平方根

- **id**：`bdh/concept/pfaffian-line-bundle`
- **类型**：concept
- **位置**：§4.2
- **问题**：为什么 $\det R\Gamma(X,\mathcal Q)$ 有一个「典范的」平方根 $\operatorname{Pf}(\mathcal Q)$，而朴素的 $\det H^0(X,\mathcal Q)$ 却不能充当这个平方根？

> 对带非退化对称配对 $\mathcal Q\otimes\mathcal Q\to\omega_X$ 的 $\omega$-正交丛，Pfaffian 线丛 $\operatorname{Pf}(\mathcal Q)$ 是 $\det R\Gamma(X,\mathcal Q)$ 的 $(\mathbb Z/2)$-分次平方根，经 Lagrange 三元组上的 Clifford 模显式定义。

## 定义

§4.2 的约定：对 $(\mathbb Z/2)$-分次向量空间 $A,B$，$A\otimes B$ 与 $B\otimes A$ 的等同由 $a\otimes b\mapsto(-1)^{p(a)p(b)}b\otimes a$ 定义；对有限维 $V$，$\det V$ 看作次数为 $\dim V\bmod2$ 的 $(\mathbb Z/2)$-分次空间。设 $X$ 是 $\mathbb C$ 上的光滑完备曲线。$X$ 上的 \emph{$\omega$-正交丛}指带非退化对称配对 $\mathcal Q\otimes\mathcal Q\to\omega_X$ 的向量丛，记 $\omega\text{-Ort}$ 为其栈；其上有线丛 $\det R\Gamma$（纤维为 $\det R\Gamma(X,\mathcal Q)$）。Laszlo 与 Sorger 在 $\omega\text{-Ort}$ 上构造了 $(\mathbb Z/2)$-分次线丛（他们称为 \emph{Pfaffian}，首现译「Pfaffian（普法夫式）」），并证明其张量平方是 $\det R\Gamma$；本书改用另一个更方便的定义，源码明言「它当然应该与 [La-So] 中的定义等价，但我们没有验证这一点」。本书的构造：在 $\omega\text{-Ort}$ 上造线丛 $\operatorname{Pf}$，纤维记 $\operatorname{Pf}(\mathcal Q)$；$-1\in\operatorname{Aut}\mathcal Q$ 在纤维上的作用给出 $(\mathbb Z/2)$-分次，即存在局部常值函数 $p:\omega\text{-Ort}\to\mathbb Z/2$ 使 $\operatorname{Pf}(\mathcal Q)$ 的次数为 $p(\mathcal Q)$；实际上 $p(\mathcal Q)=\dim H^0(\mathcal Q)\bmod2$（局部常值性由 Atiyah 与 Mumford 证明）。对 $\omega$-正交丛 $\mathcal Q$，记 $\mathcal Q^-$ 为同一丛配反向配对，$\operatorname{Pf}^-(\mathcal Q):=\operatorname{Pf}(\mathcal Q^-)$。乘 $i=\sqrt{-1}$ 的同构 $\varphi_i:\mathcal Q\xrightarrow{\sim}\mathcal Q^-$ 给出 $f_{\pm i}:=(\varphi_{\pm i})_*:\operatorname{Pf}(\mathcal Q)\xrightarrow{\sim}\operatorname{Pf}(\mathcal Q^-)$；借 $f_{\pm i}$ 把 $\operatorname{Pf}$ 与 $\operatorname{Pf}^-$ 等同，得 $c_{\pm i}:\operatorname{Pf}^{\otimes2}\xrightarrow{\sim}\det R\Gamma$，且 $(c_i)^{-1}c_{-i}$ 是乘 $(-1)^{p(\mathcal Q)}$。具体定义在 Lagrange 三元组 $(V;L_+,L_-)$ 上（偶维 $V$、非退化对称型、极大各向同性子空间 $L_+,L_-$）：取带典范 $(\mathbb Z/2)$-分次的 Clifford 代数 $\operatorname{Cl}(V)$（$V$ 为奇）的不可约分次模 $M$，置 $M_{L_-}=M/L_-M$、$M^{L_+}:=\{m\in M\mid L_+m=0\}$，二者均一维分次空间，定义 $\operatorname{Pf}(V;L_+,L_-):=M^{L_+}\otimes(M_{L_-})^*$；取 $M=\operatorname{Cl}(V)/\operatorname{Cl}(V)L_+$ 时 $M^{L_+}=\mathbb C$，得 $\operatorname{Pf}(V;L_+,L_-)^*=\operatorname{Cl}(V)/(L_-\cdot\operatorname{Cl}(V)+\operatorname{Cl}(V)\cdot L_+)$。分次对应 $-1\in\operatorname{Aut}(V;L_+,L_-)$ 的作用。§4.0 用它解决实际问题：固定 $\mathcal L\in\omega^{1/2}(X)$，以 $\operatorname{Pf}(\mathfrak g_{\mathfrak F}\otimes\mathcal L)\otimes\operatorname{Pf}(\mathfrak g\otimes\mathcal L)^{\otimes-1}$ 为 $\mathfrak F\in\operatorname{Bun}_G$ 处纤维的线丛是 $\omega^\sharp_{\operatorname{Bun}_G}$ 的平方根。

**记号**：$\mathcal Q$：$\omega$-正交丛，带非退化对称配对 $\mathcal Q\otimes\mathcal Q\to\omega_X$；$\omega\text{-Ort}$：其栈、$\det R\Gamma$：$\omega\text{-Ort}$ 上的线丛，纤维为 $\det R\Gamma(X,\mathcal Q)$、$p(\mathcal Q)=\dim H^0(\mathcal Q)\bmod2$：$\operatorname{Pf}(\mathcal Q)$ 的 $(\mathbb Z/2)$-次数，局部常值、$(V;L_+,L_-)$：Lagrange 三元组；$\operatorname{Cl}(V)$：Clifford 代数，$V$ 为奇、$c_{\pm i}$：$\operatorname{Pf}^{\otimes2}\xrightarrow{\sim}\det R\Gamma$ 的两个同构，相差符号 $(-1)^{p(\mathcal Q)}$、$\omega^\sharp_{\operatorname{Bun}_G}=\omega_{\operatorname{Bun}_G}\otimes\omega_0^{\otimes(-1)}$：归一化典范丛（式 (146)）

## 关键点

- Pfaffian 是 $\omega\text{-Ort}$ 上的线丛，不是逐点的行列式：源码强调「$\operatorname{Pf}$ 是线丛」时分次只意味着存在局部常值 $p$，故族上的一致性来自构造，而非逐纤维的选择。
- 平方根关系由 $c_{\pm i}$ 给出：$\operatorname{Pf}^{\otimes2}\cong\det R\Gamma$；但两个自然同构相差 $(-1)^{p(\mathcal Q)}$，这正是 $(\mathbb Z/2)$-分次结构留下的符号，不能靠「取 $c_i$」消掉。
- 朴素的 $\operatorname{Pf}^{?}(\mathcal Q):=\det H^0(X,\mathcal Q)$ 在族上没有意义，因为 $\dim H^0$ 会跳跃（注 i）；Serre 对偶只给出 $\det R\Gamma=\det H^0^{\otimes2}$。4.2.6 又证明 $\operatorname{Pf}\cong\det(L_+\cap L_-)$，所以点上的朴素定义是对的，错在族。
- Clifford 描述使 Pf 可算：$M^{L_+}$ 与 $M_{L_-}$ 都是一维分次空间，$\operatorname{Pf}$ 就是把两者对偶张起来；取具体的 $M=\operatorname{Cl}(V)/\operatorname{Cl}(V)L_+$ 后得到仅用 $\operatorname{Cl}(V)$ 与 $L_\pm$ 的公式 (167)。
- 在 §4.0 它承担实质任务：$G$ 单连通时 $\operatorname{Bun}_G$ 连通单连通，问题化为 $\omega^\sharp_{\operatorname{Bun}_G}$ 的平方根，而逐纤维的 Pfaffian 造出这个平方根 (148)，进而给 $\lambda_{\mathfrak F}$ 装上扭 $D$-模结构。
- 乘性：正交直和下 $\operatorname{Pf}$ 相乘（式 (168)），且 $\operatorname{Pf}$ 为偶当且仅当 $\dim(L_+\cap L_-)$ 偶；这使 Pf 在分解与符号问题上可控。

## 公式

```latex
\operatorname{Pf}(\mathcal{Q})^{\otimes 2}\xrightarrow{\ \sim\ }\det R\Gamma(X,\mathcal{Q})
```
```latex
(c_{i})^{-1}c_{-i}=(-1)^{p(\mathcal{Q})}
```
```latex
\operatorname{Pf}(V;L_{+},L_{-}):=M^{L_{+}}\otimes(M_{L_{-}})^{*}
```
```latex
\operatorname{Pf}(V;L_{+},L_{-})^{*}=\operatorname{Cl}(V)/(L_{-}\cdot\operatorname{Cl}(V)+\operatorname{Cl}(V)\cdot L_{+})
```
```latex
\operatorname{Pf}(\mathfrak{g}_{\mathfrak{F}}\otimes\mathcal{L})\otimes\operatorname{Pf}(\mathfrak{g}\otimes\mathcal{L})^{\otimes -1}
```

## 常见错误

- 把 $\operatorname{Pf}(\mathcal Q)$ 定义成 $\det H^0(X,\mathcal Q)$：这在单个 $\mathcal Q$ 上可以与 $\operatorname{Pf}$ 等同（4.2.6），但在 $\omega\text{-Ort}$ 上不给出线丛，因为 $\dim H^0$ 会跳；源码注 (i) 由此强调「朴素定义对族没有意义」。
- 把 $c_i$ 当成唯一的典范同构：$c_i$ 与 $c_{-i}$ 相差 $(-1)^{p(\mathcal Q)}$，而注 (iii) 进一步说 $c_\pm=i^{\pm p(\mathcal Q)^2}c_i$ 与正交直和分解不相容（误差 $(-1)^{p(\mathcal Q_1)p(\mathcal Q_2)}$）。在族上随意选 $c_i$ 会得到不相容的平凡化。
- 把 $\omega$-正交丛当成 $\mathcal O_X$-值正交丛：配对取值在 $\omega_X$，故 Serre 对偶给 $H^1=(H^0)^*$、$\det R\Gamma=\det H^0^{\otimes2}$，这正是「平方根」一词的来源；丢掉 $\omega_X$ 就解释不了为什么 Pf 是平方根而不是行列式本身。
- 以为本书定义与 Laszlo–Sorger 的等价性已被证明：§4.2.1 明说「它当然应该与 [La-So] 中的定义等价，但我们没有验证这一点」；引用时应保留这一保留。
- 把 (166) 中的 $M$ 随便取成任一 $\operatorname{Cl}(V)$-模：必须取不可约分次模，此时 $M^{L_+}$ 与 $M_{L_-}$ 才各一维；取非分次模会丢掉 $\operatorname{Pf}$ 的 $(\mathbb Z/2)$-分次，$c_{\pm i}$ 的符号也随之消失。

## 批注

### 易错预警：p(Q) 是局部常值，不是常数

源码写「存在局部常值函数 $p:\omega\text{-Ort}\to\mathbb Z/2$，使得 $\operatorname{Pf}(\mathcal Q)$ 的次数为 $p(\mathcal Q)$」，随后才说 $p(\mathcal Q)=\dim H^0(\mathcal Q)\bmod2$。这两句合起来的意思是：$\dim H^0\bmod2$ 在 $\omega\text{-Ort}$ 的连通分支上是常数（Atiyah–Mumford），但跨分支可以变。把 $p$ 当成整体常数，就会以为 $\operatorname{Pf}$ 是通常（非分次）线丛，进而把 $c_i$ 与 $c_{-i}$ 的差别当成可忽略的符号。

### 含糊点拨：Pf 与 det 在 Lagrange 三元组上如何分工

$\det(V;L_+,L_-):=\det L_+\otimes\det L_-\otimes(\det V)^*$ 是复形 $0\to L_-\to V/L_+\to0$ 的行列式，纯粹是外代数；$\operatorname{Pf}$ 则用 Clifford 模 $M$ 的「两半」$M^{L_+}$ 与 $M_{L_-}$。4.2.6 证明二者都典范同构于 $\det(L_+\cap L_-)$，所以 $\operatorname{Pf}$ 是 $\det$ 的平方根而不是另一个行列式。理解这一点的实用价值：算 $\operatorname{Pf}$ 时可以换成算 $\det(L_+\cap L_-)$，但只能在这两个对象都被定义的点上换，族上仍须用 Clifford 构造。

### 背景直觉：为什么 §4.0 非要用它不可

$G$ 单连通时 $Z$ 平凡，$\operatorname{Bun}_G$ 连通且单连通，要给每个 ${}^{L}G$-oper 配线丛 $\lambda_{\mathfrak F}$，只需说明 $\omega^\sharp_{\operatorname{Bun}_G}$ 有平方根（此时 $\mu_\infty\operatorname{tors}_\theta(\operatorname{Bun}_G)$ 有唯一对象）。Laszlo–Sorger 把「$\det R\Gamma(X,\mathcal Q)$ 的典范平方根」给成 $\operatorname{Pf}(\mathcal Q)$，逐纤维应用到 $\mathcal Q=\mathfrak g_{\mathfrak F}\otimes\mathcal L$ 与 $\mathcal Q=\mathfrak g\otimes\mathcal L$ 就得到 (148)。注意它依赖 $\mathcal L\in\omega^{1/2}(X)$：平方根换了，线丛就扭一个 $\alpha\mathcal A$（3.4 的 $\alpha$），这正是 4.3.1 要处理的细节。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §4.2.1–§4.2.4；印刷页 [132, 135] / PDF 页 [132, 135]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch04.tex:225-286`
- 4.2 节标题与 4.2.1 在 p.132，线丛构造在 p.133，Lagrange 三元组与 det 在 p.134–135，Clifford 定义 (166)(167) 在 p.135；本书 PDF 页 = 印刷页。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §4.0；印刷页 [122, 123] / PDF 页 [122, 123]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch04.tex:10-34`
- 式 (146) 与「Pfaffian（普法夫式）」首现在 p.122，平方根线丛 (148) 在 p.123；本书 PDF 页 = 印刷页。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
