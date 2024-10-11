import tkinter as tk
from tkinter import *
frame=tk.Tk()
frame.title("This is Applicatiom Window")
frame.geometry("800x800")

canvas=tk.Canvas(frame,width=400,height=500,background="white")
canvas.pack()
canvas.create_line(50,50,350,50,fill="blue",width=2)
canvas.create_rectangle(100,100,300,200,outline="red",width=2 )
canvas.create_polygon(100,150,200,250,300,100,fill="yellow",outline="black",width=2)






frame.mainloop()

