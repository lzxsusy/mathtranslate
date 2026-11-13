import pymupdf as fitz, re
doc=fitz.open(r"<本地路径>")
for i in (184,185,186,187):
    t=doc[i].get_text()
    print("="*20,"PDF p",i+1,"="*20)
    print(t[-1500:])
    print("tags found:", re.findall(r"\((\d+\.\d+)\)", t))