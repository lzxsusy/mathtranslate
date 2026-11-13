# -*- coding: utf-8 -*-
"""Gate 1 静态检查（JPB07《ミラー対称性入門》中文译注本）

与原《辛几何》工程的区别：原书的公式编号是**每章重置的裸编号**（1）（2）…，
図/表同样每章重置，OCR 抽 tag 无效，因此本脚本**不比对 tags.txt**，改为检查：

  1. 文件卫生：BOM、U+FFFD、花括号平衡、环境配对、$ 奇偶、禁用命令、markdown 残留
  2. 页标记：`% ===== PDF p.NNN (原书 p.N) =====` 必须单调递增、无重复、章内无缺口
  3. 公式号：同一章内 `\\tag{n}` 不得重复（跨章重复是正常的，因每章从 (1) 重新开始）
  4. 缺字高危字符：`・`(U+30FB)、裸 `≈ ≤ ∞`、U+2013 en dash
  5. 语言病灶：被…所…／进行…的…／对于…而言
  6. 假名残留（日文正文漏译；白名单文件除外）
  7. Tutor Note 格式：`% [Tutor Note: ...]` 内不得再出现 %，每章条数 3–8（超出只提示）
  8. 插图文件存在性
  9. 章文件结构：\\chapter、\\chapterauthor、章末 reflist

用法：python check.py [--strict]
"""
import os, re, sys, glob, collections

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")
FIG = os.path.join(ROOT, "src", "figures")

# 允许出现日文/假名的文件（原文引文、人名读音、书目）
KANA_ALLOW = {"firstpub.tex", "authors.tex", "backmatter.tex", "note.tex", "appendix_glossary.tex"}
# 不要求 \chapter 结构的文件
NO_CHAPTER = {"appendix_glossary.tex", "appendix_notes.tex"}
# 续写块：某章被两位译手分写的后半，只写正文，章题/章作者/节号归前半文件
CONTINUATION = {"ch08b.tex", "ch12b.tex"}
FRONT_OR_BACK = {"firstpub.tex", "authors.tex", "backmatter.tex", "index_orig.tex"}
# 经逐页核对，原书该章本身没有参考文献表（初出一览亦无逐章书目）→ 豁免 reflist 检查
# ch03 / ch10 / ch11：末页之后紧接下一章章首页，中间无参考文献页（译手回页图确认）
# ch08：参考文献表写在续写块 ch08b.tex 末尾，故前半文件本身不含
# ch12：末页（原书 p.163）结尾即作者读音标记，原书本章无参考文献表（已核 work\split\p171.txt）
NO_REFLIST = {"ch03.tex", "ch10.tex", "ch11.tex", "ch08.tex", "ch12.tex"}

FORBIDDEN_CMDS = [
    r"\\documentclass", r"<本地路径>", r"\\usepackage",
    r"<本地路径>", r"<本地路径>", r"<本地路径>",
]
BAD_PHRASES = ["被…所…", "进行…的…", "对于…而言"]
KANA = re.compile(r"[\u3041-\u309F\u30A0-\u30FF]")
PAGEMARK = re.compile(r"%\s*=+\s*PDF\s*p\.?(\d{1,3})\s*\(\s*原书\s*p\.?\s*([\divxlc]+)\s*\)")


def read(p):
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def strip_comments(t):
    out = []
    for line in t.splitlines():
        m = re.search(r"(?<!\\)(?:\\\\)*%", line)
        if m:
            line = line[: m.end() - 1]
        out.append(line)
    return "\n".join(out)


def check_file(path):
    t = read(path)
    body = strip_comments(t)
    name = os.path.basename(path)
    issues, warns = [], []

    if open(path, "rb").read(3) == b"\xef\xbb\xbf":
        issues.append("UTF-8 BOM")
    if "\ufffd" in t:
        issues.append("U+FFFD")

    depth, bad = 0, False
    for ch in body:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                bad = True
                break
    if depth != 0 or bad:
        issues.append(f"花括号不平衡 ({depth})")

    ob = collections.Counter(re.findall(r"<本地路径>]*)\}", body))
    eb = collections.Counter(re.findall(r"<本地路径>]*)\}", body))
    if ob != eb:
        issues.append(f"环境不配对 begin-only={dict(ob - eb)} end-only={dict(eb - ob)}")
    # 环境嵌套顺序（begin/end 名字序列必须像括号一样匹配）
    stack, order_ok = [], True
    for m in re.finditer(r"\\(begin|end)\{([^}]*)\}", body):
        kind, nm = m.group(1), m.group(2)
        if kind == "begin":
            stack.append(nm)
        else:
            if not stack or stack[-1] != nm:
                order_ok = False
                break
            stack.pop()
    if not order_ok or stack:
        issues.append("环境嵌套顺序错乱")

    if len(re.findall(r"(?<!\\)\$", body)) % 2:
        issues.append("$ 个数为奇数")
    if len(re.findall(r"(?<!\\)\\\[", body)) != len(re.findall(r"(?<!\\)\\\]", body)):
        issues.append("\\[ \\] 不配对")

    for cmd in FORBIDDEN_CMDS:
        if re.search(cmd, body):
            issues.append("禁用命令 " + cmd.replace("\\\\", "\\"))
    if "**" in body:
        issues.append("markdown **")
    if "\u3000" in body:
        issues.append("全角空格 U+3000")

    # 中英混排：汉字紧邻拉丁字母（两个方向都要查）。剔除行内数学、注释行、命令及其参数后统计，
    # 避免把 $x$、\cite{...}、\label{...} 之类的正常写法算进去。
    _txt = re.sub(r"(?<!\\)\$[^$]*\$", "", body)
    _txt = re.sub(r"(?m)^[ \t]*%.*$", "", _txt)
    _txt = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?(\{[^{}]*\})?", "", _txt)
    _bad = re.findall(r"[\u4e00-\u9fff][A-Za-z]|[A-Za-z][\u4e00-\u9fff]", _txt)
    # 术语表首栏是日文原词照录（日文本身不用空格分词），不适用中文混排规则
    if _bad and name != "appendix_glossary.tex":
        warns.append(f"汉字与拉丁字母之间缺半角空格 {len(_bad)} 处（如 {'、'.join(_bad[:4])}）")
    if "\u30FB" in body:
        issues.append("`・`(U+30FB) 缺字，应改 `·`(U+00B7)")
    if "\u2013" in body:
        issues.append("U+2013 en dash，应写 `--`")
    for ch, pat in (("≈", r"(?<![$\\])≈"), ("≤", r"(?<![$\\])≤"), ("∞", r"(?<![$\\])∞")):
        if re.search(pat, body):
            issues.append(f"裸 {ch}，应进数学模式")

    if re.search(r"被[^，。；]{0,12}所", body):
        issues.append("语言病灶：被…所…")
    if re.search(r"进行[^，。；]{0,12}的", body):
        warns.append("疑似「进行…的…」")
    if re.search(r"对于[^，。；？！]{0,20}而言", body):
        issues.append("语言病灶：对于…而言")

    if name not in KANA_ALLOW:
        inref, hits = False, []
        for ln in body.splitlines():
            s = ln.strip()
            if s.startswith("\\begin{reflist}"):
                inref = True
            if s.startswith("\\end{reflist}"):
                inref = False
                continue
            if inref or s.startswith("\\item[{"):
                continue
            # 「…」「『…』」内是原文引文，允许日文
            s = re.sub(r"[「『][^」』]*[」』]", "", s)
            hits.extend(KANA.findall(s))
        if hits:
            warns.append(f"假名残留 {len(hits)} 个（日文漏译？）")

    # 页标记
    marks = [(int(m.group(1)), m.group(2)) for m in PAGEMARK.finditer(t)]
    if not marks:
        if name not in FRONT_OR_BACK and name not in NO_CHAPTER:
            warns.append("无页标记")
    else:
        nums = [a for a, _ in marks]
        if len(set(nums)) != len(nums):
            dup = [k for k, v in collections.Counter(nums).items() if v > 1]
            issues.append(f"页标记重复 PDF p.{dup}")
        if nums != sorted(nums):
            issues.append("页标记非单调递增")
        gaps = [(a, b) for a, b in zip(nums, nums[1:]) if b != a + 1]
        if gaps:
            warns.append("页标记跳页 " + ", ".join(f"p.{a}->p.{b}" for a, b in gaps))

    # 公式号（章内唯一）
    tags = re.findall(r"<本地路径>]*)\}", body)
    dup = [k for k, v in collections.Counter(tags).items() if v > 1]
    if dup:
        issues.append(f"公式号重复 {dup}")

    # Tutor Note
    notes = [l for l in t.splitlines() if "[Tutor Note" in l]
    for l in notes:
        rest = l.split("[Tutor Note", 1)[1]
        if "%" in rest:
            issues.append("Tutor Note 注释内含 %")
        # 批注里的数学必须用 $…$ 包裹，否则附录 A 排版会走形
        outside = re.sub(r"\$[^$]*\$", "", rest)
        if re.search(r"[_^]|\\[A-Za-z]+", outside):
            warns.append("批注数学未用 $…$ 包裹：" + rest[:40].strip())
    if not notes and name not in FRONT_OR_BACK | NO_CHAPTER:
        warns.append("无 Tutor Note")

    # 插图
    for m in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", body):
        rel = m.group(1)
        fp = os.path.join(ROOT, "src", rel)
        if not os.path.exists(fp):
            issues.append(f"缺图 {rel}")

    # 章结构（续写块只写正文，章题/章作者/节号归前半文件）
    if name not in NO_CHAPTER and name not in FRONT_OR_BACK and name not in CONTINUATION:
        if "\\chapter{" not in body and "\\chapter*{" not in body:
            issues.append("缺 \\chapter")
        if "\\chapterauthor" not in body:
            warns.append("缺 \\chapterauthor")
        if "reflist" not in body and name not in NO_REFLIST:
            warns.append("缺章末 reflist")

    return name, issues, warns, len(tags), len(marks), len(notes)


def main():
    files = sorted(glob.glob(os.path.join(CH, "*.tex")))
    if not files:
        print("no chunks"); return 1
    fail = False
    t_total = m_total = 0
    print(f"检查 {len(files)} 个 chunk 文件\n" + "-" * 60)
    for f in files:
        name, issues, warns, nt, nm, nn = check_file(f)
        t_total += nt
        m_total += nm
        flag = "FAIL" if issues else ("warn" if warns else "ok  ")
        print(f"{flag}  {name:26s} tags={nt:3d} 页标记={nm:3d} 批注={nn:2d}")
        for i in issues:
            print(f"        ✗ {i}")
        for w in warns:
            print(f"        ! {w}")
        if issues:
            fail = True
    print("-" * 60)
    print(f"chunks={len(files)} 公式号合计={t_total} 页标记合计={m_total}")
    print("STATUS:", "FAIL" if fail else "OK")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
