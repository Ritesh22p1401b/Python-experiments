import tkinter as tk
from tkinter import *
window=tk.Tk()
window.title("This is Applicatiom Window")
window.geometry("475x500")


def press(input):
    length=len(screen.get())
    screen.insert(length,input)

def clear():
    screen.delete(0,"end")


def get_sign(sign,expression):
    value=expression.split(sign,1)
    return value

def add(a,b):
    return a+b



def equal():
    expression=screen.get()
    clear()
    try:

        if expression.find("+")>0:
            data=get_sign("+",expression)
            answer=add(data[0],data[1])

        elif expression.find("hello")>0:
            p="hello"
            return p



        screen.insert(0,answer)

    except:
        screen.insert(0,"Error")







frame = Frame(window, width=300, height=200, bg="gray11",borderwidth=2,
highlightbackground="black", highlightcolor="gray11", highlightthickness=2)
frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame.pack(expand=True) 





font=("Times New Roman Greek",14)
#Creating Screen and entering the value
scvalue = StringVar()
screen = Entry(frame, textvar=scvalue, font=font,relief=SUNKEN,borderwidth=2)
screen.pack(fill=X,ipadx=6,pady=8,padx=10) #padding of screen
scvalue.set("")




button1=Button(frame,text="hello",command=lambda:press("hello"),foreground="DarkOrange1",bg="gray1")
button1.place(relx=1.0,x=-100,y=100,anchor="ne")


button2=Button(frame,text="clear",command=clear)
button2.place(relx=1.0,x=-200,y=100,anchor="ne")


button2=Button(frame,text="+",command=lambda:press("+"))
button2.place(relx=1.0,x=-250,y=100,anchor="ne")


button2=Button(frame,text="=",command=equal)
button2.place(relx=1.0,x=-250,y=130,anchor="ne")

button=Button(frame,text="world",command=lambda:press("world"))
button.pack(side=BOTTOM,pady=5)






window.mainloop()

