from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from dtos.request.withdraw_request import WithdrawRequest
from services.account_serviceImpl import AccountServiceImpl
from utils.account_not_found_exception import AccountNotFound
from utils.phone_number_exist_exception import PhoneNumberExist


class AccountController:
    def __init__(self):
        self.account_service = AccountServiceImpl()

    def register_account(self, create_account_request: CreateAccountRequest):
        try:
            response = self.account_service.register_account(create_account_request)
            return response
        except PhoneNumberExist as e:
            return str(e)

    def login(self, login_request: LoginRequest):
        try:
            response = self.account_service.login(login_request)
            return response
        except AccountNotFound as e:
            return str(e)

    def deposit(self, deposit_request: DepositRequest):
        try:
            response = self.account_service.deposit_into(deposit_request)
            return response
        except AccountNotFound as e:
            return str(e)

    def withdraw(self, withdraw_request: WithdrawRequest):
        try:
            response = self.account_service.withdraw(withdraw_request)
            return response
        except AccountNotFound as e:
            return str(e)

    def transfer(self, transfer_request: TransferRequest):
        try:
            response = self.account_service.transfer(transfer_request)
            return response
        except AccountNotFound as e:
            return str(e)
