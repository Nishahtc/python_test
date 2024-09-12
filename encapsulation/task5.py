class BankAccount:
    def __init__(self):
        self.__Bankname = "HDFC Bank"
        self.__account_number = 123456789 
        self.__owner_name = "Nisha Modi"        
        self.__balance = 1000

    def deposit(self, amount):
    
        if amount > 0:  
            self.__balance += amount
        return self.__balance 

    def withdraw(self, amount):
        if amount > 0:  
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        
        if 0 < amount <= self.__balance:
            self.__balance -= amount  
            return self.__balance  
        else:
            print("Insufficient balance or invalid amount.")
            return self.__balance  

    def get_balance(self):
        
        return self.__balance

    def get_account_info(self):

        return f"Bank: {self.__Bankname}, Account Number: {self.__account_number}, Owner: {self.__owner_name}, Balance: {self.__balance}"


obj = BankAccount() 
obj.__owner_name="sakshi"
print("Initial Balance:", obj.get_balance())      
print("Balance after deposit:", obj.deposit(500))
print("Balance after withdraw:", obj.withdraw(300))  
print("Account Info:", obj.get_account_info()) 
