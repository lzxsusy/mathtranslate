# 函子与自然变换

- **id**：`sy0117/concept/functor-natural`
- **类型**：concept
- **章**：第1章
- **问题**：Yoneda 引理为什么说“对象由它收到的态射完全决定”？

> 函子保结构，自然变换比较函子；Yoneda 引理把对象 X 与可表函子 C(-,X) 绑定。

## 定义

函子 $F\colon\mathcal C\to\mathcal D$ 给每个对象 $X$ 一个 $FX$、每个态射 $f$ 一个 $Ff$，并保单位与复合。自然变换 $\eta\colon F\to G$ 给每个 $X$ 一个 $\eta_X\colon FX\to GX$，使 $\eta_Y\circ Ff=Gf\circ\eta_X$。Yoneda 引理给出 $\operatorname{Nat}(\mathcal C(-,X),F)\cong F(X)$。

**记号**：$\operatorname{Nat}(F,G)$ 记自然变换集；可表函子指 $\mathcal C(-,X)$ 或 $\mathcal C(X,-)$。

## 关键点

- Yoneda 嵌入 $X\mapsto\mathcal C(-,X)$ 一般是全忠实的，但是否本质满取决于范畴。
- 自然变换的方块交换图必须对每个态射成立，不能只对对象验证。
- 反变函子等价于相反范畴上的共变函子，右模就是这种情形。

## 公式

```latex
\eta_Y\circ Ff=Gf\circ\eta_X
```
```latex
\operatorname{Nat}(\mathcal C(-,X),F)\cong F(X)
```

## 常见错误

- 把自然变换写成“每个对象给一个同构”，却漏掉与态射的交换性。
- 把 $\mathcal C(-,X)$ 与 $\mathcal C(X,-)$ 的可表方向弄反。

## 批注

### 易错预警：可表方向

本章的 Yoneda 嵌入用 $X\mapsto\mathcal C(-,X)$；若写成 $\mathcal C(X,-)$，得到的是反变版本，复合方向随之反转。

### 含糊点拨：Yoneda 的证明

沿恒等态射 $1_X\in\mathcal C(X,X)$ 追踪像：自然变换由 $\eta_X(1_X)\in F(X)$ 完全决定，这就是逆映射。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §1.2–1.3；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch01.tex:44-217`
- 原书页码从略；本卡锚定中译校定本（2026-11-21 第三轮校定）的节号与源码行号，正文已对照 CUP 2021 英文原书核验。

---

权利：`rewritten`；核验：`source-verified`。
