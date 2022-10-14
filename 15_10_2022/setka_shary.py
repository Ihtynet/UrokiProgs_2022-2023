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
	
for i in range(40):
	x = random.randint(1,10) *dd-dd/2
	y = random.randint(1,10)*dd-dd/2
	canvas.create_oval(x-20,y-20, x+20,y+20, fill="black")
	
root.mainloop()