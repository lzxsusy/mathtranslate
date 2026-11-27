---
case: D27-07
id: lbook04/concept/ch9-langlands-spectral
set: lbook04
group: daily-2026-11-27
severity: minor
confirmed_by: lead（2026-11-27 当日核验）
modes: 内部不一致 / 证据归属错误
---

# 案例 D27-07 · Langlands 谱：带扭时的极点位置

> **卡片**：`lbook04/concept/ch9-langlands-spectral`<br>
> **路径**：`datasets/lbook04/cards/concepts/ch9-langlands-spectral.json`<br>
> **判定**：minor；确认者 lead（当日核验）<br>
> **失效模式**：内部不一致 / 证据归属错误<br>
> **施工日期**：2026-11-27

## 1. 正误对比

### 1.1 字段 `key_points[2]`

**错误版本（卡上原文）**

```text
留数非零 $\Rightarrow$ 存在 $\mathrm{GL}_n(\mathbb{A})$-不变配对 $\Rightarrow$ $\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}$；反过来该条件也保证 $s=1$ 处有极点（定理 4.2 后的两条观察）。
```

**正确版本（已替换）**

```text
留数非零 $\Rightarrow$ 存在 $\mathrm{GL}_n(\mathbb{A})$-不变配对 $\Rightarrow$ $\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}$；反过来该条件保证在 $s=-i\sigma$ 与 $s=1-i\sigma$ 处有单极点（$\sigma=0$ 时即 $s=1$；定理 4.2 后的两条观察是未扭情形）。
```

改动理由：Thm 4.2 给的是 s=−iσ 与 s=1−iσ 处的极点，只有 σ=0 才化为 s=1；后续两条 observation 是未扭（π×π̃）情形。

## 2. 为什么会错

> 这是从错误形态反推的失效模式，不是原始模型的私有思维链。

`key_points[2]` 说「反过来该条件也保证 s=1 处有极点」，但带 |det|^{iσ} 扭时 Thm 4.2 的极点在
s=−iσ 与 s=1−iσ，只有 σ=0 才退化成 s=1（卡自己的 `definition` 写的就是这对位置）。
另外它把「留数非零 ⇒ π ≅ π̃′⊗|det|^{iσ} 的反向」挂到「Thm 4.2 后的两条观察」，
而那两条观察是未扭情形（s=0,1 的单极点、以及 π≅π′ 的判据），反向陈述出自 Thm 2.2 的证明（印刷 p.210）。

## 3. 怎么发现的

当日核验第 13 张。子代理对照 PDF p.225（印刷 222）Thm 4.2 的极点句与紧随的两条观察，lead 复核了
「s = -ia and s = 1- ia」与「simple poles at s = 0 and s = 1」两处引文（该 PDF 文本层把 π 抽成 rr/1i）。

## 4. 证据锚点

- `bernstein_gelbart_introduction.pdf` p.222（PDF 225）：「then at s = -ia and s = 1- ia.」
- 同页：「1. L(s, rr x 1i) has simple poles at s = 0 and s = 1.」（rr/1i 为 π 的抽取乱码）

## 5. 对形式化 / Lean 的提示

形式化留数配对时，极点位置应参数化为 `s = -iσ` 与 `s = 1 - iσ`；σ=0 只是特例，不能写死 s=1。

## 6. 防再犯检查

- [x] 改前在本案例集与 `11_card_audit/casebook/` 搜过同 id / 同字段。
- [x] 页码改动已同时核对 PDF 页与印刷页，并附逐字引文。
- [x] 符号 / 措辞改动已同步 md、生成器与 `verification` 中的旧定位。
- [x] 改后 `json.load` 通过、`verify_final.py` 全量 0 parse error、`git diff --check` 干净。
