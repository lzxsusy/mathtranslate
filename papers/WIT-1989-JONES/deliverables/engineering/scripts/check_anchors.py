#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验研讨班 claims/questions 里引用的公式编号确实存在。

做法：从 Witten 中译本的合并源码 deliver/witten.tex 里收集所有 \\tag{...}，
再扫描 sessions/*/claims.jsonl 与 *.md 里出现的 [eq x.y] 与 (x.y)，
检查每个被引用的编号是否在 tag 集合里。页码类锚点由 check_claims.py 负责。

用法：
    python check_anchors.py <project_root> --tex <witten.tex>

注意：句子里的普通括号编号（如“第 (3.4) 式”）也被检查，因此若某个编号是
外部教材的（河野/上野），请写成 [河野 p.N] 而不是 (x.y)，否则会多报。
退出码：0 通过；1 有错。
"""
import json
import re
import sys
from pathlib import Path

TAG_RE = re.compile(r"\\tag\{([^}]+)\}")
EQ_REF_RE = re.compile(r"\[eq\s+([0-9]+(?:\.[0-9]+)*)\]")
PAREN_REF_RE = re.compile(r"\(([0-9]+\.[0-9]+)\)")


def collect_tags(tex_path: Path):
    text = tex_path.read_text(encoding="utf-8", errors="replace")
    return set(TAG_RE.findall(text))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--tex" in sys.argv:
        tex = Path(sys.argv[sys.argv.index("--tex") + 1])
    else:
        tex = None
    root = Path(args[0]) if args else Path(".")
    if tex is None or not tex.exists():
        print("ERROR 需要 --tex 指向 witten1989/deliver/witten.tex")
        return 1

    tags = collect_tags(tex)
    if not tags:
        print(f"ERROR 没从 {tex} 收集到任何 \\tag，路径或格式不对")
        return 1
    print(f"源码公式标签 {len(tags)} 个（例：{', '.join(sorted(tags)[:6])} …）")

    errors = []
    checked = 0
    for claims in sorted((root / "sessions").glob("s*/claims.jsonl")):
        for lineno, line in enumerate(claims.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            refs = set()
            for a in obj.get("anchors", []):
                # 只核原文锚点；[后世 ...] / [译注 ...] / 教材页码里的编号不属于本文
                if a.startswith(("[src", "[原文")):
                    refs.update(EQ_REF_RE.findall(a))
                    refs.update(PAREN_REF_RE.findall(a))
            for r in refs:
                checked += 1
                if r not in tags:
                    errors.append(f"{claims.name}:{lineno} {obj['id']} 引用 ({r})，源码无此 tag")

    # 也检查 markdown 报告里的 [eq x.y]
    for md in sorted((root / "sessions").glob("s*/*.md")):
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            for r in EQ_REF_RE.findall(line):
                checked += 1
                if r not in tags:
                    errors.append(f"{md.name}:{lineno} 引用 [eq {r}]，源码无此 tag")

    print(f"检查公式引用 {checked} 处")
    if errors:
        for e in errors:
            print(f"ERROR {e}")
        print(f"失败：{len(errors)} 个错误")
        return 1
    print("通过：0 个错误")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
