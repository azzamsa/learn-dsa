import nox


@nox.session(python=["3.9"])
def lint(session):
    session.install("-r", "requirements.txt")
    session.run("pylint", "src")


@nox.session(python=["3.8", "3.9"])
def test(session):
    session.install("-r", "requirements.txt")
    session.run("pytest", "src", "-v")


@nox.session(python=["3.9"])
def coverage(session):
    session.install("-r", "requirements.txt")
    session.run("coverage", "run", "-m", "pytest", "src")
    session.run("coverage", "report", "-m")
