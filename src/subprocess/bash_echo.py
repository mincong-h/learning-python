#!/usr/bin/env python3
#
# Hello world
# ---
# args: ['echo', 'Hello world']
# code: 0
#
import subprocess
from subprocess import CompletedProcess


def print_hello():
    result: CompletedProcess = subprocess.run(["echo", "Hello world"])
    print(f"""\
---
args: {result.args}
code: {result.returncode}""")


def main():
    print_hello()


if __name__ == "__main__":
    main()
