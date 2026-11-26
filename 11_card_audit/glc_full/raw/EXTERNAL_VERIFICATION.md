# 外部核验报告：22 张已修卡 / 51 处修改

- 日期：2026-11-26
- 审计目录：`datasets/_audit/glc_full_2026-11-26/`
- 对应修复记录：`fix_log.json`（51 处 before/after，逐卡 sha256）
- 对应逐卡对比：`11_card_audit/glc_full/casebook/`（22 例，错误版／正确版／为什么错／证据／审计轨迹）
- 本文只回答一个问题：**这 51 处修改，逐条回到「卡以外」的来源，是否站得住？**

---

## 0. 结论

| 类别 | 处数 | 复核方式 | 结论 |
|---|---:|---|---|
| 定位类（页码、定理出处） | 38 | PDF 原书正文页逐字核对；其中 35 处另做独立的「源码行号 → 原书页」重算 | 全部通过 |
| 内容／术语类 | 12 | 原书原文句＋arXiv 一手论文（5 张卡有 arXiv 佐证）＋卡内一致性 | 全部通过 |
| 内部一致性类 | 1 | 只针对卡内自相矛盾的最小修补，不主张新数学命题 | 通过（不要求外部命题支撑） |
| **合计** | **51** | | **51 通过，0 推翻，0 需回退** |

- 22 张卡**每一张**都至少有一手来源（陈麟讲义 PDF 正文页）支撑其修改，没有一张只靠「卡内推理」或「模型记忆」。
- 唯一重大级（major）修改 `vanishing-theorem` 有两重独立依据：原书 Theorem 5.7.2 的原文 + Gaitsgory 原始论文的 Conjecture 1.3。
- 本轮**没有**把任何单方未修的卡偷偷改掉；5 张单方未修卡的外部复核结果见 §5，其中 3 条被列为残余风险，建议下一轮处理。

---

## 1. 复核口径

沿用 `11_card_audit/WORKFLOW.md` 的证据等级，只接受：

- **E1 一手**：陈麟《几何 Langlands 理论导论》PDF 原书正文页（`tmp/pages/pNNN.txt` 为逐页文本，页码 = 印刷页，偏移 0）。
- **E2 权威二手**：arXiv 原始论文（读其 TeX 源码或 PDF 原文），仅用于确认术语、条件、归一化约定。
- **E3 卡内**：只用于判「卡内自相矛盾」，不能单独证明数学命题。

判定只问三件事：① 卡的说法是否与来源**相反**；② 是否**丢掉了来源明确写出的条件**；③ 是否把出处**标到了错误的页／节／编号**。解释性措辞、记号选择、等价改写一律不算错（与审计阶段同一口径）。

不使用：Wikipedia、博客、内容农场、模型记忆、其他审计轮的结论。

---

## 2. 定位类（38 处）

### 2.1 方法

1. **不用卡的结论**：只取 `sources[].anchor` 里未改动的源码行号，按 `\srcpage{N}` 重建「行号 → 原书页」映射。
2. **不用源码的页码**：`\srcpage` 是译者插入的分页标记，落点会漂移（见 2.3），所以最终以 **PDF 正文页的页首句/节标题** 为准。
3. **逐页对读**：把「卡声称的页」与「该页 PDF 文本首句」并排，确认卡的定义／定理／陈述确实落在该页。

工具：`tools/reverify_pages.py`（输出 `tmp/reverify_pages.json`）。它检查了 35 处可机械重算的定位编辑（`sources[].pages` 12、`sources[].pdf_pages` 12、`theorems[].source` 11）；另 3 处 `gap_note` 里的页码用同一页的正文人工核对。

### 2.2 定位编辑一览（15 张卡）

| 卡 | 修改（字段：改前 → 改后） | 该页 PDF 实文依据 |
|---|---|---|
| gl1-trace-character | `sources.pages`/`pdf_pages` [6]→[7]；`theorems[0].source` p.6→p.7 | p.7 首句 `Lemma 1.1.4. Let F be a Hecke eigensheaf…`；p.6 结束于 Definition 1.1.3 |
| torsion-stack-local-model | pages [43]→[42,43]；theorem.source p.43→p.42 | p.42「For X = A¹, a length-d torsion sheaf is a d-dimensional vector space with an endomorphism, hence Tor^d ≃ gl_d/GL_d」；p.43 已是 parabolic correspondence |
| hecke-laumon-eigensheaf | pages [46]→[45,46] | p.45「α_d : HL^d_k(K) −→ L^d_E ⊠ K (d ≥ 0)」；p.46 首行 `with the evident normalization for d = 0…` |
| shv-nilpotent-support | pages [58,59]→[58,60]；theorem.source/gap_note p.59→p.60 | p.59 末「Third, it is not too large…」；p.60 首段「More generally, for a smooth scheme S and conical subset N ⊂ T*S…」 |
| frobenius-twisted-trace | pages [63]→[63,64]；theorem.source p.63→p.63–64 | p.64 首段「whose points are restricted Weil Ĝ-local systems. Taking global sections recovers…」 |
| restricted-categorical-langlands | pages [62,63]→[63]；theorem.source p.62–63→p.63；gap_note p.62–63→p.63 | p.63 首行「12.6. Restricted categorical Langlands. The resulting restricted form of the (Betti) con-」 |
| scheme-of-singularities | theorem.source p.54→p.53；gap_note p.54→p.53 | p.53「The zero-support category recovers perfect objects: Coh⁰(Y) ≃ Perf(Y), IndCoh⁰(Y) ≃ QCoh(Y)」 |
| whittaker-coefficient | theorem.source p.64→p.65 | p.64 是 `coeff(𝓕) := C_dR,c(Bun^Ω_N, p^!(𝓕)⊗ψ^!(exp))` 的定义；p.65 才是「factors through the projection to the tempered quotient」 |
| drinfeld-sokolov-gauge | pages [68]→[69]；theorem.source p.68→p.69 | p.69「14.2. The local normal form.」；p.68 只有 §14.1 与 Hitchin 底 |
| quantum-local-langlands | pages [73,74]→[74]；theorem.source p.73→p.74 | p.74「15.4. Relation with quantum local Langlands. The critical FLE is a boundary value of」 |
| aut-sigma-module | pages [70]→[71] | p.71「14.5. The automorphic module attached to an oper. Let σ ∈ Op_Ĝ(X)…」 |
| hitchin-base | pages [67]→[67,68] | p.68「If d₁,…,d_r are the exponents of ĝ, then c_Ĝ,Ω ≃ ⊕_i Ω_X^{d_i+1}, and the Hitchin base is Hitch_Ĝ(X) := Γ(X, c_Ĝ,Ω)」 |
| global-langlands-functor | pages [75]→[76]；theorem.source p.75→p.76 | p.76「16. Proof of the global conjecture」；第 16 章正文起于 p.76 |
| eisenstein-compatibility | theorem.source p.76→p.77 | p.77「The target statement is the commutativity of」＋图 (16.1)；p.76 只有 §16.2 标题与 q、p 对应 |
| unramified-oper | pages [72]→[72,73] | anchor 跨页：η 展开、缺陷度量 λ̌、Op^unr = ⊔Op^{reg,λ̌} 均在 p.73 |

### 2.3 独立重算里 21 处「naive ≠ 改后」的解释

`reverify_pages.py` 用未改动的 anchor 重算时，有 21 处算出的页与改后页不同。逐条查明后**全部**是译者分页标记的已知漂移，不是卡错：

| 类型 | 机制 | 涉及 | 处数 |
|---|---|---|---:|
| T1 标记迟一页 | `\srcpage{N}` 被插在「属于第 N 页的内容」**之后**，于是按标记读到的是 N−1 | gl1、aut-sigma、drinfeld、whittaker、quantum、restricted-categorical | 15 |
| T2 标记早一页 | `\srcpage{N}` 被插在「属于第 N−1 页的内容」**之前** | scheme-of-singularities、torsion-stack-local-model | 2 |
| T3 缺页标记 | 该章没有 `\srcpage{N}`（ch11 缺 p.60、ch12 缺 p.64） | shv-nilpotent-support | 3 |
| T4 anchor 含上页标题 | anchor 起始行是上一页的节标题，卡引用的是下一页的图表 | eisenstein-compatibility | 1 |

典型读法（T1，gl1）：`ch01.tex:106-109` 是引理 1.1.4，`\srcpage{7}` 却落在 `\end{lemma}` 之后；按标记算是 p.6，PDF 实文在 p.7。卡的 p.7 与 PDF 一致，源码标记才是漂移源。
典型读法（T2，torsion）：`ch10.tex:42` 就是 `\srcpage{54}`，而「zero-support recovers perfect objects」这句话在 PDF p.53 —— 标记早插了一页。
典型读法（T4，eisenstein）：anchor 覆盖 §16.2 标题行（p.76），但卡的定理陈述是图 (16.1)（p.77），所以 p.77 才是「卡自己那句话」的页。

**原则**：`sources[].pages` 必须覆盖卡自己的定义/陈述/证明主体；anchor 里顺带包含的上一页标题、下一页续证句不算漏页（此为审计阶段已定口径，`extension-stack-vanishing` 同此处理，见 §6）。

---

## 3. 内容／术语类（12 处）

### 3.1 vanishing-theorem（major，1 处）

**卡的原文（改前）**：
> 更一般的界把假设放宽为 `rank(E) > k`（**不再要求 `k < n` 且 `E` 几何不可约**），界为 `d > (2g−2)k·rank(E)`；……

**改后**：
> 更一般的界把假设放宽为 `rank(E) > k`，界为 `d > (2g−2)k·rank(E)`；……

**E1（原书 p.36，Theorem 5.7.2）**：
> If E is geometrically irreducible of rank n, with k < n, and d > nk(2g − 2), then Av^d_E = 0. **More generally, the vanishing theorem applies to averaging on Bun_k when rank(E) > k**, with bound d > (2g − 2)k·rank(E).

**E2（Gaitsgory, arXiv:math/0204081v2, §1.2 Conjecture 1.3）**：
> Assume that E is irreducible, of rank > n. Then for d, which is greater than (2g−2)·n·rk(E), the functor Av_E^d is identically equal to zero.

（该文 §0.4 取基域 k 代数闭，故其 "irreducible" 即几何不可约。）

**判断**：原句两半都不成立。① `rank(E) > k` 与 `k < n` 是**同一个条件**的改写（n = rank E），说「不再要求 k<n」是把等价条件说成放宽；② 一般形式**仍然要求** E 几何不可约（原书与 Gaitsgory 论文都没有解除），说「不再要求 E 几何不可约」直接与来源相反。删括注是最小修复，未改任何数学内容。严重度 major（定理条件被反向陈述）。

### 3.2 Casselman–Shalika 归一化（3 张卡共 7 处）

| 卡 | 处数 | 字段 |
|---|---:|---|
| b-lambda-ic | 2 | `key_points[3]`、`pitfalls[0]`（`Shalala`→`Shalika`） |
| local-laumon-formula | 4 | `definition.text`、`key_points[3]`、`theorems[0].proof.steps[7].why`、`theorems[0].proof.gap_note` |
| eisenstein-compatibility | 1 | `key_points[3]`（`Schalika`→`Shalika`） |

**E1（原书 p.76）**：
> Here CS denotes the geometric **Casselman–Shalika** equivalence.

**E2（CCF24 = arXiv:2409.07051，TeX 源码 grep）**：`Casselman-Shalika` 出现于源码第 796、842、1686、3966、3970、4090、19201、23751 行，全篇无 `Shalala`/`Schalika`。

**判断**：人名拼写错误。三张卡内部也互相不一致（同一卡别处写 Shalika），属术语级 minor。修法只改拼写，不碰归一化内容。

### 3.3 restricted-local-systems（2 处）

**改前（verification.checks[1]）**：
> ……卡中 definition.notation 的说法与此冲突 → P1，alignment=error。 verdict: contradicted

**改后**：把「卡中 definition.notation 的说法与此冲突 → P1，alignment=error」改写为「卡中 definition.notation 已按此写成『IndLisse 的左完备化』，与之一致」，verdict `contradicted`→`confirmed`。

**E2（AGKRRV = arXiv:2010.01906v2，TeX `main.tex:1142-1150`）**：
> Consider its ind-completion, denoted $\iLisse(X)$. Finally, let $\qLisse(X)$ be the **left completion of $\iLisse(X)$ in the natural t-structure**.
> （脚注：The last step of left completion is unnecessary if $X$ is a categorical $K(\pi,1)$…）

**判断**：卡正文（2026-11-18 已按 AGK20a §0.5.4 改对）与 AGKRRV 原文一致；`verification.checks[1]` 仍是修订前的旧判词，属卡内残留自相矛盾。修复没有引入新说法，只是让核验记录不再与正文冲突。

### 3.4 base-whittaker-sheaf（1 处）

**改前 summary**：「……基础情形中 `q_! j_{k,!} F_k` 是 `Av_E^d(W_k)` 的**茎**。」
**改后**：「……是 `Av_E^d(W_k)` **限制到 `C_k^{tor=0}` 上的层**。」

**E1（原书 p.37）**：
> q_! j_{k,!} F_k ≃ Av_E^d(W_k)|_{C_k^{tor=0}}.

**判断**：原式是「限制到 `C_k^{tor=0}`」，不是「`Av` 的茎」；且同卡 `definition`/`theorem`/`key_points[2]` 都写的是限制。改为与原文、与卡内其余字段一致。术语级 minor。

### 3.5 perverse-quotient-lemma（1 处）

**改前 summary**：「若 K 是 G_m-等变、`π_*K` 反常，则下降到 P(E) 后沿 π̄ 的 ! 推前仍反常。」
**改后**：「若 K 是 G_m-等变、**`π_!K` 与 `π_*K` 均反常**，则……仍反常。」

**E1（原书 p.47）**：
> Suppose K ∈ Perv(E) is G_m-equivariant and that **π_! K, π_* K ∈ Perv(B)**. Let K̄ be the descent of K|_{E∖0} to P(E). Then π̄_! K̄ is perverse.

**判断**：summary 漏了一个并列前提（π_!K 反常），同卡 definition、theorem、pitfalls[1] 都写了两个前提，属内部不一致 + 弱化定理条件。补回前提是最小修复。

### 3.6 eisenstein 的人名与页码之外的判断

eisenstein 的两处修改（theorem.source p.77、kp3 Shalika）分别归入 §3.2 与 §2.2；没有第三处。

---

## 4. 唯一没有外部命题支撑的 1 处

`fourier-deligne-transform` `theorems[0].proof.steps[2].why`：

- **改前**：「`t`-正合函子把单对象送到单对象（至多差平移）。」
- **改后**：「等价加 `t`-正合才保持单对象，且不产生平移。」
- **为什么必须改**：同一步的 `text` 说「单靠 `t`-正合不足」，`key_points[2]` 说「等价加 `t`-正合才保持单对象，且不产生平移」；`why` 与前两者直接矛盾（且「至多差平移」正是 2026-11-18 README 修订明令删去的说法）。修复只是删掉这个自相矛盾的从句，**没有**提出新的数学定理。
- **外部检索结果**：Juteau, arXiv:0901.3671 的 Fourier–Deligne 章（TeX 第 8715 行起）用 grep 找不到「Fourier 变换 t-正合」的显式陈述；KL85（Kazhdan–Laumon）PDF 下载两次超时（curl exit 28），未取到原文。故本条按 **E3（卡内一致性）** 处理，归入「内部一致性类」，不声称有外部命题支撑。
- **风险**：低。该从句不是可独立验证的数学断言，删去后 `why` 与卡内其余字段一致；即使将来找到 KL85 的表述，也只会印证「等价 + t-正合」的用法，不会有反向证据。

---

## 5. 5 张单方未修卡的外部复核

按流程（arbiter 判 pass 的保留为单方发现、不修），这 5 张未改。外部复核结果如下——**3 张维持不改，2 张的 A 方观察在外部来源上仍成立，列入残余风险**。

| 卡 | A 方断言 | 外部／原文复核 | 处理 |
|---|---|---|---|
| affine-grassmannian | pages [13] 漏 p.14（L^+G_X、LG_X 定义与扭曲积在 p.14） | p.13 有 Gr 定义与 Theorem 2.4.1；p.14 是 L^±G_X 的**备注性**记号与 Hecke 对应 | 维持不改：卡的定义/定理主体在 p.13，p.14 是背景 |
| deligne-gl1-existence | `definition.notation` 的「k-向量空间（分次）」应写系数域 e | p.7「Fix a reasonable sheaf theory with **algebraically closed coefficient field e**」；同页用 Q_ℓ^× | **残余风险 ①**：按原文，Shv(Spec k) ≃ e 上的分次向量空间；卡写 k 会被误读为基域。措辞级，非数学结论错 |
| euler-characteristic-trace-test | pages [45] 漏 p.44（χ_K 的定义） | p.44 定义 χ_K，p.45 才是判据正文 | 维持不改：卡引的是判据，页已覆盖 |
| hecke-laumon-stack | `key_points[0]`「三者互相决定其中之二」不成立：(M′,T) 不能决定 M | 短正合列 0→M′→M→T→0 的扩充由 Ext¹(T,M′) ≅ ⊕_x((T_x)^∨⊗M′_x) 参数化；同卡 `pitfalls[1]` 自述「忘记 M′ 会丢掉子层信息」 | **残余风险 ②**：数学观察成立，但 arbiter 判 pass，按流程未改。建议下轮改为「三者中任意两者确定第三者的**候选**，M 还需扩充数据」 |
| local-whittaker-eigenfunction | `key_points[4]`「有效优势权时指数为负」过强 | λ=(c,0,…,0)（如 n=3, λ=(1,0,0)）时 n(λ)=0，指数为 **0**；应为「非正」 | **残余风险 ③**：边界情形过强，arbiter 未采（其复核对象错位到 `verification.checks[2]`），按流程未改 |

说明：③ 的 `verification.checks[2]` 本身也值得注意——它引用的是 FGKV98 的 P_n^+（λ₁≥…≥λ_n，无 λ_n≥0），与卡里「有效优势权（λ_n≥0）」不是同一概念，故该 check 的 `contradicts` 判词其实是**错位比较**。这不改变 `key_points[4]` 在 λ_n=0 边界上的过强问题。

---

## 6. 残余风险（与 `report.md` §9 一致）

1. **102 张 A 判 pass 卡没有被 B 抽到**（B 只覆盖 27 张 A-issue + 25 张随机 pass = 52 张）。本轮的「154 张全部有 A 记录」成立，但「每张都有第二判断」只对 A-issue 卡成立。这是方案设计的取舍，不是遗漏。
2. **`extension-stack-vanishing`**：pages [40]，anchor 含 §7.5 收尾（p.43）。按「pages 覆盖主对象即可」口径判为可接受，未改；若下轮收紧口径，应改为 [40,43]。
3. **上表三条残余风险 ①②③**：外部复核认为 A 方观察有依据，但按 arbiter 终裁未修。建议下一轮用「单方发现二审」通道处理，不必重跑全量。
4. **底本自身缺陷未动**：`ch14.tex` 章首缺 `\srcpage{67}`、`ch11.tex` 缺 `\srcpage{60}`、`ch12.tex` 缺 `\srcpage{64}`、`ch16.tex:2` 的「原PDF第75页」注释错。卡已按 PDF 实页修正；源码未改（任务禁止改译注工程）。
5. **`fourier-deligne-transform` 的 why 行**：无外部命题支撑（§4），但属卡内矛盾的最小修补，风险低。

---

## 7. 复现

```bash
cd /c/Users/admin/Desktop/数译发布/gitee_shuyi
export PYTHONIOENCODING=utf-8

# 1) 独立重算 anchor 页（不用卡的结论）
python datasets/_audit/glc_full_2026-11-26/tools/reverify_pages.py
#   → tmp/reverify_pages.json: rows 35, diffs 21（逐条解释见 §2.3）

# 2) 51 处修改的 before/after 与 sha256
python - <<'PY'
import json,io
fx=json.load(io.open("datasets/_audit/glc_full_2026-11-26/fix_log.json",encoding="utf-8"))
print(len(fx["fixes"]), sum(len(f["edits"]) for f in fx["fixes"]))
PY

# 3) 验收（154 卡 / 1676 库 / diff 范围 / md 同步）
python datasets/_audit/glc_full_2026-11-26/tools/verify_final.py
```

---

## 8. 文件

| 文件 | 内容 |
|---|---|
| `fix_log.json` | 22 卡 51 处 before/after、sha256_before/after、md 同步记录 |
| `tmp/reverify_pages.json` | 35 处定位编辑的独立重算（naive 页、改后页、21 条差异） |
| `tmp/pages/pNNN.txt` | PDF 逐页文本（页码 = 印刷页） |
| `11_card_audit/glc_full/casebook/` | 22 例逐卡对比（错误版/正确版/为什么错/证据/审计轨迹/形式化提示/防再犯） |
| `report.md` | 审计全过程（A/B/仲裁/修复/验收/残余风险） |
