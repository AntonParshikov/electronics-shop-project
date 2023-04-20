"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest as pytest

from src.item import Item


@pytest.fixture
def data():
    return Item('TV', 15000, 5)


def test_calculate_total_price(data):
    assert data.calculate_total_price() == 75000


def test_apply_discount(data):
    data.pay_rate = 0.5
    assert data.apply_discount() == 7500
