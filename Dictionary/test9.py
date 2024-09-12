


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 5, 'c': 4}

# Merge the dictionaries
merged_dict = {**dict1, **dict2}

# Sort the merged dictionary by values
sorted_dict = sorted(merged_dict.items(), key=lambda x: x[1])

# Print the sorted dictionary
print(sorted_dict)
