#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从 DSH 会话日志（~/.dsh/sessions/**/session.v4.jsonl.zstd）抽取对话语料。

输出（默认在 out/ 下）：
  sessions_plain.jsonl   每行 {"ts","session","role","text"}，role=user/assistant
  sessions_tools.jsonl   每行 {"ts","session","name","input","output"}（工具调用/结果，供 agent 轨迹训练用）
  session_stats.json     汇总统计

用法：
  python extract_sessions.py                 # 全量
  python extract_sessions.py --limit 20      # 只跑最大的 20 个会话
  python extract_sessions.py --stats-only    # 只统计不写文件
"""
import argparse
import io
import json
import os
import re
import sys
import zstandard

SESS_ROOT = os.path.join(os.path.expanduser("~"), ".dsh", "sessions")

# 明显含敏感信息的行直接跳过（密钥/令牌/密码形式）
SENSITIVE = re.compile(
    r"(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{16,}|"
    r"AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----)",
    re.I,
)


def find_sessions():
    out = []
    for root, _dirs, files in os.walk(SESS_ROOT):
        for f in files:
            if f == "session.v4.jsonl.zstd":
                out.append(os.path.join(root, f))
    out.sort(key=lambda p: os.path.getsize(p), reverse=True)
    return out


def iter_events(path):
    dctx = zstandard.ZstdDecompressor()
    with open(path, "rb") as fh:
        with dctx.stream_reader(fh) as reader:
            text = io.TextIOWrapper(reader, encoding="utf-8", errors="replace")
            for line in text:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except Exception:
                    continue


def _text_of(msg):
    """尽力从各种消息结构里取出纯文本。"""
    if msg is None:
        return ""
    if isinstance(msg, str):
        return msg
    if isinstance(msg, list):
        parts = []
        for it in msg:
            if isinstance(it, str):
                parts.append(it)
            elif isinstance(it, dict):
                for k in ("text", "content", "value", "thinking"):
                    v = it.get(k)
                    if isinstance(v, str) and v.strip():
                        parts.append(v)
                        break
        return "\n".join(parts)
    if isinstance(msg, dict):
        for k in ("text", "content", "message", "value", "reasoning"):
            v = msg.get(k)
            if isinstance(v, (str, list, dict)):
                got = _text_of(v)
                if got.strip():
                    return got
    return ""


def extract(path, want_tools=True):
    """返回 (plain_rows, tool_rows)。

    tool_rows 已按 callId 把 tool/call 与 tool/result 配成一条：
      {"ts","session","name","input","output","is_error"}
    """
    plain, tools = [], []
    sid = os.path.basename(os.path.dirname(path))
    pending = {}  # callId -> row
    for ev in iter_events(path):
        et = ev.get("type", "")
        ts = ev.get("time") or ev.get("createdAt") or 0
        data = ev.get("data") or {}
        if et == "user/message":
            txt = _text_of(data.get("message") or data.get("text") or data)
            if txt.strip():
                plain.append({"ts": ts, "session": sid, "role": "user", "text": txt})
        elif et == "assistant/message":
            txt = _text_of(data.get("message") or data.get("text") or data)
            if txt.strip():
                plain.append({"ts": ts, "session": sid, "role": "assistant", "text": txt})
        elif want_tools and et == "tool/call":
            cid = data.get("callId") or data.get("id") or ""
            args = data.get("arguments")
            if isinstance(args, (dict, list)):
                args = json.dumps(args, ensure_ascii=False)
            row = {
                "ts": ts, "session": sid,
                "name": data.get("name") or data.get("tool") or "",
                "input": (args or "")[:4000],
                "output": "",
                "is_error": False,
            }
            if cid:
                pending[cid] = row
                tools.append(row)
            else:
                tools.append(row)
        elif want_tools and et == "tool/result":
            msg = data.get("message") or {}
            cid = msg.get("toolCallId") or (msg.get("source") or {}).get("callId") or ""
            out = _text_of(msg.get("content") or msg.get("result") or data)[:4000]
            row = pending.pop(cid, None) if cid else None
            if row is None:
                row = {"ts": ts, "session": sid, "name": "", "input": "", "output": "", "is_error": False}
                tools.append(row)
            row["output"] = out
            row["is_error"] = bool(msg.get("isError"))
            if not row["name"]:
                row["name"] = (msg.get("source") or {}).get("toolName") or "tool"
    return plain, tools


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "out"))
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stats-only", action="store_true")
    ap.add_argument("--min-chars", type=int, default=2)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    files = find_sessions()
    if args.limit:
        files = files[: args.limit]

    n_plain = n_tools = chars = 0
    n_user = n_asst = 0
    skipped_sensitive = 0
    sessions_used = 0

    f_plain = None
    f_tools = None
    if not args.stats_only:
        f_plain = open(os.path.join(args.out, "sessions_plain.jsonl"), "w", encoding="utf-8")
        f_tools = open(os.path.join(args.out, "sessions_tools.jsonl"), "w", encoding="utf-8")

    for i, p in enumerate(files, 1):
        try:
            plain, tools = extract(p)
        except Exception as e:  # 单个会话坏了不影响整体
            print(f"[skip] {p}: {e}", file=sys.stderr)
            continue
        kept = 0
        for row in plain:
            t = row["text"]
            if len(t) < args.min_chars:
                continue
            if SENSITIVE.search(t):
                skipped_sensitive += 1
                continue
            kept += 1
            n_plain += 1
            chars += len(t)
            if row["role"] == "user":
                n_user += 1
            else:
                n_asst += 1
            if f_plain:
                f_plain.write(json.dumps(row, ensure_ascii=False) + "\n")
        for row in tools:
            n_tools += 1
            if f_tools:
                f_tools.write(json.dumps(row, ensure_ascii=False) + "\n")
        if kept:
            sessions_used += 1
        if i % 100 == 0:
            print(f"  ... {i}/{len(files)} 会话，消息 {n_plain}，字符 {chars:,}", file=sys.stderr)

    if f_plain:
        f_plain.close()
    if f_tools:
        f_tools.close()

    # 中文为主，粗估 token：中文约 1 字 ≈ 0.7 token，英文约 4 字符 ≈ 1 token；混合取 0.65 系数
    stats = {
        "sessions_total": len(find_sessions()),
        "sessions_scanned": len(files),
        "sessions_with_text": sessions_used,
        "messages": n_plain,
        "user_messages": n_user,
        "assistant_messages": n_asst,
        "chars": chars,
        "est_tokens": int(chars * 0.65),
        "tool_rows": n_tools,
        "skipped_sensitive": skipped_sensitive,
    }
    with open(os.path.join(args.out, "session_stats.json"), "w", encoding="utf-8") as fh:
        json.dump(stats, fh, ensure_ascii=False, indent=2)
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
