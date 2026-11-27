---
case: D27-05
id: ggl09/deriv/descent-to-xi
set: ggl09
group: daily-2026-11-27
severity: major
confirmed_by: lead（2026-11-27 当日核验）
modes: 逻辑方向反转 / 出处定位漂移
---

# 案例 D27-05 · 下降给出 x_i(S)：边界的「差」取反了

> **卡片**：`ggl09/deriv/descent-to-xi`<br>
> **路径**：`datasets/ggl09/cards/derivations/descent-to-xi.json`<br>
> **判定**：major；确认者 lead（当日核验）<br>
> **失效模式**：逻辑方向反转 / 出处定位漂移<br>
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `steps[4].text`

**错误版本（卡上原文）**

```text
取 $S$ 为固定时刻的曲面，则 $x_i(S)$ 是作用在 $\mathcal H$ 上的算符；在右边界 Dirichlet 处 $A,\psi,\sigma$ 全为零，$x_i=0$，非零贡献在 Neumann 边界与环绕 $w$ 的小 $S^2$ 之差；该差给出 $H^{2d_i-2}(N(\rho))$ 中的 $x_i$，即杯积算符。
```

**正确版本（已替换）**

```text
取 $S$ 为固定时刻的曲面，则 $x_i(S)$ 是作用在 $\mathcal H$ 上的算符；右边界（Dirichlet）上 $A,\psi,\sigma$ 全为零，故该处 $x_i=0$；左边界（Neumann）与右边界之差同调于环绕 $w$ 的小 $S^2$，所以非零贡献来自左边界，且等于 $x_i$ 在小 $S^2$ 上的值，它给出 $H^{2d_i-2}(N(\rho))$ 中的 $x_i$，即杯积算符。
```

改动理由：原文 p.16–17 说差分的是「左(Neumann)与右(Dirichlet)边界」，该差同调于小 S²；卡写成「Neumann 与小 S² 之差」，而这个差正是 x_i=0 的右边界，方向反了。

### 1.2 字段 `steps[4].locator`

**错误版本（卡上原文）**

```text
A p.16 eq (2.10)
```

**正确版本（已替换）**

```text
A p.16–17 eq (2.10)
```

改动理由：该步后半（左/右边界、同调于小 S²）在 p.17；locator 只到 p.16，与已改写的 step text 不匹配。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

原文说：S²×I 的**左（Neumann）与右（Dirichlet）边界之差**同调于环绕 w 的小 S²，且右边界上 x_i=0，
所以 x_i(Neumann)=x_i(S²)。推导步骤 5 却写成「Neumann 边界与小 S² 之差」——这个差恰好同调于**右边界**，
而右边界的 x_i=0，不可能「该差给出 x_i」。方向一取反，整步论证就断了。
失效点在于把「A 与 B 之差 ≅ C」误读成「A 与 C 之差 ≅ B」；三个对象两两成链时，谁减谁决定了 nonzero 落在哪。
另外 `steps[4].locator` 原写「A p.16 eq (2.10)」，只覆盖该步开头（取固定时刻的曲面）；
左/右边界与小 S² 的论证在 p.17，故本轮把 locator 一并扩为 p.16–17。

## 3. 怎么发现的

当日核验第 6 张。子代理核对 arXiv:0905.4795v2 p.16–17 的相对同调论证时发现边界顺序与卡相反；
lead 用 `ggl09.txt` 重读 p.16「the left and right boundaries … is homologous to a small two-sphere」确认。
本轮独立复核顺手核 `steps[4].locator`：它只写到 p.16（该步开头的固定时刻曲面），而左/右边界论证已跨到 p.17，
故同批把 locator 扩为 p.16–17。

## 4. 证据锚点

- `ggl09.pdf`/arXiv p.16：「the difference between the left and right boundaries of S² × I is homologous to a small two-sphere that links w」；p.16 另述右边界 Dirichlet 上 x_i=0。

## 5. 对形式化 / Lean 的提示

形式化时用相对同调 `H_2(S²×I, ∂) ≅ H_1(S¹)` 或链群 `C_2(S²×I)/C_2(∂)`；边界条件进入相对链群，`x_i(right)=0` 应作为假设显式写出。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
