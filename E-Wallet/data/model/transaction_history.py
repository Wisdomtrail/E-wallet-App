class Transaction:

    def __init__(self):
        self.__id: int = 0
        self.__amount: float = 0.00
        self.__transaction_type = None
        self.__sender_name = None

    def set_id(self, identity_number: int):
        self.__id = identity_number

    def get_id(self) -> int:
        return self.__id

    def set_amount(self, amount: float):
        self.__amount = amount

    def get_amount(self) -> float:
        return self.__amount

    def set_transfer_type(self, transaction_type: str):
        self.__transaction_type = transaction_type

    def get_transaction_type(self, identity_number) -> str:
        return self.__transaction_type
