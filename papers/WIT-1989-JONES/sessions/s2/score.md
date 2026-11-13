# S2 独立评分（Verifier）

- 评分人：verifier ｜ 日期：2026-11-13
- 独立声明：未读 `sessions/s2/transcript.md`、`reports/`、`one_pager.md`；只评 `claims.jsonl`、`questions.jsonl` 与原文（页图 `witten1989/pages/page-NN.png`、OCR `witten1989/text/page-NN.txt`、译本 `witten1989/deliver/witten.tex` 与 `witten1989/sections/*.tex`、`witten1989/deliver/校勘与审校批注汇总.md`）。页图页号 = 印刷页 − 350。
- 抽检 5 条（任务要求 ≥4；含 c-s2-06、c-s2-08）。

## 1. 抽检表

| claim | 锚点 | 实测 | 判定 | 证据路径 |
|---|---|---|---|---|
| c-s2-02 | [src p.368–369] | p.369 原文逐句："the first Chern class of L … is precisely the symplectic form that appears in (3.1) or (3.2), provided k=1. For general k, the symplectic form … represents the first Chern class of the k-th power of the determinant line bundle"；p.368–369 全文找不到"辛形式必须整"的预量子化条件；p.369 末 "the quantum Hilbert space is thus the space of global holomorphic sections of L^{⊗k}" ✓。claim 的 "写 [ω]=c₁(L^{⊗k})" 是把两句话压成一个等式，属重建，应标 | **pass**（一处需标重建） | `witten1989/text/page-19.txt`；`witten1989/pages/page-19.png` |
| c-s2-06 | [src p.370],[src p.371] | p.370 原句 verbatim："(Because of the conformal anomaly, this bundle has only a projectively flat connection, with the projective factor being canonically odd under reversal of orientation.)" ✓；p.371 projectively flat connection 与 monodromies ✓ | **pass** | `witten1989/text/page-20.txt` L29–31；`witten1989/text/page-21.txt` L13–20 |
| c-s2-07 | [src p.371] | p.371："these monodromies just correspond to an action of the purely topological mapping class group" ✓；"模函子的物理来源"是解释句，原文同页有 conformal blocks/模函子语境 | **pass** | `witten1989/text/page-21.txt` L13–20 |
| c-s2-08 | [src p.359 (2.16)–(2.17)],[src p.382 (4.21)],[河野 p.107],[上野 p.125] | (2.16) 定义 $c_2(G)$ 并归一化 $c_2(SU(N))=2N$；(2.17) 明写 "The effect of this factor is to replace $k$ in (2.8) by $k+c_2(G)/2$"——**本文已在路径积分侧做了 $k\to k+c_2/2$ 平移**（校勘 line 84 亦记此条）。claim 的"本文没有做这一步"只在"§3 未加半形式 $K^{1/2}$"这一狭义读法下可辩护；但"本文的 $k$ 与 WZW 的 level 相差 $h^\vee$"被 p.390 "integrable representations of level $k$ … $n=0\ldots k$" 与 (4.21) $q=e^{2\pi i/(N+k)}$（标准 level-$k$ 公式）反驳 | **fail** | `witten1989/text/page-09.txt` L35–45；`witten1989/text/page-40.txt` L5–6；`witten1989/text/page-32.txt` L40–41；`witten1989/deliver/校勘与审校批注汇总.md` line 84 |
| c-s2-09 | [src p.382 eq 4.21] | $q=e^{2\pi i/(N+k)}$ 在 p.382 (4.21) ✓；但 $c_2(SU(N))=2N$ 在 **p.359 (2.16)**，(4.21) 页无 $c_2$；"$h^\vee=N$ 故 $q=\ldots$" 是推论链，不是该式所写 | **partial**（$q$ 对、$c_2$ 缺锚） | `witten1989/text/page-09.txt` L35–38；`witten1989/text/page-32.txt` L40–41 |

## 2. 六维评分（每条扣分带锚点）

| 维 | 分 | 扣分点与锚点 |
|---|---|---|
| T1 原子性 | **10 / 15** | −2 c-s2-08 一条捆"半形式机制＋level shift＋本文没做＋相差 $h^\vee$"四断言（`text/page-09.txt` L35–45；`text/page-40.txt` L5–6）；−1 c-s2-09 捆 $c_2$／$h^\vee$／$q$／SU(2) 四断言（`text/page-09.txt` L35–38；`text/page-32.txt` L40–41）；−1 c-s2-10 捆 dim H⁰=k 与 t=k+1 两套计数＋"不可相减"判断（`text/page-35.txt`；`text/page-36.txt`）；−1 c-s2-02 捆"无整性条件＋直接用行列式线丛＋[ω]=c₁(L^{⊗k})"（`text/page-19.txt`） |
| T2 依据闭合 | **10 / 20** | −5 c-s2-08：锚点 (2.16)(2.17) 恰好反驳"本文没做/相差 $h^\vee$"（`text/page-09.txt` L35–45；`text/page-40.txt` L5–6；`text/page-32.txt` L40–41）；−2 c-s2-09 $c_2$ 无 p.359 锚，(4.21) 不支撑 $h^\vee=N$（`text/page-09.txt` L35–38）；−1 c-s2-10 "§4.3 $t=k+1$" 在 p.385–388 OCR 全文搜 pillow\|t=k\|k+1 无命中（`text/page-35.txt`；`text/page-36.txt`），无式号；−1 c-s2-02 "写 [ω]=c₁(L^{⊗k})" 是重建（`text/page-19.txt` 原文分两句：k=1 时 c₁(L)=辛形式、一般 k 用 $L^{\otimes k}$）；−1 外部教材锚点（李思/河野/上野）不在 Verifier 允许材料内，未独立核 |
| T3 分支失败修复 | **13 / 20** | −7：counterpoints 空 7/12（c-s2-04/05/07/09/10/11/12，脚本计数）；12 条无一条按 §2.4 的"如果我对/如果作者对→Y/Z"写双分支；修复路径只在 c-s2-03（D1 分歧＋构造性绕过）、c-s2-06（framing anomaly 待追踪）、c-s2-10（两套计数不可相减）出现 |
| T4 边界置信 | **10 / 15** | −5：7/12 无边界条件（同上）；c-s2-09 confidence=high 但锚点不全（`text/page-09.txt` L35–38）；c-s2-08 confidence=medium 尚可但结论被锚点反驳；c-s2-02 对"缺席证据"用 high 偏强（`text/page-19.txt`） |
| T5 可机读 | **8 / 15** | −7：脚本按 CHARTER §5 校验 12 条得 43 项违规——status 12 条全非法（confirmed/provisional，应为 active/contested/refuted）、confidence 12 条全字符串（应为 0–1 数值）、session 12 条全小写 "s2"（应为 "S2"）、counterpoints 空 7 条；anchors 用 "[src p.N]"/"[李思 p.N]" 而非规范 `p.N`/`eq x.y` |
| T6 反事实迁移 | **10 / 15** | −5：c-s2-08/09/10/11 有跨群/跨 $k$/跨流形/跨约定的迁移（SU(2) $k+2$ 于 `text/page-40.txt` L5–11；SU(N) 于 `text/page-09.txt` L35–38；$T^2$ 与 pillowcase 于 `text/page-35.txt`；ℏ 约定于 `text/page-19.txt`），但没有一条显式回答"换一个群/换一个流形，哪一步会变"；c-s2-10 的对比停在"不可相减" |

## 3. 总分与准入

**总分 61 / 100。** 未触发 §6.1 一票否决（c-s2-08 是锚点误读/推论错误，不是伪造引文，也非把猜想写成定理；该条自标 reconstruction/medium/provisional）。但按 §6.2 单场 T≥75 才计入 → **本场不进语料；需重评。**

## 4. 整改项（按优先级）

1. **重写 c-s2-08**：锚点 (2.16)(2.17) 已证明本文用 η-不变量在路径积分侧实现 $k\to k+c_2/2=k+h^\vee$（`text/page-09.txt` L35–45；校勘 line 84）。应改为："路径积分的正规化已含 shift；§3 的 $L^{\otimes k}$ 几何量子化未加半形式 $K^{1/2}$；加半形式后的等效能级需另推，原文未做。" 删除或改写"本文 $k$ 与 WZW level 相差 $h^\vee$"——p.390 的 "level $k$, $n=0\ldots k$" 与 (4.21) $q=e^{2\pi i/(N+k)}$ 表明本文 $k$ 就是 WZW level（`text/page-40.txt` L5–6；`text/page-32.txt` L40–41）。
2. **c-s2-09 补锚**：$c_2(SU(N))=2N$ 引 `p.359 (2.16)`，$q$ 引 `p.382 (4.21)`；把"$h^\vee=N$ 故 $q=\ldots$"改成"$q$ 取 (4.21)，$h^\vee=N$ 见 (2.16)"，去掉因果误置。
3. **schema 对齐 CHARTER §5**：session→"S2"；status→active/contested/refuted；confidence→数值（如 0.85）；补 7 条空 counterpoints；anchors 统一为 `p.N` / `eq x.y`（外部教材用 `李思 p.301` 之类但需与 §5 兼容）。
4. **c-s2-02**：补 p.369 的正面锚（$L^{\otimes k}$ 那句），把"[ω]=c₁(L^{⊗k})"标 `[重建]`。
5. **c-s2-10**：给出 "§4.3 $t=k+1$（pillowcase）" 的确切页/式（p.385–388 未定位，`text/page-35.txt`；`text/page-36.txt`），或标"我们按 (4.2x) 推"。
6. **外部教材标注**：李思/河野/上野的锚点标"Verifier 范围外未独立核"，或补页图；c-s2-12 的"河野全书 0 次"需给检索方法与版本（`河野 vii–ix`、`p.107`）。
7. **补 §2.4 双分支**：至少 2 条显式检验（建议：c-s2-08 的 level 关系；c-s2-10 的 $T^2$ 计数），写"如果我对，应看到 X；如果作者对，应看到 Y"。

## 5. 复审（2026-11-13 第二轮；历史分不改）

- 抽检：c-s2-06、c-s2-07、c-s2-08、c-s2-09、c-s2-02。

| 项 | 原问题 | 现文核对 | 判定 |
|---|---|---|---|
| c-s2-08 | "本文没做 shift／相差 $h^\vee$" 被 (2.16)(2.17) 反驳 | 重写后："有效能级就是 $k+h^\vee$：(2.16)(2.17)[p.359] 把系数修正为 $k+c_2/2$；(4.21) 与 p.390 level $k$, $n=0\ldots k$ 一致；$K^{1/2}$ 机制本文未写，半形式移位是后世解释，不能反说本文少做移位"——与 `text/page-09.txt` L35–45、`text/page-32.txt` L40–41、`text/page-40.txt` L5–6 相符 | **修复** |
| c-s2-09 | $c_2(SU(N))=2N$ 缺锚 | 已补 [src p.359 (2.16)–(2.17)]（`text/page-09.txt` L35–38） | **修复** |
| c-s2-02 | 缺 p.369 正面锚 | 仍可复核 p.369 L30–32 / L38–40（`text/page-19.txt`） | pass |
| c-s2-06 | — | p.370 L29–31 verbatim（`text/page-20.txt`） | pass |
| c-s2-07 | — | p.371 L13–20（`text/page-21.txt`） | pass |

- §6.1 否决：未触发（原 c-s2-08 属锚点误读/推论错误，非伪造引文，也非把猜想写成定理）。
- 仍未改（validator 43 项 / 12 条）：status 12 条 confirmed/provisional（非法）；confidence 12 条字符串；session 12 条小写 s2（口径）；counterpoints 空 7 条（c-s2-04/05/07/09/10/11/12）。
- 复审结论：**实质缺陷已修复（复审通过）；形式项仍有 43 项待改（T5/T4）**。历史总分 61 不追溯修改。
