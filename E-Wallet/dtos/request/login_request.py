import decimal


class LoginRequest:

    def __init__(self):
        self.__account_number = ""
        self.__get_email = ""
        self.__phone_number: str = ""
        self.__gmail: str = ""
        self.__balance = 0.00
        self.__password: str = ""
        self.__full_name: str = ""

    def set_password(self, password: str):
        self.__password = password

    def get_password(self) -> str:
        return self.__password

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def set_balance(self, balance):
        self.__balance = balance

    def set_gmail(self, gmail):
        self.__gmail = gmail

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_full_name(self):
        return self.__full_name

    def get_account_balance(self):
        return self.__balance

    def get_phone_number(self):
        return self.__account_number

    def get_email(self):
        return self.__gmail

    def set_email(self, email):
        self.__gmail = email

    def set_account_balance(self, balance):
        self.__balance = balance

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_number(self):
        return self.__account_number

