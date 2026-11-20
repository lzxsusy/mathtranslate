# 线算符：威尔逊算符与 't Hooft 算符

- **id**：`gw06/concept/line-operator`
- **类型**：concept
- **位置**：§4.5
- **问题**：若威尔逊算符与 't Hooft 算符都由 $^L\neg G$ 的表示标记，那 $G$ 与 $^L\neg G$ 的对偶究竟在这两种算符之间做了什么？

> 沿黎曼面上一条线插入的半 BPS 算符；$\Psi=\infty$ 处为威尔逊算符，$\Psi=0$ 处为 't Hooft 算符，二者都由对偶群的表示标记，$S$-对偶交换二者。

## 定义

线算符是四维 $\mathcal N=4$ 超杨–米尔斯理论中沿一条线（本文取为 $C$ 中的点 $q$ 加上 $\Sigma$ 中沿其边界的线）插入的半 BPS 缺陷，用规范群的一个表示来标记。在 $\Psi=\infty$ 的 $B$-模型一侧规范群取为 $^L\neg G$，对应的威尔逊算符把膜的 Chan-Paton 丛 ${\mathcal U}$ 换成 ${\mathcal E}_{^L\neg R}|_q\otimes{\mathcal U}$，其中 ${\mathcal E}_{^L\neg R}$ 是万有希格斯丛在表示 $^L\neg R$ 中的相伴丛。在 $\Psi=0$ 的 $A$-模型一侧规范群为 $G$，对应的是由奇点处 BPS 磁单极子构造的 't Hooft 算符。一般地威尔逊算符改变离散电通量 ${\bf e}_0$、't Hooft 算符改变离散磁通量 ${\bf m}_0$，只有来自 $^L\neg G_{\rm ad}$ 的表示才保持相应的通量。物理上线算符的乘法就是表示张量积，而 $G$ 与 $^L\neg G$ 的对偶把由 $R$ 标记的威尔逊算符映为同一 $R$ 标记的 't Hooft 算符，这是几何朗兰兹的核心论断。

**记号**：$^L\neg G$：朗兰兹对偶群、${\mathcal E}_{^L\neg R}$：万有希格斯丛在表示 $^L\neg R$ 中的相伴丛、${\bf e}_0,{\bf m}_0$：离散电通量与离散磁通量、${\mathcal U}$：膜的 Chan-Paton 丛

## 关键点

- 威尔逊算符出现在 $\Psi=\infty$（规范群 $^L\neg G$），'t Hooft 算符出现在 $\Psi=0$（规范群 $G$），两端不可对调。
- 两者都由 $^L\neg G$ 的表示分类：复合对应张量积，保通量的子类对应 $^L\neg G_{\rm ad}$ 的表示。
- (4.11)–(4.13) 的 $\hat{\mathcal V}$、$\mathcal V$ 记录分歧参数 $(\alpha,\beta,\gamma,\eta)$ 的等价关系，$\hat{\mathcal V}/\mathcal V\cong\pi_1(G)\times\pi_1({}^L\neg G)$ 正是离散通量。
- 对偶的净效果：由 $R$ 标记的威尔逊算符对应同一 $R$ 标记的 't Hooft 算符，这是 §4.6 全部讨论的出发点。
- $S:\tau\to-1/n_{\mathfrak g}\tau$ 交换 $K(\MH({}^L\neg G,C))$ 与 $K(\MH(G,C))$，并交换 $\Lambda_{\rm rt}$ 与 $\Lambda_{\cort}$、${\bf e}_0$ 与 ${\bf m}_0$。

## 公式

```latex
{\mathcal E}_{^L\neg R}|_q\otimes {\mathcal U}
```
```latex
\hat {\mathcal V}=\left(\Lambda_\cochar\oplus\Lambda_\char\right)\rtimes\Weyl.
```
```latex
{\mathcal V}=\left(\Lambda_\cort\oplus\Lambda_\rt\right)\rtimes\Weyl.
```
```latex
1\to {\mathcal V}\to \hat{\mathcal V}\to \pi_1( G)\times \pi_1({}^L\neg G)\to 1.
```

## 常见错误

- 把两端对调：威尔逊在 $\Psi=\infty$、't Hooft 在 $\Psi=0$；写反后『对偶把威尔逊换成 't Hooft』变成同侧命题，核心论断随之消失。
- 以为线算符的本征值是数：'t Hooft 算符的本征膜带的是表示空间，本征值是向量空间与重数，不是标量。
- 漏掉保通量条件：一般威尔逊算符改变 ${\bf e}_0$，只有 $^L\neg G_{\rm ad}$ 的表示保通量，否则 (4.13) 的因子无法解释。

## 批注

### 易错预警：$\Psi=\infty$ 与 $\Psi=0$ 别对调

威尔逊算符在 $\Psi=\infty$（$B$-模型，规范群 $^L\neg G$），'t Hooft 算符在 $\Psi=0$（$A$-模型，规范群 $G$）。对调之后『$G$ 与 $^L\neg G$ 的对偶把威尔逊算符映为 't Hooft 算符』就变成同一模型内部的陈述，几何朗兰兹的核心论断被抹平。原文第 36–40 行把这一映射明确表述为两类算符之间的对应。

### 含糊点拨：『由表示标记』不是『由群元素标记』

线算符的乘法对应表示张量积，所以标记是表示；只有保通量的子范畴对应 $^L\neg G_{\rm ad}$ 的表示。若误以为标记是群元素，就会把 (4.11)、(4.12) 里的平移格当成算符指标，而它们实际是分歧参数的等价群，两者相差整整一个对偶群的表示论层面。

### 背景直觉：离散通量为何是中心问题

非单连通 $G$ 的威尔逊算符可带不同离散电通量 ${\bf e}_0$，对偶下 ${\bf e}_0$ 与 ${\bf m}_0$ 互换；$\hat{\mathcal V}/\mathcal V\cong\pi_1(G)\times\pi_1({}^L\neg G)$ 把这件事代数化，所以 (4.13) 不是技术细节，而是物理内容的编码，也决定了 (4.11) 与 (4.12) 的群论形状。这也解释了 (4.13) 的右边为何是两个 $\pi_1$ 的积：电与磁各贡献一个因子。

## 出处

- Gukov–Witten 2006（hep-th/0612073v2）中译校订本 §4.5；印刷页 [97, 100] / PDF 页 [98, 101]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s04b-lines.tex:9-160`
- 线算符、威尔逊与 't Hooft 算符的对照见 PDF 第 98–101 页（印刷 97–100 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
