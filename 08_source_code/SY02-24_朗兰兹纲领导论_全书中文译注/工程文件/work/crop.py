import sys
from PIL import Image
p,x0,y0,x1,y1 = sys.argv[1], *map(float, sys.argv[2:6])
im = Image.open('pages/ch08/p%s.png'%p)
W,H = im.size
box = (int(x0*W), int(y0*H), int(x1*W), int(y1*H))
im2 = im.crop(box)
sc = float(sys.argv[6]) if len(sys.argv)>6 else 2.0
im2 = im2.resize((int(im2.width*sc), int(im2.height*sc)), Image.LANCZOS)
out = 'crop_%s.png'%p
im2.save(out)
print(out, im2.size)
