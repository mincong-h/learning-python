from enum import Enum
from typing import NamedTuple


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
