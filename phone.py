import re

from pydantic import BaseModel, field_validator

class Phone(BaseModel):
    name: str
    surname: str
    phone_private: str
    phone_worker: str | None = None
    email: str = None

    @field_validator("phone_private")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+7\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+7" и содержать от 1 до 15 цифр')
        return values

    @field_validator("name", "surname")
    @classmethod
    def validate_name(cls, values: str) -> str:
        if not re.match(r'^[А-Я][а-яё]*$', values):
            raise ValueError('Имя и фамилия должны начинаться с заглавной буквы')
        return values

    @field_validator("phone_worker")
    @classmethod
    def validate_phone_number_work(cls, values: str) -> str:
        if values is None or values == "":
            return "Номер не указан"
        if not re.match(r'^\+7\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+7" и содержать от 1 до 15 цифр')
        return values

    @field_validator("email")
    @classmethod
    def validate_email(cls, values: str) -> str:
        if values is None or values == "":
            return "Электронная почта не указана"
        if not re.match(r'^\S+@\S+\.\S+$', values):
            raise ValueError('Должны содержаться имя, @, где зарегистирована почта через точку')
        return values