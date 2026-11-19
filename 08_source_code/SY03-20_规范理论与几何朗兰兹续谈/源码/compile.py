"""Build the Chinese paper with XeLaTeX, makeindex and explicit PDF Unicode maps."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parent
BUILD = ROOT
FINAL = ROOT / "Witten_Geometric_Langlands_ZH.pdf"


def digest(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def run(command: list[str], log: Path | None = None):
    if log is None:
        result = subprocess.run(command, cwd=ROOT)
    else:
        with log.open("w", encoding="utf-8") as stream:
            result = subprocess.run(command, cwd=ROOT, stdout=stream,
                                    stderr=subprocess.STDOUT, text=True)
        if result.returncode:
            print(log.read_text(encoding="utf-8", errors="replace")[-16000:])
    if result.returncode:
        raise SystemExit(result.returncode)


def wait_for_stable_files(paths, validator, label, timeout=30.0):
    """Do not read a new TeX pass or PDF while output files are still changing."""
    deadline = time.monotonic() + timeout
    previous = None
    stable_since = None
    while time.monotonic() < deadline:
        try:
            signature = tuple(
                (path.stat().st_size, path.stat().st_mtime_ns) if path.exists() else None
                for path in paths
            )
            valid = validator()
        except (OSError, RuntimeError, ValueError):
            signature, valid = None, False
        if valid and signature == previous:
            if stable_since is not None and time.monotonic() - stable_since >= 1.0:
                return
        else:
            stable_since = time.monotonic() if valid else None
        previous = signature
        time.sleep(0.25)
    raise SystemExit(f"{label} 未在 {timeout:g} 秒内完成写入；请检查编译日志.")


def wait_for_tex_outputs():
    paths = [ROOT / f"main.{extension}"
             for extension in ("xdv", "aux", "toc", "brf", "idx", "out")]

    def complete():
        auxiliary = (ROOT / "main.aux").read_bytes()
        with (ROOT / "main.xdv").open("rb") as stream:
            stream.seek(-4, 2)
            ending = stream.read()
        return b"\\@abspage@last{" in auxiliary[-512:] and ending == b"\xdf" * 4

    wait_for_stable_files(paths, complete, "XeLaTeX 输出")


def wait_for_pdf(path):
    import fitz

    def complete():
        data = path.read_bytes()
        if not data.startswith(b"%PDF-") or b"%%EOF" not in data[-1024:]:
            return False
        with fitz.open(path) as document:
            return document.page_count > 0 and not document.is_repaired

    wait_for_stable_files([path], complete, "PDF 文件")


def check_environment(tex_only: bool):
    if sys.version_info < (3, 10):
        raise SystemExit("需要 Python 3.10 或更新版本.")
    for command in ("xelatex", "makeindex", "xdvipdfmx"):
        if shutil.which(command) is None:
            raise SystemExit(f"未找到 {command}. 请安装完整 TeX Live，并将其可执行文件加入 PATH.")
    required = ("fitz",) if tex_only else ("fitz", "pypdf", "fontTools")
    missing = [name for name in required if importlib.util.find_spec(name) is None]
    if missing:
        raise SystemExit(
            "缺少 PDF 核验或 Unicode 补全依赖. 请先运行：\n"
            "python -m pip install -r unicode_tools/requirements.txt"
        )
    manifest = json.loads((ROOT / "fonts/font_manifest.json").read_text(encoding="utf-8"))
    for font in manifest["fonts"]:
        if digest(ROOT / font["file"]) != font["sha256"]:
            raise SystemExit(f"字体文件缺失或已更改：{font['file']}")


def compile_document():
    BUILD.mkdir(exist_ok=True)
    previous = None
    last_index = None
    for iteration in range(1, 9):
        run(["xelatex", "-no-pdf", "-no-shell-escape", "-interaction=nonstopmode",
             "-halt-on-error", "-file-line-error", "-recorder",
             "main.tex"],
            BUILD / f"main-build-{iteration}.txt")
        wait_for_tex_outputs()
        index = BUILD / "main.idx"
        index_hash = digest(index)
        index_updated = False
        if index.exists() and index.stat().st_size and index_hash != last_index:
            run(["makeindex", "-s", "index.ist", "-o", "main.ind",
                 "-t", "main.ilg", "main.idx"],
                BUILD / "main-makeindex.txt")
            ind = ROOT / "main.ind"
            wait_for_stable_files(
                [ind], lambda: ind.read_bytes().rstrip().endswith(b"\\end{theindex}"),
                "索引文件"
            )
            last_index = index_hash
            index_updated = True
        state = tuple(digest(BUILD / f"main.{extension}")
                      for extension in ("aux", "toc", "brf", "idx", "out"))
        print(f"XeLaTeX 第 {iteration} 轮已完成.", flush=True)
        if iteration >= 2 and state == previous and not index_updated:
            print("目录、交叉引用、参考文献回链和索引页码已稳定.", flush=True)
            break
        previous = state
    else:
        raise SystemExit("八轮编译后引用仍未收敛，请检查 main.log.")
    complete_pdf = ROOT / "main.complete.pdf"
    if complete_pdf.exists():
        complete_pdf.unlink()
    run(["xdvipdfmx", "-o", complete_pdf.name, "main.xdv"],
        ROOT / "main-dvipdfmx.txt")
    wait_for_pdf(complete_pdf)
    complete_pdf.replace(ROOT / "main.pdf")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex-only", action="store_true",
                        help="仅编译 main.pdf，跳过 PDF Unicode 补全")
    parser.add_argument("--verify-render", action="store_true",
                        help="补全后逐页核验渲染像素完全不变")
    arguments = parser.parse_args()
    check_environment(arguments.tex_only)
    compile_document()
    if arguments.tex_only:
        print("已生成 main.pdf.")
        return
    command = [sys.executable, "unicode_tools/add_unicode_maps.py",
               "main.pdf", FINAL.name]
    if arguments.verify_render:
        command.append("--verify-render")
    run(command)
    print(f"已生成 {FINAL.name}")


if __name__ == "__main__":
    main()
