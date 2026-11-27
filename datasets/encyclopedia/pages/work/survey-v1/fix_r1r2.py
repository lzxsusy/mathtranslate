# -*- coding: utf-8 -*-
"""按 R1/R2 审校报告修页面：P0/P1/P2 + compiled_from 重建 + 附录 B 换卡。"""
import hashlib, json, re, sys
from pathlib import Path

PAGE = Path(__file__).resolve().parents[2] / "geometric-langlands.md"
ROOT = Path(__file__).resolve().parents[5]   # gitee_shuyi
text = PAGE.read_text(encoding="utf-8")
orig = text

REPL = [
    # R1 P0
    ("几何 Satake 把它等同于 Rep(Ĝ) 的一个版本，Ĝ 的表示环因此就是 Hecke 算子的共同谱 {{card:bzg/concept/dual-group}}〔BZ26 p.14 §3.1〕",
     "几何 Satake 说的是张量范畴等价 Sph_G ≃ Rep(Ĝ)；Hecke 算子的联合特征值则由 Ĝ-局部系统（Loc_Ĝ）参数化 {{card:bzg/concept/geometric-satake}}〔BZ26 p.16 §3.3〕〔BZ26 p.17 §3.5〕"),
    # R1 P1 错页
    ("谈六函子，而不只是谈迹函数〔BZ26 p.2〕", "谈六函子，而不只是谈迹函数〔BZ26 p.8 §2.1〕"),
    ("整体形式把这个逐点构造升级为函子〔BZ26 p.13 §2.5〕〔CL23 书页 p.3（PDF 8）〕",
     "整体形式把这个逐点构造升级为函子〔BZ26 p.13 §2.5〕〔CL23 书页 5（PDF 10）〕"),
    ("可约局部系统对应的是特征对象而非层 {{card:bzg/concept/glc-overview}}〔CL23 书页 p.3（PDF 8）〕",
     "可约局部系统对应的是特征对象而非层 {{card:bzg/concept/glc-overview}}〔CL23 书页 5（PDF 10）〕"),
    ("并有一列有限型的开子叠把它穷竭〔CL23 书页 12（PDF 17）定理 2.2.1〕",
     "并有一列有限型的开子叠把它穷竭〔CL23 书页 10（PDF 15）定理 2.2.1〕"),
    ("{{card:bzg/concept/adelic-uniformization}}〔CL23 书页 12（PDF 17）〕",
     "{{card:bzg/concept/adelic-uniformization}}〔CL23 书页 10（PDF 15）〕"),
    ("而层范畴要按叠来取〔CL23 书页 12（PDF 17）〕", "而层范畴要按叠来取〔CL23 书页 4（PDF 9）〕"),
    ("连通分支按度数 d 编号〔CL23 书页 13（PDF 18）注 2.2.3〕",
     "连通分支按度数 d 编号〔CL23 书页 10（PDF 15）注 2.2.3〕〔BZ26 p.10 §2.2〕"),
    ("F ↦ (supp, h→)_!(m*Sat_V ⊗ h←^*F) {{card:glc/concept/hecke-eigensheaf-general}}〔CL23 书页 14（PDF 19）〕",
     "F ↦ (supp, h→)_!(m*Sat_V ⊗ h←^*F) {{card:glc/concept/hecke-eigensheaf-general}}〔CL23 书页 12（PDF 17）§2.6〕"),
    ("{{card:bzg/concept/geometric-satake}}〔CL23 书页 14（PDF 19）§2.5〕",
     "{{card:bzg/concept/geometric-satake}}〔CL23 书页 12（PDF 17）§2.5〕"),
    ("{{card:bzg/concept/spherical-hecke-category}}〔CL23 书页 14（PDF 19）〕",
     "{{card:bzg/concept/spherical-hecke-category}}〔CL23 书页 15（PDF 20）§2.11〕"),
    ("两者接缝处的重数必须是一〔BZ26 p.26 §5.5〕",
     "V 把「所有特征空间重数一」与无分歧 GLC 一起收口（这两句是编者综合，BZ26 只说该论文导致 multiplicity one 成立）〔BZ26 p.26 §5.5〕"),
    ("〔RAS23 书页 2 §1.2〕", "〔RAS23 书页 3（PDF 4）§1.2〕"),
    ("{{card:glc/concept/geometric-class-field-theory}}〔CL23 书页 5（PDF 10）定理 1.1.1〕",
     "{{card:glc/concept/geometric-class-field-theory}}〔CL23 书页 1（PDF 6）定理 1.1.1〕"),
    ("{{card:bzg/concept/glc-statement}}〔SCH26 p.8〕", "{{card:bzg/concept/glc-statement}}〔SCH26 p.7 定理 1.7〕"),
    ("互换〔BZ26 p.6 §1.4〕", "互换〔BZ26 p.7 §1.4.1〕"),
    # R1 P1 错述 / 条件
    ("Bun_G(S) 是 X×S 上 G-挠子的群胚，等价地是 X×S → S 的截面叠",
     "Bun_G(S) 是 X×S 上 G-挠子的群胚，即 X×S 上 G-丛的模叠"),
    ("函数域情形经典侧已定理化，几何侧 char 0 的主定理是另一条线",
     "函数域情形的经典 Langlands（GL_n）已由 Drinfeld 与 Lafforgue 定理化〔LAU02 906--1〕；几何侧 char 0 的主定理是另一条线"),
    # R1 P2
    ("{{card:bzg/concept/categorical-harmonic-analysis}}〔BZ26 p.4〕",
     "{{card:bzg/concept/categorical-harmonic-analysis}}〔BZ26 p.4–5 §1.3〕〔BZ26 p.9 §2.1〕"),
    ("都在配对的模空间之间交换卷积与张量", "都在对偶向量空间、对偶阿贝尔簇之间交换卷积与张量"),
    ("只有 GL_n、SO_{2n} 这类自对偶群成立", "GL_n、SO_{2n} 自对偶；环面、E₈、F₄、G₂ 也自对偶"),
    ("GL₁ 是唯一能从头走到尾的情形", "GL₁（以及环面）是最简单、能从头走到尾的情形"),
    ("降范畴化后还能回收经典 Hecke 代数的交换性〔BZ26 p.16 §3.3〕",
     "降范畴化后还能回收经典 Hecke 代数的交换性〔BZ26 p.16 §3.2 末〕"),
    ("一般 $G$ 以 cameral cover 替代谱曲线", "一般 $G$ 的对应见 [DM96, DG02]"),
    ("后经 [Ari13, MRV19] 推广", "后经 [Ari13, MRV19a, MRV19b] 推广"),
    ("「低亏格更容易」不是定理〔LAU02 906--9〕", "「低亏格更容易」是编者判断，不是定理〔LAU02 906--9〕"),
    ("§2 因此把 $\\operatorname{QCoh}$ 写进等价，补上「对角化」的内容",
     "§2 因此把 $\\operatorname{QCoh}$ 的谱作用写进定理的另一半，补上「对角化」的内容"),
    ("（底本脚注写明）〔SCH26 p.14 §2 脚注 15〕", "（SCH26 脚注写明）〔SCH26 p.14 §2 脚注 15〕"),
    # R2 P1
    ("这是目前最一般的构造，也是「Galois → 自守」方向的关键〔SCH26 p.38 §11〕",
     "这是经典构造，也是「Galois → 自守」方向的关键；但它只覆盖 opers 这个半维子簇，一般参数的构造见 [FG09a]〔SCH26 p.38 §11〕〔BZ26 p.26 §5.5〕"),
    ("量子 GLC 仍开；Dolbeault 已有一般情形的工作〔BZ26 p.27 §6.0.4〕",
     "量子 GLC 仍开；Dolbeault 在通有（generically）情形已由 [DP12] 证明，全 Hitchin 基上仍开，[PT25] 有新进展〔BZ26 p.27 §6.0.4〕"),
    ("这一步是否已被框架覆盖，见待核。", "这一步是否已被 SCH26 的框架覆盖，现有材料无法判定。"),
    # R2 P2 记号 / 错页 / 措辞
    ("$G_m^{2g}\\times(\\ast\\times^L\\ast)\\times\\ast/G_m$", "$G_m^{2g}\\times(\\ast\\times^L_{G_m}\\ast)\\times\\ast/G_m$"),
    ("$D_{qc}(\\ast/\\hat G)$-线性", "$D_{qc}(\\ast/\\hat G)_{Ran}$-线性"),
    ("到 Ȗ^Θ 的约化", "到 ˇU^Θ 的约化"),
    ("AGKRV 2021", "AGKRRV 2021"),
    ("后面十一节都为第四步供料〔SCH26 p.7 §1〕", "后面十一节都为第四步供料〔SCH26 p.7 定理 1.7；p.8 §1〕"),
    ("〔SCH26 p.35–36 §10〕{{card:bzg/concept/eisenstein-series}}", "〔SCH26 p.36〕〔SCH26 p.37〕{{card:bzg/concept/eisenstein-series}}"),
    ("定理 9.6 给 Whittaker 系数的完全描述", "定理 9.6 把 Whittaker 侧识别为 D_qc(∗/Ĝ)"),
    ("〔SCH26 p.33 §9〕{{card:bzg/concept/whittaker-period}}", "〔SCH26 p.33 定理 9.3；p.35 定理 9.6〕{{card:bzg/concept/whittaker-period}}"),
    ("**§2 等价陈述（p.9–14）：**", "**§2 等价陈述（p.9–15）：**"),
    ("**§3 Bun_G 上的层（p.15–16）：**", "**§3 Bun_G 上的层（p.15–17）：**"),
    ("**§4 局部系统的叠（p.17–18）：**", "**§4 局部系统的叠（p.17–19）：**"),
    ("〔LAU02 906--13〕〔LAU02 906--15〕", "〔LAU02 906--14〕〔LAU02 906--15〕"),
    ("五篇不是按投稿时间排的直线，而是按论证依赖咬合的五台机器：I 造函子，II 造尖点层，III 用 Eisenstein 化到尖点，IV 用 ambidexterity 把单射与满射合成等价，V 算重数一收口〔BZ26 p.26 §6〕。编年照 §6：",
     "五篇不是按投稿时间排的直线，而是按论证依赖咬合的五台机器：I 造函子，II 造尖点层，III 用 Eisenstein 化到尖点，IV 用 ambidexterity 把单射与满射合成等价，V 算重数一收口〔BZ26 p.26 §5.5〕。编年见 SCH26 p.14 与书目 p.42–43："),
    ("Kac–Moody 局部化、ambidexterity、Eisenstein", "Kac–Moody 局部化、Eisenstein、ambidexterity"),
    # 附录 B：换卡
    ("| `bzg/concept/relative-langlands` | 相对 Langlands 与 period | [relative-langlands.json](../../benzvi_glc/cards/concepts/relative-langlands.json) | §5/§7 | p.22 |",
     "| `sy0246/concept/vanishing-theorem` | Gaitsgory 消没定理（旧路线） | [vanishing-theorem.json](../../sy0246/cards/concepts/vanishing-theorem.json) | 附录 A | 906--14 |"),
]

miss = []
for old, new in REPL:
    n = text.count(old)
    if n != 1:
        miss.append((n, old[:60]))
        continue
    text = text.replace(old, new)

# 系统性替换（多处的）
text = text.replace("〔BZ26 p.26 §6〕", "〔BZ26 p.26 §5.5〕")
text = text.replace("| p.26 §6 |", "| p.26 §5.5 |")
text = text.replace("〔SCH26 p.14 §2.11〕", "〔SCH26 p.14 §2 定理 2.11〕")
text = text.replace("〔SCH26 p.14 §2.12〕", "〔SCH26 p.14 §2 定理 2.12〕")
text = text.replace("〔SCH26 p.14–15 §2.12〕", "〔SCH26 p.14–15 §2 定理 2.12〕")

# compiled_from 重建：正文全部 {{card:...}} 唯一 id
body_start = text.index("\n---\n", text.index("compiled_from:")) + 5
body = text[body_start:]
ids = []
for m in re.finditer(r"\{\{card:([a-z0-9_]+/[a-z]+/[a-z0-9\-]+)\}\}", body):
    if m.group(1) not in ids:
        ids.append(m.group(1))
ids.sort()

card_dir = ROOT / "datasets"
hash_by_id = {}
for p in card_dir.glob("*/cards/**/*.json"):
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        continue
    cid = d.get("id")
    if cid:
        hash_by_id[cid] = hashlib.sha256(p.read_bytes()).hexdigest()[:16]

lines = ["compiled_from:"]
for cid in ids:
    h = hash_by_id.get(cid)
    if h is None:
        print("MISSING CARD FILE:", cid); sys.exit(2)
    lines.append(f"  - id: {cid}\n    hash: {h}")
block = "\n".join(lines) + "\n"

start = text.index("compiled_from:")
end = text.index("\n---\n", start) + 1
text = text[:start] + block + text[end:]

# 附录 C 箭头：I→II、I→III、II→III、II→IV；char p 虚线
oldc = '''  S2 --> I["I · 造 Langlands 函子 L_G<br/>D(Bun_G) → IndCoh_Nilp(Loc_Ĝ)"]
  KM["II · Kac–Moody + opers<br/>临界水平局部化 ⇒ 尖点层"] --> I
  I --> III["III · Eisenstein 归纳<br/>化到 Levi 与尖点"]
  III --> IV["IV · ambidexterity<br/>左/右伴随差扭同构"]
  IV --> V["V · 重数一<br/>A_Ĝ 自对偶 ⇒ 局部系统"]
  V --> TH["char 0 主定理<br/>D(Bun_G) ≃ IndCoh_Nilp(Loc_Ĝ)"]
  CP["char p（独立 2025a）<br/>Witt 提升 + LocSys′"] --> TH
'''
newc = '''  S2 --> I["I · 造 Langlands 函子 L_G<br/>D(Bun_G) → IndCoh_Nilp(Loc_Ĝ)"]
  I --> KM["II · Kac–Moody + opers<br/>临界水平局部化 ⇒ 尖点层"]
  I --> III["III · Eisenstein 归纳<br/>化到 Levi 与尖点"]
  KM --> III
  III --> IV["IV · ambidexterity<br/>左/右伴随差扭同构"]
  KM --> IV
  IV --> V["V · 重数一<br/>A_Ĝ 自对偶 ⇒ 局部系统"]
  V --> TH["char 0 主定理<br/>D(Bun_G) ≃ IndCoh_Nilp(Loc_Ĝ)"]
  TH -.-> CP["char p（独立 2025a）<br/>Witt 提升 + LocSys′"]
'''
if text.count(oldc) != 1:
    print("APPENDIX C BLOCK NOT FOUND"); sys.exit(3)
text = text.replace(oldc, newc)

# 署名/版本
text = text.replace("reviewed_on: 2026-11-27", "reviewed_on: 2026-11-28")
text = text.replace("version: 1.0", "version: 1.0.1")

PAGE.write_text(text, encoding="utf-8")
print("replacements applied:", len(REPL) - len(miss))
if miss:
    print("FAILED:", miss)
print("cards compiled_from:", len(ids))
print("bytes:", len(text.encode('utf-8')), "lines:", text.count('\n') + 1)
