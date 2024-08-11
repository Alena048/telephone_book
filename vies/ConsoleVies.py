from vies.Ivies import Iviev
from phone import Phone


class ConcoleVies(Iviev):
    def get_phone(self, mes_name: str = "Введите имя контакта\n",
                  mes_surname: str = "Введите фамилию контакта\n",
                  mes_phone_private: str = "Введите личный номер контакта\n",
                  mes_phone_worker: str = "Введите рабочий номер контакта\n",
                  mes_email: str = "Введите электорнную почту контакта\n") -> Phone:
        name = input(mes_name)
        surname = input(mes_surname)
        phone_private = input(mes_phone_private)
        phone_worker = input(mes_phone_worker)
        email = input(mes_email)
        return Phone(
            name=name,
            surname=surname,
            phone_private=phone_private,
            phone_worker=phone_worker,
            email=email
        )

    def del_phone(self, mes: str = "Введите номер контакта для удаления\n") -> str:
        return input(mes)

    def print_all_phone(self, phones: list[Phone]):
        for phone in phones:
            print(phone)
            print("*"*30)

    def search_phone(self, mes_name: str = "Введите имя контакта для поиска\n"):
        return input(mes_name)