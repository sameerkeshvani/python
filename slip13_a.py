try:
    num = int(input("Enter a number"))
    if num < 0:
        raise ValueError
except ValueError:
    print("Not a positive integer")
else:
    print("It is a positive number %d" %num)