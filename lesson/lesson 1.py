class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def deposit(self):
        return self.balance

    @deposit.setter
    def deposit(self, amount):
        self.balance += amount

    @property
    def withdraw(self):
        return self.balance

    @withdraw.setter
    def withdraw(self, neg_amount):
        self.balance -= neg_amount

    @property
    def close(self):
        return self.balance

    @close.deleter
    def close(self):
        self.balance = None

account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit = 500
print(account.balance)  # 1500

account.withdraw = 200
print(account.balance)  # 1300

del account.close
print(account.balance)  # 0