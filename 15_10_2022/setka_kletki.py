from tkinter import *
import random

root = Tk()
root.title("Урок 15-10-2022")
root.geometry("850x850")

canvas = Canvas(bg="white", width=800, height=800)
canvas.pack(anchor=CENTER, expand=1)
dd=80
d=0
for i in range(10):
	canvas.create_line(d,0,d,800)
	canvas.create_line(0,d,800,d)
	d=d+dd

for i in range(10):
	x = random.randint(0,9)*dd
	y = random.randint(0,9)*dd
	canvas.create_rectangle(x, y, x+dd, y+dd, fill="black")

root.mainloop()