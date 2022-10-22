############################
# Рисуем котика
############################

from tkinter import *
root=Tk()
root.geometry("600x600")
root.title("Урок 22-10-2022")
canvas=Canvas(bg="white",width=600,height=600)
canvas.pack(anchor=CENTER,expand=1)
canvas.create_arc(400,300,530,500,start=20,extent=-145,style=CHORD,fill="orange",outline="orange")
canvas.create_polygon(100,500,200,50,250,150,350,150,400,50,500,500,fill="orange",outline="white")
canvas.create_oval(200,200,300,300,fill="white",outline="white")
canvas.create_oval(300,200,400,300,fill="white",outline="white")
canvas.create_oval(280,280,320,320,fill="black")
canvas.create_oval(345,245,355,255,fill="black")
canvas.create_oval(245,245,255,255,fill="black")
canvas.create_arc(200,200,400,370,start=-45,extent=-90,style=ARC,width=2)
canvas.create_line(300,300,300,370,width=2)
canvas.create_oval(200,470,300,520,fill="black")
canvas.create_oval(300,470,400,520,fill="black")
canvas.create_polygon(10,10,100,100,fill="black")

root.mainloop()