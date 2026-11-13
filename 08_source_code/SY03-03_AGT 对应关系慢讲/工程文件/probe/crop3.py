import sys, os
sys.stdout.reconfigure(encoding="utf-8")
import pymupdf as fitz
doc = fitz.open(r"<本地路径>).pdf")
FIG = r"<本地路径>"
CLIPS = {
    1: (7,  fitz.Rect(120, 82, 475, 169)),
    2: (19, fitz.Rect(228, 80, 368, 224)),
    3: (56, fitz.Rect(160, 92, 440, 237)),
    4: (79, fitz.Rect(90, 82, 508, 205)),
    5: (80, fitz.Rect(193, 88, 392, 163)),
}
for fig,(pg,clip) in CLIPS.items():
    p=doc[pg-1]
    pix=p.get_pixmap(dpi=400, clip=clip)
    pix.save(os.path.join(FIG,f"fig{fig}.png"))
    print(fig,pg,pix.width,pix.height)
