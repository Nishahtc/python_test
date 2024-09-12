# Define the path to the text file
path = r"D:\just_test\Nisha\python_test\list\num.txt"

# Open the file and read its contents line by line
with open(path, 'r') as f:
    lines = f.readlines()  # Read all lines into a list

# Reverse the list of lines and print each line
for line in reversed(lines):
    print(line, end='')  # Use end='' to avoid adding extra new lines