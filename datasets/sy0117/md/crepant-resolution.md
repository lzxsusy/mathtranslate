# crepant 消解

- **id**：`sy0117/concept/crepant-resolution`
- **类型**：concept
- **章**：第8章
- **问题**：为什么三维 Gorenstein 奇点总能找到 crepant 消解，而高维不一定？

> 保持典范类的奇点消解：$K_{\widetilde X}=\pi^*K_X$，即消解不改变“扭曲程度”。

## 定义

设 $\pi\colon\widetilde X\to X$ 是奇点消解。若 $K_{\widetilde X}=\pi^*K_X$（等价地，例外除子的典范类贡献为零），则称 $\pi$ 为 **crepant 消解**。它是最“经济”的消解：不引入额外的典范类扭曲。三维 Gorenstein 奇点必有 crepant 消解（Bridgeland–King–Reid，用 $G$-Hilbert 概形给出）；四维及以上可以不存在。

**记号**：$K_{\widetilde X}=\pi^*K_X$；例外除子 $E_i$ 满足 $\sum a_iE_i$ 中 $a_i=0$。

## 关键点

- crepant 是法语词，意为“响亮、干脆”；数学上取“不引入额外典范类”之意，中文文献多保留英文。
- $\mathbb A^3/\mathbb Z_5$ 的 crepant 消解给出五次 Calabi–Yau 的镜像构造。
- crepant 消解在派生等价下与矩阵分解、LG 模型相连（BKR 猜想/定理）。

## 公式

```latex
\pi\colon\widetilde X\to X,\quad K_{\widetilde X}=\pi^*K_X
```

## 常见错误

- 把“crepant”当成“任意消解”：普通的奇点消解一般会改变典范类。
- 在维数 $\ge4$ 时默认存在性；这是三维 Gorenstein 的特权。

## 批注

### 易错预警：crepant ≠ 极小

极小消解要求例外除子没有负的自相交，crepant 要求典范类不变；两者在三维 Gorenstein 情形常同时成立，但不是同一定义。

### 背景直觉：为什么镜像对称需要它

B 侧的矩阵分解与 A 侧的消失圈只有在 crepant 消解上才匹配；非 crepant 消解会多出不属于 LG 模型的例外除子。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §8.3；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch08.tex:570-600`
- 原书页码从略；本卡锚定中译校定本（2026-11-21 第三轮校定）的节号与源码行号，正文已对照 CUP 2021 英文原书核验。

---

权利：`rewritten`；核验：`source-verified`。
