from tkinter import *
import tkinter.messagebox
root = tkinter.Tk()
root.title("When yo press a button the message will pop up")
root.geometry("500x300")
def onclick():
    tkinter.messagebox.showinfo("Welcome gfg.","Hi I am your message")
button = Button(root, text="click me", command=onclick, height=5, width=10)
button.pack(side="top")
root.mainloop()