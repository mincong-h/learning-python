from src.core.classes import *


def test_named_tuple_creation_with_keyword():
    user = User(first_name="foo", last_name="bar", email="foo.bar@example.com")

    assert user.first_name == "foo"
    assert user.last_name == "bar"
    assert user.email == "foo.bar@example.com"


def test_named_tuple_creation_without_keyword():
    user = User("foo", "bar", "foo.bar@example.com")

    assert user.first_name == "foo"
    assert user.last_name == "bar"
    assert user.email == "foo.bar@example.com"


def test_named_tuple_equality():
    u1 = User("foo", "bar", "foo.bar@example.com")
    u2 = User("foo", "bar", "foo.bar@example.com")

    assert u1 == u2
    assert hash(u1) == hash(u2)


def test_enum_values():
    assert Difficulty.EASY != 1
    assert Difficulty.MEDIUM != 2
    assert Difficulty.HARD != 3

    assert Difficulty.EASY.value == 1
    assert Difficulty.MEDIUM.value == 2
    assert Difficulty.HARD.value == 3


def test_enum_iteration():
    for d in Difficulty:
        assert isinstance(d, Difficulty)


def test_enum_to_string():
    assert str(Difficulty.EASY) == "Difficulty.EASY"
    assert str(Difficulty.MEDIUM) == "Difficulty.MEDIUM"
    assert str(Difficulty.HARD) == "Difficulty.HARD"


def test_enum_lookup():
    # access by name
    assert Difficulty["EASY"] is Difficulty.EASY
    assert Difficulty["MEDIUM"] is Difficulty.MEDIUM
    assert Difficulty["HARD"] is Difficulty.HARD

    # access by attribute
    assert Difficulty(1) is Difficulty.EASY
    assert Difficulty(2) is Difficulty.MEDIUM
    assert Difficulty(3) is Difficulty.HARD
