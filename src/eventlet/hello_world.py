#!/usr/bin/env python3
import eventlet
from datetime import datetime


def say_hello(name: str):
    return f"Hello, {name}!"


def demo1():
    """
    output:

    -- start: 21:14:46.666814 -----
    Hello, demo1!
    ---- end: 21:14:46.667007 -----
    """
    print(f"-- start: {datetime.now().time()} -----")
    sentence = eventlet.timeout.with_timeout(5, say_hello, "demo1")
    print(sentence)
    print(f"---- end: {datetime.now().time()} -----")


def demo2():
    """
    output:

    -- start: 21:19:42.640061 -----
    Hello, demo2!
    ---- end: 21:19:42.640103 -----
    """
    print(f"-- start: {datetime.now().time()} -----")
    with eventlet.timeout.Timeout(5):
        sentence = say_hello("demo2")
    print(sentence)
    print(f"---- end: {datetime.now().time()} -----")


def demo3():
    """
    output:

    -- start: 21:33:04.221446 -----
    0
    1
    2
    3
    4
    ---- end: 21:33:09.225682 -----
    """
    print(f"-- start: {datetime.now().time()} -----")
    with eventlet.timeout.Timeout(5, False):
        i = 0
        while i < 10:
            print(i)
            eventlet.sleep(1)
            i += 1
    print(f"---- end: {datetime.now().time()} -----")


def demo4():
    """
    output:

    -- start: 21:33:09.225741 -----
    0
    1
    2
    3
    4
    Traceback (most recent call last):
      File "src/eventlet/hello_world.py", line 77, in <module>
        demo4()
      File "src/eventlet/hello_world.py", line 68, in demo4
        eventlet.sleep(1)
      File "/Users/minconghuang/.local/share/virtualenvs/learning-python-8MTqpB0U/lib/python3.7/site-packages/eventlet/greenthread.py", line 36, in sleep
        hub.switch()
      File "/Users/minconghuang/.local/share/virtualenvs/learning-python-8MTqpB0U/lib/python3.7/site-packages/eventlet/hubs/hub.py", line 313, in switch
        return self.greenlet.switch()
    eventlet.timeout.Timeout: 5 seconds
    """
    print(f"-- start: {datetime.now().time()} -----")
    with eventlet.timeout.Timeout(5):
        i = 0
        while i < 10:
            print(i)
            eventlet.sleep(1)
            i += 1
    print(f"---- end: {datetime.now().time()} -----")


if __name__ == "__main__":
    demo1()
    demo2()
    demo3()
    demo4()
