from src.item import Item


class MixinLang:
    Lang = "EN"

    def __init__(self):
        self.__language = self.Lang

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_lang):
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        self.__language = ({"RU", "EN"} - {self.__language}).pop()
        return self


class KeyBoard(Item, MixinLang):
    def __init__(self, *args):
        super().__init__(*args)
