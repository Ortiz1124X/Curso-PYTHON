from tkinter import *


def select():
    outLabel.config(text="Opción {}".format(option.get()))

def reset():
    option.set(int)
    outLabel.config(text="")


root = Tk()
root.title("RADIO_BUTTONS")
root.config(bd=90)

option = IntVar()

Radiobutton(root, text="Opción 1", variable=option, value=1, activebackground="light gray", activeforeground="blue",
            command=select).pack()

Radiobutton(root, text="Opción 2", variable=option, value=2, activebackground="light gray", activeforeground="blue",
            command=select).pack()

Radiobutton(root, text="Opción 3", variable=option, value=3, activebackground="light gray", activeforeground="blue",
            command=select).pack()

outLabel = Label(root)
outLabel.pack()

Button(root, text="RESET", command=reset).pack()

root.mainloop()
