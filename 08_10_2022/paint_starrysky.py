import random
from tkinter import *

root = Tk()
root.title("Урок 10-10-2022")
root.geometry("700x700")

canvas = Canvas(bg="black", width=600, height=600)
canvas.pack(anchor=CENTER, expand=1)

for i in range(700):
    x1 = random.randint(1,600)
    y1 = random.randint(1,600)
    r = random.randint(1,5)
    canvas.create_oval(x1, y1, x1+r, y1+r, fill="white")

for i in range(20):
    x1 = random.randint(1,600)
    y1 = random.randint(1,600)
    r = random.randint(5,10)
    canvas.create_oval(x1, y1, x1+r, y1+r, fill="white")

canvas.create_oval(200, 200, 250, 250, fill="white")

dx=0
dy=0
for k in range(10):
    canvas.create_oval(150+dx, 215+dy, 300-dx, 245-dx, outline="white")
    dx=dx+3
    dy=dy+2

canvas.create_oval(200, 200, 250, 250, fill="white", )
root.mainloop()