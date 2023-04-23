import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, item_name):
        if len(item_name) <= 10:
            self.__name = item_name

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', newline='') as csvfile:
            fieldnames = ['name', 'price', 'quantity']
            writer = csv.DictReader(csvfile, fieldnames=fieldnames)
        return cls(writer)

    @staticmethod
    def string_to_number():
        pass

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    def __repr__(self):
        module_name = "__main__"
        class_name = self.__class__.__name__
        return f"<{module_name}.{class_name} object at {hex(id(all))}>"
