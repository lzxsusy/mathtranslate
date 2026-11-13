import io, sys, glob, os, re
sys.stdout.reconfigure(encoding="utf-8")
CH = r"<本地路径>"
files = [f for f in sorted(glob.glob(os.path.join(CH, "*.tex"))) if not os.path.basename(f).startswith("_")]

GLOBAL = [
    ("规范部分", "规范扇区"),
    ("物质部分", "物质扇区"),
    ("sector", "扇区"),
    ("部门", "扇区"),
    ("holonomy", "和乐"),
    ("ghost 次数", "鬼数"),
    ("ghost 数", "鬼数"),
    ("off-shell", "离壳"),
    ("Vafa--Witten", "Vafa-Witten"),
    ("超凯勒", "超 Kähler"),
]

TARGETED = {
    "c01-01.tex": [
        ("这一猜测最终在", "这一猜想最终在"),
        ("1977 年的猜测通常被引作", "1977 年的猜想通常被引作"),
    ],
    "appA-02.tex": [("一个自然猜测是", "一个自然猜想是")],
    "ch06b-03.tex": [("一个自然的猜测是", "一个自然的猜想是")],
    "ch06b-04.tex": [
        ("及其幂的 descendant 对它", "及其幂的后代（descendant）对它"),
        ("及其幂的 descendant 变形得到", "及其幂的后代形变得到"),
    ],
    "ch02-01.tex": [(" dx^\\mu", " \\dd x^\\mu")],
    "c01-03.tex": [("带有 Hamilton $U(1)$ 作用", "带有哈密顿（Hamiltonian）$U(1)$ 作用")],
    "ch07-03.tex": [("是 Hamilton 作用", "是哈密顿作用")],
}

# appA-01 的 p.124 批注改写（tr-05 复核：真正笔误是 ξ→η，σ 的鬼数 2 无误）
APP_NOTE_OLD = ("% [Tutor Note: p.124 原文笔误（照原文译出）。原文作 “The field $\\sigma$ has ghost number 2, "
                "the fields $\\rho$ has ghost number 1, and the fields $\\eta$ and $\\theta$ have ghost number $-1$.” "
                "这段描述的是 B-模型的场，而 B-模型中鬼数为 2 的玻色场是 $\\phi$（$\\sigma$ 是 §A.1 A-型一侧的场，"
                "见下句“鬼数为 2 的玻色子 $\\sigma$ 与 $\\phi$ 必须在缺陷线上等同起来”）；故首句的 $\\sigma$ 应为 $\\phi$。"
                "此外 “the fields $\\rho$ has” 单复数不一致，应为 “the field $\\rho$ has”。]")
APP_NOTE_NEW = ("% [Tutor Note: p.124 原文笔误与记号说明（正文照原文译出）。"
                "（1）场清单中 “fermionic 0-forms $\\theta$ and $\\xi$” 的 $\\xi$ 应为 $\\eta$：同页 BRST 变换表只列出 "
                "$\\phi,<本地路径>,\\eta,\\theta,\\rho$，$\\eta$ 已出现却缺其场清单条目，而 $\\xi$ 全篇仅此一见；"
                "下文配对关系也写 “fermionic 0-forms $\\beta$ and $\\eta$”。故正文照原文保留 $\\xi$，读者应读作 $\\eta$。"
                "（2）“The field $\\sigma$ has ghost number 2” 一句**不是**笔误：同页下段明确说 “鬼数为 2 的玻色子 "
                "$\\sigma$ 与 $\\phi$ 必须在缺陷线上等同起来”，且鬼数配对 $\\sigma(2)<本地路径>)$、"
                "$\\beta(-1)<本地路径>)$、$\\lambda(1)<本地路径>)$、"
                "$<本地路径>)<本地路径>)$ 自洽。（3）“the fields $\\rho$ has” 主谓不一致，"
                "应为 “the field $\\rho$ has”。]")

changed = {}
for f in files:
    s = io.open(f, encoding="utf-8").read()
    orig = s
    for old, new in GLOBAL:
        s = s.replace(old, new)
    base = os.path.basename(f)
    for old, new in TARGETED.get(base, []):
        s = s.replace(old, new)
    if base == "appA-01.tex":
        if APP_NOTE_OLD in s:
            s = s.replace(APP_NOTE_OLD, APP_NOTE_NEW)
            print("appA-01: note revised")
        else:
            print("appA-01: NOTE PATTERN NOT FOUND")
    if s != orig:
        io.open(f, "w", encoding="utf-8", newline="\n").write(s)
        changed[base] = sum(1 for a, b in zip(orig.split(), s.split()) if a != b) if False else "edited"

print("\nfiles changed:", len(changed))
for k in sorted(changed):
    print("  ", k)

# 统计替换后残留
alltxt = "".join(io.open(f, encoding="utf-8").read() for f in files)
for w in ("sector", "部门", "holonomy", "ghost 数", "off-shell", "Vafa--Witten", "超凯勒", "规范部分", "物质部分"):
    print(f"residual {w!r}: {alltxt.count(w)}")
