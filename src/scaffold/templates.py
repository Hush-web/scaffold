"""File templates used by the generators."""

GITIGNORE = """\
__pycache__/
*.pyc
*.egg-info/
dist/
build/
.venv/
venv/
.env
"""

README = """\
# __NAME__

TODO: describe what this project does.

## Install

    pip install -e .
"""

PYPROJECT_CLI = """\
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "__NAME__"
version = "0.1.0"
description = "TODO"
readme = "README.md"
requires-python = ">=3.9"
dependencies = []

[project.scripts]
__NAME__ = "__PACKAGE__.cli:main"

[tool.setuptools.packages.find]
where = ["src"]
"""

PYPROJECT_LIB = """\
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "__NAME__"
version = "0.1.0"
description = "TODO"
readme = "README.md"
requires-python = ">=3.9"
dependencies = []

[tool.setuptools.packages.find]
where = ["src"]
"""

PYPROJECT_FASTAPI = """\
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "__NAME__"
version = "0.1.0"
description = "TODO"
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
    "fastapi>=0.110.0",
    "uvicorn[standard]>=0.29.0",
    "httpx>=0.27.0",
]

[project.scripts]
__NAME__ = "__PACKAGE__.main:run"

[tool.setuptools.packages.find]
where = ["src"]
"""

CLI_PY = '''\
"""Command-line interface for __NAME__."""

import argparse
import sys


def cmd_hello(args):
    """Say hello."""
    print(f"Hello, {args.name}!")


def main():
    parser = argparse.ArgumentParser(prog="__NAME__")
    parser.add_argument("--version", action="version", version="0.1.0")
    sub = parser.add_subparsers(dest="command", required=True)

    p_hello = sub.add_parser("hello", help="Say hello")
    p_hello.add_argument("name", nargs="?", default="world")
    p_hello.set_defaults(func=cmd_hello)

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
'''

CORE_PY = '''\
"""Core logic for __NAME__."""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"
'''

INIT_LIB = '''\
"""__NAME__ — a Python library."""

from .core import greet

__all__ = ["greet"]
'''

INIT_FASTAPI = '''\
"""__NAME__ — a FastAPI application."""

from .main import app

__all__ = ["app"]
'''

MAIN_FASTAPI = '''\
"""FastAPI application for __NAME__."""

from fastapi import FastAPI

app = FastAPI(title="__NAME__", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Hello from __NAME__"}


@app.get("/health")
def health():
    return {"status": "ok"}


def run():
    """Run the dev server."""
    import uvicorn
    uvicorn.run("__PACKAGE__.main:app", host="127.0.0.1", port=8000, reload=True)
'''

TEST_CLI_PY = '''\
import subprocess
import sys


def test_hello_runs():
    result = subprocess.run(
        [sys.executable, "-m", "__PACKAGE__.cli", "hello", "world"],
        capture_output=True,
        text=True,
    )
    assert "Hello, world!" in result.stdout
'''

TEST_FASTAPI = '''\
from fastapi.testclient import TestClient
from __PACKAGE__.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
'''

SCRIPT_PY = '''\
#!/usr/bin/env python3
"""__NAME__ — a command-line script."""

import argparse


def main():
    parser = argparse.ArgumentParser(description="TODO")
    parser.add_argument("--name", default="world", help="Who to greet")
    args = parser.parse_args()

    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
'''
