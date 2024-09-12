class Vehical:
    def __init__(self,make,moble,year) :
        self.make=make
        self.moble=moble
        self.year=year
    def display_infov(self) :
        print(f"vecical info : {self.make} {self.moble} {self.year}")   
# Child Class: Car
class Car(Vehical):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)  # Call the constructor of the parent class
        self.number_of_doors = number_of_doors
                  