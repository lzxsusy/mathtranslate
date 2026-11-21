# G-oper：局部系统与横截的 Borel 旗

- **id**：`bdh/concept/g-oper-definition`
- **类型**：concept
- **位置**：§3.1
- **问题**：为什么给一个 $G$-局部系统加一条 Borel 旗、再要求联络的 $\mathfrak g/\mathfrak b$-分量落在「最负的一格」且处处不为零，就会得到一个刚性到没有对称性的对象？

> G-oper 是 $X$ 上的 $G$-局部系统连同 Borel 旗，要求 $\nabla$ 在 $\mathfrak g/\mathfrak b\otimes\omega_X$ 中的像落在 $\operatorname{gr}^{-1}\mathfrak g$ 内，且每个单负根分量处处非零。

## 定义

设 $X$ 是 $\mathbb{C}$ 上的光滑曲线（不必完备），$G$ 是连通约化群，固定 Borel 子群 $B\subset G$，令 $N=[B,B]$、$H=B/N$。李代数 $\mathfrak g$ 带典范降滤链 $\mathfrak g^{k}$：$\mathfrak g^{0}=\mathfrak b$，$\mathfrak g^{1}=\mathfrak n$，且 $\operatorname{gr}^{0}\mathfrak g=\mathfrak h$，$\operatorname{gr}^{-k}\mathfrak g$（$k>0$）是 $k$ 个单负根之和对应的权空间；特别地 $\operatorname{gr}^{-1}\mathfrak g=\bigoplus_{\alpha}\mathfrak g^{\alpha}$，$\alpha$ 取遍单负根。设 $\mathfrak{F}_B$ 是 $X$ 上的 $B$-torsor（主齐性空间），$\mathfrak{F}_G$ 是它诱导的 $G$-torsor，则有扭李代数 $\mathfrak{b}_{\mathfrak{F}}\subset\mathfrak{g}_{\mathfrak{F}}$ 与联络层 $\operatorname{Conn}(\mathfrak{F}_B)\subset\operatorname{Conn}(\mathfrak{F}_G)$，后者分别是 $\mathfrak{b}_{\mathfrak{F}}\otimes\omega_X$- 与 $\mathfrak{g}_{\mathfrak{F}}\otimes\omega_X$-torsor。包含关系给出仿射投影 $c:\operatorname{Conn}(\mathfrak{F}_G)\to(\mathfrak{g}/\mathfrak{b})_{\mathfrak{F}}\otimes\omega_X$，满足 $c^{-1}(0)=\operatorname{Conn}(\mathfrak{F}_B)$ 与 $c(\nabla+\nu)=c(\nabla)+\nu \bmod \mathfrak{b}_{\mathfrak{F}}\otimes\omega_X$。\emph{$X$ 上的 $G$-oper} 是一对 $(\mathfrak{F}_B,\nabla)$，其中 $\nabla\in\Gamma(X,\operatorname{Conn}(\mathfrak{F}_G))$，且 (1) $c(\nabla)\in\operatorname{gr}^{-1}\mathfrak{g}_{\mathfrak{F}}\otimes\omega_X\subset(\mathfrak{g}/\mathfrak{b})_{\mathfrak{F}}\otimes\omega_X$；(2) 对任意单负根 $\alpha$，$\alpha$-分量 $c(\nabla)^{\alpha}\in\Gamma(X,\mathfrak{g}^{\alpha}_{\mathfrak{F}}\otimes\omega_X)$ 在 $X$ 的任一点都不为零。等价的说法是：$G$-oper 是一个 $G$-局部系统 $(\mathfrak{F}_G,\nabla)$ 再附加一个满足 (1)、(2) 的 $B$-旗 $\mathfrak{F}_B\subset\mathfrak{F}_G$；若 $\mathfrak g$ 半单，则 $\mathfrak g$-oper 就是伴随群 $G_{ad}$ 的 oper。

**记号**：$\mathfrak{F}_B$：$X$ 上的 $B$-torsor（主齐性空间）；$\mathfrak{F}_G$：诱导的 $G$-torsor，$\mathfrak{F}_B\subset\mathfrak{F}_G$、$\mathfrak{g}_{\mathfrak{F}}:=\mathfrak{g}_{\mathfrak{F}_B}=\mathfrak{g}_{\mathfrak{F}_G}$：扭李代数，$\mathfrak{b}_{\mathfrak{F}}$ 是其 Borel 子代数，带滤链 $\mathfrak{g}^{k}_{\mathfrak{F}}$、$\operatorname{gr}^{-1}\mathfrak{g}=\bigoplus\mathfrak{g}^{\alpha}$：单负根空间之直和，是 $(\mathfrak{g}/\mathfrak{b})$ 的最低权片、$Z=Z_G=\operatorname{Center}G$：$G$ 的中心，也是连通 $X$ 上 oper 的全部自同构、$\operatorname{Op}_G(X)$：$X$ 上 $G$-oper 构成的群胚；$X'$ 在 $X$ 上平展时给出 $X_{\text{\'et}}$ 上的群胚层 $\operatorname{Op}_G$

## 关键点

- 定义是一条「位置 + 非零」的双重条件：条件 (1) 说 $\nabla$ 的 $\mathfrak g/\mathfrak b$-分量只含单负根分量，条件 (2) 说这些分量组成的截面在每一点都非零，因此它是 $\omega_X$-值的无处为零截面，而不是「一般点非零」。
- 两个条件都只看 $c(\nabla)$，即 $\nabla$ 在 $(\mathfrak g/\mathfrak b)_{\mathfrak{F}}\otimes\omega_X$ 中的像；$\mathfrak b$-分量（旗自身的水平部分）完全不受约束，这正是 $\operatorname{Conn}(\mathfrak{F}_B)\subset\operatorname{Conn}(\mathfrak{F}_G)$ 是 torsor 的含义。
- oper 结构是局部系统上的额外数据：同一 $(\mathfrak{F}_G,\nabla)$ 可以没有 oper 结构，也可以（在 §3.1.5 的假设下）至多有一个；$G$-oper 的群胚 $\operatorname{Op}_G(X)$ 因此是 $G$-局部系统栈里的子对象。
- $\mathfrak g$ 半单时 $\mathfrak g$-oper 与 $G_{ad}$-oper 是同一概念；一般 $G$ 的中心 $Z$ 会带来额外自由度，这由 §3.4 的 $\operatorname{Op}_G(X)=\operatorname{Op}_{\mathfrak g}(X)\times Z\operatorname{tors}(X)$（固定 $\omega_X$ 的平方根后）精确化。
- 平展下降给出群胚层：$\operatorname{Op}_G$ 是 $X_{\text{\'et}}$ 上的群胚层，故可谈 $\operatorname{Op}_G(X)$ 作为群胚（而非集合）；连通 $X$ 上自同构群为 $Z$（§3.1.4）。

## 公式

```latex
\mathfrak{g}^{0}=\mathfrak{b},\quad\mathfrak{g}^{1}=\mathfrak{n},\quad\operatorname{gr}^{-1}\mathfrak{g}=\bigoplus_{\alpha}\mathfrak{g}^{\alpha}
```
```latex
c:\operatorname{Conn}(\mathfrak{F}_G)\longrightarrow(\mathfrak{g}/\mathfrak{b})_{\mathfrak{F}}\otimes\omega_X,\qquad c(\nabla+\nu)=c(\nabla)+\nu\bmod\mathfrak{b}_{\mathfrak{F}}\otimes\omega_X
```
```latex
c(\nabla)\in\operatorname{gr}^{-1}\mathfrak{g}_{\mathfrak{F}}\otimes\omega_X\subset(\mathfrak{g}/\mathfrak{b})_{\mathfrak{F}}\otimes\omega_X
```
```latex
c(\nabla)^{\alpha}\in\Gamma(X,\mathfrak{g}^{\alpha}_{\mathfrak{F}}\otimes\omega_X),\qquad c(\nabla)^{\alpha}(x)\neq0\quad\forall x\in X
```

## 常见错误

- 把条件 (1) 读成 $c(\nabla)=0$：那只是 $\nabla\in\operatorname{Conn}(\mathfrak{F}_B)$ 的退化情形，此时旗与联络不构成 oper 的横截性。条件 (1) 要求 $c(\nabla)$ 恰好落在最低的一片 $\operatorname{gr}^{-1}\mathfrak g$，一般非零。
- 把「在任一点都不为零」弱化为「存在非零截面」：$c(\nabla)^{\alpha}$ 是线丛 $\mathfrak{g}^{\alpha}_{\mathfrak{F}}\otimes\omega_X$ 的截面（$\mathfrak g^{\alpha}$ 一维），非零截面若有零点就给出除子；条件要求每点非零，等价于该线丛被平凡化，这恰是 $\operatorname{Op}_G(X)$ 成为光滑栈的来源。
- 把 $G$-oper 与 $G_{ad}$-oper 混为一谈：只有 $\mathfrak g$ 半单时二者一致（§3.1.3 末），一般 $G$ 还要记录中心 $Z$ 的 torsor（§3.4）。把中心当平凡会在 §3.4 的 (55) 处丢掉 $Z\operatorname{tors}(X)$ 整个因子。
- 以为旗是无关的附加物：$c$ 依赖 $\mathfrak{F}_B$，换旗会改变 $c(\nabla)$；oper 是「局部系统 + 旗」的偶对，不是「局部系统 + 某个自动存在的旗」。不过 §3.1.5 证明：在完备亏格 $>1$ 的曲线上，给定局部系统至多有一个这样的旗。
- 在 $X$ 不完备时照搬紧致情形的结论：非完备时 $\operatorname{Op}_{\mathfrak g}(X)$ 只是归纳概形（§3.1.11 注 i），且条件 (2) 的「每点非零」不再能换成「除子次数为零」这类整体条件。

## 批注

### 易错预警：gr^{-1} 是负次数深处，不是 gr^{1}

§3.1.1 的滤链是降滤链，负下标向「深处」走：$\operatorname{gr}^{-k}\mathfrak g$ 的权是 $k$ 个单负根之和，故 $\operatorname{gr}^{-1}\mathfrak g=\bigoplus\mathfrak g^{\alpha}$ 恰是单负根空间，$\operatorname{gr}^{0}\mathfrak g=\mathfrak h$。条件 (1) 把 $c(\nabla)$ 压进这一片，意思是「联络的 $\mathfrak g/\mathfrak b$-部分只用掉一个单负根」。若误写成 $\operatorname{gr}^{1}\mathfrak g=\mathfrak n$，就会要求 $c(\nabla)$ 落在 $\mathfrak b$ 里、即 $c(\nabla)=0$，oper 退化为带旗的平坦丛，与 §3.1.6 的 $GL_n$ 模型（$\nabla(\mathcal E_i)\subset\mathcal E_{i+1}\otimes\omega_X$，旗移动一格）不符。

### 含糊点拨：为什么「不为零」是良定义的

每个 $\mathfrak g^{\alpha}$ 是一维根空间，故 $\mathfrak g^{\alpha}_{\mathfrak{F}}\otimes\omega_X$ 是线丛，$c(\nabla)^{\alpha}$ 是它的截面。「在任一点不为零」是截面性质，与选取 $\mathfrak{F}_B$ 的局部平凡化无关：换平凡化只把截面乘上可逆函数，零点集不变。这一点使条件 (2) 成为平展局部性质，从而 $\operatorname{Op}_G$ 是 $X_{\text{\'et}}$ 上的层；也解释了 §3.1.4 的刚性：没有零点可供连续移动，自同构只能是整体的中心元。

### 背景直觉：oper 这个名字的来源

在 $G=\mathrm{SL}_2$ 的情形，§3.1.6 末把 oper 翻译成 Sturm–Liouville 算子：带可逆层 $\mathcal A$ 与自伴二阶算子 $\partial:\mathcal A\to\omega_X\otimes\mathcal A^{\otimes(-1)}$，且象征处处非零。一般 $G$ 的 oper 是同一想法的「高秩化」：$\mathfrak g/\mathfrak b$ 分量只保留最低一片，等价于把联络写成算子象征的主部。正因如此，$\operatorname{Op}_{\mathfrak g}(X)$ 的坐标环与 $^{L}\mathfrak g$ 的 $z$ 代数同构（§3.3 的 Feigin–Frenkel 定理），oper 才成为几何朗兰兹中「算子」一侧的基本对象。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §3.1.1–§3.1.3；印刷页 [61, 62] / PDF 页 [61, 62]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch03.tex:10-27`
- 3.1.1–3.1.3 见原书 p.61，群胚与层一句已跨到 p.62；本书 PDF 页 = 印刷页。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
