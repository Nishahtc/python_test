import os
path=r"D:\just_test\Nisha\python_test\list\num.txt"
def unique(num, unique_numbers):
    return num not in unique

def length(num):
    return 11 <= len(num) <= 16


def read_existing_numbers():
    if os.path.exists(path):
        with open(path, 'r') as file:
            return set(line.strip() for line in file)
    return set()
def main():
    



