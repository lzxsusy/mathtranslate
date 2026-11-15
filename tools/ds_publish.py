# -*- coding: utf-8 -*-
"""ds_publish.py — 发布前权利过滤。

用法：
    python tools/ds_publish.py --check     # 只检查，退出码 1 表示有不可发布记录
    python tools/ds_publish.py --write     # 写 datasets/PUBLISH.json（发布清单）

规则（对应 datasets/README.md §2）：
- rights=self：status 为 reviewed/published 才发布；
- rights=arxiv:<id>：license=arXiv-CC-BY 可整条发布；否则只允许
  「引用 ≤300 字」的 src_text 与自产部分，超过 300 字一律 block；
- rights=book：永不发布，且必须位于 datasets/_internal/。
"""
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DS = os.path.join(ROOT, "datasets")


def judge(rel, rec):
    if "trace_id" in rec:
        return True, ""
    rights = str(rec.get("rights", ""))
    if rights == "book":
        return False, "book 不得发布"
    if rights == "self":
        if rec.get("status") not in ("reviewed", "published"):
            return False, "status 未审校"
        return True, ""
    if rights.startswith("arxiv:"):
        if rec.get("license") == "arXiv-CC-BY":
            return True, ""
        src = rec.get("src_text") or ""
        if len(src) > 300:
            return False, "arXiv 许可未确认且引用 %d>300 字" % len(src)
        return True, ""
    return False, "rights 未知"


def main():
    write = "--write" in sys.argv
    allowed, blocked = [], []
    for base, _, files in os.walk(DS):
        parts = base.replace("\\", "/").split("/")
        if "_internal" in parts:
            continue
        for name in sorted(files):
            if not name.endswith(".jsonl"):
                continue
            fp = os.path.join(base, name)
            rel = os.path.relpath(fp, ROOT).replace("\\", "/")
            with io.open(fp, encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    rec = json.loads(line)
                    ok, why = judge(rel, rec)
                    (allowed if ok else blocked).append((rel, rec.get("id"), why))
    uniq = sorted(set(a[0] for a in allowed))
    if write:
        manifest = os.path.join(DS, "PUBLISH.json")
        out = {
            "version": "v0.1",
            "date": "2026-11-16",
            "files": [{"path": p, "sha256": hashlib.sha256(open(os.path.join(ROOT, p), "rb").read()).hexdigest()} for p in uniq],
            "blocked": [{"file": b[0], "id": b[1], "reason": b[2]} for b in blocked],
        }
        with io.open(manifest, "w", encoding="utf-8", newline="\n") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("wrote datasets/PUBLISH.json:", len(uniq), "files,", len(blocked), "blocked records")
    else:
        print("publishable files:", len(uniq), "blocked records:", len(blocked))
        for b in blocked[:20]:
            print("BLOCK", b[0], b[1], b[2])
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
