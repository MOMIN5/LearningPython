string = input("Enter a String: ")
vovels = ["a","o","i","e","u","A","O","I","E","U"]
for i in string:
    if i in vovels:
        print("i =",i.lower())