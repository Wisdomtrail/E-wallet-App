import decimal

from data.model.account import Account
from data.repository.account_repository_impl import AccountRepositoryImpl
from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from dtos.request.withdraw_request import WithdrawRequest
from dtos.response.login_response import LoginResponse
from dtos.response.register_response import RegisterResponse
from dtos.response.transfer_response import TransferResponse
from dtos.response.withdraw_response import WithdrawResponse
from services.account_service import AccountService
from utils.account_not_found_exception import AccountNotFound
from utils.mapper import Mapper
from utils.phone_number_exist_exception import PhoneNumberExist
from utils.wrong_details import WrongDetails


class AccountServiceImpl(AccountService):
    account_repository = AccountRepositoryImpl()
    account = Account()

    def __init__(self):
        pass

    def register_account(self, create_account_request: CreateAccountRequest) -> RegisterResponse:
        if self.phone_number_exist(create_account_request.get_phone_number()):
            raise PhoneNumberExist(create_account_request.get_phone_number() + " " + "already exist")

        account = Mapper.map_request_with_account(create_account_request)
        saved_account = self.account_repository.add(account)
        response = Mapper.map_account_with_response(saved_account)
        return response

    def phone_number_exist(self, phone_nuber):
        phone_nuber = self.account_repository.find_by_phone_number(phone_nuber)
        if phone_nuber is not None:
            return True
        return False

    @staticmethod
    def validate_password(password):
        pass

    def login(self, login_request: LoginRequest) -> LoginResponse:
        account = self.account_repository.find_by_account_number(login_request.get_account_number())
        if account is None or account.get_password() != login_request.get_password():
            raise AccountNotFound("Account not found..")

        login_request.set_full_name(account.get_first_name() + " " + account.get_last_name())
        login_request.set_account_balance(account.get_balance())
        login_request.set_email(account.get_gmail())
        login_request.set_phone_number(account.get_phone_number())
        login_response = Mapper.map_login_request_with_response(login_request)
        return login_response

    def deposit_into(self, deposit_request: DepositRequest) -> str:
        if not self.account_not_found(deposit_request.get_receivers_account_number()):
            raise AccountNotFound("Account not found..")

        receiver_account = self.account_repository.find_by_account_number(
            deposit_request.get_receivers_account_number())
        response = Mapper.map_deposit_request_to_response(deposit_request)
        receiver_account.add_to_balance(deposit_request.get_amount())
        return response

    def check_balance(self, account_number: str) -> decimal:
        account = self.account_repository.find_by_account_number(account_number)
        return account.get_balance()

    def account_not_found(self, account):
        account_number = self.account_repository.find_by_account_number(account)
        if account_number is not None:
            return True
        return False

    def withdraw(self, withdraw_request: WithdrawRequest) -> WithdrawResponse:
        account = self.account_repository.find_by_account_number(withdraw_request.get_account_number())
        if account is None:
            raise AccountNotFound("Account not found..")
        account = self.account_repository.find_by_account_number(withdraw_request.get_account_number())
        account.withdraw_from_balance(withdraw_request.get_amount())
        withdraw_response = Mapper.map_withdraw_request_to_response(withdraw_request)
        return withdraw_response

    def transfer(self, transfer_request: TransferRequest) -> TransferResponse:
        sender_account = self.account_repository.find_by_account_number(transfer_request.get_sender_account_number())
        receiver_account = self.account_repository.find_by_account_number(
            transfer_request.get_receiver_account_number())
        if sender_account is None or receiver_account is None:
            raise AccountNotFound("Account not found..")
        sender_account.withdraw_from_balance(transfer_request.get_amount())
        receiver_account.add_to_balance(transfer_request.get_amount())
        transfer_response = Mapper.map_transfer_request_with_response(transfer_request)
        return transfer_response

