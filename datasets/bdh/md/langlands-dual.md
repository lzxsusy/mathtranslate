# 朗兰兹对偶 $^{L}G$ 与 $^{L}\mathfrak{g}$

- **id**：`bdh/concept/langlands-dual`
- **类型**：concept
- **位置**：§0
- **问题**：$^{L}G$ 到底由 $G$ 的哪些数据决定，为什么 Hecke 算子的特征值要用 $^{L}G$ 的支配权来标号？

> 把 $G$ 的根 datum 对偶过来得到 $^{L}G$；$\mathfrak{z}$ 的谱是 $^{L}\mathfrak{g}$-oper 的模空间，而 Hecke 特征层的特征值取 $^{L}G$ 的支配权，对偶贯穿全书。

## 定义

设 $G$ 是连通约化群，$T\subset B\subset G$ 是极大环面与 Borel，$(X^*(T),\Delta,X_*(T),\Delta^\vee)$ 是其根 datum。朗兰兹对偶群 $^{L}G$ 是这样一个连通约化群：其极大环面 $^{L}T$ 满足 $X^*(^{L}T)=X_*(T)$、$X_*(^{L}T)=X^*(T)$，且其根 datum 是原来那个的对偶（根与余根互换）。于是 $G$ 的支配权恰好是 $^{L}G$ 的支配余权，反之亦然。$^{L}\mathfrak{g}=\operatorname{Lie}{}^{L}G$。在本书中，$\mathfrak{z}$ 的谱典范等同于 $^{L}\mathfrak{g}$-oper 的模空间（0.2(b)），而 Hecke 算子的标号用 $P_+({}^{L}G)$，即 $^{L}G$ 的支配权。

**记号**：$^{L}G$：$G$ 的朗兰兹对偶群；$^{L}\mathfrak{g}$：其李代数；$(^{L}G)_{ad}$：其伴随群、$P_+({}^{L}G)$：$^{L}G$ 的支配权集，Hecke 算子按它标号、$^{L}T$：对偶环面，$X^*(^{L}T)=X_*(T)$

## 关键点

- 对偶只交换根与余根（环面的特征标与余特征标互换），不改变群的整体结构；$^{L}G$ 与 $G$ 一般不同构。
- $\mathfrak{z}$ 的谱是 $^{L}\mathfrak{g}$-oper 的模空间（0.2(b)），不是 $\mathfrak{g}$-oper 的；把对偶方向搞反是本章最常见的错误。
- Hecke 算子用 $P_+({}^{L}G)$ 标号：态射 $\nu:\mathbb{G}_m\to G$ 的共轭类典范等同于 $^{L}G$ 的支配权（见 5.2.3）。
- $G$ 单连通时 $^{L}G$-oper 与 $^{L}\mathfrak{g}$-oper 一致；一般情形二者的差别正是 $\lambda_{\mathfrak{F}}$ 出现的根源。

## 公式

```latex
X^{*}({}^{L}T)=X_{*}(T),\qquad X_{*}({}^{L}T)=X^{*}(T)
```
```latex
P_{+}({}^{L}G)\cong\{\nu:\mathbb{G}_{m}\to G\}/\text{共轭}
```

## 常见错误

- 把 $^{L}G$ 当成 $G$ 的复共轭或对偶向量空间：它是根 datum 的对偶，$\mathrm{SL}_n$ 的对偶是 $\mathrm{PGL}_n$，两者的李代数相同但群不同。
- 把 Hecke 算子的标号写成 $P_+(G)$：标号用的是对偶群的支配权，写反后 5.2.3 的等同就不成立。
- 在 $G$ 不单连通时仍断言「$^{L}G$-oper 与 $^{L}\mathfrak{g}$-oper 相同」：这正是 0.2(d) 要引入 $\lambda_{\mathfrak{F}}$ 的情形。

## 批注

### 背景直觉：为什么几何朗兰兹一定出现对偶群

几何朗兰兹的粗略陈述是「$X$ 上 $^{L}G$-局部系统的模空间」与「$\operatorname{Bun}_G$ 上 $\mathcal{D}$-模的某个子范畴」之间的对应。两侧分别由 $^{L}G$ 与 $G$ 控制：特征值（oper 的纤维）取 $^{L}G$ 的表示，而 Hecke 算子作用在 $G$-丛的模栈上。这种「一侧的群、另一侧的对偶群」正是朗兰兹对偶的几何体现；若把两侧的群都写成 $G$，整个对应会退化成自对偶的平凡陈述。

### 易错预警：$\mathfrak{z}^{cl}$ 的谱与 $^{L}\mathfrak{g}$-oper

0.2(b) 说「$\mathfrak{z}$ 的谱与 $^{L}\mathfrak{g}$-oper 的模空间有典范等同」，注意是 $^{L}\mathfrak{g}$ 而不是 $\mathfrak{g}$。这个对偶来自 Hitchin 纤维化的靶空间：$\operatorname{Bun}_G$ 的 Hitchin 纤维化靶空间由 $\mathfrak{g}$ 的不变量多项式描述，而对偶群的不变量多项式恰好给出 $^{L}\mathfrak{g}$-oper 的系数。把 $^{L}$ 漏掉，会把 oper 模空间写成 $\mathfrak{g}$-oper 的模空间，从而与 5.2.6 的主定理冲突。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §0.2(b)；印刷页 [4] / PDF 页 [4]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch00.tex:11-11`
- 原书 p.4；本书 PDF 页 = 印刷页。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §5.2.3；印刷页 [195] / PDF 页 [195]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch05.tex:38-40`
- 共轭类与支配权的等同；页码按原书页眉。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
