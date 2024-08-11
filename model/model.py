from model.imodel import IModel
from phone import Phone

_DB: list[Phone] = []


class Model(IModel):
    def save_phone(self, phone: Phone):
        _DB.append(phone)

    def dell_phone(self, phone_privat: str):
        for i in range(len(_DB)):
            if _DB[i].phone_private == phone_privat:
                return _DB.pop(i)
        else:
            print("Контакт с таким номером телефона отсутсвует")

    def get_all_phones(self) -> list[Phone]:
        return _DB

    def search_phone(self, name: str):
        for i in range(len(_DB)):
            if _DB[i].name == name:
                return print(_DB[i])
        else:
            print("Нет контакта с данным именем")