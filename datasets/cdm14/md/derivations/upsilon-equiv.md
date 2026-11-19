# 命题 2.4.4 的证明：逐层 $\Upsilon$ 拼成全化上的等价

> `cdm14/deriv/upsilon-equiv` · 轨道 B · 左/右晶体、IndCoh 与 Kashiwara · 状态 dev · 4 步

> **要回答的问题**：为什么 $\Upsilon$ 在一般 $Y$ 上仍是等价，而不是只在光滑 $Y$ 上？

## 一句话

把一般 $Y$ 化到「仿射 $X$ 在光滑 $Z$ 中的形式完备化」，两边都用 Čech 全化，逐层用光滑情形的 $\Upsilon$ 等价。

## 目标

证明 $\Upsilon_{Y_{\mathrm{dR}}}:\Crys^l(Y)\to\Crys^r(Y)$ 对 $Y\in\PreStk_{\mathrm{laft}}$ 是等价。

## 前提

- 引理 2.1.7 与 2.3.11：经典形式光滑时 $\Crys^l(Y)\simeq\mathrm{Tot}(\QCoh(Y_\bullet/Y_{\mathrm{dR}}))$、$\Crys^r(Y)\simeq\mathrm{Tot}(\IndCoh(Y_\bullet/Y_{\mathrm{dR}}))$。
- 命题 2.5.6（Kashiwara）把仿射 $X$ 换成它在光滑 $Z$ 中的形式完备化。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 由 Kashiwara 与仿射性，只需处理 $Y$ 为仿射 $X$ 在光滑 $Z$ 中的形式完备化。 | 一般 $Y$ 可由形式完备化逼近，而 $\Crys$ 是极限。 | `A p.22` | A·原文明确写了 |
| 2 | 把 $\Upsilon_{Y_{\mathrm{dR}}}$ 写成 $\mathrm{Tot}(\Upsilon_{Y_\bullet/Y_{\mathrm{dR}}})$：两边限制到 Čech 神经的每一项。 | 全化是极限，$\Upsilon$ 与极限交换。 | `A p.22` | A·原文明确写了 |
| 3 | 每一项 $Y_i/Y_{\mathrm{dR}}$ 是主对角线的形式完备化，在其上用 [GR1, Diagram (7.16)] 的短正合列把 $\QCoh$ 与 $\IndCoh$ 的张量 $\omega$ 化。 | 形式完备化的 $\QCoh$ 是 $\ker(j^*)$，$\IndCoh$ 是 $\ker(j^!)$，两者由 $\otimes\omega$ 联系。 | `A p.22` | B·原文暗示、我们补的中间步 |
| 4 | 逐层等价的全化仍是等价。 | $\mathrm{Tot}$ 是极限，等价在极限下保持。 | `A p.22` | A·原文明确写了 |

## 结论

$\Upsilon_{Y_{\mathrm{dR}}}$ 是等价，故 $\Crys^l(Y)$ 与 $\Crys^r(Y)$ 可视为同一范畴的两个实现。

## 缺口

- 第 3 步的短正合列来自 [GR1, Diagram (7.16)] 与命题 7.1.3/7.4.5，本文只引用未复述，条件（最终余连接、闭浸入）需另查。

## 最容易讲错的地方

- 全化保等价用的是「极限保持等价」，不是「余极限」——写反会得到相反结论。
- 第 1 步的归约依赖 Kashiwara 的等价与 $\Crys$ 对开覆盖的下降，两件事都要先证。

## 相关卡

[$\Upsilon$：左晶体与右晶体的比较](../concepts/upsilon-comparison.md) · [Kashiwara 引理：闭浸入上的晶体即开补上为零的晶体](../concepts/kashiwara.md) · [左晶体：$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$](../concepts/left-crystal.md) · [右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md)

## 出处（印刷页）

- A p.22（A p.22）

> 说明：A=命题 2.4.4 的证明；B=[GR1] 的短正合列；最没把握处：第 3 步「张量 ω 化」的准确形式。
