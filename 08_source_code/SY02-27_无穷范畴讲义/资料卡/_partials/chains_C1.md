### 链：纤维化即函子——从笛卡尔提升到拉直

**问题.** 底范畴 $D$ 上的纤维化几何数据，与函子 $D^{op}\to\Cat_{\infty}$ 的代数数据，何时可以互相翻译？翻译的代价由谁承担？

**起点.** 第 19 讲把"沿 $D$ 的纤维"逐边地定义清楚：SY02-27.concept.locally-cartesian-morphism 只要求每个基边有局部提升（第 19 讲 p1），SY02-27.concept.cartesian-fibration 则要求一切基边都有 $p$-笛卡尔提升（第 19 讲 p3）。此时纤维 $\cC_{y}$ 是 $\infty$-范畴而非单纯集，SY02-27.concept.naive-fiber 与同伦纤维的差别已被例 1.8 排除（第 19 讲 p2）。

**步骤.**

1. 先把"逐边"升级为"对复合封闭"：命题 2.3（SY02-27.stmt.19.2.3）给出三条件等价，其中 (2) 说 $g$ 局部笛卡尔当且仅当 $g\circ f$ 局部笛卡尔。
   *warrant*：把 (2.1) 方块在测试对象上的笛卡尔性与 2-单纯形填充相比较（第 19 讲 p2）。
2. 再证提升的唯一性：命题 3.1（SY02-27.stmt.19.3.1）把"$f$ 局部 $p$-笛卡尔"化归为 $\cC_{/Y}\times_{\cD_{/p(Y)}}\{p(f)\}$ 中对象的终性。
   *warrant*：归约到 $D=\Delta^{1}$ 后用 Ker.02HF 的平凡 Kan 纤维化判据（第 19 讲 p4）。
3. 于是沿边 $f\colon x\to y$ 可以取反变传输 $f^{\Downarrow}\colon\cC_{y}\to\cC_{x}$（SY02-27.concept.transport-functor，第 20 讲 p1）。它只在可缩选择空间上良定义，这正是第 2 步唯一性的直接后果；SY02-27.stmt.20.1.2 进一步说 $\ev_{1}\colon\Sect^{\Cart}_{/[1]}(\cC)\to\cC_{1}$ 是等价。
4. 把"函子性"装配成模型结构：定理 2.18（SY02-27.stmt.20.2.18）在 $(\Set^{+}_{\Delta})_{/S}$ 上造出组合、左固有模型结构，弱等价即 SY02-27.concept.cartesian-equivalence；$S=\Delta^{0}$ 时它与 Joyal 模型结构 Quillen 等价（SY02-27.stmt.20.2.21）。
   *warrant*：$\Hom^{\sharp}$ 的充实性与 $X^{\natural}$ 纤维对象的识别（第 20 讲 p4）。
5. 拉直：定理 3.2（SY02-27.stmt.20.3.2）给出 $\St^{+}_{\phi}\dashv\Un^{+}_{\phi}$，$\phi$ 弱等价时是 Quillen 等价。
   *warrant*：第 1–3 步已把两边同伦论对齐到 $\Cart_{/D}$ 与 $\Fun(D^{op},\Cat_{\infty})$。
6. 收口前的兑现：极限与余极限确实由这套翻译计算——$\lim u\simeq\Sect^{\Cart}_{/S}(X)$（SY02-27.stmt.20.5.8），$\colim u\simeq X^{\natural}$（SY02-27.stmt.20.5.9）。
   *warrant*：拉直把逐点极限送到截面，把余极限送到标记边的全空间（第 20 讲 p8）。

**收口.** 推论 3.3（SY02-27.stmt.20.3.3）给出典范等价 $\Cart_{/D}\simeq\Fun(D^{op},\Cat_{\infty})$，即所谓 Grothendieck–Lurie 构造（SY02-27.concept.straightening 与 SY02-27.concept.unstraightening）：笛卡尔纤维化与反变函子互为完整不变量。

**反事实.** 若没有命题 3.1 的唯一性，$f^{\Downarrow}$ 只能在可缩选择空间里"选一个"，传输不满足严格函子性，第 5 步只能得到 $(\infty,2)$-范畴层面的松弛对应（第 20 讲 p2 备注 1.4），$\Cart_{/D}\simeq\Fun(D^{op},\Cat_{\infty})$ 便退化为仅在同伦范畴中的陈述。

### 链：操作子作为代数的通用语法

**问题.** 交换环、结合环、左/右模、双模各有各的"多输入乘法"。能否用同一套语言写出它们，并让单位、极限、自由代数成为关于这套语言的一般定理？

**起点.** 第 21 讲把经典操作子的"逐项数据"换成 $\Fin_{*}$ 上的 $\infty$-范畴：SY02-27.concept.finite-pointed-sets 给出标记有限集的极小模型，惰性/活性态射区分"丢弃与复制"和"真正的运算"（第 21 讲 p2）。SY02-27.stmt.21.1.9 说明对称幺半 $\infty$-范畴就是使惰性态射展示 $F(\langle n\rangle)\simeq F(\langle 1\rangle)^{\times n}$ 的函子。

**步骤.**

1. 抽象出操作子：SY02-27.stmt.21.2.11 把 $\infty$-操作子定义为满足练习 2.10 三条件的 $\cO^{\otimes}\to\Fin_{*}$——惰性提升、$p$-极限分解、余变传输给出积。
   *warrant*：练习 2.10（SY02-27.stmt.21.2.10）在 $\Comm^{\otimes},\Assoc^{\otimes},\CMod^{\otimes},\LMod^{\otimes},\RMod^{\otimes},\BMod^{\otimes}$ 上逐条验证了这三条（第 21 讲 p5）。
2. 定义代数：SY02-27.stmt.21.3.2 说 $\cO$-代数就是 $\Fin_{*}$ 上保持惰性的操作子映射。
   *warrant*：惰性保积保证 $p(X)\simeq(p(X_{1}),\dots,p(X_{n}))$，活性算子 $\gamma$ 于是给出 $p(X_{1})\otimes\cdots\otimes p(X_{n})\to p(Y)$（第 22 讲 p1）。
3. 处理单位：SY02-27.concept.unital-infinity-operad 要求 $\Maps_{\cO^{\otimes}}(\langle0\rangle,X)$ 可缩（SY02-27.stmt.22.3.4）；在此假设下 SY02-27.concept.unit-object 与 SY02-27.concept.unit-algebra 有定义，且命题 3.15（SY02-27.stmt.22.3.15）把"$A$ 始""$A(\langle0\rangle)\to A(X)$ 展示单位""逐颜色成立"三条件判为等价。
   *warrant*：unital 时 $\langle0\rangle$ 是始对象（第 22 讲 p2 的 3.9），始性沿操作子映射前推。
4. 把极限交给纤维：定理 5.3（SY02-27.stmt.22.5.3）说各纤维有 $K$-极限即可，遗忘函子保持并检测。
   *warrant*：传输函子保极限，故逐纤维的极限自动带代数结构（第 22 讲 p5）。余极限方向需要额外假设：SY02-27.concept.compatible-with-colimits 与筛性（SY02-27.stmt.22.5.7）。
5. 自由代数把两步接起来：定理 5.9（SY02-27.stmt.22.5.9）给出左伴随 $\mathrm{Free}_{\cO}$，从而 $\Alg_{/\cO}(\cC)$ 有小肠余极限。
   *warrant*：自由代数消解 + 筛余极限逐项计算（第 22 讲 p5–p6）。

**收口.** 命题 5.13（SY02-27.stmt.22.5.13）在可表现 $\cO$-幺半、$\cO$ 本质小的假设下断言 $\Alg_{/\cO}(\cC)$ 可表现：单位性、极限、余极限、可表现性四条性质都归约到纤维 $\cC^{\otimes}_{X}$ 的相应性质，$\infty$-操作子只是把这四条"打包"的语法。

**反事实.** 若去掉连贯性假设（SY02-27.concept.coherent-infinity-operad，第 23 讲 p3），$\ev_{0,*}$ 不存在，SY02-27.stmt.23.3.2 的 $\Mod^{\cO}(\cC)^{\otimes}$ 无从定义；第 22 讲的代数机器仍在，但"模"这一层整块缺失，相对张量 $-\otimes_{A}-$ 无法参数化。

### 链：从群到环——解环、线性化与 HR-模

**问题.** 空间层面的群论（$\Omega^{k}$、解环）如何在线性层面变成谱环论，并且 $\mathrm{HR}$-模为什么会精确回到经典导出范畴 $D(R)$？

**起点.** 第 27 讲开篇的类比表把 Sets↔Spaces、Abelian groups↔Spectra、Tensor↔Smash、Commutative rings↔$E_{\infty}$-rings 并列。SY02-27.stmt.27.1.3 用"$(p_{1},m),(m,p_{2})$ 可逆"在有有限积的任意 $\infty$-范畴中定义 SY02-27.concept.group-in-infinity-category，SY02-27.stmt.27.1.4 则用算子 $\gamma\colon\Box^{k}\times\langle m\rangle^{\circ}\to\Box^{k}$ 在 $\Omega^{k}X$ 上装出 $E_{k}$-群结构（第 27 讲 p1）。

**步骤.**

1. 解环：定理 1.7（SY02-27.stmt.27.1.7，Boardman–Vogt–May）断言 $\Omega^{k}\colon(\Spc_{*})_{\ge k}\to\Grp_{E_{k}}(\Spc)$ 是等价。
   *warrant*：$(k-1)$-连接性使 $\pi_{i}$（$i<k$）为零，$\Omega^{k}$ 在截断上既本质满又全忠实（第 27 讲 p2）。
2. 取极限：推论 1.11（SY02-27.stmt.27.1.11）给出 $\Omega^{\infty}\colon\Sptr_{\ge0}\simeq\Grp_{E_{\infty}}(\Spc)$。
   *warrant*：例 1.9 的相容方块使 $k\to\infty$ 的逆极限与连接谱的遗忘相容；连接谱即 SY02-27.concept.picard-infinity-groupoid（第 27 讲 p2）。
3. 环化：SY02-27.stmt.27.3.1 定义 SY02-27.concept.ek-ring 为 $\Sptr$ 中的 $E_{k}$-代数；构造 3.2（SY02-27.stmt.27.3.2）用 $\pi_{*}$ 的右松弛对称幺半结构把 $E_{1}$-环送到结合环、把 $k\ge2$ 的 $E_{k}$-环送到分次交换环。
   *warrant*：$\pi_{m}X\otimes\pi_{n}Y\to\pi_{m+n}(X\otimes Y)$ 来自 $S[m]\otimes S[n]\simeq S[m+n]$（SY02-27.stmt.27.2.3，第 27 讲 p3）。
4. 线性化：构造 3.3（SY02-27.stmt.27.3.3）指出 $\pi_{0}\colon\Sptr_{\ge0}\to\mathrm{Ab}$ 经 $\mathrm{Ab}\simeq\Sptr^{\heartsuit}$ 识别为 $\tau_{\le0}$，其右伴随 $R\mapsto HR$ 就是 SY02-27.concept.eilenberg-maclane-spectrum-functor：交换环 $R$ 给出 $E_{\infty}$-环 $HR$。
   *warrant*：左伴随对称幺半，故右伴随右松弛，代数结构沿右伴随前推（第 27 讲 p4）。
5. 回到模：定理 3.8（SY02-27.stmt.27.3.8）断言对称幺半等价 $\Mod_{HR}(\Sptr)\simeq D(R)$，且 $F\dashv G$ 可识别为 $u\colon S\to HR$ 的 $\mathrm{ind}_{u}\dashv\mathrm{res}_{u}$。
   *warrant*：定理 A.2（SY02-27.stmt.27.A.2，Barr–Beck–Lurie）——$G$ 保守且保 $G$-分裂单纯余极限，故 $\cD\simeq\LMod_{T}(\cC)$（第 27 讲 p5）。

**收口.** 第 27 讲 p5 的定理 3.8 是这条链的落点：$E_{\infty}$-环 $HR$ 上的模与 $R$ 的导出范畴是同一件事，$\Sptr\to D(R)$ 的对称幺半结构与"$S\mapsto R$"的底层函子互为伴随。于是"H$R$-模"这一看似谱化的对象，其同伦范畴就是经典 $D(R)$。

**反事实.** 若 $\pi_{*}$ 是对称幺半函子，$E_{\infty}$ 结构会在线性化时原样保留为交换环，构造 3.2 中"$k\ge2$ 给分次交换"的弱化便不必要；但警告 2.4（SY02-27.stmt.27.2.4）指出 $\pi_{*}(S)\ne\mathbb{Z}$，$\pi_{*}$ 只是右松弛，因此定理 3.8 必须走"$HR$ 是 $E_{\infty}$-环、而其模范畴只看到 $E_{1}$ 层面的 $D(R)$"这条迂回路径。
