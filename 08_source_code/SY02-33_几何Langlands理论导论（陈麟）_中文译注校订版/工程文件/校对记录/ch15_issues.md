# ch15.tex 审读问题（对照英文原 PDF p71–p75）

## ch15.tex:24（原 PDF p72）

- 原文：The defect is measured by a dominant weight λ̌ ∈ X^*(Ť)^+, equivalently by a dominant coweight of G.
- 原译：缺陷由优势余权 $\check\lambda\in X_*(\check T)^+$ 度量，等价地，由 $G$ 的优势权度量。
- 类型：术语
- 改法：缺陷由优势权 $\check\lambda\in X^*(\check T)^+$ 度量，等价地，由 $G$ 的优势余权度量。
- 理由：λ̌ 是 $\check T$ 的权（等价于 $G$ 的余权），译本把“权／余权”整体对偶颠倒，$X_*$ 也应为 $X^*$；否则紧接的 25 行无法与余根 $\check\alpha_i$ 配对。

## ch15.tex:25（原 PDF p72）

- 原文：η mod b̌[[t]] = ∑_{i∈I} t^{〈λ̌,α̌_i〉} ψ_i(t) f_i dt
- 原译：\[\eta\bmod\check{\mathfrak b}[[t]]=\sum_{i\in I}t^{\langle\check\lambda,\alpha_i\rangle}\psi_i(t)f_i\,dt,\]
- 类型：公式
- 改法：指数中的 $\alpha_i$ 改为 $\check\alpha_i$：\[\eta\bmod\check{\mathfrak b}[[t]]=\sum_{i\in I}t^{\langle\check\lambda,\check\alpha_i\rangle}\psi_i(t)f_i\,dt,\]
- 理由：原文指数用余根 $\check\alpha_i$（λ̌ 是权，权与余根配对）；$\alpha_i$ 是下一行用来标记 $f_i\in\check{\mathfrak g}_{-\alpha_i}$ 的简单根，两处不可混用。

## ch15.tex:27（原 PDF p72）

- 原文：Op^unr_Ĝ(k) = ⊔_{λ̌∈Λ̌^+} Op^{reg,λ̌}_Ĝ(k)
- 原译：\[\Op^{\mathrm{unr}}_{\checkG}(k)=\coprod_{\check\lambda\in X_*(\check T)^+}\Op^{\mathrm{reg},\check\lambda}_{\checkG}(k).\]
- 类型：公式
- 改法：\[\Op^{\mathrm{unr}}_{\checkG}(k)=\coprod_{\check\lambda\in X^*(\check T)^+}\Op^{\mathrm{reg},\check\lambda}_{\checkG}(k).\]（也可保留原文的 $\check\Lambda^+$）
- 理由：分层指标 λ̌ 取遍 $\check T$ 的优势权（即 $G$ 的优势余权），而 $X_*(\check T)^+$ 是 $G$ 的优势权；指标集与 24 行同源，整体对偶错位。
