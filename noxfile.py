import pathlib

import nox
import nox.sessions

VENV_DIR = pathlib.Path(".venv")

nox.options.sessions = ["lint", "format", "tests-3.10", "tests-3.11", "tests-3.12", "coverage", "docs"]
nox.options.reuse_existing_virtualenvs = True


@nox.session
def lint(session: nox.sessions.Session):
    """
    Lints all source files and test files with `ruff`.
    """
    session.install("ruff")
    session.run("ruff", "check", "--fix", "binance", "tests", "noxfile.py")


@nox.session
def format(session: nox.sessions.Session):
    """
    Formats all source files and test files with `ruff`.
    """
    session.install("ruff")
    session.run("ruff", "format", "binance", "tests", "noxfile.py")


@nox.session(python=["3.10", "3.11", "3.12"])
def tests(session: nox.sessions.Session):
    """
    Runs the test suite.
    """
    session.install("pytest", ".")
    session.run("pytest")


@nox.session
def coverage(session: nox.sessions.Session):
    """
    Generates test coverage report.
    """
    session.install("pytest", "coverage", ".")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "report")
    session.run("coverage", "html")


@nox.session
def docs(session: nox.sessions.Session):
    """
    Generates documentation.
    """
    session.install("sphinx", "furo", ".")
    with session.chdir("docs"):
        session.run("make", "html", external=True)


@nox.session
def dev(session: nox.sessions.Session):
    """
    Prepares a development environment
    """
    session.install("virtualenv")
    session.run("virtualenv", VENV_DIR, silent=True)

    python = VENV_DIR / "bin/python"

    session.run(str(python), "-m", "pip", "install", "-e", ".[dev]", external=True)
