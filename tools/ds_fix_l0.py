# -*- coding: utf-8 -*-
"""ds_fix_l0.py — 对候选项做 L0 级确定性修正，并把改动写回语料。

用法：
    python tools/ds_fix_l0.py --batch 50 --apply
    python tools/ds_fix_l0.py --batch 50 --dry-run

只做可逆、可解释的修改：
  - flags 含 meta_block / template 的记录 → 删除（模板残渣，不是正文）；
  - 去掉排版残渣（[6pt] / 1.15 / 3em / 纯数字行），合并多余空白；
  - `\\mathbb C` → `\\mathbb{C}` 等；
  - 修改后为空 → 删除。
所有改动写入 datasets/fixes/l0_batchNN.jsonl（before/after 可回滚），
删除的记录同样留档。语料由外部流水线生成；重新生成后需重跑本脚本。
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "01_corpus_zh", "zh_paragraphs.jsonl")
QUEUE = os.path.join(ROOT, "datasets", "candidates", "harvest_queue.jsonl")
FIX_DIR = os.path.join(ROOT, "datasets", "fixes")

SIZE_RE = re.compile(r"\[\s*\d+(?:\.\d+)?\s*(?:pt|em|mm|cm|ex)\s*\]")
NUM_LINE_RE = re.compile(r"^\s*\d+(?:\.\d+)*\s*$", re.M)
MULTISPACE_RE = re.compile(r"[ \t]{3,}")
BLACKBOARD_RE = re.compile(r"\\mathbb\s+([A-Z])")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
DEF_RE = re.compile(
    r"\\(?:newcommand|renewcommand|providecommand)\*?\s*\{?\\([A-Za-z]+)\}?"
    r"(?:\s*\[\d\])?\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")
OP_RE = re.compile(r"\\DeclareMathOperator\*?\s*\{\\([A-Za-z]+)\}\s*\{([^{}]*)\}")

DROP_FLAGS = {"meta_block", "template"}
_MACRO_CACHE = {}


def macro_map(pkg):
    """按工程读取导言区宏定义，返回 {name: expansion}；只收无参数宏。"""
    if pkg in _MACRO_CACHE:
        return _MACRO_CACHE[pkg]
    base = os.path.join(ROOT, "08_source_code")
    mapping = {}
    for dirname in os.listdir(base):
        if not dirname.startswith(pkg + "_") and dirname != pkg:
            continue
        for dirpath, _dirs, files in os.walk(os.path.join(base, dirname)):
            for name in files:
                if not name.endswith((".tex", ".sty")):
                    continue
                try:
                    txt = io.open(os.path.join(dirpath, name), encoding="utf-8",
                                  errors="replace").read()
                except OSError:
                    continue
                for m in DEF_RE.finditer(txt):
                    val = m.group(2).strip()
                    if "#" not in val and val:
                        mapping[m.group(1)] = val
                for m in OP_RE.finditer(txt):
                    mapping.setdefault(m.group(1), "\\operatorname{%s}" % m.group(2).strip())
    _MACRO_CACHE[pkg] = mapping
    return mapping


def expand(text, pkg):
    m = macro_map(pkg)
    if not m:
        return text
    # 只替换独立使用的宏：\R 后不接字母
    def repl(match):
        name = match.group(1)
        return m.get(name, match.group(0))
    return re.sub(r"\\([A-Za-z]+)(?![A-Za-z])", repl, text)


def cjk(s):
    return len(CJK_RE.findall(s))


def clean(text, flags, pkg):
    t = str(text or "").replace("\r\n", "\n")
    t = SIZE_RE.sub("", t)
    if flags & {"layout_residue", "meta_block", "orphan_number"}:
        t = NUM_LINE_RE.sub("", t)
    t = expand(t, pkg)
    t = BLACKBOARD_RE.sub(r"\\mathbb{\1}", t)
    t = MULTISPACE_RE.sub(" ", t)
    t = t.strip()
    return t


def main():
    batch = 50
    if "--batch" in sys.argv:
        batch = int(sys.argv[sys.argv.index("--batch") + 1])
    apply = "--apply" in sys.argv
    if not (apply or "--dry-run" in sys.argv):
        print("需要 --apply 或 --dry-run")
        return 2

    queued = []
    with io.open(QUEUE, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            if r.get("type") == "paragraph":
                queued.append(r["id"])
    picked = queued[:batch]

    # 先把语料读进内存：para_id -> (index, record)
    records = []
    with io.open(CORPUS, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    idx = {r.get("para_id"): i for i, r in enumerate(records)}

    fixes, dropped, edited = [], 0, 0
    out = []
    for i, rec in enumerate(records):
        pid = rec.get("para_id")
        if pid not in picked:
            out.append(rec)
            continue
        flags = set(rec.get("flags") or [])
        before = str(rec.get("text") or "")
        if flags & DROP_FLAGS:
            dropped += 1
            fixes.append({"id": pid, "pkg": rec.get("pkg"), "action": "drop",
                          "reason": "flags=" + ",".join(sorted(flags & DROP_FLAGS)),
                          "before": before[:2000]})
            continue
        after = clean(before, flags, str(rec.get("pkg") or ""))
        if not after:
            dropped += 1
            fixes.append({"id": pid, "pkg": rec.get("pkg"), "action": "drop",
                          "reason": "清理后为空", "before": before[:2000]})
            continue
        if after != before:
            edited += 1
            rec = dict(rec)
            rec["text"] = after
            rec["zh_chars"] = cjk(after)
            rec["flags"] = sorted(flags | {"l0_fixed"})
            fixes.append({"id": pid, "pkg": rec.get("pkg"), "action": "edit",
                          "reason": "去排版残渣/展开黑板体/合并空白",
                          "before": before[:2000], "after": after[:2000]})
        out.append(rec)

    print("picked %d, edited %d, dropped %d, kept %d -> %d" %
          (len(picked), edited, dropped, len(records) - dropped, len(out)))
    for r in fixes[:5]:
        print("  %s %s %s" % (r["action"], r["id"], r["reason"]))
        if r.get("after"):
            print("    before: %s" % r["before"].replace("\n", " ")[:100])
            print("    after : %s" % r["after"].replace("\n", " ")[:100])

    if not apply:
        return 0

    if not os.path.isdir(FIX_DIR):
        os.makedirs(FIX_DIR)
    tag = "l0_batch%02d" % ((len(os.listdir(FIX_DIR)) if os.path.isdir(FIX_DIR) else 0) + 1)
    fix_path = os.path.join(FIX_DIR, tag + ".jsonl")
    with io.open(fix_path, "w", encoding="utf-8", newline="\n") as f:
        for r in fixes:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with io.open(CORPUS, "w", encoding="utf-8", newline="\n") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("wrote %s (%d fixes)" % (os.path.relpath(fix_path, ROOT).replace("\\", "/"), len(fixes)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
