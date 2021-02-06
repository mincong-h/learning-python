from src.jinja2.templating import *


def test_say_hello():
    message = say_hello("Python")
    assert message == "Hello, Python!"


def test_render_app():
    yml = render_app(
        version="1.0.0",
        docker=DockerInfo(image_id="12345", image_name="python", image_version="3.8.7"),
    )
    assert (
        yml
        == """\
name: my-app
version: 1.0.0
docker:
  image_name: python
  image_id: 12345
  image_version: 3.8.7"""
    )
