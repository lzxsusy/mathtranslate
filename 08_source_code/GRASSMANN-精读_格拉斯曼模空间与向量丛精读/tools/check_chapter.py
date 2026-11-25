# -*- coding: utf-8 -*-
"""按 BRIEF §7 逐章检查 6 个交付物（Lead 验收用）。

用法：
    python tools/check_chapter.py 3          # 检查 ch3
    python tools/check_chapter.py all        # 检查 9 章，输出汇总表
    python tools/check_chapter.py 3 -v       # 附每项细节

输出刻意用 ASCII 标签，避免 Windows 终端中文乱码；详细中文原因写 tmp/check-chNN.txt。
"""
import os
import re
import sys
import io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HAN = re.compile(r"[\u4e00-\u9fff]")
ERRATA_HEADER = ["chapter", "loc_book", "loc_zh", "loc_tex", "type", "severity",
                 "original", "problem", "suggestion", "evidence"]
CARD_HEADER = ["local_id", "type", "title_en", "title_zh", "track", "one_line", "anchor"]
TYPES = {"数学-难点", "数学-补证", "译注-核对", "译文-问题", "联系-他章", "背景-补充"}
REQUIRED_TYPES = ["数学-难点", "数学-补证", "译注-核对", "译文-问题", "联系-他章"]


def read(p):
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8-sig") as f:
        return f.read()


def check(nn, verbose=False):
    res = []   # (label, ok, detail)

    # 1. 导读
    p = os.path.join(ROOT, "产出", "导读", f"ch{nn}-导读.md")
    t = read(p)
    if t is None:
        res.append(("daodu", False, "missing"))
    else:
        han = len(HAN.findall(t))
        heads = re.findall(r"^##\s+[一二三四五]、(.+)$", t, re.M)
        # BRIEF §8.1 模板：干什么 / 之前 / 怎么读 / 核心结果 / 术语对照；也接受同义写法
        want = [("干什么", "位置", "书里"), ("之前", "前置"), ("怎么读", "路线"),
                ("核心", "结果"), ("术语",)]
        miss = [w[0] for i, w in enumerate(want)
                if i >= len(heads) or not any(k in heads[i] for k in w)]
        res.append(("daodu", han >= 1200 and len(heads) >= 5 and not miss,
                    f"han={han} secs={len(heads)} miss={miss}"))

    # 2. 批注
    p = os.path.join(ROOT, "产出", "批注", f"ch{nn}-批注.md")
    t = read(p)
    if t is None:
        res.append(("pizhu", False, "missing"))
    else:
        nums = [int(x) for x in re.findall(r"^##\s+(\d+)[\.、]", t, re.M)]
        cont = nums == list(range(1, len(nums) + 1)) and len(nums) >= 12
        have = {ty for ty in TYPES if f"【{ty}】" in t}
        miss = [ty for ty in REQUIRED_TYPES if ty not in have]
        # 每条是否含四要素（粗查：位置/原文/批注出现次数 >= 条数；去掉 markdown 强调符再数）
        t2 = t.replace("**", "").replace("`", "").replace("__", "")
        c_loc = t2.count("位置：")
        c_orig = t2.count("原文摘录：") + t2.count("原文：")
        c_note = t2.count("批注：")
        quad = min(c_loc, c_orig, c_note) >= len(nums) and len(nums) > 0
        ok = cont and not miss and quad
        res.append(("pizhu", ok, f"n={len(nums)} cont={cont} miss={miss} loc/orig/note={c_loc}/{c_orig}/{c_note}"))

    # 3. errata.tsv
    p = os.path.join(ROOT, "产出", "批注", f"ch{nn}-errata.tsv")
    t = read(p)
    if t is None:
        res.append(("errata", False, "missing"))
    else:
        lines = t.splitlines()
        head = [h.strip() for h in lines[0].split("\t")] if lines else []
        bad = 0
        rows = 0
        thin = []   # 证据/原文过短的条目
        for ln in lines[1:]:
            if not ln.strip():
                continue
            rows += 1
            fld = ln.split("\t")
            if len(fld) != len(ERRATA_HEADER):
                bad += 1
                continue
            if len(fld[9].strip()) < 8:
                thin.append(str(rows))
        hdr_ok = head == ERRATA_HEADER
        res.append(("errata", hdr_ok and bad == 0 and not thin,
                    f"hdr={hdr_ok} rows={rows} badcols={bad} thin={thin[:5]}"))

    # 4. 笔记
    p = os.path.join(ROOT, "产出", "笔记", f"ch{nn}-笔记.md")
    t = read(p)
    if t is None:
        res.append(("biji", False, "missing"))
    else:
        han = len(HAN.findall(t))
        heads = re.findall(r"^##\s+[一二三四五]、(.+)$", t, re.M)
        need = ["主线", "构造", "补", "疑问", "延伸"]
        miss = [k for k in need if not any(k in h for h in heads)]
        res.append(("biji", han >= 1500 and not miss, f"han={han} heads={len(heads)} miss={miss}"))

    # 5. cards tsv
    p = os.path.join(ROOT, "产出", "汇总", f"cards-ch{nn}.tsv")
    t = read(p)
    if t is None:
        res.append(("cards", False, "missing"))
    else:
        lines = [l for l in t.splitlines() if l.strip()]
        head = [h.strip() for h in lines[0].split("\t")] if lines else []
        hdr_ok = head == CARD_HEADER
        rows = lines[1:]
        badcols = sum(1 for l in rows if len(l.split("\t")) != 7)
        anc_bad = []
        src = os.path.join(ROOT, "source", "chapters", f"ch{nn}.tex")
        src_lines = read(src).splitlines() if os.path.exists(src) else []
        for l in rows:
            fld = l.split("\t")
            if len(fld) != 7:
                continue
            m = re.match(r"^chapters/ch(\d\d)\.tex:(\d+)$", fld[6].strip())
            if not m or m.group(1) != nn:
                anc_bad.append(fld[6])
                continue
            ln = int(m.group(2))
            if ln < 1 or ln > len(src_lines) or not src_lines[ln - 1].strip():
                anc_bad.append(f"{fld[6]}(blank/oob)")
        res.append(("cards", hdr_ok and badcols == 0 and not anc_bad and len(rows) >= 7,
                    f"hdr={hdr_ok} rows={len(rows)} badcols={badcols} bad_anchor={anc_bad[:3]}"))

    # 6. report
    p = os.path.join(ROOT, "产出", "汇总", f"ch{nn}-report.md")
    t = read(p)
    if t is None:
        res.append(("report", False, "missing"))
    else:
        # 支持两种写法：「存疑：……」（行内）与「## 三、存疑」小节
        m = re.search(r"存疑\s*[：:]\s*(.*?)(?:\n#|\Z)", t, re.S)
        if m:
            body = m.group(1).strip()
        else:
            m2 = re.search(r"^#+\s*[一二三四五六七八九十]*、?\s*存疑[^\n]*\n(.*?)(?=^#+\s|\Z)", t, re.S | re.M)
            body = m2.group(1).strip() if m2 else ""
        nonempty = len(body) > 5 and not re.fullmatch(r"(无|none|None|待补|TODO|—|-)", body.strip())
        res.append(("report", nonempty, f"cunyi_len={len(body)}"))

    return res


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = "-v" in sys.argv
    which = args[0] if args else "all"
    nns = [f"{i:02d}" for i in range(1, 10)] if which == "all" else [f"{int(which):02d}"]
    all_ok = True
    for nn in nns:
        res = check(nn, verbose)
        ok = all(r[1] for r in res)
        all_ok = all_ok and ok
        line = " ".join(f"{lbl}={'OK' if okk else 'FAIL'}" for lbl, okk, _ in res)
        print(f"ch{nn}: {'PASS' if ok else 'FAIL'} | {line}")
        if verbose or not ok:
            for lbl, okk, det in res:
                if verbose or not okk:
                    print(f"    {lbl}: {det}")
        out = os.path.join(ROOT, "tmp", f"check-ch{nn}.txt")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(f"ch{nn} {'PASS' if ok else 'FAIL'}\n")
            for lbl, okk, det in res:
                f.write(f"{lbl}\t{'OK' if okk else 'FAIL'}\t{det}\n")
    print("ALL PASS" if all_ok else "HAS FAIL")


if __name__ == "__main__":
    main()
