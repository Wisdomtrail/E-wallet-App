import decimal


class DepositRequest:

    def __init__(self):
        self.__senders_name: str = ""
        self.__receivers_name: str = ""
        self.__receivers_account_number: str = ""
        self.__amount: decimal = 0.00
        self.__purpose: str = ""

    def set_senders_name(self, senders_name: str):
        self.__senders_name = senders_name

    def get_senders_name(self) -> str:
        return self.__senders_name

    def set_receivers_account_number(self, receivers_account_number: str):
        self.__receivers_account_number = receivers_account_number

    def get_receivers_account_number(self) -> str:
        return self.__receivers_account_number

    def set_amount(self, amount: decimal):
        self.__amount = amount

    def get_amount(self) -> decimal:
        return self.__amount

    def get_receivers_name(self) -> str:
        return self.__receivers_name

    def set_receivers_name(self, receivers_name: str):
        self.__receivers_name = receivers_name

    def get_purpose(self) -> str:
        return self.__purpose

    def set_purpose(self, purpose: str):
        self.__purpose = purpose
