# 断言 20.13 的蛇引理交换图缺端点 0

> `raskin_lcft/correction/brauer-snake` ｜ 原书 p.89 ｜ reviewed

**一句话**：原文交换图只画出主体方块，缺最上一行 0→0→0 与各行端点 0，读者看不出「ψ 同构」来自蛇引理；译文按原图补齐。

**自测**：为什么这张图必须补上 0 行，蛇引理才能直接用？

## 初版

```
图含两行：$E_S^\times\to\mathbb A_{E,S}^\times\to C_E$ 与 $E_S^\times\to\mathbb A_E^\times\to C_E$，右列竖直标 $\psi$。
```

## 改后

```
图补齐为两行三列，最上一整行为 $0\to0\to0$，每行以 $0\to$ 起、前两行以 $\to0$ 止，$\varphi$ 标于下排向左箭头，$\psi$ 标于右列第二处竖直箭头。
```

## 为什么改

蛇引理要求上下两行都正合，而「正合」必须有端点 $0$ 才是短正合列；原图省略端点后，$\ker\psi\cong\mathrm{coker}\varphi$ 的来路就看不见了。$\varphi$ 既满又单（由 $S$ 的选取与 $E_S^\times$ 的定义），故 $\mathrm{coker}\varphi=0$，于是 $\psi$ 同构——这一步完全依赖端点。

## 补注

译文按原 PDF（印刷页 89–90）重排为 9 列 array 并加注；旧译此处曾用文字描述代替图。

## 易错点

- 把 $\varphi$ 的方向画反：它是 $\mathbb A_E^\times/\mathbb A_{E,S}^\times\to E^\times/E_S^\times$，箭头朝左。
- 省掉顶行 0 之后仍写「由蛇引理」：此时蛇引理前提不满足。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 20 讲 第一不等式的证明，p.89–90（原书 p.89）

关联：`raskin_lcft/concept/idele-class-group`、`raskin_lcft/concept/herbrand-quotient`

来源说明：勘误来自本次校对（对照 MIT OCW 公开讲义 PDF 逐页核校）；译文用 % [原文疑误：…] 注释留痕，注释不进 PDF。
