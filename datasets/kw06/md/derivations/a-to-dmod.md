# c.c. A-膜、开弦代数与 A-膜→D-模

> `kw/deriv/a-to-dmod` · 轨道 E · Langlands 与翻译器 · 状态 dev · 7 步

> **要回答的问题**：c.c. A-膜为什么能给出 D-模，开弦态与 D-模之间的对应又如何具体实现？

## 一句话

c.c. 膜是 $(A,B,A)$ 型自对偶 A-膜；$K$ 中 A-膜与它之间的开弦态是 $D_{K^{1/2}}$ 模，于是每个 $K$ 中 A-膜给出一个 D-模：无世界面瞬子，例中平坦 $(B,A,A)$ 膜给 $K_M^{1/2}$ 的全纯截面。

## 目标

由 c.c. 条件解出典范膜，说明开弦代数是 $D_{K^{1/2}}$ 模，并给出无瞬子与例证。

## 前提

- B p.185 eq (11.1)：c.c. 膜条件 $(\omega^{-1}F)^2=-1$。
- B p.186：c.c. 膜是 $(A,B,A)$ 型，在 $I$ 与 $K$ 中为 A-膜、在 $J$ 中为 B-膜。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 在 $M_H$ 上取 $\omega=\mathrm{Im}\,\tau\,\omega_K$，并要求 $(\omega^{-1}F)^2=-1$：则 $\hat N=\omega^{-1}F$ 是可积复结构，$\omega-\ii F$ 是它的全纯辛形式。 | 这个条件保证膜在辛几何意义下是 A-膜，同时给出一个可用的复结构。 | `B p.185 eq (11.1)` | A·原文明确写了 |
| 2 | 把 $F$ 展开为 $F=\mathrm{Im}\,\tau(a\,\omega_J+b\,\omega_I)$，条件给 $a^2+b^2=1$；$b\ne0$ 时 $F$ 不恰当且周期不整，只有 $b=0$ 的解可用，此时 $\hat N=I$、$F=\mathrm{Im}\,\tau\,\omega_J=d\alpha$ 恰当，线丛平凡。 | 「典范」解之所以唯一，是因为非零 $b$ 会让 $d\alpha$ 出现非整周期，从而无法定义合法的膜。 | `B p.186` | A·原文明确写了 |
| 3 | 无世界面瞬子：边界条件与 $K$ 中的全纯性给出 $(\omega-\ii F)\partial_0\Phi=0$，而 $\omega-\ii F$ 非退化，故 $\Phi$ 必为常数。 | 这条论证排除了世界面瞬子修正，使开弦态可以纯代数地计算。 | `B p.187 eq (11.7)` | A·原文明确写了 |
| 4 | 开弦代数局部由乘法 $[\kappa,f]=-\ii(\mathrm{Im}\,\tau)^{-1}\kappa(f)$、$p_\alpha=-\frac{\ii}{\mathrm{Im}\,\tau}\frac{\partial}{\partial q^\alpha}$ 生成；整体粘接时三重上链 $c^{ijk}=s^{ij}+s^{jk}+s^{ki}$，若 $c\in2\pi\mathbb Z$ 得 $D_L$，否则得 twisted 版本 $D_{L^\gamma}$（(11.16)）。 | 局部乘法与整体粘接共同定义了这个代数；twist 类出现与否由 $c$ 是否整给出。 | `B p.192 eq (11.16)` | A·原文明确写了 |
| 5 | 时间反演 $T:(A,\varphi)\mapsto(T^*A,-T^*\varphi)$ 把开弦代数映到 opposite，而 $D_L$ 的 opposite 是 $D_{L^{-1}\otimes K_M}$；自对偶要求 $L^2=K_M$，故 $L=K_M^{1/2}$。 | 这是 c.c. 膜「自对偶」的代数表达：代数与它的 opposite 同构，正是 D-模的对称性。 | `B p.194` | A·原文明确写了 |
| 6 | 于是 $K$ 中任意 A-膜 $B'$ 与 c.c. 膜之间的开弦空间是 $D_{K^{1/2}}$ 上的模，即每个 $K$ 中的 A-膜都给出一个 D-模；原文对此写 we claim/we argue，未给完整证明。 | 这是本节的核心断言：膜范畴的弦空间对应 D-模范畴，从而把 A-膜问题代数化。 | `B p.196` | B·原文暗示、我们补的中间步 |
| 7 | 例：支撑在 $\{\varphi=0\}\cong M_C$ 的平坦 $(B,A,A)$ 膜，法向费米子无零模、切向零模给出 $M_C$ 的旋量 $K_M^{1/2}\otimes(\oplus_j\Omega^{0,j})$，$Q$ 化为 $\bar\partial$，故态是 $K_M^{1/2}$ 的全纯截面。 | 这个例子把抽象的 $D_{K^{1/2}}$ 模具体化为全纯截面空间，同时也是磁特征膜的构造。 | `B p.198` | A·原文明确写了 |

## 结论

c.c. 膜是 $(A,B,A)$ 型的自对偶 A-膜：$(\omega^{-1}F)^2=-1$ 给出复结构 $\hat N=\omega^{-1}F$，唯一非凡的解是 $\hat N=I$、$F=\mathrm{Im}\,\tau\,\omega_J$。无世界面瞬子，故开弦态可直接计算；自对偶要求 Chan-Paton 丛 $L=K_M^{1/2}$。于是 $K$ 中每个 A-膜都给出一个 $D_{K^{1/2}}$ 模，例中平坦 $(B,A,A)$ 膜给 $K_M^{1/2}$ 的全纯截面。

## 缺口

- 「每个 A-膜给出 D-模」原文写 we claim/we argue，未给出完整证明（B p.196）。
- 整体粘接的三重上链在什么条件下整，原文只按 $c\in2\pi\mathbb Z$ 分情形讨论，未给出判据（B p.192）。

## 最容易讲错的地方

- $\omega$ 要取 $\mathrm{Im}\,\tau\,\omega_K$ 而不是 $\omega_J$；取错则 $\hat N\ne I$，得不到典范解。
- 粘接上链必须 $c\in2\pi\mathbb Z$ 才给 $D_L$，否则只能得到 twisted 版本 $D_{L^\gamma}$。

## 相关卡

[Ψ ≠ 0：λ-连接与扭化 D-模](../derivations/psi-lambda.md) · [电特征膜 = 平坦 ^LG_C 联络](../derivations/electric-eigenbranes.md) · [D-模](../concepts/d-module.md) · [A-膜](../concepts/a-brane.md)

## 出处（印刷页）

- B p.185–198（B p.185 eq (11.1)）

> 说明：steps 的 provenance 分布：A×6、B×1（共 7 步）；gaps 2 条、pitfalls 2 条。
