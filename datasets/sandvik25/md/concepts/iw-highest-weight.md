# IW 反常层的最高权结构（命题 4.3.1）

> `sandvik25/concept/iw-highest-weight` · 轨道 C · Iwahori–Whittaker 侧 · 状态 dev

> **先自测**：最高权结构是怎么从轨道参数化得到的，倾斜层为什么必须存在？

## 一句话

$I_u^+$-轨道由 $W_{\mathrm{ext}}$ 参数化，其中只有 $\widetilde W_{\mathrm{ext}}$ 上的轨道承载非零 Whittaker 局部系统；据此定义 $\Delta^{\mathrm{IW}}_\lambda,\nabla^{\mathrm{IW}}_\lambda,\mathrm{IC}^{\mathrm{IW}}_\lambda$，得权偏序集为 $X^\vee$ 的最高权范畴，从而有不可分解倾斜层 $T^{\mathrm{IW}}_\lambda$。

## 定义

$I_u^+$ 在 $\mathrm{Fl}_G$ 上的轨道由 $W_{\mathrm{ext}}$ 参数化，且有双射 $X^\vee\leftrightarrow\widetilde W_{\mathrm{ext}}$，$\lambda\mapsto w_\lambda$。记 $\mathrm{Fl}^{\mathrm{IW}}_{G,\lambda}$ 为对应轨道、$j^{\mathrm{IW}}_\lambda$ 为其嵌入。只有 $\lambda\in X^\vee$ 对应的轨道承载唯一秩一 Whittaker 局部系统 $\mathcal L_{\chi,\lambda}$。定义 $\Delta^{\mathrm{IW}}_\lambda:=j^{\mathrm{IW}}_{\lambda!}\mathcal L_{\chi,\lambda}[\dim\mathrm{Fl}^{\mathrm{IW}}_{G,\lambda}]$、$\nabla^{\mathrm{IW}}_\lambda:=j^{\mathrm{IW}}_{\lambda*}\mathcal L_{\chi,\lambda}[\dim]$；$\mathrm{IC}^{\mathrm{IW}}_\lambda$ 为 $\Delta^{\mathrm{IW}}_\lambda\to\nabla^{\mathrm{IW}}_\lambda$ 的像。

**记号**：$\mathcal P_{\mathrm{IW}}$ 的权偏序集是 $X^\vee$；$T^{\mathrm{IW}}_\lambda$ 为唯一的不可分解倾斜层。

## 要点（为什么需要它）

1. 「只有 $\widetilde W_{\mathrm{ext}}$ 上的轨道有非零 Whittaker 局部系统」是整节的技术核心：其它轨道上的秩一层被消没性质杀掉，于是 $\mathcal P_{\mathrm{IW}}$ 的权集恰好是 $X^\vee$，与几何侧的线丛下标完全一致。
2. 偏序集是 $X^\vee$（余根格），不是 $W_{\mathrm{ext}}$：这是把「仿射 Weyl 群的组合」压成「格上的最高权理论」，也是与 $\mathrm{Rep}(G^\vee)$ 的权分解对齐的关键。
3. 最高权范畴 ⇒ 每个权有一个不可分解倾斜层（Ringel 对偶的范畴化）；推论 4.3.2 又给出 $\mathcal D^b\mathcal P_{\mathrm{IW}}\cong\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$，于是「倾斜」可以搬到导出范畴里用。
4. 标准层与余标准层都用 $!$/$*$ 扩张加 $[\dim]$ 位移：位移常数必须与 §2.5 的 $\Delta_w$、$\nabla_w$ 一致，否则定理 4.4.1(6) 的匹配会差一个平移。

## 核心公式

$$
$\Delta^{\mathrm{IW}}_\lambda=j^{\mathrm{IW}}_{\lambda!}\mathcal L_{\chi,\lambda}[\dim\mathrm{Fl}^{\mathrm{IW}}_{G,\lambda}],\qquad \nabla^{\mathrm{IW}}_\lambda=j^{\mathrm{IW}}_{\lambda*}\mathcal L_{\chi,\lambda}[\dim\mathrm{Fl}^{\mathrm{IW}}_{G,\lambda}]$$\mathrm{IC}^{\mathrm{IW}}_\lambda=\mathrm{im}(\Delta^{\mathrm{IW}}_\lambda\to\nabla^{\mathrm{IW}}_\lambda)$
$$

$$
$\mathrm{IC}^{\mathrm{IW}}_\lambda=\mathrm{im}(\Delta^{\mathrm{IW}}_\lambda\to\nabla^{\mathrm{IW}}_\lambda)$
$$

## 定理与证明（或缺口）

### 命题 4.3.1 与推论 4.3.2

$\mathcal P_{\mathrm{IW}}$ 是以 $X^\vee$ 为权偏序集的最高权范畴，故对每个 $\lambda$ 有唯一不可分解倾斜层 $T^{\mathrm{IW}}_\lambda$；且实现函子诱导等价 $\mathcal D^b\mathcal P_{\mathrm{IW}}\cong\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$。

> 证明状态：**gap**。原文只给「关键观察」，证明留给 [ArBe]；最高权结构的验证依赖轨道上的 Whittaker 局部系统分类。

出处：`A p.10`

## 常见误解

- 把 $\lambda\mapsto w_\lambda$ 当成 $X^\vee\cong W_{\mathrm{ext}}$：它只是到极小代表元集 $\widetilde W_{\mathrm{ext}}$ 的双射，陪集信息被丢掉了。
- 倾斜层 $T^{\mathrm{IW}}_\lambda$ 与标准层 $\Delta^{\mathrm{IW}}_\lambda$ 不同构：前者同时有标准滤链与余标准滤链，后者只有一侧。

## 相关卡

[Iwahori–Whittaker 范畴 $\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$](../concepts/iw-category.md) · [IW 平均函子 $\mathrm{Av}^{\mathrm{IW}}$（定理 4.4.1）](../concepts/iw-averaging.md) · [中心层的 IW 像是倾斜层（定理 4.5.1）](../concepts/central-tilting.md)

## 出处（印刷页）

- A p.10（A p.10）

> 说明：§4.3 全在 p.10；命题 4.3.1、推论 4.3.2 同页。
