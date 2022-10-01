from tkinter import *

root = Tk()
root.title("Урок 10-10-2022")
root.geometry("300x300")

canvas = Canvas(bg="white", width=250, height=250)
canvas.pack(anchor=CENTER, expand=1)

canvas.create_oval(60,60,110,210)

root.mainloop()
