import tkinter as tk
from tkinter import messagebox, simpledialog
import re

from controllers.account_controller import AccountController
from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest

account_controller = AccountController()


def input_collector(prompt):
    root = tk.Tk()
    root.withdraw()
    collect_user_input = tk.simpledialog.askstring(title="Input", prompt=prompt)
    return collect_user_input


def display(prompt):
    messagebox.showinfo("Message", prompt)


def sign_up_page():
    page = """
    1. Login
    2. Register"""
    user_input = input_collector(page)

    if user_input == "1":
        login()
    elif user_input == "2":
        register_account()
    else:
        sign_up_page()


def login():
    account_number = input_collector("Enter your account Number")
    password = input_collector("Enter your account Password")
    login_request = LoginRequest()
    login_request.set_password(password)
    login_request.set_account_number(account_number)
    response = account_controller.login(login_request)
    display(response)
    sign_up_page()


def is_valid_nigerian_phone_number(phone_number):
    pattern = r"^(080|081|090|070|091)\d{8}$"
    return bool(re.match(pattern, phone_number))


def deposit():
    request = DepositRequest()
    account_number = input_collector("Enter account Number")
    amount = input_collector("Enter amount")
    request.set_amount(amount)
    request.set_receivers_account_number(account_number)
    response = account_controller.deposit(request)
    display(response)
    home_page()


def withdraw():
    pass


def transfer():
    pass


def check_balance():
    pass


def home_page():
    home = """
    1. Deposit
    2. Withdraw
    3. Transfer
    4. Check Balance
    5. Logout
    """
    user_input = input_collector(home)
    if user_input == "1":
        deposit()
    elif user_input == "2":
        withdraw()
    elif user_input == "3":
        transfer()
    elif user_input == "4":
        check_balance()
    elif user_input == "5":
        sign_up_page()


def register_account():
    first_name = input_collector("Enter first name")
    last_name = input_collector("Enter last name")
    while True:
        phone_number = input_collector("Enter your valid phoneNumber")
        if is_valid_nigerian_phone_number(phone_number):
            break
        else:
            display("Invalid phone number. Please enter a valid Nigerian phone number.")
    email = input_collector("Enter your email address")
    password = input_collector("Create a password for your E-wallet Account")
    register_account_request = CreateAccountRequest()
    register_account_request.set_password(password)
    register_account_request.set_phone_number(phone_number)
    register_account_request.set_gmail(email)
    register_account_request.set_last_name(last_name)
    register_account_request.set_first_name(first_name)
    response = account_controller.register_account(register_account_request)
    display(response)
    home_page()


if __name__ == "__main__":
    sign_up_page()
