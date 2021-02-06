from argparse import ArgumentParser, Action

from typing import Optional


# https://docs.python.org/3/library/argparse.html#action
class CompanyArgumentAction(Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(CompanyArgumentAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, company, option_string=None):
        # setattr(namespace, "company", "Google") is equivalent to
        #
        #     namespace.company: "Google"
        #
        setattr(namespace, self.dest, company)

        provider = self.compute_provider(company)
        if provider and namespace.cloud_provider is None:
            setattr(namespace, "cloud_provider", provider)

    def compute_provider(self, company: str) -> Optional[str]:
        if company == "Google":
            return "GCP"
        if company == "Amazon":
            return "AWS"
        if company == "Microsoft":
            return "Azure"
        return None


def create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument(
        "--company",
        type=str,
        help="Company name",
        # Register a custom action to set the value of "company",
        # compute and set the value of "cloud_provider"
        action=CompanyArgumentAction,
    )
    parser.add_argument("--cloud-provider", type=str, help="Cloud provider")
    return parser
