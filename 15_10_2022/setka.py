from tkinter import *
import random

root = Tk()
root.title("Урок 15-10-2022")
root.geometry("850x850")

canvas = Canvas(bg="white", width=800, height=800)
canvas.pack(anchor=CENTER, expand=1)
dd=80
d=0
canvas.create_rectangle(3,3,800,800, width=15)

for i in range(10):
	canvas.create_line(d,0,d,800)
	canvas.create_line(0,d,800,d)
	d=d+dd

"""
canvas.create_line(0,d,800,d, , fill='green',
                width=5, arrow=LAST, dash=4,2),
                activefill='lightgreen',
                arrowshape="10 20 10" )
Опция dash позволяет создать пунктированную линию. Множества (4, 3) означает:
4 — длинна тире или точки в пикселях;
2 — пустой промежуток между тире либо точками.
"""

root.mainloop()