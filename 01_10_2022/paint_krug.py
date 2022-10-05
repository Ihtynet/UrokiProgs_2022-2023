from tkinter import *

root = Tk()
root.title("Урок 01-10-2022")
root.geometry("300x300")

canvas = Canvas(bg="white", width=260, height=260)
canvas.pack(anchor=CENTER, expand=1)

canvas.create_oval(10,10,250,250)
canvas.create_oval(60,60,100,100)
canvas.create_oval(160,60,200,100)
canvas.create_oval(60,160,200,200)
root.mainloop()
