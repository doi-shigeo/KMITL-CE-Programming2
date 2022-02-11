# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#from tkinter import *
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# Anchor attribute doesn't work...
ttk.Label(frm, text="0").grid(column=0, columnspan=4, row=0)
ttk.Label(frm, text="Hello World!").grid(column=0, row=5)

# To show result
calc_result = ttk.Label(frm, text="")
calc_result.grid(column=0, columnspan=3, row=5)

# Quit button
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=5)
# Digits
ttk.Button(frm, text="1", command=root.destroy).grid(column=0, row=1)
ttk.Button(frm, text="2", command=root.destroy).grid(column=1, row=1)
ttk.Button(frm, text="3", command=root.destroy).grid(column=2, row=1)
ttk.Button(frm, text="4", command=root.destroy).grid(column=0, row=2)
ttk.Button(frm, text="5", command=root.destroy).grid(column=1, row=2)
ttk.Button(frm, text="6", command=root.destroy).grid(column=2, row=2)
ttk.Button(frm, text="7", command=root.destroy).grid(column=0, row=3)
ttk.Button(frm, text="8", command=root.destroy).grid(column=1, row=3)
ttk.Button(frm, text="9", command=root.destroy).grid(column=2, row=3)
ttk.Button(frm, text="0", command=root.destroy).grid(column=1, row=4)

# Operators
ttk.Button(frm, text=" C ", command=root.destroy).grid(column=0, row=4)
ttk.Button(frm, text=" . ", command=root.destroy).grid(column=2, row=4)
ttk.Button(frm, text=" + ", command=root.destroy).grid(column=3, row=1)
ttk.Button(frm, text=" - ", command=root.destroy).grid(column=3, row=2)
ttk.Button(frm, text=" * ", command=root.destroy).grid(column=3, row=3)
ttk.Button(frm, text=" / ", command=root.destroy).grid(column=3, row=4)

root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
