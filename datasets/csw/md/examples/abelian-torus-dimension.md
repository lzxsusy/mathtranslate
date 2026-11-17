---
id: csw/example/abelian-torus-dimension
type: example
track: C
---

# U(1) 在环面上的 Hilbert 空间维数 = k

> $U(1)_k$ 在 $T^2$ 上的态空间维数为 $k$；一般亏格 $g$ 为 $k^g$。

**问题**：$U(1)$ 情形下预量子化线丛的全纯截面为什么正好 $k$ 个？

## 设定

取 $G=U(1)$、$\Sigma=T^2=\mathbb{C}/(\mathbb{Z}+\tau\mathbb{Z})$。平坦 $U(1)$ 联络模空间是 $T^2$ 的对偶环面（复维 1），Kähler 形式为 $\omega=\frac{k}{2\operatorname{Im}\tau}dz\wedge d\bar z$ 类。

## 计算

1. 把联络写成 $A=\frac{\pi}{\operatorname{Im}\tau}(\bar z\,dz-z\,d\bar z)$ 的平移；模空间坐标 $(a,\bar a)\in T^2\times T^2$。 *（阿贝尔情形模空间就是平坦联络本身模去大规范变换。）*
2. 预量子化线丛 $\mathcal{L}^{\otimes k}$ 的全纯截面是 theta 函数 $\vartheta_j(z)=\sum_{m\in\mathbb{Z}}e^{\pi ik(m+j/k)^2\tau+2\pi ik(m+j/k)z}$，$j=0,\dots,k-1$。 *（全纯性与准周期性决定 theta 级数。）*
3. 这 $k$ 个 theta 函数线性无关（不同 $j$ 的领头指数不同），故 $\dim H^0=k$。 *（线性无关性由 $q$-展开的领头项决定。）*

## 结果

$\dim\mathcal{H}(T^2)=k$；亏格 $g$ 时为 $k^g$（每个把手贡献一个 $k$ 维因子）。

## 核对

取 $k=1$：$\dim=1$（只有常数截面）；取 $k=2$：$\vartheta_0,\vartheta_1$ 两个，$\dim=2$。与半形式修正后的 $k$ 无关（阿贝尔情形 $h^\vee=0$，无平移）。

## 陷阱

- 不要把这个 $k$ 与半形式的 $k+h^\vee$ 混淆：$U(1)$ 的 $h^\vee=0$。
- theta 函数的周期性与 $k$ 绑定：换 $k$ 要换 theta 级数。

## 相关卡片

- [holomorphic-sections](../concepts/holomorphic-sections.md)
- [su2-torus-theta](../examples/su2-torus-theta.md)
- [prequantization-determinant-line](../concepts/prequantization-determinant-line.md)

## 来源

- 威腾 1989，Commun. Math. Phys. 121 (1989) 351–399，§3.1 与 §4.3（U(1) 例，p.368、p.385），印刷页 [368, 385] / PDF 页 [18, 35]（witten1989/sections/s04-canonical.tex（§3.1））

---
*本卡为改写（rewritten），不含原文复制；引用请核对原始文献。*
