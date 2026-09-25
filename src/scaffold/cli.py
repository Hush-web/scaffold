"""Command-line interface for scaffold."""

import argparse
import sys

from .generators import (
    generate_script,
    generate_python_cli,
    generate_python_lib,
    generate_fastapi,
)


def main():
    parser = argparse.ArgumentParser(
        prog="scaffold",
        description="Generate Python project structures with proven patterns."
    )
    parser.add_argument("--version", action="version", version="0.1.0")
    sub = parser.add_subparsers(dest="command", required=True)

    p_script = sub.add_parser("script", help="Single-file Python script")
    p_script.add_argument("name", help="Name of the script")
    p_script.set_defaults(func=lambda args: generate_script(args.name))

    p_cli = sub.add_parser("python-cli", help="Installable Python CLI tool")
    p_cli.add_argument("name", help="Name of the project")
    p_cli.set_defaults(func=lambda args: generate_python_cli(args.name))

    p_lib = sub.add_parser("python-lib", help="Installable Python library")
    p_lib.add_argument("name", help="Name of the project")
    p_lib.set_defaults(func=lambda args: generate_python_lib(args.name))

    p_api = sub.add_parser("fastapi", help="FastAPI web application")
    p_api.add_argument("name", help="Name of the project")
    p_api.set_defaults(func=lambda args: generate_fastapi(args.name))

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
