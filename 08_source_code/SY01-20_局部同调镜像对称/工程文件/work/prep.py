# -*- coding: utf-8 -*-
"""准备论文分块：抽取原文分片、建立原书页码->源码行映射、统计编号公式块。"""
import io, os, re, json, sys

ROOT = r"<本地路径>"
SRC = r"<本地路径>"
TEXT = r"<本地路径>"

chunks = [
    ("ch00", 171, 214, "1a Statement（Lead 样板）"),
    ("ch01", 215, 364, "1b 多单值 / 1c Hirzebruch 曲面 / 1d 文章结构"),
    ("ch02", 365, 515, "2 定理的证明"),
    ("ch03", 516, 810, "3a A∞-范畴与 dg-范畴 / 3b 模与完美模"),
    ("ch04", 811, 1054, "3c 群作用与轨道范畴 / 3d dg-范畴的张量积"),
    ("ch05", 1055, 1300, "4a 带群作用的 Weinstein 扇区（前半）"),
    ("ch06", 1301, 1478, "4a 后半 / 4b 商空间的缠绕 Fukaya 范畴 / 4c Künneth / 4d Kartal 修改"),
    ("ch07", 1805, 2169, "5a G-等变层"),
    ("ch08", 2170, 2670, "5b 特征群作用 / 5c 权空间分解"),
    ("ch09", 2671, 3290, "5d 限制到子群概形 / 5e 群概形作用的乘积"),
    ("ch10", 3291, 3820, "6a 导出 dg-范畴 / 6b 等变 dg-范畴（前）"),
    ("ch11", 3821, 4215, "6b 等变 dg-范畴（后）"),
    ("ch12", 4216, 4655, "6c 扭 Künneth 公式"),
    ("ch13", 4656, 5100, "附录 A Eilenberg-Zilber 收缩（前）"),
    ("ch14", 5101, 5545, "附录 A Eilenberg-Zilber 收缩（后）"),
]

def read_lines(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read().split("\n")

src = read_lines(SRC)
print("source lines:", len(src))

# ---------------- 1) 写分片 ----------------
def strip_comment(line):
    out = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            out.append(line[i:i+2]); i += 2; continue
        if c == "%":
            break
        out.append(c); i += 1
    return "".join(out)

os.makedirs(os.path.join(ROOT, "src", "chunks", "_src"), exist_ok=True)
stats = {}
for name, a, b, title in chunks:
    lines = []
    lines.append("%% ===== %s : 原文 main.tex 第 %d--%d 行（%s）=====" % (name, a, b, title))
    lines.append("%% 本文件是原文 LaTeX 源码的逐行分片（去掉整段注释掉的旧稿），"
                 "仅供翻译时对照；最终译文写到 src/chunks/%s.tex。" % name)
    for ln in range(a, b + 1):
        if ln % 20 == 0:
            lines.append("%% ---- 原文行 %d ----" % ln)
        lines.append(src[ln - 1])
    with io.open(os.path.join(ROOT, "src", "chunks", "_src", name + "_src.tex"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    body = "\n".join(src[a-1:b])
    stats[name] = {
        "chars": len(body),
        "equation": len(re.findall(r"<本地路径>", body)),
        "align": len(re.findall(r"<本地路径>", body)),
        "gather": len(re.findall(r"<本地路径>", body)),
        "multline": len(re.findall(r"<本地路径>", body)),
        "eqnarray": len(re.findall(r"<本地路径>", body)),
        "thm_envs": len(re.findall(r"<本地路径>?:thm|dfn|defn|prp|prop|crl|cor|conj|nota|ques|exmp|example|lmm|lemma|rmk|cnv|exer)\}", body)),
        "display_bracket": len(re.findall(r"\\\[", body)),
    }

# ---------------- 2) 页码 -> 源码行 映射 ----------------
# 展平源码为「散文词 -> 行号」序列
def flatten_source(lines):
    toks = []
    for no, raw in enumerate(lines, 1):
        line = strip_comment(raw)
        # 保护命令参数里的普通文字：先删数学模式
        line = re.sub(r"\\\[.*?\\\]", " ", line)
        line = re.sub(r"\$[^$]*\$", " ", line)
        # 去掉命令名，保留参数文字
        line = re.sub(r"\\[a-zA-Z@]+\*?", " ", line)
        line = re.sub(r"[{}$&~^_]", " ", line)
        for m in re.finditer(r"[A-Za-z][A-Za-z\-']{1,}", line):
            toks.append((m.group(0).lower(), no))
    return toks

stoks = flatten_source(src)

def norm_words(s):
    s = s.lower()
    words = re.findall(r"[a-z][a-z\-']{1,}", s)
    return words

# 读 PDF 页文本
pages = []
cur = None
for line in read_lines(TEXT):
    m = re.match(r"===== PDF PAGE (\d+) =====", line)
    if m:
        cur = {"page": int(m.group(1)), "lines": []}
        pages.append(cur)
    elif cur is not None:
        cur["lines"].append(line)
print("pdf pages:", len(pages))

ptoks = []   # (word, page_index, char_offset_in_page_text)
for pi, pg in enumerate(pages):
    txt = "\n".join(pg["lines"])
    for m in re.finditer(r"[A-Za-z][A-Za-z\-']{1,}", txt):
        ptoks.append((m.group(0).lower(), pi))

# 顺序对齐：对每页取前 8 个词做 5-gram 匹配，在源码 token 序列中找位置
match_line = {}
ptr = 0
for pi in range(len(pages)):
    words = [w for (w, p) in ptoks if p == pi][:10]
    if len(words) < 4:
        continue
    found = None
    for start in range(0, max(1, len(words) - 4)):
        pat = words[start:start+5]
        # 在 ptr 之后找最长的连续 5 词匹配
        j = ptr
        while j < len(stoks) - 4:
            if all(stoks[j+k][0] == pat[k] for k in range(5)):
                found = j
                break
            j += 1
        if found is not None:
            break
    if found is None:
        print("WARN: page", pages[pi]["page"], "unmatched", words)
        continue
    match_line[pages[pi]["page"]] = stoks[found][1]
    ptr = found + 5

# 输出映射
with io.open(os.path.join(ROOT, "work", "page_map.tsv"), "w", encoding="utf-8", newline="\n") as f:
    f.write("pdf_page\tsource_line\tanchor_text\n")
    for pg in pages:
        p = pg["page"]
        snippet = " ".join(pg["lines"][:2])[:110].replace("\t", " ")
        f.write("%d\t%s\t%s\n" % (p, match_line.get(p, ""), snippet))

# 每分片的页码锚点
for name, a, b, title in chunks:
    rows = [(p, l) for p, l in sorted(match_line.items()) if a <= l <= b]
    with io.open(os.path.join(ROOT, "src", "chunks", "_src", name + "_pages.txt"), "w",
                 encoding="utf-8", newline="\n") as f:
        for p, l in rows:
            pg = pages[p-1]
            snippet = " ".join(pg["lines"][:3])[:130].replace("\n", " ")
            f.write("原书第 %d 页起于源码第 %d 行：%s\n" % (p, l, snippet))

with io.open(os.path.join(ROOT, "work", "chunk_stats.json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(stats, f, ensure_ascii=False, indent=1)

# 控制台只输出 ASCII
print(json.dumps({k: v["chars"] for k, v in stats.items()}))
print("mapped pages:", len(match_line), "of", len(pages))
