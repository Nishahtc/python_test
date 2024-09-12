class data:
    def __init__(self):
        self.__amount=20000
    def getprice(self):
        return self.__amount
obj=data()  
obj.__amount=10000
print(obj.getprice())      
