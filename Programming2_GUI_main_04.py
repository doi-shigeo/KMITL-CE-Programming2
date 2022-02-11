# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
from tkinter import ttk

# 04: define event handlers

# Event Handler
def eventhandler_clear():
    global result_label
    result_label["text"] = "0"
    return

# Common event handlers when pressing a digit button.
def eventhandler_digit(num):
    global result_label
    result = result_label.cget("text")
    if result != "0":
        result = result + str(num)
    else:
        result = str(num)
    result_label["text"] = result
    return

# event handlers for each button
# (there is a constraint that an event handler can't take ant argument)
# So delegation is used.
def eventhandler_digit1():
    eventhandler_digit(1)
    return
def eventhandler_digit2():
    eventhandler_digit(2)
    return
def eventhandler_digit3():
    eventhandler_digit(3)
    return
def eventhandler_digit4():
    eventhandler_digit(4)
    return
def eventhandler_digit5():
    eventhandler_digit(5)
    return
def eventhandler_digit6():
    eventhandler_digit(6)
    return
def eventhandler_digit7():
    eventhandler_digit(7)
    return
def eventhandler_digit8():
    eventhandler_digit(8)
    return
def eventhandler_digit9():
    eventhandler_digit(9)
    return
def eventhandler_digit0():
    eventhandler_digit(0)
    return

# start of the main program
root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

result_label = ttk.Label(frm, text="0")
result_label.grid(column=0, columnspan=3, row=0, sticky="e")
ttk.Label(frm, text="Hello World!").grid(column=0, row=4)

# Quit button
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=5)
# Digits
# When binding an event and component, command cannot take any arguments.
ttk.Button(frm, text="1", command=eventhandler_digit1).grid(column=0, row=1)
ttk.Button(frm, text="2", command=eventhandler_digit2).grid(column=1, row=1)
ttk.Button(frm, text="3", command=eventhandler_digit3).grid(column=2, row=1)
ttk.Button(frm, text="4", command=eventhandler_digit4).grid(column=0, row=2)
ttk.Button(frm, text="5", command=eventhandler_digit5).grid(column=1, row=2)
ttk.Button(frm, text="6", command=eventhandler_digit6).grid(column=2, row=2)
ttk.Button(frm, text="7", command=eventhandler_digit7).grid(column=0, row=3)
ttk.Button(frm, text="8", command=eventhandler_digit8).grid(column=1, row=3)
ttk.Button(frm, text="9", command=eventhandler_digit9).grid(column=2, row=3)
ttk.Button(frm, text="0", command=eventhandler_digit0).grid(column=1, row=4)

# Operators
ttk.Button(frm, text="C", command=eventhandler_clear).grid(column=0, row=4)
# ttk.Button(frm, text=" . ", command=root.destroy).grid(column=2, row=4)
ttk.Button(frm, text=" + ", command=root.destroy).grid(column=3, row=1)
ttk.Button(frm, text=" - ", command=root.destroy).grid(column=3, row=2)
ttk.Button(frm, text=" * ", command=root.destroy).grid(column=3, row=3)
ttk.Button(frm, text=" / ", command=root.destroy).grid(column=3, row=4)

root.mainloop()
