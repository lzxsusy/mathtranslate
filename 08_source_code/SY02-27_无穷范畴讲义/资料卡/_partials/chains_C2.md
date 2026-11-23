# C2 批论证链（第 24–26 讲）

### 链：相对张量积何以"存在且可算"，又如何给出 smash 积的刻画

**问题.** 设 $q\colon\cC^{\otimes}\to\OO^{\otimes}$ 把 $\cC^{\otimes}$ 展示为可表现 $\OO$-幺半 $\infty$-范畴，$A\in\Alg_{/\OO}(\cC)$。$\Mod^{\OO}_{A}(\cC)^{\otimes}$ 上的相对张量积 $-\otimes_{A}-$ 凭什么既存在、又能在具体 $\cC$ 中算出来？进一步，第 25 讲对带基点空间定义的 smash 积 $-\wedge-$，与 Lurie 张量积 $-\otimes-$ 是什么关系？

**起点.** 定理 1.4（`SY02-27.stmt.24.1.4`，第 24 讲 p1）：若 $\OO^{\otimes}$ 本质小、$q$ 展示可表现 $\OO$-幺半结构，则 $\Mod^{\OO}_{A}(\cC)^{\otimes}\to\OO^{\otimes}$ 把 $\Mod^{\OO}_{A}(\cC)^{\otimes}$ 展示为可表现 $\OO$-幺半 $\infty$-范畴。
*warrant*：定理 1.2（`SY02-27.stmt.24.1.2`）已把 $\Mod^{\OO}_{A}(\cC)^{\otimes}$ 造成 $\OO^{\otimes}$ 上的 $\infty$-操作子，且遗忘函子到 $\cC^{\otimes}$ 是 $\infty$-操作子映射；"展示"才有着落的对象。可表现性逐纤维验证，依据是 $-\otimes-$ 逐因子保余极限。

**步骤.**
1. 把"存在"变成"可算"：注 1.6 的 Bar 构造给出 $M\otimes_{A}N$ 是单纯对象的几何实现
   $$M\otimes N\leftarrow M\otimes A\otimes N\leftarrow M\otimes A\otimes A\otimes N\leftarrow\cdots$$
   （`SY02-27.concept.bar-construction`）。
   *warrant*：$\cC$ 可表现且张量积逐因子保余极限，故该几何实现收敛；所得对象满足相对张量积的万有性质，于是定理 1.4 的存在性被一个逐对象的配方替代。
2. 极限一侧：定理 2.1（`SY02-27.stmt.24.2.1`）说 $\Mod^{\OO}(\cC)^{\otimes}\to\Alg_{/\OO}(\cC)$ 是笛卡尔纤维化，其中态射笛卡尔当且仅当其像在 $\cC^{\otimes}$ 中同构；定理 2.8（`SY02-27.stmt.24.2.8`）说若 $q$ 是余笛卡尔纤维化且纤维 $\cC^{\otimes}_{X}$ 有 $K$-极限，则 $\Mod^{\OO}_{A}(\cC)^{\otimes}_{X}$ 有 $K$-极限且遗忘函子保持并检测。
   *warrant*：笛卡尔纤维化把"换环"变成沿 $\Alg_{/\OO}(\cC)$ 的函子性（反变传输 $\mathrm{res}_{\phi}$，`SY02-27.concept.restriction-functor`）；检测性使极限可以先在 $\cC^{\otimes}_{X}$ 中算、再拉回纤维（练习 2.2 的保守性 + 练习 2.9）。
3. 余极限一侧：推论 3.2 与定理 3.5（`SY02-27.stmt.24.3.5`）在 $\OO^{\otimes}=\mathrm{Comm}^{\otimes}$ 且 $q$ 与几何实现相容时，$\Mod^{\mathrm{Comm}}(\cC)^{\otimes}\to\Alg_{\mathrm{Comm}}(\cC)\times\OO^{\otimes}$ 是余笛卡尔纤维化，协变传输 $\mathrm{ind}_{\phi}(M)=B\otimes_{A}M$（`SY02-27.concept.induction-functor`）。
   *warrant*：余笛卡尔性由步骤 1 的 Bar 构造逐对象给出（注 3.6）；这一步把换环从反变变成协变，是后文把 $\Mod$ 当"作用"使用的支点。
4. 结构识别：命题 4.2（`SY02-27.stmt.24.4.2`）把交换代数的模等同于底结合代数的左模；命题 4.4（`SY02-27.stmt.24.4.4`）把结合代数的模等同于其双模。
   *warrant*：沿 $\mathrm{Comm}^{\otimes}\to\mathrm{Assoc}^{\otimes}$ 的拉回方图；附录 A.1 的 $_{A}\mathrm{BMod}_{B}(\cC)\simeq\mathrm{LMod}_{A}(\mathrm{RMod}_{B}(\cC))$ 提供逐项核对。
5. 第 25 讲把 $\mathrm{Pr}^{L}$ 本身变成对称幺半：定理-定义 3.1（`SY02-27.stmt.25.3.1`）给出 $(\mathrm{Pr}^{L})^{\otimes}\subseteq(\widehat{\Cat}_{\infty})^{\times}$；定理 3.7（`SY02-27.stmt.25.3.7`）给出 $C\otimes D\simeq\mathrm{RFun}(C^{\op},D)$（`SY02-27.concept.lurie-tensor-product`、`SY02-27.concept.rfun`）。
   *warrant*："对象逐分量可表现、态射逐因子保余极限"的 1-全子条件保证 $\mathrm{Fin}_{*}$ 上的 Segal 条件；3.7 的证明是 $\mathrm{LFun}(C\otimes D,E)\simeq\mathrm{LFun}(C,\mathrm{LFun}(D,E))$ 的伴随链再取右伴随，故等价可在 Hom 空间层面判定。
6. 内蕴刻画：定义 4.1 的幂等交换代数（$A\otimes A\xrightarrow{\simeq}A$，`SY02-27.concept.idempotent-commutative-algebra`），命题 4.2（`SY02-27.stmt.25.4.2`）给出全忠实性与本质像判据，命题 4.6（`SY02-27.stmt.25.4.6`）把 $\Mod^{\mathrm{Comm}}_{A}(\cC)^{\otimes}$ 变成对称幺半。
   *warrant*：幂等性使 $A$-模的张量积仍是 $A$-模；判据 "$M\simeq\mathbf{1}_{\cC}\otimes M\to A\otimes M$ 是同构"恰是"$M$ 带 $A$-模结构"的等价改写。
7. 收束到 smash 积：由练习 4.3，$\Spc_{*}$ 与 $\Sptr$ 是 $\Alg^{\mathrm{idem}}_{\mathrm{Comm}}(\mathrm{Pr}^{L})$ 的对象；推论 4.7（`SY02-27.stmt.25.4.7`）给出 $\Mod^{\mathrm{Comm}}_{\Spc_{*}}(\mathrm{Pr}^{L})\to\mathrm{Pr}^{L}$ 全忠实、本质像为带基点可表现 $\infty$-范畴，对 $\otimes$ 封闭；定义 4.4 的 smash 积 $-\wedge-$ 由此获得内蕴描述（`SY02-27.concept.smash-product`、`SY02-27.concept.pointed-presentable-infinity-category`），注 4.9 进一步说 $\Sptr$ 是 $\Alg_{\mathrm{Comm}}(\mathrm{Pr}^{L})$ 的始对象。
   *warrant*：步骤 6 的判据在 $\Spc_{*}\otimes C\simeq C_{*}$（练习 3.13）上具体化为"添基点"，故"带基点"这一朴素描述与模条件重合。

**收口.** 存在（定理 1.4）、可算（Bar 构造）、极限行为（定理 2.1、2.8）与余极限行为（推论 3.2、定理 3.5）合起来说明：$\Mod^{\OO}_{A}(\cC)^{\otimes}$ 是一个可由 $\cC$ 与 $A$ 逐点算出的对称幺半对象。把 $\cC$ 取成 $\mathrm{Pr}^{L}$、$A$ 取成幂等的 $\Spc_{*}$，相对张量积就特化为 smash 积，其"带基点可表现 $\infty$-范畴"的本质像刻画随之落地。

**反事实.** 若没有注 1.6 的 Bar 构造，定理 1.4 只说"存在"，$M\otimes_{A}N$ 在具体 $\cC$ 中无法计算，第 25 讲的 $\mathrm{RFun}(C^{\op},D)$ 也无从与 $\Mod$ 的显式描述对接。若没有命题 4.2 的幂等判据，$\Spc_{*}$、$\Sptr$ 只是"带额外结构的对象"，推论 4.7 的"本质像 = 带基点可表现 $\infty$-范畴"便退化为同义反复，smash 积的内蕴刻画失去内容。

### 链：$\odot$ 的构造与 $E_k$ 的 Dunn 加性

**问题.** 第 26 讲要在 $\mathrm{Op}_{\infty}$ 上造对称幺半结构 $\odot$，使"代数中的代数"等于"$\odot$-张量积上的代数"：$\Alg_{O_{1}}(\Alg_{O_{2}}(\cC))\simeq\Alg_{O_{1}\odot O_{2}}(\cC)$。为什么 $\mathrm{Op}_{\infty}$ 上"应该"有这样一个乘法？它凭什么与 $E_{k}$（$k$ 维小方体）的直观相容？

**起点.** 构造 1.2：在 $\mathrm{Fin}_{*}$ 上取 $\wedge$，$\langle m\rangle\wedge\langle n\rangle=\langle mn\rangle$，使 $(\mathrm{Fin}_{*},\wedge)$ 是 $\Alg_{\mathrm{Comm}}(\Cat_{\infty})$ 的对象；练习 1.3 把它升级为 $\mathrm{Op}_{\infty}$ 中的交换代数。
*warrant*：练习 1.4 给出全子 $\mathrm{Op}_{\infty}\subseteq(\Cat_{\infty})_{/\mathrm{Fin}_{*}}$，故切片上的交换代数结构可以直接沿该全子搬运，无需重新验证 Segal 条件。

**步骤.**
1. 命题—构造 1.5（`SY02-27.stmt.26.1.5`）：对任意 $\infty$-操作子 $\cC^{\otimes}\to\mathrm{Comm}^{\otimes}$ 与交换代数 $A$，存在切片操作子 $(\cC_{/A})^{\otimes}\to\cC^{\otimes}$，其单位纤维是 $\cC_{/A(\langle1\rangle)}$，惰性态射与 $q$-惰性态射一致，$\cC^{\otimes}$ 对称幺半时亦然（`SY02-27.concept.slice-operad`）。
   *warrant*：拉直把 $\cC^{\otimes}$ 读成 $\mathrm{Fin}_{*}$ 上的对称幺半纤维化，切片上取 $q$-惰性态射即可逐条验证 Segal 条件；注 1.6 给出切片中的乘法 $M\otimes N\to A\otimes A\to A$。
2. 定理—定义 1.10（`SY02-27.stmt.26.1.10`）：1-全子 $(\mathrm{Op}_{\infty})^{\odot}\subseteq((\Cat_{\infty})_{/\mathrm{Fin}_{*}})^{\otimes}$（对象各分量是 $\infty$-操作子，态射逐因子保惰性态射）给出 $\mathrm{Op}_{\infty}$ 上的对称幺半结构，乘法记 $\odot$（`SY02-27.concept.infinity-operad-tensor-product`）。
   *warrant*：把步骤 1 用于 $A=\mathrm{Fin}_{*}$、$\cC=\Cat_{\infty}$ 的切片；"逐因子保惰性态射"在复合下保持，得 Segal 条件；注 1.9 强调这不是切片上的笛卡尔结构。练习 1.13 给出判据：$\mathrm{Map}(\bigodot_{i}O_{i},O)$ 是 $\prod_{i}\mathrm{Map}(O_{i},O)$ 中"逐因子保惰性态射"的子空间。
3. 代数中的代数：构造 3.2 造出 $\Alg_{O_{2}/O}(\cC)^{\otimes}$，命题 3.5 用余笛卡尔判据把它识别为 $O_{1}^{\otimes}$ 上的 $\infty$-操作子（`SY02-27.concept.relative-algebra`）；练习 3.7（`SY02-27.stmt.26.3.7`）于是给出 $O^{\otimes}=(O_{1}\odot O_{2})^{\otimes}$ 时 $\Alg_{O_{1}}(\Alg_{O_{2}}(\cC))\simeq\Alg_{O_{1}\odot O_{2}}(\cC)$。
   *warrant*：练习 3.7 的两侧分别是"先取 $O_{2}$-代数再取 $O_{1}$-代数"与"直接在 $\odot$-张量积上取代数"，命题 3.5 的余笛卡尔性使二者在同一纤维化上逐纤维比较。
4. $E_{k}$ 的几何定义：定义 4.1 用小方体 $\infty$-操作子 $E_{k}^{\otimes}$，其 $m$ 元运算空间是 $\square^{k}$ 中互不交叠的矩形的空间（`SY02-27.concept.little-cubes-operad`、`SY02-27.concept.rectilinear-embedding`）；构造 4.9 给出逐分量的 $E_{k}^{\otimes}\times E_{k^{\prime}}^{\otimes}\to E_{k+k^{\prime}}^{\otimes}$。
   *warrant*：$\square^{k}\times\square^{k^{\prime}}\simeq\square^{k+k^{\prime}}$ 使"矩形拼接"确实是逐分量操作；练习 4.10 验证该构造逐因子保惰性态射，故它是 $\odot$ 的映射。
5. 定理 4.12（`SY02-27.stmt.26.4.12`）Dunn 加性：$(E_{k}\odot E_{k^{\prime}})^{\otimes}\simeq E_{k+k^{\prime}}^{\otimes}$。
   *warrant*：练习 1.13 的判据把 $\odot$ 的映射空间化为"逐因子保惰性"，构造 4.9 恰好满足；逐 $m$ 元运算比较时，$\square^{k}\times\square^{k^{\prime}}$ 中的矩形嵌入与 $\square^{k+k^{\prime}}$ 中的直线嵌入是同一族，故映射空间等价（`SY02-27.concept.rectilinear-embedding`）。
6. 推论 4.14 得 $(E_{k}\odot\mathrm{Comm})^{\otimes}\simeq\mathrm{Comm}^{\otimes}$；命题 4.16（`SY02-27.stmt.26.4.16`，Baez–Dolan）说若 $\cC$ 是对称幺半 $(n,1)$-范畴且 $k>n$，则 $\Alg_{E_{k}}(\cC)\simeq\Alg_{E_{\infty}}(\cC)$。
   *warrant*：$E_{k}$ 的 $m$ 元运算空间是 $(k-1)$-连通的，在 $(n,1)$-范畴中把该空间映入 $\cC$ 的映射空间后为可缩，故高阶运算不再提供数据；推论 4.14 可由定理 4.12 令 $k^{\prime}=\infty$ 得到。
7. 定理 4.23（`SY02-27.stmt.26.4.23`）：$E_{k}$-模的相对张量积由底层 $E_{1}$-模的相对张量积给出。
   *warrant*：这是第 24 讲定理 1.4 在 $E_{k}$-幺半情形的实例，加上沿 $E_{1}^{\otimes}\to E_{k}^{\otimes}$ 的拉回（余笛卡尔纤维化的函子性）；注 4.24 说明 $E_{k}$-模的乘法在底层 $E_{1}$ 上已完全决定。

**收口.** $\odot$ 的存在把"代数中的代数"化为"张量积上的代数"（练习 3.7），而 $E_{k}$ 的几何定义与 $\odot$ 相容（定理 4.12）。于是 $E_{k}$ 的代数层级、稳定化现象（命题 4.16）与模的相对张量积（定理 4.23）被纳入同一框架：$\mathrm{Op}_{\infty}$ 成为对称幺半 $\infty$-范畴，$E_{k}$ 是其中由维度参数化的一族对象，$\odot$ 对应维数相加。

**反事实.** 若只有构造 3.2 而没有命题 3.5 的余笛卡尔判据，练习 3.7 的两侧无法比对，$\Alg_{O_{1}}(\Alg_{O_{2}}(\cC))$ 只能作为抽象 $\infty$-范畴存在，"代数中的代数"也就没有可计算的形式。若 $E_{k}$ 改用任意嵌入而非直线嵌入，构造 4.9 便不逐因子保惰性态射，定理 4.12 无从陈述，Dunn 加性会退化成"$E_{k}$ 与 $E_{k^{\prime}}$ 同伦类型相乘"的模糊印象，推论 4.14 与命题 4.16 也随之失去统一来源。
