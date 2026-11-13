# -*- coding: utf-8 -*-
r"""校验 MANIFEST.json 与仓库真实内容是否一致（快速版）。

做法：单进程 `git cat-file --batch` 流式读 blob，逐条复算字节数与 sha256 前 16 位。
不依赖工作树换行状态——清单按 blob 生成，校验也按 blob，二者必然可比。

用法：
    python tools/check_manifest.py            # 校验 HEAD
    python tools/check_manifest.py --rev HEAD
"""
from __future__ import annotations

import hashlib
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> int:
    rev = "HEAD"
    if "--rev" in sys.argv:
        rev = sys.argv[sys.argv.index("--rev") + 1]

    with io.open(os.path.join(REPO, "MANIFEST.json"), encoding="utf-8") as f:
        man = json.load(f)
    want = {e["path"]: (e["bytes"], e["sha256_16"]) for e in man["files"]}

    tracked = subprocess.check_output(
        ["git", "-c", "core.quotepath=false", "ls-tree", "-r", "--name-only", rev], cwd=REPO
    ).decode("utf-8").splitlines()
    tracked = [p for p in tracked if p.startswith("git:" ) is False]
    tracked_set = set(tracked)

    specs = ["%s:%s" % (rev, p) for p in sorted(want)]
    # 用临时文件喂 stdin：直接往 PIPE 写 6k+ 行会把 git 的 stdout 管道堵死（互相等待）
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".specs", delete=False, encoding="utf-8") as tf:
        tf.write("\n".join(specs) + "\n")
        spec_file = tf.name
    proc = subprocess.Popen(
        ["git", "cat-file", "--batch"],
        cwd=REPO, stdin=open(spec_file, "rb"), stdout=subprocess.PIPE,
    )

    bad = missing = 0
    samples = []
    for path in sorted(want):
        header = proc.stdout.readline().decode().rstrip("\n")
        if not header or header.endswith("missing") or " " not in header:
            missing += 1
            if len(samples) < 5:
                samples.append(("missing", path))
            continue
        _sha, _typ, size = header.rsplit(" ", 2)
        size = int(size)
        remaining = size
        h = hashlib.sha256()
        while remaining:
            chunk = proc.stdout.read(min(1 << 20, remaining))
            if not chunk:
                break
            h.update(chunk)
            remaining -= len(chunk)
        proc.stdout.read(1)  # 尾部换行
        want_size, want_hash = want[path]
        if size != want_size or h.hexdigest()[:16] != want_hash:
            bad += 1
            if len(samples) < 5:
                samples.append(("diff", path))
    try:
        proc.wait()
    except Exception:
        pass
    try:
        os.unlink(spec_file)
    except OSError:
        pass

    extra = [p for p in tracked_set
             if p not in want and p not in ("MANIFEST.json", "_build_summary.json")]

    print("rev=%s listed=%d mismatch=%d missing=%d unlisted=%d" %
          (rev, len(want), bad, missing, len(extra)))
    for kind, p in samples:
        print("  -", kind, p)
    for p in extra[:5]:
        print("  - unlisted", p)
    ok = (bad == 0 and missing == 0 and not extra)
    print("RESULT:", "OK" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
