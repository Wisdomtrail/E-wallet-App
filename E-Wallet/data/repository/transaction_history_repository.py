from data.model.transaction_history import Transaction


class Transaction_History:
    def save(self, wallet: Transaction) -> Transaction:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

