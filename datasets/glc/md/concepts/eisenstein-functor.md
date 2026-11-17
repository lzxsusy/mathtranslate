---
id: glc/concept/eisenstein-functor
type: concept
track: F
---

# Eisenstein 函子与谱侧的幂零修正

> 自守侧 $\operatorname{Eis}_{P,!}=p_!q^*$ 有连续右伴随 $\operatorname{CT}_{P,*}=q_*p^!$；谱侧朴素函子没有，须改用幂零 ind-凝聚版本。

**问题**：为什么谱侧朴素的 $\check p_*\check q^*$ 不满足自守侧那样的伴随关系？

## 定义

令 $P\subset G$ 为抛物子群，Levi 商为 $M$。自守侧有 $\operatorname{Bun}_P$ 及投影 $p:\operatorname{Bun}_P\to\operatorname{Bun}_G$、$q:\operatorname{Bun}_P\to\operatorname{Bun}_M$，以及 Eisenstein 函子 $\operatorname{Eis}_{P,!}:=p_!q^*:\operatorname{DMod}(\operatorname{Bun}_M)\to\operatorname{DMod}(\operatorname{Bun}_G)$；它的连续右伴随是常数项函子 $\operatorname{CT}_{P,*}:=q_*p^!:\operatorname{DMod}(\operatorname{Bun}_G)\to\operatorname{DMod}(\operatorname{Bun}_M)$。因此自守侧的形式体系在取伴随时是稳定的。谱侧图表是 $\operatorname{LocSys}_{\check P}$ 带 $\check p,\check q$；朴素的函子 $\check p_*\check q^*:\operatorname{QCoh}(\operatorname{LocSys}_{\check M})\to\operatorname{QCoh}(\operatorname{LocSys}_{\check G})$ 没有所需的连续右伴随，障碍在于 $\check p$ 的真性足以保证它保持凝聚层，但它并不保持完美复形。恰当的修正正是采用幂零 ind-凝聚范畴：示意地，$\operatorname{Eis}^{\mathrm{spec}}_{\check P}:=(\check p)_*^{\operatorname{IndCoh}}\circ\check q^!$。

*记号*：$\check P\subset\check G$ 是对偶抛物子群，$\check M$ 是其 Levi 商；$(\check p)_*^{\operatorname{IndCoh}}$ 表示在 ind-凝聚层上取的推前；$\operatorname{Perf}$ 是完美复形范畴。

## 要点

- 自守侧：$\operatorname{Eis}_{P,!}:=p_!q^*$，其连续右伴随是 $\operatorname{CT}_{P,*}:=q_*p^!$。
- 自守侧的形式体系在取伴随时稳定，这是它可用作模板的原因。
- 谱侧朴素函子 $\check p_*\check q^*$ 没有所需的连续右伴随，障碍是 $\check p$ 保持凝聚层但不保持完美复形。
- 修正后的谱 Eisenstein 函子为 $\operatorname{Eis}^{\mathrm{spec}}_{\check P}:=(\check p)_*^{\operatorname{IndCoh}}\circ\check q^!$。
- 它把 Levi 侧的完美对象送进幂零奇异支撑：$\operatorname{Eis}^{\mathrm{spec}}_{\check P}(\operatorname{Perf}(\operatorname{LocSys}_{\check M}))\subset\operatorname{Coh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$。
- $\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$ 由所有 Levi 子群 $\check M$（含 $\check M=\check G$）对应的这类对象生成，故幂零条件不能任意舍弃。

## 关键公式

- $\operatorname{Eis}_{P,!}:=p_!q^*:\operatorname{DMod}(\operatorname{Bun}_M)\longrightarrow\operatorname{DMod}(\operatorname{Bun}_G),\qquad\operatorname{CT}_{P,*}:=q_*p^!$
- $\operatorname{Eis}^{\mathrm{spec}}_{\check P}:=(\check p)_*^{\operatorname{IndCoh}}\circ\check q^!,\qquad \operatorname{Eis}^{\mathrm{spec}}_{\check P}(\operatorname{Perf}(\operatorname{LocSys}_{\check M}))\subset\operatorname{Coh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$

## 定理与证明

### 谱 Eisenstein 的像落在幂零支撑内（§10.4）（要点（有缺口））

$\operatorname{Eis}^{\mathrm{spec}}_{\check P}(\operatorname{Perf}(\operatorname{LocSys}_{\check M}))\subset\operatorname{Coh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$；且 $\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$ 由所有 Levi 子群 $\check M$ 对应的这类对象生成，其中包括 $\check M=\check G$。

1. 把自守侧的伴随对 $(\operatorname{Eis}_{P,!},\operatorname{CT}_{P,*})$ 翻到谱侧，用 $\check p$ 的真性处理凝聚层。  
   *为什么*：$\check p$ 足以保持凝聚层，这一步在 $\operatorname{QCoh}$ 层面可行。
2. 把 $\check p_*$ 换成 $(\check p)_*^{\operatorname{IndCoh}}$、$\check q^*$ 换成 $\check q^!$，使函子落在幂零 ind-凝聚范畴里。  
   *为什么*：朴素版本坏在完美复形上，$\operatorname{IndCoh}$ 版本恰好修补这一点。

> 缺口：讲义用“示意地”给出该函子，未证明包含关系与生成性；完整陈述与证明见 [AG15]。

*出处*：§10.4 / 原书 p.55


## 易错点

- 朴素 $\check p_*\check q^*$ 的毛病很具体：$\check p$ 的真性只保证保持凝聚层，不保证保持完美复形——所以修正是换范畴（改用 $\operatorname{IndCoh}$），不是只换记号。
- 自守侧的右伴随是连续右伴随 $\operatorname{CT}_{P,*}=q_*p^!$，不是 $\operatorname{Eis}_{P,!}$ 的左伴随；“在取伴随时稳定”指的是这一对。
- 幂零条件不是可选项：生成性用到所有 Levi（含 $\check M=\check G$），去掉它就得不到整个 $\operatorname{IndCoh}_{\mathrm{Nilp}}(\operatorname{LocSys}_{\check G})$。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§10.4 相容性检验二：Eisenstein 级数，p.55（PDF p.55），`§10.4 相容性检验二：Eisenstein 级数（ch10.tex:88-106，p.55）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Eisenstein+series — 页面讲模形式中的 Eisenstein 级数 G_{2k} 及其与 j-不变量、Witten 亏格的关系，不含 Bun_P 上的 Eis_{P,!}=p_!q^*、CT_{P,*}=q_*p^!，也不含谱侧 Eis^spec=(p̂)_*^{IndCoh}∘q̂^! 或 Coh_Nilp 像。
- arXiv：https://arxiv.org/abs/2405.03599 — 摘要讲自守→谱侧函子、各形式等价与 Hecke 特征层的结构性质，未给 Eisenstein 函子、其连续右伴随或「像落在 Coh_Nilp」的陈述。

## 关联

- `glc/concept/categorical-langlands-conjecture`
- `glc/concept/tempered-categorical-conjecture`
- `glc/concept/nilpotent-singular-support`
