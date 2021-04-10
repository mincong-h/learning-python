import src.jinja2.es_config_generator as generator


def test_render_app():
    yml = generator.render_config(cluster_name="es-demo", node_id=1)
    assert (
        yml
        == """\
cluster.name: es-demo
node.name: es-demo-data-1
network.host: 0.0.0.0"""
    )
