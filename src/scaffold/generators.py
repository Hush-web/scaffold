"""Functions that generate each project type."""

from pathlib import Path

from . import templates


def _normalize(name: str) -> tuple[str, str]:
    """Return (folder_name, package_name)."""
    return name, name.replace("-", "_")


def _confirm_overwrite(path: Path) -> bool:
    """Ask before overwriting an existing path."""
    if not path.exists():
        return True
    answer = input(f"'{path}' already exists. Overwrite? [y/N] ").strip().lower()
    return answer == "y"


def _write(path: Path, content: str) -> None:
    """Write content to a file, creating parent folders as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _fill(template: str, name: str, package: str) -> str:
    """Replace placeholders in a template."""
    return template.replace("__NAME__", name).replace("__PACKAGE__", package)


def generate_script(name: str) -> None:
    """Generate a single-file Python script."""
    path = Path(f"{name}.py")
    if not _confirm_overwrite(path):
        print("Aborted.")
        return

    _write(path, templates.SCRIPT_PY.replace("__NAME__", name))
    print(f"Created {path}")


def generate_python_cli(name: str) -> None:
    """Generate an installable Python CLI tool."""
    folder, package = _normalize(name)
    root = Path(folder)

    if not _confirm_overwrite(root):
        print("Aborted.")
        return

    pkg_dir = root / "src" / package
    tests_dir = root / "tests"

    _write(root / "pyproject.toml", _fill(templates.PYPROJECT_CLI, name, package))
    _write(root / "README.md", _fill(templates.README, name, package))
    _write(root / ".gitignore", templates.GITIGNORE)
    _write(pkg_dir / "__init__.py", "")
    _write(pkg_dir / "cli.py", _fill(templates.CLI_PY, name, package))
    _write(tests_dir / "__init__.py", "")
    _write(tests_dir / "test_cli.py", _fill(templates.TEST_CLI_PY, name, package))

    print(f"Created {root}/")
    print(f"Next: cd {folder} && pip install -e . && {name} hello")


def generate_python_lib(name: str) -> None:
    """Generate an installable Python library."""
    folder, package = _normalize(name)
    root = Path(folder)

    if not _confirm_overwrite(root):
        print("Aborted.")
        return

    pkg_dir = root / "src" / package

    _write(root / "pyproject.toml", _fill(templates.PYPROJECT_LIB, name, package))
    _write(root / "README.md", _fill(templates.README, name, package))
    _write(root / ".gitignore", templates.GITIGNORE)
    _write(pkg_dir / "__init__.py", _fill(templates.INIT_LIB, name, package))
    _write(pkg_dir / "core.py", _fill(templates.CORE_PY, name, package))

    print(f"Created {root}/")
    print(f"Next: cd {folder} && pip install -e .")


def generate_fastapi(name: str) -> None:
    """Generate a FastAPI web application."""
    folder, package = _normalize(name)
    root = Path(folder)

    if not _confirm_overwrite(root):
        print("Aborted.")
        return

    pkg_dir = root / "src" / package
    tests_dir = root / "tests"

    _write(root / "pyproject.toml", _fill(templates.PYPROJECT_FASTAPI, name, package))
    _write(root / "README.md", _fill(templates.README, name, package))
    _write(root / ".gitignore", templates.GITIGNORE)
    _write(pkg_dir / "__init__.py", _fill(templates.INIT_FASTAPI, name, package))
    _write(pkg_dir / "main.py", _fill(templates.MAIN_FASTAPI, name, package))
    _write(tests_dir / "__init__.py", "")
    _write(tests_dir / "test_main.py", _fill(templates.TEST_FASTAPI, name, package))

    print(f"Created {root}/")
    print(f"Next: cd {folder} && pip install -e . && {name}")
