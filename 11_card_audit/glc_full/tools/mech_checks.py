#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mechanical cross-checks for every glc card (lead baseline, independent of A/B).

Truth sources
  * PDF TOC (printed pages 1-4)             -> section number -> printed page
  * 源码/chapters/chNN.tex \\label{sec:N.M}   -> section number -> local line span
  * 源码/chapters/chNN.tex {N.M.K}          -> numbered object -> local line
  * PDF body page texts                     -> where a number actually appears

Anchor grammar actually used by the cards (all 160 show one of these):
  "源码/chapters/ch02.tex:51-55（定理 2.2.4）"
  "源码/chapters/ch04.tex:143-146,160-169（§4.8 定义 4.8.1、§4.10）"
  "定理 9.1.1（ch09.tex:12-16，p.48）"
  "源码/chapters/ch08.tex:123（尖点性论证）；124-126 为编者注"
"""
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
REPO = os.path.abspath(os.path.join(ROOT, "..", "..", ".."))
CH_DIR = os.path.join(
    REPO, "08_source_code",
    "SY02-33_几何Langlands理论导论（陈麟）_中文译注校订版", "源码", "chapters")

TOC_LINE = re.compile(r"^\s*(\d{1,2}\.\d{1,2})\.\s+(.+?)\s+(\d{1,3})\s*$")
SEC_LABEL = re.compile(r"\\label\{sec:(\d{1,2}\.\d{1,2})\}")
OBJ = re.compile(r"\{(\d{1,2}\.\d{1,2}\.\d{1,2})\}")
SEC_CLAIM = re.compile(r"§\s*(\d{1,2}\.\d{1,2})")
OBJ_CLAIM = re.compile(r"(?:定义|定理|命题|引理|猜想|推论)\s*(\d{1,2}\.\d{1,2}\.\d{1,2})")
CHAP_CLAIM = re.compile(r"第\s*(\d{1,2})\s*章")
CHREF = re.compile(r"ch(\d{1,2})\.tex:((?:\d+(?:-\d+)?)(?:[,，]\s*\d+(?:-\d+)?)*)")
BARE_RANGE = re.compile(r"(?<![\d:.-])(\d+)-(\d+)\s*行")
PAGE_IN_SRC = re.compile(r"p\.\s*(\d{1,3})(?:\s*[–~-]\s*(\d{1,3}))?")
NUM_IN_PDF = re.compile(r"(?<!\d)(?<!\.\d)(\d{1,2}\.\d{1,2}\.\d{1,2})(?!\d)(?!\.\d)")
SRC_PAGE = re.compile(r"^\s*\\srcpage\{(\d+)\}")
UNNUMBERED = ("未编号", "无编号", "没有编号")


def load_toc():
    toc = {}
    for p in range(1, 7):
        fn = os.path.join(ROOT, "tmp", "pages", "p%03d.txt" % p)
        if not os.path.isfile(fn):
            continue
        lines = open(fn, encoding="utf-8").read().splitlines()
        i = 0
        while i < len(lines):
            s = lines[i]
            i += 1
            m = TOC_LINE.match(s)
            if m:
                toc[m.group(1)] = {"title": m.group(2), "page": int(m.group(3))}
                continue
            m2 = re.match(r"^\s*(\d{1,2}\.\d{1,2})\.\s+(\S.*)$", s)
            if m2 and i < len(lines):
                m3 = re.match(r"^\s*(.+?)\s+(\d{1,3})\s*$", lines[i])
                if m3 and not re.match(r"^\s*\d{1,2}\.\d{1,2}\.", lines[i]):
                    toc[m2.group(1)] = {"title": m2.group(2) + " " + m3.group(1),
                                        "page": int(m3.group(2))}
                    i += 1
    return toc


def load_tex():
    """section -> [(chapter, start_line, end_line)], object -> [(chapter, line)]"""
    secs, objs = {}, {}
    for fn in sorted(glob.glob(os.path.join(CH_DIR, "ch*.tex"))):
        ch = int(re.search(r"ch(\d+)\.tex$", fn).group(1))
        raw = open(fn, encoding="utf-8").read().splitlines()
        labels = []
        for n, line in enumerate(raw, 1):
            for m in SEC_LABEL.finditer(line):
                labels.append((n, m.group(1)))
                objs_for = None  # noqa: F841
            for m in OBJ.finditer(line):
                objs.setdefault(m.group(1), []).append((ch, n))
        labels.sort()
        for i, (ln, num) in enumerate(labels):
            end = labels[i + 1][0] - 1 if i + 1 < len(labels) else len(raw)
            secs.setdefault(num, []).append((ch, ln, end))
    return secs, objs


def tex_page_map():
    """ch -> {line: printed original page}, driven by \\srcpage{N} markers.

    Convention (verified against glc.pdf): \\srcpage{N} is a page-break marker, the
    text AFTER it lives on printed page N; the marker line itself is assigned to N.
    Lines before the first marker get None.
    """
    out = {}
    for fn in sorted(glob.glob(os.path.join(CH_DIR, "ch*.tex"))):
        ch = int(re.search(r"ch(\d+)\.tex$", fn).group(1))
        cur, m = None, {}
        for i, line in enumerate(open(fn, encoding="utf-8"), 1):
            mm = SRC_PAGE.match(line)
            if mm:
                cur = int(mm.group(1))
            m[i] = cur
        out[ch] = m
    return out


def pdf_object_pages():
    idx = {}
    for fn in sorted(glob.glob(os.path.join(ROOT, "tmp", "pages", "p*.txt"))):
        pno = int(re.search(r"p(\d+)\.txt$", fn).group(1))
        if pno <= 4:          # cover + TOC (p.2-4) carry every number; ignore them
            continue
        for m in NUM_IN_PDF.finditer(open(fn, encoding="utf-8").read()):
            idx.setdefault(m.group(1), set()).add(pno)
    return idx


def parse_anchor(anchor):
    refs = []
    for m in CHREF.finditer(anchor):
        ch = int(m.group(1))
        rngs = []
        for part in re.split(r"[,，]\s*", m.group(2)):
            if "-" in part:
                a, b = part.split("-")
                rngs.append((int(a), int(b)))
            else:
                rngs.append((int(part), int(part)))
        refs.append([ch, rngs])
    if refs:
        consumed = [m.span(2) for m in CHREF.finditer(anchor)]
        for m in re.finditer(r"(?<![\w.])(\d+)-(\d+)(?!\d)", anchor):
            if any(m.start() >= a and m.end() <= b for a, b in consumed):
                continue
            if re.search(r"p\.\s*$", anchor[:m.start()]) or "页" in anchor[m.start() - 2:m.start()]:
                continue
            refs[-1][1].append((int(m.group(1)), int(m.group(2))))
    phints = [int(m.group(1)) for m in re.finditer(r"p\.\s*(\d{1,3})", anchor)]
    return refs, phints


def card_texts(c):
    out = []
    for key in ("section", "summary", "question", "definition", "key_points",
                "formulas", "theorems", "pitfalls", "sources"):
        v = c.get(key)
        if isinstance(v, str):
            out.append(v)
        elif isinstance(v, list):
            for it in v:
                if isinstance(it, str):
                    out.append(it)
                elif isinstance(it, dict):
                    out.extend(x for x in it.values() if isinstance(x, str))
        elif isinstance(v, dict):
            out.extend(x for x in v.values() if isinstance(x, str))
    return out


def main():
    toc = load_toc()
    secs, objs = load_tex()
    tpg = tex_page_map()
    pdfobj = pdf_object_pages()
    toc_pages = sorted({v["page"] for v in toc.values()})
    cards = []
    for p in sorted(glob.glob(os.path.join(REPO, "datasets", "glc", "cards",
                                           "**", "*.json"), recursive=True)):
        cards.append((p, json.load(open(p, encoding="utf-8"))))

    out = []
    for path, c in cards:
        flags = []
        rel = os.path.relpath(path, REPO).replace("\\", "/")
        texts = card_texts(c)
        honest_unnumbered = [t for t in texts if any(u in t for u in UNNUMBERED)]

        for si, s in enumerate(c["sources"]):
            tag = "sources[%d]" % si
            pset = set(s["pages"])
            if list(s["pages"]) != list(s["pdf_pages"]):
                flags.append({"code": "source_pages_eq", "where": tag,
                              "detail": "pages%s != pdf_pages%s"
                                        % (s["pages"], s["pdf_pages"])})
            refs, phints = parse_anchor(s["anchor"])
            if not refs:
                flags.append({"code": "anchor_unparsed", "where": tag,
                              "detail": s["anchor"][:120]})
                continue
            chapters = {ch for ch, _ in refs}
            secs_claimed = sorted(set(SEC_CLAIM.findall(s["section"])))
            chaps_claimed = [int(x) for x in CHAP_CLAIM.findall(s["section"])]
            want_ch = {int(sc.split(".")[0]) for sc in secs_claimed} | set(chaps_claimed)
            if want_ch and not (want_ch & chapters):
                flags.append({"code": "anchor_chapter", "where": tag,
                              "detail": "section %r wants ch%s, anchor ch%s"
                                        % (s["section"][:40], sorted(want_ch),
                                           sorted(chapters))})
            for sc in secs_claimed:
                ch = int(sc.split(".")[0])
                locs = [(a, b) for cc, a, b in secs.get(sc, []) if cc == ch]
                if sc not in toc:
                    flags.append({"code": "toc_missing", "where": tag,
                                  "detail": "§%s not in PDF TOC" % sc})
                if not locs:
                    flags.append({"code": "section_absent_tex", "where": tag,
                                  "detail": "no \\label{sec:%s}" % sc})
                else:
                    a, b = locs[0]
                    hit = any(cc == ch and not (hi < a or lo > b)
                              for cc, rngs in refs for lo, hi in rngs)
                    if not hit:
                        flags.append({"code": "anchor_section", "where": tag,
                                      "detail": "§%s spans L%d-%d, anchor %s"
                                                % (sc, a, b, s["anchor"][:64])})
                if sc in toc:
                    tp = toc[sc]["page"]
                    later = [q for q in toc_pages if q > tp]
                    tq = later[0] if later else tp + 4
                    if not (pset & set(range(tp, tq + 1))):
                        flags.append({"code": "page_section", "where": tag,
                                      "detail": "§%s spans p.%d–%d, card says %s"
                                                % (sc, tp, tq - 1, s["pages"])})
            for ph in phints:
                ok = ph in pset
                for sc in secs_claimed:
                    if not ok and sc in toc and abs(toc[sc]["page"] - ph) <= 1:
                        ok = True
                if not ok:
                    flags.append({"code": "page_hint", "where": tag,
                                  "detail": "anchor hint p.%d vs card pages %s"
                                            % (ph, s["pages"])})

            apages = set()
            for ch, rngs in refs:
                for lo, hi in rngs:
                    for ln in range(lo, hi + 1):
                        pp = tpg.get(ch, {}).get(ln)
                        if pp:
                            apages.add(pp)
            extra = sorted(apages - pset)
            if extra:
                flags.append({"code": "anchor_pages", "where": tag,
                              "detail": "anchor-cited lines live on p.%s, outside pages %s"
                                        % (extra, s["pages"])})

        claims = {}
        for t in [s2["section"] for s2 in c["sources"]]:
            for m in OBJ_CLAIM.finditer(t):
                claims.setdefault(m.group(1), set()).add("sources")
        for ti, th in enumerate(c["theorems"]):
            for m in OBJ_CLAIM.finditer(th.get("source", "")):
                claims.setdefault(m.group(1), set()).add("theorems[%d]" % ti)
        pset = set().union(*[set(s["pages"]) for s in c["sources"]])
        for num, where in sorted(claims.items()):
            locs = objs.get(num, [])
            pages_found = pdfobj.get(num, set())
            if not locs:
                flags.append({"code": "object_absent_tex", "where": num,
                              "detail": "%s has no {N.M.K} anywhere in 源码" % num})
                continue
            if pages_found:
                if not (pset & pages_found) and not any(
                        abs(p - q) <= 1 for p in pset for q in pages_found):
                    flags.append({"code": "page_object", "where": num,
                                  "detail": "%s on PDF p.%s, card says %s"
                                            % (num, sorted(pages_found), sorted(pset))})
            elif not honest_unnumbered:
                flags.append({"code": "object_only_in_translation", "where": num,
                              "detail": "%s in 源码 but on no PDF page; card does not "
                                        "say 未编号" % num})

        for ti, t in enumerate(c["theorems"]):
            src = t.get("source", "")
            m = PAGE_IN_SRC.search(src)
            if m:
                a = int(m.group(1))
                b = int(m.group(2)) if m.group(2) else a
                if not (set(range(a, b + 1)) & pset):
                    flags.append({"code": "theorem_src_pages",
                                  "where": "theorems[%d].source" % ti,
                                  "detail": "%r vs card pages %s"
                                            % (src, sorted(pset))})
        out.append({"id": c["id"], "path": rel, "flags": flags})

    with open(os.path.join(ROOT, "tmp", "mech.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    cnt = {}
    for c in out:
        for fl in c["flags"]:
            cnt[fl["code"]] = cnt.get(fl["code"], 0) + 1
    print("cards:", len(out), "| cards with flags:",
          sum(1 for c in out if c["flags"]), "| flag kinds:", len(cnt))
    print("flag counts:", json.dumps(cnt, ensure_ascii=False, sort_keys=True))
    for code in sorted(cnt):
        hits = [(c["id"], f) for c in out for f in c["flags"] if f["code"] == code]
        print("\n## %s (%d)" % (code, len(hits)))
        for cid, f in hits[:26]:
            print("  %-44s %-18s %s" % (cid.replace("glc/concept/", ""),
                                        f["where"], f["detail"][:108]))
        if len(hits) > 26:
            print("  ... %d more" % (len(hits) - 26))


if __name__ == "__main__":
    main()
