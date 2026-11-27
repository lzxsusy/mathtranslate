# Yao《一般线性群的局部 Langlands 对应》（yao17）资料卡 · 骨架图

这张图是 36 页讲义的完整逻辑骨架：先把 Galois 侧的 Weil–Deligne 表示摆出来并说明它为什么与 $\ell$ 进表示等价（§1），再把自守侧的光滑/容许表示与 Hecke 模接上（§2.1），用抛物诱导与 Jacquet 函子定义超尖点（§2.2），然后陈述 LLC 并给出 Henniart 的四步路线（§2.3）；接着用 Bernstein–Zelevinsky 分类把「一般表示」化归为「超尖点 + 段长」（§3.1），补上平方可积/缓增/generic/导子/深度这些不变量（§3.2–§3.6）；最后用 Bernstein 分解把惯性对应推出来（§4），§5–§6 只剩标题。节点是概念卡，边是推导卡；标注页码是底本**印刷页**（= PDF 页）。

```text
§1  p.2          [A] weil-group
                       │  W_K = 生成元 + I_K，驯商 I_K/P_K ≅ Ẑ(1)
                       ▼
                 [A] wd-representation ──deriv──▶ wd-from-galois
                       │  (ρ, N)：N 幂零、ρ(τ)Nρ(τ)^{-1} = q^{-n}N
                       ▼
                 [A] frobenius-semisimple        [A] tate-epsilon
                       │  引理 1.2：φ-半单 ⇒ N = 0      │  定理 1.3：L/ε 三公理唯一确定
                       ▼                                ▼
                 [A] wd-functor ─────────────────▶ [A] wd-invariants
                       │  引理 1.5 + 推论 1.6–1.8      │  c(ρ)、L(ρ,s)、ε(ρ,s,ψ)
                       │  惯性类型 ρ|_{I_K}（引理 1.9）
                       ▼
§2.1 p.10        [B] smooth-admissible
                       │  光滑 ⊂ 容许；反变对偶
                       ▼
                 [B] hecke-modules
                       │  π ↦ π^∞ ≃ H(G)-模（引理 2.1/2.2）
                       ▼
                 [B] satake                      [B] harish-chandra-character
                       │  H(G//K) ≅ C[t^{±1}]^{S_n}     │  定理 2.5/2.8、引理 2.6/2.7
                       ▼                                ▼
§2.2 p.16        [B] parabolic-induction ──deriv──▶ supercuspidal-criterion
                       │  I_P / J_P、δ_P^{1/2}           │  引理 2.10：π 超尖点 ⇔ 一切 J_P π = 0
                       ▼
                 [B] jacquet-supercuspidal
                       │  矩阵系数紧支；引理 2.11/2.12
                       ▼
§2.3 p.21        [O] llc-statement ───────────────▶ [O] llc-finer-properties
                       │  定理 2.13 五条                │  定理 2.14：超尖点/本质 L^r/一般
                       │  Henniart：(i) n=1 → (ii) Sp → (iii) 扭转 → (iv) 一般
                       ▼
§3.1 p.23        [C] zelevinsky-segment
                       │  Δ(π,m)、linked/precedes、(∗)
                       ▼
                 [O] bz-classification ──deriv──▶ induction-to-supercuspidal
                       │  定理 3.1 (1)–(7)               │  rec_n = ⊕ Sp_{m_i} ∘ rec_{n_i}
                       ▼                                ▼
                 [C] supercuspidal-support ──deriv──▶ gl2-llc-cases
                       │  支撑 supp(π)、St_n             │  n=2 的四类 ↔ WD 四类
                       ▼
§3.2 p.27        [C] square-integrable-tempered
                       │  本质 L^r ⊂ 平方可积 ⊂ 缓增；定理 3.2/3.3、推论 3.4
                       ▼
§3.2.3 p.28      [C] generic-whittaker
                       │  θ_ψ、Whittaker 模型、定理 3.6（generic ⇔ rec 可约）
                       ▼
§3.3–3.6 p.29    [C] conductor-depth ──deriv──▶ depth-zero-chain
                       │  c(π)=c(rec_n π)（引理 3.8）    │  五条等价：非分歧 / Iwahori / 深度 0
                       │  ε(π,s,ψ) = q^{-(c+n n(ψ))s} ε(π,0,ψ)
                       ▼
§4  p.32         [D] bernstein-decomposition
                       │  引理 4.1 + 定理 4.2：Rep^∞_n = ∏ R(L,ς)
                       ▼
                 [D] inertial-correspondence ◀──deriv── inertia-from-bernstein
                       │  引理 4.3/4.4/4.5：分量 ↔ ρ|_{I_K}
                       ▼
§4.3 p.35        [D] type-and-k-type
                       │  type / K-type / 极小 K-type；Bushnell–Kutzko
                       ▼
§5–§6 p.36       （底本只有标题：Carayol 的上同调实现、局部 Langlands 的族）
```

## 三条竖线（读图提示）

1. **左竖线是自守侧**（B 轨）：光滑 → Hecke 模 → Satake/Harish-Chandra → 抛物诱导 → 超尖点。
2. **右竖线是 Galois 侧**（A 轨）：Weil 群 → Weil–Deligne 表示 → φ-半单 → Tate 的 $L$/$ε$ → $\WD$ 函子与不变量。
3. **中间是主定理与分类**（O/C 轨）：LLC 陈述（p.21）→ BZ 分类（p.23）→ 平方可积/缓增/generic（p.27–28）→ 导子与深度（p.30）。

## 六张推导卡的位置

| 推导卡 | 回答什么 | 页码 |
| --- | --- | --- |
| `wd-from-galois` | $\rho\mapsto(\rho,N)$ 具体怎么造，$N$ 为什么幂零、为什么满足共轭关系 | p.7–8 |
| `supercuspidal-criterion` | 引理 2.10 的证明链：非超尖点 ⇒ 可嵌入真抛物诱导 | p.19–20 |
| `gl2-llc-cases` | $n=2$ 的四类表示各自对应哪类 $(\rho,N)$ | p.25–26 |
| `induction-to-supercuspidal` | 定理 2.13 为何只需在超尖点上验证，一般 $\rec_n$ 怎么拼 | p.26 |
| `depth-zero-chain` | 深度 0、Iwahori-球面、非分歧在 Galois 侧各对应什么 | p.30 |
| `inertia-from-bernstein` | 引理 4.4 怎么从 BZ 分类与引理 4.3 推出来 | p.33–34 |

## 底本的三处「空缺」

底本明确留白、卡片里也都如实标注：

- §3.4（容许表示的导子与新向量）：只有标题。
- §3.5.1（导子与深度）、§3.6.1–§3.6.2：只有标题。
- §5（Carayol）、§6（族）：只有两行标题，无正文。
- §3.3.4「Iwahori-不动向量」：原文写「to be added in second draft」；§3.6 的 L-因子与 ε-因子也写「To be completed in second draft」。
