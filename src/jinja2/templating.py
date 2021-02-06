from jinja2 import Template


def say_hello(name: str) -> str:
    template = Template("Hello, {{ name }}!")
    return template.render(name=name)
