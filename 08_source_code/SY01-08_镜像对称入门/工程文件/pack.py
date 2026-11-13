"""打包七件套到 deliverable/。用法：python pack.py [--no-zip]"""
import sys, csv, shutil, zipfile, pathlib, datetime
sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(r"<本地路径>")
DEL = ROOT / "deliverable"
TAG = "JPB08"          # 正式编号（原 JPB07 已被《双有理幾何学》占用）
SHORT = "镜像对称入门"
PDF_SRC = ROOT / "src" / "main.pdf"


def copy(src, dst):
    if not src.exists():
        print("MISSING", src)
        return None
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"  {dst.name:46s} {dst.stat().st_size:>9,d} B")
    return dst


def export_glossary():
    """glossary.tsv → deliverable/术语表_日汉对照.csv（同步一份 md 表）"""
    src = ROOT / "work" / "glossary.tsv"
    rows, group = [], ""
    for line in src.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        if line.startswith("#"):
            t = line.lstrip("# ").strip()
            if t and not t.startswith("格式") and not t.startswith("维护") and not t.startswith("判定") and not t.startswith("拆条") and not t.startswith("说明列"):
                group = t
            continue
        parts = line.split("\t")
        while len(parts) < 3:
            parts.append("")
        rows.append([group, parts[0].strip(), parts[1].strip(), parts[2].strip()])
    out = DEL / "术语表_日汉对照.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["分组", "日文（含 OCR 变体）", "中文译名", "说明"])
        w.writerows(rows)
    print(f"  {out.name:46s} {out.stat().st_size:>9,d} B  ({len(rows)} 条)")
    return len(rows)


def main(no_zip=False):
    DEL.mkdir(parents=True, exist_ok=True)
    print("== 打包七件套 ==")
    # 1. 成品 PDF
    if PDF_SRC.exists():
        copy(PDF_SRC, DEL / f"{SHORT}_中文译注本.pdf")
    # 2. 源码
    src_zip = DEL / f"{TAG}_{SHORT}_源码.zip"
    if not no_zip:
        with zipfile.ZipFile(src_zip, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted((ROOT / "src").rglob("*")):
                if p.is_file() and p.suffix in {".tex", ".png", ".jpg", ".pdf"}:
                    z.write(p, p.relative_to(ROOT).as_posix())
        print(f"  {src_zip.name:46s} {src_zip.stat().st_size:>9,d} B")
    # 3-6. 文档
    for name in ["译注汇总.md", "README.md", "阅读参考指南.md", "工程总结.md"]:
        copy(ROOT / name, DEL / name)
    # 7. 术语表
    n = export_glossary()
    # 清单
    files = sorted(p for p in DEL.iterdir() if p.is_file())
    man = DEL / "交付清单.md"
    lines = [f"# 交付清单 · {TAG}《{SHORT}》中文译注本", "",
             f"生成时间：{datetime.datetime.now():%Y-%m-%d %H:%M}", "",
             "| 文件 | 大小 |", "|---|---:|"]
    for p in files:
        lines.append(f"| {p.name} | {p.stat().st_size:,} B |")
    lines += ["", f"术语表 {n} 条。", ""]
    man.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n共 {len(files) + 1} 个文件在 {DEL}")


if __name__ == "__main__":
    main(no_zip="--no-zip" in sys.argv)
