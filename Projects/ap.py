"""
Arithmetic Progression

an = a + (n-1)d

a - the first term of ap
n - the number of term
d - common difference
an - nth term
"""

a = int(input("Enter the first term: "))
n = int(input("Enter the number of term: "))
d = int(input("Enter the common difference: "))

an = a + (n-1) * d

print("The nth term is",an)