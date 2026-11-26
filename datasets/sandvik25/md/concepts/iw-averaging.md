# IW 平均函子 $\mathrm{Av}^{\mathrm{IW}}$（定理 4.4.1）

> `sandvik25/concept/iw-averaging` · 轨道 C · Iwahori–Whittaker 侧 · 状态 dev

> **先自测**：平均函子为什么是 $t$-正合的，全忠实性又靠什么截面？

## 一句话

$\mathrm{Av}^{\mathrm{IW}}(\mathcal F)=\Delta^{\mathrm{IW}}_0\star_I\mathcal F$ 是反常 $t$-正合的，且在反常层上穿过反球商，给出全忠实函子 $\mathcal P_I^{\mathrm{asph}}\hookrightarrow\mathcal P_{\mathrm{IW}}$。

## 定义

定义 $\mathrm{Av}^{\mathrm{IW}}\colon\mathcal D^b(I\backslash\mathrm{Fl}_G)\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$，$\mathcal F\mapsto\Delta^{\mathrm{IW}}_0\star_I\mathcal F$。定理 4.4.1（[ArBe]）：(1) $\mathrm{Av}^{\mathrm{IW}}$ 是反常 $t$-正合的；(2) 其限制到 $\mathcal P_I$ 上穿过一个全忠实函子 $\mathcal P_I^{\mathrm{asph}}\to\mathcal P_{\mathrm{IW}}$。

**记号**：$\Delta^{\mathrm{IW}}_0$ 是权 $0$ 的标准层；$\star_I$ 为 §4.2 的右卷积。

## 要点（为什么需要它）

1. 两条计算式是全部证明的支点：(5) $\mathrm{Av}^{\mathrm{IW}}(\mathrm{IC}_w)=0$ 除非 $w\in\widetilde W_{\mathrm{ext}}$；(6) $\mathrm{Av}^{\mathrm{IW}}(\Delta_w)\cong\Delta^{\mathrm{IW}}_\lambda$、$\mathrm{Av}^{\mathrm{IW}}(\nabla_w)\cong\nabla^{\mathrm{IW}}_\lambda$，其中 $\lambda$ 由 $W\cdot w=W\cdot w_\lambda$ 唯一确定。
2. (5) 直接给出 (2) 的「穿过反球商」：被杀掉的正是 $w\notin\widetilde W_{\mathrm{ext}}$ 的单层。
3. (6) 给出 $t$-正合性：标准层与余标准层都映到标准层与余标准层，于是反常 $t$-结构逐层对齐。
4. 全忠实性的证明是「造截面」：从 $I\cap I_u^+$-等变平均到 $I$-等变、取反常上同调、再套反球商函子；原文只说「直观上如此」。

## 核心公式

$$
$\mathrm{Av}^{\mathrm{IW}}\colon\mathcal D^b(I\backslash\mathrm{Fl}_G)\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G),\quad \mathcal F\mapsto\Delta^{\mathrm{IW}}_0\star_I\mathcal F$$\mathrm{Av}^{\mathrm{IW}}(\mathrm{IC}_w)=0\ (w\notin\widetilde W_{\mathrm{ext}}),\qquad \mathrm{Av}^{\mathrm{IW}}(\Delta_w)\cong\Delta^{\mathrm{IW}}_\lambda,\ \mathrm{Av}^{\mathrm{IW}}(\nabla_w)\cong\nabla^{\mathrm{IW}}_\lambda$
$$

$$
$\mathrm{Av}^{\mathrm{IW}}(\mathrm{IC}_w)=0\ (w\notin\widetilde W_{\mathrm{ext}}),\qquad \mathrm{Av}^{\mathrm{IW}}(\Delta_w)\cong\Delta^{\mathrm{IW}}_\lambda,\ \mathrm{Av}^{\mathrm{IW}}(\nabla_w)\cong\nabla^{\mathrm{IW}}_\lambda$
$$

## 定理与证明（或缺口）

### 定理 4.4.1（Arkhipov–Bezrukavnikov）

$\mathrm{Av}^{\mathrm{IW}}$ 反常 $t$-正合；其在 $\mathcal P_I$ 上的限制穿过全忠实函子 $\mathcal P_I^{\mathrm{asph}}\to\mathcal P_{\mathrm{IW}}$。

> 证明状态：**sketch**。第 1、3 步都只有概述；本译本把「截面构造」标为待补细节。

出处：`A p.10`

## 常见误解

- 把 $\mathrm{Av}^{\mathrm{IW}}$ 当成 $\mathcal D^b(I\backslash\mathrm{Fl}_G)$ 到自身的投影：它的终点是 IW 范畴，等变性被替换掉了。
- 式 (6) 里的 $\lambda$ 由「$W\cdot w=W\cdot w_\lambda$」唯一确定，不是 $w$ 本身的下标；同一双边胞腔里的不同 $w$ 会映到同一个 $\lambda$。

## 相关卡

[IW 反常层的最高权结构（命题 4.3.1）](../concepts/iw-highest-weight.md) · [反球商 $\mathcal P_I^{\mathrm{asph}}$](../concepts/antispherical-quotient.md) · [平均函子为什么 $t$-正合：式 (5)(6) 的用法](../derivations/iw-averaging-t-exact.md)

## 出处（印刷页）

- A p.10（A p.10）

> 说明：§4.4 与定理 4.4.1 的证明梗概全在 p.10，公式编号 (5)(6) 同页。
