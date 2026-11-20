# Morita 等价

- **id**：`sy0117/concept/morita`
- **类型**：concept
- **章**：第1章
- **问题**：Morita 等价为什么不要求两个环同构？

> 两个环的模范畴等价，就称它们 Morita 等价；等价由一对互为逆的双模给出。

## 定义

环 $A,B$ 的 Morita 等价由 $(A,B)$-双模 $M$ 与 $(B,A)$-双模 $N$ 给出，并有 $M\otimes_B N\cong A$、$N\otimes_A M\cong B$，从而 $\mathrm{Mod}\text{-}A\simeq\mathrm{Mod}\text{-}B$。

**记号**：$M$ 同时是左 $A$-模与右 $B$-模，且两种作用相容；$N$ 的方向相反。

## 关键点

- Morita 等价保持模范畴的加法、Abel、导出结构，但不保持环同构。
- 矩阵环 $M_n(A)$ 与 $A$ Morita 等价。
- 等价双模的复合要与单位同构相容，不能只给对象级同构。

## 公式

```latex
M\otimes_B N\cong A
```
```latex
N\otimes_A M\cong B
```
```latex
\mathrm{Mod}\text{-}A\simeq\mathrm{Mod}\text{-}B
```

## 常见错误

- 把 Morita 等价当成环同构，进而误以为中心相同。
- 只给 $M$ 不给 $N$，或忘记双模作用的相容性。

## 批注

### 含糊点拨：双模的左右作用

$M$ 的 $A$-左作用与 $B$-右作用必须满足 $(a m)b=a(mb)$；否则张量积不结合。

### 背景直觉：表示论的“相同”

Morita 等价把“同一个环的不同矩阵实现”视为同一表示论；这正是后来导出等价的原型。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §1.6；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch01.tex:330-481`
- 原书页码从略：本机无英文原书与页面图像，只以中译本节号与源码行号定位。

---

权利：`rewritten`；核验：`source-only`。
