from src.argparse.cli import *


def test_parser_creation():
    parser = create_parser()
    namespace = parser.parse_args(["--company", "Google"])
    assert namespace.__dict__ == {
        "company": "Google",
        "cloud_provider": None,
    }
