# HANDOFF：几何 Langlands 综述 v1.0.1

日期：2026-11-28 · 负责人：lead（本会话 root agent）

## 交付物

| 文件 | 说明 |
|---|---|
| `datasets/encyclopedia/pages/geometric-langlands.md` | 新综述页，790 行 / 约 84 KB；8 节 + 附录 A/B/C |
| `datasets/encyclopedia/pages/work/geometric-langlands-v0.3-2026-11-27.md` | 旧页（Laumon 2002 底本）归档，未删 |
| `datasets/encyclopedia/pages/kapustin-witten.md` | 旧导航页，保留未动（用户要求保留的两个旧页之一） |
| `datasets/encyclopedia/pages/langlands-program.md` | 旧导航页，保留未动（另一个） |
| `datasets/encyclopedia/pages/work/survey-v1/` | 起草、统稿脚本、卡表、证据抽取、两份审校报告 |

页面结构：0 导读 / 1 命题形状 / 2 陈述 / 3 为什么 / 4 具体化 / 5 证明地图 / 6 证明细节 / 7 现状；
附录 A 年表、附录 B 60 张资料卡索引、附录 C 总证明图。5 张分节 mermaid + 1 张总图。

## 机械校验（可复跑）

```bash
cd datasets/encyclopedia/pages/work/survey-v1
python check_survey.py ../../geometric-langlands.md
```

当前结果：cards 60 unique / 95 refs，missing 0；local links 73，dead 0；citation markers 202；OK。
另核：compiled_from 60 条与正文 60 张唯一卡集合完全相等；附录 B 60 行与正文卡集合完全相等。

## 审校与已修

- R1（§0–§4）报告：`work/survey-v1/reports/r1-verify-0-4.md`（30 条：P0 1 / P1 17 / P2 12）。
- R2（§5–end）报告：`work/survey-v1/reports/r2-verify-5-end.md`（260 行：P1 6 / P2 一批 / 附录与 front matter）。
- 已修：R1 的 P0（§1.4 把几何 Satake 说成「表示环＝共同谱」，改为张量范畴等价 + 联合特征值由 `Loc_Ĝ` 参数化）
  与全部 17 条 P1（含 CL23 §2.2–2.6 十处整段页码重标、L246「截面叠」错述、L348/L390/L141/L240/L292 错页）；
  R2 的 6 条 P1（BD 1996「最一般」改为仅 oper 型参数、Dolbeault `generically`、附录 C 箭头方向与 I→II/II→III/II→IV、
  「接缝重数必须一」改为编者综合）与 P2（BZ26 §5.5、定理 2.11/2.12 节号、L461/477/563/585 页码、记号 `^L_{G_m}`/`_Ran`/`ˇU^Θ`/AGKRRV、
  §5.2 页范围、附录 B 换卡、RAS23 页码体例统一）。
- `compiled_from` 从 39 条重建为正文实际 60 张卡（sha256 前 16 位），附录 B 去掉未使用的 `relative-langlands`、
  补上 `sy0246/concept/vanishing-theorem`。
- 统稿后补修（R1/R2 未列）：L543 的 CL23 引注原写「p.36–37 §5.7–§6.2」，按目录实为书页 37–40（§5.7 在 37、
  §6.2 在 40），已改「书页 37–40（PDF 42–45）」；并把「书页 p.3/p.5/p.2–3」统一为「书页 3/5/2–3」。

## 未修 / 遗留（如实记录）

1. §2.3 的 FGV 一栏仍标「仓库无 FGV 中译，待核」：本仓库确实没有 FGV 原文或中译，未外部核对。
2. §5.4「全证明里技术门槛最高的一步」、§4.3「低亏格更容易不是定理」、§6.2 重数一「编者综合」
   均为编者判断，正文已标明；不是文献原话。
3. 「上千页」只给量级，仓库没有五篇的逐篇页数，未精确统计。
4. R2 报告后的修改由 lead 直接执行，**没有再把改后页面送回 R1/R2 二次全量核对**；
   R1/R2 的结论对应的是 v1.0（修改前）。这是本版最大的程序性风险。
5. `check_survey.py` 的 `entries` 解析恒报 0（它按 `{{entry:…}}` 宏统计，本页把 entries 放在 front matter 列表里）。
   工具 bug，不影响页面；未改脚本。
6. 五篇 arXiv 号（I 2405.03599v3、II 2405.03648、III 2409.07051、IV 2409.08670、V 2409.09856v3、
   char p 2508.02237）已由 SCH26 书目 p.41–44 与 CL23 书目双证；II–IV 的版本号仍只按书目。

## 独立校对（lead，2026-11-28 01:35）

- 通读全文并抽查源文：BZ26 p.11（de Rham `Loc` 的定义）、p.14–16（Gr 与几何 Satake）、SCH26 s02（char p 条件、`LocSys′`）、s11（BD 1996 与 SL₂ oper）、s08（Frobenius 迹）。
- 另修一处误译：§6.1 原「Beilinson 投影自动失效」改为「迹已落在 `IndLisse(X)^{⊗I}` 中，Beilinson 投影操作自动不起作用」（SCH26 s08）。
- 另修一处记号：§2.2 的「Gr = LG₊\\LG/LG₊ 的双陪集」改为「Gr = LG/LG₊；其 LG₊-轨道（等价于双陪集 LG₊\\LG/LG₊）」。
- 同步更新 `datasets/encyclopedia/pages/langlands-program.md` 的链接标题为「从谱定理到五部曲」（原 HANDOFF 记「保留未动」，此处以实际改动为准）。
- 外部核验：I 2405.03599v3、V 2409.09856v3、char p 2508.02237v1 的标题/版本已对 arXiv abs 页；II–IV 仍只按 SCH26/CL23 书目。
- 未改 `index.jsonl` 与 `entries/geometry/geometric-langlands.json`：其摘要仍是「GL_n 已证、一般约化群仍是猜想」，与新页 §7.1 不一致；因改 entry 会牵动其单一来源（袁瑶 2020）口径，留给后续单独修订。
- 页面仍 `status: draft`、`reviewed_by: []`：本次是 AI 独立校对，不冒充人工复核；建议人工复核后再升 `reviewed`。

## 未做

- 未 `git commit`、未推送（仓库里有其他会话的改动，本次只应提交上述交付物；是否提交由用户决定）。
- 未做 PDF/HTML 渲染（仓库暂无 `{{entry:}}`/`{{card:}}` 的站点构建器；卡片导航以仓库内相对路径 JSON 为准）。
