import pytest
import core


def test_helloworld_library():
    result = core.say_hello()
    assert result == "Hello world!"
