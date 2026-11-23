# 交织函子的拟逆：$\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D}$ 与 $\Gamma$ 的交换

> `mloc/concept/inverse-intertwining-functor` · type=concept · track=E · status=draft · verification=source-only

**别名**：$LI_w$ 的拟逆、交织函子的逆、对偶与 $R\Gamma$ 的交换、inverse intertwining functor

## 摘要

$LI_w$ 的拟逆是 $\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D}$：对偶把 $w$ 换成 $w^{-1}$，与 $R\Gamma$ 的交换是关键。

## 问题

$LI_w$ 的拟逆为什么能写成 $\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D}$，其中对偶与整体截面 $R\Gamma$ 的交换起了什么作用？

## 定义

记 $\theta=W\cdot\lambda$。对偶函子 $\mathbb{D}(V^\bullet)=R\Hom_{D_\lambda}(V^\bullet,\mathbb{D}(D_\lambda))[\dim X]$ 把 $D^b_{coh}(D_\lambda)$ 送到 $D^b_{coh}(D_{-\lambda})$（§3.4，ch03e.tex:12-13）。定理 4.4：$LI_w:D^b_{coh}(D_\lambda)\to D^b_{coh}(D_{w\lambda})$ 的拟逆等于 $\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D}$。证明的关键是「对偶与整体截面交换」：引理 4.2 给出 $R\Gamma(\mathbb{D}(V^\bullet))=R\Hom_{D_\lambda}(V^\bullet,\mathbb{D}(D_\lambda))[\dim X]$；当 $\lambda$ 正则时 $R\Gamma\circ\mathbb{D}=\mathbb{D}_{alg}[\dim X]\circ R\Gamma$（引理 4.3），其中 $\mathbb{D}_{alg}(V^\bullet)=R\Hom_{U_\theta}(V^\bullet,\mathbb{D}(U_\theta))$。

记号：$\mathbb{D}(D_\lambda)$ 是 $D_\lambda$ 的对偶模，$\dim X$ 为旗簇维数（等于 $\dim\mathfrak{n}$）；$\theta=W\cdot\lambda$，$U_\theta$ 为 $\theta$ 的完全素化包络。$\lambda$ 正则时 $U_\theta$ 同调维数有限、且主反自同构给出 $U_\theta^\circ\cong U_{-\theta}$，故 $\mathbb{D}_{alg}$ 把 $D^b_{fg}(U_\theta)$ 送到 $D^b_{fg}(U_{-\theta})$ 且 $\mathbb{D}_{alg}^2\cong1$（ch03e.tex:52-54）。$D_\lambda=D_{X,\lambda+\rho}$ 按 §2.1 约定；$(\nu)$ 为几何平移（§2.2），$\mathbb{D}(V(\nu))=\mathbb{D}(V)(-\nu)$。

## 要点

- 拟逆不是 $LI_{w^{-1}}$ 本身：$LI_{w^{-1}}$ 确实把 $D_{w\lambda}$ 送回 $D_\lambda$，但只有当 $\lambda$ 是 $\Sigma^+_w$-反支配时它才同构于 $LI_w$ 的逆（定理 3.19(i)）；一般情形必须夹上两个 $\mathbb{D}$。
- $\mathbb{D}$ 把 $D_\lambda$ 送到 $D_{-\lambda}$，所以三项复合 $\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D}$ 才回到出发范畴，途中经过 $D_{-w\lambda}$ 与 $D_{-\lambda}$。
- 引理 4.3 的交换性在正则 $\lambda$ 时才给出 $\mathbb{D}_{alg}$ 的形式：正则性保证 $U_\theta$ 同调维数有限、$U_\theta^\circ\cong U_{-\theta}$，从而代数对偶是良好定义的。
- 证明先对单反射做：若 $\lambda$ 是 $\alpha$-反支配，则由定理 3.23（$R\Gamma\circ LI_{s_\alpha}\cong R\Gamma$）推得 $LI_{s_\alpha}\circ(\mathbb{D}\circ LI_{s_\alpha}\circ\mathbb{D})\cong1$，再用几何平移（引理 3.5）推到任意 $w$。
- 对偶与平移交换时权要变号：$\mathbb{D}(V(\nu))=\mathbb{D}(V)(-\nu)$（引理 4.1），这是引理 4.3 的图表能对齐的原因。
- 引理 4.2 的证明依赖「$\Hom_{D_\lambda}(P,\mathbb{D}(D_\lambda))$ 对 $\Gamma$ 零调」这一事实（$P$ 取凝聚投射对象），它是把 $R\Gamma$ 换成 $R\Hom$ 的技术要点。

## 公式

$$$\mathbb{D}(V^\bullet)=R\Hom_{D_\lambda}\bigl(V^\bullet,\mathbb{D}(D_\lambda)\bigr)[\dim X]$$$

$$$(LI_w)^{-1}\cong\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D}$$$

$$$R\Gamma\bigl(\mathbb{D}(V^\bullet)\bigr)=R\Hom_{D_\lambda}\bigl(V^\bullet,\mathbb{D}(D_\lambda)\bigr)[\dim X]$$$

$$$R\Gamma\circ\mathbb{D}=\mathbb{D}_{alg}[\dim X]\circ R\Gamma\qquad(\lambda\ \text{正则})$$$

$$$\mathbb{D}\bigl(V^\bullet(\nu)\bigr)=\mathbb{D}(V^\bullet)(-\nu)$$$

## 相关定理

### 定理 4.4：拟逆的公式

对任意 $w\in W$，交织函子 $LI_w:D^b_{coh}(D_\lambda)\to D^b_{coh}(D_{w\lambda})$ 的拟逆等于 $\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D}:D^b_{coh}(D_{w\lambda})\to D^b_{coh}(D_\lambda)$。

证明状态：`complete`

1. 先设 $\lambda$ 是 $\alpha$-反支配的。由定理 3.23 有 $R\Gamma\circ LI_{s_\alpha}\cong R\Gamma$，又由引理 4.3 有 $R\Gamma\circ\mathbb{D}=\mathbb{D}_{alg}[\dim X]\circ R\Gamma$（$\lambda$ 正则时），于是 $R\Gamma(\mathbb{D}(V^\bullet))=R\Gamma(\mathbb{D}(LI_{s_\alpha}(V^\bullet)))$。
   - 为什么：$R\Gamma\circ LI_{s_\alpha}\cong R\Gamma$ 把 $LI_{s_\alpha}$ 从 $R\Gamma$ 中消去，而引理 4.3 允许把 $\mathbb{D}$ 移到 $R\Gamma$ 的另一侧。
2. 注意 $\mathbb{D}(V^\bullet)\in D^b_{coh}(D_{-\lambda})$ 而 $\mathbb{D}(LI_{s_\alpha}(V^\bullet))\in D^b_{coh}(D_{-s_\alpha\lambda})$；因 $-s_\alpha\lambda$ 是 $\alpha$-反支配的，可对后者再用一次第 1 步，得 $R\Gamma(\mathbb{D}(V^\bullet))=R\Gamma(LI_{s_\alpha}\mathbb{D}(LI_{s_\alpha}(V^\bullet)))$。
   - 为什么：反支配性在 $\lambda\mapsto-s_\alpha\lambda$ 下保持，这正是能把 $LI_{s_\alpha}$ 反复搬运的原因。
3. 两个复形同在 $D^b_{coh}(D_{-\lambda})$ 中，而 $R\Gamma$ 是范畴等价，故它们同构：$\mathbb{D}(V^\bullet)=LI_{s_\alpha}(\mathbb{D}(LI_{s_\alpha}(V^\bullet)))$，即 $LI_{s_\alpha}\circ(\mathbb{D}\circ LI_{s_\alpha}\circ\mathbb{D})\cong1$。
   - 为什么：正则 $\lambda$ 时 $R\Gamma$ 与 $L\Delta$ 互为逆（定理 1.12），故 $R\Gamma$ 反映同构。
4. 这些函子都与几何平移交换（引理 3.5、4.1），故上述关系对任意 $w$ 成立：$LI_w\circ(\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D})\cong1$。
   - 为什么：几何平移是范畴等价且只把权按 $w$ 搬运，单反射情形的等式可沿既约分解搬过去。

### 引理 4.3：$R\Gamma$ 与 $\mathbb{D}$ 的交换

设 $\lambda\in\mathfrak{h}^*$ 正则。则函子图表交换：$R\Gamma\circ\mathbb{D}=\mathbb{D}_{alg}[\dim X]\circ R\Gamma$，其中 $\mathbb{D}_{alg}(V^\bullet)=R\Hom_{U_\theta}(V^\bullet,\mathbb{D}(U_\theta))$。

证明状态：`sketch`

1. 取 $U_\theta$-模的上方有界复形 $F^\bullet\to V^\bullet$，其中 $F^\bullet$ 由有限秩自由 $U_\theta$-模组成，并用 $L\Delta_\lambda(F^\bullet)$ 替换 $V^\bullet$。
   - 为什么：$L\Delta_\lambda$ 是 $D^b_{fg}(U_\theta)\simeq D^b_{coh}(D_\lambda)$ 的等价（定理 1.12），故可在 $D_\lambda$ 一侧用自由消解计算。
2. 用引理 4.2 把 $R\Gamma(\mathbb{D}(\Delta_\lambda(F^\bullet)))$ 写成 $R\Hom_{D_\lambda}(\Delta_\lambda(F^\bullet),\mathbb{D}(D_\lambda))[\dim X]$，再把它化成 $\Hom^\bullet_{U_\theta}(F^\bullet,\mathbb{D}(U_\theta))[\dim X]$。
   - 为什么：$\Delta_\lambda$ 与 $\Gamma$ 在自由对象上互为逆，$\Hom_{D_\lambda}(\Delta_\lambda(-),\mathbb{D}(D_\lambda))$ 就是 $\Hom_{U_\theta}(-,\mathbb{D}(U_\theta))$。
3. 自由复形上 $\Hom^\bullet$ 与 $R\Hom$ 一致，故得 $\mathbb{D}_{alg}(V^\bullet)[\dim X]$，即 $R\Gamma\circ\mathbb{D}=\mathbb{D}_{alg}[\dim X]\circ R\Gamma$。
   - 为什么：$F^\bullet$ 的每一项都自由，$\Hom$ 复形自动是右导出函子的模型，无需再取消解。

> 缺口：第 2 步把 $\Hom_{D_\lambda}(\Delta_\lambda(-),\mathbb{D}(D_\lambda))$ 等同于 $\Hom_{U_\theta}(-,\mathbb{D}(U_\theta))$，其细节依赖定理 1.12 与 $\mathbb{D}(D_\lambda)$ 的显式描述（底本 ch03e.tex:56-66），本卡未逐行复核。

### 引理 4.1：对偶与几何平移交换（权变号）

对任意 $\nu\in P(\Sigma)$，函子图表交换：先作 $\mathbb{D}$ 再作 $(-\nu)$，等于先作 $(\nu)$ 再作 $\mathbb{D}$；即 $\mathbb{D}(V^\bullet(\nu))=\mathbb{D}(V^\bullet)(-\nu)$。

证明状态：`complete`

1. 用 $\mathbb{D}(D_{\lambda+\nu})=\mathcal{O}(\nu)\otimes\mathbb{D}(D_\lambda)\otimes\mathcal{O}(-\nu)$ 把对偶模的扭变写成共轭。
   - 为什么：该等式由 $D_{\lambda+\nu}=(D_\lambda)(\nu)$ 与对偶对张量的相容性直接得出。
2. 代入 $\mathbb{D}(V(\nu))=R\Hom_{D_{\lambda+\nu}}(\mathcal{O}(\nu)\otimes V,\ \mathcal{O}(\nu)\otimes\mathbb{D}(D_\lambda)\otimes\mathcal{O}(-\nu))[\dim X]$，把共用的 $\mathcal{O}(\nu)\otimes(-)$ 从 $R\Hom$ 两侧消去。
   - 为什么：$\mathcal{O}(\nu)$ 可逆，张量它不改变 $R\Hom$ 的同构类型，只把 $\mathcal{O}(-\nu)$ 留在外面。
3. 得到 $R\Hom_{D_\lambda}(V,\mathbb{D}(D_\lambda))[\dim X]\otimes\mathcal{O}(-\nu)=\mathbb{D}(V)(-\nu)$。
   - 为什么：这正是 $\mathbb{D}$ 与 $(-\nu)$ 交换的断言。

## 易错点

- 定理 4.4 是在 $D^b_{coh}$ 上说的；不能直接读到 $\mathcal{M}_{qc}$ 层——那里 $I_w$ 只右正合，可逆性要用推论 3.22 的条件。
- $\mathbb{D}$ 是反变函子，复合顺序不能交换：把 $\mathbb{D}\circ LI_{w^{-1}}\circ\mathbb{D}$ 写成 $LI_{w^{-1}}\circ\mathbb{D}\circ\mathbb{D}$ 会得到反方向（且 $\mathbb{D}^2\ncong1$ 于层上，只在 $\mathbb{D}_{alg}$ 上成立）。
- 引理 4.3 要求 $\lambda$ 正则；不正则时 $U_\theta$ 的同调维数与 $U_\theta^\circ\cong U_{-\theta}$ 都失去保证，只能退回引理 4.2 的 $R\Gamma\circ\mathbb{D}$ 表述。
- 引理 4.1 的平移方向容易写反：$\mathbb{D}$ 把 $\mathcal{O}(\nu)$ 的扭变送到 $\mathcal{O}(-\nu)$，不是 $\mathcal{O}(\nu)$；这与对偶把 $D_\lambda$ 送到 $D_{-\lambda}$ 是同一件事。

## 相关卡

- `mloc/concept/intertwining-functor-i-w`
- `mloc/concept/weyl-group-action-on-d-lambda-modules`
- `mloc/concept/intertwining-and-holonomic`
- `mloc/concept/geometric-translation-functor`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.4 对偶函子与 $\Gamma$ 的交换（引理 4.1–4.3） · p.[59, 60]（PDF [63, 64]） · `源码/chapters/ch03e.tex:12-24, 47-77（$\mathbb{D}$、引理 4.1、4.2、4.3）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · §3.4 拟逆的公式（定理 4.4） · p.[61]（PDF [65]） · `源码/chapters/ch03e.tex:79-100（定理 4.4 及其证明）`
