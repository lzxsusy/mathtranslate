# Delta 函数与 Hecke 特征值

- **id**：`bdh/concept/delta-function-eigenvalue`
- **类型**：concept
- **位置**：§10.1
- **问题**：为什么 𝔡_{𝓛,χ} 上的 Cartan 作用恰好是 χ，而不是被扭 λ 或临界内积修正过的另一个权？

> 最低特征空间 𝔡_{𝓛,χ} 由 δ 型截面实现，Cartan 子代数按 χ 作用；把这一作用写成式 (394)，再用最高权 -hBχ 的 Verma 特征标的平坦形变证明它。

## 定义

设 $\mathcal{L}\in Z\operatorname{tors}_\theta(O)$，$\chi\in P_+({}^{L}G)$，$\lambda=\lambda_{\mathcal{L}}$ 是 $\mathcal{GR}$ 上的局部 Pfaffian（普法夫式）丛，$\mathfrak{d}_{\mathcal{L},\chi}$ 是 8.1.5 中的最低特征空间。8.1.5 给出典范嵌入 $\mathfrak{d}_{\mathcal{L},\chi}\hookrightarrow\Gamma(\mathcal{GR},I_\chi\lambda_{\mathcal{L}}^{-1})$，其像含于 $G(O)$-不变部分之中。用 (81) 把 $I/I^2$ 与李代数胚 $\mathfrak{a}_{{}^{L}\mathfrak{g}}$ 等同；有李子代数胚 $\mathfrak{a}_{{}^{L}\mathfrak{n}}\subset\mathfrak{a}_{{}^{L}\mathfrak{b}}\subset\mathfrak{a}_{{}^{L}\mathfrak{g}}$，且 $\mathfrak{a}_{{}^{L}\mathfrak{b}}/\mathfrak{a}_{{}^{L}\mathfrak{n}}=A_{{}^{L}\mathfrak{g}}(O)\otimes{}^{L}\mathfrak{h}$。定理 10.1.2 断言：(i) $\mathfrak{a}_{{}^{L}\mathfrak{n}}$ 零化 $\mathfrak{d}_{\mathcal{L},\chi}$，故 $a\delta$ 对 $a\in{}^{L}\mathfrak{h}$、$\delta\in\mathfrak{d}_{\mathcal{L},\chi}$ 有意义；(ii) $a\delta=\chi(a)\delta$。10.1.3 把它改写成 $a\delta=-(d(a),B\chi)\cdot\delta$（$a\in I^{\le 0}$），其中 $d:I^{\le 0}\to\mathfrak{h}$ 是 (83) 中的映射，$\chi$ 被看作 $\mathfrak{h}$ 的元素，$B:\mathfrak{h}\to\mathfrak{h}^*$ 对应于临界内积 (18)。证明路线：10.1.5 在 $U_\chi$ 上构造平坦 $\mathbb{C}[h]$-族 $M$（$\mathcal{D}_{\lambda^h}$-模）与嵌入 $\mathfrak{d}_\chi\hookrightarrow\Gamma(U_\chi,M\lambda^{-1})$，使 $h=0$ 的纤维与 (392) 一致、像被 $\mathfrak{g}\otimes\mathfrak{m}$ 零化、且 $c\in C=U\mathfrak{g}$ 按最高权 $-hB\chi$ 的 Verma 特征标 $\varphi$ 作用；10.1.6 由这些性质推出 (397) 与 (398)，再由 10.1.5(ii) 得 (394)；10.1.7 具体构造 $M$：沿闭嵌入 $\operatorname{Orb}_\chi\hookrightarrow U_\chi$ 取正向像，$M=\omega_{\operatorname{Orb}_\chi}\otimes_{\mathcal{O}}N$，其中 $N=p^{\dagger}\mathcal{D}_{\lambda^{-h}}$，并用 $l=B\chi$（即 9.1.13）验证所需交换性。

**记号**：$\mathfrak{d}_{\mathcal{L},\chi}$：$\Gamma(\mathcal{GR},I_\chi\lambda_{\mathcal{L}}^{-1})^{G(O)}$ 中由 (392) 给出的最低特征空间、$\mathfrak{a}_{{}^{L}\mathfrak{g}}$：与 $I/I^2$ 等同的李代数胚；$\mathfrak{a}_{{}^{L}\mathfrak{n}}\subset\mathfrak{a}_{{}^{L}\mathfrak{b}}$ 为子代数胚、$d:I^{\le 0}\to\mathfrak{h}$：(83) 中的映射；$B:\mathfrak{h}\to\mathfrak{h}^*$：临界内积 (18) 诱导的同构、$\varphi$：最高权 $-hB\chi$ 的 Verma 模特征标，$\varphi:C\to\mathbb{C}[h]$

## 关键点

- 10.1.1：8.1.5 给出 $\mathfrak{d}_{\mathcal{L},\chi}\hookrightarrow\Gamma(\mathcal{GR},I_\chi\lambda_{\mathcal{L}}^{-1})$，像在 $G(O)$-不变部分；$I/I^2$ 与 $\mathfrak{a}_{{}^{L}\mathfrak{g}}$ 等同，且 $\mathfrak{a}_{{}^{L}\mathfrak{b}}/\mathfrak{a}_{{}^{L}\mathfrak{n}}=A_{{}^{L}\mathfrak{g}}(O)\otimes{}^{L}\mathfrak{h}$，故 $a\delta$ 对 $a\in{}^{L}\mathfrak{h}$ 有意义。
- 10.1.2：(i) $\mathfrak{a}_{{}^{L}\mathfrak{n}}$ 零化 $\mathfrak{d}_{\mathcal{L},\chi}$；(ii) $a\delta=\chi(a)\delta$。这里 $\chi\in P_+({}^{L}G)$ 同时被看作 ${}^{L}\mathfrak{h}$ 上的线性泛函（10.1.2 的注），$a$ 取遍 ${}^{L}\mathfrak{h}$。
- 10.1.3：等价形式 (394) 是 $a\delta=-(d(a),B\chi)\cdot\delta$（$a\in I^{\le 0}$）；负号与 $B\chi$ 源自左端定义所用的映射 (291) 依赖 $\mathfrak{g}$ 上内积的选取（10.1.3 的注）。
- 10.1.5：证明策略是构造平坦 $\mathbb{C}[h]$-族 $M$ 与嵌入 (395)，使四条性质成立；关键是 (iv) $c\delta_h=\varphi(c)\delta_h$，即 $C$ 通过最高权 $-hB\chi$ 的 Verma 特征标作用。10.1.4 说明为何不能直接形变 $I_\chi$：$\operatorname{Orb}_\chi$ 上的可逆 $\lambda^h$-扭 $\mathcal{D}$-模只对离散的 $h$ 存在。
- 10.1.6：由 (i)–(iv) 推出 (397) $a^{\flat}\delta_0=-(d(a),B\chi)\delta_0$ 与 (398)；再用 10.1.5(ii) 中“$M_0$ 的合成等于 (392)”把 $\delta_0$ 换回 $\delta$，即得 (394)。
- 10.1.7：$M$ 的构造是 $M=\omega_{\operatorname{Orb}_\chi}\otimes_{\mathcal{O}}N$ 沿 $\operatorname{Orb}_\chi\hookrightarrow U_\chi$ 的正向像，$N=p^{\dagger}\mathcal{D}_{\lambda^{-h}}$；(ii)–(iv) 归约为 $(\mathfrak{g}\otimes\mathfrak{m})\mathbb{1}=0$ 与 $c\mathbb{1}=\varphi(c)\mathbb{1}$，后者等价于图 (404) 的交换性，由 (405) $l=B\chi$（命题 9.1.13）推出。

## 公式

```latex
\mathfrak{d}_{\mathcal{L},\chi}\hookrightarrow\Gamma(\mathcal{GR},I_\chi\lambda_{\mathcal{L}}^{-1})
```
```latex
a\delta=\chi(a)\delta
```
```latex
a\delta=-(d(a),B\chi)\cdot\delta
```
```latex
\mathfrak{d}_\chi\hookrightarrow\Gamma(U_\chi,M\lambda^{-1})
```
```latex
c\delta_{h}=\varphi(c)\delta_{h}
```
```latex
a^{\flat}\delta_{0}=-(d(a),B\chi)\cdot\delta_{0}
```
```latex
h^{-1}\tilde a\cdot\delta_{h}\equiv-(d(a),B\chi)\cdot\delta_{h}\mod h
```
```latex
\omega_{\operatorname{Orb}_\chi}\to\omega_{\operatorname{Orb}_\chi}\otimes_{\mathcal{O}}N
```
```latex
l=B\chi
```

## 常见错误

- 把 (394) 当成 (ii) 的平凡改写：$\chi$ 作为 ${}^{L}\mathfrak{h}$ 的元素与作为支配权的等同、$d$ 与 $B$ 的选取都依赖 3.6.11 与内积 (18)；漏掉 $B$ 会把右端写成 $-(d(a),\chi)\delta$，差一个内积识别。
- 把 (394) 的符号写反：源码是 $a\delta=-(d(a),B\chi)\cdot\delta$，负号来自 (291) 的定义；改成正号会使 10.1.6 中 (397) 与 $\varphi(c)$ 的 $h$ 系数不一致，进而推不出 (394)。
- 以为可以在 $\operatorname{Orb}_\chi$ 上直接取 $\lambda^h$-扭 $\mathcal{D}$-模族：10.1.4 明确说这对连续 $h$ 不可能（可逆 $\lambda^h$-扭 $\mathcal{D}$-模只对离散的 $h$ 存在），所以 10.1.7 改用 $U_\chi$ 上的正向像构造 $M$。

## 批注

### 易错预警：χ 的两个身份

$\chi\in P_+({}^{L}G)$ 在这里同时被当作 ${}^{L}\mathfrak{h}$ 上的线性泛函（10.1.2 的注）与 ${}^{L}\mathfrak{h}$ 的元素（10.1.3 中的 $B\chi$）：$B:\mathfrak{h}\to\mathfrak{h}^*$ 用内积 (18) 把泛函识别为元素。写 (394) 时若把 $B\chi$ 直接换成 $\chi$，形式上只差一个内积，实际上把“权”与“权的对偶”混为一谈，10.1.6 中 $\varphi(c)$ 的 $h$ 系数就会差一个内积因子。

### 含糊点拨：为什么要整个 ℂ[h]-族

直接在 $h=0$ 处计算 $a\delta$ 会遇到 10.1.4 指出的困难：$\lambda^h$-扭 $\mathcal{D}$-模只对离散的 $h$ 存在，不能把 $I_\chi$ 连续形变。10.1.5 的办法是把问题放进平坦 $\mathbb{C}[h]$-族：$h=0$ 的纤维与 $I_\chi$ 对接，一般纤维 $M$ 承载 Verma 特征标 $\varphi$，从而用 $\varphi(c)$ 的 $h$-展开控制 $c$ 的作用。这样 (394) 就被化归为 (397) 在 $h=0$ 处的同余。

### 背景直觉：δ 函数为何是最低权

$\mathfrak{d}_{\mathcal{L},\chi}$ 由 $\operatorname{Orb}_\chi$ 上的 $\delta$ 型截面张成，是 $L_0$ 的最低特征空间（8.1.5 的结论）。把它放到 $U_\chi$ 上做形变，相当于用 Verma 模的权来“看见”Hecke 特征值 $\chi$：$\delta$ 在 $G(O)$-不变截面的底部，任何 $\mathfrak{g}\otimes\mathfrak{m}$ 的作用都把它杀掉，于是只剩 Cartan 部分按 $\chi$ 作用。这也解释了为什么 (ii) 的右端是一个纯量 $\chi(a)$，而不是某个算子。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §10.1；印刷页 [375, 376, 377, 378, 379, 380] / PDF 页 [375, 376, 377, 378, 379, 380]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch10.tex:16-142`
- 页码为原书印刷页，PDF 页 = 印刷页（偏移 0）。§10.1 见 p.375–380（\SourcePage{375} 在第 9 行、{376} 在第 38 行、{377} 在第 64 行、{378} 在第 80 行、{379} 在第 96 行、{380} 在第 115 行）。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
