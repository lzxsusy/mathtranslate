# 良栈与极良栈（good / very good stacks）

- **id**：`bdh/concept/good-very-good-stacks`
- **类型**：concept
- **位置**：§1.1
- **问题**：余切栈的维数为什么可能超过 $2\dim\mathcal{Y}$，而「良」「极良」这两个条件各自排除了什么？

> 光滑等维代数栈的余切栈总满足 $\dim T^{*}\mathcal{Y}\ge 2\dim\mathcal{Y}$；等号定义良栈，把逐层的余维条件加强为严格不等定义极良栈，后者等价于 $T^{*}\mathcal{Y}^{0}$ 稠密。

## 定义

设 $\mathcal{Y}$ 是 $\mathbb{C}$ 上光滑的等维代数栈，$\Theta_{\mathcal{Y}}$ 为其切层；余切栈 $T^{*}\mathcal{Y}=\operatorname{Spec}\operatorname{Sym}\Theta_{\mathcal{Y}}$ 未必光滑，$\dim T^{*}\mathcal{Y}=2\dim\mathcal{Y}$ 也一般不成立（例如无限代数群的分类栈，或 $\mathfrak{sl}_n$ 模去 $\mathrm{SL}_n$ 的伴随作用所得的商）。但式 (1) 总成立。若式 (2) 成立，即 $\dim T^{*}\mathcal{Y}=2\dim\mathcal{Y}$，则称 $\mathcal{Y}$ 为良（good）；此时 $T^{*}\mathcal{Y}$ 局部是纯维数 $2\dim\mathcal{Y}$ 的完全交。良等价于逐层的余维条件 (3)：对一切 $n>0$，自同构群维数为 $n$ 的点集余维至少 $n$。把 (3) 的 $\ge$ 换成 $>$（式 (4)）则称 $\mathcal{Y}$ 为极良（very good）。极良当且仅当 $T^{*}\mathcal{Y}^{0}$ 在 $T^{*}\mathcal{Y}$ 中稠密，其中 $\mathcal{Y}^{0}:=\{y\in\mathcal{Y}\mid \dim G_y=0\}$ 是 $\mathcal{Y}$ 的最大 Deligne--Mumford 子栈。

**记号**：$\mathcal{Y}$：$\mathbb{C}$ 上光滑的等维代数栈、$\Theta_{\mathcal{Y}}$：切层；$T^{*}\mathcal{Y}=\operatorname{Spec}\operatorname{Sym}\Theta_{\mathcal{Y}}$：余切栈、$G_y$：点 $y$ 的自同构群；$\mathcal{Y}^{0}$：$\dim G_y=0$ 的点构成的子栈

## 关键点

- 式 (1) 对一切光滑等维代数栈成立，等号却未必：p.6 给出两个反例——无限代数群的分类栈，以及 $\mathfrak{sl}_n$ 模去 $\mathrm{SL}_n$ 的伴随作用所得的商。
- 良的定义是式 (2) 的等式 $\dim T^{*}\mathcal{Y}=2\dim\mathcal{Y}$；此时 $T^{*}\mathcal{Y}$ 局部是纯维数 $2\dim\mathcal{Y}$ 的完全交（ch01.tex:18）。
- 式 (2) 与式 (3) 等价：$\operatorname{codim}\{y\in\mathcal{Y}\mid \dim G_y=n\}\ge n$ 对一切 $n>0$。这把整体维数条件换成了可以逐层检验的余维条件（ch01.tex:20-23）。
- 极良是把 (3) 的 $\ge$ 换成严格不等 $>$（式 (4)）；故极良强于良（ch01.tex:24-28）。
- 极良当且仅当 $T^{*}\mathcal{Y}^{0}$ 在 $T^{*}\mathcal{Y}$ 中稠密；特别地，$\mathcal{Y}$ 的每个连通分支 $\mathcal{Y}_i$ 的 $T^{*}\mathcal{Y}_i$ 不可约（ch01.tex:30-34）。
- 若 $\mathcal{Y}=K\backslash S$（$S$ 光滑、$K$ 作用），则 $T^{*}\mathcal{Y}$ 由 $T^{*}S$ 经哈密顿约化得到（见 1.2.1），这也是 1.1.1 想说的「一般情形与此十分相似」（ch01.tex:18）。
- 命名是玩笑：「良」实为「good for lazybones」（对懒人友好），见 1.1.4 末的注与 p.6 的译注（ch01.tex:36-37）。

## 公式

```latex
\dim T^{*}\mathcal{Y}\ge 2\dim\mathcal{Y}
```
```latex
\dim T^{*}\mathcal{Y}=2\dim\mathcal{Y}
```
```latex
\operatorname{codim}\{y\in\mathcal{Y}\mid \dim G_y=n\}\ge n\qquad\text{对一切 }n>0.
```
```latex
\operatorname{codim}\{y\in\mathcal{Y}\mid \dim G_y=n\}>n\qquad\text{对一切 }n>0.
```
```latex
\mathcal{Y}^{0}:=\{y\in\mathcal{Y}\mid \dim G_y=0\}
```

## 常见错误

- 把「极良」只当成「良加光滑」：极良给的是 $T^{*}\mathcal{Y}^{0}$ 稠密与辛结构可用，$T^{*}\mathcal{Y}$ 本身一般仍然奇异；良只保证维数对、局部是完全交。
- 把式 (4) 写成 $\ge$：极良的关键就是处处严格大于，差一个等号恰好是「良但非极良」的边界情形，此时 $T^{*}\mathcal{Y}^{0}$ 不再稠密，2.2.4 注中那套辛几何论证会失效。
- 把条件 (3) 只验 $n=1$：条件要求对一切 $n>0$ 成立，只验最低一层会漏掉高维自同构群构成的层。
- 把「良」译成「好栈」或当成普通形容词：原文是作者的自嘲「good for lazybones」，术语表定为「良栈 / 极良栈」，首现处须按译注保留原文字面以便对照（ch01.tex:36-37）。

## 批注

### 背景直觉：为什么维数会「多出来」

把 $T^{*}\mathcal{Y}$ 想成「点加余切向量」：对 $\mathcal{Y}=K\backslash S$，它等于 $K\backslash\mu^{-1}(0)$，而自同构群变大的层会让 $\mu^{-1}(0)$ 比 $2\dim\mathcal{Y}$ 应有的更大。$\mathfrak{sl}_n$ 模去 $\mathrm{SL}_n$ 的伴随商就是这种情形：$T^{*}$ 的维数与 $2\dim$ 对不上。式 (3) 的余维条件正是在逐层堵住这种超额，所以它能与整体的等式 (2) 等价。

### 含糊点拨：极良到底比良多给了什么

良只保证 $T^{*}\mathcal{Y}$ 的维数与局部完全交性；要用辛几何（例如把 Hitchin 纤维化说成 Lagrange 纤维化），需要 $T^{*}\mathcal{Y}$ 有一个开稠密的辛 DM 子栈，这正是极良提供的 $T^{*}\mathcal{Y}^{0}$。于是 2.1.2 要证 $\operatorname{Bun}_G$ 极良、2.10.1 只证它良，两处强度不同，不能互相代替。

### 易错预警：别把 $\mathcal{Y}^{0}$ 与 $\mathcal{Y}$ 的光滑点集混同

$\mathcal{Y}^{0}$ 由自同构群维数为零的点组成，是最大 Deligne--Mumford 子栈；它不是 $\mathcal{Y}$ 的光滑点集（$\mathcal{Y}$ 作为光滑栈本来处处光滑），也不是去掉奇点后的开集。极良的等价说法是 $T^{*}\mathcal{Y}^{0}$ 在 $T^{*}\mathcal{Y}$ 中稠密，而不是 $\mathcal{Y}^{0}$ 在 $\mathcal{Y}$ 中稠密——后者对一般的栈根本不成立。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §1.1.1；印刷页 [6] / PDF 页 [6]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch01.tex:10-37`
- 1.1.1 整节在印刷页 6：`\SourcePage{6}` 在 ch01.tex:4，下一处 `\SourcePage{7}` 在 ch01.tex:39，故式 (1)–(4)、$\mathcal{Y}^{0}$ 的定义与末段玩笑注都在 p.6（PDF 页 6）。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
