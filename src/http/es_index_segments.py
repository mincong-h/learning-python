#!/usr/bin/env python3
from typing import List, Dict, Set

import requests


def get_segments() -> Dict[str, Set[str]]:
    response = requests.get("http://localhost:9200/_all/_segments")
    json = response.json()
    # {
    #   "_shards" : {
    #     "total" : 4,
    #     "successful" : 2,
    #     "failed" : 0
    #   },
    #   "indices" : {
    #     "my_index" : {
    #       "shards" : {
    #         "0" : [
    #           {
    #             "routing" : {
    #               "state" : "STARTED",
    #               "primary" : true,
    #               "node" : "AZbE1oFCS0CGIbMurA4zsg"
    #             },
    #             "num_committed_segments" : 0,
    #             "num_search_segments" : 3,
    #             "segments" : {
    #               "_0" : {
    #                 "generation" : 0,
    #                 "num_docs" : 1,
    #                 "deleted_docs" : 0,
    #                 "size_in_bytes" : 3437,
    #                 "memory_in_bytes" : 1412,
    #                 "committed" : false,
    #                 "search" : true,
    #                 "version" : "8.5.1",
    #                 "compound" : true,
    #                 "attributes" : {
    #                   "Lucene50StoredFieldsFormat.mode" : "BEST_SPEED"
    #                 }
    #               },
    #               "_1" : {
    #                 "generation" : 1,
    #                 "num_docs" : 1,
    #                 "deleted_docs" : 0,
    #                 "size_in_bytes" : 3445,
    #                 "memory_in_bytes" : 1412,
    #                 "committed" : false,
    #                 "search" : true,
    #                 "version" : "8.5.1",
    #                 "compound" : true,
    #                 "attributes" : {
    #                   "Lucene50StoredFieldsFormat.mode" : "BEST_SPEED"
    #                 }
    #               },
    #               "_2" : {
    #                 "generation" : 2,
    #                 "num_docs" : 1,
    #                 "deleted_docs" : 0,
    #                 "size_in_bytes" : 3496,
    #                 "memory_in_bytes" : 1412,
    #                 "committed" : false,
    #                 "search" : true,
    #                 "version" : "8.5.1",
    #                 "compound" : true,
    #                 "attributes" : {
    #                   "Lucene50StoredFieldsFormat.mode" : "BEST_SPEED"
    #                 }
    #               }
    #             }
    #           }
    #         ]
    #       }
    #     },
    #     "my_index2" : {
    #       "shards" : {
    #         "0" : [
    #           {
    #             "routing" : {
    #               "state" : "STARTED",
    #               "primary" : true,
    #               "node" : "AZbE1oFCS0CGIbMurA4zsg"
    #             },
    #             "num_committed_segments" : 0,
    #             "num_search_segments" : 1,
    #             "segments" : {
    #               "_0" : {
    #                 "generation" : 0,
    #                 "num_docs" : 1,
    #                 "deleted_docs" : 0,
    #                 "size_in_bytes" : 3452,
    #                 "memory_in_bytes" : 1412,
    #                 "committed" : false,
    #                 "search" : true,
    #                 "version" : "8.5.1",
    #                 "compound" : true,
    #                 "attributes" : {
    #                   "Lucene50StoredFieldsFormat.mode" : "BEST_SPEED"
    #                 }
    #               }
    #             }
    #           }
    #         ]
    #       }
    #     }
    #   }
    # }
    results = {}
    for index_name, index in json["indices"].items():
        versions = set()
        for _, shards in index["shards"].items():
            for shard in shards:
                for _, segment in shard["segments"].items():
                    versions.add(segment["version"])
        results[index_name] = versions
    return results


def main():
    print("Segments:")
    for k, v in get_segments().items():
        print(f"- {k}: {v}")


if __name__ == "__main__":
    main()
