# -*- coding: utf-8 -*-
"""Extract page-marked text from the survey's source PDFs for verification."""
import pathlib, sys
import pymupdf

ROOT = pathlib.Path(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi")
OUT = pathlib.Path(__file__).parent

BOOKS = {
    "SCH26": ROOT / "08_source_code/SY02-45_Scholze布尔巴基1252几何Langlands的证明/成品/SY02-45_Scholze布尔巴基1252几何Langlands的证明_中译注本.pdf",
    "CL23": ROOT / "08_source_code/SY02-33_几何Langlands理论导论（陈麟）_中文译注校订版/成品/几何Langlands理论导论（陈麟）_中文译注校订版.pdf",
    "LAU02": ROOT / "08_source_code/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应/成品/SY02-46_Laumon布尔巴基906Drinfeld-Langlands对应_中译注本.pdf",
    "RAS23": ROOT / "08_source_code/SY02-47_Raskin射影曲线上的几何Langlands讲义/成品/SY02-47_Raskin射影曲线上的几何Langlands讲义_中译注本.pdf",
}

for tag, path in BOOKS.items():
    if not path.exists():
        print(tag, "MISSING", path)
        continue
    doc = pymupdf.open(path)
    parts = []
    for i, page in enumerate(doc, 1):
        parts.append(f"\n===== PAGE {i} =====\n")
        parts.append(page.get_text("text"))
    out = OUT / f"{tag}.txt"
    out.write_text("".join(parts), encoding="utf-8")
    print(tag, len(doc), "pages ->", out.name, out.stat().st_size, "bytes")
