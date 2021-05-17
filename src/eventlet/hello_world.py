#!/usr/bin/env python3
import eventlet
from datetime import datetime


def say_hello(name: str):
    return f"Hello, {name}!"


def main():
    print(f"-- start: {datetime.now().time()}")
    sentence = eventlet.timeout.with_timeout(30, say_hello, "world")
    print(sentence)
    print(f"---- end: {datetime.now().time()}")


if __name__ == "__main__":
    main()
