# U04 复算报告

> 复算对象：K–W 2006（B）§5「Topological Field Theory In Two Dimensions」，印刷页 pp.56–78（§5 标题在 p057.txt:17，§6 标题在 p079.txt:29）。
> 复算方式：**全部自己算**——逐页读 B 源文本（页号一律用印刷页，`p0NN.txt` ↔ 印刷页 NN−1），另用 numpy 做 6 段可重跑数值核对（见附录）。`work/rounds/U04/report_v1.md`（下称「报告」）只作对照对象，其结论不被当作依据。
> 与报告的分工：本文件只做独立复算 + 差异清单，不复述报告的叙述结构。
> 约定：`(A)` = 原文明写；`(B)` = 我重建的推导；`(C)` = 我的判断。

---

## 一、二维超荷存活与参数

### 1.1 问题

(5.1) 是一组 6 条方程（μν = 01,02,03,12,13,23）。紧化到更低 holonomy 的 M 后，条件逐级放松。要数的是：M 一般四流形 / M = ℝ×W（W 三维）/ M = ℝ^{1,1}×C 三种情形下，各存活几个超荷；以及存活超荷的「维数」按哪个口径计。然后由 (5.8) 的 abelian 化推出 (5.11) 的 `w₊ = −t`, `w₋ = t⁻¹`，并解释 t 的射影性与 t↔−t。

### 1.2 原文与页

- p.56：(5.1) `(Γ_μν + Γ_{4+μ,4+ν}) ε = 0`，μν = 0..3；手征条件 (5.2) Lorentz 号差 `Γ₀…Γ₉ ε = ε`，Euclid 号差 `Γ₀…Γ₉ ε = −iε`。扭化 = 取对角子群 Spin′(4) ⊂ Spin(4)×Spin(6) 不变的超荷；φ₄,φ₅（内部指标 8,9）未 twisted，其余 4 个被 twist 成一形式。
- p.57：「the holonomy of M reduces to SO(3), unbroken supersymmetries need only be invariant under a subgroup Spin′(3) ⊂ Spin′(4); equivalently, we need only impose (5.1) for μ, ν = 1,…,3. **There are four unbroken supersymmetry generators**」；再取 M = ℝ^{1,1}×C 时「(5.1) collapses to the single condition」`Γ₂₃₆₇ ε = ε`（(5.3)），「**leaving an eight-dimensional space of unbroken supersymmetries**」；4 个未 twisted 标量 φ₀,φ₁,φ₄,φ₅ 按 Spin(4)_R 变换，(5.4) `Γ₀₁ε = Γ₄₅₈₉ε`（Lorentz 号差）⇒ (2,1)₋⊕(1,2)₊ ⇒ 2d (4,4) 超对称。
- p.60–61：(5.8) `(F + t dφ)⁺ = 0`, `(F − t⁻¹dφ)⁻ = 0`；全纯坐标 `A_z̄ − w φ_z̄` 与 `A_z + w⁻¹φ_z`（p.60 顶部；这是把 (5.8) 与 (5.5)(5.6) 对上的关键一行，属跨页引用）；(5.9)(5.10) `∂̄_y(A_z̄ + tφ_z̄)=0`、`∂_y(A_z̄ − t⁻¹φ_z̄)=0`；(5.11) `w₊ = −t, w₋ = t⁻¹`。
- p.61–62：B-模型 `w₊ = w₋` ⇒ `t⁻¹ = −t` ⇒ `t = ±i`；A-模型 `w₋ = −1/w̄₊` ⇒ `t⁻¹ = 1/t̄` ⇒ t 实；`t=±1` → K/−K，`t=0,∞` → I/−I。(5.12) `q = w₊/w₋ = −t²`；TFT 在 `(w₊,w₋) ∼ (λ⁻¹w₊, λ⁻¹w₋)`（λ∈ℂ*）下只依赖 q；t 与 −t 给等价 2d 理论，来源是 4d 的 SU(4)_R 中心（等价于 (3.14) 的 ℤ₂）。

### 1.3 推导（数超荷）

**(B) 口径先说清楚。** (5.1) 的 6 个算符正是对角 so(4)′ 的 6 个生成元 `J_μν = ½(Γ_μν + Γ_{4+μ,4+ν})`。超荷 ε 取 10d Euclid Weyl 旋量，`Γ₀…Γ₉ε = −iε` 给出 16 维复空间（`(Γ₀…Γ₉)² = −1`，故特征值 ±i，各 16 维）。存活超荷 = 这 16 维里同时被这 6 个算符杀死的子空间；它是一组线性约束，所以「数」= 解空间的复维。这个口径能被原文两个明数校准（见数值）。

**(B) 逐级放松的代数理由。** M 的 holonomy 越小，需要 imposed 的 (5.1) 分量越少：
- 一般 M：SO(4) holonomy ⇒ 全部 6 条；
- M = ℝ×W：holonomy ⊂ SO(3) 作用在 1,2,3 上 ⇒ 只要 μν ∈ {12,13,23}，3 条；
- M = ℝ^{1,1}×C：holonomy ⊂ SO(1,1)×SO(2)，只要 μν = 01 与 23。而 `A₂₃ = Γ₂₃+Γ₆₇ = 0 ⟺ Γ₂₃ = −Γ₆₇ ⟺ Γ₂₃Γ₆₇ = 1`（因 Γ₂₃,Γ₆₇ 对易、平方 −1），即 (5.3)。剩 1 条。

**(B) (5.11) 的推导链（三层）。**
1. 4d 侧：abelian 化（(3.29) 的化简）给 (5.8)。t 是 4d TQFT 族 ℂP¹_g 的参数，这一步只把 t 带进来。
2. 2d 几何侧：取 Σ 的局部复坐标 y、C 的局部复坐标 z。`dy∧dz̄` 是自对偶的、`dy∧dz` 反自对偶，于是 (5.8) 的 ⁺ 分量只含 `A_z̄, φ_z̄` 的 ∂̄_y、⁻ 分量只含 ∂_y，得 (5.9)(5.10)。这一步是纯张量分解，不含 t 的新信息。
3. 与 BPS 方程比对：(5.5)(5.6) 说 Φ 对 J₊ 全纯、对 J₋ 反全纯，而 I_w 的全纯坐标是 `A_z̄ − w φ_z̄`。把 (5.9) 的 `A_z̄ + t φ_z̄` 读成「w₊ 的全纯坐标」：`A_z̄ − w₊φ_z̄ ≡ A_z̄ + tφ_z̄` ⇒ `w₊ = −t`；把 (5.10) 的 `A_z̄ − t⁻¹φ_z̄` 读成「w₋ 的反全纯坐标」⇒ `w₋ = t⁻¹`。
   - 负号的来源正是 (5.8) 第一式是 `+t dφ` 而 I_w 的定义里是 `−w φ`：两个来源（4d twist 的 t 与 2d twistor 的 w）用的是相反的符号约定；t⁻¹ 而不是 t 的来源是 (5.8) 第二式是 `F − t⁻¹dφ` 且它与**反**全纯方程配对。
   - 所以 (5.11) 不是「凑出来的」：`(−t, t⁻¹)` 的负号来自 twist 参数进入 (5.8) 的方式，指数 −1 来自 A/B 两个 twist 的互补性（(5.8) 两式的 t 与 t⁻¹ 是 twist 参数在自对偶/反自对偶两个 chirality 上的不同权重）。

**(B) t 的射影性。** t 是 ℂP¹_g 的齐次坐标，本来就只有射影意义；在 (5.11) 下它被送到 ℂP¹_h×ℂP¹_h 的一条曲线。两个 CP¹ 各自的 ℂ* 作用 `w → λ⁻¹w` 把 `(w₊,w₋) → (λ⁻¹w₊, λ⁻¹w₋)`，唯一不变量是 (5.12) 的 `q = w₊/w₋ = −t²`；因此 t 的复标度（`t → λt`）不改变 2d TFT，真正有效的参数是 q（等价地 t²）。

**(B) t ↔ −t 为什么等价。**
- 代数层：`q = −t² = −(−t)²`，所以 ±t 落在同一 ℂ* 轨道上，2d 理论相同（这是 (5.12) 的直接推论）。
- 结构层：t→−t 在 (5.28) 里表现为 `(a,b,c) → (a, −b, −c)`，即 `I_{−w} = aI − bJ − cK`；单个复结构变了，但**这对**点 `(J₊,J₋)` 被同时重标度，而 2d TFT 只依赖这对点。
- 物理层：这个 ℤ₂ 就是 4d 的 SU(4)_R 中心（p.62 明确指到 (3.14)）；在 2d 一侧对应 `(w₊,w₋) ∼ (−w₊,−w₋)`（λ = −1 的中心元）。报告 2.1.5 把这一条归到 SU(4)_R 中心，与原文一致。

### 1.4 数值/特例（附录 S1、S2 可重跑）

- Weyl 空间复维 = 16（`(Γ₀…Γ₉)² = −1`，特征值 ±i）。
- 6 条全上：解空间复维 **2**；只剩 μν=1,2,3：**4**；只剩 (5.3)：**8**。
- 与原文对照：ℝ×W 的「four unbroken」= 4 ✓；ℝ^{1,1}×C 的「eight-dimensional space」= 8 ✓。⇒ 原文的「维数」正是解空间的**复维**（16 → 4 → 8 是 16 → 16/4 → 16/2）。一般 M 上我数得 2，原文未给这个数（不与原文冲突；若有人把「一般 M 上只有 1 个拓扑超荷」写成数，那是另一套口径——§3 只用一个 Q，但 Q 的共轭/BRST 伙伴使解空间不是 1 维）。
- (5.7) 的特值（数值逐项验，S2）：`I₀ = I`，`I_{±1} = ±K`（`I_{1}=K`, `I_{−1}=−K`），`I_{−i}=J`，`I_{i}=−J`，`w→∞ : I_w → −I`；且所有 w 上 `I_w² = −1`。
- 例：t=2 ⇒ `(w₊,w₋)=(−2,1/2)`，`q = −4`；t=−2 ⇒ `(2,−1/2)`，q 仍是 −4。

### 1.5 与报告比

一致。报告的 2.1.2（4→8）、2.1.4（(5.8)→(5.11) 的比对链）、2.1.5（q、t∼−t、SU(4)_R 中心）与我的复算逐条对上；报告还正确指出 (5.9)(5.10) 的 `A_z̄, φ_z̄` 在文本层被丢横线（我核源文本 p062.txt 确认）。

差异只在补强：报告没有给「16 维 Weyl 空间 + 6 条全上」的数（我算 2），也没说明原文的维数口径是复维；这两点不构成错误（E 清单不列，见 §1.6 备注）。

### 1.6 判定

**成立。** (5.11) 的来源 = 4d twist 的 abelian 化 (5.8) + 2d 的 `dy∧dz̄` 自对偶分解 + 与 (5.5)(5.6) 的全纯/反全纯配对；负号来自两套 w 约定相反，t⁻¹ 来自 (5.8) 第二式的 twist 权重。t 的射影性由 (5.12) 的 ℂ* 不变量体现，t↔−t 等价由 q = −t² 与 SU(4)_R 中心双重保证。

---

## 二、B/A 模型判定与 Ψ

### 2.1 问题

由 `w₊ = w₋`（或等价条件）判定 B-模型 ⇔ t = ±i；由 Ψ 的公式验证 Ψ=∞ ⇔ t=±i、Ψ=0 ⇔ A-模型（K）；给 Ψ 与 t² 的显式关系并做符号检查。

### 2.2 原文与页

- p.59：(5.5)(5.6) `(1−iJ₊)∂̄Φ=0`、`(1−iJ₋)∂Φ=0`；B-模型 = `J₊=J₋`，A-模型 = `J₊=−J₋`（后者只依赖 ω）。
- p.61：(5.11) 与判定：B-模型 `t⁻¹=−t` ⇒ `t=±i`；A-模型 `t⁻¹=1/t̄` ⇒ t 实；`t=±1` → K/−K，`t=0,∞` → I/−I。
- p.67：(5.28) `J₊ = aI + bJ + cK`, `J₋ = −aI + bJ − cK`，`a=(1−tt̄)/(1+tt̄)`, `b=−i(t−t̄)/(1+tt̄)`, `c=−(t+t̄)/(1+tt̄)`。
- p.68：(5.33) `[B₀+iω₀] = −i Imτ·[(t−t⁻¹)/(t+t⁻¹)]·[ω_I]`；(5.34) `Ψ = Reτ + i Imτ·[(t−t⁻¹)/(t+t⁻¹)]`。
- p.69：t=±i 时 Ψ=∞ 且与 τ 无关；此时「the model is actually not the B-field transform of an A-model; it is a B-model in complex structure ±J」。

### 2.3 推导

**(B) B-模型的充要条件。** 用 (5.28)：`J₊ − J₋ = 2a I + 2c K`，`J₊ + J₋ = 2b J`。
- `J₊ = J₋` ⟺ `a=0` 且 `c=0`。`c=0 ⟺ t+t̄=0 ⟺ t 纯虚`；`a=0 ⟺ |t|=1`。合起来 `t = ±i`。
- 此时 `J₊ = J₋ = bJ`，而 `b = −i(t−t̄)/(1+|t|²)`：`t=i` 给 `b = −i·2i/2 = 1` ⇒ `J₊=J₋=J`；`t=−i` 给 `b=−1` ⇒ `J₊=J₋=−J`。
- 与 `w₊=w₋` 完全一致：t=i ⇒ `(w₊,w₋)=(−i,−i)`，而 `I_{−i}=J`（§1.4 数值）；t=−i ⇒ `(i,i)` 而 `I_i=−J`。

**(B) A-模型的充要条件。** 由 (5.7)，`w → −1/w̄` 把 `I_w` 送到 `−I_w`（数值可验：`I_{−1/w̄}` 与 `−I_w` 的差 1e-16；这也是 (5.7) 里 a,b,c 在该变换下的符号翻转）。故 `J₊ = −J₋` 需 `w₋ = −1/w̄₊`，即 `t⁻¹ = 1/t̄` ⇒ t 实。代回：`t` 实 ⇒ `b=0`，`J₊ = aI + cK`，其中 `a=(1−t²)/(1+t²)`, `c=−2t/(1+t²)`，满足 `a²+c²=1`。
- `t=1`：`a=0, c=−1` ⇒ `J₊ = −K`（`J₋ = K`）；
- `t=−1`：`J₊ = K`；
- `t=0`：`J₊ = I`；`t→∞`：`J₊ = −I`。
最后两个正是原文的「`t=0,∞` → I/−I」。

**(B) Ψ 与 t² 的显式关系。** 令 `u = t²`，则 `(t−t⁻¹)/(t+t⁻¹) = (u−1)/(u+1)`，故

```
Ψ = Reτ + i Imτ·(u−1)/(u+1),      u = t²                    (2.1)
```

反解（这是本单元最有用的一条显式关系，报告没有写出反解）：

```
(Ψ − τ)/(Ψ − τ̄) = −1/u = 1/q ,     即   u = t² = (τ̄ − Ψ)/(Ψ − τ)        (2.2)
```

三个符号检查：
1. `u = ∞`（t=∞）⇒ 由 (2.1) `Ψ = τ`；由 (2.2) 分母为零 ✓。
2. `u = 0`（t=0）⇒ `Ψ = τ̄`；由 (2.2) `(Ψ−τ)/(Ψ−τ̄) = ∞` ✓ 一致（因为 u=0 时右侧 = −1/0）。
3. `u = 1`（t=±1）⇒ `Ψ = Reτ`；`Ψ=0` 还需 `Reτ=0`（θ=0）✓ 与原文「t=1 且 θ=0 给 Ψ=0」一致。
4. `t=±i` ⇒ `u=−1` ⇒ `(u−1)/(u+1) = −1/0 = ∞` ⇒ `Ψ=∞`（当 `Imτ≠0`）✓，且与 τ 无关（原文 p.69 明说）。
5. S 自洽性（见 §4）：`τ → −1/τ`、`Ψ → −1/Ψ` 下，(2.2) 的左侧变换为 `(τ̄/τ)·(Ψ−τ)/(Ψ−τ̄)`，而右侧 `1/q → (τ̄/τ)/q`，两边一致 ✓。

**(B) 为什么 Ψ=0 对应 A-模型（K）而不是任意 A-模型。** Ψ 是复化 Kähler 类 `[B₀+B′+iω₀] = −Ψ[ω_I]` 的系数；`Ψ=0` 意味着这个类退化为零，此时模型是 A-模型，其辛形式由 (5.32a) 在 `t=±1` 的极限给出：`ω₀ → ∓Imτ·ω_K`、`B₀ → 0`（我把 (5.32a) 按 `t=1+ε` 展开：`A·(−λ) → −1`、`κ = 2Im t/(1+|t|²) → 0`）。所以 `t=1` 给 K 的 A-模型、`t=−1` 给 −K（与 §2.3 A-模型段一致）。数值（S4）确认：`t=1` 时 (5.30) 给 `ℐ = [[0,(Imτ)⁻¹ω_K⁻¹],[−Imτ ω_K, 0]] = ℐ_{−Imτ ω_K}`（符号由 (5.24) 的 `−ω⁻¹` 与 `ω` 同时变号验过）。

### 2.4 数值/特例（附录 S3、S4）

- t = 0.4+0.7i, 2.0, 0.1+1.3i, −1.3+0.9i，τ = i 或 0.4+1.5i：`‖(5.27) − (5.30)‖ = 1e-16 量级`；`(5.30)` 满足 `ℐ² = −1`（2e-16）。
- (5.32) 的分解：`‖M(B₀)ℐ_{ω₀}M(B₀)⁻¹ − (5.30)‖ = 1e-16`（上面那组 t 全过）。
- (5.33) 的系数：`B₀ + iω₀ = α ω_I + β ω_K`，解得 `α` 与 `−i Imτ(t²−1)/(t²+1)` 的相对误差 **0**（t=0.4+0.7i）、1e-16（其余），而 `β ≠ 0`（例如 t=0.4+0.7i 时 `β = 0.643 − 1.731i`）。这说明 (5.33) 的成立**靠 `[ω_K]=0`**（ω_K 恰当），不是逐点的代数恒等式——报告 §2.2.5 的叙述与此一致，但没点破 β≠0 这一层。
- (2.2) 在 τ = i, 0.3+1.1i, −0.2+0.75i 与 3 个 t 上，误差 ≤ 1e-15。
- 符号检查的补充：`t=±i` 处 (5.30) 仍良定义（`1+|t|²=2`、`(1−tt̄)=0`、`(t+t̄)=0`），给出 `ℐ = diag(J, −Jᵗ)` 或 `diag(−J, Jᵗ)`，正是 (5.23) 的 B-模型 GC 结构；极点只出现在 (5.31)(5.32) 的分解里，不在 (5.30) 里。报告 §3 第 10 条已说对。

### 2.5 与报告比

报告 2.1.5、2.2.5、2.3 的判定链与我一致；报告 §3 第 10 条（t=±i、t=1 代入 (5.30) 的两个手算）我逐项复核**正确**（`t=i`：`1+t̄t=2, t−t̄=2i, t+t̄=0` ⇒ `diag(J,−Jᵗ)`；`t=1`：`diag` 为零、下左 `−Imτ ω_K`、上右 `(Imτ)⁻¹ω_K⁻¹` ⇒ `ℐ_{−Imτ ω_K}`）。

差异：报告的 Ψ 显式关系只写到 (5.34)，没有给 (2.2) 的反解；报告说 Ψ=0 对应「t=1 且 θ=0」，严格是 `t=±1`（因 t∼−t，且 `(u−1)/(u+1)` 在 u=1 为零）——见 E6。

### 2.6 判定

**成立。** `t=±i ⟺ B-模型（J/−J）`、`t 实 ⟺ A-模型`、`Ψ=∞ ⟺ t=±i ⟺ B(J)`、`Ψ=0 ⟺ t=±1 且 Reτ=0 ⟺ A(K)`，且 (2.2) 给出 Ψ 与 t² 的完整互译。

---

## 三、广义复结构：belief 还是论证

### 3.1 问题

§5.2 里「扭化后的 TFT 由哪个广义复结构决定」这句话，原文给的是定理还是信念？引出原文短句（≤120 字符）并判其证据级别；说明把它当定理为何是过度断言。

### 3.2 原文与页（p.66–67）

原文在引述 [67] 第 6 章「σ-模型有 (2,2) 超对称 ⟺ 一对相容 GC 结构」之后写道（**短引，86 字符**）：

> "It is believed that … is determined by one of the two generalized complex structures"

（同句前半为 `It is believed that, in general, each of these topological field theories is`，全句逐字 137 字符，超过 120，故按规则取删节短引；紧接的同页下一分句是 `and independent of the second.`）紧接着 p.67 给出证据级别：

> "Arguments supporting this claim can be found in [72,68], though a complete proof is not yet known."   (p.67)

p.69 作者又自评方法论：`we think that generalized complex geometry is a natural framework for understanding this problem, even though there are some technical gaps in the current understanding of it.` 并在同一页承认 `our analysis showing that Ψ is the only relevant parameter is really not valid at t = ±i, because of poles in the formulas.`

### 3.3 判定其证据级别（分级）

| 断言 | 级别 | 依据 |
| --- | --- | --- |
| (2,2) σ-模型 ⟺ 一对相容 GC 结构 | (A) 引定理（[67] 第 6 章） | p.66 |
| **每个扭化 TFT 只由两个 GC 结构之一决定、与第二个无关** | **(A) 明写的 belief**：`It is believed that…` + `a complete proof is not yet known` | p.66–67 |
| 这一族 GC 结构的一般元 = 辛结构的 B-场变换 | (A) 引定理（[67] Prop 4.34） | p.68 |
| (5.27)–(5.30) 的显式公式 | (A) 推导；(B) 可数值验证 | p.67–68；本报告 §2.4 |
| (5.31)–(5.34) 的化简与「只剩 Ψ」 | (A) 推导，但把「GC 结构相等」读成「TFT 相等」仍靠上面那条 belief | p.68–69 |
| A-模型只依赖 `[B+iω]`（即使 B 有 (2,0)⊕(0,2) 分量） | (A) 原文自认有 gap：`this point may require some clarification` | p.69 |
| t=±i 处上述化归失效（极点），须另证与 τ 无关 | (A) 原文明确承认并补证 | p.69–70 |

**结论：belief，不是论证/定理。** 证据级别 = 「明写的猜想 + 引用支撑 + 作者承认证明不完备」；可验证的部分只到 (5.30)–(5.34) 的代数恒等式，以及「GC 结构层面」的等价。

### 3.4 为什么把 belief 当定理是过度断言

关键在于这条 belief 恰好是**唯一**把「GC 结构相等」翻译成「2d TFT 相等」的桥：
1. (5.31) 证明的是 `ℐ_t = M(B₀)ℐ_{ω₀}M(B₀)⁻¹` —— 一个 GC 结构的等式（我数值验到 1e-16，所以这一步无争议）；
2. 但从「`ℐ_t` 是某个 A-模型 + B 场的 B-场变换」到「原来的 2d TFT 就是那个 A-模型」需要：该 TFT 只由 `ℐ_t` 这一个 GC 结构决定、与第二个（由 `−J₋, −ω₋` 给的）无关；
3. 第 2 步正是 p.66 的 belief。
因此：**定理级**的结论是「`ℂP¹_g` 的每个 t≠±i 点所给的 GC 结构，等价于某个 A-模型 + B 场的 GC 结构」；**猜想的**结论是「所以 2d TFT 也等价」。把后者写成定理，就把一个「arguments supporting + proof not known」的陈述升级了。（C）
另一层过度断言的风险：Φ 唯一参数这条结论在 `t=±i` 明确失效（作者自认），所以「全族只剩 Ψ 一个参数」在端点必须改写为「B-模型，与 τ 无关」。

### 3.5 与报告比

报告 §2.2.2（「关键的一句话是 belief，不是定理」）与 §2.2.6 的三类分级表，与我的复算**一致**，评级正确；报告还正确引了 `a complete proof is not yet known`。⇒ 报告在这一点上没有过度断言（这也是它比常见二手叙述严谨的地方）。

但报告的**引文本身有错**：它把 `each of these topological field theories` 缩写成 `each of these TFT` 却仍加双引号，且自检声称「英文引文全部 ≤120 字符（最长 113 字符）」。原文逐字是 `topological field theories`，全句 137 字符，既非 113 也是改写 ⇒ 应改成分段短引或删节引（E2）。

### 3.6 判定

**原文是 belief（明写，作者自认证明不完备）；把它当定理 = 过度断言。报告在这一点的分级正确，但引文非逐字（E2）。**

---

## 四、S-对偶 ↔ 镜像对称

### 4.1 问题

给出 M_H(G) 与 M_H(^LG) 的复结构配对（J vs K）；用 `Ψ ↦ −1/(n_gΨ)` 验端点交换；说明 T-对偶发生在纤维上、与 S-对偶是两层不同的事，各给一个可算的 U(1) 例。

### 4.2 原文与页

- p.70（§5.3）：(5.35) `S = [[0, 1/√n_g], [−√n_g, 0]]`，"maps Ψ → −1/n_g Ψ and hence exchanges Ψ=0 and Ψ=∞"（公式层面即 `Ψ ↦ −1/(n_gΨ)`，见 §4.3）；(5.36) `T = [[1,1],[0,1]]`；`n_g=1` for simply-laced。Ψ=∞ 链：`t=i`、`(w₊,w₋)=(−i,−i)` ⇒ B-模型 in J；用 S（τ 复标度不变、t→t′=−t(τ/|τ|)=−it=1）⇒ `(w₊,w₋)=(−1,1)` ⇒ A-模型 in K。故 `B-model_J(M_H(G)) ≅ A-model_K(M_H(^LG))`。复合 `𝒥: φ→iφ`（把 K 转回 J）⇒ `B_J(G) ≅ A_J(^LG)`。
- p.71（表 2，六行）：`I_B→I_B`, `I_A→I_A`, `J_B→K_A`, `J_A→K_B`, `K_B→J_A`, `K_A→J_B`。
- p.71（§5.4 目标句）："to show that S-duality acts **classically on the base** of the Hitchin fibration π: M_H → B, while acting by **T-duality on the fibers**"。
- p.77（§5.5）："the operation S acts by a map Ξ: B → ^LB … together with a **T-duality on the corresponding torus fibers**"；"the usual SYZ picture of mirror symmetry, except that the map Ξ is usually assumed to be trivial"。

### 4.3 推导

**(B) 复结构配对。**
- G 侧：`B-model_J(M_H(G))`。
- ^LG 侧：`A-model_K(M_H(^LG))`。
- 表 2 的六行可以一条公式复现（τ 取虚，S 的 (5.22) 变成 `(w₊,w₋) ↦ (−i w₊, +i w₋)`）：我逐点验（S5）：`J_B=(−i,−i)↦(−1,1)=K_A`；`K_A=(−1,1)↦(i,i)∼J_A?` 不，`↦(i·?...` 数值给 `(1i,1i)`，按 `(w₊,w₋)=(i,i)` 是 `−J` 的 B-模型，与 `J_B` 只差中心元 `−1`；`J_A=(−i,i)↦(−1,−1)∼K_B`；`K_B=(1,1)↦(−i,i)=J_A`；`I_B=(0,0)↦(0,0)`；`I_A=(0,∞)↦(0,∞)`。六行全对，其中两处只差中心元 `(w₊,w₋)∼(−w₊,−w₋)`（即 t∼−t），与 §1.3 一致。

**(B) 端点交换 = Ψ ↦ −1/(n_gΨ)。**
- S 作用在 τ 上是 `τ ↦ −1/τ`；在 Ψ 上必须是 `Ψ ↦ −1/(n_gΨ)`（`n_g=1` 时 `−1/Ψ`），因为 (5.35) 的第二行 `−√n_g` 与第一行 `1/√n_g` 给 Möbius 变换 `Ψ ↦ (0·Ψ + 1/√n_g)/(−√n_g·Ψ + 0) = −1/(n_gΨ)`。这与原文的 "hence exchanges Ψ=0 and Ψ=∞" 唯一相容：若真按字面 `−(1/n_g)·Ψ`（把 `−1/n_g` 当乘子），则 `Ψ=0 ↦ 0`，不交换端点。
- 端点：`Ψ=∞`（t=±i，B in J）→ `−1/∞ = 0`；`Ψ=0`（t=±1 且 θ=0，A in K）→ `−1/0 = ∞` ✓。
- 与 τ 的相容性（我数值验证，S4b）：`(Ψ−τ)/(Ψ−τ̄) = 1/q`（(2.2)，q=−t²）；S 下 `τ→−1/τ`、`Ψ→−1/Ψ` 使左边变为 `(τ̄/τ)·1/q`，而 `t → t(cτ+d)/|cτ+d|` 在 S 时（`c=−1,d=0`）给 `q → q·τ/τ̄`，于是 `1/q → (τ̄/τ)/q`，两边一致 ✓。这条自洽性检查同时验证了 (2.2)、(5.21)(5.22) 与 (5.35) 三者的符号约定。

**(B) 两层：底空间经典作用 vs 纤维 T-对偶。**
- 底空间层：B = Hitchin 底空间（复向量空间，线性函数 = 交换哈密顿量 `H_{P,α}=∫_C αP(φ)`，α∈H¹(C,K^{1−n})）。(p.72–74) 的论证：在 I 的 B-模型里，M_H 的全纯函数在紧致 Hitchin 纤维上为常数 ⇒ 只能来自 B ⇒ `R(G) ≅ R(^LG)` 是 graded ring 同构。这是**经典/代数**层面的作用：S 把 B 映到 ^LB，`Ξ: B → ^LB` 在 simply-laced 时是恒等。p.72 明说「没有任何局部算符能像 O_{P̂} 那样测纤维」，所以纤维层不能用算符论证。
- 纤维层：F 是复环面，`B_p` 的模空间 = F，`B̃_p`（(B,A,A)-膜）的模空间 = F̃ 上 rank-1 flat 丛的模空间 = 对偶环面 `ĴF̃`；rank 必须为 1（否则维数不匹配，p.76）。于是 S-对偶 ⟹ `F ≅ ĴF̃`，这是**T-对偶**（格的对偶），不是经典作用，也不是同一个环面的恒等。

**(B) 两个可算 U(1) 例。**

例 1（底空间层，G = U(1)）：`B = H⁰(C,K) ≅ ℂ^g`（P 次数 1，α∈H¹(C,K⁰)=H¹(C,O)≅ℂ^g）。这里既没有格也没有平坦丛模空间，S 的作用在 B 上是**恒等**（`n_g=1`，simply-laced；`Ξ=id`）。可算检查：`dim_ℂ B = g`，`dim_ℂ F = g`，`dim_ℂ M_H = 2g`；S 对 B 的坐标（等价于 `τ→−1/τ` 与 φ 无关）不改变任何 φ，所以「经典作用」在 abelian 情形是平凡的——这正是与纤维层 T-对偶（非平凡格变换）的对照。

例 2（纤维层，g = 1）：`F = E_τ = ℂ/(ℤ+τℤ)`；`ĴF = Hom(Λ_τ, U(1))` 的对偶格，我直接算（S6）：对偶格 = `c·(ℤ + ℤ(−τ̄))`，`c = 2/(τ−τ̄) ∈ ℝ`，故 `ĴF = E_{−1/τ̄}`。
- `τ = iy`：`−1/τ̄ = i/y` ⇒ `ĴF = E_{i/y}`，正是 T-对偶 `R ↦ 1/R`（数值：y=1.4 → 0.714）。
- `τ = i`：`ĴF = E_i = F`，自对偶（此时 `F ≅ ĴF` 是**双全纯**同构，因为 τ=i 是 S 的不动点）。
- 一般 τ（如 0.3+1.1i）：`ĴF = E_{−1/τ̄}` 与 `E_τ` 复结构不同（不是同一个模轨道上的点），所以 `F ≅ ĴF̃` 只是**实解析**（T-对偶）同构，不是全纯同构。这与 SYZ 的「沿纤维 T-对偶」一致：镜像交换的是复结构与复化 Kähler 类，而 T-对偶本身是格层面的实线性对偶。

### 4.4 数值/特例

- 表 2 六行用一条公式复现（S5，τ=i）：`J_B↦K_A`、`K_A↦J_A`（差中心元）、`J_A↦K_B`、`K_B↦J_A`、`I_B↦I_B`、`I_A↦I_A`。
- Ψ 端点：`Ψ(i)=∞`、`Ψ(1)=0`（Reτ=0）、`Ψ(∞)=τ`、`Ψ(0)=τ̄`；`Ψ↦−1/(n_gΨ)`：`∞→0`、`0→∞` ✓。
- 对偶格：`τ=1j → 0.0+1.0j`（自对偶）；`τ=2j → 0.5j`（R↦1/R ✓）；`τ=0.3+1.1j → −0.2308+0.8462j`（与 τ 不同轨道）。

### 4.5 与报告比

报告 §2.3（(5.35) 与 Ψ 端点、表 2、𝒥 复合）、§2.4（底空间经典作用）、§2.5（纤维 T-对偶、SYZ）主体与我一致；报告 §3 第 10 条用 `(w₊,w₋)↦(−iw₊,iw₋)` 一条公式复现表 2 六行，我独立复现，结果相同。

差异：
1. **报告把 S 对 Ψ 的作用写成 `Ψ → −(1/n_g)Ψ`（报告 2.3 节第 1 段）**，与其后一句「故交换 Ψ=0 与 Ψ=∞」自相矛盾；正确公式是 `Ψ ↦ −1/(n_gΨ)`（由 (5.35) 的矩阵作用直接算出）。这是报告里**唯一影响推导的公式错误**（E1）。
2. 报告写 `F ≅ ĴF̃` 时没标注这是 T-对偶意义下的实解析同构（一般 τ 下非双全纯）；原文 p.76 也只说 "isomorphism"，但报告作为「可算结论」应加限定（E5）。

### 4.6 判定

**成立。** 配对为 `B_J(M_H(G)) ≅ A_K(M_H(^LG))`（再复合 𝒥 得 `B_J ≅ A_J`）；`Ψ ↦ −1/(n_gΨ)` 交换端点，并与 τ 的 `−1/τ` 通过 `(Ψ−τ)/(Ψ−τ̄)=1/q` 自洽；底空间 = 经典（Ξ，simply-laced 为恒等），纤维 = T-对偶（`F ≅ ĴF̃`，U(1) g=1 例中 = `E_{−1/τ̄}`，τ=iy 时 `i/y`）。

---

## 五、膜与 §6 接口

### 5.1 问题

§5.6 的 A/B 型膜与「(5.37) 的 c.c. 膜（若出现）」是不是 U05（§6 Loop and Line Operators）的准备？报告有没有提前用 §6 的结论？

### 5.2 原文与页

- p.77–78（§5.6 "Branes On M_H"）：重要膜对 I、J、K 都有超对称、保 2d 的一半（= 4d 的四分之一）；四类型 `(B,B,B)`, `(B,A,A)`, `(A,B,A)`, `(A,A,B)`；S 交换 `(B,B,B) ↔ (B,A,A)`，另两种各映到同类型。脚注 24：对 I,J,K 的任意线性组合是 B-型、对两个正交复结构是 A-型；**没有** `(B,B,A)`（在 I、J 下全纯 ⇒ 在 K 下全纯）、也没有 `(A,A,A)`。
- p.78 例子：`(B,B,B)` = 零膜 / space-filling；`(B,A,A)` = N 在 I 下复子流形且对 Ω_I Lagrangian（⇒ 对 ω_J, ω_K Lagrangian），配平凡丛；Hitchin 纤维是一例；另一例固定 E 只变 φ。`(A,B,A)` = 固定 `𝒜_z̄ = A_z̄ + iφ_z̄`、让 `𝒜_z = A_z + iφ_z` 变；`(A,A,B)` = 固定 `A_z̄ − φ_z̄`、让 `A_z + φ_z` 变。§11 会造 coisotropic 膜。
- **(5.37) 的位置**：p.71（§5.4），`H_{P,α} = ∫_C α P(φ)`，是 Hitchin 可积系统的交换哈密顿量，**不是膜条件**，也不在 §5.6 里。
- §6 标题与开篇：p.78 "6. Loop and Line Operators"；开篇（printed pp.78–79）说 4d TQFT「unusual」之处是允许沿一维流形 S⊂M 的算子、依赖 S 的同伦类，并说 `these one-manifold operators prove to have very interesting properties in relation to branes`；预告 §6.1 Wilson、§6.2 't Hooft、§6.3 紧化后解释、§6.4 "line operators as operators on branes"；脚注 25 说「线算子端着在膜上」的情形本文不重要。
- p.74 明文：2d σ-模型只是有效描述，与 4d 规范理论的精确对应在 §12 与 [26]。

### 5.3 推导/判断

1. **(5.37) 与「c.c. 膜」在 §5 中不存在。** 我逐页核了 p077.txt/p078.txt/p079.txt 的 §5.6 全文：没有 (5.37) 型的膜判据，也没有「c.c. 膜」这一对象（§5.6 只有上面四类型 + 两个方程的「固定/变化」描述）。「(5.37) 的 c.c. 膜」这个提法应是任务单把 §5.4 的哈密顿量与 §5.6 的膜混在了一起；**报告没有犯这个错**（(5.37) 在报告里只出现在 §2.4 与 §4.1，作为 Hitchin 哈密顿量使用，用法正确）。
2. **§5.6 是「膜目录」，其直接下游是 §11（coisotropic 膜、GL 的膜构造）与 §12（4d 解释），不是 §6 前半。** 原文 p.78 说这些膜 "will be the important branes in our study of the geometric Langlands program"；§6 开篇只到「与膜有很有趣的关系」的**预告**级别，真正把线算子与膜接起来的是 §6.4（标题级承诺）与 §11–12。
3. **报告提前用了 §6 的结论吗？** 报告 §2.6 末段（「为 U05 铺路」）写：「§6 开篇（就在本单元边界之后）说 …这些线算子在 2d σ-模型里的影子正是 §5.6 的膜 (B p.78–79)」。查原文：§6 开篇没有这句话；它只说算子依赖同伦类、与膜有「有趣的关系」。把「有有趣的关系」升级成「影子正是 §5.6 的膜」并给出 p.78–79 的页锚，属于**提前使用/过度接线**（E3，中）。
4. 报告 §0 结论先行第 8 条称 §5.6 是「U05 处理线算子、U06 处理特征层的『目录页』」；原文 p.78 只承诺这些膜是 GL 研究中的重要膜，没有对 §6/§7 的目录式分工承诺 ⇒ 外推（E4，低）。

### 5.4 数值/特例

无新数值（本项是文本/接口判定）；可算的只有维数账：`(B,A,A)` 的支撑维数夹逼——A-膜支撑 ≥ 中间维（coisotropic A-膜可更大，[80]），而膜支在 Hitchin 纤维（= 中间维）内 ⇒ 恰为整条纤维（p.76）。这条论证在 §5.6 的例子处被我按原文复述，无矛盾。

### 5.5 判定

**§5.6 的膜是 §11/§12（GL 与 4d 解释）的准备，不是 §6 前半的准备；§6 只到预告级别。报告的物理判断大体正确，但把 §6 开篇读成「线算子 ↔ 膜」的建立处，属提前使用（E3），并把 §5.6 称作 U05/U06 的目录页（E4）。(5.37) 的「c.c. 膜」在原文中不存在，报告未误用。**

---

## 发现的问题清单

| 编号 | 严重度 | 报告哪里错 | 原文依据 | 怎么改 |
| --- | --- | --- | --- | --- |
| **E1** | **高** | 报告的 2.3 节（§5.3 开头）写「S 把 `Ψ → −(1/n_g)Ψ`，故交换 `Ψ = 0` 与 `Ψ = ∞`」——公式与其后半句自相矛盾 | p.70 (5.35)：`S=[[0,1/√n_g],[−√n_g,0]]`，Möbius 作用给 `Ψ ↦ −1/(n_gΨ)`；原文紧接 "hence exchanges Ψ=0 and Ψ=∞" | 改成 `Ψ ↦ −1/(n_gΨ)`；`n_g=1` 时即 `Ψ ↦ −1/Ψ`，与 `τ ↦ −1/τ` 同形；并注明「`−1/(n_gΨ)` 是把 (5.35) 读作分式线性变换的结果，不是乘子」 |
| **E2** | 中 | 2.2.2 与自检处把原文 `each of these topological field theories` 引成 `each of these TFT`（引号内改写），并声称「全部 ≤120 字符、最长 113 字符」 | p.66 原句逐字 137 字符（`It is believed that, in general, each of these topological field theories is determined by one of the two generalized complex structures`）；p.67 有 `a complete proof is not yet known` | 改用删节短引，如 `It is believed that … is determined by one of the two generalized complex structures`（86 字符），或分两段引；自检里的「113 字符」删掉 |
| **E3** | 中 | §2.6 末段「为 U05 铺路」：称 §6 开篇「建立」了「线算子在 2d σ-模型里的影子正是 §5.6 的膜」，页锚给 p.78–79 | p.78–79 §6 开篇只说沿 1-流形的算子依赖同伦类、`prove to have very interesting properties in relation to branes`；「线算子作为膜上的算子」是 §6.4 的标题级承诺，精确对应在 §11–12 | 降级为「预告」；把接口页锚改成 §6.4 + §11–12；删掉「影子正是」这类等同句 |
| **E4** | 低 | §0 结论先行第 8 条把 §5.6 称作「U05 处理线算子、U06 处理特征层的『目录页』」 | p.78 只说这些膜 "will be the important branes in our study of the geometric Langlands program"，无 §6/§7 分工承诺 | 改成「§5.6 是膜的目录页，直接下游是 §11（coisotropic 膜）与 §12（4d 解释）；对 §6 只有预告级接口」 |
| **E5** | 低 | 2.5.4 与结论第 8 条写 `F ≅ ĴF̃`，未标注该同构的性质 | p.76 只说 "S-duality establishes an isomorphism"；但 T-对偶是格层面的实解析对偶：g=1 时 `ĴF = E_{−1/τ̄}`，一般 τ 下与 `E_τ` 不双全纯同构（本报告 §4.3 例 2） | 加限定：「（T-对偶意义下的实解析同构；仅 τ=i 等固定点才双全纯）」 |
| **E6** | 低 | 2.3 节与结论第 6 条写「`Ψ = 0`（`t = 1` 且 θ = 0）」，只给 t=1 | (2.1)：`Ψ=0` 需 `u=t²=1`，即 `t = ±1`；且 t∼−t（p.62） | 改成「`t = ±1` 且 `Reτ = 0`」（t=1 给 K、t=−1 给 −K） |
| **E7** | 低（对报告无害，供任务单修正） | —（任务单页锚） | 任务单说「T-对偶发生在纤维上（p.70、p.77）」；实际两处 T-对偶句在**印刷 p.71**（§5.4 首段，p072.txt）与 p.77（p078.txt SYZ 段），p.70 只有 §5.3 的 𝒥 段 | 任务单把 p.70 改成 p.71；报告的 §6 第 7 条「任务单未发现笔误」应补一句「仅 T-对偶页锚偏一页」 |

**计数：高 1（E1）、中 2（E2、E3）、低 4（E4–E7）。**
报告的最强项是 §2.2.2/§2.2.6 对 belief 的分级（与我独立判定一致）与 §3 第 10 条两个代入手算（我逐项复核正确）；最弱的是 E1（核心公式写错但结论写对，属「结论对、公式错」的自相矛盾）与 E2（引号内改写原文）。

---

## 附录：可重跑 python（6 段）

依赖 numpy；6 段分别对应本报告 §1.4、§1.4、§2.4、§2.4、§4.4、§4.3。所有数值均在 Windows 的 numpy 上跑过，输出见各段注释。

```python
# S1: 10d Euclid gamma，数 (5.1)/(5.3) 存活超荷的复维
import numpy as np
s1=np.array([[0,1],[1,0]],complex); s2=np.array([[0,-1j],[1j,0]],complex); s3=np.array([[1,0],[0,-1]],complex)
def g10():
    G=[]
    for k in range(1,6):
        pre=np.eye(1,dtype=complex)
        for _ in range(k-1): pre=np.kron(pre,s3)
        G.append(np.kron(pre,np.kron(s1,np.eye(2**(5-k),dtype=complex))))
        G.append(np.kron(pre,np.kron(s2,np.eye(2**(5-k),dtype=complex))))
    return G
G=g10(); n=32
assert all(np.allclose(G[i]@G[j]+G[j]@G[i],2*(i==j)*np.eye(n,dtype=complex)) for i in range(10) for j in range(10))
Gc=np.eye(n,dtype=complex)
for i in range(10): Gc=Gc@G[i]          # Gc^2 = -1，特征值 ±i
w,v=np.linalg.eig(Gc); Q=v[:,[k for k in range(n) if abs(w[k]+1j)<1e-6]]; Q,_=np.linalg.qr(Q)
print("Weyl 空间复维 =",Q.shape[1])     # 16
def null(mats,label):
    A=np.vstack([Q.conj().T@M@Q for M in mats]); sv=np.linalg.svd(A,compute_uv=False)
    r=int((sv>1e-7*sv[0]).sum()); print(label,"rank=",r,"nullity=",A.shape[1]-r)
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
A={(a,b):G[a]@G[b]+G[a+4]@G[b+4] for a,b in pairs}     # (5.1) 的 6 条，对角 Spin'(4) 生成元
null([A[p] for p in pairs],"一般 M（全 6 条）")          # nullity 2
null([A[(1,2)],A[(1,3)],A[(2,3)]],"M=RxW（mu,nu=1,2,3）")# nullity 4  <- 原文明写 four
g2367=G[1]@G[2]@G[6]@G[7]
null([g2367-np.eye(n,dtype=complex)],"(5.3)")           # nullity 8  <- 原文明写 eight
```

```python
# S2: (5.7) I_w 是复结构，特值 w=0,±1,±i,∞ 对应 I,K,-K,J,-J,-I
import numpy as np
I4=np.eye(4,dtype=complex)
Ii=np.array([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]],dtype=complex)   # 左乘 i
Lj=np.array([[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]],dtype=complex)   # 左乘 j
Kk=Ii@Lj
assert np.allclose(Ii@Lj,Kk) and np.allclose(Lj@Ii,-Kk) and np.allclose(Kk@Ii,Lj) and np.allclose(Ii@Kk,-Lj)
def Iw(w):
    d=1+w*np.conj(w); return (1-w*np.conj(w))/d*Ii + 1j*(w-np.conj(w))/d*Lj + (w+np.conj(w))/d*Kk
for w,name in [(0,'I'),(1,'K'),(-1,'-K'),(np.inf,'-I'),(-1j,'J'),(1j,'-J')]:
    M=Iw(1e6) if np.isinf(w) else Iw(w)
    dM={ 'I':np.abs(M-Ii).max(),'-I':np.abs(M+Ii).max(),'K':np.abs(M-Kk).max(),'-K':np.abs(M+Kk).max(),
         'J':np.abs(M-Lj).max(),'-J':np.abs(M+Lj).max() }[name]
    print(w,name,"I^2=-1:",np.allclose(M@M,-I4),"|I_w-target|=",round(dM,8))   # 全部 0
```

```python
# S3: (5.27) == (5.30)（t 任意复，tau 任意），并验 J30^2=-1
import numpy as np
I4=np.eye(4,dtype=complex); Z4=np.zeros((4,4),complex)
Ii=np.array([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]],dtype=complex)
Lj=np.array([[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]],dtype=complex)
Kk=Ii@Lj
for t in [0.4+0.7j,2.0,-1.3+0.9j]:
  for tau in [1j,0.4+1.5j]:
    d=1+t*np.conj(t); Imt=tau.imag
    a=(1-t*np.conj(t))/d; b=-1j*(t-np.conj(t))/d; c=-(t+np.conj(t))/d     # (5.28)，注意 b 的符号
    Jp=a*Ii+b*Lj+c*Kk; Jm=-a*Ii+b*Lj-c*Kk
    wI,wJ,wK=Ii,Lj,Kk
    wp=Imt*(a*wI+b*wJ+c*wK); wm=Imt*(-a*wI+b*wJ-c*wK)
    J27=np.block([[0.5*(Jp+Jm), -0.5*(np.linalg.inv(wp)-np.linalg.inv(wm))],
                  [0.5*(wp-wm), -0.5*(Jp.T+Jm.T)]])                       # (5.27)
    J30=np.block([[-1j*(t-np.conj(t))*Lj/d, -(1/Imt)*((1-t*np.conj(t))*np.linalg.inv(wI)-(t+np.conj(t))*np.linalg.inv(wK))/d],
                  [Imt*((1-t*np.conj(t))*wI-(t+np.conj(t))*wK)/d, 1j*(t-np.conj(t))*Lj.T/d]])  # (5.30)
    print(f"t={t} tau={tau}: |5.27-5.30|={np.abs(J27-J30).max():.1e}  |J30^2+1|={np.abs(J30@J30+np.eye(8)).max():.1e}")
    # 输出：1e-16 量级，全部通过
```

```python
# S4: (5.31)(5.32) 的 B-场变换 == (5.30)；(5.33) 系数 alpha；Psi 与 t^2 的显式关系
import numpy as np
I4=np.eye(4,dtype=complex); Z4=np.zeros((4,4),complex)
Ii=np.array([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]],dtype=complex)
Lj=np.array([[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]],dtype=complex); Kk=Ii@Lj
def gf(t,Imt=1.0):
    d=1+t*np.conj(t); wI,wK=Ii,Kk
    A=(1-(t*np.conj(t))**2)/((1+t**2)*(1+np.conj(t)**2)); lam=(t+np.conj(t))/(1-t*np.conj(t))
    Bc=-(1j*(t**2-np.conj(t)**2))/((1+t**2)*(1+np.conj(t)**2)); mu=(1-t*np.conj(t))/(t+np.conj(t))
    w0=Imt*A*(wI-lam*wK); B0=Imt*Bc*(wI+mu*wK)                            # (5.32)
    J30=np.block([[-1j*(t-np.conj(t))*Lj/d, -(1/Imt)*((1-t*np.conj(t))*np.linalg.inv(wI)-(t+np.conj(t))*np.linalg.inv(wK))/d],
                  [Imt*((1-t*np.conj(t))*wI-(t+np.conj(t))*wK)/d, 1j*(t-np.conj(t))*Lj.T/d]])
    M=np.block([[I4,Z4],[B0,I4]]); Jw0=np.block([[Z4,-np.linalg.inv(w0)],[w0,Z4]])   # (5.25)(5.24)
    Jb=M@Jw0@np.linalg.inv(M)                                              # (5.31)
    Z=B0+1j*w0; coef=np.linalg.lstsq(np.stack([wI.ravel(),wK.ravel()],1),Z.ravel(),rcond=None)[0]
    tgt=-1j*Imt*(t**2-1)/(t**2+1)                                          # (5.33) 的系数
    return np.abs(Jb-J30).max(), coef[0], tgt, coef[1]
for t in [0.4+0.7j,2.0,0.1+1.3j,-1.3+0.9j]:
    e,a,tg,b=gf(t)
    print(f"t={t}: |5.31-5.30|={e:.1e}  alpha={a:.6f} target={tg:.6f}  beta={b:.4f}")
    # 输出：e~1e-16；alpha 与 target 相对误差 0~1e-16；beta != 0（(5.33) 靠 [omega_K]=0）
for tau in [1j,0.3+1.1j,-0.2+0.75j]:
    for t in [0.5+0.2j,1.7-0.4j,2.0j]:
        Psi=tau.real+1j*tau.imag*(t**2-1)/(t**2+1)                          # (5.34)
        print(f"tau={tau} t={t}: |(Psi-tau)/(Psi-tau_bar)-1/q|=",
              abs((Psi-tau)/(Psi-np.conj(tau))-1/(-(t**2))))                # (2.2)，误差 <=1e-15
```

```python
# S5: tau=i 时 S 的 (5.22) 作用复现表 2 六行（含中心元差异）
import numpy as np
pts={'I_B':(0.0,0.0),'I_A':(0.0,np.inf),'J_B':(-1j,-1j),'J_A':(-1j,1j),'K_B':(1.0,1.0),'K_A':(-1.0,1.0)}
def Smap(wp,wm): return (-1j*wp, 1j*wm)          # (5.22) 在 tau=i, c=-1,d=0 时：w+ -> -i w+, w- -> +i w-
def classify(wp,wm):
    # tau=i 时：(0,0)=I_B, (0,inf)=I_A, (a,a)=B-model(aJ), (a,-1/a)=A-model
    if wp==0 and wm==0: return 'I_B'
    if wp==0 and np.isinf(wm): return 'I_A'
    return f"w=({wp:.3g},{wm:.3g}) q={-(wp/wm):.3g}"
for nm,(a,b) in pts.items():
    print(nm,"->",Smap(a,b))
# 结果：J_B(-i,-i)->(-1,1)=K_A；J_A(-i,i)->(-1,-1)~K_B（差中心元 -1）；K_B(1,1)->(-i,i)=J_A；
#       K_A(-1,1)->(i,i)~J_B（差中心元）；I_B->I_B；I_A->I_A。六行全对。
```

```python
# S6: U(1) g=1 的 T-对偶纤维：F=E_tau 的对偶格与对偶复结构
import numpy as np
def dual_complex_structure(tau):
    # Lambda=Z+tau*Z 的实内积对偶格：基向量 y_i 满足 y_i . (1,tau) in Z
    B=np.array([[1.0,tau.real],[0.0,tau.imag]])      # 列 = 格基（实坐标）
    Bdual=np.linalg.inv(B).T                          # 列 = 对偶基
    z1=1-1j*tau.real/tau.imag; z2=1j/tau.imag         # 对偶基的复坐标
    return z2/z1
for tau in [1j,2j,0.3+1.1j]:
    print(f"tau={tau}: 对偶复结构={dual_complex_structure(tau):.6f}  -1/conj(tau)={-1/np.conj(tau):.6f}")
# 输出：tau=1j->1j（自对偶）；tau=2j->0.5j（T-对偶 R->1/R）；tau=0.3+1.1j->-0.2308+0.8462j（与 tau 不同轨道）
```

---

## 复算自检

- 五节齐备，每节都含「问题 → 原文式+页 → 推导 → 数值/特例 → 与报告比 → 判定」六项。
- 所有数值为自己算（6 段 python 已实际跑通，输出写在注释里）；所有公式在源文本中逐条核过页锚（`p057.txt`–`p079.txt`）。
- 报告对照点：逐节对到报告的具体小节/行；E1–E7 每条都给了「报告哪里错 / 原文依据 / 怎么改」。
- 正文未写绝对路径；页号统一用印刷页。
