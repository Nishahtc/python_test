class BankAccount:
    def __init__(self):

        self.__Bankname="Hdfc bank"
        self.__account_number = 123456789 
        self.__owner_name = "Nisha modi"        
        self.__balance =100000

    def deposit(self, amount):
    
        if amount > 0:  
            self.__balance += amount
        return self.__balance 

    def withdraw(self, amount):
        
        if 0 < amount <= self.__balance:
            return self.__balance  

    def get_balance(self):

        return self.__balance

    def get_account_info(self):
        return f"Bank: {self.__Bankname}, Account Number: {self.__account_number}, Owner: {self.__owner_name}, Balance: {self.__balance}"

        
        



obj = BankAccount() 
obj.__owner_name="sakshi"
print("Initial Balance:", obj.get_balance())      
print("Balance after deposit:", obj.deposit(1000))
print("Balance after withdraw:", obj.withdraw(2000))  
print("Account Info:", obj.get_account_info()) 
            
