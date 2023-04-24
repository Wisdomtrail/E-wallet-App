import unittest

from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from dtos.request.withdraw_request import WithdrawRequest
from services.account_serviceImpl import AccountServiceImpl


class TestAccountServiceImpl(unittest.TestCase):
    request = CreateAccountRequest()
    service = AccountServiceImpl()

    @classmethod
    def setUpClass(cls):
        cls.service = AccountServiceImpl()
        cls.request = CreateAccountRequest()
        cls.request.set_first_name("John")
        cls.request.set_last_name("Doe")
        cls.request.set_gmail("john@gmail.com")
        cls.request.set_phone_number("09152652431")
        cls.request.set_password("password")
        cls.response = cls.service.register_account(cls.request)
        cls.service = AccountServiceImpl()
        cls.request = CreateAccountRequest()
        cls.request.set_password("password")
        cls.request.set_first_name("zainab")
        cls.request.set_last_name("Doe")
        cls.request.set_gmail("zainab@gmail.com")
        cls.request.set_phone_number("08134132226")
        cls.response = cls.service.register_account(cls.request)

    def test_register_account(self):
        expected = """
         Account Number: 9152652431
         Gmail: john@gmail.com
         Full Name: John Doe
         Balance: 0.0"""
        self.assertEqual(expected, self.response.__str__())

    def test_login(self):
        request = LoginRequest()
        request.set_phone_number("09152652431")
        request.set_password("password")
        request.set_account_number("9152652431")
        response = self.service.login(request)
        expected = """
        full_name: John Doe
        email: john@gmail.com
        phone_number: 9152652431
        account_balance: 0.0"""
        self.assertEqual(expected, response.__str__())

    def test_deposit(self):
        request = DepositRequest()
        request.set_amount(100)
        request.set_receivers_account_number("9152652431")
        request.set_senders_name("sunday")
        request.set_receivers_name("zainab")
        response = self.service.deposit_into(request)
        expected = """
        Senders Name: sunday
        Receivers Account: 9152652431
        Receivers Name: zainab
        Balance: 100"""
        self.assertEqual(expected, response.__str__())

    def test_withdraw(self):
        request = DepositRequest()
        request.set_amount(100)
        request.set_receivers_account_number("9152652431")
        request.set_senders_name("sunday")
        request.set_receivers_name("zainab")
        self.service.deposit_into(request)

        request = WithdrawRequest()
        request.set_amount(10)
        request.set_account_number("9152652431")
        response = self.service.withdraw(request)
        balance = self.service.check_balance("9152652431")

        expected = """
        Amount: 10
        location: E-Wallet
        Account_Number: 9152652431"""
        self.assertEqual(expected, response.__str__())
        self.assertEqual(90, balance)

    def test_transfer(self):
        deposit_request = DepositRequest()
        deposit_request.set_amount(100)
        deposit_request.set_receivers_account_number("9152652431")
        deposit_request.set_senders_name("sunday")
        deposit_request.set_receivers_name("zainab")
        self.service.deposit_into(deposit_request)

        request = TransferRequest()
        request.set_amount(50)
        request.set_receiver_account_number("8134132226")
        request.set_sender_account_number("9152652431")
        response = self.service.transfer(request)

        expected = """
        TransferResponse(amount: 50
        receiver_account_number: 8134132226
        sender_account_number: 9152652431)"""
        self.assertEqual(expected, response.__str__())
        self.assertEqual(50, self.service.check_balance("8134132226"))
        self.assertEqual(50,self.service.check_balance("9152652431"))