##############################
#  Различные рисунки
#  согланные алгоритмами
##
###############################

from tkinter import *
import random

root = Tk()
root.title("Урок 22-10-2022")
root.geometry("850x850")

canvas = Canvas(bg="white", width=800, height=800)
canvas.pack(anchor=CENTER, expand=1)

canvas.create_rectangle(4, 4, 800, 800, width=8)

def setka():
    dd = 80
    d = 0
    for i in range(10):
        canvas.create_line(d, 0, d, 800)
        canvas.create_line(0, d, 800, d)
        d = d + dd

def shary_lines():
    mx = 0
    my = 0
    mascolor = ["black", "green", "red", "yellow", "blue"]

    for i in range(10):
        col = random.choice(mascolor)

        x = random.randint(1, 10) * dd - dd / 2
        y = random.randint(1, 10) * dd - dd / 2
        canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=col)
        if i != 0:
            canvas.create_line(mx, my, x, y, width=3, fill="green", dash=(4, 2))
        mx = x
        my = y

def kvadraty1():
    for x in range(20,800,10):
        canvas.create_rectangle(x, x, 800-x, 800-x)

def krugy1():
    for x in range(20,800,10):
        canvas.create_oval(x, x, 800-x, 800-x)

def linii1():
    for x in range(0,810,10):
        canvas.create_line(400, 400, x, 0)
        canvas.create_line(400, 400, 0, x)
        canvas.create_line(400, 400, x, 800)
        canvas.create_line(400, 400, 800, x)

def krugy2():
    for x in range(20,400,10):
        canvas.create_oval(x, x, 400-x, 400-x)
        canvas.create_oval(x+400, x, 400-x+400, 400-x)
        canvas.create_oval(x, x+400, 400-x, 400-x+400)
        canvas.create_oval(x+400, x+400, 400-x+400, 400-x+400)

def kvadraty2():
    dx=20
    for x in range(20,800,10):
        canvas.create_rectangle(dx, dx, x, x)
        dx=dx+5


def misen():
    k=0
    for x in range(20,400,20):
        k = k + 1
        if k % 2 == 0:
            col = "white"
        else:
            col = "black"
        canvas.create_oval(x, x, 800-x, 800-x, fill=col)
        canvas.create_line(400, 0, 400, 800, width=5)
        canvas.create_line( 0,400, 800, 400, width=5)


#krugy1()
#kvadraty1()
#linii1()
#krugy2()
#kvadraty2()
misen()

root.mainloop()
