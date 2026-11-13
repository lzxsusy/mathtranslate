# -*- coding: utf-8 -*-
"""底本/草稿尽调与原文分节提取（用 chr(92) 拼反斜杠，避免转义地狱）。"""
import sys, os, glob
sys.stdout.reconfigure(encoding="utf-8")
B = chr(92)                      # 反斜杠
BS2 = B + B                      # 正则里匹配“一个字面反斜杠”
ROOT = r"<本地路径>"
SEC = os.path.join(ROOT, "sections")
SRC = r"<本地路径>"
REF = os.path.join(ROOT, "work", "ref")
os.makedirs(REF, exist_ok=True)

out = []
def P(s=""):
    out.append(str(s)); print(s)

files = sorted(glob.glob(os.path.join(SEC, "*.tex")))
alltex = "".join(open(f, encoding="utf-8").read() for f in files)
t = open(SRC, encoding="utf-8", errors="replace").read()

def find_all(pat, text):
    import re
    return re.findall(pat, text)

P("=== 草稿 vs 原文 结构对比 ===")
def stat(name, pat_draft, pat_en=None):
    a = len(find_all(pat_draft, alltex))
    b = len(find_all(pat_en if pat_en else pat_draft, t))
    P(f"{name:22s} draft={a:5d}   original={b:5d}")

stat("section",        BS2+"section"+BS2+"*?"+B+"{")
stat("subsection",     BS2+"subsection"+BS2+"*?"+B+"{")
stat("equation",       BS2+"begin"+B+"{equation"+B+"}")
stat("align",          BS2+"begin"+B+"{align"+B+"}")
stat("gather",         BS2+"begin"+B+"{gather"+B+"}")
stat("multline",       BS2+"begin"+B+"{multline"+B+"}")
stat("figure",         BS2+"begin"+B+"{figure"+B+"}")
stat("table",          BS2+"begin"+B+"{table"+B+"}")
stat("tabular",        BS2+"begin"+B+"{tabular"+B+"}")
stat("footnote",       BS2+"footnote"+B+"{")
stat("label",          BS2+"label"+B+"{")
stat("cite",           BS2+"cite")
stat("index",          BS2+"index"+B+"{")
stat("ref",            BS2+"ref"+B+"{")
stat("eqref",          BS2+"eqref"+B+"{")
stat("cref",           BS2+"cref")
stat("itemize",        BS2+"begin"+B+"{itemize"+B+"}")
stat("enumerate",      BS2+"begin"+B+"{enumerate"+B+"}")
P("draft chars=%d, original chars=%d" % (len(alltex), len(t)))

P("\n=== 原文编号方案探测 ===")
for kw in ["numberwithin", "numberwithin{equation}", "theequation", "thesection"]:
    P(f"{kw:24s} appears {t.count(kw)} times")
i = t.find("numberwithin")
if i >= 0:
    P(repr(t[i-80:i+120]))
P("原文 eqref 使用次数: %d" % t.count(B+"eqref"))
P("原文 ref 使用次数: %d" % t.count(B+"ref{"))

# ---------- 排版普查 ----------
P("\n=== 排版普查（草稿） ===")
CJK = "\u4e00-\u9fff"
import re
def c(pat, txt=alltex):
    return len(re.findall(pat, txt))
P("CJK 后句点 '. '   : %d" % c("["+CJK+r"]\.\s"))
P("CJK 后句号 '。'    : %d" % c("["+CJK+r"]。"))
P("CJK 后半角逗号 ', ': %d" % c("["+CJK+r"],\s"))
P("CJK 后半角分号 '; ': %d" % c("["+CJK+r"];\s"))
P("CJK 后半角冒号 ': ': %d" % c("["+CJK+r"]:\s"))
P("半角括号内含中文   : %d" % c(r"\([^)\n]*["+CJK+r"][^)\n]*\)"))
P("全角括号 '（'      : %d" % c("（"))
P("英文双引号 '\"'    : %d" % c('"'))
P("中文引号 '“'       : %d" % c("“"))
P("'...' 省略号       : %d" % c(r"\.\.\."))
P("Markdown '**'      : %d" % c(r"\*\*"))
P("U+FFFD             : %d" % c("\ufffd"))
P("BOM 文件数: %d" % sum(1 for f in files if open(f,'rb').read(3)==b'\xef\xbb\xbf'))
P("TAB 文件数: %d" % sum(1 for f in files if '\t' in open(f,encoding='utf-8').read()))
P("CRLF 文件数: %d" % sum(1 for f in files if '\r\n' in open(f,encoding='utf-8',newline='').read()))

# 句点前不是 CJK 的样本（区分缩写/公式后句点）
others = re.findall(r".{0,20}\.\s", alltex)
noncjk = [s for s in others if s and not re.search("["+CJK+r"]\.\s$", s)]
P("\n'. ' 前不是中文的样本数: %d" % len(noncjk))
for s in noncjk[:15]:
    P("   " + repr(s))

# ---------- 原文按 section 切分 ----------
P("\n=== 原文分节提取 ===")
# 找所有 section 位置
sec_re = re.compile(BS2+"section" + BS2 + r"\*?\{" )
positions = [(m.start(), m.end()) for m in sec_re.finditer(t)]
P("原始 section 数: %d" % len(positions))
secs = []
for k, (s, e) in enumerate(positions):
    # 取标题
    depth = 1
    j = e
    while j < len(t) and depth:
        if t[j] == B:
            j += 2; continue
        if t[j] == "{": depth += 1
        elif t[j] == "}": depth -= 1
        j += 1
    title = t[e:j-1]
    end = positions[k+1][0] if k+1 < len(positions) else len(t)
    secs.append((title, t[s:end]))
for k, (title, body) in enumerate(secs):
    print(f"  [{k+1:02d}] {title[:70]!r}  len={len(body)}")

# 映射到草稿文件
mapping = [
    ("00-introduction", [0, 1]),      # Introduction + Prerequisites/acks
    ("01-electromagnetic", [2]),
    ("02-multiplets", [3]),
    ("03-renormalization", [4]),
    ("04-pure-su2", [5]),
    ("05-one-flavor", [6]),
    ("06-six-dimensions", [7]),
    ("07-higgs", [8]),
    ("08-two-three-flavors", [9]),
    ("09-gaiotto", [10]),
    ("10-argyres-douglas", [11]),
    ("11-other-groups", [12]),
    ("12-su-n-duality", [13]),
    ("13-conclusions", [14]),
    ("A-instantons", [15]),
    ("B-theory-zoo", [16]),
]
P("\n写出 work/ref/*-en.tex:")
for name, idxs in mapping:
    body = "\n\n% ===== 原文相邻 section 分界 =====\n\n".join(secs[i][1] for i in idxs)
    head = "% 原文（arXiv:1312.2684v2, dummies.tex）对应小节：\n" + \
           "\n".join("%   - " + secs[i][0] for i in idxs) + "\n\n"
    with open(os.path.join(REF, name + "-en.tex"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(head + body)
    print(f"  {name}-en.tex  {len(body)} chars")

with open(os.path.join(ROOT, "work", "probe", "probe.md"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write("# 项目尽调（自动生成，2026-11-05）\n\n```\n" + "\n".join(out) + "\n```\n")
print("\nwritten work/probe/probe.md")
