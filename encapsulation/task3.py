class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.__account_number = 123456789
        self.__owner_name ="Nisha modi"
        self.__balance=50000

    def deposit(self, amount):
        self.__balance += abs(amount)

    def withdraw(self, amount):
        self.__balance -= abs(amount)

    def get_balance(self):
        return self.__balance

    def get_account_info(self):
        return f"Account Number: {self.__account_number}, Owner: {self.__owner_name}"
obj=BankAccount()   
print(obj.deposit(100))
print(obj.withdraw(200))
