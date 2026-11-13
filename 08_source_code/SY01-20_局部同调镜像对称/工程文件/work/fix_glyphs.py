import glob
import io
import unicodedata

# 1) errata: ✔ -> \checkmark{}
for p in glob.glob(r"<本地路径>*.tex"):
    s = io.open(p, encoding="utf-8").read()
    if "\u2714" in s:
        s = s.replace("\u2714", r"\checkmark{}")
        io.open(p, "w", encoding="utf-8").write(s)
        print("errata fixed", p)

# 2) refs.bib: NFC normalize
p = r"<本地路径>"
s = io.open(p, encoding="utf-8").read()
s2 = unicodedata.normalize("NFC", s)
io.open(p, "w", encoding="utf-8").write(s2)
print("bib nfc changed", s != s2)
