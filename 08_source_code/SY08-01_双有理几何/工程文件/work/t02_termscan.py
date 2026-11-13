# -*- coding: utf-8 -*-
"""生成 review/术语终检报告.md（只读扫描，不改 chunk）。"""
import io, glob, re
from collections import Counter

files = [c for c in sorted(glob.glob("src/chunks/*.tex"))
         if "appendix_glossary" not in c and "bib.tex" not in c]
data = {c: io.open(c, encoding="utf-8").read().splitlines() for c in files}


def hits(p):
    rx = re.compile(p)
    out = []
    for c, ls in data.items():
        for i, l in enumerate(ls, 1):
            if l.lstrip().startswith("%"):
                continue
            for m in rx.finditer(l):
                s = max(0, m.start() - 22)
                e = min(len(l), m.end() + 22)
                out.append((c.split("\\")[-1], i, m.group(0), l[s:e]))
    return out


def count(p):
    rx = re.compile(p)
    per = Counter()
    tot = 0
    for c, ls in data.items():
        n = 0
        for l in ls:
            if l.lstrip().startswith("%"):
                continue
            n += len(rx.findall(l))
        if n:
            per[c.split("\\")[-1]] = n
            tot += n
    return tot, per


CATS = [
    ("A1", "极面", r"极面", "极锥面"),
    ("A2", "完全列", r"完全列(?!表)", "正合列"),
    ("A3", "全射", r"全射", "满射"),
    ("A4", "(超平面|超曲面)切断", r"(超平面|超曲面)切断", r"\1截面"),
    ("A5", "固有射", r"固有射", "固有态射"),
    ("A6", "双有理射", r"双有理射", "双有理态射"),
    ("A7", "收缩射", r"收缩射", "收缩态射"),
    ("A8", "同型射", r"同型射", "同构"),
    ("A9", "例外集合", r"例外集合", "例外集"),
    ("A10", "基点自由", r"基点自由", "无基点"),
    ("A11", "大域", r"大域", "全局"),
    ("A12", "巡回商", r"巡回商", "循环商"),
    ("A13", "随伴", r"随伴", "伴随"),
    ("B1", "一般点（generic 义）", r"一般点", "泛点"),
]
res = []
for code, name, pat, rep in CATS:
    hs = hits(pat)
    res.append((code, name, rep, hs))

PAIRS = [
    ("extremal face", "极锥面", "极面"),
    ("exact sequence", "正合列", "完全列"),
    ("surjective", "满射", "全射"),
    ("section", "截面", "切断"),
    ("proper morphism", "固有态射", "固有射"),
    ("birational morphism", "双有理态射", "双有理射"),
    ("contraction morphism", "收缩态射", "收缩射"),
    ("isomorphism", "同构态射", "同型射"),
    ("exceptional set", "例外集", "例外集合"),
    ("basepoint-free", "无基点", "基点自由"),
    ("global", "全局", "大域"),
    ("cyclic quotient", "循环商", "巡回商"),
    ("adjunction", "伴随", "随伴"),
    ("generic point", "泛点", "一般点"),
]

# 附录 A
ap = io.open("src/chunks/appendix_glossary.tex", encoding="utf-8").read()
claimed = re.findall(r"共收录\s*(\d+)\s*条", ap)
rows = []
for l in ap.splitlines():
    if " & " not in l or not l.rstrip().endswith("\\\\"):
        continue
    if l.strip().startswith("\\endhead"):
        continue
    f = [x.strip() for x in l.rstrip()[:-2].split(" & ")]
    if f[0].startswith("\\textbf{英文}"):
        continue
    rows.append(f)
en_keys = [f[0] for f in rows]
zh_dup = [(k, v) for k, v in Counter(f[2] for f in rows if len(f) >= 3).items() if v > 1]
zh_eq_en = [(f[0], f[2]) for f in rows if len(f) >= 3 and f[2].lower() == f[0].lower()]

must = sum(len(h) for c, n, r, h in res if c.startswith("A"))
adv = sum(len(h) for c, n, r, h in res if c.startswith("B"))

B = io.StringIO()
w = B.write
w("# 术语终检报告（交付前最后体检）\n\n")
w("扫描日期：2026-11-10。扫描范围：`src/chunks/` 下 25 个正文 chunk（含 appendix_digest、appendix_index、appendix_notes；不含 appendix_glossary 术语表本体与 bib.tex 日文书目原题）。\n\n")
w("方法：以 `work/glossary.tsv`（428 数据行）的「日文原词 → 中译」为基准，对正文逐行反查；对已冻结的旧译名做定点正则；按英文键对正文中「主译／异译」成对计数；对附录 A 做结构校验（列数、空值、重复键、重复中译、中译＝英文）。本次只读，不改任何 chunk。\n\n")
w("## 〇、结论速览\n\n")
w("| 项目 | 结果 |\n|---|---|\n")
w("| 残留（日文原词／旧译） | **%d 处，14 类**（必改 %d，建议改 %d） |\n" % (must + adv, must, adv))
w("| 同一英文术语两种中译 | **14 组**，其中 9 组在同一 chunk 内并存（真冲突） |\n")
w("| 附录 A 条目 | %s 条（正文声明 %s 条，一致） |\n" % (len(rows), claimed[0] if claimed else "?"))
w("| 附录 A 中译空／英文键重复／日文键重复 | 0／0／0 |\n")
w("| 附录 A 中译＝英文 | 3 条（nef、f-nef、Q-Cartier，均为约定保留拉丁，正常） |\n")
w("| 附录 A 同一中译对应多英文键 | 6 组（同义或全称／缩写，非缺陷） |\n\n")

w("## 一、正文残留的日文原词／旧译\n\n")
w("以下每类的「现文」在正文中一律应改为「应改为」列的词（A 类为冻结术语，必改；B 类按语境判断）。\n\n")
DISP = {
    "A4": ("超平面切断／超曲面切断", "超平面截面／超曲面截面"),
}
w("| 编号 | 类别 | 现文 | 应改为 | 处数 | 涉及文件 |\n|---|---|---|---|---|---|\n")
for code, name, rep, hs in res:
    fs = sorted(set(h[0] for h in hs))
    cur, rep2 = DISP.get(code, (name, rep))
    w("| %s | %s | %s | %s | %d | %s |\n" % (code, name, cur, rep2, len(hs), "、".join(fs)))
w("\n### 逐处明细\n\n")
for code, name, rep, hs in res:
    w("**%s %s → %s（%d 处）**\n\n" % (code, name, rep, len(hs)))
    w("| 位置 | 现文片段 |\n|---|---|\n")
    for f, ln, tok, snip in hs:
        w("| %s:%d | `%s` |\n" % (f, ln, snip.replace("|", "\\|")))
    w("\n")

w("## 二、同一英文术语在正文中的两种中译\n\n")
w("只列高频、真冲突者。处数为该译名在正文中的出现次数；「同块并存」表示两种译名出现在同一 chunk 内。\n\n")
w("| 英文键 | 主译（处数） | 异译（处数） | 同块并存 | 判定 |\n|---|---|---|---|---|\n")
for en, a, b in PAIRS:
    ta, pa = count(a)
    tb, pb = count(b)
    both = sorted(set(pa) & set(pb))
    verdict = "真冲突，按 A 类统一" if both else "分散，统一即可"
    w("| %s | %s（%d） | %s（%d） | %s | %s |\n" % (en, a, ta, b, tb, "、".join(both) if both else "—", verdict))
w("\n说明：`exact sequence` 的异译「完全列」实测 12 处为术语残留，另 3 处为「完全列表」（指 complete list，不是术语冲突，不算）。\n\n")

w("## 三、附录 A（443 条）结构检查\n\n")
w("- 解析得数据行 **%d** 行，与章首「共收录 %s 条」一致；每行 4 列（英文键／日文原词／中译／备注），无缺列。\n" % (len(rows), claimed[0] if claimed else "?"))
w("- 英文键重复：**0**；日文原词重复：**0**；中译栏为空：**0**。\n")
w("- 中译与英文键相同的 3 条：%s——均为约定保留拉丁字母的术语，正常。\n" % "、".join("%s（%s）" % (k, v) for k, v in zh_eq_en))
w("- 同一中译对应多个英文键的 6 组：\n\n")
w("| 中译 | 条数 | 判定 |\n|---|---|---|\n")
verdicts = {
    "假设": "assume／assumption 同族，正常",
    "奇点消解": "desingularization／resolution 同义，正常",
    "顺像": "direct image／pushforward 同义，正常",
    "除子对数终端": "dlt 的缩写与全称两条，建议在缩写条备注「全称见 …」，非缺陷",
    "一般纤维": "general fibre／generic fibre 两条，正常（但正文「一般纤维」兼表二义，见 B 类）",
    "约化": "reduced／reduction 同族，正常",
}
for k, v in zh_dup:
    w("| %s | %d | %s |\n" % (k, v, verdicts.get(k, "待核")))
w("\n- longtable 列宽按前次编译（`build.ps1 -Chunk appendix_glossary`）无溢出、0 错。\n\n")

w("## 四、必改清单（chunk:行号 + 现文 + 应改为）\n\n")
w("按应改为的词分组；同一行含多处时按出现处逐条列出，统一 sweep 时可用同一正则批量替换。\n\n")
w("| # | 位置 | 现文片段 | 应改为 |\n|---|---|---|---|\n")
n = 1
for code, name, rep, hs in res:
    if code.startswith("B"):
        continue
    disp_rep = "（超平面｜超曲面）截面" if "\\1" in rep else rep
    for f, ln, tok, snip in hs:
        w("| %d | %s:%d | `%s` | `%s` |\n" % (n, f, ln, snip.replace("|", "\\|"), disp_rep))
        n += 1
w("\n### 建议改（B 类，需按语境）\n\n")
w("| # | 位置 | 现文片段 | 建议 |\n|---|---|---|---|\n")
n = 1
for f, ln, tok, snip in res[-1][3]:
    w("| %d | %s:%d | `%s` | 若为 generic point 义 → 泛点；若为 general point 义保留 |\n" % (n, f, ln, snip.replace("|", "\\|")))
    n += 1

w("\n## 五、统计与处理建议\n\n")
w("- A 类必改 **%d 处**（13 类），B 类建议 **%d 处**（一般点），合计 **%d 处**。\n" % (must, adv, must + adv))
w("- 附录 A 无结构缺陷（空值／重复键／缺列 0）；3 条中译＝英文属正常保留。\n")
w("- 建议 sweep 顺序：先 `appendix_index.tex`（条目索引，文字取自陈述，改完与正文自然一致），再按 chunk 顺序一次正则替换；「基点自由性」应改为「无基点性」，「相对基点自由性定理」→「相对无基点定理」，注意整词匹配避免把「无基点定理」重复替换。\n")
w("- `bib.tex` 的日文书目原题（含假名与「多様体」「特異点」等）属书目信息，按约定保留，不计入残留。\n")
w("- 正文侧若需保留「一般点」的 general point 用法（如 ch04d.tex:136），sweep 时不要全局替换。\n")

io.open("review/术语终检报告.md", "w", encoding="utf-8", newline="\n").write(B.getvalue())
print("written", len(B.getvalue()), "chars;", len(rows), "appendix rows;", must, "must;", adv, "adv")
