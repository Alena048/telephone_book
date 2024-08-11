from model.model import Model
from vies.ConsoleVies import ConcoleVies
from controler.consol_controler import ConsolControler
from phone import Phone


def main():
    model = Model()
    vies = ConcoleVies()
    contr = ConsolControler(
        model=model, vies=vies
    )

    while True:
        user_input = input("1 - Добавить новый номер\n"
                           "2 - Показать всю телефонную книгу\n"
                           "3 - Удалить номер телефона из телефонной книги\n"
                           "4 - Найти по имени контакты\n"
                           "5 - Выйти из телефонной книги\n")
        if user_input == "1":
            contr.save_phone()
        if user_input == "2":
            contr.get_all_phones()
        if user_input == "3":
            contr.dell_phone()
        if user_input == "4":
            contr.search_phone()
        if user_input == "5":
            break

if __name__ == '__main__':
    main()


