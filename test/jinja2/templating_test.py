from src.jinja2.templating import *


def test_say_hello():
    message = say_hello("Python")
    assert message == "Hello, Python!"
