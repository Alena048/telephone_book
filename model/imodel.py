from phone import Phone
from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def save_phone(self, phone: Phone):
        pass

    @abstractmethod
    def dell_phone(self, phone_privat: int):
        pass

    @abstractmethod
    def get_all_phones(self) -> list[Phone]:
        pass

    @abstractmethod
    def search_phone(self, name: str):
        pass