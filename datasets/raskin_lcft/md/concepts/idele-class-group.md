# 伊代尔类群

> `raskin_lcft/concept/idele-class-group` ｜ track A ｜ reviewed

**一句话**：整体域 F 的伊代尔群模去主伊代尔 A_F^×/F^×；它是 gcft 的主角，代替局部情形里的 K^×。

**自测**：为什么整体类域论要用 A_F^×/F^× 而不是 F^× 或其完备化？

## 定义

整体域 $F$ 的伊代尔群 $\mathbb A_F^\times$ 是 $\prod_v F_v^\times$ 的受限直积（几乎处处取 $\mathcal O_v^\times$）。对角嵌入 $F^\times\hookrightarrow\mathbb A_F^\times$ 给出伊代尔类群 $C_F=\mathbb A_F^\times/F^\times$。整体类域论断言 $\mathrm{Gal}(F^{\mathrm{ab}}/F)\cong\widehat{C_F}$。

记号：$C_F=\mathbb A_F^\times/F^\times$；$C_E/N_{E/F}C_E$ 对应 $\\mathrm{Gal}(E/F)$。

## 要点

- 局部—整体的统一：$C_F$ 的每个素位分量都是 $F_v^\times$，gcft 由各处的 lcft 拼起来（第 21 讲阿廷互反就是这个拼法）。
- 范数商 $C_F/N(C_E)$ 是整体互反律的左边，其阶等于 $[E:F]$（第一不等式）。
- 类群不是紧的，但 $C_F^0$（次数 0 部分）紧；两个不等式正是绕开非紧性的技术。
- 第 4–5 讲的 $n=2$ 情形（乘积公式 + 二次互反）是 $C_F$ 图景的初等投影。

## 公式

C_F=\mathbb A_F^\times/F^\times
\mathrm{Gal}(F^{\mathrm{ab}}/F)\cong\widehat{C_F}

## 定理与证明

### 定理 1.7 / 20.8（gcft 主定理）

设 $F$ 是整体域，则 $\mathrm{Gal}(\overline F/F)^{\mathrm{ab}}\cong\widehat{\mathbb A_F^\times/F^\times}$；对有限 Galois 扩张 $E/F$ 有 $\mathrm{Gal}(E/F)^{\mathrm{ab}}\cong N(\mathbb A_E^\times)\backslash\mathbb A_F^\times/F^\times$。

（sketch；来源：原书 p.87）


缺口：由两个不等式（定理 20.9）挤压得到，见「第一不等式」与「第二不等式下降」两张推导卡。

## 易错点

- 把 C_F 当成紧群：它不是紧的（有 Z 分量），紧的是它的某个连通/全纯部分
- 把「主伊代尔」当成「主理想」：F^× 嵌入 A_F^× 是对角嵌入
- 混淆 A_F（加法）与 A_F^×（乘法）的拓扑
- 把 $\widehat{C_F}$ 的帽子理解成「取紧化」：这里是 profinite 完备化，不是单点紧化。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 4 讲 整体类域论与二次互反律，p.14–18（原书 p.14）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 20 讲 第一不等式的证明，p.86–91（原书 p.86）

关联：`raskin_lcft/concept/lcft-main-theorem`、`raskin_lcft/concept/norm-group`、`raskin_lcft/concept/hilbert-symbol`

来源说明：卡由中译本的数学内容改写，不含底本原文；页码为底本印刷页。
