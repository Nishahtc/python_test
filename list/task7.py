 #Define the path to the text file
path = r"D:\Nishatxt\nisha.txt"

# Open the file and read its contents
with open(path, 'r') as f:
    data = f.read()  # Read the entire content

# Split the content into words
words = data.split()

# Reverse the order of wordsi
reversed_words = words[::-1]

# Join the reversed words into a single string
reversed_data = ' '.join(reversed_words)

# Print the reversed content
print(reversed_data)