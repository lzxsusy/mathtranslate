#!/usr/bin/env python3
"""Use the installed Biber, with a local workaround for broken macOS fat binaries."""
from pathlib import Path
import os, platform, shutil, subprocess, sys, tempfile
binary=shutil.which("biber")
if not binary:
    raise SystemExit("Biber is required but is not installed")
probe=subprocess.run([binary,"--version"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
if probe.returncode and sys.platform=="darwin":
    architecture="arm64" if platform.machine()=="arm64" else "x86_64"
    cache=Path(tempfile.gettempdir()) / f"dirichlet-biber-{os.getuid()}-{architecture}"
    if not cache.is_file():
        subprocess.run(["lipo",binary,"-thin",architecture,"-output",str(cache)],check=True)
        cache.chmod(0o700)
    binary=str(cache)
raise SystemExit(subprocess.call([binary,*sys.argv[1:]]))
