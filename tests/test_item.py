"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest as pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def data():
    return Item('TV', 15000, 5)


def test_calculate_total_price(data):
    assert data.calculate_total_price() == 75000


def test_apply_discount(data):
    data.pay_rate = 0.5
    assert data.apply_discount() == 7500


# def test_instantiate_from_csv(data):
#     item1 = Item.instantiate_from_csv()
#     assert item1.name == 'Смартфон'
#     assert item1.price == 100


def test_name():
    item1 = Item('Microwave', 10000, 1)
    item2 = Item('Refregerator', 5000, 1)
    assert len(item1.name) <= 10
    assert item2.name == 'Refregerator'


def test_string_to_number():
    assert Item.string_to_number("10.0") == 10


def test_repr(data):
    assert repr(data) == "Item('TV', 15000, 5)"


def test_str(data):
    assert str(data) == 'TV'


def test_add(data):
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert data.quantity + phone1.quantity == 10
