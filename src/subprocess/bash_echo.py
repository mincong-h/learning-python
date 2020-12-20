#!/usr/bin/env python3
#
# Console output of `print_hello`:
#
# ```
# Hello world
# ---
# args: ['echo', 'Hello world']
# code: 0
# ```
#
# Console output of `get_hello`:
#
# ```
# Hello world
# ```
import subprocess
from subprocess import CompletedProcess


def print_hello():
    result: CompletedProcess = subprocess.run(["echo", "Hello world"])
    print(
        f"""\
---
args: {result.args}
code: {result.returncode}"""
    )


def get_hello() -> str:
    result: CompletedProcess = subprocess.run(
        ["echo", "Hello world"], capture_output=True
    )
    return result.stdout.decode("UTF-8")


def main():
    print_hello()
    print(get_hello())


if __name__ == "__main__":
    main()
