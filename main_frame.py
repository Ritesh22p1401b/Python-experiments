import tkinter as tk
from tkinter import *
frame=tk.Tk()
frame.title("This is Applicatiom Window")
frame.geometry("475x425")

# canvas=tk.Canvas(frame,width=600,height=500,background="white")
# canvas.pack()
# canvas.create_line(50,50,350,50,fill="blue",width=2)
# canvas.create_rectangle(100,100,300,200,outline="red",width=2 )
# canvas.create_polygon(100,150,200,250,300,100,fill="yellow",outline="black",width=2)


# canvas.create_text(300,350,text="Tkinter Canvas drawing",font=("serif",16),fill="purple")

# canvas.create_oval(90,20,210,90,width = 2,fill="yellow")
# canvas.create_line(90,90,300,90)


button1=Button(frame,text="ok")
button2=Button(frame,text="cancel")
button1.pack(side=TOP,pady=5)
button2.pack(side=BOTTOM,pady=5)

frame.mainloop()

