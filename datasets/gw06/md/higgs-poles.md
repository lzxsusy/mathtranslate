# 希格斯场的极点系数

- **id**：`gw06/concept/higgs-poles`
- **类型**：concept
- **位置**：§2.2
- **问题**：面算符的 β、γ 两个参数在希格斯场的极点中如何出现，它们在三个复结构里分别扮演什么角色？

> 在复结构 I 中，面算符给希格斯场 φ 引入留数为 (β+iγ)/2 的一阶极点；β、γ 因此是特征多项式极点系数的实部与虚部。

## 定义

令 $z=x^1+ix^2$，把式 (2.2) 的 $A=\alpha\,d\theta$、$\phi=\beta\,dr/r-\gamma\,d\theta$ 用复坐标写出，得 $\varphi=\frac{1}{2}(\beta+i\gamma)\,dz/z$（式 (2.11)）：从复结构 $I$ 看，面算符在希格斯场 $\varphi$（$\phi$ 的 $(1,0)$ 部分）中引入一个留数为 $\frac{1}{2}(\beta+i\gamma)$ 的一阶极点。换成复结构 $J$，自然的复变量是 $G_{\mathbb{C}}$ 值联络 $\mathcal{A}=A+i\phi$，它按希钦方程平坦，绕 $p$ 的单值性为 $U=\exp(-2\pi(\alpha-i\gamma))$（式 (2.12)），全纯依赖于 $\gamma+i\alpha$ 而与 $\beta$ 无关。换成 $K=IJ$，$\tilde{\mathcal{A}}=A+i\star\phi$ 的单值性为 $\exp(-2\pi(\alpha+i\beta))$。三个复结构由此给出表 1。

**记号**：$z=x^1+ix^2$；$\varphi$：$\phi$ 的 $(1,0)$ 部分；$\mathcal{A}=A+i\phi$：复联络；$U$：绕 $p$ 的单值性；$\star$：霍奇星。

## 关键点

- 复结构 $I$：$\varphi=\frac{1}{2}(\beta+i\gamma)\,dz/z$，留数为 $\frac{1}{2}(\beta+i\gamma)$，是一阶极点（式 (2.11)）。
- 复结构 $J$：单值性 $U=\exp(-2\pi(\alpha-i\gamma))$，全纯依赖 $\gamma+i\alpha$，与 $\beta$ 无关（式 (2.12)）。
- 复结构 $K$：单值性 $\exp(-2\pi(\alpha+i\beta))$，全纯依赖 $\alpha+i\beta$。
- 表 1：$I$ 行复模 $\beta+i\gamma$、Kähler 模 $\alpha$；$J$ 行复模 $\gamma+i\alpha$、Kähler 模 $\beta$；$K$ 行复模 $\alpha+i\beta$、Kähler 模 $\gamma$。

## 公式

```latex
\varphi=\frac{1}{2}(\beta+i\gamma)\,\frac{dz}{z}
```
```latex
U=\exp(-2\pi(\alpha-i\gamma))
```

## 常见错误

- 把留数记成 $\beta+i\gamma$（漏掉因子 $\frac{1}{2}$）：式 (2.11) 的 $\frac{1}{2}$ 来自 $\phi$ 的 $(1,0)$ 投影，漏掉会让后面 $I$ 行的复模与 $J$、$K$ 行对不上。
- 以为三个复结构的复模都是 $\beta+i\gamma$：它们分别是 $\beta+i\gamma$、$\gamma+i\alpha$、$\alpha+i\beta$，循环置换。
- 忽略“单极点”这一条件：$dz/z$ 是一阶极点，对应驯服分歧；高阶极点（野分歧）的面算符不在本文范围内。

## 批注

### 易错预警：$\frac{1}{2}$ 从哪来

$\phi$ 是实一形式，$\varphi$ 是它的 $(1,0)$ 部分：$\phi=\varphi+\bar\varphi$。把 $\beta\,dr/r-\gamma\,d\theta$ 写成复形式时 $dr/r+i\,d\theta=dz/z$，实部与虚部各贡献一半，于是留数是 $\frac{1}{2}(\beta+i\gamma)$。反过来，若把 $\varphi$ 直接写成 $(\beta+i\gamma)dz/z$，则在实坐标下 $\phi$ 的系数会变成 $2\beta$ 与 $2\gamma$，与式 (2.2) 差一个整体因子，后面表 1 的循环对称也无法对齐。

### 含糊点拨：三个复结构的分工

$I$ 看的是希格斯丛的全纯结构，$J$ 看的是平坦 $G_{\mathbb{C}}$-联络，$K=IJ$ 是两者的合成。同一个面算符在三个复结构下读出的“复模”不同，这正是超 Kähler 商的三组复坐标；表 1 就是把这三组坐标排在一起。

### 背景直觉：极点系数 = 抛物权

在 $I$ 中，带分歧希格斯丛的抛物结构由分歧点处的旗与权给出；$\beta+i\gamma$ 是希格斯场留数，$\alpha$ 是抛物权（模余特征格）。这与第 3.4 节抛物丛的构造是同一套数据的两种说法。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §2.2；印刷页 [9, 10] / PDF 页 [10, 11]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s02a-definition.tex:170-236`
- 式 (2.11)–(2.12) 与表 1；印刷页 9–10，原文 PDF 第 10–11 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
