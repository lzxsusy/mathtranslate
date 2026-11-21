# 扭 D-模与线丛 λ_𝓛

- **id**：`bdh/concept/twisted-dmodule-lambda`
- **类型**：concept
- **位置**：§5.1
- **问题**：为什么必须先有 λ_𝓛 的 2n 次方同构，才能把 λ_𝓛^{-1}⊗𝒟' 变成 Bun_G 上真正的左 𝒟-模？

> 线丛 λ_𝓛 带 λ_𝓛^{⊗2n}≅(ω^♯)^{⊗n}，故是 𝒟'-模；用它扭 𝒟' 得 Bun_G 上的左 𝒟-模 M_𝓛 与 M_𝔉，后者完整且奇异支集是 Hitchin 纤维化的零纤维。

## 定义

设 $X$ 为光滑完备曲线，$G$ 为约化群，$Z$ 为 ${}^{L}G$ 的中心。对 $\mathcal{L}\in Z\operatorname{tors}_\theta(X)$，4.4.3 定义了 $\operatorname{Bun}_G$ 上的线丛 $\lambda_{\mathcal{L}}\in\mu_\infty\operatorname{tors}_\theta(\operatorname{Bun}_G)$，它带同构 $\lambda_{\mathcal{L}}^{\otimes 2n}\xrightarrow{\sim}(\omega^{\sharp}_{\operatorname{Bun}_G})^{\otimes n}$，其中 $n\ne 0$。这个同构使 $\lambda_{\mathcal{L}}$ 成为 $\mathcal{D}'$-模，于是 $M_{\mathcal{L}}:=\lambda_{\mathcal{L}}^{-1}\otimes_{\mathcal{O}_{\operatorname{Bun}_G}}\mathcal{D}'$ 是 $\operatorname{Bun}_G$ 上的左 $\mathcal{D}$-模。按 2.7.4 与 3.3.2，有典范代数态射 $h_X\varphi_X:A_{{}^{L}\mathfrak{g}}(X)\to\Gamma(\operatorname{Bun}_G,\mathcal{D}')$；$\Gamma(\operatorname{Bun}_G,\mathcal{D}')$ 在 $\mathcal{D}'$ 上的右作用给出 $M_{\mathcal{L}}$ 上的 $A_{{}^{L}\mathfrak{g}}(X)$-模结构，故 $M_{\mathcal{L}}$ 是以 $\operatorname{Spec}A_{{}^{L}\mathfrak{g}}(X)=\mathcal{O}\mathfrak{p}_{{}^{L}\mathfrak{g}}(X)$ 为参数的一族左 $\mathcal{D}$-模。对 ${}^{L}G$-oper $\mathfrak{F}$，令 $M_{\mathfrak{F}}=M_{\mathcal{L}}/\mathfrak{m}_{\mathfrak{F}}M_{\mathcal{L}}=\lambda_{\mathcal{L}}^{-1}\otimes\mathcal{D}'/\mathcal{D}'\mathfrak{m}_{\mathfrak{F}}$，其中 $\mathfrak{m}_{\mathfrak{F}}\subset A_{{}^{L}\mathfrak{g}}(X)$ 是对应于 $\mathfrak{F}$ 的极大理想：这是把参数特化到 $\mathfrak{F}$ 所得的纤维。局部情形（5.2.12）：$\mathcal{GR}$ 上有局部 Pfaffian（普法夫式）线丛 $\lambda_{\mathcal{L}}^{\operatorname{loc}}$，完备化扭泛包络代数 $\bar U'$ 通过 $\Gamma(\mathcal{GR},\mathcal{D}')$ 作用在 $\Gamma(\mathcal{GR},M\lambda_{\mathcal{L}}^{-1})$ 上。

**记号**：$\lambda_{\mathcal{L}}$：$\operatorname{Bun}_G$ 上的线丛，满足 $\lambda_{\mathcal{L}}^{\otimes 2n}\cong(\omega^{\sharp}_{\operatorname{Bun}_G})^{\otimes n}$、$\mathcal{D}'$：$\operatorname{Bun}_G$ 上的扭微分算子环；$M_{\mathcal{L}}=\lambda_{\mathcal{L}}^{-1}\otimes_{\mathcal{O}}\mathcal{D}'$、$A_{{}^{L}\mathfrak{g}}(X)$：$X$ 上 ${}^{L}\mathfrak{g}$-oper 的坐标环；$\mathfrak{m}_{\mathfrak{F}}$：对应于 oper $\mathfrak{F}$ 的极大理想、$\lambda_{\mathcal{L}}^{\operatorname{loc}}$：$\mathcal{GR}$ 上的局部 Pfaffian（普法夫式）线丛

## 关键点

- $\lambda_{\mathcal{L}}$ 是 $\operatorname{Bun}_G$ 上的线丛，带同构 $\lambda_{\mathcal{L}}^{\otimes 2n}\cong(\omega^{\sharp}_{\operatorname{Bun}_G})^{\otimes n}$（$n\ne 0$）；正是这个 2n 次方同构使 $\lambda_{\mathcal{L}}$ 成为 $\mathcal{D}'$-模，从而 $M_{\mathcal{L}}$ 是左 $\mathcal{D}$-模（5.1.1）。
- 典范态射 $h_X\varphi_X:A_{{}^{L}\mathfrak{g}}(X)\to\Gamma(\operatorname{Bun}_G,\mathcal{D}')$ 给出 $M_{\mathcal{L}}$ 的 $A$-模结构；参数空间是 $\operatorname{Spec}A_{{}^{L}\mathfrak{g}}(X)=\mathcal{O}\mathfrak{p}_{{}^{L}\mathfrak{g}}(X)$，即 $X$ 上 ${}^{L}\mathfrak{g}$-oper 的栈（5.1.1）。
- $M_{\mathfrak{F}}$ 是 $M_{\mathcal{L}}$ 在极大理想 $\mathfrak{m}_{\mathfrak{F}}$ 处的纤维：$M_{\mathfrak{F}}=M_{\mathcal{L}}/\mathfrak{m}_{\mathfrak{F}}M_{\mathcal{L}}=\lambda_{\mathcal{L}}^{-1}\otimes\mathcal{D}'/\mathcal{D}'\mathfrak{m}_{\mathfrak{F}}$（5.1.1）。
- 5.1.2(i)：$M_{\mathcal{L}}$ 在 $A_{{}^{L}\mathfrak{g}}(X)$ 上平坦。证明用 $\operatorname{gr}\mathcal{D}'$ 在 $\operatorname{gr}A$ 上平坦（2.2.4(iii)），故 $\mathcal{D}'$ 在 $A$ 上平坦。
- 5.1.2(ii)：$M_{\mathfrak{F}}$ 完整，其奇异支集作为闭链与 Hitchin 纤维化的零纤维重合；这由 $\operatorname{gr}(\mathcal{D}'/\mathcal{D}'I)=\operatorname{gr}\mathcal{D}'/(\operatorname{gr}\mathcal{D}'\cdot\operatorname{gr}I)$ 在 $I$ 极大时读出（5.1.2 的证明）。
- 局部版本（5.2.12）：$\lambda_{\mathcal{L}}^{\operatorname{loc}}$ 是 $\mathcal{GR}$ 上的局部 Pfaffian 丛，$\bar U'$ 经 $\Gamma(\mathcal{GR},\mathcal{D}')$ 作用；基点处的 $\delta$-函数给出 $\mathit{Vac}'=\Gamma(\mathcal{GR},I_1\lambda_{\mathcal{L}}^{-1})$。

## 公式

```latex
\lambda_{\mathcal{L}}^{\otimes 2n}\xrightarrow{\sim}(\omega^{\sharp}_{\operatorname{Bun}_G})^{\otimes n}
```
```latex
M_{\mathcal{L}}:=\lambda_{\mathcal{L}}^{-1}\otimes_{\mathcal{O}_{\operatorname{Bun}_G}}\mathcal{D}'
```
```latex
M_{\mathfrak{F}}=M_{\mathcal{L}}/\mathfrak{m}_{\mathfrak{F}}M_{\mathcal{L}}=\lambda_{\mathcal{L}}^{-1}\otimes\mathcal{D}'/\mathcal{D}'\mathfrak{m}_{\mathfrak{F}}
```
```latex
\operatorname{gr}(\mathcal{D}'/\mathcal{D}'I)=\operatorname{gr}\mathcal{D}'/(\operatorname{gr}\mathcal{D}'\cdot\operatorname{gr}I)
```
```latex
M\lambda_{\mathcal{L}}^{-1}:=M\otimes_{\mathcal{O}_{\mathcal{GR}}}(\lambda_{\mathcal{L}}^{\operatorname{loc}})^{\otimes -1}
```

## 常见错误

- 把 $\lambda_{\mathcal{L}}$ 当普通线丛直接与 $\mathcal{D}'$ 张量：没有 2n 次方同构，$\lambda_{\mathcal{L}}^{-1}\otimes\mathcal{D}'$ 只是 $\mathcal{O}$-模；$\mathcal{D}'$ 的右作用不能转成左 $\mathcal{D}$-模作用，$M_{\mathcal{L}}$ 也就不是 $\mathcal{D}$-模。
- 把 $M_{\mathcal{L}}$ 的平坦性与 $M_{\mathfrak{F}}$ 的完整性混淆：前者是 $A$-模的平坦（5.1.2(i)），后者是 $\mathcal{D}$-模的完整（5.1.2(ii)）；$M_{\mathfrak{F}}$ 已通过 $\mathfrak{m}_{\mathfrak{F}}$ 把 $A$ 特化为 $\mathbb{C}$，再说它“在 $A$ 上平坦”没有意义。
- 把奇异支集写成整个余切丛：5.1.2(ii) 的支集是 Hitchin 纤维化的零纤维这一 Lagrangian 闭链；完整模的奇异支集必须是 Lagrangian，写成整个 $T^*\operatorname{Bun}_G$ 就与“完整”矛盾。

## 批注

### 易错预警：2n 次方不是 n 次方

$\lambda^{\otimes 2n}\cong(\omega^{\sharp})^{\otimes n}$ 的指数差一个因子 2，这不是笔误：$\lambda$ 是 $\omega^{\sharp}$ 的 2n 次根，正是构造扭 $\mathcal{D}$-模所需的那一个根。若按 n 次方记账，就会得出 $\lambda^{-1}\otimes\mathcal{D}'$ 上没有 $\mathcal{D}$-模结构，或把 $\theta$-特征标的平移量算错——后文所有 $\lambda_{\mathcal{L}}$ 的扭都依赖这个 2n。

### 含糊点拨：𝔪_𝔉 处的纤维

$M_{\mathfrak{F}}$ 的定义是商 $M_{\mathcal{L}}/\mathfrak{m}_{\mathfrak{F}}M_{\mathcal{L}}$，等价于把 $A$ 经 $A/\mathfrak{m}_{\mathfrak{F}}=\mathbb{C}$ 特化。这一步与 5.2.8 的“参数族”观点是同一件事的两面：那里把 $\mathfrak{F}_{\mathcal{L}}$ 看成 $X\times\operatorname{Spec}A$ 上的 ${}^{L}G$-torsor 族，这里则在 $\mathfrak{F}$ 处取纤维。5.1.2(ii) 的完整性正是从这个商与 $\operatorname{gr}$ 的计算读出的。

### 背景直觉：Pfaffian 丛从哪来

$\lambda_{\mathcal{L}}$ 来自 $\mu_\infty\operatorname{tors}_\theta(\operatorname{Bun}_G)$；局部版本 $\lambda_{\mathcal{L}}^{\operatorname{loc}}$ 则是 $\mathcal{GR}$ 上的 Pfaffian（普法夫式）丛。它由 $G(K)$ 的中心扩张在 $\mathcal{GR}$ 上的作用给出，且 $1\in\mathbb{C}$ 的作用为乘以 $-1$，于是 $\bar U'$ 反作用于 $\Gamma(\mathcal{GR},\mathcal{D}')$。把“中心扩张—线丛—扭算子环”这条链条记住，5.2.12 与第 8–9 章的全部 $\lambda$ 记号就都能对上。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §5.1；印刷页 [192] / PDF 页 [192]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch05.tex:11-24`
- 页码为原书印刷页，PDF 页 = 印刷页（偏移 0）。5.1.1–5.1.2 在原书 p.192：源码 \SourcePage{193} 起于第 26 行，故第 11–24 行仍在 p.192。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §5.2.12；印刷页 [197] / PDF 页 [197]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch05.tex:96-98`
- 5.2.12 见原书 p.197（\SourcePage{197} 在第 91 行、{198} 在第 106 行）；仅按节号与源码行号定位。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
