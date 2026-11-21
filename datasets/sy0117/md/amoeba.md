# 阿米巴（amoeba）

- **id**：`sy0117/concept/amoeba`
- **类型**：concept
- **章**：第8章
- **问题**：为什么把超曲面取对数后得到的图形，能帮我们读出它的热带化？

> 复环面中超曲面在逐坐标对数映射下的像；它把复几何对象压成 $\mathbb R^n$ 里一只带腿的“变形虫”，其缩放极限就是热带超曲面。

## 定义

设 $V\subset(\mathbb C^*)^n$ 是超曲面，逐坐标对数映射为
$\operatorname{Log}(z_1,\dots,z_n)=(\log|z_1|,\dots,\log|z_n|)\in\mathbb R^n$。
集合 $A(V)=\operatorname{Log}(V)$ 称为 $V$ 的**阿米巴**（amoeba，希腊语“变形虫”）：它通常是一块带若干“腿”的厚实区域，补集由有限个凸区域拼成。令 $t\to\infty$，把 $A(V)$ 按 $1/\log t$ 缩放，其极限（按 Hausdorff 距离）就是 $V$ 的热带化 $\operatorname{Trop}(V)$。

**记号**：$\operatorname{Log}\colon(\mathbb C^*)^n\to\mathbb R^n$；$A(V)=\operatorname{Log}(V)$；$\operatorname{Trop}(V)=\lim_{t\to\infty}\frac1{\log t}\operatorname{Log}(V)$。

## 关键点

- 阿米巴只记录 $|z_i|$，丢掉全部辐角，因此是实 $n$ 维集合而非复对象。
- 补集的分量对应 Newton 多面体的面：这是 Forsberg–Passare–Tsikh 的定理。
- 缩放极限给出热带化，边的重数等于对应相交数；这正是“热带几何是阿米巴的骨架”的精确含义。

## 公式

```latex
A(V)=\{\operatorname{Log}(z):z\in V\}
```
```latex
\operatorname{Trop}(V)=\lim_{t\to\infty}\tfrac1{\log t}A(V)
```

## 常见错误

- 把 $\operatorname{Log}$ 当成复对数；这里的像落在 $\mathbb R^n$，没有“多值”问题。
- 把阿米巴当成代数簇来算维数：它是带边界的实集合，边界来自 $|z_i|\to0$ 或 $\infty$。

## 批注

### 易错预警：Log 不是全纯映射

$\operatorname{Log}$ 逐坐标取模再取对数，连续但非全纯；因此 $A(V)$ 的“边界”没有复解析意义，不能用除子理论直接算。

### 背景直觉：为什么叫变形虫

$n=2$ 时 $A(V)$ 是平面区域，中央一团、伸出若干条腿（tentacle），形似变形虫；腿的数目与 Newton 多边形的边数有关。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §8.2；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch08.tex:440-470`
- 原书页码从略；本卡锚定中译校定本（2026-11-21 第三轮校定）的节号与源码行号，正文已对照 CUP 2021 英文原书核验。

---

权利：`rewritten`；核验：`source-verified`。
