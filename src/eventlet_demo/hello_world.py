#!/usr/bin/env python3
import eventlet
from datetime import datetime


def say_hello(name: str):
    return f"Hello, ${name}!"


def main():
    print(f"start: {datetime.now()}")
    sentence = eventlet.timeout.with_timeout(say_hello, "world", timeout_value="5s")
    print(sentence)
    print(f"end: {datetime.now()}")


if __name__ == "__main__":
    main()
