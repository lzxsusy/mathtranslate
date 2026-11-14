#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把工程打包到桌面交付目录。"""
import os
import shutil
import sys
from pathlib import Path

QSG = Path(__file__).resolve().parent.parent
DESKTOP = Path(os.path.expanduser("~")) / "Desktop"
DST = DESKTOP / "量化辛几何导引_中文译注版"


def copy_tree(src: Path, dst: Path, patterns=("*",)):
    dst.mkdir(parents=True, exist_ok=True)
    for p in sorted(src.glob("*")):
        if p.name in ("build", "__pycache__"):
            continue
        if p.is_file():
            shutil.copy2(p, dst / p.name)
        elif p.is_dir():
            shutil.copytree(p, dst / p.name, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("__pycache__"))


def main():
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)
    shutil.copy2(QSG / "main.tex", DST / "main.tex")
    shutil.copy2(QSG / "preamble.tex", DST / "preamble.tex")
    shutil.copy2(QSG / "README.md", DST / "README.md")
    copy_tree(QSG / "tex", DST / "tex")
    copy_tree(QSG / "figures", DST / "figures")
    copy_tree(QSG / "tools", DST / "tools")
    copy_tree(QSG / "审校记录", DST / "审校记录")
    shutil.copy2(QSG / "notes" / "GLOSSARY.md", DST / "审校记录" / "术语表_GLOSSARY.md")
    shutil.copy2(QSG / "main.pdf", DST / "量化辛几何导引_中文译注版.pdf")
    n_fig = len(list((DST / "figures").glob("*.png")))
    total = sum(p.stat().st_size for p in DST.rglob("*") if p.is_file())
    print(f"交付目录: {DST}")
    print(f"文件数: {sum(1 for p in DST.rglob('*') if p.is_file())}  图: {n_fig}  总大小: {total/1024/1024:.1f} MiB")
    print(f"PDF: {DST/'量化辛几何导引_中文译注版.pdf'}")


if __name__ == "__main__":
    main()
