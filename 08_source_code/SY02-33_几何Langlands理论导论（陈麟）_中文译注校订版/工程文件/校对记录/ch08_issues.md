# ch08（Aut_E 的构造）审读：问题清单

范围：`src/chapters/ch08.tex` 全 118 行（原 PDF p44–p47）。
逐句对照 `work/en/ch08_en.txt`（p44–p47），公式按 p044–p047 的 PNG 放大复核。

结论：P1 1 条（20 行，增译）；P2 2 条（22 行术语、59 行记号）。未发现漏译、逻辑反转或箭头方向错误；p045 的 $\mathrm{HL}_k^d$ 定义与 $\overrightarrow h_!\overleftarrow h^*$ 公式、p046 的定义 8.4 与 Hecke 对应基变换、p047 的 $(t_x^{d+n})^*$／$(\tau_x^d)^*$ 两式均已逐字核对无误。

## ch08.tex:20（原 PDF p44）

- 原文：Since pC is smooth on the chosen good open, a nonzero descended sheaf is automatically perverse and irreducible.
- 原译：由于 $p_C$ 在所选良好开子叠上光滑，采用相对反常归一化后，非零的下降层自动是不可约反常层。
- 类型：增译
- 改法：由于 $p_C$ 在所选良好开子叠上光滑，非零的下降层自动是不可约反常层。
- 理由：原文只说 $p_C$ 在该开子叠上光滑，并无“采用相对反常归一化”这一条件，该术语全书未定义，读者会误以为下降还需额外的归一化步骤。

## ch08.tex:22（原 PDF p44）

- 原文：Work on a smooth open chart V ⊂ C_n^∘ ∩ Bun_n^d.
- 原译：在光滑开图册 $V\subset C_n^\circ\cap\Bun_n^d$ 上工作。
- 类型：术语
- 改法：在光滑开图 $V\subset C_n^\circ\cap\Bun_n^d$ 上工作。
- 理由：chart 是单张开图／坐标卡；本书“图册”专指 atlas（第 2、4 章的“光滑图册”“方便的图册”），此处混用会让读者误以为 $V$ 是由多张开图拼成的图册。

## ch08.tex:59（原 PDF p46）

- 原文：α_d : HL^d_k(K) −→ L^d_E ⊠ K (d ≥ 0)
- 原译：\[\alpha^d:\mathrm{HL}_k^d(\cK)\xrightarrow{\sim}\cL_E^d\boxtimes\cK\qquad(d\ge0),\]
- 类型：公式
- 改法：\[\alpha_d:\mathrm{HL}_k^d(\cK)\xrightarrow{\sim}\cL_E^d\boxtimes\cK\qquad(d\ge0),\]
- 理由：原文为下标 $\alpha_d$（p046 放大核对），译稿写成上标 $\alpha^d$，与原文上下标不符；这是以 $d$ 编号的一族同构，应保留下标。
