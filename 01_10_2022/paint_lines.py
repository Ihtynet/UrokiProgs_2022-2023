import random
from tkinter import *

root = Tk()
root.title("Урок 10-10-2022")
root.geometry("300x300")

canvas = Canvas(bg="white", width=250, height=250)
canvas.pack(anchor=CENTER, expand=1)

x1 = random.randint(1,300)
y1 = random.randint(1,300)

for i in range(100):
    x2 = random.randint(1,300)
    y2 = random.randint(1,300)
    canvas.create_line(x1, y1, x2, y2)
    x1 = x2
    y1 = y2

root.mainloop()