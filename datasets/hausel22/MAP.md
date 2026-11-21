# Hausel ICM 2022（hausel22）资料卡 · 骨架图

这张图是 Hausel《Enhanced mirror symmetry for Langlands dual Hitchin systems》（Proc. ICM 2022, Vol. 3, pp. 2228–2249）的逻辑骨架：先把 Hitchin 系统的镜像对称拆成拓扑、同调、SYZ 三个层次，再用 Kapustin–Witten 的 $S$ 对偶把它升级成"增强"版本（连算子一起匹配），最后在幂零锥上把增强猜想变成可以算的重数代数。箭头上的数字是原文**印刷页**；概念卡是节点，推导卡是把节点连起来的边。

```text
§1  p.2229–2230  [A] hitchin-system ──▶ mirror-symmetry
                    │   超 Kähler (I,J,K)、M_Dol ≅ (M,I)、M_DR ≅ (M,J)
                    ▼
§2.1 p.2230      [A] mirror-symmetry（拓扑 / 同调 / SYZ 三方面）
                    ├──▶ homology-mirror-symmetry
                    └──▶ syz-mirror-symmetry ──deriv──▶ syz-from-hitchin
                    ▼
§2.2 p.2231      [A] langlands-dual-group ──▶ geometric-langlands-correspondence
                    │   GL_n^∨ ≅ GL_n、SL_n^∨ ≅ PGL_n、opers
                    ▼
§2.3 p.2232      [A] SYZ for Hitchin：M_Dol 与 M^∨_Dol 同底 A、纤维互对偶
                    ▼
§2.4 p.2233      [B] topological-mirror-symmetry ──▶ stringy-hodge-numbers
                    │   Γ = Jac_C[n]、gerbe α、h^{p,q}_st,α、费米子移位
                    │   └──deriv──▶ stringy-hodge-shift
                    ▼  （猜想 2.1）
§2.5 p.2234–2235 [C] hyperkahler-branes（四类型）──▶ kapustin-witten-duality
                    │   └──▶ enhanced-mirror-symmetry ──▶ classical-limit-langlands
                    ▼
§3   p.2235      [O] enhanced-mirror-program（总览：已证 vs 猜想）
                    ▼
§3.1 p.2236–2238 [D] bialynicki-birula-attraction ──▶ very-stable-higgs-bundle
                    │   └──deriv──▶ very-stable-chain
                    ├──▶ equivariant-multiplicity ──deriv──▶ multiplicity-polynomial
                    └──▶ local-multiplicity-algebra ──deriv──▶ gorenstein-multiplicity-algebra
                    ▼
§3.2 p.2238–2240 [D] local-multiplicity-algebra ──deriv──▶ q-delta-grassmann
                    │   定理 3.10：Q_δ ≅ ∏ H^*(Gr(i,n))^{m_i}
                    ▼
§3.3 p.2241–2243 [E] affine-grassmannian ──deriv──▶ hecke-to-wobbly
                    ├──▶ jet-scheme ──deriv──▶ jet-scheme-n2
                    └──▶ 定理 3.12：μ=(d+1)ω_k 时 Q_μ ≅ C[J_d(Q_{ω_k})]
                    ▼
§3.3.1 p.2244    [E] lagrangian-closure ──▶ 定理 3.18
                    ▼
§3.4 p.2244–2246 [C] classical-limit-langlands ──deriv──▶ s-intertwines-operators
                        （3.12）–（3.14）──▶ 猜想 3.19（几何 Satake 的经典极限）
```

## 怎么用这张图

1. **第一次读**：从 `hitchin-system` 出发，沿左列主链 A → B → C 走一遍，看清"拓扑/同调/SYZ"三层的关系；这一段决定后面所有猜想的措辞。
2. **想补技术细节**：在 §3 停下来读 D 轨五件套（BB 分解 → 非常稳定 → 等变重数 → 局部重数代数 → Gorenstein），这是全篇唯一"能算"的部分。
3. **想做研究**：直接看 §3.3–3.4 的 E/C 轨，那里是猜想 3.12、3.19 的入口，也是原文"未发表结果"所在。

## 三条推荐阅读路径

### 几何侧（先把 Hitchin 系统读懂）

`hitchin-system` → `mirror-symmetry` → `langlands-dual-group` → `syz-mirror-symmetry` → `homology-mirror-symmetry`

配推导：`syz-from-hitchin`

### 数论侧（拓扑镜像对称与 Hodge 数）

`topological-mirror-symmetry` → `stringy-hodge-numbers` → `langlands-dual-group`

配推导：`stringy-hodge-shift`

### 代数侧（幂零锥上的重数代数，本包重点）

`bialynicki-birula-attraction` → `very-stable-higgs-bundle` → `equivariant-multiplicity` → `local-multiplicity-algebra` → `affine-grassmannian` → `jet-scheme` → `lagrangian-closure`

配推导：`very-stable-chain` → `multiplicity-polynomial` → `gorenstein-multiplicity-algebra` → `q-delta-grassmann` → `hecke-to-wobbly` → `jet-scheme-n2` → `s-intertwines-operators`

## 印本页对照

| 印刷页 | 内容 | 相关卡 |
| --- | --- | --- |
| 2228 | 标题、摘要、MSC、关键词 | `enhanced-mirror-program` |
| 2229–2230 | §1 引言 | `hitchin-system`、`mirror-symmetry` |
| 2230 | §2.1 镜像对称三方面 | `homology-mirror-symmetry`、`syz-mirror-symmetry` |
| 2231 | §2.2 几何 Langlands | `langlands-dual-group`、`geometric-langlands-correspondence` |
| 2232 | §2.3 SYZ for Hitchin | `syz-from-hitchin` |
| 2233 | §2.4 拓扑镜像对称、猜想 2.1 | `topological-mirror-symmetry`、`stringy-hodge-numbers` |
| 2233 | §2.4 末：GWZ 的 $p$ 进证明 | `topological-mirror-symmetry` |
| 2234–2235 | §2.5 Kapustin–Witten、增强镜像对称 | `kapustin-witten-duality`、`hyperkahler-branes`、`enhanced-mirror-symmetry` |
| 2235–2236 | §3 引入、BB 分解 | `enhanced-mirror-program`、`bialynicki-birula-attraction` |
| 2237 | 定理 3.1、3.2 | `very-stable-chain` |
| 2238 | 定理 3.3–3.6、定义 3.4/3.7 | `very-stable-higgs-bundle`、`equivariant-multiplicity`、`local-multiplicity-algebra` |
| 2239 | 注 3.8、定理 3.9 | `gorenstein-multiplicity-algebra` |
| 2240 | 定理 3.10、Hecke 图 (3.1) | `q-delta-grassmann` |
| 2241–2242 | §3.3 仿射 Grassmannian、支配权 | `affine-grassmannian`、`hecke-to-wobbly` |
| 2243 | 定理 3.12、注 3.13–3.16 | `jet-scheme`、`jet-scheme-n2` |
| 2244 | §3.3.1 拉格朗日闭包、定理 3.18 | `lagrangian-closure` |
| 2245 | §3.4 (3.12)–(3.14) | `classical-limit-langlands`、`s-intertwines-operators` |
| 2246 | 猜想 3.19、注 3.20、致谢 | `s-intertwines-operators` |
| 2247–2249 | 参考文献 | — |
