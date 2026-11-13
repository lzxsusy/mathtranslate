#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从 DSH 会话日志里筛选「高价值任务轨迹」，压成 任务意图 → 关键动作 → 验证证据 → 结论 四段式。

输出（out/ 下）：
  traj_selected.jsonl   每条轨迹一行 JSON（紧凑版，可直接进训练集）
  traj_preview.md       人类可读的样本预览（默认前 20 条），供人工过目
  traj_stats.json       统计

用法：
  python curate_traj.py --top 400 --preview 20
"""
import argparse
import hashlib
import io
import json
import os
import re

import extract_sessions as ex

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")

SYS_MARK = ("Current runtime context.", "<system-reminder>", "<hindsight_knowledge",
            "Time sampled while preparing turn")
SUCCESS = re.compile(r"(已写|写入成功|Written|wrote|passed|全部通过|success|created|创建成功|Saved|saved)", re.I)
ERROR = re.compile(r"(Traceback|exit code: [1-9]|Error:|error:|失败|FAILED|not found|Permission denied)")
WRITE_TOOL = re.compile(r"(write|edit|patch|create|save|present|apply)", re.I)
VERIFY = re.compile(r"(pytest|npm test|go test|cargo test|compile|latexmk|xelatex|pdflatex|--check|validate|verify|lint)", re.I)


def is_sys(text):
    head = text[:200]
    return any(k in head for k in SYS_MARK)


def pick_intent(msgs):
    for m in msgs:
        if m["role"] != "user":
            continue
        t = m["text"].strip()
        if len(t) < 20 or is_sys(t):
            continue
        return t
    return ""


def pick_final(msgs, min_len=200):
    for m in reversed(msgs):
        if m["role"] == "assistant" and len(m["text"]) >= min_len and not is_sys(m["text"]):
            return m["text"]
    return ""


def compact_steps(tools, limit=24, cut=220):
    """把工具调用压成 (动作, 参数摘要, 结果摘要) 序列，合并连续重复的工具名。"""
    steps = []
    prev_name = None
    for t in tools:
        name = (t.get("name") or "").strip() or "tool"
        params = (t.get("input") or "").strip()
        res = (t.get("output") or "").replace("\n", " ").strip()
        if name == prev_name and steps:
            steps[-1]["重复次数"] = steps[-1].get("重复次数", 1) + 1
            continue
        prev_name = name
        if not params and not res:
            continue
        # 参数只留最有信息量的部分：去掉 JSON 外壳的常见键名
        p = params.replace("\n", " ")
        for junk in ('{"', '": "', '", "', '"}', '"}'):
            p = p.replace(junk, " " if junk != '{"' else "")
        p = " ".join(p.split())
        steps.append({
            "动作": name,
            "参数": p[:cut],
            "结果": ("[错误] " if t.get("is_error") else "") + res[:cut],
        })
        if len(steps) >= limit:
            break
    return steps


def score(sid, msgs, tools, deliverable_count):
    chars = sum(len(m["text"]) for m in msgs)
    n_user = sum(1 for m in msgs if m["role"] == "user" and not is_sys(m["text"]))
    n_asst = sum(1 for m in msgs if m["role"] == "assistant")
    n_tools = len(tools)
    err = sum(1 for t in tools if t.get("is_error") or
              ERROR.search(((t.get("output") or "") + (t.get("input") or ""))[:2000]))
    okw = sum(1 for t in tools if WRITE_TOOL.search(t.get("name") or "") and
              SUCCESS.search((t.get("output") or "")[:2000]))
    verify = sum(1 for t in tools if VERIFY.search(((t.get("input") or "") + (t.get("name") or ""))[:500]))
    err_ratio = err / n_tools if n_tools else 0.0

    s = 0.0
    detail = []
    if deliverable_count:
        s += 2.0; detail.append(f"交付物×{deliverable_count}")
    if okw:
        s += 2.0; detail.append(f"写入成功×{okw}")
    if verify:
        s += 1.0; detail.append(f"校验命令×{verify}")
    s += min(3.0, chars / 200000.0)
    s += 1.5 * (1.0 - min(err_ratio, 1.0))
    if 2 <= n_user <= 30:
        s += 0.5
    if err_ratio > 0.5:
        s -= 2.0; detail.append(f"错误率{err_ratio:.0%}")
    if chars < 5000:
        s -= 1.0
    if n_tools == 0:
        s -= 1.0
    if not detail:
        detail.append("无显式产物证据")
    return round(s, 2), chars, n_user, n_asst, n_tools, round(err_ratio, 3), "；".join(detail)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=400)
    ap.add_argument("--preview", type=int, default=20)
    ap.add_argument("--min-score", type=float, default=2.0)
    args = ap.parse_args()

    os.makedirs(OUT, exist_ok=True)
    files = ex.find_sessions()
    print(f"扫描 {len(files)} 个会话 …")

    cands = []
    for i, p in enumerate(files, 1):
        try:
            plain, tools = ex.extract(p)
        except Exception:
            continue
        if not plain:
            continue
        sid = os.path.basename(os.path.dirname(p))
        # 交付物事件要单独扫一遍原始流
        deliverable_count = 0
        try:
            for ev in ex.iter_events(p):
                if ev.get("type") in ("deliverables/presented", "deliverable/presented"):
                    deliverable_count += 1
        except Exception:
            pass
        intent = pick_intent(plain)
        if not intent:
            continue
        s, chars, n_user, n_asst, n_tools, err_ratio, why = score(sid, plain, tools, deliverable_count)
        if s < args.min_score:
            continue
        cands.append({
            "session": sid, "score": s, "chars": chars, "user_msgs": n_user,
            "asst_msgs": n_asst, "tools": n_tools, "err_ratio": err_ratio,
            "why": why, "intent": intent, "msgs": plain, "trows": tools,
        })
        if i % 100 == 0:
            print(f"  {i}/{len(files)}，命中 {len(cands)}")

    # 按分排序 + 按任务意图去重
    cands.sort(key=lambda r: -r["score"])
    seen = set()
    picked = []
    for r in cands:
        key = hashlib.md5(re.sub(r"\s+", "", r["intent"])[:120].encode("utf-8")).hexdigest()
        if key in seen:
            continue
        seen.add(key)
        picked.append(r)
        if len(picked) >= args.top:
            break

    with io.open(os.path.join(OUT, "traj_selected.jsonl"), "w", encoding="utf-8") as f:
        for r in picked:
            f.write(json.dumps({
                "session": r["session"],
                "score": r["score"],
                "证据": r["why"],
                "任务意图": r["intent"][:2000],
                "关键动作": compact_steps(r["trows"]),
                "结论": pick_final(r["msgs"])[:4000],
            }, ensure_ascii=False) + "\n")

    with io.open(os.path.join(OUT, "traj_preview.md"), "w", encoding="utf-8") as f:
        f.write("# 精选轨迹样本（供人工过目）\n\n")
        f.write(f"共入选 {len(picked)} 条，这里展示前 {min(args.preview, len(picked))} 条。\n\n")
        for idx, r in enumerate(picked[: args.preview], 1):
            f.write(f"## {idx}. `{r['session'][:16]}` ｜ 得分 {r['score']} ｜ {r['why']}\n\n")
            f.write(f"- 规模：{r['chars']:,} 字符 / {r['user_msgs']} 轮用户 / {r['tools']} 次工具 / 错误率 {r['err_ratio']:.0%}\n\n")
            f.write(f"**任务意图**\n\n> {r['intent'][:320].replace(chr(10), ' ')}\n\n")
            steps = compact_steps(r["trows"], limit=8, cut=110)
            if steps:
                f.write("**关键动作**\n\n")
                for s in steps:
                    f.write(f"1. `{s['动作']}` {s['参数'][:90]}\n")
                f.write("\n")
            fin = pick_final(r["msgs"])
            if fin:
                f.write(f"**结论**\n\n> {fin[:320].replace(chr(10), ' ')}\n\n")
            f.write("---\n\n")

    stats = {
        "scanned": len(files),
        "candidates": len(cands),
        "selected": len(picked),
        "min_score": args.min_score,
        "avg_score": round(sum(r["score"] for r in picked) / len(picked), 2) if picked else 0,
    }
    with io.open(os.path.join(OUT, "traj_stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
