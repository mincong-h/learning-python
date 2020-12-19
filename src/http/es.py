#!/usr/bin/env python3
import requests


def ping_elasticsearch() -> str:
    response = requests.get("http://localhost:9200")
    info = response.json()
    # {
    #   "name" : "8426206b7d62",
    #   "cluster_name" : "docker-cluster",
    #   "cluster_uuid" : "Vi46a1m6ST-uM1izW1HYxw",
    #   "version" : {
    #     "number" : "7.8.0",
    #     "build_flavor" : "default",
    #     "build_type" : "docker",
    #     "build_hash" : "757314695644ea9a1dc2fecd26d1a43856725e65",
    #     "build_date" : "2020-06-14T19:35:50.234439Z",
    #     "build_snapshot" : false,
    #     "lucene_version" : "8.5.1",
    #     "minimum_wire_compatibility_version" : "6.8.0",
    #     "minimum_index_compatibility_version" : "6.0.0-beta1"
    #   },
    #   "tagline" : "You Know, for Search"
    # }
    return f"""\
Summary:
  name: "{info["name"]}"
  cluster_name: "{info["cluster_name"]}"
  cluster_uuid: "{info["cluster_uuid"]}"
  version: "{info["version"]["number"]}"
"""


def main():
    summary = ping_elasticsearch()
    print(summary)


if __name__ == "__main__":
    main()
