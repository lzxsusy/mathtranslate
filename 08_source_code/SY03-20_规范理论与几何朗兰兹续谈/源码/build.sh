#!/usr/bin/env sh
set -eu
PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$PROJECT_DIR"
if command -v python3 >/dev/null 2>&1; then
    exec python3 compile.py "$@"
fi
exec python compile.py "$@"
