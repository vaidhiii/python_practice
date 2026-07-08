class Bank_Account:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount_deposit):
        self.balance += amount_deposit
        print(f"{amount_deposit} deposited successfully.")

    def withdraw(self, amount_withdrawn):
        if amount_withdrawn <= self.balance:
            self.balance = self.balance - amount_withdrawn
            print(f"{amount_withdrawn} withdrawn successfully.")

    def check_balance(self):
        print(f"Your Balance:{self.balance}")


account1 = Bank_Account("Rebecca Mikaelson", "2026077532", 100000)

account1.check_balance()
account1.deposit(200000)
account1.check_balance()
account1.withdraw(50000)
account1.check_balance()
