import pytest as pytest

from src.phone import Phone


@pytest.fixture
def data():
    return Phone('Xiaomi', 25000, 5, 3)


def test_repr(data):
    assert repr(data) == "Phone('Xiaomi', 25000, 5, 3)"
