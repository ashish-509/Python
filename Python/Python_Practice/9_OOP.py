# Create a class BankAccount with:
    # deposit
    # withdraw
    # balance check
    # error handling for insufficient balance



class BankAccount:  
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}.")


# Example usage:
account = BankAccount()
account.deposit(100)
account.check_balance()
account.withdraw(30)
account.check_balance()
account.withdraw(80)
account.check_balance()
account.withdraw(-10)
account.deposit(-20)
