import pymupdf, os
p = r"C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\Ben-Zvi-几何朗兰兹对偶是什么-2026综述.pdf"
out = r"C:\Users\admin\Downloads\GL_work\figures"
os.makedirs(out, exist_ok=True)
doc = pymupdf.open(p)
names = {6: "fig1", 10: "fig2", 19: "fig3"}
for pno, name in names.items():
    page = doc[pno-1]
    for img in page.get_images(full=True):
        xref = img[0]
        pix = pymupdf.Pixmap(doc, xref)
        if pix.n - pix.alpha >= 4:
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        # downscale to reasonable width for print (~150 dpi at 12cm => ~700px). keep 1400
        w, h = pix.width, pix.height
        scale = 1400 / max(w, h)
        if scale < 1:
            pix = pymupdf.Pixmap(pix, 0)  # copy
        path = os.path.join(out, name + ".png")
        pix.save(path)
        print(path, pix.width, pix.height, os.path.getsize(path)//1024, "KB")
