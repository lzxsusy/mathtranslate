# -*- coding: utf-8 -*-
"""把新装工具加入用户 PATH（幂等：已存在则跳过；保留顺序，去重）。
同时把真实 Python 放到 WindowsApps 之前，避免 `python` 命中 Store stub。"""
import os, sys
sys.stdout.reconfigure(encoding="utf-8")

ADD = [
    r"<本地路径>",
    r"<本地路径>",
    r"<本地路径>",
    r"C:\Program Files\qpdf 12.4.2\bin",
]
PRIORITY = [
    r"<本地路径> Harness\resources\runtime\cli\bin",
]

old = os.environ.get("PATH", "")
user = os.environ.get("PATH", "")
# 读取注册表里的用户 PATH（不是合并后的）
import winreg
with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
    try:
        upath, typ = winreg.QueryValueEx(k, "Path")
    except FileNotFoundError:
        upath, typ = "", winreg.REG_EXPAND_SZ

parts = [p for p in upath.split(";") if p.strip()]
lower = {p.lower() for p in parts}

new_parts = []
for p in PRIORITY:
    if p.lower() not in lower:
        new_parts.append(p)
        lower.add(p.lower())
for p in ADD:
    if p.lower() not in lower:
        new_parts.append(p)
        lower.add(p.lower())
# 其余保持原顺序
for p in parts:
    if p not in new_parts:
        new_parts.append(p)

newpath = ";".join(new_parts)
with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE) as k:
    winreg.SetValueEx(k, "Path", 0, winreg.REG_EXPAND_SZ, newpath)
print("user PATH updated:")
for p in new_parts:
    print("  ", p)
