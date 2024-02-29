import pytest
from client import Client
import core
import os

def test_env():
    os.environ["INITIAL_VALUE"] = "10"
    result = core.check_env_variables()
    assert result == 10

    os.environ["INITIAL_VALUE"] = "18"
    result = core.check_env_variables()
    assert result == 18
