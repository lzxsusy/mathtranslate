# 带分歧的西格玛模型与面参数

- **id**：`gw06/concept/sigma-model-ramified`
- **类型**：concept
- **位置**：§4.2
- **问题**：在 $C$ 上一点 $p$ 插入面算符，为什么只改变 $C$ 一侧的模空间、却让 $\Sigma$ 上的二维理论保持 $(4,4)$ 超对称？

> 在 $\Sigma\times C$ 的 $\Sigma\times p$ 上插入面算符，四维理论约化为目标为带分歧希格斯丛模空间 $\MH(\alpha,\beta,\gamma;p)$ 的二维西格玛模型，面参数与离散通量按格周期记账。

## 定义

取 $M=\Sigma\times C$、规范群 $^LG$，在 $\Sigma_p=\Sigma\times p$ 上插入驯服面算符，由参数 $(^L\neg\alpha,^L\neg\beta,^L\neg\gamma,^L\neg\eta)\in{}^L\TT\times\mathfrak t^\vee\times\mathfrak t^\vee\times{}^L\TT$ 标记，并取列维子群 $\mathbb L=\TT$。紧化后 $\Sigma$ 上的二维理论是目标空间为带分歧希格斯丛模空间 $\MH(\alpha,\beta,\gamma;p)$ 的西格玛模型，其底是抛物丛模空间 $\M(\alpha;p)$；两侧参数由 (4.2)–(4.3) 相联系。物理上：面算符是四维余维 $2$ 算符，沿 $\Sigma$ 铺满二维、沿 $C$ 只是点 $p$，所以它只在 $C$ 上加 $p$ 处的抛物结构，不在 $\Sigma$ 上加缺陷；目标空间超 Kähler 保证 $\Sigma$ 上的 $(4,4)$ 超对称不破缺。分歧不改变离散通量的定义，但使它们的作用发生质的变化：${\bf m}_0$ 可经平移 $\alpha$、${\bf e}_0$ 可经平移 $\eta$ 而改变。

**记号**：$^L\neg\alpha,{}^L\neg\beta,{}^L\neg\gamma,{}^L\neg\eta$：面算符参数、$\MH(\alpha,\beta,\gamma;p)$：带分歧希格斯丛模空间、$\M(\alpha;p)$：$p$ 处带抛物结构的模空间（希钦纤维化的底）、$\Lambda_\char,\Lambda_\rt,\Lambda_\cochar,\Lambda_\cowt$：权、根、余权、余根格

## 关键点

- 面算符支撑在 $\Sigma_p=\Sigma\times p$：四维余维 $2$，沿 $\Sigma$ 是二维、沿 $C$ 只是点 $p$，故只在 $C$ 上加抛物结构，不破坏 $\Sigma$ 上的 $(4,4)$。
- 两侧面参数由 (4.2)–(4.3) 相连：$\alpha={}^L\eta$、$\eta=-{}^L\alpha$，且 $(^L\beta,^L\gamma)=({\rm Im}\,\tau)(\beta^*,\gamma^*)$；反解时 $\beta,\gamma$ 与 $^L\beta,^L\gamma$ 互换、${\rm Im}\,^L\tau$ 与 ${\rm Im}\,\tau$ 互换。
- 目标空间 $\MH$ 超 Kähler，故 $\Sigma$ 上的模型有 $(4,4)$ 超对称；这来自靶空间几何，与是否插入面算符无关。
- 对秩 $r$ 的 $G$（排除 $r$ 与 $g_C$ 都很小的例外），$\MH(\alpha,\beta,\gamma;p)$ 的第二 Betti 数为 $r+1$：一个 $\theta$ 角来自四维 $\theta$ 角，其余 $r$ 个来自 $\eta$。
- 离散通量：${\bf m}_0\in\pi_1(G)$ 标记 $\MH$ 的分支，${\bf e}_0$ 是 $\pi_1(G_{\rm ad})/\pi_1(G)$ 的特征标，即 ${\bf e}_0\in\Lambda_\char/\Lambda_\rt$；有分歧时 ${\bf m}_0$、${\bf e}_0$ 可分别经平移 $\alpha$、$\eta$ 改变。

## 公式

```latex
(\alpha,\eta)=(^L\neg\eta,-^L\neg\alpha)
```
```latex
({}^L\neg\beta,{}^L\neg\gamma)=({\rm Im}\,\tau)(\beta^*,\gamma^*)
```
```latex
{\bf e}_0\in \Lambda_{\rm char}/\Lambda_{\rm rt}
```
```latex
\pi_1(G_{\rm ad})/\pi_1(G)=\Lambda_\cowt/\Lambda_\cochar
```

## 常见错误

- 把面算符当成 $\Sigma$ 上的缺陷：会预期超对称破缺到 $(2,2)$，并把 $\MH(\alpha,\beta,\gamma;p)$ 误当成某种边界条件的模空间；实际缺陷在 $C$ 上，$p$ 处只加抛物结构。
- 把 ${\bf e}_0$ 与 ${\bf m}_0$ 的格混用：${\bf m}_0$ 取 $\pi_1(G)$（标记 $\MH$ 分支），${\bf e}_0$ 取 $\pi_1(G_{\rm ad})/\pi_1(G)=\Lambda_\cowt/\Lambda_\cochar$ 的特征标；若让 ${\bf e}_0\in\Lambda_\cochar$ 或 ${\bf m}_0\in\Lambda_\char$，(4.5) 与 (4.6) 描述的就不再是同一个中心。
- 漏掉 $(\alpha,\eta)=({}^L\eta,-{}^L\alpha)$ 第一行的负号：则 $^L\gamma+i^L\alpha=({\rm Im}\,\tau)\gamma^*-i\eta$ 的虚部变成 $+i\eta$，复化 Kähler 类整体反号，$\eta$ 的周期也从 $\Lambda_\rt$ 错成别的格。

## 批注

### 易错预警：面算符住在哪一维

面算符沿 $\Sigma$ 铺满二维、沿 $C$ 只是一个点 $p$，在四维理论中是余维 $2$ 的算符。若把它想成 $\Sigma$ 上的缺陷，就会预期 $\Sigma$ 上超对称破缺到 $(2,2)$，还会把 $\MH(\alpha,\beta,\gamma;p)$ 当成某种边界条件的模空间。正确图像是：缺陷住在 $C$ 上，$p$ 处的抛物结构改变了靶空间，而 $\Sigma$ 上的 $(4,4)$ 超对称完整保留，因为靶空间仍是超 Kähler 的。

### 含糊点拨：$\eta$ 是哪个 $\theta$ 角

这里的 $\eta$ 不是四维 $\theta$ 角，而是二维西格玛模型除四维 $\theta$ 角之外的 $r$ 个 $\theta$ 角：四维 $\theta$ 角由 $\tau=\theta/2\pi+4\pi i/e^2$ 的实部给出，$\eta$ 则是面算符的第四个参数。之所以能把 $\eta$ 当平移参数处理，是因为由 (4.2) 可见 $S$-对偶把 $\theta$ 角与几何参数 $(\alpha,\beta,\gamma)$ 互换，于是 $\eta$ 的周期由格而非连续参数控制，平移 $\eta$ 才是在改模型的离散数据。

### 背景直觉：分歧为什么正好是抛物结构

面算符在 $p$ 处把规范群破缺到列维子群 $\mathbb L=\TT$，在几何一侧这恰是「丛在 $p$ 处带抛物结构」。于是「带分歧平坦丛」翻译成「抛物希格斯丛」，四维面算符的参数就成了抛物权重，这正是整套对应能在 $C$ 上逐点记账的原因。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §4.2；印刷页 [83, 86] / PDF 页 [84, 87]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s04a-branes.tex:73-210`
- §4.2 见 PDF 第 84 页起（印刷第 83 页起），至印刷第 86 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
