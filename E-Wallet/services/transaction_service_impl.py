from data.model.transaction_history import Transaction
from services.transaction_service import TransactionService


class TransactionServiceImpl(TransactionService):
    def find_all_transaction(self) -> Transaction:
        pass

    def find_transaction_by_id(self, identity_number: int) -> Transaction:
        pass

    def view_all_debit_transaction(self):
        pass

    def view_all_credit_transaction(self):
        pass