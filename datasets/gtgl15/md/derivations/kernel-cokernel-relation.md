# 核与余核线丛的关系 $\mathcal L\cong\mathcal N(\mathcal R)$

> `gtgl15/deriv/kernel-cokernel-relation` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev · 4 步

> **要回答的问题**：为什么本征向量的线丛与余核的线丛不是同一个，而恰好差一个分歧除子（及其 $K^{N-1}$ 版本）？

## 一句话

用 $2\times2$ 局部模型 $\varphi\sim\bigl(\begin{smallmatrix}0&z\\1&0\end{smallmatrix}\bigr)$、$y^2=z$ 显式算出核线丛 $\mathcal N$ 与余核线丛 $\mathcal L$ 相差分歧除子：$\mathcal L\cong\mathcal N(\mathcal R)\cong\mathcal N\otimes\psi^*K^{N-1}$。

## 目标

在局部模型下计算核/余核的过渡函数，导出 $\mathcal L\cong\mathcal N(\mathcal R)\cong\mathcal N\otimes\psi^*K^{N-1}$。

## 前提

- $D\subset K$ 是谱曲线，$y$ 是 $K$ 的纤维坐标；$\varphi$ 是 $E$ 上的 Higgs 场。
- 非分歧点上方 $\varphi-y$ 的核与余核都是一维的；局部模型取 $N=2$、$\varphi\sim\bigl(\begin{smallmatrix}0&z\\1&0\end{smallmatrix}\bigr)$，$\det(y-\varphi)=y^2-z$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 在局部模型中，$\varphi-y=\bigl(\begin{smallmatrix}-y&z\\1&-y\end{smallmatrix}\bigr)$；本征向量取 $s=(y,1)$，满足 $(\varphi-y)s=0$。 | 直接用 $y^2=z$ 验证 $(\varphi-y)s=0$。 | `A p.12 eq (2.14)` | A·原文明确写了 |
| 2 | 余核由 $t=(1,0)$ 生成；写成 $s=u+2yt$ 的形式，$u=(-y,1)$ 是与核配对的余核截面。 | 这一步给出核与余核之间的显式过渡。 | `A p.12 eq (2.16)` | A·原文明确写了 |
| 3 | 过渡函数相差因子 $2y$（等价地 $y$），其零集即分歧除子 $\mathcal R$；故 $\mathcal L\cong\mathcal N(\mathcal R)$。 | 线丛的过渡函数相乘即得 twist。 | `A p.13 eq (2.21)` | A·原文明确写了 |
| 4 | $\mathcal R$ 的除子类等于 $\psi^*K^{N-1}$ 的除子类，故 $\mathcal L\cong\mathcal N\otimes\psi^*K^{N-1}$。 | $\psi$ 的分歧除子由 $K^{N-1}$ 的拉回给出。 | `A p.13 eq (2.22)` | A·原文明确写了 |

## 结论

$\mathcal L\cong\mathcal N(\mathcal R)\cong\mathcal N\otimes\psi^*K^{N-1}$。

## 缺口

- 局部模型只是 $N=2$ 的特例；一般 $N$ 的过渡函数要靠行列式/典范丛论证，原文未逐项展开。

## 最容易讲错的地方

- $\mathcal N(\mathcal R)$ 的 $\mathcal R$ 是 $D$ 上的分歧除子，不是 $C$ 上的判别式轨迹。
- $N=2$ 局部的 $y^2=z$ 不能直接搬到一般 $N$；推广要用 $\det$ 与 $K^{N-1}$。
- 核与余核都是线丛但不同：混淆它们会让阿贝尔化的推前公式错一个 twist。

## 相关卡

[核线丛与余核线丛](../concepts/kernel-cokernel.md) · [谱曲线](../concepts/spectral-curve.md) · [谱覆盖、判别式与分歧除子](../concepts/spectral-cover.md) · [阿贝尔化与 Prym 簇](../concepts/abelianization-prym.md) · [一般纤维的阿贝尔化：$F\cong\mathrm{Prym}(D/C)$](../derivations/prym-abelianization.md)

## 出处（印刷页）

- A p.11–13（A p.13 eq (2.20)）
- A p.13（A p.13 eq (2.22)）

> 说明：A4：eq (2.14)–(2.22) 的局部计算原文逐步写出；B=把“过渡函数差 $y$”翻译成 twist 的语言。最没把握处：eq (2.22) 中 $\mathcal R$ 与 $\psi^*K^{N-1}$ 的等同原文只给结论式。
