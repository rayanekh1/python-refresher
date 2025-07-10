# bank_account.py


class BankAccount:
    def __init__(self, owner_name, acct_num, starting_balance=0.0):
        self.owner = owner_name
        self.account_number = acct_num
        self.balance = float(starting_balance)

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("You can't deposit nothing or less. Try again.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds. Don’t try it.")
        if amount <= 0:
            raise Exception("Withdraw must be more than zero.")
        self.balance -= amount
        return self.balance

    def check_balance(self):
        # just making it easier to read
        return round(self.balance, 2)

    def __str__(self):
        return f"BankAccount(owner='{self.owner}', acct='{self.account_number}', balance=${self.balance:.2f})"
