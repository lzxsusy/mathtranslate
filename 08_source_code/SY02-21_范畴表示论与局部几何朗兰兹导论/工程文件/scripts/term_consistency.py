"""术语一致性检查：全书（ch01–ch25，排除 ch26 文献）中不得出现已废弃的译法。"""
import io, os, re, sys

root = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "源码", "chunks")

# 被废弃的写法 -> 应使用的写法
FORBIDDEN = {
    "上表示": "余表示（corepresent）",
    "基形式": "基本形式（basic form）",
    "茎存储": "茎承载",
    "D模": "D-模",
    "环群": "环路群",
    "Hecke 特徵層": "Hecke 特征层",
    "射幂零": "射幂幺",
}

# 术语在不同语境下允许出现的英文（白名单，不算未译）
ALLOWED_EN = {"Hecke", "Whittaker", "Kac–Moody", "Verma", "Satake", "Kazhdan–Lusztig",
              "Ran", "Betti", "de Rham", "étale", "oper", "dg", "QCoh", "IndCoh",
              "LocSys", "Op", "Bun", "DGCat", "Borel", "Levi", "Lang", "Frobenius",
              "Morita", "Künneth", "Bar", "Weyl", "Gauss", "Kloosterman", "Stokes",
              "Artin", "GAGA", "Riemann–Hilbert", "Orlov", "Springer", "Grothendieck",
              "Tate", "Chern", "Steinberg", "Shahidi", "Rodier", "Jacquet", "Moy–Prasad",
              "Zelevinsky", "Lusztig", "Vogan", "Bezrukavnikov", "Finkelberg", "Arakawa",
              "Skryabin", "Wakimoto", "Raskin", "Beraldo", "Nadler", "Ben-Zvi",
              "Gunningham", "Orem", "Sakellaridis", "Venkatesh", "Arinkin", "Gaitsgory",
              "Dhillon", "Feigin", "Frenkel", "Kac", "Iwahori", "Temp", "Casselman",
              "Shalika", "Kashiwara", "Tanisaki", "Mirković", "Vilonen", "Drinfeld",
              "Beilinson", "Deligne", "Verdier", "Hamilton", "Kostant", "Bernstein"}

def main():
    bad = 0
    files = sorted(f for f in os.listdir(root) if re.fullmatch(r"ch\d\d\.tex", f) and f != "ch26.tex")
    for f in files:
        s = io.open(os.path.join(root, f), encoding="utf-8").read()
        for wrong, right in FORBIDDEN.items():
            n = s.count(wrong)
            if n:
                bad += n
                print("FAIL %s: 「%s」出现 %d 次，应为「%s」" % (f, wrong, n, right))
    if bad == 0:
        print("PASS 术语一致性：%d 个正文章节，未发现废弃译法（检查项 %d 个）" % (len(files), len(FORBIDDEN)))
    return 0 if bad == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
