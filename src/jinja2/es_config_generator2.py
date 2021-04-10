import os
from typing import NamedTuple

from jinja2 import FileSystemLoader, Environment


class ClusterConfig(NamedTuple):
    name: str


class NodeConfig(NamedTuple):
    name: str


def render_config(cluster_name: str, node_id: int) -> str:
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("elasticsearch.yml.v2.j2")

    cluster = ClusterConfig(name=cluster_name)
    node = NodeConfig(name=f"{cluster_name}-data-{node_id}")

    return template.render(cluster=cluster, node=node)
