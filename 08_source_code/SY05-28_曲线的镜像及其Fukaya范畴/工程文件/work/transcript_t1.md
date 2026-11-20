# Talk 1 逐页速记（读图所得，供通读笔记与翻译底稿）

记号约定：`->` 表示原稿的箭头/推出；`[?]` 表示字迹难辨处，编号对应 `02_疑点清单.tsv`。

## t1-01（原稿第 1 页）

标题：D. Auroux — Mirrors of curves and their Fukaya categories — Miami, Jan 27-28-29 2020 — Talk 1

- 设定：给定超曲面 H^{n-1}［系数域为非阿基米德域，例如 Novikov 域；最简单的情形不需要］（例如热带极限附近的复超曲面退化族），嵌入代数环面、环簇或阿贝尔簇 V^n
  -> 镜像 Landau–Ginzburg 模型 (Y,W)，其中 Y 是 Calabi–Yau (n+1) 维（原稿 (n+1)-fld），W ∈ O(Y) 是超势。（依赖于嵌入的选取）
- Contribution（Abouzaid–A.–Katzarkov，经 SYZ；另见较早的 Hori–Vafa、Clarke、…、Chan–Lau–Leung、…）：
  H = f^{-1}(0)，f(x) = Σ_{α∈A⊆Z^n} c_α t^{ρ(α)} x^α 为 Laurent 多项式（t→0）
  => 热带化 φ(ξ) = max_{α∈A}(⟨α,ξ⟩ − ρ(α))
- ★ 令 (Y,ω) 为环 Calabi–Yau，矩多胞形 Δ_Y = {(ξ,η) | η ≥ φ(ξ)} ⊆ R^{n+1}，
  W_0 = −z^{(0,…,0,1)} 为环单项式，在每个环除子上零化 1 阶
  => (Y,W_0) 是 H ⊂ (C*)^n 的镜像（例如 SYZ 镜像给出一个沿 H 具 Morse–Bott 奇点的 LG 模型）
- 例 (1)：z_1+z_2+1 = 0 ——(热带化：η ≥ max(0,ξ_1,ξ_2))——> Y ≅ C^3，w_0 = −z_1z_2z_3
  更一般地 T_{n-1} = {x_1+…+x_n+1 = 0} ⟷ (C^{n+1}, −Π z_i)
- 例 (2)：x_1+x_2+ t/(x_1x_2) + 1 = 0 ——(热带化：带洞三角形)——> Y ≅ Tot(O(−3)→P^2)，w_0 = −u z_0z_1z_2
- 注 1：w_0 的光滑纤维 ≅ (C*)^n；奇纤维 w_0^{-1}(0) = Y 中若干边界层之并；
  临界轨迹 = 若干余维 2 环层之并 —— 对极大退化（"热带光滑"）的曲线，这是一族 C* 与 P^1 的三价构形
- 注 2：在简单例中 Y 是某底簇上的线丛，w_0 = u·σ（u 纤维坐标，σ 底函数）=> 由 Orlov 的 Knörrer 周期性
  D^b_sg(Y,w_0) ≅ D^b Coh(σ^{-1}(0))（通常奇异），即 (n−1) 维镜像
  例 (1) 裤子 {x_1+x_2+1=0} ⟷ {z_1z_2 = 0} ⊂ C^2（σ: C^2 → C 为镜像）；类似 T_{n-1} ⟷ {Π z_i = 0} ⊂ C^n
  例 (2) ⟷ {z_0z_1z_2 = 0} ⊂ P^2
- 更高亏格时这类镜像带栈/非既约 => 不予考虑

## t1-02（原稿第 2 页）

- ★ 对 H ⊂ V^n 环簇（Fano），由 f(x) = Σ_{α∈A} c_α t^{ρ(α)} x^α ∈ H^0(V, ℒ) 定义（Conv(A) = Newt(ℒ)）
  镜像为 (Y^{n+1}, w_0 + w_V)；Y 与前面相同（由 Trop(f) 确定的环 Calabi–Yau 簇）；
  超势的额外项，每条 Σ_V 的射线一项：w_V = Σ_{ν ∈ ray(Σ_V)} T^{c(ν)} z^{(ν, λ(ν))}，
  λ: Σ_V → R 为分段线性函数，下降给出 ℒ = O(H)
- 例 (1)：{x_0+x_1+x_2 = 0} ⊂ P^2 ⟷ (C^3, −z_1z_2z_3 + T(z_1+z_2+z_3))（w_0 项 + w_V 项）
- 例 (2)：C ⊂ V_Δ ⟷ (Y = O(−3) over P^2 [z_0:z_1:z_2], −u z_0z_1z_2 + Tu(z_0^3+z_1^3+z_2^3))
  （N.B.: w_V 沿光滑三次椭圆曲线为 Morse–Bott）
- 例 (3)：亏格 g 曲线 ⊂ 环 del Pezzo 曲面，g ≥ 2 ⟷ crit(w_0+w_V) = 双色构形，由 (3g−3) 条 P^1 在 (2g−2) 个结点处相接
  例如亏格 2 ⟷ crit(w_0+w_V)
- ★ 这些构造对阿贝尔簇也成立（见 e.g. C. Cannizzo 的学位论文），且对完全交成立（H^{n−k} ⊂ V^n ⟷ Y^{n+k}，w_0 有 k 项）
- HMS relates:
  (A) W(H)（H 的 wrapped Fukaya 范畴）⟷ D^b_sg(Y,W)（或经 Orlov：D^b Coh(σ^{-1}(0))）
      已研究：AAEKO、H. Lee、Nadler、Gammage–Shende、Lekili–Polishchuk、…（下划线：曲线在 (C*)^2 中）
      走向高维，但用 microlocal sheaves。GPS ⇒ 同一件事
  (B) D^b Coh(H) 到 F(Y,W)：
      (0) 经 plabic sheaves（Nadler）或 sectors（GPS）—— 当 Y 正合（weakly）时
      (1) 经 [?] wrapped Fukaya 范畴（Abouzaid–A.）
      (2) 经 "F(σ^{-1}(0))"，当不能正合时，用 Knörrer 周期性得到非 LG 的镜像（N. Jeffs [?]）
      (3) 直接在 crit(w)（或 crit(w_0,w_V)）上工作，绕开把 H 嵌入 V 的需要？？
          → 对曲线的镜像：在 C* 与 P^1 的三价构形中的拉格朗日 Floer 理论？（A.–Efimov–Katzarkov 进行中）
  「our FOCUS」括住 (1)–(2)；今天聚焦 (1)

## t1-03（原稿第 3 页）

- 标题：The Floer-theoretic wrapped Fukaya cat. of (Y,w_0) 或 (Y,w_0+w_V) ［Abouzaid–A.］
  （对环 LG 模型的 ad hoc 构造 —— 可用 sectors 的语言推广…… ⚠ Y 非正合！）
  ↳ 用单项式容许性（monomial admissibility），另见 Hanlon 的学位论文
- Objects: 真嵌入的拉格朗日 L ⊂ Y，满足
  · 平凡地无阻碍（不边界全纯圆盘）
  · 带额外数据（spin 结构、分次、局部系统）
  · 单项式容许：
     → 当 |w_0| > 1 时，arg(w_0)|_L 局部常值（即 w_0|_L 落在若干径向弧之并中）∈ (−π/2, π/2)
     → 回忆 w_0 的纤维 ≅ (C*)^n；在这些纤维的紧集之外，存在有限开覆盖 {U_j} 与一族单项式 z^ν
       ［若 V 紧，恰为 w_V 中出现的那些；否则用 Newt(f) = Conv(A) 选取环紧化 V̄］
       使得 arg(z^ν)|_{L∩U_j} 局部常值（取指定值，例如 0）。
- Hamilton 扰动：L 容许 → 流 L^t（与 L Hamilton 同痕；仍容许）
  流在无穷远处增大 arg(w_0) 与 arg(z^ν) 的值
  · 对 w_0 以及出现在 w_V 中的 z^ν，在**有界区间**内增大 —— 不卷绕（NO WRAPPING）
  · 对其他单项式（来自紧化、出现在 w_V 中但不在 w_0 中），增大到 ∞（卷绕 WRAP）
  于是定义 hom(L_0,L_1) = lim_{t→∞} CF^•(L_0^t, L_1)，配上自然的连续映射。
- ★ 这些纤维方向的"部分卷绕" Hamilton 量，本质上就是 Hanlon 学位论文中作为环镜像族的单值群出现的那些；
  在 F((C*)^n, w_V) ≅ D^b(V̄) 上的诱导函子，在 HMS 下对应 −⊗O(D)，D = V̄−V 为紧化除子。
  所以直极限在纤维方向等于那个局部化，它给出 D^b(V̄) → D^b(V)。
- ★ 例：(C^3, w_0 = −z_1z_2z_3)（裤子的镜像），L_0 = 沿 U 形弧的平行移动；ℓ_0 = (R_+)^2 ⊆ (C*)^2 = w_0^{-1}(−1)
  图（原稿下半页）：左：w_0^{-1}(−1) ≅ (C*)^2 ⊇ L_0=(R_+)^2；中：三个 C^2 拼成的圆盘（环紧化）；
  右：单值群 + 卷绕 Hamilton 量作用下 L_0 的像，arg(z_i) = f_i(log|z_i|)，arg(z_i)=0 当 |z_i| >> min_j|z_j| ⇒ 卷绕 ↑（t→∞）；
  下：U 形弧 L_0（黑）与其像（蓝），底部标 ×0

## t1-04（原稿第 4 页）

- hom(L_0,L_0) ≃ CW^•(ℓ_0,ℓ_0) ⊕ CW^•(ℓ_0,ℓ_0)[−1]   （Abouzaid–A.）
      = K[x_1^{±1}, x_2^{±1}]，微分 ∂ = 乘以 1+x_1+x_2
  故 H^•hom(L_0,L_0) ≅ K[x_1^{±1}, x_2^{±1}]/(1+x_1+x_2)（环同构）≅ hom(O,O)，对裤子成立 ✓
- 类似地，对超曲面 H ⊂ (C*)^n，可得 L_0 与 O_H 在 HMS 下相配。
  → 还需要一个生成性（generation）陈述（对裤子没问题）。
  （同样的计算！∂ = 乘以 f = H 的定义方程）这给出 HMS。
