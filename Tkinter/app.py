
# called tkinter
from tkinter import *
# called root Tk

import mysql.connector


midb = mysql.connector.connect(
    host='localhost',
    user='savecode',
    password='0986778998Salva!',
    database='sql_test',
)

root = Tk()

# Enterside value
display = Entry(root)

# location grid in row one and column one and width
# sticky = W+E is teh West and Est
display.grid(row=1, columnspan=6, sticky=W+E)

# index for display

i = 0


def get_numbers(num):
    global i
    display.insert(i, num)
    i += 1


def get_operators(operator):
    global i
    operator_lenght = len(operator)
    display.insert(i, operator)
    i += operator_lenght


def remove_characters():
    global i
    display.delete(i)
    i -= 1

def clear_display():
    global i
    display.delete(0, END)
    i=0

def calculate():
    display_state = display.get()
    try:
      result = eval(display_state)
      clear_display()
      display.insert(0, result)

    except EXCEPTION as Identitier:
      clear_display()
      display.insert(0, "ERROR")




# size for window
root.title("Tkinter GUI")

# created buttons

Button(root, text="1", command=lambda: get_numbers(1)).grid(
    row=2, column=0, sticky=W+E)

Button(root, text="2", command=lambda: get_numbers(2)).grid(
    row=2, column=1, sticky=W+E)

Button(root, text="3", command=lambda: get_numbers(3)).grid(
    row=2, column=2, sticky=W+E)

Button(root, text="+", command=lambda: get_operators("+")
       ).grid(row=2, column=3, sticky=W+E)

Button(root, text="4", command=lambda: get_numbers(4)).grid(
    row=3, column=0, sticky=W+E)

Button(root, text="5", command=lambda: get_numbers(5)).grid(
    row=3, column=1, sticky=W+E)

Button(root, text="6", command=lambda: get_numbers(6)).grid(
    row=3, column=2, sticky=W+E)

Button(root, text="-", command=lambda: get_operators("-")
       ).grid(row=3, column=3, sticky=W+E)

Button(root, text="7", command=lambda: get_numbers(7)).grid(
    row=4, column=0, sticky=W+E)

Button(root, text="8", command=lambda: get_numbers(8)).grid(
    row=4, column=1, sticky=W+E)

Button(root, text="9", command=lambda: get_numbers(9)).grid(
    row=4, column=2, sticky=W+E)

Button(root, text="*", command=lambda: get_operators("*")
       ).grid(row=4, column=3, sticky=W+E)

# options and zero

Button(root, text="^2", command=lambda: get_operators(
    "**2")).grid(row=5, column=0, sticky=W+E)

Button(root, text="0", command=lambda: get_numbers(0)).grid(
    row=5, column=1, sticky=W+E)

Button(root, text="%", command=lambda: get_operators(
    "%")).grid(row=5, column=2, sticky=W+E)

Button(root, text="/", command=lambda: get_operators("/")
       ).grid(row=5, column=3, sticky=W+E)


Button(root, text="AC", command=lambda: clear_display()).grid(row=6,
                                                                  column=0, sticky=W+E, columnspan=2)

Button(root, text="(", command=lambda: get_operators(
    "(")).grid(row=6, column=2, sticky=W+E)

Button(root, text=")", command=lambda: get_operators(
    ")")).grid(row=6, column=3, sticky=W+E)

Button(root, text="<-", command=lambda: remove_characters()).grid(row=7,
                                                                  column=0, sticky=W+E, columnspan=2)

Button(root, text="=", command=lambda: calculate()).grid(
    row=7, column=2, sticky=W+E, columnspan=2)

# column = To put the widget in the specified column.
# columnspan = To fix the columns widget will occupy.

# icon name aplication
root.mainloop()
