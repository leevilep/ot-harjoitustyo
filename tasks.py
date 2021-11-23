from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest src/tests")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src/tests")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")