import pymupdf as fitz
doc=fitz.open(r"<本地路径>")
out=[]
for i in range(6,14):
    out.append("="*10+f" PDF p{i+1} "+"="*10)
    out.append(doc[i].get_text())
open(r"<本地路径>","w",encoding="utf-8").write("\n".join(out))
print("ok")