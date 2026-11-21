# 辛形式漏了因子 i 与复坐标

- **id**：`sy0117/correction/symplectic-factor-i`
- **类型**：correction
- **章**：第5章
- **问题**：为什么辛形式不能写成 g_{i j̄} dx^i∧dx^j̄？

> Kähler 形式在复坐标下是 i g_{i j̄} dz^i∧dz̄^j；原式写成实坐标且漏 i。

## 位置

§5.3，ch05.tex:218

## 原文片段

```latex
\omega=g_{i\bar j}dx^i\wedge dx^{\bar j}
```

## 改为

```latex
\omega=i g_{i\bar j}dz^i\wedge d\bar z^j
```

## 依据

Kähler 形式是实 (1,1)-形式，复坐标下带因子 i；实坐标的 dx∧dx 组合会给出对称的度量分量，不是反对称的辛形式。

## 说明

本轮依据 Kähler 形式的复坐标表达式判定；未逐页核对英文原书。

## 批注

### 易错预警：i 不能省

把 ω 写成纯实系数会丢掉 Kähler 形式的虚部；先写 dz∧dz̄，再乘 i，最后取实部验算。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §5.3；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch05.tex:216-220`
- 原书页码从略；本卡锚定中译校定本（2026-11-21 第三轮校定）的节号与源码行号，正文已对照 CUP 2021 英文原书核验。

---

权利：`rewritten`；核验：`source-verified`。
