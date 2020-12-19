import responses

from src.http import es_index_segments


@responses.activate
def test_simple():
    # Given
    responses.add(
        responses.GET,
        "http://localhost:9200/_all/_segments",
        status=200,
        json={
            "_shards": {"total": 4, "successful": 2, "failed": 0},
            "indices": {
                "my_index": {
                    "shards": {
                        "0": [
                            {
                                "routing": {
                                    "state": "STARTED",
                                    "primary": True,
                                    "node": "AZbE1oFCS0CGIbMurA4zsg",
                                },
                                "num_committed_segments": 0,
                                "num_search_segments": 3,
                                "segments": {
                                    "_0": {
                                        "generation": 0,
                                        "num_docs": 1,
                                        "deleted_docs": 0,
                                        "size_in_bytes": 3437,
                                        "memory_in_bytes": 1412,
                                        "committed": False,
                                        "search": True,
                                        "version": "8.5.1",
                                        "compound": True,
                                        "attributes": {
                                            "Lucene50StoredFieldsFormat.mode": "BEST_SPEED"
                                        },
                                    },
                                    "_1": {
                                        "generation": 1,
                                        "num_docs": 1,
                                        "deleted_docs": 0,
                                        "size_in_bytes": 3445,
                                        "memory_in_bytes": 1412,
                                        "committed": False,
                                        "search": True,
                                        "version": "8.5.1",
                                        "compound": True,
                                        "attributes": {
                                            "Lucene50StoredFieldsFormat.mode": "BEST_SPEED"
                                        },
                                    },
                                    "_2": {
                                        "generation": 2,
                                        "num_docs": 1,
                                        "deleted_docs": 0,
                                        "size_in_bytes": 3496,
                                        "memory_in_bytes": 1412,
                                        "committed": False,
                                        "search": True,
                                        "version": "8.5.1",
                                        "compound": True,
                                        "attributes": {
                                            "Lucene50StoredFieldsFormat.mode": "BEST_SPEED"
                                        },
                                    },
                                },
                            }
                        ]
                    }
                },
                "my_index2": {
                    "shards": {
                        "0": [
                            {
                                "routing": {
                                    "state": "STARTED",
                                    "primary": True,
                                    "node": "AZbE1oFCS0CGIbMurA4zsg",
                                },
                                "num_committed_segments": 0,
                                "num_search_segments": 1,
                                "segments": {
                                    "_0": {
                                        "generation": 0,
                                        "num_docs": 1,
                                        "deleted_docs": 0,
                                        "size_in_bytes": 3452,
                                        "memory_in_bytes": 1412,
                                        "committed": False,
                                        "search": True,
                                        "version": "8.5.1",
                                        "compound": True,
                                        "attributes": {
                                            "Lucene50StoredFieldsFormat.mode": "BEST_SPEED"
                                        },
                                    }
                                },
                            }
                        ]
                    }
                },
            },
        },
    )

    # When
    segments = es_index_segments.get_segments()

    # Then
    assert segments == {"my_index": {"8.5.1"}, "my_index2": {"8.5.1"}}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == "http://localhost:9200/_all/_segments"
    assert responses.calls[0].response.status_code == 200
