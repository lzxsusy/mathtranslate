# Ext 群与扩张

- **id**：`sy0117/concept/ext`
- **类型**：concept
- **章**：第2章
- **问题**：Ext 为什么不依赖投射分解的选取？

> Ext 群用投射分解计算 Hom 的同调，分类扩张；Yoneda 积使其成为分次环。

## 定义

取 $M$ 的投射分解 $P_\bullet\to M$，定义 $\operatorname{Ext}^n_A(M,N):=H^n(\operatorname{Hom}_A(P_\bullet,N))$。比较定理保证不同投射分解给出典范同构；$\operatorname{Ext}^1$ 分类短正合列 $0\to N\to E\to M\to0$。

**记号**：$\operatorname{Ext}^0_A(M,N)=\operatorname{Hom}_A(M,N)$；Yoneda 积把 $\operatorname{Ext}^p(M,N)\otimes\operatorname{Ext}^q(N,L)\to\operatorname{Ext}^{p+q}(M,L)$。

## 关键点

- 投射分解的比较映射在同伦意义下唯一，故 Ext 与分解选取无关。
- Ext 的 Yoneda 积与合成一致，使 $\bigoplus_n\operatorname{Ext}^n(M,M)$ 成为分次环。
- Koszul 分解给出多项式环上模的显式 Ext。

## 公式

```latex
\operatorname{Ext}^n_A(M,N):=H^n(\operatorname{Hom}_A(P_\bullet,N))
```
```latex
\operatorname{Ext}^1_A(M,N)\leftrightarrow\{0\to N\to E\to M\to0\}
```

## 常见错误

- 用任意分解（非投射/自由）硬算 Ext，得到的结果依赖分解。
- 把 $\operatorname{Ext}^1$ 只当成扩张的集合，忘掉它的加法群结构。

## 批注

### 易错预警：分解必须投射

Ext 的定义要求 $P_i$ 投射（或自由）；用一般分解取 Hom 上同调不保持同构。

### 背景直觉：Ext 是“高阶 Hom”

$\operatorname{Ext}^n$ 衡量“先映射再修正”的障碍；在导出范畴里它只是 Hom 的平移分量。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §2.3；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch02.tex:474-771`
- 原书页码从略：本机无英文原书与页面图像，只以中译本节号与源码行号定位。

---

权利：`rewritten`；核验：`source-only`。
