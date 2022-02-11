# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Event Handler
# Once event occurred, show a dialog.
def eventhandler_digit(num):
    global result_label
    # get the text from a widget
    result = result_label.cget("text")
    result = result + str(num)
    # set the text to a widget
    result_label["text"] = result + "!"
    # show a dialog box
    messagebox.showinfo("Hello Python", "Hello World")
    return


def eventhandler_digit1():
    eventhandler_digit(1)
    return

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

result_label = ttk.Label(frm, text="0")
result_label.grid(column=0, columnspan=3, row=0, sticky="e")
ttk.Label(frm, text="Hello World!").grid(column=0, row=4)

# Quit button
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=5)
# Digits
# When binding an event and component, command cannot take any arguments.
button_1 = ttk.Button(frm, text="1", command=eventhandler_digit1).grid(column=0, row=1)
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
