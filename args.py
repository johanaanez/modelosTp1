import argparse


def parse_arguments():
    usage_options = "%(prog)s [-v] [-f] "

    parser = argparse.ArgumentParser(
        usage=usage_options,
        description="<command description>"
    )

    parser.add_argument("-v", "--verbose", default=False)
    parser.add_argument("-f", "--file")

    return parser.parse_args()
