class TransferResponse:
    def __init__(self):
        self.amount = None
        self.receiver_account_number = None
        self.sender_account_number = None

    def set_amount(self, amount):
        self.amount = amount

    def set_receiver_account_number(self, account_number):
        self.receiver_account_number = account_number

    def set_sender_account_number(self, account_number):
        self.sender_account_number = account_number

    def get_amount(self):
        return self.amount

    def get_receiver_account_number(self):
        return self.receiver_account_number

    def get_sender_account_number(self):
        return self.sender_account_number

    def __str__(self):
        return f"""
        TransferResponse(amount: {self.amount}
        receiver_account_number: {self.receiver_account_number}
        sender_account_number: {self.sender_account_number})"""
