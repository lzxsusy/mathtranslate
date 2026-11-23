"""把中文译文语料打包进插件：01_corpus_zh/zh_paragraphs.jsonl -> plugins/dsh-kb/data/zh/*.gz

为什么单独一个脚本：译文层是仓库里最大的数据集（4.9 万段、33 MB），
插件包只带 gz；源文件仍以仓库里的 jsonl 为准。
打包时只留检索与阅读用得上的字段（去掉 para_id/flags/seg/file 里的冗余），
mtime=0 让同样的输入总是打出同样的字节，便于核对发布物。
"""
import gzip
import hashlib
import io
import json
import os

SRC = "01_corpus_zh/zh_paragraphs.jsonl"
OUT_DIR = os.path.join("plugins", "dsh-kb", "data", "zh")
OUT = os.path.join(OUT_DIR, "zh_paragraphs.jsonl.gz")

os.makedirs(OUT_DIR, exist_ok=True)

buf = []
n = 0
seen = set()
for line in io.open(SRC, encoding="utf-8"):
    s = line.strip()
    if not s:
        continue
    r = json.loads(s)
    txt = r.get("text") or ""
    if not txt:
        continue
    t0 = txt.strip()
    key = ("t", r.get("pkg"), t0) if len(t0) >= 40 else ("p", r.get("pkg"), r.get("para"), t0)
    if key in seen:
        continue
    seen.add(key)
    n += 1
    row = {
        "pkg": r.get("pkg") or "?",
        "para": r.get("para"),
        "page_orig": r.get("page_orig"),
        "env": r.get("env") or "text",
        "tier": r.get("tier") or "?",
        "zh_chars": r.get("zh_chars") or len(txt),
        "text": txt,
    }
    if r.get("file"):
        row["file"] = r["file"]
    buf.append(json.dumps(row, ensure_ascii=False))

body = ("\n".join(buf) + "\n").encode("utf-8")
with io.open(OUT, "wb") as fh:
    gz = gzip.GzipFile(filename="", mode="wb", fileobj=fh, mtime=0)
    gz.write(body)
    gz.close()

print("src  : %s  %d 段" % (SRC, n))
print("json : %.1f MB -> out %.2f MB" % (len(body) / 1e6, os.path.getsize(OUT) / 1e6))
print("sha1 : %s" % hashlib.sha1(body).hexdigest()[:16])
