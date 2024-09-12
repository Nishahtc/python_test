class BankAccount:
    def _init_(self):
        self.__Bankname = "HDFC Bank"
        self.__account_number = 123456789 
        self.__owner_name = "Nisha Modi"        
        self.__balance = 100000

    def deposit(self, amount):
        if amount > 0:  
            self.__balance += amount
        return self.__balance 

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount  # Balance should be reduced when withdrawal happens
            return self.__balance
        else:
            return "Insufficient balance or invalid amount!"

    def get_balance(self):
        return self.__balance

    def get_account_info(self):
        return f"Bank: {self._Bankname}, Account Number: {self.account_number}, Owner: {self.owner_name}, Balance: {self._balance}"

# Example usage:
obj = BankAccount()
# To change the owner's name, use a proper method or setter (not direct access to private attributes)
# obj.__owner_name = "sakshi"  # This is not allowed as __owner_name is private

print("Initial Balance:", obj.get_balance())      
print("Balance after deposit:", obj.deposit(1000))
print("Balance after withdrawal:", obj.withdraw(2000))  
print("Account Info:", obj.get_account_info())