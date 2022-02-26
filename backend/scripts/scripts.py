import subprocess

project_folder = "app"

targets = f"{project_folder} scripts conftest.py"


class TextStyle:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def lint() -> None:
    """Same functionality as the linting script (lint.sh).

    Having these commands in a Python file enables them to be run with `poetry run`."""

    print("🚨 Type checking with mypy...")
    subprocess.run(f"mypy {targets} --exclude alembic", shell=True, text=True)

    print("🎨 Checking code formatting with black...")
    subprocess.run(f"black {targets} --check", shell=True, text=True)

    print("🎨 Checking imports with isort...")
    subprocess.run(f"isort --check-only {targets}", shell=True, text=True)

    print("🎨 Checking code style with flake8...")
    subprocess.run(f"flake8 {targets}", shell=True, text=True)

    # print("🔒️  Scan for security issues with bandit...")
    # subprocess.run(f"bandit -r -q {project_folder}", shell=True, text=True)


def format() -> None:
    """Same functionality as the formatting script (format.sh).

    Having these commands in a Python file enables them to be run with `poetry run`."""

    print("🎨 Sort imports one per line, so autoflake can remove unused imports")
    subprocess.run(f"isort --force-single-line-imports {targets}", shell=True, text=True)
    subprocess.run(
        f"autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place {targets} --exclude=__init__.py",  # noqa: E501
        shell=True,
        text=True,
    )

    print("🎨 Format code with black")
    subprocess.run(f"black {targets}", shell=True, text=True)

    print("🎨 Sort imports with isort")
    subprocess.run(f"isort {targets}", shell=True, text=True)

    print("✅ Formatting complete!")


def format_and_lint() -> None:
    """Runs linting and formatting in one go."""
    print(f"🎨 {TextStyle.UNDERLINE}Running formatters...{TextStyle.END}")
    format()
    print(f"\n🚨 {TextStyle.UNDERLINE}Running linters...{TextStyle.END}")
    lint()


def test() -> None:
    """Same functionality as the testing script (test.sh).

    Having these commands in a Python file enables them to be run with `poetry run`."""
    # parser = argparse.ArgumentParser(description='Say hi.')
    # parser.add_argument('target', type=str, default="tests", help='the name of the target')
    # args = parser.parse_args()

    subprocess.run(f"pytest --cov={project_folder}", shell=True, text=True)


def format_lint_test() -> None:
    """Runs linting, formatting, and testing in one go."""
    print(f"🎨 {TextStyle.UNDERLINE}Running formatters...{TextStyle.END}")
    format()
    print(f"🚨 {TextStyle.UNDERLINE}Running linters...{TextStyle.END}")
    lint()
    print(f"🧪 {TextStyle.UNDERLINE}Running tests...{TextStyle.END}")
    test()
