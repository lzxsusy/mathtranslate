# 列维型子群 $\mathbb L$ 与 $\mathbb L$ 型面算符

- **id**：`gw06/concept/levi-surface-operator`
- **类型**：concept
- **位置**：§2.6
- **问题**：$\mathbb L$ 型面算符与“参数 $\mathbb L$-不变的普通面算符”到底差在哪里？

> $\mathbb L$ 型面算符要求参数 $\mathbb L$-不变，并在路径积分中只对 $D$ 上取值于 $\mathbb L$ 的规范变换求商，$\eta$ 是其阿贝尔部分的 $\theta$ 角。

## 定义

把极大环面 $\TT$ 换成 $G$ 的、含 $\TT$ 且可刻画为某个 $\alpha\in\mathfrak t$ 的中心化子的子群 $\mathbb L$，得到列维型子群（$\TT$ 本身是极小列维子群，$\mathbb L=G$ 是极大情形）。所谓 $\mathbb L$ 型面算符，是指支撑 $D$ 上的奇点仍由 $(\alpha,\beta,\gamma)$ 标记，但要求这三个参数在 $\mathbb L$ 下不变；并且在量子路径积分中，被除掉的规范变换是那些限制到 $D$ 上取值于 $\mathbb L$ 的变换，而不只是取值于 $\TT$ 的变换。正因为最后这一步，$\mathbb L$ 型算符不是普通面算符在参数 $\mathbb L$-不变时的特例，而是不同的路径积分。量子层面还有参数 $\eta$：此时 $\TT$ 被 $\mathbb L$ 取代，$\eta$ 取值于相应子群，定义为 $\mathbb L$ 的阿贝尔部分的 $\theta$ 角。

**记号**：$\mathbb L$：列维型子群；$\mathcal W_\mathbb L$：$\mathbb L$ 与 ${}^L\neg\mathbb L$ 共有的外尔群；${\mathcal W}_\mathbb L$-不变部分：$\TT\times\mathfrak t\times\mathfrak t\times{}^L\neg\TT$ 中的不变子集；$\EUP$：抛物子群；$\EUN$：幂幺根。

## 关键点

- $\mathbb L\subset G$ 含 $\TT$，且可刻画为与某个 $\alpha\in\mathfrak t$ 交换的元素组成的子群；$\TT$ 是极小列维子群，$\alpha=0$ 给 $\mathbb L=G$。
- $\mathbb L$ 型面算符与 $\TT$ 型算符不是特例关系：它的路径积分在 $D$ 上只对取值于 $\mathbb L$ 的规范变换求商，因此是不同的路径积分。
- $(\alpha,\beta,\gamma)$ 的 $\mathbb L$-不变性等价于 ${\mathcal W}_\mathbb L$-不变性，因为 $\mathbb L$ 与 ${}^L\neg\mathbb L$ 的外尔群相同；用后者表述可把 $\eta$ 与其余变量同等对待。
- $\eta$ 是 $\mathbb L$ 阿贝尔部分的 $\theta$ 角，要求它 ${\mathcal W}_\mathbb L$-不变，意味着它是 $D$ 上结构群为 $\mathbb L$ 的丛的阿贝尔磁通量的特征。
- 对偶猜想：$\mathbb L$ 型面算符映为 ${}^L\neg\mathbb L$ 型，参数按 $(\alpha,\beta,\gamma,\eta)\to(\eta,\beta,\gamma,-\alpha)$ 变换。

## 公式

```latex
\left(\begin{matrix}* & * & 0 \\ * & * & 0 \\ 0 & 0 & * \end{matrix}\right)
```
```latex
[\alpha,\psi]=i\lambda\psi, ~\lambda\geq 0
```
```latex
(\alpha,\beta,\gamma,\eta)\to(\eta,\beta,\gamma,-\alpha)
```

## 定理

**$\mathbb L$ 与 ${}^L\neg\mathbb L$ 有相同的外尔群**：列维子群 $\mathbb L\subset G$ 与 ${}^L\neg\mathbb L\subset{}^L\neg G$ 之间存在自然对应，其刻画方式是两者的外尔群相同，记作 ${\mathcal W}_\mathbb L$。

证明：sketch（）

1. $G$ 的外尔群 $\mathcal W$ 与 ${}^L\neg G$ 的外尔群 ${}^L\neg\mathcal W$ 自然等同（附录 A）。 —— 这是朗兰兹对偶群的标准性质：根系与余根系互换而外尔群不变。
2. $\mathbb L$ 与 ${}^L\neg\mathbb L$ 的外尔群分别是 $\mathcal W$ 与 ${}^L\neg\mathcal W$ 的子群。 —— 列维子群的外尔群由它所保留的单根生成。
3. 二者的外尔群相同，故可用 ${\mathcal W}_\mathbb L$ 统一刻画不变参数。 —— 等价说法是 ${}^L\neg\mathbb L$ 的余根是 $\mathbb L$ 的余根的倍数（长、短根倍数不同）。

缺口：对应的存在性依赖根数据的标准事实，细节见附录 A。

## 常见错误

- 把 $\mathbb L$ 型算符当成 $\mathbb L$-不变的普通面算符：忽略了在 $D$ 上只对 $\mathbb L$-值规范变换求商，会漏掉新的路径积分；对这类特殊参数，普通 $\TT$ 型算符反而会变奇异。
- 把 $\eta$ 当成仍取值于 ${}^L\neg\TT$：$\mathbb L\neq\TT$ 时它只是 $\mathbb L$ 阿贝尔部分的 $\theta$ 角，即 ${\mathcal W}_\mathbb L$-不变的那部分。
- 以为 $\mathbb L$ 决定唯一的抛物子群：非极小 $\mathbb L$ 可联系若干不等价的 $\EUP$，取向由 $\alpha$ 的符号另行选定。

## 批注

### 易错预警：$\mathbb L$ 不变不等于 ${\mathcal W}_\mathbb L$ 不变？

二者等价，但方向容易记反：$\mathbb L$-不变性是对 $(\alpha,\beta,\gamma)$ 在群 $\mathbb L$ 下不变，而 ${\mathcal W}_\mathbb L$-不变性是对外尔群不变；后者更强地要求把 $\eta$ 也纳入同一套变量，正因如此才能写出一致的四元对偶公式。

### 含糊点拨：为什么 $\eta$ 必须 ${\mathcal W}_\mathbb L$-不变

限制在 $D$ 上的丛结构群是 $\mathbb L$，其阿贝尔磁通量（特征类）在 ${\mathcal W}_\mathbb L$ 下不变；$\eta$ 作为该磁通量的对偶变量，自然也须 ${\mathcal W}_\mathbb L$-不变。若漏掉这一点，就会允许 $\eta$ 取到 $\mathbb L$ 不保持的方向，得到不存在的算符。

### 背景直觉：从环面到列维：分歧的层级

地面算符的“类型”由单值性所在的子群决定：$\TT$ 型是最细的（单值性在半环面里），$\mathbb L$ 型允许单值性落在更大的列维子群里；在几何朗兰兹一侧，这对应希格斯丛的抛物结构从博雷尔型放宽到列维型。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §2.6；印刷页 [27, 29] / PDF 页 [28, 30]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s02b-duality.tex:906-1020`
- 列维型子群、$\mathbb L$ 型面算符的定义与 $\eta$ 的取值、式 (2.55)(2.56)；印刷页 27–29，原文 PDF 第 28–30 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
