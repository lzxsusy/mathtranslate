# 4.2 中乘以 $i$ 的自同构应作 $\varphi$ 而非 $\phi$

- **id**：`bdh/correction/phi-to-varphi`
- **类型**：correction
- **位置**：§4
- **问题**：为什么 4.2 中乘以 $i$ 的自同构要写作 $\varphi$ 而不是 $\phi$？

> $f_{\pm i}$ 的定义把圈形 $\varphi$ 排成直体 $\phi$，与 §4.1 的 $\phi_{S,\mathfrak{F}}$ 族混同。

## 位置

§4.2 ch04.tex:234

## 原文片段

```latex
f_{\pm i}:=(\phi_{\pm i})_{*}
```

## 改为

```latex
f_{\pm i}:=(\varphi_{\pm i})_{*}
```

## 依据

原书 p.133 此处是圈形 $\varphi$（放大核对），而直体 $\phi$ 在 §4.1（p.125）专指 $\phi_{S,\mathfrak{F}}$ 族；若写成 $\phi_{\pm i}$，读者会把它读成那个族的特例。可这里 $\varphi_i:\mathcal{Q}\to\mathcal{Q}^{-}$ 是「乘以 $i=\sqrt{-1}$」诱导的自同构——$\mathcal{Q}^{-}$ 只是把配对改成相反号，乘以 $i$ 恰好使配对变号——同段随后正是用它把 $\operatorname{Pf}(\mathcal{Q})$ 与 $\operatorname{Pf}(\mathcal{Q}^{-})$ 等同起来。记为 $\phi_{\pm i}$ 后，$\phi$ 的既有指称被占用，$f_{\pm i}$ 的构造反而找不到定义。

## 说明

译本改译：ch04.tex:234 的 $\phi_{\pm i}$、$\phi_i$ 改为 $\varphi$；同章 4.3.13 证明中的同类直体（ch04.tex:779、782 共 4 处）一并改为 $\varphi$。p.125 的 $\phi_{S,\mathfrak{F}}$ 族保持直体未动。

## 批注

### 易错预警：$\phi$ 与 $\varphi$ 在这本书里是两个对象

圈形 $\varphi$ 用于「乘以 $i$」这类自同构以及证明中的普通函数；直体 $\phi$ 留给 4.1 的 $\phi_{S,\mathfrak{F}}$ 族。二者字形接近，排印时最容易混，但一混指称就错了——读者会以为 $\varphi_i$ 是 $\phi_{S,\mathfrak{F}}$ 在某个 $S,\mathfrak{F}$ 下的特例。

### 背景直觉：乘以 $i$ 为什么给出同构

$\mathcal{Q}^{-}$ 与 $\mathcal{Q}$ 的差别只在配对取相反号；乘以 $i=\sqrt{-1}$ 后二次型变号，于是 $\mathcal{Q}\cong\mathcal{Q}^{-}$，$\varphi_i$ 就是这个同构。$f_{\pm i}$ 用它把 Pfaffian 线丛与它的「负号版本」等同，4.2 之后所有 $c_{\pm i}$ 的构造都建立在这个等同之上。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §4.2；印刷页 [133] / PDF 页 [133]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch04.tex:232-236`
- 印刷页=PDF 页；页标记 $\SourcePage{134}$ 在 ch04.tex:253，故 232–236 行属 p.133。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
