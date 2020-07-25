from enum import Enum, IntFlag
from typing import NamedTuple


#
# typing — Support for type hints
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
#
class User(NamedTuple):
    first_name: str
    last_name: str
    email: str


#
# enum — Support for enumerations
# https://docs.python.org/3/library/enum.html
#
class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


#
# IntFlag
# https://docs.python.org/3/library/enum.html#intflag
#
class Permission(IntFlag):
    R = 4  # readable
    W = 2  # writable
    X = 1  # executable
    RW = R | W
    RWX = R | W | X
