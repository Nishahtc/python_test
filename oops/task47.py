import json

def marks():
    marks = int(input("Please enter marks: "))

    if marks > 80:
        division = "merit 1st division"
    elif marks > 60:
        division = "1st division"
    elif marks > 45:
        division = "2nd division"
    elif marks < 45:
        division = "fail"
    else:
        division = "enter correct marks"

    # Create a dictionary to hold the output
    output = {
        "marks": marks,
        "division": division
    }
    # Convert the dictionary to JSON format
    json_output = json.dumps(output)

    # Print the JSON output
    print(json_output)

# Call the function
marks()