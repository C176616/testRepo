import pytest
import src.core as core


def test_myFunction():
    result = core.myFunction()
    assert result == "Hello world!"
