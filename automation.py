"""Simple automation starter script."""

import argparse
import logging


def run(name: str) -> None:
    logging.info("Running automation for %s", name)
    print(f"Hello, {name}! Automation is working.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Automation starter script")
    parser.add_argument("--name", default="World", help="name to greet")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    run(args.name)


if __name__ == "__main__":
    main()
