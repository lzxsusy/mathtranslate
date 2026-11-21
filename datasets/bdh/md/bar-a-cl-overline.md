# 2.4.2 的态射 $\bar a^{cl}$ 漏了两条上划线

- **id**：`bdh/correction/bar-a-cl-overline`
- **类型**：correction
- **位置**：§2
- **问题**：为什么这里必须补上 $\bar a^{cl}$ 与 $\overline{\operatorname{Sym}}$ 的上划线？

> 2.4.2 把 $\bar a^{cl}$ 与 $\overline{\operatorname{Sym}}$ 的上划线一起漏掉，读者会去找一个并不存在的 $a^{cl}$。

## 位置

§2.4 ch02.tex:137

## 原文片段

```latex
a^{cl}:(\operatorname{Sym}(\mathfrak{g}\otimes K_x))^{\mathfrak{g}\otimes K_x}
```

## 改为

```latex
\bar{a}^{cl}:(\overline{\operatorname{Sym}}(\mathfrak{g}\otimes K_x))^{\mathfrak{g}\otimes K_x}
```

## 依据

1.2.7（ch01.tex:169–173）定义的态射是 $\bar a^{cl}:((\overline{\operatorname{Sym}}\mathfrak{g})^{\mathfrak{g}})^{\pi_0(K)}\to P_{(\mathfrak{g},K)}$，源与靶都带完备化上划线；本句后半紧接着说「$(\overline{\operatorname{Sym}}(\mathfrak{g}\otimes K_x))^{\mathfrak{g}\otimes K_x}$ 是 $\overline{\operatorname{Sym}}(\mathfrak{g}\otimes K_x)$ 的泊松中心」，也带上划线。照原译读，$a^{cl}$ 在书中没有定义，而未完备化的 $\operatorname{Sym}$ 不可能满射到完备化的 $\mathfrak{z}_x^{cl}$。

## 说明

译本改译：只改 ch02.tex:137 这一处（同一片段内 3 个符号）；2.4.2 其余文字与 2.4.1 的描述未动。判定依据是 1.2.7 的定义与同句后半的上划线，不是英文印刷页逐字对照。

## 批注

### 易错预警：上划线是完备化，不是装饰

这里的 $\overline{\operatorname{Sym}}$ 表示完备化后的对称代数（1.2 中记作 $\overline{\operatorname{Sym}}\Theta_S$）；漏掉上划线后，源变成普通对称代数，靶却是完备化的 $\mathfrak{z}_x^{cl}$，满射性立刻不成立，$\mathfrak{z}_x^{cl}$ 的泊松中心结构也从「完备化的中心」掉回「中心」。

### 含糊点拨：$\bar a^{cl}$ 与 $a^{cl}$ 是两个对象

书中只定义了带横杠的 $\bar a^{cl}$；不带横杠的 $a^{cl}$ 没有出处。读者若在 2.4.2 看到 $a^{cl}$，会以为另有定义，往前翻却找不到，这是典型的排印漏字而不是记号简写。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §2.4；印刷页 [22] / PDF 页 [22]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch02.tex:133-139`
- 印刷页=PDF 页；这段在 2.4.2 开头，整段位于 p.22（下一处页标记在 ch02.tex:141）。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
