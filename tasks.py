from invoke import task
from os import system


@task
def clean(_):
    system("rm -rf build")
    system("rm -rf .vscode")