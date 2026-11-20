import csv, re, sys, pathlib

BASE = pathlib.Path(r"C:\Users\admin\Downloads\_mirror_review")
SY24 = pathlib.Path(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY01-24_镜像对称（Siebert 讲义中译本）\成品\SY01-24_术语表.md")

def norm(s):
    s = s.strip().lower()
    s = s.replace("–", "-").replace("—", "-").replace("’", "'")
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

ours = {}
with open(BASE / "glossary.tsv", encoding="utf-8") as f:
    for row in csv.DictReader(f, delimiter="\t"):
        en = norm(row["en"])
        if en and en not in ours:
            ours[en] = (row["zh"], row.get("mode", ""))

sy24 = []
for line in SY24.read_text(encoding="utf-8").splitlines():
    if not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 6 or not cells[0].isdigit():
        continue
    sy24.append((cells[1], cells[2], norm(cells[2]), cells[5]))

out_lines = []
same, diff = [], []
for zh_cn, en, en_n, note in sy24:
    hit = None
    if en_n in ours:
        hit = ours[en_n]
    else:
        # try first alternative separated by /
        for alt in re.split(r"/|或", en_n):
            alt = alt.strip()
            if alt and alt in ours:
                hit = ours[alt]
                break
    if hit:
        if hit[0].replace(" ", "") == zh_cn.replace(" ", ""):
            same.append((en, zh_cn))
        else:
            diff.append((en, zh_cn, hit[0], note))
    else:
        same.append((en, zh_cn + "（本次未收）"))

print(f"SY01-24 条目 {len(sy24)}；一致 {len(same)}；差异 {len(diff)}")
for d in diff:
    print("DIFF", d)

only_ours = [e for e in ours if norm(e) not in {s[2] for s in sy24}]
print(f"本次独自收词 {len(only_ours)}")
