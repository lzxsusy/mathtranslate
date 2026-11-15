import fitz
p = r"<HOME>\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\Ben-Zvi-几何朗兰兹对偶是什么-2026综述.pdf"
doc = fitz.open(p)
for pno in range(len(doc)):
    imgs = doc[pno].get_images(full=True)
    if imgs:
        print(pno+1, [(i[0], i[2], i[3]) for i in imgs])
