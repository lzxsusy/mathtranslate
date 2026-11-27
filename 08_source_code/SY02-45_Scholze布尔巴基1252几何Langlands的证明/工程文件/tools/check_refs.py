# -*- coding: utf-8 -*-
"""从 s13-refs.tex 抽参考文献为 refs.tsv，并逐条外核（arXiv API / Crossref）。

用法：
  python check_refs.py extract   # 生成 refs.tsv
  python check_refs.py verify    # 逐条核对，输出 refs-check.tsv
"""
import re
import json
import sys
import time
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
TEX = BASE / "源码" / "sections" / "s13-refs.tex"
OUT = BASE / "工程文件" / "work" / "refs.tsv"
CHECK = BASE / "工程文件" / "work" / "refs-check.tsv"

UA = {"User-Agent": "SY02-45-refcheck/1.0 (mailto:lzx@example.org)"}


def extract():
    text = TEX.read_text(encoding="utf-8").replace("\r\n", "\n")
    items = re.findall(r"\\item\s+(.*?)(?=\n\\item\s|\n\\end\{list\})", text, re.S)
    rows = []
    for i, body in enumerate(items, 1):
        body = " ".join(body.split())
        # 作者与年份
        m = re.match(r"(.*?)\s*\((\d{4}[a-c]?)\)\.\s*(.*)$", body, re.S)
        if m:
            authors, year, rest = m.group(1), m.group(2), m.group(3)
        else:
            authors, year, rest = "", "", body
        m2 = re.search(r"arXiv:\s*([0-9]{4}\.[0-9]{4,5})(v\d+)?", rest)
        arxiv = m2.group(1) if m2 else ""
        m3 = re.search(
            r"\\textit\{(.*?)\}\s*\\textbf\{(\d+)\}\s*(?:\((\d+(?:[-\u2013]\d+)?)\))?,?\s*pp\.\s*([0-9\u2013\-]+)",
            rest,
        )
        if m3:
            venue, vol, issue, pages = m3.group(1), m3.group(2), m3.group(3) or "", m3.group(4)
        else:
            venue = vol = issue = pages = ""
        t = re.search(r"\u201c(.+?)\u201d", rest)
        if t:
            title = t.group(1)
        else:
            t = re.search(r"\\textit\{(.+?)\}", rest)
            title = t.group(1) if t else ""
        title = title.replace("{", "").replace("}", "")
        rows.append([str(i), authors.strip(), year, title, venue, vol, issue, pages, arxiv, body])
    OUT.write_text(
        "序号\t作者\t年份\t标题\t期刊/丛书\t卷\t期\t页\tarXiv\t原文条目\n"
        + "\n".join("\t".join(r) for r in rows),
        encoding="utf-8",
    )
    print(f"抽取 {len(rows)} 条 → {OUT}")
    return rows


def get(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as f:
        return f.read().decode("utf-8", "replace")


def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def verify():
    rows = [l.split("\t") for l in OUT.read_text(encoding="utf-8").splitlines()[1:]]
    out = ["序号\t类型\t核验\t说明"]
    for r in rows:
        idx, authors, year, title, venue, vol, issue, pages, arxiv = r[:9]
        if arxiv:
            try:
                xml = get(f"http://export.arxiv.org/api/query?id_list={arxiv}")
                mt = re.search(r"<entry>.*?<title>(.*?)</title>", xml, re.S)
                md = re.search(r"<published>(\d{4})", xml, re.S)
                if not mt:
                    out.append(f"{idx}\tarXiv\tMISS\t{arxiv} 查询无结果")
                else:
                    real = " ".join(mt.group(1).split())
                    same = norm(real)[:40] == norm(title)[:40] or norm(title)[:40] in norm(real)
                    yr = md.group(1) if md else "?"
                    out.append(
                        f"{idx}\tarXiv\t{'OK' if same else 'CHECK'}\t{arxiv} → {real[:90]} ({yr}; 原 {year})"
                    )
            except Exception as e:
                out.append(f"{idx}\tarXiv\tERR\t{arxiv} {type(e).__name__}: {e}")
            time.sleep(1.0)
        elif venue:
            q = urllib.parse.quote(f"{title} {authors.split(',')[0]} {venue}")
            try:
                js = json.loads(get(f"https://api.crossref.org/works?query.bibliographic={q}&rows=3"))
                best = None
                for it in js["message"]["items"]:
                    t = (it.get("title") or [""])[0]
                    if norm(t)[:35] == norm(title)[:35]:
                        best = it
                        break
                if best is None:
                    out.append(f"{idx}\tCrossref\tMISS\t{title[:60]} 未匹配到同题记录")
                else:
                    cv = best.get("volume", "")
                    cp = best.get("page", "")
                    cj = (best.get("container-title") or [""])[0]
                    ok = (not vol or cv == vol) and (not pages or cp.replace("-", "–") == pages.replace("-", "–"))
                    out.append(
                        f"{idx}\tCrossref\t{'OK' if ok else 'DIFF'}\t{title[:50]} | 卷 {vol}→{cv} 页 {pages}→{cp} 刊 {cj[:40]}"
                    )
            except Exception as e:
                out.append(f"{idx}\tCrossref\tERR\t{type(e).__name__}: {e}")
            time.sleep(1.0)
        else:
            out.append(f"{idx}\t-\tSKIP\t无 arXiv/期刊信息（书或讲义）")
    CHECK.write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "extract":
        extract()
    else:
        if not OUT.exists():
            extract()
        verify()
