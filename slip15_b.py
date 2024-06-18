def displayoddvalues(string):
    for i in range(len(string)):
        if i%2 == 0:
            print(string[i])
string = input("Enter a string")
displayoddvalues(string)