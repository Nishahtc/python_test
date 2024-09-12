class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
            print( s1.name,sum/3)

s1=Student("Nisha",[90, 95, 86])  
s1.name="pari"              
s1.get_avg()            