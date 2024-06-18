num = int(input("Enter a number"))
def prime():
    flag = 1
    for i in range(2,num):
        if num % i == 0:
            flag = 0
            print("%d is not a prime number"%num)
            break
    if flag == 1:
        print("%d is a prime number" %num)
def factorial():
    fact = 1
    i = 1
    while i<=num:
        fact = fact*i
        i+=1
    print("Factorial of %d is %d" %(num, fact))
prime()
factorial()