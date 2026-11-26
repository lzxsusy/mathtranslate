# Sandvik《Arkhipov–Bezrukavnikov 等价》（sandvik25）资料卡 · 骨架图

这张图是 13 页报告的完整逻辑骨架：先把反球模 $M^{\mathrm{asph}}$ 摆出来并给它三种候选范畴化（§1），再在 $p$ 进侧把它实现为中心层与 Wakimoto 层（§2），接着在 Springer 解消的凝聚层上造出三造函子 $F_1\to F_2\to F$（§3），然后构造 IW 侧最高权范畴与平均函子（§4），最后把两侧焊成主等价（§5）。节点是概念卡，边是推导卡；标注页码是底本**印刷页**（= PDF 页）。

```text
§1  p.1          [O] three-categorifications
                       │  M^asph 的三条路线：K 群 / q-形变 Whittaker / IW 函数
                       ▼
                 [O] ab-equivalence-theorem ──deriv──▶ fully-faithful-hom
                       │  主定理 5.0.1 与推论 5.0.2 的结论摘要
                       ▼
§2  p.2–6        [A] antispherical-module ─────▶ [A] wakimoto-sheaves
                       │  符号诱导               │  W_λ = ∇_{λ₁} ⋆ Δ_{-λ₂}
                       ▼                          ▼
                 [A] nearby-cycles  ──deriv──▶ [A] wakimoto-filtration
                       │  Ψ_f 五性质              │  定理 2.5.3：重数 = dim V_λ
                       ▼                          │
                 [A] central-affine-grassmannian  │
                       │  Gr^cen → Fl（一般纤维 / 特殊纤维）
                       ▼                          ▼
                 [A] gaitsgory-central-functor ──deriv──▶ nearby-cycles-to-central
                       │  Z = Ψ_f(– ⊠ k[1])；t-正合、幺半、π_* Z = id
                       ▼
§2.6 p.6         [C] antispherical-quotient      （P_I^asph ← Serre 商）
                       │
§3  p.6–8        [B] springer-resolution ──▶ [B] hat-n-x
                       │  Ñ = G∨×_{B∨} n∨            │  N̂ ⊂ N̂_X，∂X
                       ▼                              ▼
                 [B] functor-f1 ──deriv──▶ f1-monoidal
                       │  Rep(G∨×T∨) → P_I^Wak
                       ▼
                 [B] functor-f2 ──deriv──▶ tannakian-algebra
                       │  经 A-mod 换基
                       ▼
                 [B] functor-f3
                       │  D^b Coh(Ñ) → D^b P_I
                       ▼
§4  p.9–11       [C] whittaker-sheaves ──▶ [C] iw-category
                       │  L_AS、消没              │  D^b_IW(Fl)
                       ▼                          ▼
                 [C] iw-highest-weight  ──deriv──▶ iw-averaging-t-exact
                       │  标准/余标准/倾斜 T^IW_λ  │  式 (5)(6) ⇒ t-正合
                       ▼                          ▼
                 [C] iw-averaging ────────▶ [C] central-tilting
                       │  Av^IW = Δ^IW_0 ⋆ –       │  定理 4.5.1：重数 = dim V_λ
                       │                          │
                       └──────────┬───────────────┘
                                  ▼
§5  p.11–12      [D] functor-fiw ──▶ [D] five-categories
                       │  F^IW = Av^IW ∘ F         五个范畴的等价图
                       ▼
                 [D] five-categories：D^bCoh(Ñ) ~ D^bP_I^asph ~ D^bP_IW ~ D^b_IW(Fl)
```

## 骨架的三条硬约束

1. **$F_1\to F_2\to F$ 不能跳**：$F_1$ 只定义在表示范畴上（自由对象），$F_2$ 用 Tannakian 重构把它扩到自由凝聚层，$F$ 再下降到整个导出范畴。跳步就会缺「下降」那一步（原文 p.8 明确省略）。
2. **$Z$ 与 $\mathrm{Av}^{\mathrm{IW}}$ 必须分开看**：$Z$ 从球侧走到 Iwahori 侧且像落在中心；$\mathrm{Av}^{\mathrm{IW}}$ 再把 Iwahori 侧搬到 IW 侧。主函子是两者复合，不是任何一个单独的函子。
3. **两处「不同构但同类」**：$\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$ 与 $\Delta^{\mathrm{IW}}_\lambda$ 只在 $K_0$ 中相等；$T^{\mathrm{IW}}(L_\lambda)\cong T^{\mathrm{IW}}_\lambda$ 是主定理的**推论**而非构造。这两处是全篇最容易误读为「显然对应」的地方。

## 原文自认的空白（本包的 `gap_note` 都落在这些点上）

| 位置 | 原文措辞 | 影响 |
| --- | --- | --- |
| §2.2 命题 2.2.2 | 「不显然，因为 $\exp_X$ 不是代数映射」 | $\Psi_f$ 的 $t$-正合性是后续一切的基础，但只有引用 |
| §2.4 定理 2.4.1(1)(3)(4) | 只给 (2)(5) 的论证 | 幺半性与中心性未展开 |
| §2.5 定理 2.5.3 | 只陈述 | Wakimoto 滤链的存在性无证明 |
| §3.3 Tannakian 重构 | 「can be checked」 | $A$ 的具体构造是黑箱 |
| §3.4 下降 | 「can be checked rather explicitly, and is omitted」 | 全文最大的省略 |
| §4.3 命题 4.3.1 | 只称「key observation」 | 最高权结构未证 |
| §4.5 定理 4.5.1 | 三步梗概，拟极小情形「much more difficult」 | 全文最难的证明被压缩成一句 |
| §5 定理 5.0.1 | 「routine homological algebra」「not hard to check」 | 两处计算都只给结果 |
