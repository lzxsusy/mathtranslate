# 范畴与函子

- **id**：`sy0117/concept/category`
- **类型**：concept
- **章**：第1章
- **问题**：为什么范畴论先比较态射而不是比较对象？

> 把对象、态射、复合与单位公理化，用函子与自然变换比较不同数学结构。

## 定义

范畴 $\mathcal C$ 由对象类 $\operatorname{Ob}\mathcal C$、每对对象 $X,Y$ 的 Hom 集 $\mathcal C(X,Y)$、复合 $\circ$ 与单位 $1_X$ 组成；复合结合，单位左吸收与右吸收。函子同时给对象与态射，并保复合与单位；自然变换给两个函子之间的态射族。

**记号**：$\mathcal C(X,Y)$ 也记 $\operatorname{Hom}_{\mathcal C}(X,Y)$；小范畴要求对象类与所有 Hom 集都是集合。

## 关键点

- 态射携带的对象间关系比对象本身更多；只比较对象会丢掉复合信息。
- 相反范畴 $\mathcal C^{\mathrm{op}}$ 反转复合次序，Hom 集不变。
- 范畴等价只需函子与自然同构，不要求对象一一对应。

## 公式

```latex
\mathcal C(X,Y)
```
```latex
1_Y\circ f=f=f\circ 1_X
```
```latex
F(g\circ f)=F(g)\circ F(f)
```

## 常见错误

- 把“对象同构”当成“对象相等”；或在验算函子时漏掉单位。
- 把 $\mathcal C^{\mathrm{op}}$ 的复合方向与 Hom 集方向同时反掉。

## 批注

### 易错预警：Hom 的方向

$\mathcal C^{\mathrm{op}}(X,Y)=\mathcal C(Y,X)$，但复合写成 $f\circ^{\mathrm{op}}g=g\circ f$；只反 Hom 不反复合，会把相反范畴算成原范畴。

### 背景直觉：自然变换才是“自然”

书里反复说“这个同构是自然的”，意思是对所有对象同时给出且与态射相容；单个人工同构不构成自然变换。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §1.1–1.3；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch01.tex:4-217`
- 原书页码从略；本卡锚定中译校定本（2026-11-21 第三轮校定）的节号与源码行号，正文已对照 CUP 2021 英文原书核验。

---

权利：`rewritten`；核验：`source-verified`。
