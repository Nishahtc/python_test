import numpy as np
def create_array_from_input():
    print("Enter the elements of the array row by row, separated by spaces.")
    rows = int(input("Enter the number of rows: "))
    
    array_list = []
    for i in range(rows):
        row_input = input(f"Enter elements for row {i + 1}: ")
        row = list(map(int, row_input.split()))  # Convert input string to a list of integers
        array_list.append(row)
    
    return np.array(array_list)

# Create the array from user input
arr = create_array_from_input()
print("Original array:")
print(arr)

# Find unique elements
unique_elements = np.unique(arr)
print("Unique elements:")
print(unique_elements)