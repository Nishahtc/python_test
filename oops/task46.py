import json

def marks():
    marks = int(input("Please enter marks: "))
    result = {}

    if marks > 80:
        result["division"] = "merit 1st division"
    elif marks > 60:
        result["division"] = "1st division"
    elif marks > 45:
        result["division"] = "2nd division"
    elif marks < 45:
        result["division"] = "fail"
    else:
        result["error"] = "Please enter correct marks."

    # Print the result in JSON format
    print(json.dumps(result, indent=4))

marks()