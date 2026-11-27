---
case: D27-12
id: sy38/concept/tamagawa-number
set: sy0238
group: daily-2026-11-27
severity: minor
confirmed_by: lead（2026-11-27 当日核验）
modes: 归因或作者错误
---

# 案例 D27-12 · 玉河数：Weil 猜想的完成者写成了一个不存在的合作者

> **卡片**：`sy38/concept/tamagawa-number`<br>
> **路径**：`datasets/sy0238/cards/concepts/tamagawa-number.json`<br>
> **判定**：minor；确认者 lead（当日核验）<br>
> **失效模式**：归因或作者错误<br>
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `key_points[1]`

**错误版本（卡上原文）**

```text
$\tau(\mathrm{SL}_n)=1$ 属于 Weil 猜想的一类情形（Langlands 证 $\mathrm{SL}_2$，一般情形后来由 Lai–Kunnemann 等完成）；原文只引 [Col11, Appendix B] 与 [Lur, Lecture 1]。
```

**正确版本（已替换）**

```text
$\tau(\mathrm{SL}_n)=1$ 是 Weil 猜想（单连通半单群的 Tamagawa 数=1）的特例：Langlands 证分裂情形，Rapoport 与 Lai 推广到拟分裂情形，Kottwitz（1988）用 Arthur 迹公式完成数域一般情形；原文只引 [Col11, Appendix B] 与 [Lur, Lecture 1]。
```

改动理由：史实归属错误：Weil 猜想数域情形由 Langlands（分裂）→ Rapoport/Lai（拟分裂）→ Kottwitz 1988（一般）完成，没有「Lai–Künnemann」这一完成链。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

`key_points[1]` 想说明 τ(SL_n)=1 是 Weil 猜想的特例，却把「一般情形」的完成者写成「Lai–Künnemann」。
标准史实是：Langlands（1966）证分裂情形，Rapoport（1976）与 Lai（1980）把证明改写到拟分裂情形，
Kottwitz（1988, Annals 127）用 Arthur 迹公式完成数域上的一般情形；函数域情形后来由 Gaitsgory–Lurie（2019）解决。
公开文献里没有「Lai–Künnemann」这条完成链：Künnemann 的公开著作目录（Regensburg）以 Arakelov 几何为主，
未见 Tamagawa 数的工作。这是把两个人名拼成一个不存在的合作者的「归因幻觉」，属历史归属错误，
不影响 τ 的定义与体积公式，故定 minor。

## 3. 怎么发现的

本轮独立复核第 8 张。首轮核验其实已在 `notes` 里写下「Lai–Künnemann 这一历史归属无法核实」，
但因「本地一手源 p.7 只讲 τ 与体积公式、未给历史」而判 pass。本轮换路径：用 Lurie 的 AWS 课程大纲、
2025 年 Pacific J. Math. 综述的引用链与 Kottwitz 1988 原文的归属交叉核对，三处都给
「Langlands（分裂）→ Rapoport/Lai（拟分裂）→ Kottwitz（数域一般）」，没有 Lai–Künnemann，遂改判 issue。

## 4. 证据锚点

- `Anschütz 2020` p.7 只给 `τ(G)` 的定义与 `τ(SL_n)=1` 的体积推论，未给完成者；卡的「原文只引 [Col11, Appendix B] 与 [Lur, Lecture 1]」本身不假。
- Lurie, *Tamagawa Numbers via Nonabelian Poincaré Duality*（AWS 课程大纲）：「When K is a number field, this conjecture was proven by Kottwitz (building on earlier work of Langlands and Lai).」（math.ias.edu/~lurie/282ynotes/syllabus.pdf）
- Pacific J. Math. 338 (2025) 综述：「first proved for split groups over number fields by Langlands [1966] … rewritten … for quasisplit groups by Rapoport [1976] and Lai [1980] … Kottwitz [1988] proved Weil's conjecture over number fields.」（msp.org/pjm/2025/338-1/pjm-v338-n1-p06-p.pdf）
- Kottwitz, *Tamagawa numbers*, Ann. of Math. 127 (1988), 629–646。

## 5. 对形式化 / Lean 的提示

τ(G) 是体积，不是定理陈述里的对象；若要形式化，陈述写成 `TamagawaNumber G = 1`（G 单连通半单），历史归属放 docstring，不要写进类型或假设。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
