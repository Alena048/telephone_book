from phone import Phone
from model.imodel import IModel
from vies.Ivies import Iviev


class ConsolControler:
    def __init__(self, model: IModel, vies: Iviev):
        self.model = model
        self.vies = vies

    def save_phone(self):
        phone = self.vies.get_phone()
        self.model.save_phone(phone)

    def dell_phone(self):
        phone_privat = self.vies.del_phone()
        self.model.dell_phone(phone_privat)

    def get_all_phones(self):
        phones = self.model.get_all_phones()
        self.vies.print_all_phone(phones)

    def search_phone(self):
        name = self.vies.search_phone()
        self.model.search_phone(name)