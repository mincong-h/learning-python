from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--company", type=str, help="Company name")
    parser.add_argument("--cloud-provider", type=str, help="Cloud provider")
    return parser
