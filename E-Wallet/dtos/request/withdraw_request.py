import decimal


class WithdrawRequest:

    def __init__(self):
        self.__account_number: str = ""
        self.__amount: decimal = 0.00

    def set_account_number(self, account_number: str):
        self.__account_number = account_number

    def get_account_number(self) -> str:
        return self.__account_number

    def set_amount(self, amount: decimal):
        self.__amount = amount

    def get_amount(self) -> decimal:
        return self.__amount


