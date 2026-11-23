# 审校报告 A：导引与 §1（SY02-32）

- 审校对象：`源码/sections/s01-intro.tex`（导引，原书 p.1–3）、`源码/sections/s02-sec1.tex`（§1，原书 p.3–12）
- 底本：Frenkel–Langlands–Ngô, « Formule des traces et fonctorialité : le début d'un programme », arXiv:1003.4578v2（法语，54 页）
- 方法：逐段对照 `工程文件/work/src/p001.txt`–`p012.txt`；公式与可疑字号用底本 PDF 按页放大 6×–10× 复核（缩放截图见附录 A）；术语对照 `工程文件/work/glossary.tsv`（137 条冻结表）；体例对照 `工程文件/SPEC.md`、`BRIEF.md`；已知疑点对照 `工程文件/work/疑点清单.tsv`（第 1 条 p.5 (1.7)(1.8) 的 v∉S/v∈S 为原文排版笔误、译本已照录加注，按委托不计为错误）。
- 声明：本次只读审校，未改动 `源码/`、`资料卡/` 下任何文件。
- 结论：共 **34 条**。按严重度：**高 1、中 12、低 21**（高/中必须修；低供参考）。

## 一、问题总览

| 严重度 | 条数 | 数学 | 漏译/语义 | 术语 | 文风 | 译注/体例 |
|---|---|---|---|---|---|---|
| 高 | 1 | 1 | 0 | 0 | 0 | 0 |
| 中 | 12 | 4 | 4 | 0 | 4 | 0 |
| 低 | 21 | 3 | 3 | 1 | 11 | 3 |
| 合计 | 34 | 8 | 7 | 1 | 15 | 3 |

修复优先级建议：① (1.7) 漏 `\sum_n`（唯一高）；② 导引两处语义（作者序数、求和方向）；③ §1 记号系统（`L_S`、`\rho^j_H`）与 (1.6) 余项指数的处理办法；④ `{}^LH` 与「中心核上的满同态」；⑤ 4 处病句。

---

## 二、高优先级（必须修）

| 位置 | 类型 | 严重度 | 问题 | 建议改法 |
|---|---|---|---|---|
| `s02-sec1.tex:84–88`（原书 p.7，(1.7)） | 数学 | 高 | 译本 (1.7) 缺少原文夹在 `\ln N\mathfrak p_v` 与花括号之间的 `\sum_n`。原文页面图为 `∑_{v∉S} ln N𝔭_v ∑_n { ∑_{π^st} m(π^st) ∏_{v∈S} tr π^st_v(f_v) · trρ^n(A(π_v))/N𝔭_v^{ns} }`（见附录 A 的 p7b.png）。漏掉后 `n` 成为无约束自由指标，`trρ^n` 与 `N𝔭_v^{ns}` 都失去意义；且译文 (1.7) 与 (1.8) 只差一个 `n`，读者看不出 (1.7) 是对 n 求和、而 (1.8) 只取 n=1 项。 | 在第 85 行 `\ln N\p_v` 后插入 `\sum_n`：`\sum_{v\notin S}\ln N\p_v\sum_n\left(\sum_{\pi^{\mathrm{st}}}m(\pi^{\mathrm{st}})\prod_{v\in S}\operatorname{tr}\pi^{\mathrm{st}}_v(f_v)\frac{\operatorname{tr}\rho^n(A(\pi_v))}{N\p_v^{ns}}\right),`（其余照旧；(1.8) 不动） |

---

## 三、中优先级（必须修）

| 位置 | 类型 | 严重度 | 问题 | 建议改法 |
|---|---|---|---|---|
| `s01-intro.tex:7`（原书 p.1） | 漏译/语义走样 | 中 | 「我们三人中的一位，Langlands，受第二位作者 Ngô……」「第三位作者 Frenkel 注意到」把原文的三人内部序数 "un deuxième"（我们中的另一位）、"Le troisième"（第三位）误成署名次序。按署名（Frenkel、Langlands、Ngô，见 p.1 页面图），「第二位作者」是 Langlands 而非 Ngô，「第三位作者」是 Ngô 而非 Frenkel，句内自相矛盾。 | 改为：「我们三人中的一位 Langlands，受我们中的另一位 Ngô 关于基本引理的工作的鼓舞——二十多年间基本引理一直没有证明，这在许多方面阻碍了自守形式解析理论的任何实质性进展——曾勾画过一个用以建立函子性的纲领，而函子性是这一理论的两个主要目标之一。第三位，Frenkel，注意到，……」 |
| `s01-intro.tex:15`（原书 p.2） | 漏译/语义走样 | 中 | 「差不多就是 $F$ 上有限维向量空间 $V$ 上某个函数在 $V\otimes\mathbb{A}_F$ 上求和」把原文 "une somme sur un espace vectoriel V de dimension finie sur F d'une fonction sur V⊗A_F" 的求和域与函数定义域颠倒：原文是「沿 $V$ 求和，被求和的是 $V\otimes\mathbb{A}_F$ 上的函数」。现译成「$V$ 上的函数在 $V\otimes\mathbb{A}_F$ 上求和」，数学上正好相反。 | 改为：「……就是对一个 $F$ 上有限维向量空间 $V$ 求和，被求和的是定义在 $V\otimes\mathbb{A}_F$ 上的一个函数；该函数的行为使得可以对 $V\subset V\otimes\mathbb{A}_F$ 这一对使用 Poisson 公式。」 |
| `s02-sec1.tex:20`（原书 p.4） | 漏译/语义走样 | 中 | 「一个中心核上的满同态」误读 "un homomorphisme surjectif … à noyau central"：原文 "à noyau central" 修饰 homomorphisme（核为中心的满同态），不是「在中心核上」。 | 改为：「一个核为中心的满同态」，整句为「人们甚至要在 $F$ 上找一个约化群 $H$、一个核为中心的满同态 $\psi:{}^LH\longrightarrow{}^{\lambda}H\subset{}^{\lambda}G_\varphi$，以及一个表示 $\pi_H$……」 |
| `s02-sec1.tex:106`（原书 p.8） | 漏译/语义走样 | 中 | 原文 "de façon qu'en principe les fonctions L pour lesquelles les sommes (1.7) ou (1.8) n'ont pas de pôle à la droite de la ligne Re s = 1"（原文此句本身有脱误，见下）。译本作「从而原则上使 (1.7) 或 (1.8) 中的和没有位于直线 Re s=1 右侧的极点」，丢掉了 "les fonctions L"，把「L 函数无极点」说成「和无极点」——而「和没有极点」在这一语境中不成立。 | 改为：「从而原则上使 (1.7)、(1.8) 中出现的 $L$ 函数在直线 $\operatorname{Re}s=1$ 右侧没有极点。」并在该句后加译注：`\yizhu{原文此处语句有脱误（「les fonctions L pour lesquelles les sommes (1.7) ou (1.8) n'ont pas de pôle…」），按上下文应理解为 $L$ 函数无极点，译文据此译出。}{依据：原书 p.8；对照 (1.7)、(1.8)}` |
| `s02-sec1.tex:166`（原书 p.11） | 数学 | 中 | 「来自 ${}^LH$ 且 $\rho$ 限制到 ${}^{\lambda}H$ 不含平凡表示的」——原文 "celles qui proviennent des sous-groupes λH tels que la restriction de ρ à λH ne contient pas de représentation triviale"，来源也是 `${}^{\lambda}H$。译文前半用 `${}^LH$`，与后半 `${}^{\lambda}H$` 矛盾，改变了「按子群分类」的含义（同段下文与 (1.10) 都用 `${}^{\lambda}H$`）。 | 改 `${}^LH$` 为 `${}^{\lambda}H$`：`来源 ${}^{\lambda}H$ 且 $\rho$ 限制到 ${}^{\lambda}H$ 不含平凡表示的，以及其余的`。 |
| `s02-sec1.tex:35、:44、:52、:72–73、:104、:149、:155、:176`（原书 p.5–12） | 数学 | 中 | 原文部分 $L$ 函数一律用 **下标**：$L_S(s,\pi,\rho)$、$L'_S(s,\pi,\rho)$（p.5 (1.1′)(1.3)、p.7 (1.5) 三处已用 10 倍放大页面图确认下标，见附录 A 的 p5_11p.png、p5_12_13.png、p7_15.png；p.8–p.10 各处文字层同样作 LS，可视为同一写法）。译本全部改为 **上标** `L^S`，且无任何说明，违反「公式按原文逐符号」。 | 方案一（推荐）：全部改回下标，如 `L_S(s,\pi,\rho)=\prod_{v\notin S}L(s,\pi_v,\rho).`；`-\frac{L'_S(s,\pi,\rho)}{L_S(s,\pi,\rho)}=-\sum_{v\notin S}\frac{L'_v(s,\pi,\rho)}{L_v(s,\pi,\rho)}=\sum_{v\notin S}\ln N\p_v\sum_n\frac{\operatorname{tr}\rho^n(A(\pi_v))}{N\p_v^{ns}}.` 方案二：保留上标，但在 (1.1′) 后加一条译注：`\yizhu{原文部分 $L$ 函数记作 $L_S$（下标 $S$）；为与通行的上标写法一致，译本改为 $L^S$，其余符号照原文。}{依据：原书 p.5}` |
| `s02-sec1.tex:40、:44、:48`（原书 p.5） | 数学 | 中 | 原文 $\rho^j_H$（$j$ 为上标、$H$ 为下标，(1.2)(1.3) 页面图确认）被系统性改写为 $\rho_{H,j}$；同样未加说明。 | 改回：`:40` 作 `\bigoplus_j\sigma_j\otimes\rho^j_H,`；`:44` 作 `L_S(s,\pi,\rho)=\prod_j\prod_i L_S(s+i,\pi_H,\rho^j_H),`；`:48` 作 `$L_S(s,\pi_H,\rho^j_H)$`。（若统一改上标，须按上一条加译注说明。） |
| `s02-sec1.tex:79`（原书 p.7） | 数学 | 中 | (1.6) 的余项原文印作 $O(1/N\mathfrak p_v^{2})$（10 倍放大图 p7_16b.png 确认上标只有 2，无 s），译本径改为 $O(1/N\p_v^{2s})$ 且无译注。数学上 $2s$ 才自洽，但按项目规矩「原文笔误须照录并加注」，不能径改。 | 照录并加注：`+\sum_{v\notin S}O\!\left(\frac{1}{N\p_v^{2}}\right).` 后加 `\yizhu{原文此处印作 $N\mathfrak p_v^{2}$；按 (1.5) 的 Ramanujan 估计，$n\ge2$ 的项应为 $N\mathfrak p_v^{-2s}$，译文照原文排印。}{依据：原书 p.7 页面图}`（若坚持保留 $2s$，也必须加同类译注。） |
| `s02-sec1.tex:18`（原书 p.4） | 文风 | 中 | 「甚至对每个位 $v$，是局部 Weil 群到 ${}^{\lambda}G_{\varphi,v}$ 中的一个同态。」整句无主语，是上句枚举（「首先……其次……」）的残片，单独成句后不成话。 | 改为：「甚至对每个位 $v$，还有局部 Weil 群到 ${}^{\lambda}G_{\varphi,v}$ 中的一个同态。」 |
| `s02-sec1.tex:5`（原书 p.3） | 文风 | 中 | 「以及如何借助它来期望实现这些目标」把 "comment avec son aide on peut espérer les réaliser" 直译成「来期望实现」，动词叠加、语义含混。 | 改为：「以及如何借助它有望实现这些目标」。 |
| `s02-sec1.tex:57`（原书 p.6） | 文风 | 中 | 「因此这个差应期望是 $\operatorname{Re}s>1$ 中的全纯函数」——"est censée être" 是「理应/应是」，「应期望是」既非中文也误译。 | 改为：「因此这个差理应是 $\operatorname{Re}s>1$ 上的全纯函数」。 |
| `s02-sec1.tex:59`（原书 p.6） | 文风 | 中 | 「首先减去满足 $\varphi$ 非平凡的配对 $(\varphi,\psi)$ 的贡献」——「满足」后接形容词性小句，搭配错误（原文 "les paires telles que φ n'est pas trivial"）。 | 改为：「首先减去那些 $\varphi$ 非平凡的配对 $(\varphi,\psi)$ 的贡献」。 |

---

## 四、低优先级（供参考）

| 位置 | 类型 | 严重度 | 问题 | 建议改法 |
|---|---|---|---|---|
| `s01-intro.tex:7` | 术语 | 低 | 「代数几何（算术的或非算术的）」把 "diophantienne ou non" 译作「算术的」；diophantienne 是「丢番图的」，与「算术的」不等价。 | 「自守形式与代数几何（丢番图的或非丢番图的）之间预期的联系」。 |
| `s01-intro.tex:7、10、12、15、17` | 文风 | 低 | 超过 SPEC 的 70 字上限：:7 首句 106 字、:10 首句 79 字、:12 首句 84 字、:15 两句 73/88 字；:17「强调……之重要，怎么强调都不为过」把 "Il est impossible de souligner toute l'importance" 的「强调」重复两次。 | :7 在「而函子性是这一理论的两个主要目标之一」处断句；:12 在「处理复代数曲线上的理论」处断句；:15 在「差不多就是……」前断句；:17 改为「这种处理迹公式所提出的解析问题的可能性，其重要性无法过分强调。」 |
| `s01-intro.tex:9` | 文风 | 低 | 「基本引理现在已由 [N] 的结果得到」——「已由……得到」缺「确立」；「已近在手边」宜「已近在咫尺」。 | 「基本引理现已借助 [N] 的结果得到确立，因此稳定迹公式已近在咫尺。」 |
| `s01-intro.tex:15` | 漏译（增译） | 低 | 「$\mathbb{F}_q$ 上曲线 $X$ 的函数域 $F$」中的 $X$ 为增译：原文只作 "une courbe sur Fq"，曲线 $X$ 至 §2（p.12）才引入。 | 删去 $X$：「$\mathbb{F}_q$ 上某条曲线的函数域 $F$ 的自守形式」。 |
| `s01-intro.tex:9` | 译注 | 低 | 译注称「Ngô Bao Châu 于 2008 年宣布证明基本引理」，但 2008 年宣布一事不在原书 p.1（p.1 只说 "grâce aux résultats de [N]"），来源却标「原书 p.1 与文献 [N]」；文献 [N] 条目为 `B. C. Ngô, Le lemme fondamental pour les algèbres de Lie, Publ. Math. IHÉS No. 111 (2010), 1--169`，与注文一致。 | 来源改为：`{依据：文献 [N] 条目；「2008 年宣布」为学界公认事实（B 级），非原书 p.1 内容}` |
| `s02-sec1.tex:5` | 文风 | 低 | 「尽管 Arthur 做出了英勇而根本的贡献」——"héroïques" 用于数学贡献，中文「英勇」多指战斗气概。 | 「尽管 Arthur 做出了卓绝而根本的贡献」。 |
| `s02-sec1.tex:11` | 文风 | 低 | 公式后另起一句「附属于一个群 $G$ 的自守形式——更确切地说自守形式的 $L$-包——以及其 $L$-群的一个表示 $\rho$。」缺谓语，是残句（原文 "rattachés à…" 分词句）。 | 并入上句：「$L$ 函数是（对所有有限或无限位 $v$ 取）乘积 (1.1)，它附属于一个群 $G$ 的自守形式——更确切地说，附属于自守形式的 $L$-包——以及其 $L$-群的一个表示 $\rho$。」 |
| `s02-sec1.tex:15` | 文风 | 低 | 「把若干对象附属于一个自守表示」——"rattacher à" 直译，中文搭配生硬。 | 「把若干对象联系到一个自守表示 $\pi=\pi_G$ 上」。 |
| `s02-sec1.tex:18` | 漏译 | 低 | 原文 "On s'attend même à pouvoir construire…" 的 "même"（甚至）未译。 | 「人们甚至希望构造一个自守 Galois 群……」。 |
| `s02-sec1.tex:20` | 文风 | 低 | 「大得无用且笨重」——"inutilement gros et guindé" 的 guindé 意为「生硬、矜持、不自然」，非「笨重」。 | 「会大得无用且生硬」。 |
| `s02-sec1.tex:26` | 数学 | 低 | 原文 p.4 公式 $\{A(\pi_v)\}=\{\psi(A(\pi_{H,v})\}$ 确少一个右括号（页面图确认），译本径补为 `\{\psi(A(\pi_{H,v}))\}` 未加注，违反「原文笔误照录加注」；补括号本身可取。 | 保留补正，但加注：`\yizhu{原文此式少一个右括号，译文补足。}{依据：原书 p.4 页面图}` |
| `s02-sec1.tex:30` | 文风 | 低 | 「人们预期能够利用稳定迹公式做适当的递推……一方面……另一方面……」一句 99 字，超出 70 字上限。 | 在「并依据函子性原则证明两件事：」后拆成两句陈述。 |
| `s02-sec1.tex:37` | 译注/体例 | 低 | 「原文此处把 (1.1) 与部分 $L$ 函数共用同一编号……」是一条未套 `\yizhu` 的裸说明，会作为正文排出。 | 改为 `\yizhu{原文此处把 (1.1) 与部分 $L$ 函数共用同一编号，译本为免混淆，将部分 $L$ 函数标作 (1.1$'$)，其余编号照原文。}{依据：原书 p.5}` |
| `s02-sec1.tex:48` | 数学 | 低 | 「$L(s,\pi,\rho)$ 可解析延拓到直线 $\operatorname{Re}s=1$」——原文 "se prolonge"；本节随后正讨论该直线上的极点，故不是全纯的「解析延拓」。 | 「$L(s,\pi,\rho)$ 可延拓到直线 $\operatorname{Re}s=1$」。 |
| `s02-sec1.tex:54` | 文风 | 低 | 「使 $\varphi$ 的像与 ${}^LH$ 交换的 $\varphi$」——「使……交换」把 φ 当成施动者，原文是 φ 的像与 ${}^LH$ 交换。 | 「以及那些其像与 ${}^LH$ 交换的 $\varphi$」。 |
| `s02-sec1.tex:57` | 文风 | 低 | 相邻两句均以「显然」开头（「显然这个问题不会容易。……显然，上述讨论隐含了……」），重复。 | 后一句改为「应当说，上述讨论已隐含了一般函子性的证明。」 |
| `s02-sec1.tex:59` | 文风 | 低 | 「最后我们就把 $\varphi$ 假定为平凡的 $\pi$ 分离出来」语序拗口；「目标是从右到左依次处理」漏掉 "d'en tenir compte" 的宾语。 | 「最后我们分离出那些 $\varphi$ 应为平凡的 $\pi$」；「目标是按从右到左的顺序依次把它们考虑进去」。 |
| `s02-sec1.tex:76` | 译注 | 低 | 原文 p.7 重出 "la conjecture de la conjecture de Ramanujan"（页面图确认），译本径作「Ramanujan 猜想」未加注。 | 保留译文，加注：`\yizhu{原文此处「de la conjecture」重出，译文未复。}{依据：原书 p.7}` |
| `s02-sec1.tex:112` | 数学 | 低 | 「以及 $\rho$ 到 ${}^LH\to{}^LG$ 的限制 $\rho_H$」照原文压缩语序硬译，易读成「限制到映射上」；原意是 $\rho$ 限制到 ${}^LH$ 得 $\rho_H$（经 ${}^LH\to{}^LG$ 视为 ${}^LG$ 的表示）。 | 「以及 $\rho$ 到 ${}^LH$ 的限制 $\rho_H$（经 ${}^LH\to{}^LG$ 视为 ${}^LG$ 的表示）」。 |
| `s02-sec1.tex:122` | 漏译 | 低 | 「刚才描述的东西会是对函子性的一个确认」漏译 "en utilisant la formule des traces stable"（用稳定迹公式得到的确认）。 | 「刚才描述的东西会是用稳定迹公式对函子性的一个确认，但这不是我们所提议的。」 |
| `s02-sec1.tex:164` | 文风 | 低 | 「即从迹公式中提取其他非 Ramanujan 型表示——从而联系于既非平凡也非主嵌入的 $\varphi$——的贡献」破折号插入把「表示……的贡献」割裂。 | 改为：「即从迹公式中提取其他非 Ramanujan 型表示（它们联系于既非平凡也非主嵌入的 $\varphi$）的贡献」。 |

---

## 五、已核实、无需修改的部分

1. **术语与冻结表一致**：逐条核对 `glossary.tsv` 中 §1 相关条目——formule des traces 迹公式、formule des traces stable 稳定迹公式、fonctorialité 函子性、L-paquet L-包、L-groupe L-群、endoscopie 内窥、lemme fondamental 基本引理、classe de conjugaison 共轭类、centralisateur 中心化子、droite critique 临界线、bande critique 临界带、hypothèse de Ramanujan Ramanujan 假设、type Ramanujan Ramanujan 型、multiplicité 重数、terme dominant 主项、contribution dominante 主贡献、transfert 转移、quasi-déployé 拟分裂、sous-groupe hyperspécial 超特殊子群、algèbre de Hecke Hecke 代数、corps de classes 类域、réciprocité 互反律、correspondance de Langlands Langlands 对应、représentation ℓ-adique ℓ-进表示——全部一致，未发现违背冻结译法。（「主部」用于 partie principale，冻结表未收，不计违背。）
2. **让步/猜测语气保留**：逐句核对，除中-10 一处外均保留："Nous espérons néanmoins qu'ils lisent…"「我们仍希望他们……仔细阅读」；"on ne s'attend pas à ce que ces données soient uniques"「并不预期这些数据是唯一的」；"au moins en principe / en principe"「至少原则上 / 原则上」；"ne devraient avoir ni pôle ni zéro"「应既无极点也无零点」；"Ils sont censés ne pas exister"「它们被认为不存在」；"on peut espérer pouvoir écarter"「可以希望……排除」；"n'est pas tenue pour réaliste"「并不现实」；"Il s'agit d'un projet mais d'un projet qui est censé mener à sa propre réalisation"「这是一个计划，而且是一个理应导致自身实现的计划」（"mener à" 译「导致」宜改「带来」，但语气正确）。
3. **公式落位**：(1.1)–(1.14) 编号与原文一一对应；(1.1′) 为译本自设（原文与 (1.1) 共用编号），已有说明。逐式核对指标、上下标、求和/乘积范围，除本报告所列三处（(1.7) 漏 `\sum_n`；(1.6) 余项的 2 与 2s；部分 $L$ 函数与 $\rho^j_H$ 的记号改动）外与原文一致；(1.8)(1.9)(1.11)(1.12)(1.14) 完全一致；(1.10) 的内层迹译本写作 $\pi^{\mathrm{st}}_{H,v}$、原文作 $\pi^{\mathrm{st}}_v$，属澄清性增字（语义无误，可不必改，记录备查）。
4. **结构**：`\srcpage{1}`–`\srcpage{12}` 与原文页一一对应；导引 5 段对原文 5 段；§1 编号公式与段落切分忠实。
5. **禁用句式**：全文未出现「被……所……」「对于……而言」「进行……的讨论」；未见连续三个「的」的病句。
6. **译注**：本范围共 6 条（导引 1、§1 5），正文均 ≤120 字，格式统一为 `\yizhu{…}{依据：…}`；事实核对：λ-群记号说明、Ramanujan 型说明、(1.7)(1.8) 笔误说明、稳定重数说明（带 I 级来源）均与原文相符；[N] 条目为 `Publ. Math. IHÉS No. 111 (2010), 1--169`，与导引译注一致。
7. **编译状态**：`工程文件/reports/分章报告.md` 记录 xelatex 两遍 39 页、0 error；本次为只读审校，未重编译。

---

## 附录 A：核对用的页面放大图

均在 `C:/Users/admin/Downloads/_rev_a/`（由底本 PDF 用 pymupdf 渲染裁剪）：

| 文件 | 内容 |
|---|---|
| `p7b.png` | p.7 (1.5)–(1.8) 整段：(1.7) 的 `∑_n` 与 (1.8) 无 `∑_n` |
| `p7_16b.png` | p.7 (1.6) 余项 10×放大：$O(1/N\mathfrak p_v^{2})$（上标只有 2） |
| `p7_15.png` | p.7 (1.5) 10×放大：$L'_S$、$L_S$ 为下标 |
| `p5_11p.png`、`p5_12_13.png` | p.5 (1.1′)(1.2)(1.3)：下标 $L_S$、上标 $\rho^j_H$ |
| `p4_psi.png`、`p4_br.png`、`p4_eq.png` | p.4：$\psi$ 式、"à noyau central" 的断行、原文缺右括号 |
| `p1_top.png` | p.1 标题与署名顺序（Frenkel、Langlands、Ngô） |

## 附录 B：页–行对照

- `s01-intro.tex`：:5 → p.1 起；:7–:12 → p.1–2；:15–:17 → p.2；:20 → p.3。
- `s02-sec1.tex`：:3–:18 → p.3–4；:20–:30 → p.4；:33–:48 → p.5；:50–:59 → p.6；:61–:81 → p.7；:83–:106 → p.7–8；:108–:122 → p.8–9；:124–:141 → p.9–10；:143–:164 → p.10–11；:166–:179 → p.11–12。

## 附录 C：限制说明

- `工程文件/work/pages/` 仅有 p004.png、p005.png 两张页面图；其余页的公式核对直接用底本 PDF 按页渲染（pymupdf 2.1）。
- 本报告的行号基于当前 `源码/sections/*.tex`（s01 共 20 行、s02 共 179 行）。
