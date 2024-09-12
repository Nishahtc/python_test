#inheritance
class A:
    def vala(self):
        print("Welcome to india a")
class B:
    def valab(self):
        print("Welcome to india b")
class c(A,B):
    def valac(self):
        print("Welcome to india b")        
ob=c()
ob.vala()
ob.valab()        
ob.valac()       
