# Orlov 定理与 K3 的 Hodge 等距

> `functoriality/concept/orlov-theorem` ｜ track B ｜ draft

**一句话**：全忠实正合函子若有左右伴随，则同构于某个 Fourier–Mukai 变换且核在同构下唯一；K3 的导出等价等价于 Hodge 等距。

**自测**：Orlov 定理为什么能把导出范畴之间的函子整体等同于乘积上的核？

## 定义

Orlov 定理（原文定理 3.2）：固定光滑射影簇 $X$ 与 $Y$，设 $F:D^b(X)\to D^b(Y)$ 是全忠实正合函子；若 $F$ 既有左伴随又有右伴随，则存在 $\mathscr P\in D^b(X\times Y)$ 使 $F$ 自然同构于 $\Phi_{\mathscr P}$，且 $\mathscr P$ 在同构意义下唯一。原文强调更强的形式：$X\times Y$ 上的凝聚层导出范畴与从 $D^b(X)$ 到 $D^b(Y)$ 的函子范畴之间自然等价。两个推论例子是 K3 曲面的 Hodge 等距判据（定理 3.3）与爆破的半正交分解（定理 3.4）。

记号：$\widetilde H(X;\Z)$：扩充 Hodge 格；$\langle D^b(X),D^b(Y),\ldots\rangle$：半正交分解；$\Phi_{\mathscr P}$ 以 $\mathscr P$ 为核。

## 要点

- 伴随条件不可省：左右伴随齐备才能把函子「反向」也控制在 $D^b$ 内部，从而读出核。
- 结论比「每个函子都有核」更强：核本身与函子之间的对应是范畴等价，$D^b(X\times Y)$ 就是函子范畴的模型。
- K3 情形：线性正合等价与扩充 Hodge 格 $\widetilde H$ 的等距是同一件事，这是 Hodge 结构进入导出范畴的通道。
- 爆破给出半正交分解，说明导出范畴的三角结构记录了爆破的几何；这类结论是辛侧拉格朗日对应构造的范本。

## 公式

$F:D^b(X)\to D^b(Y)$
$\widetilde H(X;\Z)\xrightarrow{\simeq}\widetilde H(Y;\Z)$
$D^b(\widetilde X)=\left\langle D^b(X),\underbrace{D^b(Y),\ldots,D^b(Y)}_{c-1}\right\rangle.$

## 定理与证明

### Orlov 表示定理

设 X、Y 是光滑射影簇，F 是从 D^b(X) 到 D^b(Y) 的全忠实正合函子。若 F 既有左伴随又有右伴随，则存在核 P∈D^b(X×Y)，使 F 自然同构于 Φ_P，且 P 在同构意义下唯一。

（none；来源：原书 p.20 §3.2）


缺口：原文只陈述定理并引 Orlov 的定理 2.2，未给证明；核的构造与唯一性证明在 Orlov 原文。

### K3 的导出等价判据

设 X、Y 是 K3 曲面。D^b(X) 与 D^b(Y) 之间存在线性正合等价，当且仅当存在扩充 Hodge 格之间的等距 H~(X;Z)≅H~(Y;Z)。

（none；来源：原书 p.20 §3.2）


缺口：原文引 Huybrechts 命题 10.10 与 Orlov 定理 3.3，未给证明；「线性」指保持 Hodge 结构。

### 爆破的半正交分解

设 X 是光滑射影簇，Y⊂X 是余维 c≥2 的光滑子簇，X~ 是 X 沿 Y 的爆破。则 D^b(X~) 有半正交分解，由 D^b(X) 与 c-1 份 D^b(Y) 组成。

（none；来源：原书 p.20 §3.2）


缺口：原文引 Orlov 定理 4.3，只给分解式 (47)，未讨论半正交性证明。

## 易错点

- 漏掉伴随条件：只假设 F 全忠实正合并不足以保证 F 是 Fourier–Mukai 变换。
- 把「核唯一」读成唯一确定的对象：这里的唯一性是在同构意义下，且核随函子的自然同构类而变。
- 把 K3 判据里的线性正合等价换成三角等价：必须保持 Hodge 结构，否则判据不成立。
- 把 $\widetilde H$ 当作普通上同调：扩充 Hodge 格包含度数 0 与 4 的部分，并带相交形式。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§3.2，p.20–20（原书 p.20 §3.2）

关联：`functoriality/concept/fourier-mukai`、`functoriality/concept/derived-category-coherent`、`functoriality/deriv/fm-composition`

来源说明：原书 p.20 §3.2（定理 3.2、3.3、3.4）；公式取自中译本 chapter3.tex。
