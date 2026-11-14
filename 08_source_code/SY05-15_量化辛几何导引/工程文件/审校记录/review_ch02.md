# 第 2 章审校记录（review_ch02.md）

范围：原书 Chapter 2 *Physics in Symplectic Topology*，印刷页 p.22–p.51，扫描 PDF p.30–p.59。
译者：ch02-physics。下表记录逐页核对中发现的**原文疑误/记号不一致**；凡在译文中保留原文
写法者，均在相应位置加了 `% [Tutor Note: ...]` 批注说明。表中「页」为印刷页码。

| # | 页 / 位置 | 原文（照录） | 疑点 | 建议改法 |
|---|---|---|---|---|
| 1 | p.24, 例 2.1.1 的 Euler–Lagrange 方程 | `mg = d/dt m v_2(t)(γ(t),γ̇(t)) = m q̈_2(t)` | 由 (2.3) $L=\frac12m\|v\|^2-mgq_2$ 得 $\partial L/\partial q_2=-mg$，故左端应为 $-mg$；否则与「$q_2$ 为抛物函数、轨迹为抛物线（开口向下）」矛盾 | 左端改为 $-mg$ |
| 2 | p.25, 例 2.1.2 | `Γ^k_{ij} = Σ_{i=1}^{2} g^{kl}Γ_{lij}` | 求和指标应为 $l$；原文对 $i$ 求和，与左端自由指标 $k$、被求和式中的 $l$ 均不相容 | 改为 `Σ_{l=1}^{2} g^{kl}Γ_{lij}` |
| 3 | p.28, 命题 2.2.1 的证明开头 | `L = L(q,v) : T*R² → R` | 与定义 2.1.1、事实 2.1.1 冲突：$L$ 定义在切丛 $T R^2$ 上；落在 $T^*R^2$ 上的是其 Legendre 变换 $\mathcal{L}(L)$ | 定义域改为 $T R^2$ |
| 4 | p.32, 例 2.3.2 的反正向 | `ω_p(X_G(p),v) = −ω_p(v,X_G(p)) = dG_p(v) ≠ 0` | 由定义 1.7.1（$\dd G=-\iota_{X_G}\omega$）得 $\omega_p(X_G(p),v)=-\dd G_p(v)$，末项差一负号（不影响「$\ne0$」的结论） | 末项改为 $-\dd G_p(v)$ |
| 5 | p.39, 式 (2.29) | `... , ½\|z_n\|²) ∈ R^n_{≥0},` 之后语句多一个 `)` | 排版笔误：`⟨μ(z_1,…),v⟩ = H_v(r_1,…,r_n,θ_n))` 多一个右括号 | 删去多余 `)` |
| 6 | p.41, 定理 2.5.1 (i)(iii) | `a finite union of pairwise disjoint connected of submanifolds`；`denoted by im(u)` | (i) 多一个 `of`，应为 `connected submanifolds`；(iii) 中 `im(u)` 应为 `im(μ)` | 分别改为 `connected submanifolds`、`im(μ)` |
| 7 | p.47, §2.8 开头 | `one family of directions is given by the moment image im(u)` | `im(u)` 应为 `im(μ)`（同类错误在 p.47 出现两次） | 改为 `im(μ)` |
| 8 | p.50, 定理 2.8.1 (i) | `then L := F^{-1}(p) it is a Lagrangian torus` | 多余的 `it` | 删去 `it` |
| 9 | p.43, 例 2.6.1 中 $\{H,H_2\}$ | `Σ_{i=1}^{2}( ∂H/∂p_i ∂H_2/∂q_i − ∂H/∂q_i ∂H_2/∂p_i )` | (a) 空间 Kepler 问题应为 $\sum_{i=1}^3$（$i=3$ 项自动为零，故结果不变）；(b) 按 (2.8)、(2.5) 的约定 $\{F,G\}=\sum_i(\partial_{q_i}F\partial_{p_i}G-\partial_{p_i}F\partial_{q_i}G)$，上式的被求和式整体与之反号（结果仍为 0，不影响结论） | 上限改 3；被求和式按 (2.8) 重排 |
| 10 | p.43, 例 2.6.1 | `{A_1,A_2} = −A_3, {A_2,A_3} = −A_1, {A_1,A_3} = A_2` | 按 (2.8) 的标准括号，角动量满足 $\{A_1,A_2\}=A_3,\{A_2,A_3\}=A_1,\{A_1,A_3\}=-A_2$；原文三式整体反号，等价于采用了与 (2.8) 相反的括号约定。本段只需 $\{A_i,A_j\}\ne0$，结论不受影响 | 统一括号约定后取标准式，或明确声明相反约定 |
| 11 | p.33, 练习 2.3.2 | `limsup_{F',G' \xrightarrow{C^0} F,G} \|\{F_k,G_k\}\|_{C^0} > \|\{F,G\}\|_{C^0}` | 记号矛盾：正文给的是函数列 $F_k\to F$、$G_k\to G$，$\limsup$ 应取 $k\to\infty$（或 $\limsup_{F'\to F,G'\to G}\|\{F',G'\}\|$），而括号内却写 $F_k,G_k$ | 或改为 $\limsup_{k\to\infty}$，或把括号内改为 $F',G'$ |
| 12 | p.36, 例 2.4.4 | `X_A(q,p)=(Aq,Ap)` 是「由 $H_A(q,p)=q^{\mathrm T}Ap$ 生成的哈密顿向量场」 | 按 (2.4)（$\dd H=-\iota_{X_H}\omega_{\mathrm{can}}$）与 (2.5)，$X_{H_A}=(-Aq,-Ap)=-X_A$；即 $X_A$ 实际由 $-H_A$ 生成。原文与 (2.25)、(2.26) 的 $\mu=q\times p$ 只在与 (2.4) 相反的符号约定下自洽（(2.9) 的符号亦随之翻转） | 取 $H_A=-q^{\mathrm T}Ap$（此时 $\mu=-q\times p$），或整体声明相反的符号约定；建议以「$\mu=q\times p$ 是物理角动量」为准记忆结论 |
| 13 | p.45, §2.7 第 2 段 | `derived from such a symmetry, one derived a conservative` | 词语重复、语法不顺（非数学错误） | 改为 `one obtains a conservative` |
| 14 | p.47, §2.8 第 2 段 | `The discussion so far in fact rephrase the polar coordinates` | 主谓不一致（非数学错误） | 改为 `rephrases` |

## 说明

- 第 1–13 项中，凡涉及符号/公式者，译文**一律保留原文写法**并在对应位置以
  `% [Tutor Note: ...]` 指出正确形式与核对要点；第 13–14 项为文字问题，译文按语义通顺处理。
- 第 9、10、12 项相互关联：原文在 §2.6–§2.8 的若干计算中使用的是「与 (2.8) 相反的」
  括号/哈密顿向量场符号约定。凡遇「括号为零」的结论，符号不影响正确性；但读者若逐项
  重算会得到整体反号，核对时须固定一个约定并全章一致。
- 另有若干纯排版/语法小疵（如 p.51「Denote by e is the unit vector」多 `is`、p.52
  「the angular momentum A is equal to q×p」句法不顺），不影响数学内容，译文已按语义通顺
  处理，未逐条列出。
