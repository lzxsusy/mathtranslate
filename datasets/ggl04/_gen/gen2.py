# -*- coding: utf-8 -*-
"""生成 ggl04 其余概念卡与全部推导卡。"""
import json, os
ROOT = os.path.join(os.path.dirname(__file__), "..")
CON = os.path.join(ROOT, "cards", "concepts")
DER = os.path.join(ROOT, "cards", "derivations")

cards = []

cards.append({
 "id": "ggl04/concept/k-invariant-lagrangian",
 "type": "concept",
 "title": "K-不变 Lagrange 膜与 $\\mathbb R^3$ 中的曲线 $\\ell$",
 "aliases": ["K-invariant Lagrangian", "curve l in R3"],
 "track": "D",
 "summary": "极大紧子群 $U(1)$ 不变的 Lagrange 膜是 moment map 下 $\\mathbb R^3$ 中曲线 $\\ell$ 的原像；$\\ell$ 的三种端点情形给出 $S^2$、$\\mathbb R^2$、$\\mathbb R\\times S^1$。",
 "question": "$K\\cong U(1)$ 不变的 Lagrange 膜为什么能用 $\\mathbb R^3$ 里的一条曲线来分类？",
 "definition": {
  "text": "在 $SU(2)$ 与 $SL(2,\\mathbb R)$ 的例子里，$J_z$ 生成极大紧子群 $K\\cong U(1)$。$Y$ 作为 Gibbons–Hawking 空间带 moment map $\\vec w:Y\\to\\mathbb R^3$，$K$ 旋转 $S^1$ 纤维。若 $B'$ 的支撑 $M$ 在 $K$ 下不变，则 $M=\\pi^{-1}(\\ell)$，$\\ell\\subset\\mathbb R^3$ 是 moment map 下的曲线。由 $\\omega_Y|_M=d\\chi\\wedge dw_3$ 知 $\\ell$ 必须落在常 $w_3$ 的平面 $w_3=b$ 内；$\\omega_J|_M$ 非退化当且仅当 $dw_2$ 沿 $\\ell$ 处处非零，即 $\\ell$ 可写成 $w_1=f(w_2)$。",
  "notation": "$K\\cong U(1)$ 由 $J_z$ 生成，$\\vec w$ 为 moment map，$\\ell$ 为平面 $w_3=b$ 中的曲线，$\\chi$ 为 $S^1$ 纤维坐标，$b$ 为位移参数。"
 },
 "key_points": [
  "三种拓扑由 $\\ell$ 的端点决定：连接 $\\pm\\vec w_*$ 给 $M\\cong S^2$（$SU(2)$ 情形）；一端到无穷、一端终止于定点给 $M\\cong\\mathbb R^2$（离散系列）；两端都到无穷给 $M\\cong\\mathbb R\\times S^1$（主系列与互补系列）。",
  "闭合的 $\\ell$ 不允许：$M=\\pi^{-1}(\\ell)$ 会包围一个盘，盘上 $\\omega_Y$ 的通量不为零，被 $M$ 界定的膜不存在。",
  "$\\mathbb R\\times S^1$ 情形有两个实模：沿 $S^1$ 的 Wilson 线 $\\exp(2\\pi i\\delta)$ 与位移 $b$；A-模型只依赖 $\\delta+ib$ 的全纯函数，故 $s=\\delta+ib+\\mathrm{const}$ 是模空间的自然坐标。",
  "$\\ell$ 的方向决定膜的类型：竖直（沿 $w_3$）$\\Rightarrow M$ 在 $J$ 中全纯、$(A,B,A)$，退化为 Kähler 极化量子化；水平（沿 $w_2$）$\\Rightarrow\\omega_J|_M=0$、$(B,A,A)$，给出 $D$-模（§3.9）。",
  "$\\ell$ 是否终止于定点决定谱是否有界：终止时有最高/最低权态（$J_z$ 谱半有界）；不终止时谱双边无界，得 Harish-Chandra 模。"
 ],
 "formulas": [
  "$\\vec w:Y\\to\\mathbb R^3,\\qquad M=\\pi^{-1}(\\ell),\\qquad \\ell\\subset\\{w_3=b\\}$",
  "$\\omega_Y|_M=d\\chi\\wedge dw_3,\\qquad \\omega_J|_M\\ \\text{非退化}\\iff dw_2|_\\ell\\neq0$",
  "$ds^2=H\\,d\\vec w\\cdot d\\vec w+H^{-1}(d\\chi+\\vec a\\cdot d\\vec w)^2,\\qquad \\nabla\\times\\vec a=\\nabla H$"
 ],
 "theorems": [
  {
   "name": "$K$-不变 Lagrange 膜的拓扑分类",
   "statement": "设 $M\\subset Y$ 是 $K\\cong U(1)$ 不变的 Lagrange 膜且 $\\omega_J|_M$ 非退化，则 $M$ 的拓扑只有 $S^2$、$\\mathbb R^2$、$\\mathbb R\\times S^1$ 三种，分别对应 $\\ell$ 连接两个定点、终止于一个定点、两端无穷。",
   "proof": {
    "status": "sketch",
    "steps": [
     {"no": 1, "text": "$K$ 不变性与维数迫使 $M=\\pi^{-1}(\\ell)$，且 $\\omega_Y|_M=d\\chi\\wedge dw_3$ 为辛形式要求 $w_3$ 在 $\\ell$ 上为常数。", "why": "这一步把膜的分类问题降成平面里曲线的分类。"},
     {"no": 2, "text": "$S^1$ 纤维在 $\\ell$ 的两端可以收缩（当端点趋于两个定点 $\\pm\\vec w_*$ 时）或不收缩，据此读出 $M$ 的拓扑。", "why": "端点行为决定纤维是否退化，从而决定 $M$ 是 $S^2$、$\\mathbb R^2$ 还是 $\\mathbb R\\times S^1$。"}
    ],
    "gap_note": "原文只列出三种并逐例对应（§3.2、§3.3、§3.4），未证明没有第四种；本卡按原文表述记为 sketch。"
   },
   "source": "A p.50 §3.7"
  }
 ],
 "pitfalls": [
  "不要把 $\\ell$ 当成 $M$ 本身：$M$ 是 $\\ell$ 上 $S^1$ 纤维的原像，维数比 $\\ell$ 高一维。",
  "不要以为闭合 $\\ell$ 也能用：盘上的 $\\omega_Y$ 通量使膜不存在（原文用盘瞬子论证）。",
  "不要忽略 $w_3$ 必须为常数：$\\omega_Y|_M=d\\chi\\wedge dw_3$ 要求 $\\ell$ 落在水平面内，否则 $\\omega_Y|_M$ 不是辛形式。"
 ],
 "related": ["ggl04/concept/harish-chandra-curve", "ggl04/deriv/casimir-from-curve", "ggl04/concept/brane-quantization"],
 "sources": [
  {"text": "A", "section": "3.7. Harish-Chandra Modules From Branes", "pages": [46, 46], "anchor": "A p.46 eq (3.46)", "quote": "It is convenient to use the fact that Y admits a family of hyper-Kahler metrics"},
  {"text": "A", "section": "3.7", "pages": [49, 49], "anchor": "A p.49 §3.7", "quote": "There are thus three topologies for M"},
  {"text": "A", "section": "3.7", "pages": [50, 50], "anchor": "A p.50 §3.7", "quote": "this is equivalent to saying that dw2 is everywhere nonzero along"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "A 为主（§3.7 的 Gibbons–Hawking 形式与三条拓扑）。最没把握的是「没有第四种拓扑」：原文只说 there are thus three，未给完整证明。"
})

cards.append({
 "id": "ggl04/concept/harish-chandra-curve",
 "type": "concept",
 "title": "Harish-Chandra 模的曲线参数 $s=\\delta+ib$",
 "aliases": ["HC module from curve", "s parameter of curve brane"],
 "track": "E",
 "summary": "只要求渐近 $SL(2,\\mathbb R)$ 不变的膜给出 Harish-Chandra 模；$J_z$ 谱 $s+n$ 中的复参数 $s=\\delta+ib+\\mathrm{const}$，实部是单值、虚部是位移。",
 "question": "非酉的 $SL(2,\\mathbb R)$ 表示怎样用一条只渐近不变的曲线膜实现？",
 "definition": {
  "text": "对不必酉的 $SL(2,\\mathbb R)$ 表示，$J_z$ 的本征值是 $s+n$（$n$ 跑遍一段连续整数，$s\\in\\mathbb C$），这类模称为 Harish-Chandra 模。它不能由 $K$-不变的 Lagrange 膜得到：那要求 $\\ell$ 精确地终止于定点，于是谱半有界。改用只渐近 $SL(2,\\mathbb R)$ 不变的膜（$\\ell$ 在无穷远处趋于 $w_2$ 轴但不终止于定点），则 $J_z$ 谱双边无界。此时模空间坐标是 $s=\\delta+ib+\\mathrm{const}$：$\\delta$ 是沿 $S^1$ 的单值（Wilson 线），$b$ 是 $S^1$ 纤维的位移。",
  "notation": "$s\\in\\mathbb C$ 为 $J_z$ 谱的平移，$\\delta$ 为单值参数，$b$ 为位移，$\\mu=\\beta+i\\gamma$ 为周期，$\\eta$ 为世界面 $\\theta$ 角。"
 },
 "key_points": [
  "判据是谱：$J_z$ 本征值为 $s+n$、每个 $n$ 重数有限；$s$ 只定义到加整数，故参数空间是 $\\mathbb C/\\mathbb Z$。",
  "$\\ell$ 终止于 $\\pm\\vec w_*$ 时才有最高/最低权（谱半有界）；只渐近趋于定点而不终止时两类权都不出现，得到双边无界的 HC 模——这正是 §3.8 讨论的可约性与形变。",
  "参数关系 $\\mu=\\beta+i\\gamma=\\eta+i\\gamma+n$ 与 $\\mu/2=s+n+1/2$ 合起来给 $J^2=(\\mu^2-1)/4=(s+n)(s+n+1)$，即 (3.57)。",
  "$\\mathrm{Im}\\,s=\\gamma/2$ 由 A-模型复结构定：$\\delta+ib$ 全纯，故 $b$ 与 $\\gamma$ 绑定（(3.55) $b=\\gamma/2$），$\\delta$ 与 $\\eta$ 配对。",
  "并非所有 HC 模都来自 A-膜：Casimir 的形变值 $c'_i$ 要满足可积性/整性条件，否则 $B_{cc}$ 不存在（§3.10）。"
 ],
 "formulas": [
  "$J_z\\psi=(s+n)\\psi,\\qquad n\\in\\mathbb Z,\\ s\\in\\mathbb C$",
  "$s=\\delta+ib+\\mathrm{const},\\qquad b=\\gamma/2,\\qquad \\mu/2=s+n+1/2$",
  "$J^2=\\dfrac{\\mu^2-1}{4}=(s+n)(s+n+1)$"
 ],
 "theorems": [
  {
   "name": "曲线参数与 Casimir 的对应",
   "statement": "设膜只渐近 $SL(2,\\mathbb R)$ 不变、$\\ell$ 渐近平行于 $w_2$ 轴，则 $J_z$ 谱为 $\\{s+n\\}$，且 $J^2=(s+n)(s+n+1)$，其中 $\\mu/2=s+n+1/2$、$\\mu=\\beta+i\\gamma$。",
   "proof": {
    "status": "complete",
    "steps": [
     {"no": 1, "text": "$\\ell$ 渐近平行于 $w_2$ 轴使 $w_2$ 沿 $M$ 无下界，而 $w_2$ 是 $K$ 的 moment map，故 $J_z$ 谱为 $\\{s+n\\}$，$s$ 定义模 1。", "why": "把几何上的无界性翻译成谱的双边无界，这是 HC 模区别于离散系列的标志。"},
     {"no": 2, "text": "单值 $\\delta$ 给 $\\mathrm{Re}\\,s$，位移 $b$ 给 $\\mathrm{Im}\\,s$；A-模型在 $\\delta+ib$ 上全纯，故 $s=\\delta+ib+\\mathrm{const}$。", "why": "这是 (3.54)；全纯性保证两个实模合成一个复参数。"},
     {"no": 3, "text": "要得到最高/最低权需 $\\ell$ 终止于定点，此时 $b=\\gamma/2$，故 $\\mathrm{Im}\\,s=\\gamma/2$；结合 $\\mu=\\beta+i\\gamma=\\eta+i\\gamma+n$ 得 $\\mu/2=s+n+1/2$，于是 $J^2=(\\mu^2-1)/4=(s+n)(s+n+1)$。", "why": "把曲线参数、周期与 Casimir 三者对齐，是全文把表示论翻译成几何的核心等式。"},
     {"no": 4, "text": "常数取 $1/2$：$\\mu=\\beta=\\gamma=0$ 的最高/最低权模有 $s=1/2$（§3.3 的 $D^\\pm_0$）。", "why": "定出唯一待定常数，使 (3.57) 与 (3.7) 在 $\\mu=n$ 时一致。"}
    ],
    "gap_note": ""
   },
   "source": "A p.51 eq (3.57)"
  }
 ],
 "pitfalls": [
  "不要以为 HC 模一定是酉的：多数 $s$ 给非酉模；酉性要求 $s$ 落在主系列 $s=-1/2+i\\nu$ 或离散系列的离散点上。",
  "不要把 $s$ 与 $J^2$ 混同：$J^2=s(s+1)$ 只在最高/最低权态上成立，一般 HC 模里 $J_z$ 谱是 $s+n$，Casimir 由 $\\mu$ 单独定。",
  "不要忽略 $s$ 与 $s+1$ 等价：参数空间是 $\\mathbb C/\\mathbb Z$，不是整个 $\\mathbb C$。"
 ],
 "related": ["ggl04/concept/k-invariant-lagrangian", "ggl04/deriv/casimir-from-curve", "ggl04/concept/unitarity-by-tau"],
 "sources": [
  {"text": "A", "section": "3.7", "pages": [45, 45], "anchor": "A p.45 §3.7", "quote": "Such representations are known mathematically as Harish-Chandra modules"},
  {"text": "A", "section": "3.7", "pages": [51, 51], "anchor": "A p.51 eq (3.54)", "quote": "the imaginary part of µ is twice the imaginary part of s"},
  {"text": "A", "section": "3.8", "pages": [52, 52], "anchor": "A p.52 §3.8", "quote": "This is what we expect for a brane associated to a highest or lowest weight representation"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "A 为主；第 4 步的常数 $1/2$ 依据 §3.3 的 $D^\\pm_0$（$s=1/2$）。最没把握的是「只渐近不变」的精确判据：原文自认不知道 “suﬃciently close” 的正确判据。",
 "corrections": [{"id": "E3", "note": "原文 p.51 引 (3.11) 得 $\\mu=\\beta+i\\gamma=\\eta+i\\gamma+n$；实际用到的是 (3.16)（$\\beta=\\eta+n$）与 (3.17)（$\\mu=\\lambda+n$），(3.11) 只给 $\\mu=\\beta+i\\gamma$。见 errata E3。"}]
})

cards.append({
 "id": "ggl04/concept/b-a-a-d-module",
 "type": "concept",
 "title": "水平曲线的 $(B,A,A)$ 膜与 $D$-模",
 "aliases": ["BAA brane", "D-module from brane"],
 "track": "E",
 "summary": "当 $\\ell$ 水平时 $M$ 在 $I$ 中全纯、$\\omega_J|_M=0$，$(B_{cc},B')$ 弦给的是 $D$-模而非量子化，扭化为 $K^{1/2}\\otimes\\mathcal O(1)^\\lambda$。",
 "question": "同一条曲线图景里，什么时候得到的是 $D$-模而不是量子化？",
 "definition": {
  "text": "在 §3.7 的曲线图景里，若 $\\ell$ 取水平方向（沿 $w_2$），则 $M$ 在复结构 $I$（而非 $J$）中全纯，且 $\\omega_J|_M=0$。这时 $B'$ 是 $(B,A,A)$ 型膜，$(B_{cc},B')$ 弦空间不是 $M$ 的量子化，而是 $M$ 上某个 $D$-模的整体截面。具体地，$Y$ 是 $T^*\\mathbb{CP}^1$ 的仿射形变，$M'=\\mathbb{CP}^1\\setminus\\{0,\\infty\\}$，$D$-模由 $K^{1/2}\\otimes\\mathcal O(1)^\\lambda$ 扭转，$\\lambda=\\eta+i\\gamma$。",
  "notation": "$I,J$ 为两个复结构；$(B,A,A)$ 表示 $B_{cc}$ 端 $B$-型、$B'$ 端 $A$-型；$\\lambda=\\eta+i\\gamma$ 扭化参数；$K^{1/2}$ 半形式。"
 },
 "key_points": [
  "判据是 $\\omega_J|_M$：非零给量子化（$(A,B,A)$ 或一般 $(B,B,B)$），为零给 $D$-模。两者被 $\\ell$ 的方向连续区分，但物理对象在 $\\omega_J|_M\\to0$ 时退化。",
  "$D$-模侧仍有 $SL(2,\\mathbb R)$ 作用与最高/最低权分解：$\\epsilon\\to0$ 时 $B'$ 分裂成支撑在 $\\{0\\}$ 与 $\\mathbb{CP}^1\\setminus\\{\\infty\\}$ 的两个膜，分别给最低权与最高权 HC 模（(3.73)、(3.74)）。",
  "扭化 $\\lambda=\\eta+i\\gamma$ 与量子化侧的 $\\mu=\\beta+i\\gamma$ 共用 $\\gamma$：这是原文把两套构造放进同一族膜的原因。",
  "水平情形的 $D$-模在 $\\epsilon\\to0$ 时分裂（$x_+x_-=\\epsilon$），正对应表示论里 $J^2=n(n+1)$ 的可约点。"
 ],
 "formulas": [
  "$\\omega_J|_M=0,\\qquad M\\ \\text{在}\\ I\\ \\text{中全纯}$",
  "$D\\text{-模}=K^{1/2}\\otimes\\mathcal O(1)^{\\lambda},\\qquad \\lambda=\\eta+i\\gamma$",
  "$x_+x_-=\\epsilon=z^2-\\mu^2/4$"
 ],
 "theorems": [
  {
   "name": "水平膜的 $D$-模描述",
   "statement": "若 $\\ell$ 水平（$\\omega_J|_M=0$），则 $(B_{cc},B')$ 弦空间的整体截面构成 $M'=\\mathbb{CP}^1\\setminus\\{0,\\infty\\}$ 上扭化为 $K^{1/2}\\otimes\\mathcal O(1)^\\lambda$ 的 $D$-模；$\\epsilon\\to0$ 时它分裂为最低权与最高权两个 HC 模。",
   "proof": {
    "status": "sketch",
    "steps": [
     {"no": 1, "text": "$\\ell$ 水平使 $M$ 在 $I$ 中全纯而 $\\omega_J|_M=0$，故 $B'$ 是 $(B,A,A)$ 型，弦空间由 $\\bar\\partial_I$ 而非 $\\bar\\partial_J$ 的上同调给出。", "why": "这解释了为什么结果是 $D$-模：可积结构换成 $I$，截面空间不再带 Kähler 极化。"},
     {"no": 2, "text": "把 $Y$ 写成 $T^*\\mathbb{CP}^1$ 的仿射形变并用 $x_\\pm$ 坐标，$\\epsilon=z^2-\\mu^2/4$；半形式与 $B$ 场合成扭化 $\\lambda=\\eta+i\\gamma$。", "why": "给出 $D$-模的显式扭化，使它能与量子化侧共用 $\\gamma$。"},
     {"no": 3, "text": "$\\epsilon\\to0$ 时 $x_+x_-=0$ 分裂成 $x_+=0$ 与 $x_-=0$ 两支，分别给最低权、最高权 HC 模。", "why": "把 $D$-模的退化与表示的可约点对上。"}
    ],
    "gap_note": "原文对 $D$-模只作定性描述（「可以 sheaﬁﬁed」），没有写出完整的 $D$-模；本卡按原文口径记为 sketch。"
   },
   "source": "A p.59 §3.9"
  }
 ],
 "pitfalls": [
  "不要把 $D$-模当成量子化的另一种写法：它没有 Hilbert 结构，$\\omega_J|_M=0$ 时连辛形式都没有。",
  "不要混淆 $(A,B,A)$ 与 $(B,A,A)$：前者 $B'$ 在 $J$ 中全纯（$M$ 复子流形），后者 $B'$ 在 $I$ 中全纯（$M$ 全纯但 $\\omega_J$ 退化）。",
  "不要忽略 $\\lambda$ 的实部 $\\eta$：它是 $B$ 场通量，决定 $D$-模的扭化次数。"
 ],
 "related": ["ggl04/concept/k-invariant-lagrangian", "ggl04/concept/harish-chandra-curve", "ggl04/concept/brane-quantization"],
 "sources": [
  {"text": "A", "section": "3.9. Relation To D-Modules", "pages": [59, 59], "anchor": "A p.59 §3.9", "quote": "M is holomorphic in complex structure I and B′ is a brane of type"},
  {"text": "A", "section": "3.9", "pages": [60, 60], "anchor": "A p.60 §3.9", "quote": "the space of (Bcc, B′) strings can be sheaﬁﬁed over CP1"},
  {"text": "A", "section": "3.9", "pages": [62, 62], "anchor": "A p.62 eq (3.72)", "quote": "The logarithm of this monodromy corresponds to the parameter s = δ+ib"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "A 为主（§3.9 的定性描述 + (3.66)–(3.74) 的坐标）。最没把握的是 $D$-模的具体形式：原文只说可以 sheaﬁﬁed，未给完整构造。"
})

cards.append({
 "id": "ggl04/concept/cs-quantization",
 "type": "concept",
 "title": "Chern–Simons 理论的膜量子化与能级移位",
 "aliases": ["quantization of Chern-Simons", "CS level shift from branes"],
 "track": "A",
 "summary": "把平坦 $G$-联络模空间当作辛流形量子化，$B_{cc}$ 曲率给 $\\mathrm{Re}\\,\\Omega$，弦空间为 $H^0(M,L_*^{bk}\\otimes K^{1/2})$，故 $bk=k+h$。",
 "question": "怎样用膜量子化重算 Chern–Simons 理论的 Hilbert 空间与能级移位？",
 "definition": {
  "text": "取 $M=\\mathrm{Hom}(\\pi_1(C),G)/G$（$C$ 为亏格 $g$ 的曲面），它是 Chern–Simons 理论的经典相空间，带辛形式 $\\omega^*=\\frac1{4\\pi}\\int_C\\mathrm{Tr}\\,\\delta A\\wedge\\delta A$。取整 $bk$，令 $\\omega=bk\\,\\omega^*$（整形式），$L=(L^*)^{bk}$。复化为 $Y=\\mathrm{Hom}(\\pi_1(C),G_{\\mathbb C})/G_{\\mathbb C}$，带全纯辛形式 $\\Omega=bk\\,\\Omega^*$，其 $\\mathrm{Re}\\,\\Omega|_M=\\omega$。$Y$ 上有超 Kähler 度规（Hitchin 方程，需在 $C$ 上取复结构），$B_{cc}$ 曲率取 $\\mathrm{Re}\\,\\Omega$，故 $(M,\\omega)$ 的量子化是 $H=H^0(M,L_*^{bk}\\otimes K^{1/2})$。由 $K^{1/2}\\cong L_*^{-h}$（$h$ 为对偶 Coxeter 数）得 $H=H^0(M,L_*^{k})$，$k=bk-h$。",
  "notation": "$C$ 亏格 $g$ 曲面，$G$ 单连通紧群，$M$ 平坦联络模空间，$\\omega^*$ 标准辛形式，$bk$ 整数能级，$h$ 对偶 Coxeter 数，$k$ 为移位后的能级。"
 },
 "key_points": [
  "$\\omega^*$ 的整性：$\\mathrm{Tr}$ 归一使 $\\omega^*/2\\pi$ 是 $H^2(M,\\mathbb Z)\\cong\\mathbb Z$ 的生成元，故 $bk\\in\\mathbb Z$ 才使 $L$ 存在。",
  "移位来自半形式：$K^{1/2}\\cong L_*^{-h}$，故 $H^0(M,L_*^{bk}\\otimes K^{1/2})=H^0(M,L_*^{bk-h})$，即 $bk=k+h$；$k$ 是 WZW 的能级。",
  "$B_{cc}$ 的唯一性：$G$ 单连通且 $bk$ 整数时，曲率为 $\\mathrm{Re}\\,\\Omega$ 的线丛与 $B_{cc}$ 唯一；$B'$ 也唯一（$M$ 单连通 spin）。",
  "两个极化图像：Hitchin 纤维 $F$ 对 $\\mathrm{Im}\\,\\Omega$ 是 Lagrangian、$\\mathrm{Re}\\,\\Omega|_F$ 非退化，故 $H$ 同时是 $F$ 的量子化；$H_t$ 在 Teichmüller 空间上成平坦丛。",
  "带 twist 的推广：对合 $\\varphi$ 给 $h_\\varphi=h_+-h_-$、$k_\\varphi=bk-h_\\varphi$，且 $k+h=k_\\varphi+h_\\varphi$（(4.8)），与 [40] 的一圈修正一致。"
 ],
 "formulas": [
  "$\\omega^*=\\dfrac1{4\\pi}\\int_C\\mathrm{Tr}\\,\\delta A\\wedge\\delta A$",
  "$H=H^0(M,L_*^{bk}\\otimes K^{1/2}),\\qquad K^{1/2}\\cong L_*^{-h}$",
  "$bk=k+h,\\qquad k_\\varphi=bk-h_\\varphi,\\qquad k+h=k_\\varphi+h_\\varphi$"
 ],
 "theorems": [
  {
   "name": "CS 量子化的能级移位",
   "statement": "以 $\\omega=bk\\,\\omega^*$ 量子化平坦 $G$-联络模空间，得到的 Hilbert 空间同构于能级 $k=bk-h$ 的 Chern–Simons 理论 Hilbert 空间，$h$ 为 $G$ 的对偶 Coxeter 数。",
   "proof": {
    "status": "complete",
    "steps": [
     {"no": 1, "text": "$\\Omega=bk\\,\\Omega^*$ 限制到 $M$ 给 $bk\\,\\omega^*$，$G$ 单连通且 $bk$ 整使曲率 $\\mathrm{Re}\\,\\Omega$ 的线丛与 $B_{cc}$ 唯一存在。", "why": "保证这套量子化确实实现给定的 $(M,\\omega)$，而不是别的辛形式。"},
     {"no": 2, "text": "弦空间作为向量空间是 $H^0(M,L_*^{bk}\\otimes K^{1/2})$；半形式 $K^{1/2}\\cong L_*^{-h}$ 把它换成 $H^0(M,L_*^{bk-h})$。", "why": "这是移位的全部来源，与几何量子化里 $L^{\\otimes k}\\otimes K^{1/2}$ 的写法一致。"},
     {"no": 3, "text": "标准代数几何描述说 CS 能级 $k$ 的 Hilbert 空间是 $H^0(M,L_*^k)$，故 $k=bk-h$。", "why": "与原文 (4.4)、(4.5) 一致，并解释 $bk$ 与 $k$ 的差别。"}
    ],
    "gap_note": ""
   },
   "source": "A p.67 eq (4.5)"
  }
 ],
 "pitfalls": [
  "不要把 $bk$ 与 $k$ 混用：$bk$ 是 A-模型线丛的整数能级，$k=bk-h$ 才是 CS/WZW 能级；$h>0$ 的移位不能丢（$SU(2)$ 时 $h=2$）。",
  "不要以为 $M$ 单连通就没有别的障碍：$B'$ 还需要平坦 $\\mathrm{Spin}^c$ 结构，只在 $M$ 单连通 spin 时唯一。",
  "不要把 $\\Omega$ 与 $\\omega$ 混同：$\\Omega$ 是 $Y$ 上的全纯辛形式，只有 $\\mathrm{Re}\\,\\Omega|_M=\\omega$。"
 ],
 "related": ["ggl04/concept/half-form-shift", "ggl04/deriv/cs-level-shift", "ggl04/concept/canonical-coisotropic-brane"],
 "sources": [
  {"text": "A", "section": "4. Quantization Of Chern-Simons", "pages": [64, 64], "anchor": "A p.64 eq (4.1)", "quote": "M (which is the classical phase space of the Chern-Simons theory)"},
  {"text": "A", "section": "4", "pages": [65, 65], "anchor": "A p.65 §4", "quote": "The line bundle L → M extends to a unitary line bundle"},
  {"text": "A", "section": "4", "pages": [66, 66], "anchor": "A p.66 §4", "quote": "That is actually the standard result in Chern-Simons gauge theory"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "A 为主（§4 的构造与 (4.1)–(4.8)）。「$K^{1/2}\\cong L_*^{-h}$」原文在 p.66 以引用的方式给出，本卡照引；外部对照见 notes 的外部来源表。",
 "corrections": [{"id": "E1", "note": "原文 p.65 把 $B_{cc}$ 写成 the canonical isotropic brane；按其 §2.1 的定义与 $(\\omega^{-1}F)^2=-1$ 条件应为 coisotropic。见 errata E1。"}]
})

for c in cards:
    with open(os.path.join(CON, c["id"].split("/")[-1] + ".json"), "w", encoding="utf-8") as f:
        json.dump(c, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", c["id"])

derivs = []

derivs.append({
 "id": "ggl04/deriv/periods-to-su2-irrep",
 "type": "deriv",
 "title": "从三个周期到 $SU(2)$ 不可约表示",
 "aliases": ["periods to SU(2) irrep", "flux quantization to spin j"],
 "track": "D",
 "summary": "整性 $\\mu=n$ 加半形式移位给出 $n$ 维 $SU(2)$ 不可约表示：$j=(n-1)/2$、$J^2=(n^2-1)/4$，并与 (3.7) 的 Casimir 对上。",
 "question": "$S^2$ 上的通量量子数 $n$ 为什么对应自旋 $j=(n-1)/2$ 而不是 $n/2$？",
 "goal": "在 $Y:x^2+y^2+z^2=\\mu^2/4$ 的例子里，从 $S$ 上的周期整性出发，推出 $\\mu=n$、$\\dim H=n$、$j=(n-1)/2$、$J^2=(n^2-1)/4$，并说明半形式移位是 $n$ 而非 $n+1$ 的原因。",
 "setup": [
  {"text": "$Y$ 为仿射曲面 $x^2+y^2+z^2=\\mu^2/4\\subset\\mathbb C^3$，$\\Omega=h^{-1}dy\\wedge dz/x$，$S\\subset Y$ 为其中的 2-圈。", "why": "这是全文能完全算出的例子，所有参数都由 $S$ 上的周期给定，才能把抽象构造落到具体维数。"},
  {"text": "A-模型只依赖 $\\lambda=\\eta+i\\gamma$；$B_{cc}$ 存在要求 $F+B=\\omega_J$，积分得 $\\int_S c_1(L)+\\eta=\\beta$。", "why": "把几何周期换成线丛度数，才能用全纯截面数维数。"}
 ],
 "steps": [
  {"text": "由 (3.2) 与 $\\mathrm{Re}\\,\\Omega/2\\pi$ 的整性得 $n=\\mathrm{Re}(h^{-1}\\mu)\\in\\mathbb Z$；对 $\\tau$-对称的实切片取 $\\mu=\\beta=n=\\int_M c_1(L)$。", "why": "整性把连续参数 $\\mu$ 离散化，这是维数取整数的来源。", "locator": "A p.29 eq (3.2)", "provenance": "A"},
  {"text": "$\\tau$ 的固定点集为实 $x,y,z$ 且 $x^2+y^2+z^2=\\mu^2/4$，即 $M=S^2$；$B'$ 存在要求 $\\eta=0$，故 $\\mu=n$。", "why": "固定点集条件保证内积正定（§2.4），$\\eta=0$ 保证 $B'$ 的平坦结构存在。", "locator": "A p.34 eq (3.19)", "provenance": "A"},
  {"text": "$M$ 单连通故 $L'$ 平凡、$N=L=\\mathcal O(n)$；$K_{S^2}=\\mathcal O(-2)$ 给 $K^{1/2}=\\mathcal O(-1)$，故 $H=H^0(S^2,\\mathcal O(n-1))$，$\\dim H=n$。", "why": "半形式把 $n+1$ 降到 $n$，这一步是 $j=(n-1)/2$ 的关键。", "locator": "A p.35 §3.2", "provenance": "B"},
  {"text": "$n$ 维不可约 $SU(2)$ 表示有 $j=(n-1)/2$、$J^2=j(j+1)=(n^2-1)/4$，与 (3.7) 在 $\\mu=n$ 时一致；$J_z$ 谱为 $-(n-1)/2,1-(n-1)/2,\\dots,(n-1)/2$。", "why": "与 (3.7) 的吻合反过来定出 (3.5) 中常数 $c=-1/4$。", "locator": "A p.35 eq (3.21)", "provenance": "A"}
 ],
 "result": "$\\mu=n\\in\\mathbb Z$，$H=H^0(S^2,\\mathcal O(n-1))$ 为 $n$ 维，$j=(n-1)/2$，$J^2=(n^2-1)/4$，$J_z$ 谱从 $-(n-1)/2$ 到 $(n-1)/2$ 步长 1。",
 "gaps": [
  {"text": "第 3 步的 $K^{1/2}=\\mathcal O(-1)$ 在本篇只以「半形式」一笔带过，本卡按 $K_{S^2}=\\mathcal O(-2)$ 补出；若忽略它，维数为 $n+1$，与 (3.21) 的谱直接矛盾。"}
 ],
 "pitfalls": [
  "不要把 $n$ 直接当自旋：$n$ 是通量量子数，$j=(n-1)/2$ 才是自旋，差 1 来自半形式。",
  "不要以为 $\\mu$ 可以是任意实数：$\\tau$-对称要求 $\\mu^2$ 实，$B'$ 存在还要求 $\\eta=0$，合起来才给 $\\mu=n$。"
 ],
 "related": ["ggl04/concept/half-form-shift", "ggl04/deriv/casimir-from-curve", "ggl04/concept/brane-quantization"],
 "sources": [
  {"text": "A", "section": "3.2. SU(2)", "pages": [35, 35], "anchor": "A p.35 §3.2", "quote": "Quantization of M with n units of ﬂux gives a Hilbert space H of dimension n"},
  {"text": "A", "section": "3.1. An Example", "pages": [29, 29], "anchor": "A p.29 eq (3.2)", "quote": "Hence the cohomology class of Re Ω/2π is integral if n = Re (h−1µ) is an integer."},
  {"text": "A", "section": "3.1", "pages": [30, 30], "anchor": "A p.30 eq (3.6)", "quote": "The form of the algebra is then that x, y, and z obey the SO(3, C) commutation relations"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "步骤 1、2、4 出自 A（原文逐字给出 (3.2)、(3.19)、(3.21)）；步骤 3 的关键一步（$K^{1/2}=\\mathcal O(-1)$）是本卡按 $K_{S^2}=\\mathcal O(-2)$ 补的，归 B，并与 §2.3 的「W≅K^{1/2}」以及 notes 外部来源表交叉核对。"
})

derivs.append({
 "id": "ggl04/deriv/casimir-from-curve",
 "type": "deriv",
 "title": "由曲线参数推出 $J^2=(s+n)(s+n+1)$",
 "aliases": ["Casimir from curve moduli", "s and b from curve"],
 "track": "E",
 "summary": "曲线模 $\\delta$ 与 $b$ 合成 $s=\\delta+ib+\\mathrm{const}$；终止于定点给 $b=\\gamma/2$，再由 $\\mu=\\beta+i\\gamma$ 得 $J^2=(s+n)(s+n+1)$。",
 "question": "曲线膜的模空间坐标 $\\delta,b$ 怎样合成 $J^2=(s+n)(s+n+1)$？",
 "goal": "从 §3.7 的曲线模空间出发，证明只渐近不变膜的 $J_z$ 谱为 $s+n$ 且 $J^2=(\\mu^2-1)/4=(s+n)(s+n+1)$，并说明常数 $1/2$ 的来源。",
 "setup": [
  {"text": "膜由平面 $w_3=b$ 中的曲线 $\\ell$ 给出，$\\ell$ 渐近平行于 $w_2$ 轴，$M=\\pi^{-1}(\\ell)\\cong\\mathbb R\\times S^1$。", "why": "这是 $J_z$ 无界的几何来源，也是 HC 模（而非离散系列）的载体。"},
  {"text": "$M$ 上的两个实模：沿 $S^1$ 的 Wilson 线 $\\exp(2\\pi i\\delta)$ 与位移 $b$；A-模型在 $\\delta+ib$ 上全纯。", "why": "全纯性保证两个实参数合成一个复参数 $s$，这是 (3.54) 的前提。"}
 ],
 "steps": [
  {"text": "$w_2$ 是 $K$ 的 moment map 且沿 $M$ 无下界，故 $J_z$ 谱为 $\\{s+n\\}$，$s$ 定义模 1。", "why": "把 $M$ 的几何无界性翻译成谱的双边无界。", "locator": "A p.51 §3.7", "provenance": "A"},
  {"text": "$\\mathrm{Re}\\,s$ 由绕 $S^1$ 的单值给出：$\\mathrm{Re}\\,s=\\delta+\\mathrm{const}$；结合全纯性得 $s=\\delta+ib+\\mathrm{const}$。", "why": "这是 (3.54)，把两个实模写成复参数。", "locator": "A p.51 eq (3.54)", "provenance": "A"},
  {"text": "要得到最高/最低权，$\\ell$ 必须终止于定点 $\\pm\\frac12(\\alpha,\\beta,\\gamma)$，于是 $b=\\gamma/2$。", "why": "把 $b$ 与超 Kähler 周期的虚部绑定，才能消去一个实参数。", "locator": "A p.51 eq (3.55)", "provenance": "A"},
  {"text": "由 $\\mu=\\beta+i\\gamma=\\eta+i\\gamma+n$ 与 $\\mathrm{Im}\\,\\mu=2\\,\\mathrm{Im}\\,s$ 得 $\\mu/2=s+n+\\mathrm{const}$；常数取 $1/2$（$\\mu=0$ 时 $s=1/2$），故 $J^2=(\\mu^2-1)/4=(s+n+1/2)^2-1/4=(s+n)(s+n+1)$。", "why": "得到与 (3.7)、(3.36) 一致的 Casimir，完成几何到表示论的翻译。", "locator": "A p.51 eq (3.57)", "provenance": "A"}
 ],
 "result": "$s=\\delta+ib+\\mathrm{const}$、$b=\\gamma/2$、$\\mu/2=s+n+1/2$，故 $J^2=(s+n)(s+n+1)$；最高权与最低权膜的差别只是 $\\ell$ 终止于哪一侧定点，不改变 Casimir。",
 "gaps": [],
 "pitfalls": [
  "不要把 $b$ 与 $\\gamma$ 的关系反过来用：$b=\\gamma/2$ 只在 $\\ell$ 终止于定点时成立，只渐近不变时 $b$ 与 $\\gamma$ 无此绑定。",
  "不要漏掉常数 $1/2$：没有它 $J^2=(s+n)^2$ 型，与 $\\mu=0$、$s=1/2$ 的 $D^\\pm_0$ 不符。"
 ],
 "related": ["ggl04/concept/harish-chandra-curve", "ggl04/concept/k-invariant-lagrangian", "ggl04/deriv/periods-to-su2-irrep"],
 "sources": [
  {"text": "A", "section": "3.7", "pages": [51, 51], "anchor": "A p.51 eq (3.57)", "quote": "the imaginary part of µ is twice the imaginary part of s"},
  {"text": "A", "section": "3.8", "pages": [52, 52], "anchor": "A p.52 §3.8", "quote": "This is what we expect for a brane associated to a highest or lowest weight representation"},
  {"text": "A", "section": "3.7", "pages": [50, 50], "anchor": "A p.50 §3.7", "quote": "For the space of (Bcc, B′) strings to have an interpretation in terms of quantization"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "四步都出自 A（(3.54)–(3.57) 连续给出）。常数 $1/2$ 的定法按原文「$\\mu=\\beta=\\gamma=0$ 时 $s=1/2$」，依据 §3.3 的 $D^\\pm_0$。"
})

derivs.append({
 "id": "ggl04/deriv/cs-level-shift",
 "type": "deriv",
 "title": "Chern–Simons 能级移位 $bk=k+h$ 的推导",
 "aliases": ["CS level shift", "bk equals k plus h"],
 "track": "A",
 "summary": "平坦联络模空间的量子化给 $H^0(M,L_*^{bk}\\otimes K^{1/2})$；用 $K^{1/2}\\cong L_*^{-h}$ 把它化成 $H^0(M,L_*^{bk-h})$，故 $k=bk-h$。",
 "question": "为什么 A-模型里的整数 $bk$ 与 Chern–Simons 能级 $k$ 相差一个对偶 Coxeter 数？",
 "goal": "从 §4 的构造推出 $H=H^0(M,L_*^{bk}\\otimes K^{1/2})$、$K^{1/2}\\cong L_*^{-h}$，从而 $k=bk-h$，并验证带 twist 时 $k+h=k_\\varphi+h_\\varphi$。",
 "setup": [
  {"text": "$M=\\mathrm{Hom}(\\pi_1(C),G)/G$，$\\omega^*=\\frac1{4\\pi}\\int_C\\mathrm{Tr}\\,\\delta A\\wedge\\delta A$，取 $\\omega=bk\\,\\omega^*$ 且 $bk\\in\\mathbb Z$。", "why": "先把经典相空间与整性条件固定下来，$bk$ 才有意义。"},
  {"text": "$Y=\\mathrm{Hom}(\\pi_1(C),G_{\\mathbb C})/G_{\\mathbb C}$，$\\Omega=bk\\,\\Omega^*$，$\\mathrm{Re}\\,\\Omega|_M=\\omega$；$Y$ 上有 Hitchin 方程给的超 Kähler 度规。", "why": "这保证 $B_{cc}$ 的曲率正是 $\\mathrm{Re}\\,\\Omega$，从而 A-模型确实量子化 $(M,\\omega)$。"}
 ],
 "steps": [
  {"text": "$G$ 单连通、$bk$ 整使曲率 $\\mathrm{Re}\\,\\Omega$ 的线丛 $L$ 与 $B_{cc}$ 唯一存在；$B'$ 也唯一（$M$ 单连通 spin）。", "why": "两个膜都存在且唯一，弦空间才是确定的量子化对象。", "locator": "A p.65 §4", "provenance": "A"},
  {"text": "弦空间作为向量空间是 $H^0(M,L_*^{bk}\\otimes K^{1/2})$，来自 $W\\cong K^{1/2}$ 的半形式移位。", "why": "这是 (4.4)；移位不是约定而是费米子真空丛的族反常。", "locator": "A p.66 eq (4.4)", "provenance": "A"},
  {"text": "$K^{1/2}\\cong L_*^{-h}$（$h$ 为对偶 Coxeter 数），故 $H^0(M,L_*^{bk}\\otimes K^{1/2})=H^0(M,L_*^{bk-h})$。", "why": "把半形式吸收进能级，得到标准的 $H^0(M,L_*^k)$。", "locator": "A p.66 §4", "provenance": "A"},
  {"text": "标准代数几何描述说 CS 能级 $k$ 的 Hilbert 空间是 $H^0(M,L_*^k)$，故 $k=bk-h$，即 $bk=k+h$。", "why": "完成 $bk$ 与 $k$ 的换算。", "locator": "A p.67 eq (4.5)", "provenance": "A"},
  {"text": "带 twist $\\varphi$ 时 $h_\\varphi=h_+-h_-$，$k_\\varphi=bk-h_\\varphi$，于是 $k+h=k_\\varphi+h_\\varphi$（(4.8)），与 [40] 的一圈修正一致。", "why": "检验移位在 twist 下自洽，说明它不是某个极化的偶然产物。", "locator": "A p.69 eq (4.8)", "provenance": "A"}
 ],
 "result": "$H=H^0(M,L_*^{bk}\\otimes K^{1/2})\\cong H^0(M,L_*^{bk-h})$，故 $bk=k+h$；带 twist 时 $k_\\varphi=bk-h_\\varphi$ 且 $k+h=k_\\varphi+h_\\varphi$。",
 "gaps": [
  {"text": "第 3 步的 $K^{1/2}\\cong L_*^{-h}$ 原文以引用形式给出，本篇未证明；本卡只能照引，未独立验证 $h$ 的归一化。"}
 ],
 "pitfalls": [
  "不要把 $h$ 与 $h_\\varphi$ 混同：$h$ 是对偶 Coxeter 数（$SU(2)$ 时 2），$h_\\varphi=h_+-h_-$ 依赖对合 $\\varphi$。",
  "不要以为 $bk$ 与 $k$ 只差符号：$bk=k+h$，$h>0$ 故 $bk>k$。",
  "不要把 $\\mathrm{Re}\\,\\Omega|_M=\\omega$ 与 $\\Omega=bk\\,\\Omega^*$ 弄反：是先有 $bk\\,\\omega^*$ 再有 $\\Omega$ 的整倍。"
 ],
 "related": ["ggl04/concept/cs-quantization", "ggl04/concept/half-form-shift", "ggl04/concept/canonical-coisotropic-brane"],
 "sources": [
  {"text": "A", "section": "4", "pages": [64, 64], "anchor": "A p.64 eq (4.1)", "quote": "M (which is the classical phase space of the Chern-Simons theory)"},
  {"text": "A", "section": "4", "pages": [66, 66], "anchor": "A p.66 §4", "quote": "That is actually the standard result in Chern-Simons gauge theory"},
  {"text": "A", "section": "4", "pages": [67, 67], "anchor": "A p.67 eq (4.5)", "quote": "Many formulas in Chern-Simons gauge theory are most simply written not in terms of the"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "五步都出自 A（(4.4)–(4.8)）。第 3 步的 $K^{1/2}\\cong L_*^{-h}$ 是原文引自 [40] 的标准事实，本卡未独立证明，故 gaps 记一条。"
})

for d in derivs:
    with open(os.path.join(DER, d["id"].split("/")[-1] + ".json"), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", d["id"])
