# -*- coding: utf-8 -*-
"""合规门禁：按 COMPLIANCE.md 检查仓库是否还能提交。

用法：
    python tools/check_compliance.py            # 检查已跟踪文件，违规时退出码 1
    python tools/check_compliance.py --all      # 同时检查未跟踪的新文件
    python tools/check_compliance.py --quiet    # 只打印违规

检查项：
  R1 扫描件/影印本/原书 PDF/页面图 不得入库
  R2 原文 PDF 直链 不得出现
  R3 成品 PDF 不得入库（Release 外链或申请获取）
  R4 越权许可措辞
  R5 台账覆盖 08_source_code 全部工程，且状态为「合规」
  R6 本脚本 + .githooks/pre-commit
"""
import csv
import os
import io
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# Windows 控制台默认 GBK，违规信息里带 © 等字符会让 print 直接崩，门禁变成假失败
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

TEXT_EXT = {".md", ".txt", ".tsv", ".csv", ".json", ".jsonl", ".py", ".ps1", ".sh",
            ".html", ".js", ".css", ".yml", ".yaml", ".tex", ".bib", ".rst"}
# 这些文件本身就在讨论规则，措辞检查跳过（但仍检查链接与文件）
POLICY_FILES = {"COMPLIANCE.md", "LICENSE", "AUDIT_2026-11-15.md",
                "ASSESSMENT_2026-11-16.md", "CHANGELOG.md", "RELEASE_REGISTER.csv",
                "README.md", "00_README.md", "DATASHEET.md",
                "04_playbook/README.md", "tools/check_compliance.py",
                "tools/build_release_register.py"}
# 自撰交付物（讲义、读书笔记），非第三方底本成品
ALLOW_PDF = re.compile(r"^papers/[^/]+/deliverables/")


def repo_public_projects():
    """台账里 成品在仓=是 且 成品级别=随仓公开 的工程目录集合。

    R3 的红线针对「在版图书底本的译文成品」；底本为公开课程讲义/开放许可材料时，
    只要在 RELEASE_REGISTER.csv 登记为随仓公开，成品 PDF 即随仓发布。
    """
    import csv as _csv
    try:
        rows = list(_csv.DictReader(io.open("RELEASE_REGISTER.csv", encoding="utf-8-sig")))
    except OSError:
        return set()
    return {
        r.get("工程目录", "").replace("\\", "/")
        for r in rows
        if (r.get("成品在仓") or "").strip() == "是" and (r.get("成品级别") or "").strip() == "随仓公开"
    }

violations = []
warnings = []


def add(kind, msg):
    violations.append((kind, msg))


def warn(msg):
    warnings.append(msg)


def git_files(all_files=False):
    args = ["git", "ls-files", "-z"]
    if all_files:
        args = ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"]
    out = subprocess.run(args, capture_output=True).stdout
    return [p.decode("utf-8", "replace") for p in out.split(b"\0") if p]


def is_text(rel):
    return os.path.splitext(rel)[1].lower() in TEXT_EXT


def read_bytes(rel, limit=None):
    try:
        with open(rel, "rb") as f:
            return f.read() if limit is None else f.read(limit)
    except OSError:
        return b""


PUBLIC_PROJECTS = None


def check_paths(files):
    global PUBLIC_PROJECTS
    if PUBLIC_PROJECTS is None:
        PUBLIC_PROJECTS = repo_public_projects()
    for rel in files:
        low = rel.replace("\\", "/")
        parts = low.split("/")
        name = parts[-1]
        ext = os.path.splitext(name)[1].lower()

        # R1：原本 / originals / 扫描件目录
        if any(p in ("原本", "07_originals", "originals") for p in parts[:-1]):
            add("R1", "%s：原文/原本目录不得入库（L4）" % rel)
            continue
        if re.search(r"(扫描件|扫描版|影印本|scanned|scan[_-]\d|ocr[_-]?\d|ocr版本)", name, re.I) and ext in (".pdf", ".png", ".jpg", ".tif", ".tiff"):
            add("R1", "%s：疑似扫描件/OCR 页面图（L4）" % rel)
            continue
        # R1：PDF 命名里带 arXiv 号（多半是原文）
        if ext == ".pdf" and re.search(r"arXiv|arxiv", name):
            add("R1", "%s：疑似原文 PDF（L4）" % rel)
            continue
        if ALLOW_PDF.match(low):
            continue

        # R3：成品 PDF（台账登记为「随仓公开」的工程放行）
        if ext == ".pdf" and ("成品" in parts[:-1] or "deliverables/成品" in low):
            if any(low.startswith(p + "/") for p in PUBLIC_PROJECTS):
                continue
            add("R3", "%s：成品 PDF 不得入库，改用 Release 外链或申请获取" % rel)
            continue
        if ext == ".pdf" and name == "main.pdf":
            add("R3", "%s：编译产物 main.pdf 不得入库（可由源码重建）" % rel)
            continue
        if ext == ".pdf" and ("/源码/" in low or low.startswith("08_source_code")) and name in ("main.pdf",):
            add("R3", "%s：编译产物不得入库" % rel)
            continue

        # 大 PDF 提示（非阻断）
        if ext == ".pdf":
            size = os.path.getsize(rel)
            if size > 3 * 1024 * 1024 and "papers/" not in low:
                warn("%s：%.1f MB，确认不是整本扫描件" % (rel, size / 1048576))


def check_texts(files):
    link_pat = re.compile(r"raw\.(?:gitcode|githubusercontent|gitee)\.com/\S+?\.pdf", re.I)
    bad_claims = [
        (re.compile(r"全库统一\s*\*{0,2}CC BY 4\.0"), "R4 全库统一 CC BY 4.0（译文不适用）"),
        (re.compile(r"译文[^。\n]{0,20}CC BY 4\.0"), "R4 译文标 CC BY 4.0（越权）"),
        (re.compile(r"欢迎[^。\n]{0,12}(训练|蒸馏)[^。\n]{0,12}商用"), "R4 欢迎训练/商用（对译文越权）"),
        (re.compile(r"已获授权|经作者同意|已取得授权"), "R9 授权表述缺凭证"),
    ]
    for rel in files:
        if not is_text(rel):
            continue
        raw = read_bytes(rel)
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("utf-8", "replace")
        if os.path.basename(rel) not in POLICY_FILES and rel not in POLICY_FILES:
            for m in link_pat.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                add("R2", "%s:%d：原文 PDF 直链不得出现（%s…）" % (rel, line, m.group(0)[:60]))
            for pat, label in bad_claims:
                for m in pat.finditer(text):
                    line = text.count("\n", 0, m.start()) + 1
                    # 只有在同一行也提到译文/语料时才算越权
                    line_txt = text.splitlines()[line - 1] if line - 1 < len(text.splitlines()) else ""
                    if label.startswith("R4") and not re.search(r"译文|译注|语料|成品", line_txt):
                        continue
                    if re.search(r"不适用|不授权|无权|不在本许可|除外|不得|不作|未获", line_txt):
                        continue
                    add(label.split()[0], "%s:%d：%s → %s" % (rel, line, label, line_txt.strip()[:80]))


def check_register(files):
    reg = "RELEASE_REGISTER.csv"
    if reg not in files:
        add("R5", "缺少 RELEASE_REGISTER.csv（台账）")
        return
    rows = {}
    with open(reg, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            rows[r["id"]] = r
    base = "08_source_code"
    for d in sorted(os.listdir(base)):
        if not os.path.isdir(os.path.join(base, d)):
            continue
        pid = d.split("_", 1)[0]
        if pid not in rows:
            add("R5", "08_source_code/%s：未在台账登记" % d)
            continue
        if rows[pid]["状态"] != "合规":
            add("R5", "%s：台账状态=%s，先整改再提交" % (pid, rows[pid]["状态"]))
        if rows[pid]["成品级别"] == "Release 外链" and not rows[pid]["成品直链"].startswith("http"):
            warn("%s：标 Release 外链但无直链" % pid)


def check_pdf_metadata(files):
    """粗查 PDF 是否像扫描件：/Producer 命中文档扫描仪，或全文件几乎无字体。"""
    scanner = re.compile(rb"/Producer\s*\(([^)]{0,120})\)", re.I)
    hints = re.compile(rb"(ScanSnap|Canon|EPSON|Epson|HP Scan|ABBYY|Acrobat.*Scan|CamScanner|KODAK|Fujitsu)", re.I)
    for rel in files:
        if not rel.lower().endswith(".pdf"):
            continue
        head = read_bytes(rel, 65536)
        m = scanner.search(head)
        if m and hints.search(m.group(1)):
            warn("%s：PDF Producer 像扫描仪（%s），请确认非 L4" % (rel, m.group(1).decode("latin-1", "replace")[:60]))


def main():
    all_files = "--all" in sys.argv
    quiet = "--quiet" in sys.argv
    files = git_files(all_files)
    if not quiet:
        print("检查 %d 个文件 …" % len(files))
    check_paths(files)
    check_texts(files)
    check_register(files)
    check_pdf_metadata(files)

    for w in warnings:
        print("WARN", w)
    if violations:
        print("\n违规 %d 项：" % len(violations))
        for kind, msg in violations:
            print("  [%s] %s" % (kind, msg))
        print("\n见 COMPLIANCE.md；修完再提交。")
        sys.exit(1)
    print("\n合规检查通过（%d 条提示）。" % len(warnings))


if __name__ == "__main__":
    main()
