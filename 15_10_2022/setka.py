from tkinter import *
import random

# Создаем окно и канву
root = Tk()
root.title("Урок 15-10-2022")
root.geometry("850x850")
canvas = Canvas(bg="white", width=800, height=800)
canvas.pack(anchor=CENTER, expand=1)

# Рисуем окантовку
canvas.create_rectangle(4,4,800,800, width=8)

dd=80
d=0
for i in range(10):
	canvas.create_line(d,0,d,800)
	canvas.create_line(0,d,800,d)
	d=d+dd

mx=0
my=0
mascolor =["black","green","red","yellow","blue"]

for i in range(10):
	col = random.choice(mascolor)  # Получаем случайныйцвет из нашего массива
	x = random.randint(1,10) *dd-dd/2
	y = random.randint(1,10)*dd-dd/2
	canvas.create_oval(x-20,y-20, x+20,y+20, fill=col)
	if i !=0:
		canvas.create_line(mx,my,x,y, width=3, fill="green", dash=(4, 2)) # рисуем зеленую пунктирную линию
	mx=x  # запомнили текущую x
	my=y  # запомнили текущую y

# выводим окно
root.mainloop()