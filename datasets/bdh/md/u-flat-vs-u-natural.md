# 8.1 末注中 $U^{\natural}_1$ 应为 $U^{\flat}_1$

- **id**：`bdh/correction/u-flat-vs-u-natural`
- **类型**：correction
- **位置**：§8
- **问题**：为什么 8.1 末注里的 $U^{\natural}_1/U^{\natural}_0$ 必须改成 $U^{\flat}_1/U^{\flat}_0$？

> 过滤片 $U^{\flat}_1/U^{\flat}_0$ 被排成 $U^{\natural}_1/U^{\natural}_0$，把重整化代数与它的过滤片混为一谈。

## 位置

§8.1 ch08.tex:52

## 原文片段

```latex
U^{\natural}_{1}/U^{\natural}_{0}
```

## 改为

```latex
U^{\flat}_{1}/U^{\flat}_{0}
```

## 依据

5.6.7（ch05.tex:953–956）的记号里 $U^{\natural}$ 是重整化泛包络代数，$U^{\flat}_i$ 是 $U^{\natural}_i$ 中消灭 $\mathit{Vac}'$ 真空向量的元素之集，$U^{\flat}_1/U^{\flat}_0$ 才是 $I/I^2$ 的像所在的商；同处还写「自然映射 $U^{\flat}_1/U^{\flat}_0\to U^{\natural}_1/U^{\natural}_0$」——两个商同时出现，正说明不能混。10.1.6（ch10.tex:76）在完全相同的构造中写 $a^{\flat}\in U^{\flat}_1$，且 $a$ 与 $a^{\flat}$ 在 $U^{\flat}_1/U^{\flat}_0$ 中有相同的像。若写成 $U^{\natural}_1/U^{\natural}_0$，$u$ 与 $a$ 的像不在同一个空间里，8.1 末注的等同就无从比较。

## 说明

译本改译：改 ch08.tex:52 两处（$u\in U^{\flat}_1$ 与 $U^{\flat}_1/U^{\flat}_0$）；同段其余 $U^{\natural}$ 指重整化代数本身，保持 ♮ 未动。依据是 5.6.7 的过滤与 10.1.6 的同一构造，未对照英文印刷页。

## 批注

### 易错预警：♮ 是代数，♭ 是它的过滤片

$U^{\natural}$ 是整个重整化泛包络代数，$U^{\natural}_i$ 是它的过滤；再取其中消灭真空向量的元素，才得到 $U^{\flat}_i$。两个上标只差一个符号，指数却变了：$U^{\flat}_1/U^{\flat}_0$ 是 $\mathfrak{z}$ 上的拓扑李代数胚，$U^{\natural}_1/U^{\natural}_0$ 则大得多。

### 背景直觉：为什么 8.1 末注要用 ♭

8.1 末注要把 $u\in U^{\flat}_1$ 与 $a\in I/I^2$ 在 $U^{\flat}_1/U^{\flat}_0$ 中的像等同。这一步依赖 5.6.7 的「自然映射」给出 $I/I^2\to U^{\flat}_1/U^{\flat}_0$；若把商换成 $U^{\natural}_1/U^{\natural}_0$，这个映射的靶就错了，$a$ 与 $u$ 根本不在同一个商里。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §8.1；印刷页 [369] / PDF 页 [369]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch08.tex:50-52`
- 印刷页=PDF 页；页标记 $\SourcePage{369}$ 在 ch08.tex:50，故 50–52 行属 p.369。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
