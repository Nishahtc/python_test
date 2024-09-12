import json

class Student:
    def __init__(self, marks):
        self.marks = marks
        self.division = self.calculate_division()

    def calculate_division(self):
        if self.marks > 80:
            return "merit 1st division"
        elif self.marks > 60:
            return "1st division"
        elif self.marks > 45:
            return "2nd division"
        elif self.marks < 45:
            return "fail"
        else:
            return "enter correct marks"

    def to_json(self):
        output = {
            "marks": self.marks,
            "division": self.division,
        }
        return json.dumps(output, indent=2)

def main():
    try:
        marks = int(input("Enter student marks: "))
        student = Student(marks)
        print(student.to_json())
    except ValueError:
        print("Please enter a valid integer for marks.")

if __name__ == "__main__":
    main()
