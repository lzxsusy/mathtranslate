# Lefschetz 纤维化与消失圈

- **id**：`sy0117/concept/lefschetz-fibration`
- **类型**：concept
- **章**：第6章
- **问题**：为什么 Lefschetz 纤维化的临界点能给出 Fukaya 范畴的生成元？

> Lefschetz 纤维化把流形映到曲线，临界点附近是二次模型；消失圈生成 Fukaya–Seidel 范畴。

## 定义

Lefschetz 纤维化 $\pi\colon X\to\Sigma$ 在临界点附近同构于 $z_1^2+\cdots+z_n^2$；绕过临界值一圈，纤维上的消失圈 $V_i$ 被单值化变换。Fukaya–Seidel 范畴以这些消失圈为对象，其 Hom 由 Floer 复形给出。

**记号**：$n$ 是纤维的复维数；临界点非退化，且每个临界值只对应一个临界点。

## 关键点

- 临界点附近的局部模型是二次函数，消失圈就是二次奇点的 Milnor 纤维。
- 单值化变换把消失圈按 Dehn 扭转作用在纤维上。
- Fukaya–Seidel 范畴的生成元是消失圈，而不是整个纤维。

## 公式

```latex
W=\sum_{i=1}^n z_i^2
```
```latex
\pi\colon X\to\Sigma
```
```latex
V_i\subset\pi^{-1}(p)
```

## 常见错误

- 把 Lefschetz 纤维化的纤维维数算错；$n$ 是复维数，实维数是 $2n$。
- 忽略消失圈在单值化下的变化，把它们当成固定子流形。

## 批注

### 易错预警：临界值不是正则值

在临界值处纤维退化，不能把整条纤维当光滑 Lagrangian；要用消失圈。

### 背景直觉：Morse 理论的复几何版

Morse 函数用临界点生成链群；Lefschetz 纤维化用消失圈生成 Fukaya 范畴，二者都是“临界点给出生成元”。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §6.2；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch06.tex:299-708`
- 原书页码从略：本机无英文原书与页面图像，只以中译本节号与源码行号定位。

---

权利：`rewritten`；核验：`source-only`。
