#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from pathlib import Path

import uvicorn


def _inject_repo_root() -> None:
    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        if (parent / "app" / "api.py").exists():
            sys.path.insert(0, str(parent))
            return


_inject_repo_root()


def _prefer_local_venv_python() -> None:
    here = Path(__file__).resolve()
    venv_python = here.parent.parent / ".venv" / "bin" / "python3"
    if not venv_python.exists():
        return
    current = Path(sys.executable)
    if current == venv_python:
        return
    os.execv(str(venv_python), [str(venv_python), str(here), *sys.argv[1:]])


_prefer_local_venv_python()


if __name__ == "__main__":
    uvicorn.run("app.api:app", host="127.0.0.1", port=8099, reload=False)
