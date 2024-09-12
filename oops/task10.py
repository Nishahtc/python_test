class Avg:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg_get(self):
        sum=0
        for val in self.marks:
            sum+=val
            average = sum / len(self.marks)
            print(s1.name, sum/3 )
s1=Avg("nisha",[90,92,91])
s1.Avg_get()
