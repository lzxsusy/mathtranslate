# wrapped Fukaya 范畴

- **id**：`sy0117/concept/wrapped-fukaya`
- **类型**：concept
- **章**：第6章
- **问题**：为什么非紧流形上要用 wrapped 版本，而不是普通 Fukaya 范畴？

> wrapped Fukaya 范畴允许非紧 Lagrangian，用无穷远处的 Hamiltonian 流把 Floer 复形“卷”成有限型。

## 定义

对带 contact 边界的 Liouville 流形，wrapped Fukaya 范畴的对象是 admissible Lagrangian，Hom 取无穷远处 Hamiltonian 流的极限。部分 wrapped 版本还要选 stop，stop 决定哪些方向允许卷绕。

**记号**：stop 是 contact 边界上的闭子集；wrapped 版本对应 stop 为空，partially wrapped 对应非空 stop。

## 关键点

- wrapped 的 Hom 在无穷远处取 colimit，使原本无限维的 Floer 复形变成有限型。
- stop 的选择改变范畴：不同 stop 给出不同的 partially wrapped Fukaya 范畴。
- wrapped 范畴与 LG 模型、矩阵分解通过 HMS 配对。

## 公式

```latex
\operatorname{Hom}(L_0,L_1)=CF^\bullet(L_0,L_1)
```
```latex
\text{stop}\subset\partial_\infty M
```

## 常见错误

- 把 wrapped 与 partially wrapped 混用；两者对 stop 的处理不同。
- 把 stop 当成流形内部的子流形；它在 contact 边界上。

## 批注

### 易错预警：stop 保留英文

中译保留 stop 不译，是为了避免与拓扑中的“端点/停止点”混淆；读作“允许卷绕方向的边界标记”。

### 含糊点拨：wrapped 的极限

Hom 不是某一固定 Hamiltonian 流下的 Floer 复形，而是随流参数取 colimit；忘记这一点会把无穷维误当有限维。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §6.3；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch06.tex:709-1271`
- 原书页码从略：本机无英文原书与页面图像，只以中译本节号与源码行号定位。

---

权利：`rewritten`；核验：`source-only`。
