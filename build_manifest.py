# -*- coding: utf-8 -*-
r"""按**仓库里真实存在的 blob** 重建 MANIFEST.json 与 _build_summary.json。

为什么要从 git 对象读而不是从工作树读：
  `.gitattributes` 固定 `text=auto eol=lf` 后，工作树里可能是 CRLF，而仓库里存的是 LF。
  早期清单是从工作树生成的，提交后集体失配（反馈里那句「40% 字节数不符」就是这个）。
  现在一律以 `HEAD:<path>` 的 blob 为准，清单与仓库内容必然一致。

实现用单进程 `git cat-file --batch` 流式读，6818 个文件约 10 秒；早期逐文件起进程要十几分钟。

用法（在仓库根目录，且工作树已提交干净）：
    python build_manifest.py
    python build_manifest.py --rev HEAD
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
REPO = os.path.dirname(os.path.abspath(__file__))
SKIP = {"MANIFEST.json", "_build_summary.json"}


def main():
    rev = "HEAD"
    if "--rev" in sys.argv:
        rev = sys.argv[sys.argv.index("--rev") + 1]

    names = [n for n in subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", rev], cwd=REPO
    ).decode("utf-8").splitlines() if n and n not in SKIP]

    specs = ["%s:%s" % (rev, n) for n in names]
    with tempfile.NamedTemporaryFile("w", suffix=".specs", delete=False, encoding="utf-8") as tf:
        tf.write("\n".join(specs) + "\n")
        spec_file = tf.name

    proc = subprocess.Popen(
        ["git", "cat-file", "--batch"],
        cwd=REPO, stdin=open(spec_file, "rb"), stdout=subprocess.PIPE,
    )
    entries = []
    total = 0
    for name in names:
        header = proc.stdout.readline().decode().rstrip("\n")
        if not header or header.endswith("missing"):
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
        proc.stdout.read(1)
        entries.append({"path": name, "bytes": size, "sha256_16": h.hexdigest()[:16]})
        total += size
    proc.wait()
    try:
        os.unlink(spec_file)
    except OSError:
        pass

    manifest = {"rev": rev, "file_count": len(entries), "total_bytes": total, "files": entries}
    with io.open(os.path.join(REPO, "MANIFEST.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)

    summary = {
        "manifest_rev": rev,
        "manifest_files": len(entries),
        "total_bytes": total,
        "total_mb": round(total / 1048576.0, 1),
        "generated_by": "build_manifest.py",
    }
    with io.open(os.path.join(REPO, "_build_summary.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)

    print("rev=%s files=%d total=%.1f MB" % (rev, len(entries), total / 1048576.0))


if __name__ == "__main__":
    main()
