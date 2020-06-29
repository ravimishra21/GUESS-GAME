from tkinter import *
from random import randint

root = Tk()

root.title("RAVI GUESS THE NUMBER")

root.geometry("1000x600")

class ValueSmallError(Exception):
    pass

class ValueLargeError(Exception):
    pass

ans = randint(1,100)

def guess():
    num = int(num1.get())

    try:
        if num > ans:
            raise ValueLargeError
        elif num < ans:
            raise ValueSmallError
        else:
            Label(root,text = "CONGRATULATIONS RAVI,HURAAY, !!!! YOU ARE WINNER!!!!",font=("times new roman",22,"bold"),bg="pink",border=11).grid(column=0,row=25)
    except ValueLargeError:
        Label(root, text =  "Guys , Your no is large, guess again",font=("times new roman",22,"bold"),bg="red",border=11).grid(column=0, row=25)
    except ValueSmallError:
        Label(root,text = "Guys , Your no is small, guess again",font=("times new roman",22,"bold"),bg="red",border=11).grid(column=0, row=25)
    return


Label(root,text="\t\t\t*** RAVI GUESS THE NUMBER ***",font=("times new roman",22,"bold"),bg="yellow",border=11).grid(column=0,row=0)

Label(root,text="\nGUESS THE NUMBER IS : (1-100)",font=("times new roman",19,"bold"),bg="blue",border=11).grid(columnspan=2,row=10)

num1 = Entry(root,font=("times new roman",19,"bold"),bg="orange")
num1.grid(column=1,row=10)

btn1 = Button(root,text="Submit",command=guess,font=("times new roman",13,"bold"),bg="pink",border=11).grid(column=1,row=15)

root.mainloop()
         

 
