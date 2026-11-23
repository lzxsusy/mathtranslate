# 非消没定理：$R\Gamma$ 的保守性

> `mloc/concept/nonvanishing-theorem` · type=concept · track=C · status=draft · verification=source-only

**别名**：nonvanishing theorem、非消没定理、第 2 章定理 4.1、第 2 章引理 4.2

## 摘要

$\lambda$ 正则时 $R\Gamma$ 保守：复形态射拟同构当且仅当其整体截面复形态射拟同构；故 $R\Gamma(C^\bullet)=0$ 迫使 $C^\bullet=0$。

## 问题

$R\Gamma$ 会漏掉非零复形吗？在什么条件下「所有上同调消没」推出模本身为零？

## 定义

设 $\lambda$ 正则，$D_{qc}(\mathcal{M}(D_\lambda))$ 是 $D(\mathcal{M}(D_\lambda))$ 中上同调拟凝聚的全子范畴。$R\Gamma$ 是整体截面函子 $\Gamma$ 的右导出。非消没定理说：$\lambda$ 正则时 $R\Gamma$ 不杀死任何非零对象，即 $R\Gamma$ 是保守函子。

记号：$D_{qc}(\mathcal{M}(D_\lambda))$：上同调属于 $\mathcal{M}_{qc}(D_\lambda)$ 的复形；$\Gamma(X,-)=\operatorname{Hom}_{D_\lambda}(D_\lambda,-)$；$R\Gamma$ 用内射或 $\Gamma$-零调消解计算；$C^\bullet_f$ 表示态射 $f$ 的映射锥。

## 要点

- 第 2 章定理 4.1 是「$f$ 拟同构 $\Leftrightarrow$ $R\Gamma(f)$ 拟同构」；第 2 章引理 4.2 是其 $D^\bullet=0$ 的特例，两者由映射锥的标准三角互相等价。
- 证明对 $n(\lambda)$ 归纳。底情形 $n(\lambda)=0$（$\lambda$ 反支配）时 $\Gamma$ 正合，若 $H^i(C^\bullet)\neq0$，用 $\mathcal{O}(-2\rho)$ 丰富造出非零整体截面，与 $\Gamma(C^\bullet)=0$ 矛盾。
- 归纳步用第 2 章引理 2.3 的短正合列把 $C^\bullet$ 与 $C^\bullet(p_\alpha)$ 联系起来，而 $n(\lambda+p_\alpha)<n(\lambda)$，故可对后者用归纳假设。
- 第 2 章推论 4.3：$\lambda$ 正则且所有 $H^i(X,V)=0$ 时 $V=0$；第 2 章推论 4.4：$\lambda$ 反支配且正则时每个拟凝聚 $D_\lambda$-模由整体截面生成。
- 第 2 章推论 4.4 正是 §1 中「$\lambda$ 反支配正则时 $Q\mathcal{M}_{qc}=\mathcal{M}_{qc}$」的依据（配合第 3 章定理 1.2）。

## 公式

$$$f\ \text{拟同构}\iff R\Gamma(f)\ \text{拟同构}$$$

$$$R\Gamma(C^\bullet)=0\ \Longrightarrow\ C^\bullet=0\qquad(\lambda\ \text{正则})$$$

$$$H^i(X,V)=0\ (\forall i\ge0)\ \Longrightarrow\ V=0\qquad(\lambda\ \text{正则})$$$

$$$V=\Gamma(X,V)\cdot D_\lambda\qquad(\lambda\ \text{反支配且正则})$$$

## 相关定理

### 第 2 章定理 4.1（非消没定理）

设 $\lambda\in\mathfrak{h}^*$ 正则，$C^\bullet,D^\bullet\in D_{qc}(\mathcal{M}(D_\lambda))$，$f:C^\bullet\to D^\bullet$ 是态射。则 $f$ 是拟同构当且仅当 $R\Gamma(f):R\Gamma(C^\bullet)\to R\Gamma(D^\bullet)$ 是拟同构。

证明状态：`complete`

1. 设 $C^\bullet_f$ 是 $f$ 的映射锥，有标准三角 $C^\bullet_f\to C^\bullet\xrightarrow{f}D^\bullet\to C^\bullet_f[1]$。
   - 为什么：映射锥的标准三角是导出范畴的公理。
2. 施 $R\Gamma$ 得三角 $R\Gamma(C^\bullet_f)\to R\Gamma(C^\bullet)\xrightarrow{R\Gamma(f)}R\Gamma(D^\bullet)\to R\Gamma(C^\bullet_f)[1]$。
   - 为什么：$R\Gamma$ 是三角函子。
3. 若 $R\Gamma(f)$ 拟同构，则由上同调长正合列得 $H^i(R\Gamma(C^\bullet_f))=0$（一切 $i$），即 $R\Gamma(C^\bullet_f)=0$。
   - 为什么：三角中相邻两个态射的锥同调为零，故第三个对象零调。
4. 由第 2 章引理 4.2 得 $C^\bullet_f=0$，故 $f$ 拟同构；反向由 $R\Gamma$ 是函子直接得到。
   - 为什么：$C^\bullet_f=0$ 当且仅当 $f$ 是拟同构。

### 第 2 章引理 4.2（$R\Gamma$ 不杀死非零复形）

设 $\lambda\in\mathfrak{h}^*$ 正则，$C^\bullet\in D_{qc}(\mathcal{M}(D_\lambda))$ 且 $R\Gamma(C^\bullet)=0$。则 $C^\bullet=0$。

证明状态：`complete`

1. 对 $n(\lambda)$ 归纳。设 $n(\lambda)=0$，则 $\Gamma$ 正合；不妨设 $C^\bullet$ 由 $\Gamma$-零调对象组成，此时 $R\Gamma(C^\bullet)=\Gamma(C^\bullet)=0$。
   - 为什么：$\lambda$ 反支配时第 2 章推论 3.2 给出 $\Gamma$ 正合；任一复形可换成 $\Gamma$-零调消解而不改变 $R\Gamma$。
2. 若某 $i$ 使 $H^i(C^\bullet)\neq0$，取支配权 $\mu$ 使 $H^i(C^\bullet)(-\mu)$ 有非零整体截面；由第 2 章引理 2.2 得 $\Gamma(X,H^i(C^\bullet))\otimes F=\Gamma(X,H^i(C^\bullet)\otimes\mathcal{F})\neq0$，故 $\Gamma(X,H^i(C^\bullet))\neq0$。
   - 为什么：$\mathcal{O}(-2\rho)$ 丰富保证 $\mu$ 存在；有限维 $F$ 使整体截面与 $\otimes F$ 交换。
3. 由 $0\to\ker d^i\to C^i\to\operatorname{im}d^i\to0$ 与 $0\to\operatorname{im}d^{i-1}\to\ker d^i\to H^i(C^\bullet)\to0$ 的长正合列（$\Gamma$ 正合使高阶项消失），得 $\Gamma(X,H^i(C^\bullet))=H^i(\Gamma(C^\bullet))$。
   - 为什么：$n(\lambda)=0$ 时 $\Gamma$ 正合，两条短正合列的长正合列退化为短正合列，逐段取出 $H^i$ 项即得。
4. 这与 $H^i(\Gamma(C^\bullet))=0$ 矛盾，故 $n(\lambda)=0$ 时 $C^\bullet=0$。
   - 为什么：$\Gamma(C^\bullet)=R\Gamma(C^\bullet)=0$。
5. 设 $n(\lambda)=k>0$，不妨设 $C^\bullet$ 由 $\Gamma$-零调对象组成。取正则支配权 $\tau$ 使 $\eta=\tau+w(\mu-\lambda)$ 支配，用第 2 章引理 2.2 把 $C^\bullet$ 扭成 $C^\bullet(-w^{-1}\tau)$；它仍由 $\Gamma$-零调对象组成且 $R\Gamma=0$。
   - 为什么：第 2 章引理 2.2 的 $[\lambda]$-截断保持 $\Gamma$-零调性；$w\lambda$、$w\mu$ 反支配使扭变的参数落在可应用范围。
6. 令 $G^\bullet=(C^\bullet(-s_\alpha w^{-1}\sigma)\otimes\mathcal{F})[\lambda]$，用第 2 章引理 2.3 得 $C^\bullet(p_\alpha)$ 由 $\Gamma$-零调对象组成且 $\Gamma(C^\bullet(p_\alpha))=0$；由 $n(s_\alpha\lambda)<k$ 与归纳假设得 $C^\bullet(p_\alpha)=0$，故 $C^\bullet=0$。
   - 为什么：$p_\alpha$ 对应 $s_\alpha\lambda$，其 $n$ 值严格小于 $k$，归纳假设适用。

### 第 2 章推论 4.3（全上同调消没推出模为零）

设 $\lambda\in\mathfrak{h}^*$ 正则，$V\in\mathcal{M}_{qc}(D_\lambda)$。若对一切 $i\ge0$ 有 $H^i(X,V)=0$，则 $V=0$。

证明状态：`complete`

1. 把 $V$ 看作集中在 $0$ 次的复形 $C^\bullet$，则 $R\Gamma(C^\bullet)=0$。
   - 为什么：$R\Gamma$ 在 $0$ 次给出 $\Gamma(V)=H^0(X,V)=0$，高阶项亦然。
2. 由第 2 章引理 4.2 得 $C^\bullet=0$，即 $V=0$。
   - 为什么：第 2 章引理 4.2 对正则 $\lambda$ 与任意 $D_{qc}$ 复形成立。

### 第 2 章推论 4.4（反支配正则时由整体截面生成）

设 $\lambda\in\mathfrak{h}^*$ 反支配且正则，$V\in\mathcal{M}_{qc}(D_\lambda)$。则由 $\Gamma(X,V)$ 生成的子模等于 $V$，即 $V=\Gamma(X,V)\cdot D_\lambda$。

证明状态：`complete`

1. 设 $W=\Gamma(X,V)\cdot D_\lambda\subseteq V$ 是由整体截面生成的子模；由第 2 章推论 3.2，$0\to\Gamma(X,W)\to\Gamma(X,V)\to\Gamma(X,V/W)\to0$ 正合。
   - 为什么：$\lambda$ 反支配使 $\Gamma$ 正合（第 2 章推论 3.2）。
2. 由第 2 章推论 3.2，$\Gamma$ 正合，故 $H^i(X,V/W)=0$ 对一切 $i\ge0$；再由第 2 章推论 4.3 得 $V/W=0$。
   - 为什么：$\lambda$ 反支配使 $\Gamma$ 正合，故 $V/W$ 的各阶上同调全消没；第 2 章推论 4.3 把「全上同调消没」变成「模为零」。
3. 故 $W=V$，即 $V$ 由整体截面生成。
   - 为什么：$W=V$ 是定义。

## 易错点

- 「非消没」不是断言某个 $H^i\neq0$；第 2 章定理 4.1 是 $R\Gamma$ 的保守性，具体非零性要另找（例如 BWB 的 $H^{\ell(w)}$）。
- $\lambda$ 必须正则；奇异 $\lambda$ 时 $R\Gamma$ 可以杀死非零复形（参看第 3 章命题 2.7 的无穷左上同调维数）。
- $D_{qc}(\mathcal{M}(D_\lambda))$ 是全子范畴（上同调拟凝聚），不是 $D(\mathcal{M}_{qc}(D_\lambda))$；两者由第 3 章定理 1.6 等价，但记号与适用对象不同。
- $D_\lambda=D_{X,\lambda+\rho}$；$R\Gamma$ 的 $U_\theta$-模结构经 $U_\theta\cong\Gamma(X,D_\lambda)$（第 2 章定理 6.1），不是任意选取。

## 相关卡

- `mloc/concept/vanishing-theorem`
- `mloc/concept/localization-equivalence`
- `dmod/concept/coherent-d-module`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §4 $D_\lambda$-模上同调的非消没定理 · p.[26, 27, 28]（PDF [30, 31, 32]） · `源码/chapters/ch02b.tex:84-201（第 2 章定理 4.1、第 2 章引理 4.2、第 2 章推论 4.3、4.4 及证明）`
