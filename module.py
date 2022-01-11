import os
import logging


def import_module():
    # Import python file
    import calculation

    print(calculation.add(1, 1))

    # import a single thing in the file
    from calculation import add

    print(add(1, 2))

    # Import everything to this file
    from calculation import *
    print(add(1, 3))


def print_os():
    print(os.name)


def log_text(text):
    logger = logging.getLogger("MAIN")
    logger.error(f"Logging error with text {text}")
