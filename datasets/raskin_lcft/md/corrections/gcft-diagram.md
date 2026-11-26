# 定理 20.8 印作 Gal^ab(G)，G 全书未定义

> `raskin_lcft/correction/gcft-diagram` ｜ 原书 p.87 ｜ reviewed

**一句话**：gcft 主定理左端印成 Gal^ab(G)，而 G 全书未定义；按上下文应为 Gal(F̄/F)^ab，右端帽子罩整个商群。

**自测**：为什么断定左端是 Gal(F̄/F)^ab 而不是别的群？

## 初版

```
$\mathrm{Gal}^{\mathrm{ab}}(G)\cong\widehat{(\mathbb A_F^\times/F^\times)}$。
```

## 改后

```
$\mathrm{Gal}(\overline F/F)^{\mathrm{ab}}\cong\widehat{\mathbb A_F^\times/F^\times}$。
```

## 为什么改

本讲此前已固定 $G_K=\mathrm{Gal}(\overline K/K)$、$G_L=\mathrm{Gal}(\overline K/L)$ 的记号，而 $G$ 作为群从未定义；gcft 左端必须是绝对 Galois 群的交换化，否则与右端（伊代尔类群的对偶）对不上。另外右端的帽子应罩整个 $\mathbb A_F^\times/F^\times$，不是只罩分子。

## 补注

译文按标准 gcft 主定理订正并加注；第二式 $\mathrm{Gal}(E/F)^{\mathrm{ab}}\cong N(\mathbb A_E^\times)\backslash\mathbb A_F^\times/F^\times$ 原文正确。

## 易错点

- 把 $\widehat{\mathbb A_F^\times/F^\times}$ 写成 $\widehat{\mathbb A_F^\times}/F^\times$：完备化与商不对易。
- 以为 $N(\mathbb A_E^\times)\backslash\mathbb A_F^\times/F^\times$ 中两个商可合并成一个。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 20 讲 第一不等式的证明，p.87–88（原书 p.87）

关联：`raskin_lcft/concept/idele-class-group`、`raskin_lcft/concept/brauer-group`

来源说明：勘误来自本次校对（对照 MIT OCW 公开讲义 PDF 逐页核校）；译文用 % [原文疑误：…] 注释留痕，注释不进 PDF。
