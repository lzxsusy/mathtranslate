# 命题 6.4.2：三种扭化版本在仿射上逐点相等

> `cdm14/deriv/twist-three` · 轨道 F · 扭化 · 状态 dev · 4 步

> **要回答的问题**：为什么只需在仿射 DG 概形上验证？

## 一句话

只在 $S\in\DGSch_{\mathrm{aff}}$ 上算：把核写成纤维积，再用引理 6.3.10 与指数映射把三个版本对齐。

## 目标

证明图 (6.2) 中 $\mathrm{Tw}^{\mathrm{/red}}_a\to\mathrm{Tw}^{\mathrm{/red}}$、$\mathrm{Tw}^{\mathrm{/red}}\to\mathrm{Tw}$、$\mathrm{Tw}_a\to\mathrm{Tw}$ 都是等价。

## 前提

- $\mathrm{Tw}(Y)=\ker(p^*_{\mathrm{dR},Y})$。
- 引理 6.3.10：$\mathbf{Ge}^{\mathrm{/red}}_{\mathbb G_m}(Y)\simeq\ker(\mathbf{Ge}_{\mathbb G_m}(Y)\to\mathbf{Ge}_{\mathbb G_m}({}^{\mathrm{cl,red}}Y))$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 三个函子都是沿 $(\DGSch_{\mathrm{aff}})^{\mathrm{op}}\to(\PreStk)^{\mathrm{op}}$ 的右 Kan 延拓，故只需在 $S\in\DGSch_{\mathrm{aff}}$ 上比较。 | 右 Kan 延拓逐对象计算。 | `A p.54` | A·原文明确写了 |
| 2 | 在 $S$ 上把 $\mathrm{Tw}^{\mathrm{/red}}(S)$ 写成 $\mathbf{Ge}^{\mathrm{/red}}_{\mathbb G_m}(S_{\mathrm{dR}})\times_{\mathbf{Ge}^{\mathrm{/red}}_{\mathbb G_m}(S)}\{*\}$。 | 核的定义。 | `A p.54` | A·原文明确写了 |
| 3 | 用引理 6.3.10 把 $\mathbf{Ge}^{\mathrm{/red}}$ 换成 $\ker(\mathbf{Ge}\to\mathbf{Ge}({}^{\mathrm{cl,red}}))$，再与 $\mathrm{Tw}$ 的核逐项比较。 | 两个核相同。 | `A p.54` | B·原文暗示、我们补的中间步 |
| 4 | $\mathbb G_a$ 版本由指数映射 $\exp$ 同构（[GR1, 6.8.8]）。 | 既约部分上 $\exp$ 可逆。 | `A p.54` | B·原文暗示、我们补的中间步 |

## 结论

$\mathrm{Tw}^{\mathrm{/red}}_a\simeq\mathrm{Tw}^{\mathrm{/red}}\simeq\mathrm{Tw}_a\simeq\mathrm{Tw}$。

## 缺口

- 第 3 步「两个核相同」需要把 $S_{\mathrm{dR}}$ 与 ${}^{\mathrm{cl,red}}S$ 的关系理清，原文用一段计算完成，此处只记结构。

## 最容易讲错的地方

- 不能在一般预栈上直接算：右 Kan 延拓的论证只保证仿射上相等，再借延拓唯一性。
- $\exp$ 只在既约部分可逆，不能对 $S$ 整体用。

## 相关卡

[$\mathbb G_m$-gerbe 与 $\mathbf{Ge}_{\mathbb G_m}$](../concepts/gm-gerbe.md) · [扭化 $\mathrm{Tw}(Y)$](../concepts/twisting.md)

## 出处（印刷页）

- A p.54（A p.54）

> 说明：A=命题 6.4.2 的证明；B=引理 6.3.10 与 [GR1, 6.8.8]；最没把握处：第 3 步的核比较。
