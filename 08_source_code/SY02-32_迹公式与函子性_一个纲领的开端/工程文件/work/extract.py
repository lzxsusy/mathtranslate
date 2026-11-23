# -*- coding: utf-8 -*-
"""把底本 PDF 逐页抽成带页标记的纯文本，并修补 pdfTeX 分解重音（´e -> é）。"""
import re, sys, unicodedata
import pymupdf

SRC = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\44_Frenkel-Ngo-Langlands_1003.4578.pdf"
OUT = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-32_迹公式与函子性_一个纲领的开端\工程文件\work\fulltext.txt"

ACC = {"\u00b4": {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú", "y": "ý", "A": "Á", "E": "É", "I": "Í", "O": "Ó", "U": "Ú"},
       "`": {"a": "à", "e": "è", "i": "ì", "o": "ò", "u": "ù", "A": "À", "E": "È", "I": "Ì", "O": "Ò", "U": "Ù"},
       "\u02c6": {"a": "â", "e": "ê", "i": "î", "o": "ô", "u": "û", "A": "Â", "E": "Ê", "I": "Î", "O": "Ô", "U": "Û"},
       "\u02dc": {"a": "â", "e": "ê", "i": "î", "o": "ô", "u": "û", "n": "ñ", "N": "Ñ"},
       "\u00a8": {"a": "ä", "e": "ë", "i": "ï", "o": "ö", "u": "ü", "A": "Ä", "E": "Ë", "I": "Ï", "O": "Ö", "U": "Ü"},
       "\u00b8": {"c": "ç", "C": "Ç"}}

def fix_accents(s):
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in ACC and i + 1 < len(s) and s[i+1] in ACC[ch]:
            out.append(ACC[ch][s[i+1]]); i += 2
        else:
            out.append(ch); i += 1
    s = "".join(out)
    return unicodedata.normalize("NFC", s)

def main():
    doc = pymupdf.open(SRC)
    parts = []
    for no, page in enumerate(doc, start=1):
        txt = page.get_text("text")
        parts.append(f"\n===== BOOK PAGE {no} (PDF {no}) =====\n" + fix_accents(txt))
    open(OUT, "w", encoding="utf-8").write("".join(parts))
    print("pages:", doc.page_count, "chars:", sum(len(p) for p in parts))

if __name__ == "__main__":
    main()
