from data.model.transaction_history import Transaction


class TransactionService:

    def find_all_transaction(self) -> Transaction:
        raise NotImplementedError

    def find_transaction_by_id(self, identity_number: int) -> Transaction:
        raise NotImplementedError

    def view_all_debit_transaction(self):
        raise NotImplementedError

    def view_all_credit_transaction(self):
        raise NotImplementedError
