from PIL import Image
import sys
src = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-14_Hitchin可积系统的量子化与Hecke特征层\工程文件\work\pages"
page, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
im = Image.open(rf"{src}\p{int(page):03d}.png")
c = im.crop((x0, y0, x1, y1))
scale = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = rf"C:\Users\admin\Downloads\_zoom_p{int(page):03d}_{x0}_{y0}.png"
c.save(out)
print(out, c.size)
