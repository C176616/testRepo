import pytest
import core


def test_myFunction():
    result = core.make_client()
    assert result == "Hello world!"
