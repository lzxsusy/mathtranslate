# -*- coding: utf-8 -*-
r"""build_manifest.py —— 从 git 对象重建 MANIFEST.json。

做法与 `check_manifest.py` 对齐：按 blob 流式读内容，记字节数与 sha256 前 16 位
（**不是** git 对象 id）。MANIFEST.json 自身不计入清单。

用法：
    python tools/build_manifest.py              # 用 HEAD 的内容重建
    python tools/build_manifest.py --rev HEAD
"""
from __future__ import annotations

import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> int:
    rev = "HEAD"
    if "--rev" in sys.argv:
        rev = sys.argv[sys.argv.index("--rev") + 1]
    head = subprocess.check_output(["git", "rev-parse", rev], cwd=REPO).decode().strip()
    tracked = subprocess.check_output(
        ["git", "-c", "core.quotepath=false", "ls-tree", "-r", "--name-only", rev], cwd=REPO
    ).decode("utf-8", "replace").splitlines()
    paths = sorted(p for p in tracked if p != "MANIFEST.json")

    spec_file = tempfile.NamedTemporaryFile("w", suffix=".specs", delete=False, encoding="utf-8")
    spec_file.write("\n".join("%s:%s" % (rev, p) for p in paths) + "\n")
    spec_file.close()
    proc = subprocess.Popen(
        ["git", "cat-file", "--batch"], cwd=REPO,
        stdin=open(spec_file.name, "rb"), stdout=subprocess.PIPE,
    )
    entries = []
    total = 0
    for path in paths:
        header = proc.stdout.readline().decode().rstrip("\n")
        if not header or header.endswith("missing") or " " not in header:
            print(f"[warn] missing {path}")
            continue
        _sha, _typ, size = header.rsplit(" ", 2)
        size = int(size)
        remaining, h = size, hashlib.sha256()
        while remaining:
            chunk = proc.stdout.read(min(1 << 20, remaining))
            if not chunk:
                break
            h.update(chunk)
            remaining -= len(chunk)
        proc.stdout.read(1)
        entries.append({"path": path, "bytes": size, "sha256_16": h.hexdigest()[:16]})
        total += size
    try:
        proc.wait()
    except Exception:
        pass
    try:
        os.unlink(spec_file.name)
    except OSError:
        pass

    man = {"rev": head, "file_count": len(entries), "total_bytes": total, "files": entries}
    with io.open(os.path.join(REPO, "MANIFEST.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(man, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"manifest: rev={head[:8]} files={len(entries)} bytes={total:,}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
