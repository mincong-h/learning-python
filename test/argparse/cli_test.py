from src.argparse.cli import *


def test_args_parsing_with_computed_provider_google():
    parser = create_parser()
    namespace = parser.parse_args(["--company", "Google"])
    assert namespace.__dict__ == {
        "company": "Google",
        "cloud_provider": "GCP",
    }


def test_args_parsing_with_computed_provider_amazon():
    parser = create_parser()
    namespace = parser.parse_args(["--company", "Amazon"])
    assert namespace.__dict__ == {
        "company": "Amazon",
        "cloud_provider": "AWS",
    }


def test_args_parsing_with_computed_provider_microsoft():
    parser = create_parser()
    namespace = parser.parse_args(["--company", "Microsoft"])
    assert namespace.__dict__ == {
        "company": "Microsoft",
        "cloud_provider": "Azure",
    }


def test_args_parsing_with_computed_provider_unknown():
    parser = create_parser()
    namespace = parser.parse_args(["--company", "GitHub"])
    assert namespace.__dict__ == {
        "company": "GitHub",
        "cloud_provider": None,
    }


def test_args_parsing_with_explicit_provider():
    parser = create_parser()
    namespace = parser.parse_args(["--company", "Google", "--cloud-provider", "OVH"])
    assert namespace.__dict__ == {
        "company": "Google",
        "cloud_provider": "OVH",
    }


def test_args_parsing_with_explicit_provider2():
    parser = create_parser()
    namespace = parser.parse_args(["--cloud-provider", "OVH", "--company", "Google"])
    assert namespace.__dict__ == {
        "company": "Google",
        "cloud_provider": "OVH",
    }
