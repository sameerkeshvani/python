string = input("Enter a string")
lower = 0
upper = 0
for s in string:
    if ord(s) >=97 and ord(s) <=122:
        lower +=1
    elif ord(s) >=65 and ord(s) <=90:
        upper +=1
print("Lower case : %d" %lower)
print("Upper case : %d" %upper)