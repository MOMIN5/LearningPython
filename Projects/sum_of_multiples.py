
num = int(input("Enter the number: "))
limit = int(input("Enter the number of multiples of sum you want: "))
fact = 1
value = 0

while(fact <= limit):
    value = value + num * fact
    fact += 1
    
print(value)

'''
num = int(input("Enter the number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i
    
print(fact)
'''