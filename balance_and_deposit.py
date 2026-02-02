class InsufficientBalanceError(Exception):
    pass
class InvalidAmountError(Exception):
    pass
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    @property
    def balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.__balance -= amount
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.balance)