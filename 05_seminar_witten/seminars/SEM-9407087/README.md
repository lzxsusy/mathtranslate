# SEM-9407087 研讨班档案

**主文**：Seiberg–Witten, *Electric–Magnetic Duality, Monopole Condensation, and Confinement in N=2 Supersymmetric Yang–Mills Theory*, hep-th/9407087（45 页）。
**日期**：2026-11-09
**形式**：三位讲读人通读全文 → 独立报告 → 交叉质询 → 回应 → 圆桌三题 → 综合。
**一句话结论**：这是一篇“构造 + 验证 + 条件性论证”的论文，不是“第一原理推导 + 唯一性定理”；它精确到给定电荷的 BPS 质量公式，但没有给出完整 BPS 谱，也没有证明唯一性。

---

## 先读什么

1. `one_pager.md` —— 一页纸结论（5 分钟）
2. `notes.md` —— 综合笔记（30–40 分钟）
3. `transcript.md` —— 圆桌记录与裁决（20 分钟）
4. `errata.md` —— 用户备忘 M1–M12 的逐条更正、文本层错误、研讨班内部更正
5. `reports/` —— 三份独立报告（r01 物理、r02 数学、r03 文本/批判）
6. `challenges/` —— 九份质询/回应 + 三份圆桌稿 + 三份 rebuttal

---

## 目录

| 路径 | 内容 |
|---|---|
| `source/9407087v1.pdf` | 原文 45 页 |
| `source/9407087v1_中文译注.pdf` | 中译 32 页 |
| `source/pages/p001–p045.png` | 150 dpi 页图（公式核对唯一真值） |
| `source/text/p001–p045.txt` | 文字层（仅定位；p010/p012 含控制字符） |
| `source/user_notes/` | 用户三张手绘图 + `participant_memo.md`（M1–M12） |
| `map.yaml` | 章节地图、页码、核心问题、公式/图 |
| `brief.md` | 角色、硬性要求、报告格式、流程 |
| `reports/r01.md` | 物理结构与论证链（19 claims） |
| `reports/r02.md` | 数学工具与计算（26 claims） |
| `reports/r03.md` | 文本、证据与批判（33 claims） |
| `reports/rXX_response.md` | 三份逐条回应 |
| `challenges/` | 六份交叉质询 + 三份圆桌稿 + 三份 rebuttal |
| `transcript.md` | 圆桌记录、三题裁决、M1–M12 摘要 |
| `notes.md` | 综合笔记（含正调和函数引理、证据分级表） |
| `errata.md` | 更正清单（M1–M12、E1–E12） |
| `claims/merged.jsonl` | 20 条合并 claim（含锚点/状态/置信度） |
| `questions/merged.jsonl` | 8 条未决问题 |
| `manifest.json` | 文件清单、hash、页数、完成状态 |

---

## 六条关键结论

1. **三个奇点是定理（给定标准事实）**：若单值性阿贝尔，`a²` 整体坐标，`Im τ` 是 C 去 punctures 上的正调和函数 ⇒ 常数，与 `Im τ∼(2/π)ln|a|→∞` 矛盾。
2. **“恰好两个有限奇点”与 `du≠0` 是假设**，不是定理；p24/p28/p34 明写。
3. **SW 曲线是猜出来再验证的**：`y²=(x²−1)(x−u)`、`λ=(√2/2π)dx√(x−u)/√(x²−1)`；`a,a_D` 是周期，`τ=b₁/b₂`。
4. **唯一性是 proof-gap**：p38 只有一句 Torelli 型论证；`dλ/du ∝ λ₁` 的 ansatz 必要性未证。不能写“SW 唯一确定预势”。
5. **p42 是条件性排除**：路径可证，但四维“无墙 ⇒ 谱局部常数”判据未证；p21 明说只在二维证明、四维 “would be desirable”。
6. **禁闭方向**：磁单极凝聚 → 电禁闭；`u₀` 破缺前是 N=2 QED，软破缺后才是 N=1 SQED。

---

## 研讨班增量

- **正调和函数引理**：把 M5 的“结论对、理由错”升级为定理。
- **f 常数的 ln² 排除**：r02 给出，r01/r03 接受；补上“残数抵消”的漏洞。
- **p42 口径**：条件性必要性排除，依赖三条假设。
- **唯一性缺口清单**：ansatz 必要性 + Torelli 型重合，分开列。
- **抓到硬错误**：(5.21) 根号套错、(6.6) cusp 映射错、`map.yaml` figures 错、`core.md` 9701069 误标。

---

## 复用为模板

把本目录复制为 `seminars/SEM-<id>/`，替换：
1. `source/` 的 PDF、页图、文字层；
2. `seminar.yaml`、`map.yaml`、`brief.md`；
3. `source/user_notes/`（若有用户备忘/手图）；
4. 角色分工与页码区间。
流程、报告格式、质询模板、圆桌三题、验收评分表见 `<本地路径>`。