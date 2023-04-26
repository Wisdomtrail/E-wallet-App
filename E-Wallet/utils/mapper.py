from data.model.account import Account
from data.repository.account_repository_impl import AccountRepositoryImpl
from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from dtos.request.withdraw_request import WithdrawRequest
from dtos.response.deposit_response import DepositResponse
from dtos.response.login_response import LoginResponse
from dtos.response.register_response import RegisterResponse
from dtos.response.transfer_response import TransferResponse
from dtos.response.withdraw_response import WithdrawResponse


class Mapper:

    @staticmethod
    def map_request_with_account(request: CreateAccountRequest) -> Account:
        account = Account()
        account.set_gmail(request.get_gmail())
        account.set_last_name(request.get_last_name())
        account.set_first_name(request.get_first_name())
        account.set_phone_number(request.get_phone_number())
        account.set_password(request.get_password())
        return account

    @staticmethod
    def map_account_with_response(account: Account):
        response = RegisterResponse()
        response.set_account_number(account.get_account_number())
        response.set_gmail(account.get_gmail())
        response.set_full_name(account.get_first_name() + " " + account.get_last_name())
        response.set_balance(account.get_balance())
        return response

    @staticmethod
    def map_deposit_request_to_response(deposit_request: DepositRequest):
        response = DepositResponse()
        account_repo = AccountRepositoryImpl()
        account = account_repo.find_by_account_number(deposit_request.get_receivers_account_number())
        response.set_receiver_account(deposit_request.get_receivers_account_number())
        response.set_receivers_name(account.get_first_name() + " " +account.get_last_name())
        response.set_amount(deposit_request.get_amount())

        return response

    @staticmethod
    def map_withdraw_request_to_response(request: WithdrawRequest) -> WithdrawResponse:
        response = WithdrawResponse()
        response.set_amount(request.get_amount())
        response.set_account_number(request.get_account_number())
        return response

    @staticmethod
    def map_login_request_with_response(request: LoginRequest):
        response = LoginResponse()
        response.set_full_name(request.get_full_name())
        response.set_phone_number(request.get_phone_number())
        response.set_email(request.get_email())
        response.set_account_balance(request.get_account_balance())
        return response

    @staticmethod
    def map_transfer_request_with_response(transfer_request: TransferRequest):
        response = TransferResponse()
        response.set_amount(transfer_request.get_amount())
        response.set_receiver_account_number(transfer_request.get_receiver_account_number())
        response.set_sender_account_number(transfer_request.get_sender_account_number())
        return response
