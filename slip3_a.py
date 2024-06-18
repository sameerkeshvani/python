def is_key_present(x):
    d = {1:10, 2:20, 3:30, 4:40}
    if x in d:
        print("Key Exists")
        key=int(input("Enter the key to replace\n"))
        value=int(input("Enter the value to replace\n"))
        d.update({key:value})
        print("After updating dictionary is %s" %d)
    else:
        print("Key Does Not Exists")
is_key_present(4)