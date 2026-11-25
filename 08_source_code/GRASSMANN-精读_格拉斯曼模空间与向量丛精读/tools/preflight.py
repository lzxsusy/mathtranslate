# -*- coding: utf-8 -*-
"""开工前自检：文件齐不齐、PDF 页数对不对、页表会不会漂、工具在不在。

    python tools\\preflight.py            # 结果打到 stdout，并写 preflight.txt
退出码 0 = 全 OK；1 = 有 FAIL（先修再开工）。

检查项都写死在本文件里，改 BRIEF 页表时同步改 CH。
"""
import os
import sys
import io
import hashlib
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PY = sys.executable
CH = {
    1: ("ch01", (7, 29), (10, 33), "Hitchin"),
    2: ("ch02", (30, 54), (34, 59), "Koszul"),
    3: ("ch03", (55, 71), (60, 77), "Reider"),
    4: ("ch04", (72, 81), (78, 89), "相交"),
    5: ("ch05", (82, 93), (90, 103), "Beilinson"),
    6: ("ch06", (94, 115), (104, 129), "算术"),
    7: ("ch07", (116, 134), (130, 149), "凝聚系"),
    8: ("ch08", (135, 159), (150, 177), "Regularity"),
    9: ("ch09", (160, 170), (178, 189), "可约曲线"),
}
ZH_MD5 = "eecebd77c68cea9f75c91d66c5cb2ef5"

lines = []
fails = []


def ok(msg):
    lines.append("[ OK ] " + msg)


def fail(msg):
    lines.append("[FAIL] " + msg)
    fails.append(msg)


def info(msg):
    lines.append("[ -- ] " + msg)


# 1. 文件

need = ["BRIEF.md", "STATUS.md", "zh-译文.pdf", os.path.join("original", "en-原书.pdf"),
        os.path.join("source", "main.tex"), os.path.join("source", "TERMINOLOGY.md"),
        os.path.join("source", "PROGRESS.md"),
        os.path.join("source", "chapters", "frontmatter.tex"),
        os.path.join("tools", "pdf_pages.py")]
for i in range(1, 10):
    need.append(os.path.join("source", "chapters", "ch%02d.tex" % i))
missing = [p for p in need if not os.path.isfile(os.path.join(ROOT, p))]
if missing:
    fail("缺文件：" + "; ".join(missing))
else:
    ok("输入文件齐全（%d 个）" % len(need))

for d in ["产出/导读", "产出/批注", "产出/笔记", "产出/汇总", "产出/_pages", "tmp"]:
    p = os.path.join(ROOT, *d.split("/"))
    os.makedirs(p, exist_ok=True)
ok("产出目录与 tmp 就绪")

# 2. PDF 页数与 md5

try:
    import pymupdf as fitz
except ImportError:
    try:
        import fitz
    except ImportError:
        fitz = None
        fail("pymupdf 不可用（import 失败）")

zh_pdf = os.path.join(ROOT, "zh-译文.pdf")
en_pdf = os.path.join(ROOT, "original", "en-原书.pdf")
if fitz and os.path.isfile(zh_pdf) and os.path.isfile(en_pdf):
    zd = fitz.open(zh_pdf)
    ed = fitz.open(en_pdf)
    if zd.page_count == 170:
        ok("zh-译文.pdf 170 页")
    else:
        fail("zh-译文.pdf 页数 %d ≠ 170" % zd.page_count)
    if ed.page_count == 190:
        ok("en-原书.pdf 190 页")
    else:
        fail("en-原书.pdf 页数 %d ≠ 190" % ed.page_count)

    h = hashlib.md5()
    with open(zh_pdf, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    md5 = h.hexdigest()
    if md5 == ZH_MD5:
        ok("zh-译文.pdf md5 与 PROGRESS 记录一致")
    else:
        info("zh-译文.pdf md5 = %s（PROGRESS 记 %s；若 PDF 被重编译过属正常，但页表要复核）" % (md5, ZH_MD5))

    # 3. 页表漂移：每章首页文本里应有该章的标志性字样
    drift = 0
    for n, (tex, zh, en, probe) in CH.items():
        p = zd[zh[0] - 1]
        t = p.get_text()
        if probe.lower() in t.lower():
            continue
        # 有的章首页只有标题、正文在次页
        t2 = zd[min(zh[0], zd.page_count - 1)].get_text()
        if probe.lower() in t2.lower():
            info("ch%d 首页未见 %r，次页命中（可接受，抽一张图确认）" % (n, probe))
        else:
            fail("ch%d 页表可能漂移：中译 p.%d/%d 都找不到 %r" % (n, zh[0], zh[0] + 1, probe))
            drift += 1
    if drift == 0:
        ok("9 章首页探针全部命中（页表未漂）")
else:
    info("跳过 PDF 检查")

# 4. 外部工具

pandoc = r"C:\Users\admin\AppData\Local\Pandoc\pandoc.exe"
if os.path.isfile(pandoc):
    try:
        v = subprocess.run([pandoc, "--version"], capture_output=True, text=True, timeout=30)
        ok("pandoc: " + v.stdout.splitlines()[0].strip())
    except Exception as e:  # noqa: BLE001
        info("pandoc 存在但调用失败: %r" % (e,))
else:
    info("pandoc 不在默认路径（Phase 4 的 docx 汇编会跳过，md 仍可交付）")

xelatex = r"C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"
info("xelatex %s（本轮不需要编译，本地编译结论不作数）" % ("可用" if os.path.isfile(xelatex) else "缺失"))

# 5. 章源文件规模（太小说明解压不全）

sizes = []
for n, (tex, zh, en, probe) in CH.items():
    p = os.path.join(ROOT, "source", "chapters", tex + ".tex")
    s = os.path.getsize(p) if os.path.isfile(p) else 0
    sizes.append("ch%d=%dB" % (n, s))
    if s < 20000:
        fail("ch%d 源文件仅 %d 字节，可疑" % (n, s))
if not any(f.startswith("ch") and "字节" in f for f in fails):
    ok("9 章源文件规模正常（" + ", ".join(sizes) + "）")

# 6. 卡片库

cards = os.path.join(os.path.dirname(ROOT), "_cards_grassmann")
if os.path.isdir(cards):
    ok("_cards_grassmann 存在")
else:
    fail("_cards_grassmann 缺失（Phase 3 要写到这里）")

# 7. 已有译注清单（章读者靠它避免重复登记）
notes = os.path.join(ROOT, "产出", "汇总", "existing-notes.tsv")
if os.path.isfile(notes):
    n = sum(1 for _ in open(notes, encoding="utf-8")) - 1
    if n == 81:
        ok("existing-notes.tsv 81 条（已有译注，不许重复登记）")
    else:
        fail("existing-notes.tsv 只有 %d 条，应为 81；重跑 tools\\extract_existing_notes.py" % n)
else:
    fail("existing-notes.tsv 缺失；先跑 tools\\extract_existing_notes.py")

head = "格拉斯曼精读工程 · preflight"
out = [head, "=" * 60] + lines + ["=" * 60,
      "结论：%d 个 FAIL" % len(fails)]
if fails:
    out += ["修复建议见 BRIEF.md §2 / §10"]
text = "\n".join(out) + "\n"
with open(os.path.join(ROOT, "preflight.txt"), "w", encoding="utf-8", newline="\n") as f:
    f.write(text)
print(text)
sys.exit(1 if fails else 0)
