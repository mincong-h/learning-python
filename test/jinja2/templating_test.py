from src.jinja2.templating import *


def test_say_hello():
    message = say_hello("Python")
    assert message == "Hello, Python!"


def test_render_app():
    yml = render_app(version="1.0.0")
    assert yml == """\
name: my-app
version: 1.0.0"""