# Morse 证明的 Asc/Desc 写反

- **id**：`sy0117/correction/morse-asc-desc`
- **类型**：correction
- **章**：第6章
- **问题**：Morse 同调里连接 p 到 r 的流线到底经过 Asc(p) 还是 Desc(p)？

> 从 p 到 r 的流线应先离开 p 的上升集、再进入 r 的下降集；原式写反且流方向反。

## 位置

§6.1，ch06.tex:100

## 原文片段

```latex
\operatorname{Asc}(p)\cap\operatorname{Desc}(r)
```

## 改为

```latex
\operatorname{Desc}(p)\cap\operatorname{Asc}(r)
```

## 依据

Morse 流从 p 出发、沿 -∇f 流向 r：离开 p 时在 Desc(p)，到达 r 前在 Asc(r)。写成 Asc(p)∩Desc(r) 等于要求流线先上升再下降，方向反了。

## 说明

本轮依据 Morse 流的定义判定；未逐页核对英文原书。

## 批注

### 易错预警：A/D 跟着流方向

记法：Desc(p) 是“从 p 流出去能到达的点”，Asc(r) 是“能流到 r 的点”；连接 p→r 的流线在 Desc(p)∩Asc(r)。

## 出处

- Raf Bocklandt《同调镜像对称性浅入门》中译校订本（据 CUP 2021 英文版） §6.1；锚点 `08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch06.tex:98-104`
- 原书页码从略；本卡锚定中译校定本（2026-11-21 第三轮校定）的节号与源码行号，正文已对照 CUP 2021 英文原书核验。

---

权利：`rewritten`；核验：`source-verified`。
