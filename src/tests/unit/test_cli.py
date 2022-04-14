from src.main import cli
from unittest.mock import Mock

"""
To test the entire project and print output, run this from the root directory:
python -m pytest -s
"""

def setup():
    """
    # This should execute at the start of each test.
    :return: None
    """
    print("Executing Setup")


def teardown():
    """
    This should execute at the end of each test.
    :return: None
    """
    print("Executing Teardown")


def test_main():
    """
    To test a specific function...
    python -m pytest -s tests/test_cli.py::test_main
    :return: None
    """
    assert True

