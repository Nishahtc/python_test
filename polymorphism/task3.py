#overriding
class A:
    def displaya(self):
        print("Hii welcome")
class B(A):
    
    def display(self):
        super().displaya()
        print("hello")
        
         
obj=B()
obj.display()
