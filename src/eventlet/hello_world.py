#!/usr/bin/env python3
import eventlet
from datetime import datetime


def say_hello(name: str):
    return f"Hello, {name}!"


def demo1():
    """
    output:

    -- start: 21:14:46.666814 -----
    Hello, world!
    ---- end: 21:14:46.667007 -----
    """
    print(f"-- start: {datetime.now().time()} -----")
    sentence = eventlet.timeout.with_timeout(30, say_hello, "world")
    print(sentence)
    print(f"---- end: {datetime.now().time()} -----")


if __name__ == "__main__":
    demo1()
