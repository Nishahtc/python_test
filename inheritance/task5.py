class vehical:
    make=None
    model=None
    year=None
    def display(self):
        print("************ vehical ************\n ")
        print(f"make:{self.make}")
        print(f"model:{self.model}")
        print(f"year:{self.year}")
class Car(vehical):
    number_of_doors=None
    def display(self):
         print("************ car ************ ")
         print(f"make:{self.make}")
         print(f"model:{self.model}")
         print(f"year:{self.year}")



class motercycle(vehical):
    has_side_car=None
    def display(self):
         print("******************** ")
         print(f"make:{self.make}")
         print(f"model:{self.model}")
         print(f"year:{self.year}")
         print(f"Has side car:{self.has_side_car}")
obj=Car()         
obj.number_of_doors=4
obj.make="Thar"
obj.model="mahindri"
obj.year=2024
obj.display()


obj1=motercycle()
obj1.has_side_car="yes"
obj1.make="tvs"
obj.model="4x4"
obj.year=2024
obj.display()