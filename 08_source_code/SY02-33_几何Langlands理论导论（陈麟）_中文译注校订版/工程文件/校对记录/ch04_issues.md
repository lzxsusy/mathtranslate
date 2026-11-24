# ch04（Laumon 层）审读：问题清单

范围：`src/chapters/ch04.tex` 全 173 行（原 PDF p26 中部–p32）。
逐句对照 `work/en/ch04_en.txt`，公式全部按 p026–p032 的 PNG 复核。

结论：P1 0 条；P2 3 条（34、56、132 行，均属术语/记号）。未发现影响数学内容的误译、漏译、增译、逻辑反转或编号错误；定理/Lemma/命题的编号与陈述均与原文一致。

## ch04.tex:34（原 PDF p27）
- 原文：Thus the universal positive Hecke kernel should be pulled back from a sheaf on Tor.
- 原译：因此，通用的正 Hecke 核应当是 $\Tor$ 上一个层的拉回。
- 类型：术语
- 改法：因此，泛正 Hecke 核应当是 $\Tor$ 上一个层的拉回。
- 理由："universal" 指 $\Hecke_{\GL_n}^+$ 上的泛（万有）核，中文几何文献的固定说法是"泛"；译作"通用的"会被读成"一般用途的"，泛性质反而丢了。

## ch04.tex:56（原 PDF p28）
- 原文：The stratum Tor(d) is open; it is the image of X(d) → Tord, D 7−→ OD.
- 原译：层 $\Tor^{(d)}$ 是开的；它是 $X^{(d)}\longrightarrow\Tor^d,\ D\longmapsto\cO_D$ 的像。
- 类型：术语
- 改法：分片 $\Tor^{(d)}$ 是开的；它是 $X^{(d)}\longrightarrow\Tor^d,\ D\longmapsto\cO_D$ 的像。
- 理由："stratum" 被译作"层"，与术语表 sheaf — 层 直接撞车，"层 $\Tor^{(d)}$ 是开的""层 $\Tor^\lambda$ 局部闭地映入 $\Tor^d$"读起来是错的（层没有开/闭、也不映入叠）；同类用法见 112（整体层 $\Tor^\lambda$）、116、122（各层是幂零轨道的商叠）、143（Schubert 层），建议统一改作"分片"（或"轨迹/子叠"）。

## ch04.tex:132（原 PDF p30）
- 原文：Equivalently, if χ^λ ∈ Irr(Sd) is the Specht representation corresponding to λ, then Schur–Weyl duality gives V λ ≃ (V ⊗d ⊗ χλ )Sd .
- 原译：若 $\chi_\lambda\in\operatorname{Irr}(S_d)$ 是与 $\lambda$ 对应的 Specht 表示，则 Schur–Weyl 对偶给出 $V^\lambda\simeq(V^{\otimes d}\otimes\chi_\lambda)^{S_d}$。
- 类型：公式
- 改法：若 $\chi^\lambda\in\operatorname{Irr}(S_d)$ 是与 $\lambda$ 对应的 Specht 表示，则 Schur–Weyl 对偶给出 $V^\lambda\simeq(V^{\otimes d}\otimes\chi^\lambda)^{S_d}$。
- 理由：原文记号是上标 $\chi^\lambda$（p030、p032 PNG 均如此，与 $V^\lambda$ 同为上标）；译稿改成下标，虽不影响含义，但属于对上标/下标的可核偏差，且 168–169 行同样出现，建议照原文统一。
