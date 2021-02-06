import os
from typing import NamedTuple

from jinja2 import Template, FileSystemLoader, Environment


class DockerInfo(NamedTuple):
    image_id: str
    image_name: str
    image_version: str


def say_hello(name: str) -> str:
    template = Template("Hello, {{ name }}!")
    return template.render(name=name)


def render_app(version: str, docker: DockerInfo) -> str:
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("app.j2")
    return template.render(version=version, docker=docker)
