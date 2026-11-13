# -*- coding: utf-8 -*-
r"""发布前脱敏（JSON 感知版）。

为什么要有 JSON 感知：早期版本直接在 .jsonl 的**原始字节**上跑正则，替换文本里带反斜杠时
会把合法 JSON 变成非法（例如把公式 `\\phi_{0}\\\\` 前后拼出 `\<本地路径>`），导致整行解析失败。
现在对 .jsonl 逐行 json.loads -> 递归清洗字符串值 -> json.dumps，绝不动 JSON 结构。

用法：
    python tools/scrub_publish.py            # 只统计（dry-run）
    python tools/scrub_publish.py --write    # 就地改写
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATTERNS = [
    (re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"), "[已脱敏]"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{20,}"), "[已脱敏]"),
    (re.compile(r"sk-[A-Za-z0-9\-_]{20,}"), "[已脱敏]"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "[已脱敏]"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "[已脱敏]"),
    (re.compile(r"ssh-ed25519 AAAA[A-Za-z0-9+/=]+"), "[已脱敏]"),
    (re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}"), "[邮箱隐去]"),
    (re.compile(r"(?i)\b[A-Za-z]:[\\/]+Users[\\/][^\s\"'<>|]*"), "<本地路径>"),
    (re.compile(r"\\\\[A-Za-z0-9._\-]+\\[^\s\"'<>|]*"), "<本地路径>"),
]

TEXT_EXT = {".md", ".txt", ".tsv", ".csv", ".tex", ".json", ".jsonl", ".yaml", ".yml",
            ".py", ".ps1", ".js", ".html", ".css", ".gitignore", ".gitattributes", ""}
SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def scrub_text(s: str) -> tuple[str, int]:
    hits = 0
    for rx, rep in PATTERNS:
        s, n = rx.subn(rep, s)
        hits += n
    return s, hits


def scrub_obj(o, counter) -> object:
    if isinstance(o, str):
        return scrub_text(o)[0] if scrub_text(o)[1] else o
    if isinstance(o, list):
        return [scrub_obj(x, counter) for x in o]
    if isinstance(o, dict):
        return {k: scrub_obj(v, counter) for k, v in o.items()}
    return o


def process(path: str, write: bool) -> tuple[int, int]:
    """返回 (替换处数, 是否改动文件)。"""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".jsonl":
        out = []
        hits = 0
        changed = False
        with io.open(path, encoding="utf-8") as f:
            for line in f:
                s = line.rstrip("\n")
                if not s.strip():
                    continue
                obj = json.loads(s)          # 源数据必须合法；坏行直接抛错暴露
                new, n = scrub_text(s)
                if n:
                    changed = True
                    hits += n
                    # 只信任结构化重写：先清洗值再统一序列化
                    obj = scrub_obj(obj, None)
                    new = json.dumps(obj, ensure_ascii=False)
                out.append(new)
        if write and changed:
            with io.open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write("\n".join(out) + "\n")
        return hits, changed

    with io.open(path, encoding="utf-8", errors="ignore") as f:
        s = f.read()
    new, hits = scrub_text(s)
    if write and hits:
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)
    return hits, bool(hits)


def main():
    write = "--write" in sys.argv
    total_hits = 0
    touched = 0
    for dp, dn, fn in os.walk(REPO):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for name in fn:
            ext = os.path.splitext(name)[1].lower()
            if ext not in TEXT_EXT:
                continue
            p = os.path.join(dp, name)
            try:
                hits, changed = process(p, write)
            except UnicodeDecodeError:
                continue
            except json.JSONDecodeError as e:
                print("[跳过-非法JSON] %s :: %s" % (os.path.relpath(p, REPO), e))
                continue
            total_hits += hits
            if changed:
                touched += 1
    print("files_touched=%d replacements=%d write=%s" % (touched, total_hits, write))


if __name__ == "__main__":
    main()
