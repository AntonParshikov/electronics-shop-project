"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest as pytest

from src.item import Item

from src import item


@pytest.fixture
def data():
    return Item('TV', 15000, 5)


def test_calculate_total_price(data):
    assert data.calculate_total_price() == 75000


def test_apply_discount(data):
    data.pay_rate = 0.5
    assert data.apply_discount() == 7500


def test_instantiate_from_csv():
    item1 = Item('Смартфон', 10000, 1)
    item1.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'


def test_name(data):
    item1 = Item('Microwave', 10000, 1)
    assert len(item1.name) == 9


def test_string_to_number():
    assert Item.string_to_number("10.0") == 10
