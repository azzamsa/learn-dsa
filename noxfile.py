import nox


@nox.session(python=["3.8", "3.9"])
def lint(session):
    session.install("pylint==2.11.1")
    session.run("pylint", "src")


@nox.session(python=["3.8", "3.9"])
def tests(session):
    session.install("pytest==6.2.5")
    session.run("pytest", "src")


@nox.session(python=["3.9"])
def coverage(session):
    session.install("coverage==6.1.2")
    session.install("pytest==6.2.5")
    session.run("coverage", "run", "-m", "pytest", "src")
    session.run("coverage", "report", "-m")
