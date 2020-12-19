import responses
import requests

from src.http import es


@responses.activate
def test_simple():
    responses.add(
        responses.GET,
        "http://localhost:9200",
        status=404,
        json={
            "name": "8426206b7d62",
            "cluster_name": "docker-cluster",
            "cluster_uuid": "Vi46a1m6ST-uM1izW1HYxw",
            "version": {
                "number": "7.8.0",
                "build_flavor": "default",
                "build_type": "docker",
                "build_hash": "757314695644ea9a1dc2fecd26d1a43856725e65",
                "build_date": "2020-06-14T19:35:50.234439Z",
                "build_snapshot": False,
                "lucene_version": "8.5.1",
                "minimum_wire_compatibility_version": "6.8.0",
                "minimum_index_compatibility_version": "6.0.0-beta1",
            },
            "tagline": "You Know, for Search",
        },
    )

    summary = es.ping_elasticsearch()

    assert (
        summary
        == """\
Summary:
  name: "8426206b7d62"
  cluster_name: "docker-cluster"
  cluster_uuid: "Vi46a1m6ST-uM1izW1HYxw"
  version: "7.8.0"
"""
    )

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == "http://localhost:9200/"
