"""def marks():
    marks=int(input(" please enter marks:-"))
    if marks>80:
        print("merit 1st division")
    elif marks > 60:
        print("1st division")
    elif marks > 45:
        print("2nd division")
    elif marks <45 :
        print("fail")
    else:
        print("enter correct marks:-")

    
marks()"""
import json

def marks():
    # Prompt the user to enter marks
    student_id = input("Please enter student ID: ")
    marks = int(input("Please enter marks: "))

    # Determine the division based on the marks
    if marks > 80:
        result = "merit 1st division"
    elif marks > 60:
        result = "1st division"
    elif marks > 45:
        result = "2nd division"
    elif marks < 45:
        result = "fail"
    else:
        result= "enter correct marks"

    # Create a dictionary to hold the output
    output = {
        "student id":student_id,
        "marks": marks,
        "division":result
    }

    # Convert the dictionary to JSON format with custom formatting
    json_output = json.dumps(output, indent=2)

    # Print the JSON output
    print(json_output)

# Call the function
marks()