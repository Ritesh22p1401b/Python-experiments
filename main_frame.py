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




frame = Frame(window, width=300, height=200, bg="gray11",borderwidth=2,
highlightbackground="black", highlightcolor="gray11", highlightthickness=2)
frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame.pack(expand=True) 


frame1 = Frame(window, width=300, height=100, bg="gray11",borderwidth=2,
highlightbackground="black", highlightcolor="gray11", highlightthickness=2)
frame1.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame1.pack(expand=True) 


font=("Times New Roman Greek",14)
#Creating Screen and entering the value
scvalue = StringVar()
screen = Entry(frame, textvar=scvalue, font=font,relief=SUNKEN,borderwidth=2)
screen.pack(fill=X,ipadx=6,pady=8,padx=10) #padding of screen
scvalue.set("")




button1=Button(frame,text="place",command=lambda:press("Buton created using place method"),foreground="DarkOrange1",bg="gray1")
button1.place(relx=1.0,x=-100,y=100,anchor="ne")


button2=Button(frame,text="clear",command=clear)
button2.place(relx=1.0,x=-200,y=100,anchor="ne")



button=Button(frame,text="pack",command=lambda:press("button created by using pack method"))
button.pack(side=BOTTOM,pady=5)


button5=Button(frame1, text="grid button",command=lambda:press("button with grid"))
button5.grid(row=5,column=3)



window.mainloop()

