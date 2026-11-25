# -*- coding: utf-8 -*-
"""校验 _cards_grassmann 的卡片。

    python tools\\validate_cards.py              # 全部卡
    python tools\\validate_cards.py --strict     # 额外要求 taxonomy.md 里列的卡都存在
    python tools\\validate_cards.py cards/concepts/xxx.json

退出码 0 = 全过；1 = 有 error（warn 不影响退出码）。
"""
import os
import re
import sys
import io
import json
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
CHDIR = os.path.join(os.path.dirname(ROOT), "Grassmannians-精读", "source", "chapters")
_NO_SRC = False
TAXONOMY = os.path.join(ROOT, "taxonomy.md")

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

TRACKS = {"A"} | {str(i) for i in range(1, 10)}
ID_RE = re.compile(r"^grassmann/(concept|example)/[a-z0-9][a-z0-9-]*$")
ANCHOR_RE = re.compile(r"^chapters/ch(0[1-9])\.tex:(\d+)$")
ABS_PATH_RE = re.compile(r"[A-Za-z]:\\[A-Za-z0-9_. -]+\\|[A-Za-z]:/[A-Za-z0-9_. -]+/")

errs = []
warns = []


def err(path, msg):
    errs.append("%s: %s" % (os.path.basename(path), msg))


def warn(path, msg):
    warns.append("%s: %s" % (os.path.basename(path), msg))


def cjk_len(s):
    return sum(1 for ch in s if "\u4e00" <= ch <= "\u9fff")


def nonempty(s):
    return isinstance(s, str) and s.strip() != ""


def walk_strings(o, path=""):
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk_strings(v, "%s[%d]" % (path, i))
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from walk_strings(v, "%s.%s" % (path, k))


def tex_lines(chap):
    p = os.path.join(CHDIR, "ch%s.tex" % chap)
    if not os.path.isfile(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.readlines()


def check_anchor(path, a):
    m = ANCHOR_RE.match(a or "")
    if not m:
        err(path, "anchor 格式错（应为 chapters/chNN.tex:行号）: %r" % (a,))
        return False
    chap, ln = m.group(1), int(m.group(2))
    lines = tex_lines(chap)
    if lines is None:
        if not os.path.isdir(CHDIR):
            global _NO_SRC
            if not _NO_SRC:
                _NO_SRC = True
                warn(path, "缺少 source/chapters 源码树，跳过 anchor 行号校验（只查格式）")
            return True
        err(path, "anchor 指向不存在的章文件 ch%s.tex" % chap)
        return False
    if not (1 <= ln <= len(lines)):
        err(path, "anchor 行号 %d 超出 ch%s.tex（共 %d 行）" % (ln, chap, len(lines)))
        return False
    if lines[ln - 1].strip() == "":
        warn(path, "anchor ch%s.tex:%d 是空行" % (chap, ln))
        return False
    return True


def check_proof(path, pr, tname):
    if not isinstance(pr, dict):
        err(path, "theorem[%s].proof 必须是对象" % tname)
        return
    st = pr.get("status")
    if st not in ("complete", "sketch", "reference"):
        err(path, "theorem[%s].proof.status 非法: %r" % (tname, st))
        return
    if st == "complete":
        steps = pr.get("steps") or []
        if not isinstance(steps, list) or len(steps) < 2:
            err(path, "theorem[%s] status=complete 需 steps≥2" % tname)
            return
        for i, s in enumerate(steps):
            if not isinstance(s, dict) or not nonempty(s.get("text")) or not nonempty(s.get("why")):
                err(path, "theorem[%s].steps[%d] 缺 text 或 why" % (tname, i))
    elif st == "sketch":
        if not nonempty(pr.get("gap_note")):
            err(path, "theorem[%s] status=sketch 需 gap_note" % tname)


def check_card(path, card, ids, concept_ids):
    ct = card.get("type")
    if ct not in ("concept", "example"):
        err(path, "type 必须是 concept/example，得到 %r" % (ct,))
        return
    cid = card.get("id", "")
    if not ID_RE.match(cid):
        err(path, "id 不合规范: %r" % (cid,))
    else:
        if not cid.startswith("grassmann/%s/" % ct):
            err(path, "id 前缀与 type 不一致: %r" % (cid,))
        slug = cid.rsplit("/", 1)[-1]
        if os.path.splitext(os.path.basename(path))[0] != slug:
            err(path, "文件名与 id 末段不一致: %r vs %r" % (os.path.basename(path), slug))

    if not nonempty(card.get("title")):
        err(path, "缺 title")
    if not isinstance(card.get("aliases"), list):
        err(path, "aliases 必须是数组")
    if card.get("track") not in TRACKS:
        err(path, "track 非法: %r（A 或 1–9）" % (card.get("track"),))

    s = card.get("summary", "")
    n = cjk_len(s) if isinstance(s, str) else 0
    if not (20 <= n <= 120):
        err(path, "summary 汉字数 %d 不在 20–120" % n)
    q = card.get("question", "")
    if not (isinstance(q, str) and q.strip().endswith(("？", "?"))):
        err(path, "question 必须以问号结尾")

    d = card.get("definition") or {}
    if not isinstance(d, dict) or not nonempty(d.get("text")):
        err(path, "definition.text 空")
    if not nonempty(d.get("notation")):
        warn(path, "definition.notation 空（建议补记号约定）")

    kp = card.get("key_points") or []
    if not isinstance(kp, list) or len(kp) < 3:
        err(path, "key_points 需 ≥3 条")
    elif any(not nonempty(x) for x in kp):
        err(path, "key_points 有空条目")

    fs = card.get("formulas") or []
    if not isinstance(fs, list) or len(fs) < 1:
        err(path, "formulas 需 ≥1 条")
    else:
        for i, f in enumerate(fs):
            if not nonempty(f):
                err(path, "formulas[%d] 空" % i)
            elif isinstance(f, str) and f.count("$") % 2 == 1:
                err(path, "formulas[%d] $ 不成对" % i)

    th = card.get("theorems") or []
    if not isinstance(th, list) or len(th) < 1:
        err(path, "theorems 需 ≥1 条")
    else:
        for t in th:
            if not isinstance(t, dict):
                err(path, "theorems 条目必须是对象")
                continue
            nm = t.get("name", "?")
            for k in ("name", "statement", "source"):
                if not nonempty(t.get(k)):
                    err(path, "theorem[%s] 缺 %s" % (nm, k))
            check_proof(path, t.get("proof"), nm)

    pf = card.get("pitfalls") or []
    if not isinstance(pf, list) or len(pf) < 1:
        err(path, "pitfalls 需 ≥1 条（真坑）")

    rel = card.get("related") or []
    if not isinstance(rel, list) or len(rel) < 2:
        err(path, "related 需 ≥2 条概念卡 id")
    else:
        for r in rel:
            if r not in concept_ids and r not in ids:
                err(path, "related 里有无法解析的 id: %r" % (r,))

    if ct == "example":
        cr = card.get("concept_refs") or []
        if not isinstance(cr, list) or len(cr) < 2:
            err(path, "例子卡 concept_refs 需 ≥2")
        else:
            for r in cr:
                if r not in concept_ids:
                    err(path, "concept_refs 里不是概念卡 or 不存在: %r" % (r,))
        for k in ("setup", "computation"):
            if not nonempty(card.get(k)):
                err(path, "例子卡缺 %s" % k)

    srcs = card.get("sources") or []
    if not isinstance(srcs, list) or len(srcs) < 1:
        err(path, "sources 需 ≥1 条")
    else:
        for i, s2 in enumerate(srcs):
            if not isinstance(s2, dict):
                err(path, "sources[%d] 必须是对象" % i)
                continue
            for k in ("book", "section", "pages_zh", "pages_en", "anchor"):
                if not nonempty(s2.get(k)):
                    err(path, "sources[%d] 缺 %s" % (i, k))
            check_anchor(path, s2.get("anchor"))

    if card.get("rights") != "rewritten":
        err(path, "rights 必须是 rewritten")
    if card.get("status") not in ("draft", "reviewed"):
        err(path, "status 必须是 draft/reviewed")

    for where, val in walk_strings(card):
        if ABS_PATH_RE.search(val):
            err(path, "出现本机绝对路径（%s）" % where)
            break
        if "\t" in val:
            err(path, "含 tab（%s）" % where)
            break


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    strict = "--strict" in sys.argv
    files = args or sorted(glob.glob(os.path.join(CARDS, "*", "*.json")))
    if not files:
        print("没有卡片文件")
        return 1

    cards = []
    for p in files:
        try:
            with open(p, encoding="utf-8") as f:
                c = json.load(f)
        except Exception as e:  # noqa: BLE001
            err(p, "JSON 解析失败: %s" % e)
            continue
        cards.append((p, c))

    ids = {c.get("id") for _, c in cards}
    concept_ids = {c.get("id") for _, c in cards if c.get("type") == "concept"}
    dup = len(cards) - len(ids)
    if dup:
        errs.append("有 %d 个重复 id" % dup)

    for p, c in cards:
        check_card(p, c, ids, concept_ids)

    if strict and os.path.isfile(TAXONOMY):
        with open(TAXONOMY, encoding="utf-8") as f:
            tax = f.read()
        want = set(re.findall(r"`(grassmann/(?:concept|example)/[a-z0-9-]+)`", tax))
        missing = want - ids
        extra = ids - want
        for m in sorted(missing):
            errs.append("taxonomy 列了但文件不存在: %s" % m)
        if extra:
            warns.append("有 %d 张卡未登记进 taxonomy" % len(extra))

    out = ["概念卡 %d / 例子卡 %d / 共 %d" % (
        sum(1 for _, c in cards if c.get("type") == "concept"),
        sum(1 for _, c in cards if c.get("type") == "example"), len(cards))]
    out += ["ERROR " + e for e in errs]
    out += ["WARN  " + w for w in warns]
    out.append("结论：%d error, %d warn" % (len(errs), len(warns)))
    print("\n".join(out))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
