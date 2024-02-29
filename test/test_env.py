import pytest
from client import Client
import core
import os

def test_env():
    os.environ["INITIAL_VALUE"] = "10"
    assert core.check_env_variables() == 10

    os.environ["INITIAL_VALUE"] = "18"
    assert core.check_env_variables() == 10
