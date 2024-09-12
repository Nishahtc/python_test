import json
def student():
    marks=int(input("enter student marks:-"))
    
    if marks>80:
        division="merit 1st division"
    elif marks>60:
        division="1st division"
    elif marks>45:
        division="2nd division"
    elif marks<45:
        division="fail"
    else:
        division="enter correct marks"
    output = {
        "marks": marks,
        "division": division,
        
    }

    
    json_data = json.dumps(output, indent=2)  

    
    print(json_data)

student()

  