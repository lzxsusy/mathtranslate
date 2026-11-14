# -*- coding: utf-8 -*-
"""D0：从 LaTeX 源码建「结构索引」（节点 + 引用边），零 LLM。

只做确定性抽取：
  - 识别 amsthm / \newtheorem 定义的环境（含自定义名），建立 env -> kind 映射；
  - 扫描所有 .tex（跳过 preamble/main/_check 等），按花括号配对切出环境体；
  - 每个环境一条 node（label 优先，无 label 用文件+行号生成临时 ID）；
  - 节点体内（及紧随的 proof）的 \\ref/\\eqref/... 生成 uses 边；
  - 正文段落里的 ref 生成 mentions 边（confidence 0.5，仅作为线索）；
  - 兼容 SY01-23 的 \\BookRef/\\BookEqRef/\\BookSectionRef/\\BookChapterRef 宏；
  - 输出 nodes.jsonl / edges.jsonl / SUMMARY.md。

这不是最终标注：node 只是 L1 骨架（没有 difficulty/role），edge 的 method=rule、status=proposed。
用法：
  python build_structure_index.py --root "<项目>/源码" --paper-id SY07-08 --out index
"""
from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

KIND_BY_TITLE = {
    "定理": "theorem", "Theorem": "theorem",
    "引理": "lemma", "Lemma": "lemma",
    "命题": "proposition", "Proposition": "proposition",
    "推论": "corollary", "Corollary": "corollary",
    "定义": "definition", "Definition": "definition",
    "例": "example", "Example": "example",
    "注": "remark", "Remark": "remark", "注意": "remark",
    "构造": "construction", "Construction": "construction",
    "猜想": "conjecture", "Conjecture": "conjecture",
    "断言": "claim", "Claim": "claim",
    "问题": "question", "Question": "question",
    "假设": "assumption", "Assumption": "assumption",
    "记号": "notation", "Notation": "notation",
    "习题": "exercise", "Exercise": "exercise",
    "条目": "item", "结果": "result", "陈述": "statement",
    "约定": "convention", "背景": "background",
}

DEFAULT_ENVS = {
    "theorem": "theorem", "thm": "theorem",
    "lemma": "lemma", "lem": "lemma", "lmm": "lemma",
    "proposition": "proposition", "prop": "proposition", "propn": "proposition", "prp": "proposition",
    "corollary": "corollary", "cor": "corollary", "crl": "corollary",
    "definition": "definition", "defn": "definition", "dfn": "definition", "def": "definition",
    "example": "example", "examples": "example", "exmp": "example",
    "remark": "remark", "rem": "remark", "rmk": "remark", "remarks": "remark",
    "construction": "construction",
    "conjecture": "conjecture", "conj": "conjecture", "cnv": "convention",
    "claim": "claim", "question": "question", "ques": "question",
    "problem": "problem", "assumption": "assumption",
    "note": "remark", "letteraxiom": "assumption",
    "notation": "notation", "nota": "notation",
    "exercise": "exercise", "exer": "exercise",
    "result": "result", "statement": "statement",
    "convention": "convention", "background": "background", "item": "item",
    "proof": "proof", "proof*": "proof",
}

NON_NODE_KINDS = {"proof", "item"}
EXCLUDE_NAMES = {
    "preamble.tex", "refs.tex", "main.tex", "translator_note.tex",
    "index-zh.tex", "figure-dimensions.tex",
}
EXCLUDE_PREFIX = ("_",)

RE_NEWTHM = re.compile(
    r"\\newtheorem\*?\{([^}]+)\}(?:\[([^\]]*)\])?\{([^}]*)\}(?:\[([^\]]*)\])?"
)
TOKEN_RE = re.compile(r"\\(begin|end)\{([^}]+)\}")
HEAD_RE = re.compile(r"\\(chapter|section|subsection|subsubsection)\*?\{([^}]*)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
STD_REF_RE = re.compile(r"\\(?:ref|eqref|autoref|cref|Cref|pageref)\{([^}]+)\}")
BOOK_REF_RE = re.compile(r"\\Book(?:Eq|Section)?Ref\{([^}]+)\}\{[^}]*\}")
BOOK_CHAP_RE = re.compile(r"\\BookChapterRef\{([^}]+)\}")


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def strip_comment(line: str) -> str:
    out = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            out.append(line[i:i + 2])
            i += 2
            continue
        if c == "%":
            break
        out.append(c)
        i += 1
    return "".join(out)


def env_kind_map(root: str) -> dict[str, str]:
    mapping = dict(DEFAULT_ENVS)
    for dirpath, _dirs, files in os.walk(root):
        for name in files:
            if not (name.startswith("preamble") and name.endswith(".tex")):
                continue
            text = read_text(os.path.join(dirpath, name))
            for env, _share, title, _sec in RE_NEWTHM.findall(text):
                kind = KIND_BY_TITLE.get(title.strip())
                if kind:
                    mapping[env.strip()] = kind
    return mapping


def iter_tex_files(root: str) -> list[str]:
    out = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in files:
            if not name.endswith(".tex"):
                continue
            if name in EXCLUDE_NAMES or name.startswith(EXCLUDE_PREFIX):
                continue
            path = os.path.join(dirpath, name)
            try:
                if os.path.getsize(path) > 4 * 1024 * 1024:
                    continue
            except OSError:
                continue
            out.append(path)
    return sorted(out)


def find_envs(text: str):
    """返回 [(env, body_start, body_end, begin_pos)]，按出现顺序。"""
    stack: list[tuple[str, int]] = []
    recs = []
    for m in TOKEN_RE.finditer(text):
        typ, env = m.group(1), m.group(2).strip()
        if typ == "begin":
            stack.append((env, m.end()))
        else:
            for i in range(len(stack) - 1, -1, -1):
                if stack[i][0] == env:
                    _, start = stack[i]
                    del stack[i:]
                    recs.append((env, start, m.start(), m.start()))
                    break
    recs.sort(key=lambda r: r[1])
    return recs


def line_index(text: str):
    return [0] + [m.end() for m in re.finditer(r"\n", text)]


def line_of(starts: list[int], pos: int) -> int:
    return bisect.bisect_right(starts, pos)


def optional_title(text: str, pos: int) -> str:
    if pos < len(text) and text[pos] == "[":
        depth = 0
        for i in range(pos, min(len(text), pos + 300)):
            if text[i] == "[":
                depth += 1
            elif text[i] == "]":
                depth -= 1
                if depth == 0:
                    return text[pos + 1:i].strip()
    return ""


def iter_refs(text: str):
    """yield (target, pos, kind) —— kind = std | book | chap。"""
    for m in STD_REF_RE.finditer(text):
        for t in m.group(1).split(","):
            t = t.strip()
            if t:
                yield t, m.start(), "std"
    for m in BOOK_REF_RE.finditer(text):
        yield m.group(1).strip(), m.start(), "book"
    for m in BOOK_CHAP_RE.finditer(text):
        yield f"chap:{m.group(1).strip()}", m.start(), "chap"


def pagerank(nodes: list[dict], edges: list[dict], iters: int = 30, d: float = 0.85) -> dict[str, float]:
    ids = [n["node_id"] for n in nodes]
    if not ids:
        return {}
    n = len(ids)
    out = defaultdict(list)
    for e in edges:
        out[e["src"]].append(e["dst"])
    pr = {i: 1.0 / n for i in ids}
    for _ in range(iters):
        nxt = {i: (1.0 - d) / n for i in ids}
        for i in ids:
            targets = out.get(i) or []
            if not targets:
                share = pr[i] / n
                for j in ids:
                    nxt[j] += d * share
            else:
                share = pr[i] / len(targets)
                for j in targets:
                    if j in nxt:
                        nxt[j] += d * share
        pr = nxt
    return pr


def make_edge(src: str, dst: str, rel: str, quote: str, rel_file: str, rel_line: int,
              context: str, confidence: float) -> dict:
    return {
        "src": src, "dst": dst, "rel": rel, "method": "rule",
        "confidence": confidence, "status": "proposed",
        "evidence": {"quote": quote, "tex_file": rel_file, "tex_line": rel_line, "context": context},
    }


def build(root: str, paper_id: str, out_dir: str) -> dict:
    mapping = env_kind_map(root)
    files = iter_tex_files(root)
    nodes: list[dict] = []
    edges: list[dict] = []
    env_counter = Counter()
    unmapped = Counter()
    label_to_node: dict[str, str] = {}
    duplicate_labels = 0
    unresolved = Counter()
    refs_total = 0
    mention_count = 0

    for path in files:
        rel = os.path.relpath(path, root).replace("\\", "/")
        raw = read_text(path)
        text = "\n".join(strip_comment(line) for line in raw.split("\n"))
        lines = text.split("\n")
        starts = line_index(text)
        recs = find_envs(text)

        spans: list[tuple[int, int, str]] = []   # 所有已识别节点的体范围（含 proof 归并）
        file_nodes: list[dict] = []
        pending_proof: dict | None = None

        # 章节标题节点：只用来解析 chap:/sec: 引用，不算「定理型节点」
        for hm in HEAD_RE.finditer(text):
            tail = text[hm.end():hm.end() + 240]
            lm = LABEL_RE.search(tail)
            if not lm:
                continue
            label = lm.group(1).strip()
            if label in label_to_node:
                continue
            start_line = line_of(starts, hm.start())
            node = {
                "node_id": f"{paper_id}:{label}",
                "paper_id": paper_id,
                "kind": hm.group(1),
                "env": hm.group(1),
                "label": label,
                "title": hm.group(2).strip(),
                "statement_zh": hm.group(2).strip(),
                "locator": {"tex_file": rel, "tex_lines": [start_line, start_line]},
                "body_sha1": "",
                "has_proof": False,
                "structural": True,
                "source": "tex",
            }
            nodes.append(node)
            file_nodes.append(node)
            label_to_node[label] = node["node_id"]

        for env, bstart, bend, _ in recs:
            env_counter[env] += 1
            kind = mapping.get(env)
            if kind is None and env.endswith("*"):
                kind = mapping.get(env[:-1])
            if kind is None:
                unmapped[env] += 1
                continue
            body = text[bstart:bend]
            if kind == "proof":
                target = pending_proof
                if target is None:
                    continue
                spans.append((bstart, bend, target["node_id"]))
                target["has_proof"] = True
                for t, pos, _k in iter_refs(body):
                    refs_total += 1
                    if t == target.get("label"):
                        continue
                    dst = label_to_node.get(t)
                    ln = line_of(starts, bstart + pos)
                    if dst is None:
                        unresolved[t] += 1
                        continue
                    edges.append(make_edge(target["node_id"], dst, "uses",
                                           lines[ln - 1].strip()[:200], rel, ln, "proof", 1.0))
                continue

            label_m = LABEL_RE.search(body)
            label = label_m.group(1).strip() if label_m else ""
            start_line = line_of(starts, bstart)
            end_line = line_of(starts, max(bstart, bend - 1))
            sha = hashlib.sha1(body.encode("utf-8")).hexdigest()[:16]
            node_id = f"{paper_id}:{label}" if label else f"{paper_id}:auto-{os.path.splitext(rel)[0].replace('/', '-')}-{start_line}"
            if label:
                if label in label_to_node:
                    duplicate_labels += 1
                    node_id = f"{paper_id}:{label}#{duplicate_labels}"
                else:
                    label_to_node[label] = node_id

            node = {
                "node_id": node_id,
                "paper_id": paper_id,
                "kind": kind,
                "env": env,
                "label": label,
                "title": optional_title(text, bstart),
                "statement_zh": "",
                "locator": {"tex_file": rel, "tex_lines": [start_line, end_line]},
                "body_sha1": sha,
                "has_proof": False,
                "source": "tex",
            }
            nodes.append(node)
            file_nodes.append(node)
            spans.append((bstart, bend, node_id))
            pending_proof = node

            for t, pos, _k in iter_refs(body):
                refs_total += 1
                if t == label:
                    continue
                dst = label_to_node.get(t)
                ln = line_of(starts, bstart + pos)
                if dst is None:
                    unresolved[t] += 1
                    continue
                edges.append(make_edge(node_id, dst, "uses",
                                       lines[ln - 1].strip()[:200], rel, ln, "statement", 1.0))

        file_nodes.sort(key=lambda n: n["locator"]["tex_lines"][0])

        # 正文 ref → mentions（不在任何已识别环境体内）
        def inside_span(pos: int) -> bool:
            for s, e, _ in spans:
                if s <= pos < e:
                    return True
            return False

        for t, pos, _k in iter_refs(text):
            if inside_span(pos):
                continue
            refs_total += 1
            dst = label_to_node.get(t)
            if dst is None:
                unresolved[t] += 1
                continue
            prev = None
            for n in file_nodes:
                n_start = starts[n["locator"]["tex_lines"][0] - 1] if n["locator"]["tex_lines"][0] - 1 < len(starts) else 0
                if n_start < pos:
                    prev = n
                else:
                    break
            if prev is None:
                continue
            ln = line_of(starts, pos)
            edges.append(make_edge(prev["node_id"], dst, "mentions",
                                   lines[ln - 1].strip()[:200], rel, ln, "prose", 0.5))
            mention_count += 1

    # 去重：同一 (src,dst) 优先保留 uses，其次 confidence 高者
    merged: dict[tuple[str, str], dict] = {}
    for e in edges:
        key = (e["src"], e["dst"])
        if key not in merged:
            merged[key] = e
            merged[key]["multiplicity"] = 1
            continue
        merged[key]["multiplicity"] += 1
        if e["confidence"] > merged[key]["confidence"]:
            keep_multi = merged[key]["multiplicity"]
            merged[key] = e
            merged[key]["multiplicity"] = keep_multi
    edges = list(merged.values())

    pr = pagerank(nodes, edges)
    indeg = Counter(e["dst"] for e in edges)
    outdeg = Counter(e["src"] for e in edges)
    for n in nodes:
        n["in_degree"] = indeg.get(n["node_id"], 0)
        n["out_degree"] = outdeg.get(n["node_id"], 0)
        n["pagerank"] = round(pr.get(n["node_id"], 0.0), 8)

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "nodes.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for n in nodes:
            f.write(json.dumps(n, ensure_ascii=False) + "\n")
    with open(os.path.join(out_dir, "edges.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for e in edges:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    labeled = [n for n in nodes if n["label"]]
    theorem_like = [n for n in labeled if not n.get("structural")]
    structural_n = sum(1 for n in nodes if n.get("structural"))
    top_pr = sorted(theorem_like, key=lambda n: n["pagerank"], reverse=True)[:15]
    top_in = sorted(theorem_like, key=lambda n: n["in_degree"], reverse=True)[:15]
    by_kind = Counter(n["kind"] for n in nodes)
    uses_n = sum(1 for e in edges if e["rel"] == "uses")
    mention_n = sum(1 for e in edges if e["rel"] == "mentions")

    lines = []
    lines.append(f"# 结构索引 · {paper_id}\n")
    lines.append("> 由 `tools/build_structure_index.py` 生成（D0，零 LLM，确定性抽取）。"
                 "nodes 只是骨架，不含 role/difficulty；edges 的 method=rule、status=proposed。"
                 "`uses`=节点内/证明内引用，`mentions`=正文提及（confidence 0.5，仅线索）。\n")
    lines.append("## 总览\n")
    lines.append("| 项 | 值 |")
    lines.append("|---|---|")
    lines.append(f"| 扫描 .tex 文件 | {len(files)} |")
    lines.append(f"| 环境实例（全部） | {sum(env_counter.values())} |")
    lines.append(f"| 已识别为节点 | {len(nodes)}（定理型 {len(nodes)-structural_n}，章/节结构 {structural_n}；带 label {len(labeled)}） |")
    lines.append(f"| 类型分布 | " + "、".join(f"{k} {v}" for k, v in by_kind.most_common()) + " |")
    lines.append(f"| 引用总数 | {refs_total} |")
    lines.append(f"| 去重后边 | {len(edges)}（uses {uses_n} / mentions {mention_n}） |")
    lines.append(f"| 正文 mention 条数 | {mention_count} |")
    lines.append(f"| 解析失败引用 | {sum(unresolved.values())}（目标去重 {len(unresolved)}） |")
    lines.append(f"| 重复 label | {duplicate_labels} |")
    lines.append(f"| 带 proof 的节点 | {sum(1 for n in nodes if n.get('has_proof'))} |")
    lines.append("")
    if not labeled:
        lines.append("> ⚠️ 本工程所有节点都没有 `\\label`：**无法建边**。"
                     "这是翻译流程的缺口——任务书需要求「保留/补齐 label」。\n")
    if unmapped:
        lines.append("## 未映射环境（Top 20）\n")
        lines.append("这些环境没在 preamble/默认表里找到中文标题，暂不建节点；补 `KIND_BY_TITLE` 即可。\n")
        lines.append("| env | 次数 |")
        lines.append("|---|---|")
        for env, cnt in unmapped.most_common(20):
            lines.append(f"| `{env}` | {cnt} |")
        lines.append("")
    lines.append("## PageRank Top 15（全文最承重的节点）\n")
    lines.append("| # | node | kind | 入度 | PR | 位置 |")
    lines.append("|---|---|---|---|---|---|")
    for i, n in enumerate(top_pr, 1):
        loc = f"{n['locator']['tex_file']}:{n['locator']['tex_lines'][0]}"
        lines.append(f"| {i} | `{n['node_id']}` | {n['kind']} | {n['in_degree']} | {n['pagerank']:.4f} | {loc} |")
    lines.append("")
    lines.append("## 被引用最多 Top 15\n")
    lines.append("| # | node | kind | 入度 | 位置 |")
    lines.append("|---|---|---|---|---|")
    for i, n in enumerate(top_in, 1):
        loc = f"{n['locator']['tex_file']}:{n['locator']['tex_lines'][0]}"
        lines.append(f"| {i} | `{n['node_id']}` | {n['kind']} | {n['in_degree']} | {loc} |")
    lines.append("")
    if unresolved:
        lines.append("## 解析失败的引用目标（Top 20）\n")
        lines.append("常见原因：label 在未扫描的附录/别册、拼写差异、`\\cref` 多目标拆分、章级引用无节点。\n")
        lines.append("| target | 次数 |")
        lines.append("|---|---|")
        for t, c in unresolved.most_common(20):
            lines.append(f"| `{t}` | {c} |")
        lines.append("")
    lines.append("## 下一步\n")
    lines.append("- 人工/LLM 只补 `role`、`difficulty`、`statement_zh`，不改边；")
    lines.append("- 边进人工闸门：每类抽 50 条 precision ≥0.9 才允许扩书；")
    lines.append("- 把本目录登记进 `index/README.md`。")
    lines.append("")

    with open(os.path.join(out_dir, "SUMMARY.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    return {
        "paper_id": paper_id, "files": len(files), "nodes": len(nodes),
        "labeled": len(labeled), "edges": len(edges),
        "uses": uses_n, "mentions": mention_n,
        "unresolved": sum(unresolved.values()), "duplicate_labels": duplicate_labels,
        "unmapped": unmapped.most_common(8),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="项目源码根目录（含 preamble/chunks/chapters 的那层）")
    ap.add_argument("--paper-id", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index"))
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    out_dir = os.path.join(os.path.abspath(args.out), args.paper_id)
    if not os.path.isdir(root):
        sys.exit(f"root not found: {root}")
    stats = build(root, args.paper_id, out_dir)
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    print(f"written: {out_dir}")


if __name__ == "__main__":
    main()
