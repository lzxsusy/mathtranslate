# 第 7 章 审校记录（review_ch07）

底本：张俊、祝安铜《量化辛几何导引》英文版扫描件。章范围：印刷页 172--194，
扫描 PDF p.180--p.202。下文「印刷页」= PDF 页 − 8。

记录格式：位置 / 原文 / 疑点 / 建议改法。凡在译文中**保留原文写法**者，正文相应
位置均有 `% [Tutor Note: 原文疑误——…]` 批注。

---

## 一、确认为笔误 / 记号不一致

1. **PDF p.189（印刷页 181），Reeb 场验证**
   - 原文：`ν₁(p)a₁ + ν₁(p)a₂ = 0`
   - 疑点：第二个 `ν₁(p)` 应为 `ν₂(p)`。由式 (7.11) 直接读出的是
     `ν₁(p)a₁ + ν₂(p)a₂ = 0`；否则紧接着「`ι_{R_α}dα` 在任意
     `w ∈ T_z∂X_Ω` 上消失」不成立。
   - 建议：改为 `ν₁(p)a₁ + ν₂(p)a₂ = 0`。译文保留原文并加批注。

2. **PDF p.194（印刷页 186），定理 7.2.2 的证明梗概**
   - 原文：`where Z⁴(x₁) and Z⁴(x₁) denote symplectic cylinders with widths
     x₁ and x₂`
   - 疑点：第二个 `Z⁴(x₁)` 应为 `Z⁴(x₂)`，否则与 "widths x₁ and x₂"、图 7.10
     以及 `B⁴(r) ⊂ X_Ω ⊂ Z⁴(x₁) ∪ Z⁴(x₂)` 矛盾。
   - 建议：第二个改为 `Z⁴(x₂)`。译文保留原文并加批注。

3. **PDF p.196（印刷页 188），刘维尔类的长正合列**
   - 原文：`the inclusion i: L → W induces the following long exact sequence`
   - 疑点：`W` 应为 `X`。全段其余部分（长正合列、式 (7.16) 的积分区域）均用
     `X`；`H_2(X;R)=0` 的论证也只在 `X` 上成立，`W` 未定义。
   - 建议：改为 `i: L → X`。译文按 `X` 处理并加批注。

4. **PDF p.199（印刷页 191），命题 7.3.1 的证明**
   - 原文：新面积类第二个分量印作
     `Ω(e₂) − a(Ω(e₁) − Ω(e₂))`
   - 疑点：与紧接其前的 `aΩ(e₁) + (1−a)Ω(e₂)` 不符；按后者应为
     `Ω(e₂) − a(Ω(e₂) − Ω(e₁))`。只有修正后的形式才能推出原文下一不等式
     `Ω(e₂) − a(Ω(e₂)−Ω(e₁)) ≥ 2(Ω(e₁) − a(Ω(e₂)−Ω(e₁)))` 及结论
     `a ≥ Ω(e₁)/(Ω(e₂)−Ω(e₁)) − 1`。
   - 建议：改为 `Ω(e₂) − a(Ω(e₂) − Ω(e₁))`。译文保留原文并加批注。

5. **PDF p.195（印刷页 187），人名**
   - 原文：`J. C. Sikarov [208-209]`
   - 疑点：通行拼写为 Jean-Claude Sikorav（J.-C. Sikorav）。
   - 建议：正文改用「Sikorav」，缩写可作 `J.-C. Sikorav`。译文已按通行拼写
     处理并加批注。

6. **PDF p.191（印刷页 183），定义 7.2.2 (iii)**
   - 原文：`(see the third picture in See Figure 7.6)`
   - 疑点：`in See` 重复（`in` 与 `See` 并存）。
   - 建议：改为 `(see the third picture in Figure 7.6)`。

7. **PDF p.197（印刷页 189），例 7.3.2**
   - 原文：`For pair (r,s) = (1,2), it's hard to` ⏎ `if L = S¹(1)×S¹(2) or …`
   - 疑点：`hard to` 与下一行 `if` 之间显然缺一个动词（应为 `tell` 或
     `distinguish`），系排版/校对付印遗漏。
   - 建议：补为 `it's hard to distinguish if …`。译文按语义译为「很难分辨……」，
     并加批注。

## 二、语法 / 用词瑕疵（不影响数学内容）

8. **PDF p.186（印刷页 178），7.1 节末**
   - 原文：`the Floer homology applied to a Liouville domains in (an open)
     Liouville manifold`
   - 疑点：`a … domains` 单复数不一致。
   - 建议：改为 `a Liouville domain in …` 或 `Liouville domains in …`。

9. **PDF p.193（印刷页 185），例 7.2.6**
   - 原文：`T_min is obtained by the simple closed Reeb orbit occurs at the
     torus fiber μ⁻¹((ε,ε))`
   - 疑点：`is obtained by … occurs` 句法混乱。
   - 建议：改为 `T_min is attained by the simple closed Reeb orbit that occurs
     at the torus fiber μ⁻¹((ε,ε))`。译文按语义译为「由……给出」。

10. **PDF p.199（印刷页 191），命题 7.3.1 的证明开头**
    - 原文：`by subtracting an appropriate many e₁ to e₂`
    - 疑点：`an appropriate many` 与 `subtracting … to` 均不规范。
    - 建议：改为 `by subtracting an appropriate number of e₁ from e₂`。

11. **PDF p.197（印刷页 189），例 7.3.2**
    - 原文：`For pair (r,s) = (1,2)`
    - 疑点：缺冠词。
    - 建议：`For the pair (r,s) = (1,2)`。

## 三、体例说明（非原文错误）

12. **「Fact」环境**：导言区未定义 `wfact`。按本项目既有做法（参见 ch02/ch06），
    正文用 `\whead{事实}{编号}` 手工排版，编号与原文（事实 7.1.1、事实 7.3.1）
    保持一致，正文交叉引用统一作「事实 7.x.x」。

13. **环面凹 / 环面凸的命名**：原文 Definition 7.2.2 的命名与轮廓曲线的凸凹
    **相反**（toric concave 的轮廓曲线是凸曲线，toric convex 的反而是凹曲线），
    并非笔误，但极易误译误读。译文照原文保留「环面凹/环面凸」，并在定义后加
    Tutor Note 明确提示。

14. **图 7.2 与图 7.6 的互引**：p.178 原文写「其矩映射像（见图 7.6 最右图）」之处
    指的是图 7.6 最右（单调）图；但图 7.6 实际在 p.183 才出现，属前向引用，
    译文照译未改。

## 四、核查清单（逐符号）

- (7.1)--(7.8)：Floer 延拓映射、作用量偏移、过滤移位，已与 PDF p.181--p.185
  逐符号核对；注意 (7.6) 左端为 `A_{H₁} − A_{H₂}`（与 (7.5) 方向相反），(7.7)
  在 `H₁ ≥ H₂` 时给出过滤保持，均已核对。
- (7.9)--(7.14)：环面区域、矩映射像、Reeb 场、周期、容量判据，已与 PDF
  p.186--p.192 逐符号核对。`ν_i(p)p_i` 的因子 2、周期公式中的 `λ_pν_i(p)`、
  「坐标轴交点轨道周期 = 截距 × π」均已在批注中说明来历。
- (7.15)--(7.16)：刘维尔类与长正合列，已与 PDF p.195--p.196 逐符号核对；
  连接和记号按原文用 `Σ₁#Σ̄₂`（译文中为 `\#`）。
- 定理 7.3.1 的四个形状不变量公式：已与 PDF p.200 放大逐符号核对（含
  `x₂ ≥ 2x₁`、`x₁ < R/3`、`a > x₁ ≥ a/2`、`b/a ∈ N_{≥2}` 等边界条件）。
