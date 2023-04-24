from data.model.transaction_history import Transaction
from data.repository.transaction_history_repository import Transaction_History


class Transaction_History_Impl(Transaction_History):
    transactions = []
    counter = 0

    def save(self, transaction: Transaction) -> Transaction:
        self.transactions.append(transaction)
        self.counter += 1
        return transaction

    def count(self) -> int:
        return self.counter
