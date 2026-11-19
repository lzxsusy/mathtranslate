# 为什么把讨论限制在球（无分歧）情形

> `gaits04/concept/why-spherical` · 轨 D 层化与猜想 · 状态 reviewed · 核验 source-only

**问题：** 限制在无分歧情形，损失了什么，又换来了什么？

**一句话：** 球尖点自守表示对应唯一（相差一个标量）的双商上的函数，几何上目标明确；一般尖点表示没有典范的函数可选，故不知该构造什么样的层。

**别名：** `spherical case`、`unramified`、`why restrict`

## 定义

最后讨论一个问题：为什么把讨论限制在球（即无分歧）情形？理由如下：如前所述，球尖点自守表示对应 $\mathrm{GL}_n(K)\backslash\mathrm{GL}_n(\mathbb A)/\mathrm{GL}_n(\mathbb O)$ 上一个确定的函数 $f$，它唯一到相差一个标量。因此，几何上我们要构造 $D^b(\mathfrak{B}\mathrm{un}_n)$ 中一个特定的对象；当 $k=\mathbb{F}_q$ 时，它给出这个函数。对一般的尖点自守表示 $\pi$，很难在 $\pi\subset\operatorname{Funct}_{cusp}(\mathrm{GL}_n(K)\backslash\mathrm{GL}_n(\mathbb A))$ 中典范地选出一个函数。因此，在相应的 $\mathfrak{B}\mathrm{un}_n$ 版本上该构造什么样的层，并不清楚。

**记号：** $\pi\subset\operatorname{Funct}_{cusp}$：一般尖点表示是子空间而非单个函数；球情形才有典范的球向量。

## 要点

- 球情形下 $\pi^{\mathrm{GL}_n(\mathbb O)}$ 一维，故「取一个函数」只差标量，几何对象的目标是明确的。
- 一般尖点表示的球向量为 $0$，没有典范向量可对应，故「该造什么层」本身不清楚。
- 这是技术性限制，不是本质限制：一般情形需要另外的几何化（如 Whittaker 模型、或考虑整个 $\pi$ 的层化）。

## 公式

$$
f\in\operatorname{Funct}(\mathrm{GL}_n(K)\backslash\mathrm{GL}_n(\mathbb A)/\mathrm{GL}_n(\mathbb O)),\qquad \dim\pi^{\mathrm{GL}_n(\mathbb O)}=1
$$

## 易错点

- 以为限制在球情形是「为了简单」：作者明说是因为一般情形下不知道要构造什么，属概念困难而非计算困难。

## 批注

**〔背景直觉〕一个函数 = 一个层**　几何 Langlands 的「对象」是层，而层在 $\mathbb{F}_q$ 上取迹才给函数。球情形下一个表示只给一个函数（差标量），所以「层 ↔ 函数」的对应是清楚的；一般情形一个表示给的是无穷维空间，没有典范元素可取迹。

## 相关

[[eigensheaf]]、[[sheaf-function]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§3.5，原书 pp. 278（PDF pp. 280）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec3.tex:66-72（§3.5）`
