class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            print("Deposit amount must be positive")
            return False

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Error: Insufficient funds")
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        print("Current Balance: $" self.account_balance)
        return self.account_balance
