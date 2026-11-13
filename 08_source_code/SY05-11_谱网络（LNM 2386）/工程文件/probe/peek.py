import pymupdf as fitz, re
SRC=r"<本地路径>"
doc=fitz.open(SRC)
for i in (0,1,2,20,42,43,48,67,111):
    t=doc[i].get_text()
    print("="*20,"p",i+1,"="*20)
    print(t[:1200])