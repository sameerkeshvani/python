from tkinter import *
import string
def prim():
    num = int(e1.get())
    flag = False
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                flag = True
                break
    if flag:
        myText.set(f"{num} is not a prime number")
    else:
        myText.set(f"{num} is a prime number")
def perf():
    n = int(e1.get())
    sum1 = 0
    for i in range(1,n):
        if(n%i==0):
            sum1 = sum1+ i
    if(sum1==n):
        myText.set(f"{n} The number is a pefect number!")
    else:
        myText.set(f"{n} The number is not a perfect number!")
def arms():
    num = int(e1.get())
    sum = 0
    temp = num
    while temp>0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        myText.set(f"{num} is an armstrong number")
    else:
        myText.set(f"{num} is not an armstrong number")
master = Tk()
master.geometry("300x150")
myText=StringVar()
Label(master, text="Enter a number :").grid(row = 0, sticky= W)
Label(master, text="Your answer is: ").grid(row=2, sticky=W)
result=Label(master, text = "", textvariable=myText).grid(row=2, column=1, sticky=W)
e1 = Entry(master, width=20)
e1.grid(row=0, column=1)
radio=StringVar()
b1= Radiobutton(master, text="Click to check prime or not", variable=radio, width=40, value=1, indicator=0, command=prim)
b1.grid(row=7, column=0, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)
b2 = Radiobutton(master, text="Click to chec perfect or not",variable=radio,width=40,value=2,indicator=0,command=perf)
b2.grid(row=10, column=0, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)
b3 = Radiobutton(master, text="Click to check armstrong or not", variable=radio, width=40, value=3, indicator=0, command=arms)
b3.grid(row=13,column=0,columnspan=2,rowspan=2,sticky=W+E+N+S,padx=5,pady=5)
mainloop()