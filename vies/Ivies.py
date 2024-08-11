from abc import ABC, abstractmethod
from phone import Phone


class Iviev(ABC):
    @abstractmethod
    def get_phone(self) -> Phone:
        pass

    @abstractmethod
    def print_all_phone(self, phones: list[Phone]):
        pass

    @abstractmethod
    def del_phone(self) -> str:
        pass

    @abstractmethod
    def search_phone(self) -> str:
        pass