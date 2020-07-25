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
