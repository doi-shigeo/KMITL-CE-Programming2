# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# This code refers to https://docs.python.org/3/library/tkinter.html
# by Shigeo DOI 19/Nov/2021

# This program is derived from "A Hello World Program" in https://docs.python.org/3/library/tkinter.html

from tkinter import *
from tkinter import ttk
root = Tk() # Initialize Tk. Making a window.
frm = ttk.Frame(root, padding=10) # Make a frame widget
frm.grid() # Use window as a grid layout
ttk.Label(frm, text="Hello World!").grid(column=0, row=0) # Add a label
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0) # Add a button to quit
root.mainloop()




