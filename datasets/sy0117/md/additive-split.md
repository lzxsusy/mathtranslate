# 加法完备化与分裂完备化

- **id**：`sy0117/concept/additive-split`
- **类型**：concept
- **章**：第1章
- **问题**：为什么分裂完备化的对象要写成 (X,e)，而不是直接写像？

> 加法完备化补上有限直和，分裂完备化把幂等元的像补成对象；两者合起来才便于比较模范畴。

## 定义

加法完备化 $\operatorname{Add}\mathcal C$ 的形式有限直和再取直和项；分裂完备化 $\operatorname{Split}\mathcal C$ 的对象是 $(X,e)$，其中 $e\colon X\to X$ 满足 $e^2=e$，态射为 $e'\mathcal C(X,X')e$。Karoubi 完备化就是分裂完备化。

**记号**：$e$ 是幂等元；$(X,e)$ 代表 $\operatorname{im}e$，但像在原来的范畴里未必存在，所以要把像正式补成对象。

## 关键点

- $\operatorname{Split}(\operatorname{Add}\mathcal C)$ 与 $\operatorname{Add}(\operatorname{Split}\mathcal C)$ 等价，但不是字面相等。
- 幂等元分裂后，$\operatorname{im}e$ 与 $\operatorname{im}(1-e)$ 互补。
- Morita 等价在加法/分裂完备化后更容易陈述。

## 公式

```latex
\operatorname{Split}\mathcal C
```
```latex
e^2=e
```
```latex
\operatorname{Hom}((X,e),(X',e'))=e'\mathcal C(X,X')e
```

## 常见错误

- 把 $\operatorname{SplitAdd}\mathcal C$ 的对象误写成 $X$；实际是 $(X,e)$。
- 忘记 $e'\circ f\circ e$ 的左右夹逼，导致复合不封闭。

## 批注

### 易错预警：对象是 (X,e)

只写 $X$ 会丢掉“取哪个直和项”的数据；不同幂等元给出同一 $X$ 的不同对象。

### 背景直觉：为什么先加后裂

先取有限直和，才有足够的直和项可裂；两种次序在等价意义下一致，但定义处要说明取哪一种。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §1.4–1.5；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch01.tex:218-329`
- 原书页码从略；本卡锚定中译校定本（2026-11-21 第三轮校定）的节号与源码行号，正文已对照 CUP 2021 英文原书核验。

---

权利：`rewritten`；核验：`source-verified`。
