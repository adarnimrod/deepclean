"""Clean old versions of Docker images."""

import argparse


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(
        description=__doc__,
    )
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
