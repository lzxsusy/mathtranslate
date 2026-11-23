# 与有限维模张量：$V\otimes_\mathbb{C}F$ 与相干族

> `mloc/concept/tensor-with-finite-dimensional` · type=concept · track=E · status=draft · verification=source-only

**别名**：有限维模张量、$\mathcal{M}_{cc}$、相干族、coherent family

## 摘要

对有限维 $\mathfrak{g}$-模 $F$，$V\mapsto V\otimes_\mathbb{C}F$ 保持有限长当且仅当各阶截面张量后有限长；不可约模的张量积由相干族 $\Phi$ 统一编码。

## 问题

与有限维模张量为什么能把各阶截面同调的信息打包成一个定义在整权格 $P(\Sigma)$ 上的相干族 $\Phi$？

## 定义

设 $F$ 是有限维 $\mathfrak{g}$-模，$\mathcal{F}=\mathcal{O}_X\otimes_\mathbb{C}F$，$V\otimes_\mathbb{C}F$ 指 $\Delta_\lambda(V)\otimes_{\mathcal{O}_X}\mathcal{F}$ 的整体截面（即其 $0$ 次上同调）。记 $\mathcal{M}_{cc}(U(\mathfrak{g}))$ 为这样的有限长模范畴：对一切有限维 $F$，$V\otimes_\mathbb{C}F$ 仍有限长；引理 7.3 说明它是厚子范畴、对 $\otimes F$ 封闭。定理 7.7：设 $\lambda$ 正则反支配、$V\in\mathcal{M}_{cc}(U_\theta)$ 不可约，则存在唯一函数 $\Phi:P(\Sigma)\to K(\mathcal{M}_{fl}(U(\mathfrak{g})))$ 满足 $\Phi(0)=\operatorname{ch}(V)$、$\Phi(\nu)$ 是无穷小特征标 $\chi_{\lambda+\nu}$ 的模之差、且 $\operatorname{ch}(V\otimes_\mathbb{C}F)=\sum_\nu\Phi(\nu)$（按 $F$ 的权计重数）；它由显式公式 $\Phi(\mu)=\sum_{p\ge0}(-1)^p\operatorname{ch}(H^p(X,\Delta_\lambda(V)(\mu)))$ 给出（§3.7，ch03f.tex:96-129）。

记号：$\operatorname{ch}$ 为形式特征标，$K$ 为 Grothendieck 群；$\mathcal{M}_{fl}(U(\mathfrak{g}))$ 为有限长 $\mathfrak{g}$-模范畴，$\mathcal{M}_{cc}\subsetneq\mathcal{M}_{fl}$（注 7.2，Stafford 反例）；$\Delta_\lambda(V)(\mu)$ 是几何平移（§2.2），$\mu\in P(\Sigma)$；$\chi_{\lambda+\nu}$ 为无穷小特征标；$S(\theta,F)=\{\lambda+\mu_i\}$ 是 $F$ 的权 $\mu_i$ 平移后的集合。$D_\lambda=D_{X,\lambda+\rho}$ 按 §2.1 约定。

## 要点

- 引理 7.1：$V\otimes_\mathbb{C}F$ 被有限多个 $\chi_{\nu}$（$\nu\in S(\theta,F)$）的乘积 $\prod(\zeta-\chi_\nu(\zeta))$ 零化，故其合成因子只能落在 $\lambda$ 加上 $F$ 的权的有限集合上——这是「有限长」的来源。
- 引理 7.4 给的是（$\lambda$ 正则时的）等价：$V\otimes_\mathbb{C}F$ 有限长 $\iff$ 各 $H^p(X,\Delta_\lambda(V)(\nu))$ 有限长；一般情形只断言单向。
- $\mathcal{M}_{cc}$ 严格小于 $\mathcal{M}_{fl}$（注 7.2，Stafford 反例），所以定理 7.7 的前提 $V\in\mathcal{M}_{cc}$ 不能放宽成「有限长」。
- 命题 7.5：$\lambda$ 反支配、$\Delta_\lambda(V)$ 完整时，$V\otimes_\mathbb{C}F$ 有限长；这把完整性（几何条件）转成了纯代数结论。
- 定理 7.7 的显式公式是 Euler 示性数：用 $\Delta_\lambda(V)\otimes\mathcal{F}$ 的滤过谱序列，$E_1$ 项是各 $H^{p-q}(X,\Delta_\lambda(V)(\nu_q))$，收敛到 $H^p(X,\Delta_\lambda(V))\otimes F$，而后者只在 $p=0$ 非零，故总 Euler 数等于 $\operatorname{ch}(V\otimes F)$。
- 唯一性靠权重数分离：由 [5, Ch. VI] 存在权集为 $\{w\mu\}$（各重数 $1$）的有限维模，故 $\sum_w\Phi(w\mu)$ 由 (iii) 唯一确定；再由 $\lambda$ 正则反支配推出这些项的无穷小特征标互不相同。

## 公式

$$$\Phi(\mu)=\sum_{p\ge0}(-1)^p\operatorname{ch}\bigl(H^p(X,\Delta_\lambda(V)(\mu))\bigr)$$$

$$$\operatorname{ch}(V\otimes_\mathbb{C}F)=\sum_{\nu}\Phi(\nu)$$$

$$$\prod_{\nu\in S(\theta,F)}\bigl(\zeta-\chi_\nu(\zeta)\bigr)\ \text{零化}\ V\otimes_\mathbb{C}F$$$

$$$H^p\bigl(X,\Delta_\lambda(V)(\nu)\bigr)\ \text{有限长}\ (\forall\nu)\ \Longrightarrow\ V\otimes_\mathbb{C}F\ \text{有限长}$$$

## 相关定理

### 定理 7.7：相干族的存在唯一性与显式公式

设 $\lambda$ 正则反支配，$V$ 是 $\mathcal{M}_{cc}(U_\theta)$ 中的不可约模。则存在唯一函数 $\Phi:P(\Sigma)\to K(\mathcal{M}_{fl}(U(\mathfrak{g})))$，使 (i) $\Phi(0)=\operatorname{ch}(V)$；(ii) $\Phi(\nu)$ 是若干无穷小特征标为 $\chi_{\lambda+\nu}$ 的 $\mathfrak{g}$-模之差；(iii) 对任意有限维 $F$ 有 $\operatorname{ch}(V\otimes_\mathbb{C}F)=\sum_\nu\Phi(\nu)$（$\nu$ 取遍 $F$ 的权，按重数计）。并且 $\Phi(\mu)=\sum_{p\ge0}(-1)^p\operatorname{ch}(H^p(X,\Delta_\lambda(V)(\mu)))$。

证明状态：`complete`

1. 先验证显式公式满足 (i)(ii)。(i) 由 $\Delta_\lambda(V)(0)=\Delta_\lambda(V)$ 且 $H^0(X,\Delta_\lambda(V))=V$ 得出；(ii) 由 $H^p$ 只含无穷小特征标 $\chi_{\lambda+\mu}$ 的模得出。
   - 为什么：对 $\mu$ 平移到 $\lambda+\mu$ 后，$\Delta_\lambda(V)(\mu)$ 的无穷小特征标就是 $\chi_{\lambda+\mu}$，故各项的差落在该特征标上。
2. 验证 (iii)：对 $\Delta_\lambda(V)\otimes_{\mathcal{O}_X}\mathcal{F}$ 的滤过取谱序列，其 $E_1$ 项为 $H^{p-q}(X,\Delta_\lambda(V)(\nu_q))$，收敛到 $H^p(X,\Delta_\lambda(V))\otimes_\mathbb{C}F$，后者当 $p=0$ 时等于 $V\otimes_\mathbb{C}F$、当 $p\ne0$ 时为 $0$。
   - 为什么：滤过的分次层是 $\Delta_\lambda(V)(\nu_q)$ 的直和（$\nu_q$ 取遍 $F$ 的权），谱序列的 $E_1$ 就是逐项上同调。
3. 计算 $E_1$ 总复形的 Euler 示性数：$\sum_{p,q}(-1)^{p+q}\operatorname{ch}(H^{p-q}(X,\Delta_\lambda(V)(\nu_q)))=\sum_{s,\nu}(-1)^s\operatorname{ch}(H^s(X,\Delta_\lambda(V)(\nu)))$；由 Euler 原理它等于 $E_\infty$ 的 Euler 数，即 $\operatorname{ch}(V\otimes_\mathbb{C}F)$。
   - 为什么：谱序列不改变 Euler 示性数，而 $E_\infty$ 就是 $\operatorname{Gr}$ 后的 $H^p(X,\Delta_\lambda(V))\otimes F$，只有 $p=0$ 一项存活。
4. 证唯一性：映射 $F\mapsto\operatorname{ch}(V\otimes F)$ 延拓到有限维模范畴的 Grothendieck 群上；对支配权 $\mu$，取权集为 $\{w\mu\}$、各重数为 $1$ 的有限维模，则 $\sum_{w\in W}\Phi(w\mu)$ 被 (iii) 唯一确定。
   - 为什么：这种有限维模在 Grothendieck 群里可用基础表示表示，故 $\sum_w\Phi(w\mu)$ 是已知量。
5. 再由 (ii)，$\sum_w\Phi(w\mu)$ 的各项对应的无穷小特征标互不相同：若 $\chi_{\lambda+\mu}=\chi_{\lambda+w\mu}$，则存在 $w'$ 使 $w'(\lambda+w\mu)=\lambda+\mu$，推出 $w'\in W_\lambda$ 且（用 $\lambda$ 正则反支配与 $\mu$ 支配）$w'=1$、$w\mu=\mu$。故每一项被唯一分离，$\Phi$ 唯一。
   - 为什么：$\lambda$ 正则使 $W_\lambda$ 的平移不能抵消 $\mu$ 的支配性，这是唯一性真正的用武之地。

### 引理 7.4：有限长判据

设 $V\in\mathcal{M}(U_\theta)$，$F$ 有限维。若对一切 $\nu$ 有 $H^p(X,\Delta_\lambda(V)(\nu))$ 有限长，则 $V\otimes_\mathbb{C}F$ 有限长；当 $\lambda$ 正则时这是等价。

证明状态：`sketch`

1. 对 $\Delta_\lambda(V)\otimes\mathcal{F}$ 的滤过取谱序列，其 $E_1$ 项是 $H^{p-q}(X,\Delta_\lambda(V)(\nu_q))$，收敛到 $H^p(X,\Delta_\lambda(V))\otimes F$。
   - 为什么：与定理 7.7 的证明同一个谱序列，只是这里只关心有限长性。
2. 对 $p$ 归纳：$E_1$ 各项有限长且只有有限多个非零，故每个 $H^p(X,\Delta_\lambda(V))\otimes F$ 有限长；特别地 $p=0$ 给出 $V\otimes F$ 有限长。
   - 为什么：谱序列的收敛项由 $E_1$ 逐步取上同调得到，有限长的扩张仍有限长。
3. $\lambda$ 正则时反向也成立：$\Gamma$ 与 $\Delta_\lambda$ 互为逆（定理 1.12），故 $V\otimes F$ 的有限长性回推各项有限长。
   - 为什么：正则性保证 $R\Gamma$ 与 $L\Delta_\lambda$ 的等价，从而两侧信息对等。

> 缺口：证明依赖定理 1.12 与附录 C 的谱序列构造；本卡只复述其骨架，未逐行复核谱序列的收敛细节。

### 命题 7.5：完整模的张量积有限长

设 $\lambda$ 反支配，$\Delta_\lambda(V)$ 完整。则对任意有限维 $F$，$V\otimes_\mathbb{C}F$ 有限长。

证明状态：`sketch`

1. 完整模有有限长，故可设 $\Delta_\lambda(V)$ 不可约，并取其在 $\Gamma$ 下的像。
   - 为什么：完整模的有限长性（ch03e.tex:280）允许对长度归纳，归约到不可约情形。
2. 用引理 5.3 取 $\Delta_\lambda(V)$ 中不含非零截面的最大子模，把问题化到 $\Gamma(X,V)\ne0$ 的情形。
   - 为什么：无截面部分对 $\otimes F$ 的贡献可由 5.7 控制，有截面部分才是 5.1 的适用范围。
3. 在 $\Gamma(X,V)\ne0$ 时用命题 5.1，$V$ 由不可约 $U_\theta$-模生成，再用引理 7.4 的判据得 $V\otimes F$ 有限长。
   - 为什么：5.1 把几何对象换成不可约 $U_\theta$-模，7.4 则把有限长性化为截面同调的有限长性。

> 缺口：第 2 步对「最大无截面子模」的商所做的 $\otimes F$ 分析依赖 5.7 的短正合列与 7.4 的归纳（底本 ch03f.tex:78-87），本卡未逐行复核。

## 易错点

- 定理 7.7 要求 $\lambda$ 正则反支配且 $V\in\mathcal{M}_{cc}$；不正则时无穷小特征标会塌缩，第 5 步的唯一性论证失效。
- $\mathcal{M}_{cc}\subsetneq\mathcal{M}_{fl}$ 是真包含（注 7.2 的 Stafford 反例）；把 7.7 用在仅有限长的 $V$ 上属于超出原文的推广。
- 显式公式里的 $H^p$ 取的是 $\Delta_\lambda(V)(\mu)$（已作几何平移）的上同调，不是 $V$ 的；漏掉 $(\mu)$ 会把 $\Phi$ 算成常数。
- $V\otimes_\mathbb{C}F$ 的 $D$-模结构来自 $\Delta_\lambda(V)\otimes_{\mathcal{O}_X}\mathcal{F}$，不是把 $F$ 当常层张量——后者会丢掉 $\mathfrak{g}$-模结构，得到的特征标也不是 $\operatorname{ch}(V\otimes F)$。

## 相关卡

- `mloc/concept/intertwining-and-holonomic`
- `mloc/concept/irreducible-d-lambda-sections`
- `mloc/concept/geometric-translation-functor`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.7 与有限维模张量（引理 7.1–7.5、注 7.2） · p.[68, 69]（PDF [72, 73]） · `源码/chapters/ch03f.tex:6-95（引理 7.1、注 7.2、引理 7.3–7.5、注 7.6）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.7 相干族（定理 7.7） · p.[69, 70]（PDF [73, 74]） · `源码/chapters/ch03f.tex:96-129（定理 7.7、显式公式与相干族）`
