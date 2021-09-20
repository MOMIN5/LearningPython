"""
"""

input_int = int(input("Enter the first number: "))
limit = int(input("How many numbers you want to generate?: "))

for i in range(1,(limit + 1)):
    print(input_int * i)