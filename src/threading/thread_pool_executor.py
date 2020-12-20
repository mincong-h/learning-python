#!/usr/bin/env python3
#
# Console output:
#
# 13:47:37: ThreadPoolExecutor-0_0 - Hello world 0
# 13:47:37: ThreadPoolExecutor-0_0 - Hello world 1
# 13:47:37: ThreadPoolExecutor-0_0 - Hello world 2
# 13:47:37: ThreadPoolExecutor-0_3 - Hello world 3
# 13:47:37: ThreadPoolExecutor-0_2 - Hello world 4
# 13:47:37: ThreadPoolExecutor-0_2 - Hello world 5
# 13:47:37: ThreadPoolExecutor-0_2 - Hello world 6
# 13:47:37: ThreadPoolExecutor-0_2 - Hello world 7
#
import threading
from concurrent import futures
import logging

PARALLELISM = 4
TASKS = 8


def say_hello(value: int):
    name = threading.current_thread().name
    logging.info(f"{name} - Hello world {value}")


def main():
    logging.basicConfig(
        format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S"
    )
    with futures.ThreadPoolExecutor(max_workers=PARALLELISM) as pool:
        pool.map(say_hello, range(TASKS))


if __name__ == "__main__":
    main()
