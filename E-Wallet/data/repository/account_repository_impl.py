from data.model.account import Account
from data.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):

    accounts: list[Account] = []
    counter = 0

    def delete(self, account_number: str) -> None:
        for account in self.accounts:
            if account.get_account_number() == account_number:
                self.accounts.remove(account)
                self.counter -= 1
                break

    def add(self, account: Account) -> Account:
        if account.get_account_number() == "":
            account_number = self.generate_account_number(account.get_phone_number())
            account.set_account_number(account_number)
            self.accounts.append(account)

        self.counter += 1
        return account

    @staticmethod
    def generate_account_number(phone_number: str) -> str:
        phone_number = phone_number.lstrip("0")
        account_number = phone_number
        return account_number

    def count(self) -> int:
        return self.counter

    def find_by_account_number(self, account_number: str) -> Account | None:
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def find_by_phone_number(self, phone_number) -> Account | None:
        for account in self.accounts:
            if account.get_phone_number() == phone_number:
                return account
        return None

