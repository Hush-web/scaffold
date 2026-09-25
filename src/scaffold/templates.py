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


# --- Scraper ---

PYPROJECT_SCRAPER = """\
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
    "requests>=2.31.0",
    "beautifulsoup4>=4.12.0",
]

[project.scripts]
__NAME__ = "__PACKAGE__.cli:main"

[tool.setuptools.packages.find]
where = ["src"]
"""

INIT_SCRAPER = '''\
"""__NAME__ - a web scraper."""

from .scraper import fetch, parse_links

__all__ = ["fetch", "parse_links"]
'''

SCRAPER_PY = '''\
"""Scraper for __NAME__."""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; __NAME__/0.1)"}


def fetch(url: str, timeout: int = 15) -> str:
    """Fetch HTML from a URL."""
    response = requests.get(url, headers=HEADERS, timeout=timeout)
    response.raise_for_status()
    return response.text


def parse_links(html: str, base: str = "") -> list[str]:
    """Return all absolute links found in the HTML."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        links.append(urljoin(base, a["href"]))
    return links
'''

CLI_SCRAPER = '''\
"""CLI for __NAME__."""

import argparse
import sys

from .scraper import fetch, parse_links


def main():
    parser = argparse.ArgumentParser(prog="__NAME__")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("--links", action="store_true", help="Print links")
    args = parser.parse_args()

    try:
        html = fetch(args.url)
    except Exception as e:
        print(f"Failed to fetch: {e}", file=sys.stderr)
        sys.exit(1)

    if args.links:
        for link in parse_links(html, base=args.url):
            print(link)
    else:
        print(html[:2000])


if __name__ == "__main__":
    main()
'''

TEST_SCRAPER = '''\
from __PACKAGE__.scraper import parse_links


def test_parse_links_basic():
    html = '<html><body><a href="https://example.com">x</a></body></html>'
    assert parse_links(html) == ["https://example.com"]
'''


# --- Telegram bot ---

PYPROJECT_BOT = """\
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
    "python-telegram-bot>=21.0",
]

[project.scripts]
__NAME__ = "__PACKAGE__.bot:main"

[tool.setuptools.packages.find]
where = ["src"]
"""

INIT_BOT = '''\
"""__NAME__ - a Telegram bot."""
'''

BOT_PY = '''\
"""Telegram bot for __NAME__."""

import os
import sys

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN_ENV = "TELEGRAM_BOT_TOKEN"


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I am __NAME__.")


async def cmd_echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args) if context.args else "nothing to echo"
    await update.message.reply_text(text)


async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")


def main():
    token = os.getenv(TOKEN_ENV)
    if not token:
        print(f"Set {TOKEN_ENV} first.", file=sys.stderr)
        sys.exit(1)

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("echo", cmd_echo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    print("Bot running. Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
'''

TEST_BOT = '''\
def test_placeholder():
    assert True
'''


# --- RAG ---

PYPROJECT_RAG = """\
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
    "openai>=1.0.0",
    "numpy>=1.26.0",
]

[project.scripts]
__NAME__ = "__PACKAGE__.cli:main"

[tool.setuptools.packages.find]
where = ["src"]
"""

INIT_RAG = '''\
"""__NAME__ - a RAG system."""

from .rag import Store, embed, answer

__all__ = ["Store", "embed", "answer"]
'''

RAG_PY = '''\
"""Minimal RAG system for __NAME__."""

import os
import numpy as np
from openai import OpenAI


MODEL_EMBED = os.getenv("RAG_EMBED_MODEL", "text-embedding-3-small")
MODEL_CHAT = os.getenv("RAG_CHAT_MODEL", "gpt-4o-mini")


def _client() -> OpenAI:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("Set OPENAI_API_KEY")
    return OpenAI(api_key=key)


def embed(text: str) -> list[float]:
    """Embed a single string."""
    response = _client().embeddings.create(model=MODEL_EMBED, input=text)
    return response.data[0].embedding


class Store:
    """In-memory vector store."""

    def __init__(self):
        self.texts = []
        self.vectors = []

    def add(self, text: str) -> None:
        self.texts.append(text)
        self.vectors.append(embed(text))

    def search(self, query: str, top_k: int = 3) -> list[str]:
        if not self.texts:
            return []
        q = np.array(embed(query))
        m = np.array(self.vectors)
        sims = m @ q / (np.linalg.norm(m, axis=1) * np.linalg.norm(q) + 1e-9)
        order = np.argsort(-sims)[:top_k]
        return [self.texts[i] for i in order]


def answer(store: Store, question: str) -> str:
    """Retrieve context and ask the LLM."""
    contexts = store.search(question, top_k=3)
    context = "\\n\\n".join(contexts) if contexts else "(no context)"
    prompt = f"Answer using only this context.\\n\\nContext:\\n{context}\\n\\nQuestion: {question}"
    response = _client().chat.completions.create(
        model=MODEL_CHAT,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content
'''

CLI_RAG = '''\
"""CLI for __NAME__."""

import argparse
from pathlib import Path

from .rag import Store, answer


def main():
    parser = argparse.ArgumentParser(prog="__NAME__")
    sub = parser.add_subparsers(dest="command", required=True)

    p_ingest = sub.add_parser("ingest", help="Ingest a text file")
    p_ingest.add_argument("path")

    p_ask = sub.add_parser("ask", help="Ask a question")
    p_ask.add_argument("question")

    args = parser.parse_args()
    store = Store()

    if args.command == "ingest":
        text = Path(args.path).read_text(encoding="utf-8", errors="ignore")
        chunks = [c.strip() for c in text.split("\\n\\n") if c.strip()]
        for c in chunks:
            store.add(c)
        print(f"Ingested {len(chunks)} chunks.")
    else:
        print(answer(store, args.question))


if __name__ == "__main__":
    main()
'''

TEST_RAG = '''\
from __PACKAGE__.rag import Store


def test_store_is_empty():
    assert Store().search("anything") == []
'''
