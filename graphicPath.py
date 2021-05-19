from tkinter import *


def printer(event):
    print("Как всегда очередной 'Hello World!'")


root = Tk()

c = Canvas(root, width=300, height=300, bg="white")
c.create_line([])
lab = Label(root, text="Схема соединения потребителей между собой", font="Arial 16")
lab.pack()

root.minsize(width=800, height=500)
root.mainloop()

# import tkinter
# root = tkinter.Tk()
