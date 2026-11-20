# 拓扑扭曲（GL 扭曲）与 $\Psi$ 平面

- **id**：`gw06/concept/topological-twist`
- **类型**：concept
- **位置**：§4.1
- **问题**：同一个 $\mathcal N=4$ 理论为什么能同时给出 $B$-模型与 $A$-模型，而 $S$-对偶不过是 $\Psi$ 平面上的一个分式线性变换？

> GL 扭曲由复参数 $t$ 给出，其 $\mathbb{CP}^1$ 坐标 $\Psi$ 上的分式线性作用把 $S$-对偶变成 $\Psi\to-1/(n_{\mathfrak g}\Psi)$；$\Psi=\infty$ 与 $\Psi=0$ 分别是 $J$ 型 $B$-模型与 $K$ 型 $A$-模型。

## 定义

拓扑扭曲把超对称代数中的一个分量当作 BRST 算子，使作用量对度量的依赖只剩拓扑部分，从而得到拓扑场论。本文用 GL 扭曲：它依赖一个复参数 $t$，给出一族以 $\mathbb{CP}^1$ 参数化的四维拓扑场论，$\Psi$ 是这个 $\mathbb{CP}^1$ 的坐标（可看作复 $\Psi$ 平面再加一个无穷远点）。$\Psi$ 是 $t$ 与规范耦合 $\tau=\theta/2\pi+4\pi i/e^2$ 的组合；对偶变换按 $\tau\to(a\tau+b)/(c\tau+d)$ 作用于 $\tau$ 时，$\Psi$ 作同一分式线性变换。物理上两个特殊点各给出一种拓扑模型：$\Psi=\infty$ 处是 $C$ 上希格斯丛模空间 $\MH$ 在复结构 $J$ 中的 $B$-模型，$\Psi=0$ 处是辛结构为 $\omega=({\rm Im}\,\tau)\omega_K$ 的 $A$-模型；两者都不依赖四维耦合 $e^2$，故可在弱耦合下研究。

**记号**：$t$：GL 扭曲参数（复）、$\tau=\theta/2\pi+4\pi i/e^2$：四维规范耦合、$\Psi$：$\mathbb{CP}^1$ 上的复坐标，是 $t$ 与 $\tau$ 的组合、$\omega_K$：复结构 $K$ 的辛（Kähler）形式、$\MH$：$C$ 上希格斯丛的模空间

## 关键点

- GL 扭曲由复参数 $t$ 标记，给出一族以 $\mathbb{CP}^1$ 参数化的四维拓扑场论；$\Psi$ 就是这个 $\mathbb{CP}^1$ 上的坐标，可看作复 $\Psi$ 平面加上无穷远点。
- 对偶变换在 $\tau$ 上按 $\tau\to(a\tau+b)/(c\tau+d)$ 作用，在 $\Psi$ 上按 $\Psi\to(a\Psi+b)/(c\Psi+d)$ 作用；特别地 $S$ 把 $\Psi=\infty$ 映到 $\Psi=0$，因为只有分式线性变换才交换 $0$ 与 $\infty$。
- $\Psi=\infty$ 处得到 $\MH$ 在复结构 $J$ 中的 $B$-模型，它全纯依赖于 $\alpha+i\gamma$，而局部不依赖 $\beta$ 与 $\eta$。
- $\Psi=0$ 处得到辛结构 $\omega=({\rm Im}\,\tau)\omega_K$ 的 $A$-模型，其中 ${\rm Im}\,\tau={4\pi/e^2}$ 来自动能项的归一化。
- 两种模型都不依赖 $e^2$，故都可在弱耦合下计算；$S$-对偶自动把 $J$ 型 $B$-膜与 $K$ 型 $A$-膜互换，这就是基本的几何朗兰兹对偶。

## 公式

```latex
\tau=\theta/2\pi+4\pi i/e^2
```
```latex
\Psi\to (a\Psi+b)/(c\Psi+d)
```
```latex
\omega=({\rm Im}\,\tau)\omega_K
```
```latex
{\rm Im}\,\tau={4\pi/e^2}
```

## 常见错误

- 把 $S:\tau\to-1/n_{\mathfrak g}\tau$ 按字面读成 $-\tau/n_{\mathfrak g}$：这只是把 $\tau$ 乘常数，把 $\Psi=\infty$ 映到 $\infty$，于是 $\Psi=\infty$ 与 $\Psi=0$ 不再互换，整套 $B$-模型与 $A$-模型的对应失去出发点。
- 把 $\Psi=0$ 处的模型也当成 $B$-模型：那里是辛结构 $\omega=({\rm Im}\,\tau)\omega_K$ 的 $A$-模型；记反后会把 $S$-对偶说成 $B$–$B$ 自对偶，并丢掉 $A$-模型一侧的全部膜构造。
- 把 ${\rm Im}\,\tau$ 当作与 $e^2$ 无关的常数：${\rm Im}\,\tau=4\pi/e^2$ 恰是弱耦合下发散的量，它只整体标度 $\omega$、不改变模型本身；忘了这一点会误以为 $\omega$ 在弱耦合有固定标度。

## 批注

### 易错预警：分母的括号不能省

原文把 $S$ 印作 $\tau\to-1/n_{\mathfrak g}\tau$，按字面读成 $-\tau/n_{\mathfrak g}$：这只是把 $\tau$ 乘一个常数，属于重标度，会把 $\Psi=\infty$ 映到 $\infty$，不可能把 $\infty$ 映到 $0$。同一句话却要求它交换 $\Psi=\infty$ 与 $\Psi=0$，故唯一自洽的读法是 $-1/(n_{\mathfrak g}\tau)$。第 4.3 节对 $\Psi$ 写的 $S:\Psi\to-1/n_{\mathfrak g}\Psi$ 有同样的排版问题。若照字面处理，$\mathrm{SL}(2,\Z)$ 的作用既不成群，两侧也不再对偶。

### 含糊点拨：$\Psi$ 是 $t$ 与 $\tau$ 的什么组合

原文只说 $\Psi$ 是 $t$ 与 $\tau$ 的某种组合，没有给出显式公式，因此不能替它补一个。可以核验的只有变换律：$\tau$ 作分式线性变换时，$\Psi$ 作同一个分式线性变换。据此，$\mathbb{CP}^1$ 上的 $S$ 必然交换 $\infty$ 与 $0$；第 4.2 节进一步给出，在 $^L\tau$ 取纯虚数时 $t=i$ 落在 $\Psi=\infty$、$t=1$ 落在 $\Psi=0$。本节用到的全部信息就是这两条。

### 背景直觉：扭曲之后几何还剩下什么

GL 扭曲把 $\mathcal N=4$ 的超对称代数换成拓扑 BRST 代数，理论对度量的依赖只剩拓扑部分，于是 $C$ 上的复几何（希格斯丛、平坦丛）可以直接当作二维模型的靶空间来读。几何朗兰兹的整套翻译就发生在 $\Psi=\infty$ 与 $\Psi=0$ 这两个特殊点之间。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §4.1；印刷页 [82, 83] / PDF 页 [83, 84]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s04a-branes.tex:24-71`
- §4.1 见 PDF 第 83 页末至第 84 页首（印刷第 82–83 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
