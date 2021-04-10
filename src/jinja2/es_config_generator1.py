import os

from jinja2 import FileSystemLoader, Environment


def render_config(cluster_name: str, node_name: str) -> str:
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("elasticsearch.yml.v1.j2")
    return template.render(cluster_name=cluster_name, node_name=node_name)
