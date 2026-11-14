# -*- coding: utf-8 -*-
"""按《校订规范（v2）术语与译名规则》批量统一全书术语。

规则要点：
  * wrapped / thimble / stop 等专业术语保留英文；
  * 托里克簇 -> 环簇（toric variety 的通行中文名）；
  * 充足 / 非常充足 -> 丰富 / 极丰富（ample / very ample）；
  * exact（辛几何语境，仅第 6 章）统一作“正合”，与第 8、9 章一致；
  * 索引键（\\index{pinyin@显示}）与 index-terms.tsv 同步改写。

用法： python tools/apply_term_policy.py [--dry-run]
"""
import os
import re
import shutil
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(BASE, "chapters")

CJK = r"[\u4e00-\u9fff]"

# 1) 索引键优先改写（避免显示名替换后键与显示名不一致）
INDEX_MAP = [
    ("tuolikecu@托里克簇", "huanzu@环簇"),
    ("tuolikechuzi@托里克除子", "huanzuchuzi@环簇除子"),
    ("lefschetzzhangpeng@Lefschetz 帐篷", "lefschetzthimble@Lefschetz thimble"),
    ("juanraofukayafanchou@卷绕 Fukaya 范畴", "wrappedfukayafanchou@wrapped Fukaya 范畴"),
    ("bufenjuanraofukayafanchou@部分卷绕 Fukaya 范畴",
     "partiallywrappedfukayafanchou@partially wrapped Fukaya 范畴"),
    ("tingzhizi@停止子", "stop@stop"),
    ("qiandangxinliuxing@恰当辛流形", "zhenghexinliuxing@正合辛流形"),
    ("qiandanglagelangriziliuxing@恰当拉格朗日子流形",
     "zhenghelagelangriziliuxing@正合拉格朗日子流形"),
    ("qiandangfukayafanchou@恰当 Fukaya 范畴", "zhenghefukayafanchou@正合 Fukaya 范畴"),
    ("feichangchongzu@非常充足", "jifengfu@极丰富"),
    ("chongzu@充足", "fengfu@丰富"),
]

# 2) 正文替换（按顺序执行，长词先于短词）
TEXT_MAP = [
    ("部分卷绕", "partially wrapped"),
    ("完全卷绕", "fully wrapped"),
    ("卷绕", "wrapped"),
    ("Lefschetz 帐篷", "Lefschetz thimble"),
    ("消失帐篷", "thimble"),
    ("帐篷", "thimble"),
    ("停止子", "stop"),
    ("非常充足", "极丰富"),
    ("充足", "丰富"),
    ("托里克除子", "环簇除子"),
    ("托里克簇", "环簇"),
    ("托里克几何", "环簇几何"),
    ("托里克紧化", "环簇紧化"),
    ("托里克消解", "环簇消解"),
    ("托里克图", "环簇图"),
    ("托里克层", "环簇层"),
    ("托里克情形", "环簇情形"),
    ("非托里克", "非环簇"),
    ("托里克", "环簇"),
    ("曲弯范畴", "弯曲范畴"),
    ("坐标角色", "坐标特征标"),
]

CH06_MAP = [("恰当", "正合")]

SPACED = ["thimble", "wrapped", "stop"]


def add_spaces(s):
    for w in SPACED:
        s = re.sub(r"(?<=%s)(%s)" % (CJK, w), r" \1", s)
        s = re.sub(r"(%s)(?=%s)" % (w, CJK), r"\1 ", s)
    return s


def main():
    dry = "--dry-run" in sys.argv
    backup = os.path.join(BASE, "work", "backup_chapters")
    os.makedirs(backup, exist_ok=True)

    hits = []
    for name in sorted(os.listdir(CH)):
        if not name.endswith(".tex"):
            continue
        path = os.path.join(CH, name)
        raw = open(path, encoding="utf-8").read()
        rules = INDEX_MAP + TEXT_MAP + (CH06_MAP if name == "ch06.tex" else [])
        s = raw
        for a, b in rules:
            c = s.count(a)
            if c:
                hits.append((name, a, b, c))
            s = s.replace(a, b)
        s = add_spaces(s)
        if s != raw and not dry:
            shutil.copyfile(path, os.path.join(backup, name))
            open(path, "w", encoding="utf-8").write(s)

    for name, a, b, c in hits:
        print("%-10s %-22s -> %-24s %d" % (name, a, b, c))
    print("files changed:", len({h[0] for h in hits}), "| mode:", "dry-run" if dry else "written")


if __name__ == "__main__":
    main()
