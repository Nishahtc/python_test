class Account:
    def __init__(self,bal,acc_no) :
        self.balance=bal
        self.acc_no=acc_no
    def debite(self,amount):
        self.balance-=amount
        print(amount) 
        print(self.get_blance())
    def credite(self,amount) :
        self.balance+=amount
        print(amount)
        print(self.get_blance())
    def get_blance(self) :
        return self.balance   

acc1=Account(10000,12345) 
print(acc1.balance) 
print(acc1.acc_no)      
acc1=credits(5000)  
   

