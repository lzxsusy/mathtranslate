# 4.4.16 证明中半直积符号 $\rtimes$ 应为 $\ltimes$

- **id**：`bdh/correction/rtimes-to-ltimes`
- **类型**：correction
- **位置**：§4
- **问题**：为什么 4.4.16 证明里的 $\rtimes$ 必须改成 $\ltimes$？

> 半直积写反成 $\rtimes$，把 $\operatorname{Aut}_Z O$ 与 $\widetilde{G}(K)$ 的从属方向弄颠倒了。

## 位置

§4.4 ch04.tex:1087

## 原文片段

```latex
\operatorname{Aut}_Z O\rtimes\widetilde{G}(K)
```

## 改为

```latex
\operatorname{Aut}_Z O\ltimes\widetilde{G}(K)
```

## 依据

原书 p.172 该符号的字形是 ≫（即 $\ltimes$）。4.4.16 讲的是 $\operatorname{Aut}_Z O\ltimes\widetilde{G}(K)$ 在 $\lambda_{\mathcal{L}}^{\wedge}$ 上的作用：$\operatorname{Aut}_Z O$ 是正规子群、$\widetilde{G}(K)$ 通过其在 $\mathfrak{g}\otimes K$ 上的作用进入，与 4.4.14（ch04.tex:1099）的 $\operatorname{Aut}_2 O\ltimes\widetilde{G}(K)$ 及同段 1097/1101/1103 各处一致。写成 $\rtimes$ 表示反方向（$\widetilde{G}(K)$ 正规、$\operatorname{Aut}_Z O$ 作用其上），1087 的「定义了……的一个作用」就失去主语，1103「$\operatorname{Aut}_Z O$ 由 $\operatorname{Aut}_2 O$ 与 $Z$ 生成」这条生成链也读不通。

## 说明

译本改译：ch04.tex:1087、1097、1099、1101、1103 各行共 6 处 $\rtimes\to\ltimes$；同段其余文字未动。判断依据是原书字形与 4.4.14 的同一构造，未逐页对照英文印刷页。

## 批注

### 易错预警：$\ltimes$ 与 $\rtimes$ 方向相反

$A\ltimes B$ 表示 $A$ 正规、$B$ 作用在 $A$ 上（$A\rtimes B$ 则反过来，$B$ 正规）。本段 $\operatorname{Aut}_Z O$ 是正规子群、$\widetilde{G}(K)$ 通过 $\mathfrak{g}\otimes K$ 的作用进来，只能是 $\operatorname{Aut}_Z O\ltimes\widetilde{G}(K)$；符号写反后括号里的群结构整个变了，读者会去找一个并不存在的「$\operatorname{Aut}_Z O$ 作用在 $\widetilde{G}(K)$ 上」的构造。

### 含糊点拨：这个作用为什么存在

4.4.14 已经给出 $\operatorname{Aut}_2 O\ltimes\widetilde{G}(K)$ 在 $\lambda^{\wedge}_{\mathcal{L}_0}$ 上的典范作用；因 $\operatorname{Aut}_Z O$ 由 $\operatorname{Aut}_2 O$ 与 $Z$ 生成，4.4.16 只需再验证 $Z$ 与 $\widetilde{G}(K)$ 的作用相容。符号方向错了，这条「先有 $\operatorname{Aut}_2 O$、再补 $Z$」的论证顺序就读不出来。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §4.4；印刷页 [172] / PDF 页 [172]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch04.tex:1087-1103`
- 印刷页=PDF 页；页标记 $\SourcePage{175}$ 在 ch04.tex:1144，故 1087–1103 整段属 p.172。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
