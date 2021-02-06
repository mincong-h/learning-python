import os

from jinja2 import Template, FileSystemLoader, Environment


def say_hello(name: str) -> str:
    template = Template("Hello, {{ name }}!")
    return template.render(name=name)


def render_app(version: str) -> str:
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("app.j2")
    return template.render(version=version)