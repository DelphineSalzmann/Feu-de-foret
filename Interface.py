from tkinter import *
from functools import partial
from paysage import grille, paysage


root = Tk()

value = IntVar(root)
scale = Scale(root, from_=-80, to=80, showvalue=True, label="Vent Vx :",
              variable=value, tickinterval=40, orient='h', sliderlength=20)
entry = Entry(root, textvariable=value)

scale.grid(row=0, column=0)
entry.grid(row=0, column=1)

value = IntVar(root)
scale = Scale(root, from_=-80, to=80, showvalue=True, label="Vent Vy :",
              variable=value, tickinterval=40, orient='h', sliderlength=20)
entry = Entry(root, textvariable=value)

scale.grid(row=1, column=0)
entry.grid(row=1, column=1)

Button(root, text="Start", command=root.quit).grid(
    row=3, column=3, sticky=W, pady=4)

init = paysage(grille())
init.grid(row=0, column=4)


root.mainloop()
