"""Command-line interface for scaffold."""

import argparse
import sys

from .generators import (
    generate_script,
    generate_python_cli,
    generate_python_lib,
    generate_fastapi,
    generate_scraper,
    generate_telegram_bot,
    generate_rag,
)


def main():
    parser = argparse.ArgumentParser(
        prog="scaffold",
        description="Generate Python project structures with proven patterns."
    )
    parser.add_argument("--version", action="version", version="0.2.0")
    sub = parser.add_subparsers(dest="command", required=True)

    def add(name, help_text, func):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("project_name", help="Name of the project")
        p.set_defaults(func=lambda args: func(args.project_name))

    add("script", "Single-file Python script", generate_script)
    add("python-cli", "Installable Python CLI tool", generate_python_cli)
    add("python-lib", "Installable Python library", generate_python_lib)
    add("fastapi", "FastAPI web application", generate_fastapi)
    add("scraper", "Web scraper (requests + BeautifulSoup)", generate_scraper)
    add("telegram-bot", "Telegram bot (python-telegram-bot)", generate_telegram_bot)
    add("rag", "RAG system (OpenAI + numpy)", generate_rag)

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
