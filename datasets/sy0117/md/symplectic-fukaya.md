# 辛形式与 Fukaya 范畴

- **id**：`sy0117/concept/symplectic-fukaya`
- **类型**：concept
- **章**：第5章
- **问题**：Fukaya 范畴的 A∞ 结构从哪里来，为什么不能只用 Floer 上同调？

> 辛形式给流形配上非退化闭 2-形式，Lagrangian 子流形是其半数维的迷向子流形；Fukaya 范畴以它们为对象、Floer 复形为 Hom。

## 定义

辛流形 $(M,\omega)$ 带非退化闭 2-形式 $\omega$。Lagrangian 子流形 $L$ 满足 $\dim L=\frac12\dim M$ 且 $\omega|_L=0$。Fukaya 范畴的对象是 Lagrangian 子流形（带额外结构），Hom 是 Floer 复形 $CF^\bullet(L_0,L_1)$，高阶乘积由模空间计数给出。

**记号**：Kähler 情形 $\omega=i g_{i\bar j}dz^i\wedge d\bar z^j$；Floer 微分计数刚性伪全纯盘。

## 关键点

- $\omega$ 闭（$d\omega=0$）保证 Lagrangian 条件在 Hamiltonian 流下保持。
- Floer 复形的微分满足 $d^2=0$ 依赖模空间的紧化与取向。
- 高阶乘积 $\mu_n$ 使 Fukaya 范畴成为 A∞ 范畴，而不是普通范畴。

## 公式

```latex
\omega=i g_{i\bar j}dz^i\wedge d\bar z^j
```
```latex
d\omega=0
```
```latex
\omega|_L=0
```
```latex
\dim_{\mathbb R}L=\tfrac12\dim_{\mathbb R}M
```

## 常见错误

- 把辛形式写成 $g_{i\bar j}dx^i\wedge dx^{\bar j}$，漏掉因子 $i$ 与复坐标；这会把 Kähler 形式的实部/虚部弄反。
- 把 Lagrangian 当成任意子流形；$\omega|_L=0$ 是核心条件。

## 批注

### 易错预警：复坐标与因子 i

Kähler 形式在复坐标下是 $\omega=i g_{i\bar j}dz^i\wedge d\bar z^j$；写成 $dx\wedge dx$ 会漏掉 $i$，也会把实维数算错。

### 背景直觉：为什么用 A∞

Floer 同调只记住 $\mu_1$ 的上同调；盘计数还给出 $\mu_2,\mu_3,\ldots$，它们编码结合律的同伦修正。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §5.3；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch05.tex:261-406`
- 原书页码从略：本机无英文原书与页面图像，只以中译本节号与源码行号定位。

---

权利：`rewritten`；核验：`source-only`。
