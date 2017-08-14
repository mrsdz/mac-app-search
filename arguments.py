import argparse

PARSER = argparse.ArgumentParser(
    description="With this app you can easily download mac application"
)
PARSER.add_argument(
    '--app',
    help="Type name of the app you want to download."
)
PARSER.add_argument(
    '--version',
    help="Type name of the app for see version of it."
)
ARGS = PARSER.parse_args()