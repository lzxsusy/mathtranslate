# Bridgeland 稳定条件

- **id**：`sy0117/concept/stability-condition`
- **类型**：concept
- **章**：第11章
- **问题**：为什么稳定条件的心与中心荷必须满足支撑性质？

> Bridgeland 稳定条件由心、中心荷与切片公理组成；稳定对象对应中心荷相位，模空间因此获得复结构。

## 定义

稳定条件 $(Z,\mathcal A)$ 由 Abel 范畴的心 $\mathcal A\subset D^b(X)$ 与群同态 $Z\colon K_0(\mathcal A)\to\mathbb C$ 组成，并带 slicing $\{\mathcal P(\phi)\}_{\phi\in\mathbb R}$，满足支撑性质与相位单调性。

**记号**：$Z$ 是中心荷；稳定对象的相位是 $\phi(E)=\frac1\pi\arg Z(E)$。

## 关键点

- 心是 $t$-结构，决定哪些对象有“度数”。
- 中心荷的相位给出稳定对象的排序；Harder–Narasimhan 滤链由此定义。
- 稳定条件的模空间是复流形，局部同构于 $\operatorname{Hom}(K_0,\mathbb C)$。

## 公式

```latex
(Z,\mathcal A)
```
```latex
Z\colon K_0(\mathcal A)\to\mathbb C
```
```latex
\phi(E)=\tfrac1\pi\arg Z(E)
```

## 常见错误

- 把 Bridgeland 稳定条件当成 GIT 稳定性；前者是导出范畴的 $t$-结构数据。
- 忽略心 $\mathcal A$ 的选择；同一三角范畴可有不同稳定条件。

## 批注

### 易错预警：相位不是角度制

$\phi$ 以 $\pi$ 为单位；$\arg Z=\pi$ 对应 $\phi=1$，不要与 $2\pi$ 混用。

### 背景直觉：稳定条件像“复结构”

所有稳定条件构成复流形；每个点给出一个心与中心荷，类似给三角范畴选一组复坐标。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §11.3；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch11.tex:375-570`
- 原书页码从略；本卡锚定中译校定本（2026-11-21 第三轮校定）的节号与源码行号，正文已对照 CUP 2021 英文原书核验。

---

权利：`rewritten`；核验：`source-verified`。
