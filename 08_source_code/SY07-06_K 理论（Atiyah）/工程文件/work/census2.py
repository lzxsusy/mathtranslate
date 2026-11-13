# -*- coding: utf-8 -*-
import pymupdf, re, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
SRC = r"<本地路径> (M.F.アティヤ Michael Francis Atiyah) (z-library.sk  1lib.sk  z-lib.sk).pdf"
doc = pymupdf.open(SRC)
statre = re.compile(r'(定義|定理|命題|補題|系|例|注意|問題|仮定|記号|公式)\s*([0-9A-C])\s*[.．]\s*(\d+)(?:\s*[.．]\s*(\d+))?')
cnt = collections.Counter()
detail = collections.defaultdict(list)
for i in range(doc.page_count):
    for line in doc[i].get_text("text").split("\n"):
        for m in statre.finditer(line):
            kind, a, b, c = m.group(1), m.group(2), m.group(3), m.group(4)
            num = f"{a}.{b}" + (f".{c}" if c else "")
            cnt[(kind, num)] += 1
            detail[kind].append((num, i + 1))
print("=== statement env counts ===")
for k, v in sorted(cnt.items()):
    print(k, v)
print()
byk = collections.defaultdict(list)
for (kind, num) in cnt:
    byk[kind].append(num)
for k in byk:
    nums = sorted(set(byk[k]), key=lambda s: [int(x) for x in s.split('.')])
    print(f"{k} ({len(nums)}): {', '.join(nums)}")
print()
# 术语出现频度
terms = ["ベクトル束","複素ベクトル束","実ベクトル束","直線束","ファイバー","全空間","底空間","射影","切断","準同型","自己同型",
 "埋め込み","引き戻し","直和","テンソル積","外積","対称","エルミート","計量","コンパクト","可縮","胞体","ホモトピー",
 "ホモロジー","コホモロジー","完全系列","分裂原理","貼り合わせ","周期性","トム","アダムス","作用素","フレドホルム","指数",
 "位相空間","商束","部分束","付加構造","表現環","指標","対称群","巡回群","素数","フィルトレーション","チャーン","クリフォード",
 "係数","準同型写像","同型写像","連続写像","位相","開集合","閉集合","多様体","微分可能","複素構造","実構造","複体","胞体複体",
 "埋め込","引き起こ","誘導","商","核","像","双対","内積","直交","ユニタリ","行列","階数","ランク","元","可換","非可換"]
full = "\n".join(doc[i].get_text("text") for i in range(doc.page_count))
print("=== term freq ===")
for t in terms:
    n = full.count(t)
    print(f"{t}\t{n}")
