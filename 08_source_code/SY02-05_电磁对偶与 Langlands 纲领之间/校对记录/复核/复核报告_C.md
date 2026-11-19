# 复核报告 C（ch16 / ch17）

**复核员**：rev20（adversarial reviewer，只读）
**日期**：2026-11-19
**范围**：`src_orig/chapters/ch16.tex` → `src/chapters/ch16.tex`、`ch17` 的 unified diff；`logs/log_ch16.md`、`logs/log_ch17.md`；`en/ch16_en.txt`、`en/ch17_en.txt`；`pages/p-NNN.png`（110 dpi），关键公式、图示、箭头另以 400–500 dpi 从 `_bench_benzvi/langlands.pdf` 重渲裁剪（`tmp_hires/`）。
**方法**：① 每条「改为」在 `src/chapters/chNN.tex` 中 grep 定位；② 公式、图示、符号逐处对照原书页；③ 新注逐条查 (a) 数学是否成立 (b)「来源」是否名副其实 (c) 是否把推测写成事实；④ 每章另抽 4–5 处日志未提处与英文对读；⑤ 全书 grep 统计 `\curvearrowright` / `\circlearrowright` / `\circlearrowleft` 用法。
**声明**：未修改任何 `.tex`，未编译；除 `tmp_hires/`（只读裁剪图）外未新建、未改动文件。

---

## §1 总览

| 章 | 复核改动数 | 落地失败 | 改错 | 改出新错 | 注释问题 | 新发现漏译 |
|---|---|---|---|---|---|---|
| ch16 | 6 | 0 | 0 | 0 | 1 | 0 |
| ch17 | 4 | 0 | 0 | 0 | 2 | 1 |
| **合计** | **10** | **0** | **0** | **0** | **3** | **1** |

计数口径与说明：

- **改动数**：ch16 的 6 项 = 脚注 1 移位、脚注 2 新增、`导出自交`、`?` 箭头、(16.74) Tutor Note、`composes` GAP；ch17 的 4 项 = `局部算子的`、`↺` 箭头、(17.83) Tutor Note、(17.148) GAP。
- **落地失败 0**：10 项全部在 `src/chapters/chNN.tex` 命中，行号见 §2。两章的 diff 除这些项外无其他改动（ch16 3 个 hunk / ch17 3 个 hunk）。
- **改错 0、改出新错 0**：逐项对照原书页，未见反向校正、符号反转、引用失效、环境不配对或编号错位；`\begin`/`\end` 各 126/126（ch16）、196/196（ch17），`$` 各 872/1432 为偶，`\tag` 101/163 与 log 自检数字一致，`\label` 无重复、`\ref` 目标（ch17:824 → `fig:17-1`）可解析。
- **注释问题 3**：ch16 的 GAP 依据句失实（P3）；ch17 的 (17.83) 注来源标签格式违规（P3）、(17.148) GAP 定性过重（P3）。
- **新发现漏译 1**：ch17:639 把原书笔误 “genus G” 静默改为 $g$ 且未加注（P3，严格说是「漏注」）。ch16 另有 1 项 P1 术语问题（ind-coherent），校订员已在 `logs/log_ch16.md:66`（§七-1）登记为「存疑」但未改，故不计入「新发现」，列 §4 由 lead 统一处理。

---

## §2 逐条异议

### §2.1 总表

| 章:行号 | 判断 | 证据（原 PDF 页 + 原文引文） | 建议处理 |
|---|---|---|---|
| ch16:162 | **成立**（P1 修复） | PDF p.268（书页 267）；`en/ch16_en.txt:181` “I.e. we are computing the **derived** self-intersection of a point in a vector space.” 原译「一点的自交」漏 derived；本章主题正是导出自交 | 保留 |
| ch16:144 | **成立**（脚注移位） | PDF p.267（书页 266）；`en/ch16_en.txt:152` “We can rewrite\^1 this as:”，脚注 1 在 `:159` “It does require some thought to see why quotients commute with intersections.” 原稿脚注放在 `\end{align}` 之后，会脱离所指句子 | 保留 |
| ch16:150 | **成立**（脚注新增） | PDF p.268（书页 267）；`en/ch16_en.txt:166` “This is what is called the based loop space,\^2 written:”；脚注 2 原文 “It is important to keep track of notation and context. This is based loops in the world of derived algebraic geometry, not in homotopy theory.” 译文忠实 | 保留 |
| ch16:426 | **成立** | PDF p.274（书页 273）式 (16.74)：底行箭头为虚线，其上方印有 “?”（500 dpi 裁剪 `tmp_hires/crop1674c.png`）。`\stackrel{?}{\dashrightarrow}` 与印本一致 | 保留 |
| ch16:394 | **部分成立**（GAP 依据失实，P3） | PDF p.273（书页 272）确印 “the derived version of line operators spectrally **composes** over $T^*[1]\Loc_{G^\vee}$”，引文无误；但 GAP 称「作者他处用法与英文文本层均不足以判定」不实：全书 “spectrally decompose(s/decomposed)” 共 14 处（`en/ch01_en.txt:224`、`en/ch03_en.txt:14/32/215/402/585`、`en/ch10_en.txt:1087/1634`、`en/ch11_en.txt:1209/1315`、`en/ch13_en.txt:173/904`、`en/ch14_en.txt:229`、`en/ch15_en.txt:565`），“spectrally composes” 仅此 1 处。译文已按「分解」处理，方向正确 | GAP 可保留但改写依据：删「不足以判定」，改为「全书他处均作 spectrally decompose(s)，仅此处作 composes，疑为笔误；译文按 decompose 处理」；或降为普通 Tutor Note（P3） |
| ch16:429 | **成立**（注释） | PDF p.274（书页 273）(16.74)：两个 $\wr$ 连接上下两行；底行虚线加 “?”。注文对 $\wr$（Langlands 对偶下的对应）与 “?”（函子未构造、未必存在）的解释与图及紧接正文（“$H^\vee\to G^\vee$ does NOT give any kind of map $H\to G$”）一致；`[译者按（无外部依据）：…]` 标签合规 | 保留 |
| ch16:244、252、337、355（另 11、391） | **漏改（P1，已登记存疑）** | PDF p.270（书页 269）；`en/ch16_en.txt:311` “there is some tension here, which is resolved by **ind-coherent sheaves**. This is written IndCoh or QC\^!.” 译文「导出凝聚层（ind-coherent sheaves）」把 ind-coherent 与 derived coherent 混为一谈：IndCoh 是 Coh 的 ind-完备化，不是「导出凝聚层」。252「导出凝聚世界」、337「某种导出凝聚层」、355「导出凝聚层」沿袭同一误译；`ch16.tex:11`（keytakeaways）与 `:391`（旧 Tutor Note）同误，`src/appendix_notes.tex:1000` 亦同 | 由 lead 统一改为「ind-凝聚层」（或「归纳凝聚层」）并首次夹注英文；正文 244/252/337/355 可改，`ch16.tex:11`、`:391` 及 `appendix_notes.tex:1000` 按规程属受保护/跨文件内容，须另批。校订员「跨文件不擅改」的处置本身站得住，但本轮交付仍带此 P1 |
| ch17:139 | **成立**（P1 修复） | PDF p.282（书页 281）；`en/ch17_en.txt:155` “we can obtain the ordinary E3-algebra **of local operators** by filling in the ball”。原译「普通的 $E_3$-代数」丢失 “of local operators”，加「局部算子的」后准确 | 保留 |
| ch17:466 | **成立**（但日志理由失实） | PDF p.288（书页 287）印 “some variety $M^\vee\ \circlearrowleft\ G^\vee$”（500 dpi 裁剪 `tmp_hires/glyph466.png`，箭头逆时针、箭尾在左上）；改后与印本一致，也符合本章「受作用者在前用 ↺」的写法（466 原为 `M^\vee\circlearrowright G^\vee`，是该写法中的孤例）。但 log 称「受作用者在前一律用 ↺ / 全书统一」不成立：ch17 另有 31 处 `\curvearrowright`、7 处 `\circlearrowright`（362、484、502×2、595、596、677、713，均为作用者在前），且 195、240、242、313、404 以 `F\circlearrowleft V` 把作用者放在前面；ch16 则用 ↺/↻ 区分左/右作用（(16.82) $G\circlearrowleft G/U\circlearrowright T$，PDF p.276） | 保留改动；把 log 的「全书统一」改为「本章词序约定」，或由 lead 决定是否按印本统一（详见 §2.2-c）。此条不构成改错，属 P2 记录问题 |
| ch17:688–692 | **内容成立，标签格式违规**（P3） | PDF p.291（书页 290）式 (17.83) 及上下文：原文 “we have the short exact sequence: $\Z F\to G^\vee\to GL(W)$ since $[F]\in G^\vee/G^\vee$”；注文「只是示意、并非真正正合列」「$[F]$ 为共轭类」的判断正确，与原文及 (17.82) 的 $\rho$ 记号一致 | 标签 `[来源：译者按（无外部依据）：…]` 不符合 `校对规程.md` §4 四选一：第 4 项应写成 `[译者按（无外部依据）：这是基于原文上下文的推断，未找到外部依据]`，前面**不加** `来源：`。删去 `来源：` 即可（P3） |
| ch17:1164 | **部分成立**（GAP 定性过重，P3） | PDF p.299（书页 298）确印 “functions on $X(K)$ invariant under the **positive half of $G(\mathcal O)$**”，引文无误；GAP 给出的「读者可先按 $G(\mathcal O)$-不变理解」与 (17.149) `L^2(X(K)/G(\mathcal O))` 及球函数标准定义一致，方向正确。但「$G(\mathcal O)$ 是超特殊极大紧子群，并无标准的‘正半部分’」说得过死：loop group 的 “positive half” 通常就指 $G(\mathcal O)$（正环路群），作者很可能只是把 “positive half of $G(K)$” 写成了 “of $G(\mathcal O)$”；也可能是 Iwahori 的 pro-unipotent radical，但 (17.149) 已排除后者 | 建议降为 Tutor Note（或保留 GAP 但改写措辞）：先说明「positive half of the loop group 通常即 $G(\mathcal O)$」，再说明「按印本照译；由 (17.149) 知应按 $G(\mathcal O)$-不变理解」。这样既保留异文提示，又不把可判定的事说成不可判定 |
| ch17:639 | **漏注**（P3；非本轮改动） | PDF p.291（书页 290）；`en/ch17_en.txt:728` “states attached to a Riemann surface of **genus G** is not so easy to write down”。此处 G 是群记号，genus 应为 $g$，是原书笔误；译文静默改为「亏格为 $g$」，未按规程 §0-3「照译+加注」处理 | 加一条短注：「原文作 genus G，据上下文（亏格）读作 $g$」；或改回照译并加注。属 P3，可与 lead 商定是否本轮处理 |
| ch17:1161 | **非本轮改动**（P2 记号） | PDF p.299（书页 298）式 (17.148) 印 `X(K)/X(O) ↺ k[...]`，下一句印 `G(O) ↺ X(K)`；译文用 `\curvearrowright`（↷）。这是既有译稿的记号漂移，不是本轮校订引入 | 记录待统一（若按印本，应作 `\circlearrowleft`）；不计入本轮改动数 |

### §2.2 三项特别核实

**(a) ch16：GAP 与「导出自交」「ind-coherent sheaves」。**

- 「导出自交」（ch16:162）：**站得住**。原书 p.268 明写 “derived self-intersection”，且 (16.28) 起全章围绕导出自交展开；这不是过度校正。
- GAP（ch16:394）：**方向对、依据错**。原文确作 “composes”（p.273），照译+加注的处理本身可以；但把「作者他处用法不足以判定」写成事实是失实的——作者在 ch01/ch03/ch10/ch11/ch13/ch14/ch15 共 14 处都用 “spectrally decompose(s/decomposed)”，其中 `en/ch15_en.txt:565` 正是 “spectrally decompose/sheafify over $T^*X[1]$”，与 (16.70) 的 $T^*[1]\Loc$ 同型。按 `校对规程.md` §5，「原文能读懂、只是有笔误且可确定正确读法」应走 P1 或普通注，不宜记 GAP；至少应把这条证据写进 GAP。
- ind-coherent（ch16:244 等）：**真正的 P1 漏网**。校订员在 log §七-1 已把问题说清楚（「IndCoh 是 ind-（归纳）完备化，与『导出凝聚层』不是同一概念」），但以「跨文件」为由未改。复核确认这是 P1 术语错误：`ch16.tex:244` 的夹注英文尚可让读者辨认，252/337/355 则无英文，读者会直接读成 derived coherent。建议 lead 统一定名（「ind-凝聚层」/「归纳凝聚层」，以 appendix_glossary 增补一条为准），再一次性改 ch16 正文、keytakeaways、旧注与 appendix_notes。

**(b) ch17：(17.148)「the positive half of $G(\mathcal O)$」记 GAP 是否合理。**

- 印本核对：p.299 确实是 “the positive half of $G(\mathcal O)$”（不是 $G(K)$，也不是 “positive loop group” 的另一种写法）；同一页 (17.149) 立刻改用 $G(\mathcal O)$-不变，故作者意图基本可从上下文恢复：球函数 = $X(K)$ 上 $G(\mathcal O)$-不变、并在未分歧 Hecke 代数下为特征的函数。
- 可能的所指：① $G(\mathcal O)$ 本身，即 loop group $G(K)$ 的「正半部分」（最自然，且与 (17.149) 吻合）；② 某个 Iwahori 的 pro-unipotent radical（即 Iwahori 分解的正向部分）——但那样得到的是 Iwahori-不变的函数，不是球函数，且 (17.149) 明确只用 $G(\mathcal O)$；③ 作者把 “positive half of $G(K)$” 误写成 “of $G(\mathcal O)$”。①③ 实为同一读法。
- 结论：**记 GAP 偏保守，但不算错**——异文确实存在，GAP 的读者指引（按 $G(\mathcal O)$-不变理解）正确；问题在措辞把「$G(\mathcal O)$ 没有标准正半部分」绝对化，且忽略了 “positive half of the loop group = $G(\mathcal O)$” 这一标准说法。建议降为 Tutor Note，或保留 GAP 而改写措辞（P3）。另：新 GAP 与紧邻的既有注（`ch17.tex:1183` 关于 (17.148) 分母 $X(\mathcal O)\to G(\mathcal O)$ 的说明）主题相邻，读者会连续读到两条关于同一式的注，可考虑合并或让新注只谈 “positive half”。

**(c) ch17 的 ↷ / ↻ / ↺ 在全书范围是否一致（只报 ch16/ch17 结论）。**

- 统计（按出现次数，`grep -o` 逐文件）：`\curvearrowright` 全书 50 次 = ch10 14 + ch13 5 + **ch17 31**；`\circlearrowright` 全书 25 次 = ch01 1 + ch11 8 + ch12 6 + **ch16 2** + **ch17 8**；`\circlearrowleft` 全书 32 次 = ch02 1 + ch03 2 + ch08 2 + ch09 1 + ch11 1 + ch15 6 + **ch16 6** + **ch17 14**。
- ch17 内部：`\circlearrowleft` 14 处中，除 195、240、242、313、404（`F\circlearrowleft V`，作用者在前）外，都是「受作用者在前」——269、297、304、365、374、396、466、1080、1210；`\circlearrowright` 8 处（362、484、502×2、595、596、677、713）则都是「作用者在前」；另有 31 处 `\curvearrowright` 用于 Hecke 代数/范畴作用（如 (17.149)）。印本 p.288、p.291 在这些位置一律印 ↺（“$G^\vee$ ↺ $M^\vee$”“$\pi_1\to G^\vee$ ↺ $M^\vee$”“$G^\vee$ ↺ $V$”），并不区分词序。
- ch16：`\circlearrowleft` 6 处、`\circlearrowright` 2 处，且 (16.82)（p.276）印本为 $G\circlearrowleft G/U\circlearrowright T$——**ch16 用 ↺/↻ 区分左/右作用**，与 ch17 的「词序约定」语义不同。
- 结论：**三种宏在全书并不统一**。ch16 的 ↺/↻ = 左/右作用；ch17 的 ↺/↻ 大体随词序，↷ 用于代数/范畴作用；ch10/ch13 又只用 ↷。就 ch17:466 而言，改动本身同时满足「与印本一致」和「本章受作用者在前用 ↺」，**成立**；但 log 的「全书统一」是错的，应改为「本章词序约定」。若 lead 要真正统一，需先决定以印本（全用 ↺ 表左作用）还是以译本现行约定为准；这已超出单章校订范围。

---

## §3 抽查记录

抽查对象均为日志未提处；逐段与英文对读，未发现新的意义错误。

**ch16**

1. (16.1)–(16.22)，`ch16.tex:1–139` vs `en/ch16_en.txt:1–150`（PDF p.265–267）：公式、量词、Tannaka 重构段均忠实；`ch16.tex:11` 的 keytakeaways 也用了「导出凝聚层」，但该块按规程不可改（见 §4）。
2. (16.23)–(16.36)，`ch16.tex:141–260` vs EN 150–260（PDF p.267–269）：脚注移位后的句子读通；`$k[u,u^{-1}]$`、`S=\mathrm{Sym}(V[-2])`、Koszul 对偶五式均与印本一致。
3. (16.34)–(16.50)，`ch16.tex:181–290`（PDF p.269–270）：`\End_{\wedge^\bullet V^*}(k)\simeq S`、`\mathrm{pt}\times_V\mathrm{pt}` 的奇异支撑解释、`\QC^!_N` 均无误。
4. (16.61)–(16.70)，`ch16.tex:330–390`（PDF p.272–273）：纤维积图 (16.62)、$\Loc_{G^\vee}(C)=\QC^!$、nilpotent singular support、derived Satake (16.70) 逐项对照无误。另以 400 dpi 确认 (16.67) 的 ≃ 上方确有 “?”（`tmp_hires/crop167c.png`），译文 `\stackrel{?}{\simeq}` 忠实（此项非本轮改动，仅备查）。
5. (16.71)–(16.101)，`ch16.tex:400–633`（PDF p.273–278）：Borel 对应、矩映射、$\cM^0=\mathfrak h^{\vee*}[2]/W$、$\cM^1=\mathfrak g^{\vee*}[2]/G^\vee$ 的等号方向、$\Shv(LG_+\backslash LG/LG_+)$ 的卷积/张量积说明均无误；(16.82) 的 ↺/↻ 与印本一致。

**ch17**

6. (17.1)–(17.12)，`ch17.tex:100–180` vs `en/ch17_en.txt:120–190`（PDF p.281–282）：局部算子/线算子的边界条件叙述、$E_3$-代数的相对细化均忠实。
7. (17.13)–(17.28)，`ch17.tex:200–300` vs EN 230–330（PDF p.283–285）：L-因子作特征多项式、$\zeta(0)=-1/2$、Frobenius 分解图 (17.26) 均无误。
8. (17.54)–(17.57)，`ch17.tex:460–490`（PDF p.288）：`M^\vee/G^\vee` 的 $\Loc$ 定义、Frobenius 纤维、广义 L-函数读通；箭头问题见 §2.2-c。
9. (17.82)–(17.85)，`ch17.tex:676–700`（PDF p.291）：(17.83) 短正合列、$[F]\in G^\vee/G^\vee$、加倍为辛表示 $V=W\oplus W^*$ 均无误；新注内容正确（标签问题见 §2.1）。
10. (17.148)–(17.152)，`ch17.tex:1155–1200`（PDF p.299）：(17.148) 的 $X(K)/X(\mathcal O)$、Hecke 代数记号、$\Theta(\Phi)=\mathcal P_X$ 均照印本；新 GAP 与既有注都在同一式附近（见 §2.2-b）。
11. (17.155)–(17.163)，`ch17.tex:1216–1275` vs EN 1355–1425（PDF p.301–302）：$\Phi=k_{X(\mathcal O)}$、$\cA_X=\End_{\cH}(\Phi)$、$\Spec_{/(\mathfrak g^{\vee*}/G^\vee)}(\cA_X)$、$\mathrm{Gr}=G(\mathcal O)\backslash G(K)/G(\mathcal O)$ 均无误。
12. 抽读量词/否定（only、never、any、no longer、not）：`en/ch17_en.txt:37/250/358/361/476/550/591/743/766/775/861/892/976/1192/1382` 对应的译文均保留限定，未发现「漏 only/never/any」或「蕴含写成并列」；$\otimes/\oplus$、$H^*/H_*$、$Z/\mathcal Z$ 抽查未见混用。

**结构自检（两章）**：ch16 `\begin`=126、`\end`=126、`\tag`=101、`\label`=2、`$`=872（偶）、Tutor Note=11、GAP=1；ch17 `\begin`=196、`\end`=196、`\tag`=163（`\label` 计 165：163 个 `eq:17.xx` + 1 个图 label + 1 个 `ch:17`）、`$`=1432（偶）、Tutor Note=12、GAP=1。与 log 的自检数字一致；`\ref{fig:17-1}` 目标存在于 `ch17.tex:775`。

---

## §4 必须回滚 / 重做的项

**A. 必须回滚：无。**
10 项改动全部落地，且没有一项把正确的译文改错、把符号改反、或把原书笔误「改正」掉；ch16 的导出自交、两处脚注、`?` 箭头和 ch17 的「局部算子的」、`↺` 均可保留。

**B. 必须重做（P3，返工量小）：**

1. `ch16.tex:394` GAP：改写「依据」句——删去「作者他处用法与英文文本层均不足以判定」，补上全书 14 处 “spectrally decompose(s)/de-” 与唯一 1 处 “composes” 的对照；或降为普通 Tutor Note。当前文本把「证据不足」写成事实，属于注释失实。
2. `ch17.tex:688–692` 注：把 `[来源：译者按（无外部依据）：…]` 改为 `[译者按（无外部依据）：…]`（`校对规程.md` §4 第 4 项前面不带 `来源：`）。
3. `ch17.tex:1164` GAP：改写「$G(\mathcal O)$ 并无标准的正半部分」为「印本作 positive half of $G(\mathcal O)$；loop group 的 positive half 通常即 $G(\mathcal O)$，故按 $G(\mathcal O)$-不变理解（(17.149) 亦如此）」；或降为 Tutor Note，避免与既有注 `ch17.tex:1183` 重复。

**C. 必须由 lead 统一处理（不是本章校订员能独自完成的）：**

1. **ind-coherent 术语（P1）**：`ch16.tex:244、252、337、355` 应改为「ind-凝聚层」（或「归纳凝聚层」），首次出现夹注英文；同一误译还在 `ch16.tex:11`（keytakeaways，受保护）、`ch16.tex:391`（旧 Tutor Note，受保护）、`src/appendix_notes.tex:1000`（附录，跨文件）。建议先在 `appendix_glossary.tex` 增补一条「ind-coherent sheaf = ind-凝聚层」，再一次性替换，否则改 ch16 正文会造成正文与附录术语不一致。
2. **↷ / ↻ / ↺ 记号（P2）**：若决定按印本统一，ch16 的 (16.82) 与 ch17 的 8 处 `\circlearrowright`（362、484、502×2、595、596、677、713）及 31 处 `\curvearrowright` 需要一并核对；若维持译本现行约定，则不必动 ch17:466，但 log 的「全书统一」说法必须改掉，并建议在 ch16/ch17 各留一条极短的记号约定注（或列入 appendix_glossary 的记号表）。这是全书级决定，不宜在单章内零散改。
3. **ch17:639 “genus G”**：如本轮要处理，按「照译+加注」补一条短注；否则至少记入 log 的「存疑/待裁定」节，避免下轮再漏。

---

### 复核结论（一句话）

ch16/ch17 的本轮校订**没有改错、没有改出新错、没有落地失败**；真正的欠账是 ch16 的 ind-coherent 术语（P1，已登记未改），以及三处注释的文字/格式问题（P3）和 ch17:466 的理由表述（P2 记录问题，非改动错误）。
