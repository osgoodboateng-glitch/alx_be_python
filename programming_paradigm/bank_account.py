class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        elif amount <= 0:
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        # Return balance formatted to 2 decimal places
        return f"Current Balance: ${self.account_balance:.2f}"
