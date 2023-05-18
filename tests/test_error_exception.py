import pytest
from src.item import Item
from src.error_exception import InstantiateCSVError


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../src/items1.csv')


def test_instantiate_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../src/items_file.csv')
