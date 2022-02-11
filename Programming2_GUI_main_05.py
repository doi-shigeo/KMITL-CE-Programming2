# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from tkinter import ttk

# 04: define event handlers (for digits)
# 05: define event handlers (for operators)

# Event Handler
def eventhandler_clear():
    global result_label
    result_label["text"] = "0"
    return

def eventhandler_eval():
    global result_label
    result_label["text"] = str(eval(result_label["text"]))
    return

def eventhandler_operators(op):
    global result_label
    result_label["text"] = result_label["text"] + op
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
def eventhandler_digit_1():
    eventhandler_digit(1)
    return
def eventhandler_digit_2():
    eventhandler_digit(2)
    return
def eventhandler_digit_3():
    eventhandler_digit(3)
    return
def eventhandler_digit_4():
    eventhandler_digit(4)
    return
def eventhandler_digit_5():
    eventhandler_digit(5)
    return
def eventhandler_digit_6():
    eventhandler_digit(6)
    return
def eventhandler_digit_7():
    eventhandler_digit(7)
    return
def eventhandler_digit_8():
    eventhandler_digit(8)
    return
def eventhandler_digit_9():
    eventhandler_digit(9)
    return
def eventhandler_digit_0():
    eventhandler_digit(0)
    return

def eventhandler_op_asterisk():
    eventhandler_operators('*')
    return
def eventhandler_op_slash():
    eventhandler_operators('/')
    return
def eventhandler_op_plus():
    eventhandler_operators('+')
    return
def eventhandler_op_minus():
    eventhandler_operators('-')
    return



# start of the main program
root = Tk()
root.title("Simple Calc") # Set title name
frm = ttk.Frame(root, padding=10)
frm.grid()

result_label = ttk.Label(frm, text="0", font=("Times", 20))
result_label.grid(column=0, columnspan=3, row=0, sticky="e")
ttk.Label(frm, text="Hello World!").grid(column=0, row=5)

# Quit button
# root.destroy indicates quit the app.
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=5)
# Digits
# When binding an event and a component, command cannot take any argument.
ttk.Button(frm, text="1", command=eventhandler_digit_1).grid(column=0, row=1)
ttk.Button(frm, text="2", command=eventhandler_digit_2).grid(column=1, row=1)
ttk.Button(frm, text="3", command=eventhandler_digit_3).grid(column=2, row=1)
ttk.Button(frm, text="4", command=eventhandler_digit_4).grid(column=0, row=2)
ttk.Button(frm, text="5", command=eventhandler_digit_5).grid(column=1, row=2)
ttk.Button(frm, text="6", command=eventhandler_digit_6).grid(column=2, row=2)
ttk.Button(frm, text="7", command=eventhandler_digit_7).grid(column=0, row=3)
ttk.Button(frm, text="8", command=eventhandler_digit_8).grid(column=1, row=3)
ttk.Button(frm, text="9", command=eventhandler_digit_9).grid(column=2, row=3)
ttk.Button(frm, text="0", command=eventhandler_digit_0).grid(column=1, row=4)

# Operators
ttk.Button(frm, text="C", command=eventhandler_clear).grid(column=0, row=4)
ttk.Button(frm, text="=", command=eventhandler_eval).grid(column=2, row=4)
ttk.Button(frm, text="+", command=eventhandler_op_plus).grid(column=3, row=1)
ttk.Button(frm, text="-", command=eventhandler_op_minus).grid(column=3, row=2)
ttk.Button(frm, text="*", command=eventhandler_op_asterisk).grid(column=3, row=3)
ttk.Button(frm, text="/", command=eventhandler_op_slash).grid(column=3, row=4)

root.mainloop()
