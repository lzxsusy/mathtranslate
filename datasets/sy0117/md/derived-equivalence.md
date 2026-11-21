# 导出等价与 Fourier–Mukai

- **id**：`sy0117/concept/derived-equivalence`
- **类型**：concept
- **章**：第7章
- **问题**：为什么导出等价能连接几何上不同的簇？

> 导出等价是三角范畴层面的等价，常由 Fourier–Mukai 核给出；它比簇同构粗，却保留 Ext 与高阶结构。

## 定义

两个簇 $X,Y$ 的导出等价是 $D^b(X)\simeq D^b(Y)$ 的三角等价。Fourier–Mukai 函子以核 $\mathcal P\in D^b(X\times Y)$ 给出 $\Phi_{\mathcal P}(-)=R\pi_{2*}(\mathcal P\otimes L\pi_1^*(-))$；很多导出等价都来自这种核。

**记号**：$D^b(X)$ 是 $X$ 上凝聚层的导出范畴；$\pi_1,\pi_2$ 是投影。

## 关键点

- 导出等价保持 Ext 群、Serre 函子与高阶结构，但不一定保持簇同构。
- 例外集合给出半正交分解，可用于构造 Fourier–Mukai 核。
- Fourier–Mukai 核的支撑决定函子的几何意义。

## 公式

```latex
D^b(X)\simeq D^b(Y)
```
```latex
\Phi_{\mathcal P}(-)=R\pi_{2*}(\mathcal P\otimes L\pi_1^*(-))
```

## 常见错误

- 把导出等价误当簇同构；很多非同理簇也有导出等价。
- 只给核不验三角结构；不是每个核都给出等价。

## 批注

### 易错预警：导出等价不等于同构

导出等价只要求三角范畴等价；它可能把点层送到复杂对象，不保持拓扑。

### 背景直觉：为什么核能连接几何

核 $\mathcal P$ 可以看成“点与点之间的 correspondence”；Fourier–Mukai 把 $X$ 上的层沿核传到 $Y$，类似积分变换。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §7.3；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch07.tex:1267-1857`
- 原书页码从略；本卡锚定中译校定本（2026-11-21 第三轮校定）的节号与源码行号，正文已对照 CUP 2021 英文原书核验。

---

权利：`rewritten`；核验：`source-verified`。
