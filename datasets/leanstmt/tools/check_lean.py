# -*- coding: utf-8 -*-
"""检查 leanstmt 的 Lean 侧：声明存在、import 可解析、sorry 计数，并可选真跑 Lean。

用法：
  python tools/check_lean.py                          # 静态检查（不需要 Lean）
  python tools/check_lean.py --project ..\\formal      # 真跑 lake env lean（需要 elan/lake）
  python tools/check_lean.py --project <路径> --run --write-verification

产物：verification.jsonl（一行一卡：id / file / exit / sorry_count / status / checked_at）。
"""
from __future__ import annotations

import argparse
import datetime
import glob
import io
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORRY_RE = re.compile(r"\bsorry\b")
COMMENT_RE = re.compile(r"/-.*?-/|--[^\n]*", re.S)


def strip_comments(text: str) -> str:
    """粗略剥掉 Lean 注释（块注释按最短配对，够用）。"""
    return COMMENT_RE.sub(" ", text)


def cards() -> list[dict]:
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "cards", "**", "*.json"), recursive=True)):
        out.append(json.load(io.open(p, encoding="utf-8")))
    return out


def lean_files() -> list[str]:
    base = os.path.join(ROOT, "lean")
    return sorted(glob.glob(os.path.join(base, "**", "*.lean"), recursive=True))


def static_check() -> int:
    bad = 0
    files = {os.path.relpath(p, ROOT).replace("\\", "/"): io.open(p, encoding="utf-8").read()
             for p in lean_files()}
    for c in cards():
        f = c["lean"]["file"]
        if f not in files:
            print(f"ERROR {c['id']}: 缺 Lean 文件 {f}")
            bad += 1
            continue
        text = files[f]
        short = c["lean"]["name"].rsplit(".", 1)[-1]
        if not re.search(r"(?:theorem|lemma|def)\s+" + re.escape(short) + r"\b", text):
            print(f"ERROR {c['id']}: {f} 里找不到声明 {short}")
            bad += 1
        for imp in c["lean"]["imports"]:
            if not imp.startswith("Mathlib.") and not imp.startswith("ShuyiFormal"):
                print(f"ERROR {c['id']}: import 看着不像 mathlib/本项目模块：{imp}")
                bad += 1
    print(f"static: {len(cards())} cards / {len(files)} lean files, {bad} problem(s)")
    return bad


def run_lean(project: str, write: bool) -> int:
    # 找 lake：优先 elan 的 shim
    lake = None
    for cand in (os.path.expanduser("~/.elan/bin/lake.exe"),
                 os.path.expanduser("~/.elan/bin/lake"),
                 shutil.which("lake")):
        if cand and os.path.isfile(cand):
            lake = cand
            break
    if lake is None:
        print("ERROR 找不到 lake（需要 elan）；跳过 --run")
        return 1
    rel_files = sorted({c["lean"]["file"] for c in cards()})
    results = {}
    for rel in rel_files:
        # lean 文件相对包根是 lean/xxx，相对工程根要去掉 lean/ 前缀
        proj_rel = rel.split("lean/", 1)[-1]
        path = os.path.join(project, proj_rel.replace("/", os.sep))
        if not os.path.isfile(path):
            print(f"ERROR 工程里没有 {proj_rel}（先同步 lean/ 快照到工程）")
            return 1
        cmd = [lake, "env", "lean", proj_rel.replace("/", os.sep)]
        print(f"$ {' '.join(cmd)}")
        r = subprocess.run(cmd, cwd=project, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        out = (r.stdout or "") + (r.stderr or "")
        n_sorry = len(SORRY_RE.findall(strip_comments(io.open(path, encoding="utf-8").read())))
        results[proj_rel] = dict(exit=r.returncode, sorry=n_sorry,
                                 errors=[l for l in out.splitlines() if "error" in l][:5])
        print(f"  exit={r.returncode} file_sorry={n_sorry}")
    # 逐卡写 verification
    today = datetime.date.today().isoformat()
    rows = []
    bad = 0
    for c in cards():
        proj_rel = c["lean"]["file"].split("lean/", 1)[-1]
        res = results.get(proj_rel, dict(exit=99, sorry=0, errors=["not run"]))
        if res["exit"] != 0:
            print(f"ERROR {c['id']}: 编译失败：{res['errors']}")
            bad += 1
        elif res["sorry"] > 0 and c["verification"]["status"] != "gap":
            print(f"ERROR {c['id']}: 文件含 sorry 但卡是 certified")
            bad += 1
        rows.append(dict(id=c["id"], lean=c["lean"]["name"], file=c["lean"]["file"],
                         exit=res["exit"], file_sorry=res["sorry"],
                         card_status=c["verification"]["status"],
                         lean_version=c["verification"]["lean_version"],
                         mathlib_rev=c["verification"]["mathlib_rev"],
                         checked_at=today))
    if write:
        out = os.path.join(ROOT, "verification.jsonl")
        with io.open(out, "w", encoding="utf-8", newline="\n") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"wrote {out} rows={len(rows)}")
    print("OK" if not bad else "FAIL")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default=None, help="lake 工程根（含 lakefile.lean）")
    ap.add_argument("--run", action="store_true", help="真的调用 lake env lean")
    ap.add_argument("--write-verification", action="store_true")
    args = ap.parse_args()
    bad = static_check()
    if args.run:
        if not args.project:
            print("ERROR --run 需要 --project")
            return 1
        bad += run_lean(args.project, args.write_verification)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
