#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""thinking_audit.py — 思考链候选扫描、人工审计与发布闸门。

设计原则（与 09_thinking/README.md 的硬纪律配套）：

* 机器只做「值得人看」的初筛与压缩：从原始会话里抽取推理片段，生成 <=9KB 的候选卡；
* 人只看候选卡，做「上传 / 不上传 / 改写」的最终决定；
* 只有经人批准的链才进入仓库 `09_thinking/chains/`，原始 reasoning 永不入库；
* `check` 是发布闸门：新交付/新版本没有批准链时返回非零。

用法示例：
    python tools/thinking_audit.py scan --root <parent-session-id> --cards 20
    python tools/thinking_audit.py scan --since 2026-11-14 --per-project 2
    python tools/thinking_audit.py rank --top 15
    python tools/thinking_audit.py extract --session 12c946eb
    python tools/thinking_audit.py approve --card .thinking_candidates/cards/xxx.md \\
        --auditor 李泽轩 --note "第 3 段的自纠改变了术语决定"
    python tools/thinking_audit.py check --require-coverage
    python tools/thinking_audit.py coverage
"""
import argparse
import datetime
import glob
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGING = os.path.join(REPO, ".thinking_candidates")
THINK = os.path.join(REPO, "09_thinking")
CHAINS = os.path.join(THINK, "chains")
INDEX = os.path.join(THINK, "index.csv")
CATALOG = os.path.join(REPO, "site", "catalog.json")
SRC = os.path.join(REPO, "08_source_code")
SESSIONS_ROOT = os.path.join(os.path.expanduser("~"), ".dsh", "sessions")
TZ = datetime.timezone(datetime.timedelta(hours=8))

KW = {
    "self": ["不对", "等等", "其实", "重新", "修正", "错了", "有问题", "矛盾", "不一致",
             "失败", "放弃", "换一种", "回退", "存疑", "需要确认", "改成"],
    "decide": ["术语", "译名", "统一", "冻结", "翻译成", "采用", "决定", "选择", "方案",
               "取舍", "优先", "命名", "口径"],
    "verify": ["编译", "报错", "错误", "校验", "测试", "核对", "检查", "diff", "通过",
               "build", "latexmk", "xelatex", "lint", "0 error"],
}
ROLE_WORDS = ["校对", "核验", "审稿", "校对员", "审计", "评审", "verify", "review"]
CHAIN_SECTIONS = ["任务", "关键片段", "决策与替代方案", "自纠与回退", "验证证据", "逆转条件", "交付物", "审计问题"]


def now_iso():
    return datetime.datetime.now(TZ).isoformat(timespec="seconds")


def safe_rel(p):
    try:
        rel = os.path.relpath(p, REPO)
    except Exception:
        return p
    return p if rel.startswith("..") else rel


def read_header(path):
    """只读第一行，避免为索引解压整个会话。"""
    try:
        p = subprocess.Popen(["zstd", "-dc", path], stdout=subprocess.PIPE,
                             stderr=subprocess.DEVNULL)
        line = p.stdout.readline()
        try:
            p.stdout.close()
        except Exception:
            pass
        try:
            p.terminate()
        except Exception:
            pass
        return json.loads(line.decode("utf-8", "replace"))
    except Exception:
        return None


def read_events(path):
    try:
        raw = subprocess.run(["zstd", "-dc", path], capture_output=True,
                             timeout=180).stdout
    except Exception:
        return []
    out = []
    for line in raw.decode("utf-8", "replace").splitlines():
        try:
            out.append(json.loads(line))
        except Exception:
            continue
    return out


def block_text(block):
    if not isinstance(block, dict):
        return ""
    if block.get("type") in ("reasoning", "thinking"):
        return block.get("text") or ""
    return ""


def text_blocks(content):
    return [b.get("text") or "" for b in content
            if isinstance(b, dict) and b.get("type") == "text"]


def tool_calls(content):
    out = []
    for b in content:
        if not isinstance(b, dict) or b.get("type") != "tool-call":
            continue
        args = b.get("arguments")
        if isinstance(args, str):
            try:
                args = json.loads(args)
            except Exception:
                args = {"_raw": args}
        if not isinstance(args, dict):
            args = {}
        out.append((b.get("name") or "?", args))
    return out


def parse_session(path, header=None):
    hdr = header or read_header(path) or {}
    events = read_events(path)
    first_user = ""
    descriptor = ""
    reasoning = []          # list of dicts
    assistant_text = []
    calls = []
    errors = 0
    usage = dict(calls=0, inp=0, cache=0, out=0)
    for o in events:
        t = o.get("type")
        d = o.get("data") or {}
        if t == "subagent/descriptor":
            descriptor = d.get("label") or ""
        elif t == "user/message":
            c = d.get("content")
            if isinstance(c, list):
                for b in c:
                    if not isinstance(b, dict) or b.get("type") != "text":
                        continue
                    s = (b.get("text") or "").strip()
                    if not s or s.startswith("<system-reminder>"):
                        continue
                    if "current working directory" in s and len(s) < 2000:
                        continue
                    if len(s) > 20 and not first_user:
                        first_user = s
                        break
        elif t == "assistant/message":
            msg = d.get("message") or {}
            content = msg.get("content") or []
            for b in content:
                if not isinstance(b, dict):
                    continue
                if b.get("type") in ("reasoning", "thinking"):
                    s = b.get("text") or ""
                    if s.strip():
                        reasoning.append(dict(text=s, chars=len(s)))
                elif b.get("type") == "text":
                    s = b.get("text") or ""
                    if s.strip():
                        assistant_text.append(s)
            for name, args in tool_calls(content):
                calls.append((name, args))
            u = d.get("usage") or {}
            if u:
                usage["calls"] += 1
                usage["inp"] += int(u.get("inputTokens") or 0)
                usage["cache"] += int(u.get("cacheReadTokens") or 0)
                usage["out"] += int(u.get("outputTokens") or 0)
        elif t == "tool/result":
            if d.get("isError") or d.get("is_error"):
                errors += 1
    return dict(id=hdr.get("id") or os.path.basename(os.path.dirname(path)),
                created=hdr.get("createdAt") or "",
                cwd=hdr.get("cwd") or "",
                parent=hdr.get("parentSession") or "",
                depth=hdr.get("delegationDepth") or 0,
                preset=hdr.get("agentPreset") or "",
                descriptor=descriptor,
                first_user=first_user,
                reasoning=reasoning,
                assistant_text=assistant_text,
                calls=calls,
                errors=errors,
                usage=usage,
                path=path)


def load_catalog():
    if not os.path.isfile(CATALOG):
        return []
    try:
        return json.load(open(CATALOG, encoding="utf-8"))
    except Exception:
        return []


def classify_project(text, cwd="", catalog=None):
    text = text or ""
    m = re.search(r"\b(SY\d{2}-\d{2})\b", text)
    if m:
        return m.group(1)
    if "春弦抄" in text:
        return "CX"
    if "Cox" in text and ("Katz" in text or "镜像对称与代数几何" in text):
        return "SY01-26"
    if "Witten" in text and "Jones" in text:
        return "WIT-1989-JONES"
    catalog = catalog if catalog is not None else load_catalog()
    best = ("UNMAPPED", 0)
    low = text.lower()
    for e in catalog:
        cn = (e.get("cn") or "").strip()
        orig = (e.get("orig") or "").strip()
        score = 0
        if len(cn) >= 5 and cn in text:
            score = max(score, 3 + min(len(cn) / 20.0, 2))
        if len(orig) >= 10 and orig.lower() in low:
            score = max(score, 2 + min(len(orig) / 40.0, 2))
        if score > best[1]:
            best = (e.get("id") or "UNMAPPED", score)
    if best[1] >= 3:
        return best[0]
    # 08_source_code 的目录名做最后兜底
    if os.path.isdir(SRC):
        for d in os.listdir(SRC):
            mm = re.match(r"(SY\d{2}-\d{2}|CX)", d)
            if mm and mm.group(1) in text:
                return mm.group(1)
    return "UNMAPPED"


def count_kw(s):
    return {k: sum(s.count(w) for w in ws) for k, ws in KW.items()}


def sentences(text):
    parts = re.split(r"(?<=[。！？；!?;])\s*|\n+", text)
    return [p.strip() for p in parts if len(p.strip()) >= 12]


def best_window(text, budget=760, prefer=None):
    """从一大段 reasoning 里取关键词最密的一小段（含前后文）。"""
    paras = [p.strip() for p in re.split(r"\n{2,}", text) if p.strip()]
    if len(paras) <= 1:
        paras = sentences(text)
    if not paras:
        return text[:budget]
    scored = []
    for i, p in enumerate(paras):
        k = count_kw(p)
        s = 2.0 * k["self"] + 1.2 * k["decide"] + 1.0 * k["verify"]
        s += min(len(p), 1200) / 1200.0 * 0.4
        if prefer:
            for w in prefer:
                if w in p:
                    s += 2
        scored.append((s, i))
    scored.sort(reverse=True)
    picks = []
    for s, i in scored:
        if s <= 0 and picks:
            break
        if any(abs(i - j) <= 1 for j in picks):
            continue
        picks.append(i)
        if len(picks) >= 2:
            break
    if not picks:
        picks = [0]
    lo, hi = min(picks), max(picks)
    seg = paras[lo:hi + 1]
    out = "\n".join(seg)
    if len(out) > budget:
        # 从关键词第一次出现处向后截
        cand = out
        cut = budget
        for w in KW["self"] + KW["decide"]:
            idx = cand.find(w)
            if idx > 0:
                cut = min(len(cand), idx + budget // 2)
                break
        out = cand[max(0, cut - budget):cut]
    return out.strip()


def pick_episodes(sess, max_episodes=8):
    blocks = sess["reasoning"]
    ranked = []
    for i, b in enumerate(blocks):
        k = count_kw(b["text"])
        s = 2.0 * k["self"] + 1.2 * k["decide"] + 1.0 * k["verify"]
        s += math.log10(1 + b["chars"])
        ranked.append((s, i))
    ranked.sort(reverse=True)
    picks = []
    for s, i in ranked:
        if len(picks) >= max_episodes:
            break
        if any(abs(i - j) <= 0 for j in picks):
            continue
        picks.append(i)
    picks.sort()
    eps = []
    for i in picks:
        b = blocks[i]
        k = count_kw(b["text"])
        eps.append(dict(no=i + 1, total=len(blocks), chars=b["chars"],
                        kw=k, excerpt=best_window(b["text"], 760)))
    return eps


def extract_sentences(sess, kind, limit=6):
    out = []
    seen = set()
    for b in sess["reasoning"]:
        for s in sentences(b["text"]):
            if not any(w in s for w in KW[kind]):
                continue
            s = re.sub(r"\s+", " ", s)[:240]
            h = hashlib.sha1(s.encode("utf-8")).hexdigest()
            if h in seen:
                continue
            seen.add(h)
            out.append(s)
            if len(out) >= limit:
                return out
    return out


def deliverable_paths(sess):
    paths = []
    for name, args in sess["calls"]:
        for k in ("file_path", "path", "notebook_path", "target_file"):
            v = args.get(k)
            if isinstance(v, str) and len(v) > 3 and v not in paths:
                paths.append(v)
    return paths


def role_of(text):
    return any(w in (text or "") for w in ROLE_WORDS)


def score_session(sess, project):
    r = sum(b["chars"] for b in sess["reasoning"])
    kw = count_kw("\n".join(b["text"] for b in sess["reasoning"]))
    paths = deliverable_paths(sess)
    existing = [p for p in paths if os.path.exists(p)]
    vol = min(3.0, math.log10(1 + r) / 1.6)
    self_s = min(2.5, kw["self"] / 10.0)
    dec_s = min(2.0, kw["decide"] / 20.0)
    ver_s = min(1.5, kw["verify"] / 50.0)
    role = 0.6 if role_of(sess["first_user"] + " " + sess["descriptor"]) else 0.0
    outcome = 0.6 if existing else 0.0
    err = 0.4 if sess["errors"] else 0.0
    score = min(10.0, vol + self_s + dec_s + ver_s + role + outcome + err)
    why = []
    why.append("推理 %.1f 万字符（%d 段）" % (r / 10000.0, len(sess["reasoning"])))
    if kw["self"]:
        why.append("自纠 %d 处" % kw["self"])
    if kw["decide"]:
        why.append("决策 %d 处" % kw["decide"])
    if kw["verify"]:
        why.append("验证 %d 处" % kw["verify"])
    if sess["errors"]:
        why.append("工具错误 %d 次" % sess["errors"])
    if existing:
        why.append("落盘文件 %d 个" % len(existing))
    if role:
        why.append("角色含校对/核验")
    return round(score, 2), kw, paths, existing, why


def fmt_created(v):
    """createdAt 在不同版本里可能是 ISO 字符串或 epoch 毫秒整数。"""
    if isinstance(v, (int, float)):
        try:
            return datetime.datetime.fromtimestamp(v / 1000.0).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return str(v)
    return str(v or "")[:19].replace("T", " ")


def card_markdown(sess, project, score, kw, paths, existing, why, episodes, card_rel):
    created = fmt_created(sess["created"])
    front = [
        "---",
        "session: %s" % sess["id"],
        "project: %s" % project,
        "created: %s" % created,
        "model: deepseek-flash",
        "score: %.2f" % score,
        "reasoning_chars: %d" % sum(b["chars"] for b in sess["reasoning"]),
        "calls: %d" % sess["usage"]["calls"],
        "tool_errors: %d" % sess["errors"],
        "card_version: 1",
        "decision: pending",
        "approved_by:",
        "approved_at:",
        "---",
        "",
        "# 思考链候选 · %s · %s" % (project, sess["id"][:8]),
        "",
        "> 这是机器初筛的候选卡，**不是已上传的思考链**。",
        "> 审计人只在下面第 0 节做决定；`approve` 之后才会进入 `09_thinking/chains/`。",
        "",
        "## 0. 审计结论（人填）",
        "",
        "- [ ] 上传为正式链    - [ ] 不上传    - [ ] 改写后再上传",
        "理由（必填，一句话）：",
        "",
        "## 1. 任务",
        "",
        "```text",
        (sess["first_user"] or "（未取到首条任务文本）")[:1400],
        "```",
        "",
        "## 2. 为什么机器认为值得看",
        "",
    ]
    front += ["- " + x for x in why]
    front += [
        "",
        "| 项 | 值 |",
        "|---|---|",
        "| 项目 | `%s` |" % project,
        "| 会话 | `%s` |" % sess["id"],
        "| 创建时间 | %s |" % (created or "?"),
        "| 工作目录 | `%s` |" % sess["cwd"],
        "| 子代理标签 | %s |" % (sess["descriptor"] or "—"),
        "| 调用 / 输出 token | %d / %s |" % (sess["usage"]["calls"], format(sess["usage"]["out"], ",")),
        "",
        "## 3. 关键片段",
        "",
    ]
    for e in episodes:
        front += [
            "### 片段 %d/%d · %s 字符 · 自纠 %d / 决策 %d / 验证 %d" %
            (e["no"], e["total"], format(e["chars"], ","), e["kw"]["self"],
             e["kw"]["decide"], e["kw"]["verify"]),
            "",
            "```text",
            e["excerpt"],
            "```",
            "",
        ]
    front += ["## 4. 决策与替代方案", ""]
    dec = extract_sentences(sess, "decide", 6)
    if dec:
        for i, s in enumerate(dec, 1):
            front.append("%d. %s" % (i, s))
    else:
        front.append("（自动抽取未命中；审计时看第 3 节，手工补一条。）")
    front += ["", "## 5. 自纠与回退", ""]
    cor = extract_sentences(sess, "self", 6)
    if cor:
        for i, s in enumerate(cor, 1):
            front.append("%d. %s" % (i, s))
    else:
        front.append("（本会话没有明显自纠；如确有回退，请审计人补。）")
    front += ["", "## 6. 验证证据", ""]
    ver = []
    for name, args in sess["calls"]:
        cmd = args.get("command") or args.get("cmd") or ""
        if isinstance(cmd, str) and re.search(
                r"latexmk|xelatex|pdflatex|build|lint|test|check|diff|compile|pytest", cmd, re.I):
            ver.append("`%s`: `%s`" % (name, re.sub(r"\s+", " ", cmd)[:180]))
        if len(ver) >= 8:
            break
    if ver:
        front += ["- " + x for x in ver]
    else:
        front.append("- （自动未识别到构建/校验命令；工具错误 %d 次也可作为证据。）" % sess["errors"])
    front += [
        "",
        "## 7. 逆转条件",
        "",
        "- 如果出现什么证据（原文另有一版、术语表更新、编译/核验反例），这个决定应被推翻？",
        "- 当时没看到的替代解释是什么？",
        "",
        "## 8. 交付物",
        "",
    ]
    if existing:
        for p in existing[:12]:
            front.append("- `%s`" % p)
    elif paths:
        for p in paths[:12]:
            front.append("- `%s`（扫描时不存在）" % p)
    else:
        front.append("（无文件路径；可能是纯分析/检索会话。）")
    front += [
        "",
        "## 9. 审计问题（必须逐条回答后才能批准）",
        "",
        "1. 这条链里哪一个决定**真正改变了交付物**？给出文件/页码/行号。",
        "2. 被否决的方案是什么？为什么否决？如果换个证据，会不会翻案？",
        "3. 有没有一条可复用的判断规则（不是「我检查了」，而是「以后遇到 X 先看 Y」）？",
        "4. 哪一段是**噪音/重复劳动**，不应进入训练数据？",
        "5. 脱敏检查：路径、邮箱、令牌、底本长引用是否已处理？",
        "",
        "## 10. 批准命令",
        "",
        "```bash",
        "python tools/thinking_audit.py approve --card %s \\" % card_rel,
        "  --auditor <你的名字> --note \"<一句话理由>\"",
        "```",
    ]
    text = "\n".join(front) + "\n"
    # 硬上限 9KB：优先压缩第 3 节片段，保住第 4–10 节（审计必需）
    if len(text) > 9000:
        a = text.index("## 3. 关键片段")
        b = text.index("## 4. 决策与替代方案")
        head, mid, tail = text[:a], text[a:b], text[b:]
        budget = 9000 - len(head) - len(tail) - 160
        note = "> 卡片超长，片段已截断；完整推理用 `extract --session <id>` 查看。\n\n"
        if budget > 400:
            mid = "## 3. 关键片段\n\n" + note + mid[len("## 3. 关键片段"):].lstrip()[:budget]
        else:
            mid = "## 3. 关键片段\n\n" + note
        text = head + mid.rstrip() + "\n\n" + tail
    return text


def cmd_scan(args):
    catalog = load_catalog()
    paths = []
    for dp, dn, fn in os.walk(args.sessions or SESSIONS_ROOT):
        if "session.v4.jsonl.zstd" in fn:
            paths.append(os.path.join(dp, "session.v4.jsonl.zstd"))
    since = None
    if args.since:
        try:
            since = datetime.datetime.strptime(args.since, "%Y-%m-%d").replace(tzinfo=TZ)
        except ValueError:
            sys.exit("--since 需 YYYY-MM-DD")
    picked = []
    for p in paths:
        h = read_header(p)
        if not h:
            continue
        if args.root and h.get("parentSession") != args.root:
            continue
        if since and h.get("createdAt"):
            try:
                dt = datetime.datetime.fromisoformat(h["createdAt"].replace("Z", "+00:00"))
                if dt < since:
                    continue
            except Exception:
                pass
        picked.append((p, h))
    rows = []
    for p, h in picked:
        s = parse_session(p, h)
        text = s["first_user"] + " " + s["descriptor"]
        proj = classify_project(text, s["cwd"], catalog)
        if args.project and proj != args.project:
            continue
        r = sum(b["chars"] for b in s["reasoning"])
        if r < args.min_chars:
            continue
        score, kw, dpaths, existing, why = score_session(s, proj)
        rows.append(dict(session=s, project=proj, score=score, kw=kw,
                         paths=dpaths, existing=existing, why=why, rchars=r))
    rows.sort(key=lambda x: -x["score"])
    os.makedirs(args.out, exist_ok=True)
    cards_dir = os.path.join(args.out, "cards")
    os.makedirs(cards_dir, exist_ok=True)
    per = defaultdict(int)
    written = 0
    index_lines = []
    for row in rows:
        if args.cards > 0 and written >= args.cards:
            break
        s = row["session"]
        if per[row["project"]] >= args.per_project and args.per_project > 0:
            continue
        per[row["project"]] += 1
        eps = pick_episodes(s, args.episodes)
        name = "%s_%s.md" % (row["project"], s["id"][:8])
        card_rel = os.path.join(args.out, "cards", name).replace("\\", "/")
        md = card_markdown(s, row["project"], row["score"], row["kw"],
                           row["paths"], row["existing"], row["why"], eps, card_rel)
        with open(os.path.join(cards_dir, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(md)
        row["card"] = card_rel
        index_lines.append(row)
        written += 1
    with open(os.path.join(args.out, "candidates.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(dict(
                project=row["project"], score=row["score"], rchars=row["rchars"],
                session=row["session"]["id"], created=row["session"]["created"],
                calls=row["session"]["usage"]["calls"],
                out_tokens=row["session"]["usage"]["out"],
                errors=row["session"]["errors"], kw=row["kw"],
                why=row["why"], card=row.get("card", ""),
                first_user=row["session"]["first_user"][:300],
            ), ensure_ascii=False) + "\n")
    summary = dict(
        scanned=len(picked), kept=len(rows), cards=written,
        reasoning_chars=sum(r["rchars"] for r in rows),
        cost_note="成本由会话 usage 另算；本工具不做计费。",
        generated=now_iso(),
    )
    with open(os.path.join(args.out, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    top = rows[:args.top]
    print("扫描 %d 个会话，保留 %d 个（>=%d 字符推理），生成 %d 张候选卡" %
          (len(picked), len(rows), args.min_chars, written))
    print("%-10s %-18s %5s %9s %6s %5s  %s" % ("项目", "会话", "分", "推理字符", "调用", "错误", "理由"))
    for r in top:
        s = r["session"]
        print("%-10s %-18s %5.2f %9s %6d %5d  %s" %
              (r["project"], s["id"][:8], r["score"], format(r["rchars"], ","),
               s["usage"]["calls"], s["errors"], "；".join(r["why"][:3])))
    print("\n候选卡目录：%s" % cards_dir)
    print("下一步：逐张看卡 → 在卡第 0 节写结论 → approve；批准后才进 09_thinking/chains/。")


def load_candidates(out):
    p = os.path.join(out, "candidates.jsonl")
    if not os.path.isfile(p):
        sys.exit("找不到 %s，先跑 scan" % p)
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def cmd_rank(args):
    rows = load_candidates(args.out)
    rows.sort(key=lambda x: -x["score"])
    print("%-10s %-18s %5s %9s %6s %5s  %s" % ("项目", "会话", "分", "推理字符", "调用", "错误", "理由"))
    for r in rows[:args.top]:
        print("%-10s %-18s %5.2f %9s %6d %5d  %s" %
              (r["project"], r["session"][:8], r["score"], format(r["rchars"], ","),
               r["calls"], r["errors"], "；".join(r["why"][:3])))
    print("\n共 %d 条；卡片在 %s/cards/" % (len(rows), args.out))


def cmd_extract(args):
    paths = []
    for dp, dn, fn in os.walk(SESSIONS_ROOT):
        if "session.v4.jsonl.zstd" in fn:
            p = os.path.join(dp, "session.v4.jsonl.zstd")
            h = read_header(p)
            if h and (h.get("id") or "").startswith(args.session):
                paths.append((p, h))
    if not paths:
        sys.exit("找不到会话 %s" % args.session)
    p, h = paths[0]
    s = parse_session(p, h)
    text = card_markdown(s, classify_project(s["first_user"]), 0, count_kw(""), [], [], ["手动 extract"], pick_episodes(s, 12), "（从候选卡 approve）")
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("写入 %s（%d 字符）" % (args.out, len(text)))
    else:
        print(text)


def parse_front(text):
    front = {}
    if not text.startswith("---"):
        return front, text
    end = text.find("\n---", 3)
    if end < 0:
        return front, text
    for line in text[3:end].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            front[k.strip()] = v.strip()
    return front, text[end + 4:]


def scrub(text):
    text = re.sub(r"C:\\Users\\[^\\\s\"'`]+", "<本地路径>", text)
    text = re.sub(r"/c/Users/[^\s\"'`]+", "<本地路径>", text)
    text = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[邮箱隐去]", text)
    text = re.sub(r"\b(sk|ghp|gho|AKIA)[-_A-Za-z0-9]{8,}\b", "[已脱敏]", text)
    return text


def cmd_approve(args):
    if not os.path.isfile(args.card):
        sys.exit("卡片不存在：%s" % args.card)
    text = open(args.card, encoding="utf-8").read()
    front, body = parse_front(text)
    for sec in CHAIN_SECTIONS:
        if ("## " + sec) not in body and (sec not in body):
            sys.exit("卡片缺少章节「%s」，拒绝批准" % sec)
    if front.get("decision") not in ("pending", "", None):
        sys.exit("卡片 decision=%s，不是 pending；不要重复批准" % front.get("decision"))
    if front.get("reasoning_chars", "0").isdigit() and int(front["reasoning_chars"]) < 3000:
        sys.exit("推理量不足 3000 字符，不像一条有决策的链")
    proj = front.get("project") or "UNMAPPED"
    sid = front.get("session") or "unknown"
    day = (front.get("created") or now_iso())[:10]
    cid = "%s_%s" % (day, sid[:8])
    outdir = os.path.join(CHAINS, proj)
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, cid + ".md")
    if os.path.exists(outpath):
        sys.exit("目标已存在：%s" % outpath)
    if args.dry_run:
        print("dry-run：将写入 %s" % outpath)
        return
    # 重新组装 front matter：批准元数据 + 人的理由
    head = [
        "---",
        "chain_id: %s" % cid,
        "project: %s" % proj,
        "session: %s" % sid,
        "created: %s" % (front.get("created") or ""),
        "approved_by: %s" % args.auditor,
        "approved_at: %s" % now_iso(),
        "score: %s" % front.get("score", ""),
        "reasoning_chars: %s" % front.get("reasoning_chars", ""),
        "decision: approved",
        "audit_note: %s" % re.sub(r"\s+", " ", args.note)[:400],
        "source_card: %s" % safe_rel(os.path.abspath(args.card)),
        "---",
        "",
    ]
    body = body.replace("## 0. 审计结论（人填）", "## 0. 审计结论")
    body = re.sub(r"(- \[ \] 上传为正式链.*)", "已批准：%s" % args.note, body, count=1)
    out = scrub("\n".join(head) + body)
    with open(outpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    os.makedirs(THINK, exist_ok=True)
    new = not os.path.isfile(INDEX)
    with open(INDEX, "a", encoding="utf-8", newline="\n") as f:
        if new:
            f.write("project,chain_id,session,approved_by,approved_at,score,reasoning_chars,source_card,audit_note\n")
        f.write(",".join([
            proj, cid, sid, args.auditor, now_iso(), front.get("score", ""),
            front.get("reasoning_chars", ""), safe_rel(os.path.abspath(args.card)),
            args.note.replace(",", "，"),
        ]) + "\n")
    print("已批准：%s" % outpath)
    print("已登记：%s" % INDEX)


def cmd_check(args):
    errors = []
    rows = []
    if os.path.isfile(INDEX):
        import csv
        with open(INDEX, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    seen = set()
    for r in rows:
        cid = r.get("chain_id", "")
        proj = r.get("project", "")
        seen.add(proj)
        p = os.path.join(CHAINS, proj, cid + ".md")
        if not os.path.isfile(p):
            errors.append("索引条目缺文件：%s" % p)
            continue
        t = open(p, encoding="utf-8").read()
        for sec in ("## 4. 决策与替代方案", "## 6. 验证证据", "## 7. 逆转条件"):
            if sec not in t and sec.lstrip("# ") not in t:
                errors.append("%s 缺少「%s」" % (p, sec))
        if len(t) > 12000:
            errors.append("%s 超过 12KB，违反 R3" % p)
    if args.require_coverage:
        cat = load_catalog()
        need = {e.get("id") for e in cat if e.get("id")}
        missing = sorted(need - seen)
        if missing:
            errors.append("以下 %d 部已发布卷没有批准链：%s" %
                          (len(missing), ", ".join(missing[:20]) + ("…" if len(missing) > 20 else "")))
    if errors:
        print("检查失败（%d 项）：" % len(errors))
        for e in errors:
            print(" - " + e)
        sys.exit(1)
    print("检查通过：%d 条链，覆盖 %d 个项目" % (len(rows), len(seen)))


def cmd_coverage(args):
    cat = load_catalog()
    released = {e.get("id") for e in cat if e.get("id")}
    chains = defaultdict(int)
    if os.path.isfile(INDEX):
        import csv
        for r in csv.DictReader(open(INDEX, encoding="utf-8")):
            chains[r.get("project", "")] += 1
    projects = set()
    if os.path.isdir(SRC):
        for d in os.listdir(SRC):
            m = re.match(r"(SY\d{2}-\d{2}|CX)", d)
            if m:
                projects.add(m.group(1))
    projects |= released | set(chains)
    print("%-10s %-8s %6s  %s" % ("项目", "已发布", "链数", "状态"))
    missing = []
    for p in sorted(projects):
        n = chains.get(p, 0)
        st = "OK" if n else ("缺链" if p in released else "未发布/无链")
        if p in released and not n:
            missing.append(p)
        print("%-10s %-8s %6d  %s" % (p, "是" if p in released else "否", n, st))
    print("\n已发布 %d 部，其中有链 %d 部，缺链 %d 部" %
          (len(released), len(released) - len(missing), len(missing)))
    if args.json:
        json.dump(dict(released=len(released), missing=missing,
                       chains={k: v for k, v in chains.items()}),
                  open(args.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def cmd_report(args):
    rows = load_candidates(args.out)
    by = defaultdict(lambda: dict(n=0, chars=0, score=0.0))
    for r in rows:
        b = by[r["project"]]
        b["n"] += 1
        b["chars"] += r["rchars"]
        b["score"] += r["score"]
    print("候选总数 %d，推理总量 %s 字符" % (len(rows), format(sum(r["rchars"] for r in rows), ",")))
    for p, b in sorted(by.items(), key=lambda kv: -kv[1]["chars"]):
        print("%-10s %3d 条  %9s 字符  均分 %.2f" %
              (p, b["n"], format(b["chars"], ","), b["score"] / max(1, b["n"])))


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="思考链候选扫描与人工审计")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("scan", help="扫描会话，生成候选卡")
    s.add_argument("--sessions", default=SESSIONS_ROOT)
    s.add_argument("--root", help="只扫某个父会话的子会话")
    s.add_argument("--since", help="YYYY-MM-DD")
    s.add_argument("--project", help="只保留某项目")
    s.add_argument("--min-chars", type=int, default=8000)
    s.add_argument("--cards", type=int, default=20, help="最多写多少张卡（0=全部）")
    s.add_argument("--per-project", type=int, default=3)
    s.add_argument("--episodes", type=int, default=8)
    s.add_argument("--top", type=int, default=20)
    s.add_argument("--out", default=STAGING)
    s.set_defaults(func=cmd_scan)

    r = sub.add_parser("rank", help="打印候选排名")
    r.add_argument("--out", default=STAGING)
    r.add_argument("--top", type=int, default=20)
    r.set_defaults(func=cmd_rank)

    e = sub.add_parser("extract", help="导出单个会话的完整候选卡")
    e.add_argument("--session", required=True, help="会话 id 前缀")
    e.add_argument("--out")
    e.set_defaults(func=cmd_extract)

    a = sub.add_parser("approve", help="人工批准一张候选卡，写入 09_thinking/chains/")
    a.add_argument("--card", required=True)
    a.add_argument("--auditor", required=True)
    a.add_argument("--note", required=True)
    a.add_argument("--dry-run", action="store_true")
    a.set_defaults(func=cmd_approve)

    c = sub.add_parser("check", help="发布闸门：链完整性与覆盖率")
    c.add_argument("--require-coverage", action="store_true")
    c.set_defaults(func=cmd_check)

    v = sub.add_parser("coverage", help="项目覆盖表")
    v.add_argument("--json")
    v.set_defaults(func=cmd_coverage)

    p = sub.add_parser("report", help="候选汇总")
    p.add_argument("--out", default=STAGING)
    p.set_defaults(func=cmd_report)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
