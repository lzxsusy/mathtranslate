r"""生成 chunks/_order_body.tex 与 chunks/_order_app.tex：
按固定块顺序列出所有已交付的片段文件（正文 / 附录分两个文件，便于 main.tex 在两者之间写 \appendix）。
用法：python tools/gen_order.py
命名约定：<块名>-NN.tex（NN 两位数字，NN 从 01 起）。
"""
import sys, io, os, glob, re
sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")

BODY = ["c01", "ch02", "ch03", "ch04", "ch05", "ch06a", "ch06b", "ch07", "ch08", "ch09"]
APP = ["appA", "appB", "appC", "appD"]


def collect(chunks):
    lines = []
    for chunk in chunks:
        files = sorted(glob.glob(os.path.join(CH, f"{chunk}[.-]*.tex")))
        files = [f for f in files if re.fullmatch(rf"{re.escape(chunk)}(-\d\d)?\.tex", os.path.basename(f))]
        for f in files:
            lines.append("\\input{chunks/" + os.path.basename(f)[:-4] + "}")
    return lines


body = collect(BODY)
app = collect(APP)
for name, lines in (("_order_body.tex", body), ("_order_app.tex", app)):
    io.open(os.path.join(CH, name), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + ("\n" if lines else ""))
print(f"_order_body.tex: {len(body)} files; _order_app.tex: {len(app)} files")
for l in body + app:
    print("  ", l)
