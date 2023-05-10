import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def playstation_5():
    return KeyBoard("playstation_5", 50000, 5)


def test_init(playstation_5):
    assert str(playstation_5) == "playstation_5"


def test_lang(playstation_5):
    assert playstation_5.language == "EN"


def test_change_lang(playstation_5):
    playstation_5.change_lang()
    assert playstation_5.language == "RU"
    playstation_5.change_lang()
    assert playstation_5.language == "EN"
