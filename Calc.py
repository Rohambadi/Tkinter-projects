from tkinter import *

root = Tk()
root.title("Gui Calculator")
root.geometry('280x280')
root.resizable(False, False)

x = ""
equation = StringVar()
calculation = Label(root, font=7, textvariable=equation)
equation.set("Enter your Expression: ")
calculation.grid(columnspan=4)


def btnpress(num):
    global x
    x += str(num)
    equation.set(x)


def btnequalpress():
    global x
    total = str(eval(x))
    equation.set(total)
    x = ""


def btnclearpress():
    global x
    x = ""
    equation.set("Enter your Expression: ")


btn0 = Button(root, text="0", width=7, height=2, command=lambda: btnpress(0))
btn0.grid(row=4, column=0)

btn1 = Button(root, text="1", width=7, height=2, command=lambda: btnpress(1))
btn1.grid(row=1, column=0)

btn2 = Button(root, text="2", width=7, height=2, command=lambda: btnpress(2))
btn2.grid(row=1, column=1)

btn3 = Button(root, text="3", width=7, height=2, command=lambda: btnpress(3))
btn3.grid(row=1, column=2)

btn4 = Button(root, text="4", width=7, height=2, command=lambda: btnpress(4))
btn4.grid(row=2, column=0)

btn5 = Button(root, text="5", width=7, height=2, command=lambda: btnpress(5))
btn5.grid(row=2, column=1)

btn6 = Button(root, text="6", width=7, height=2, command=lambda: btnpress(6))
btn6.grid(row=2, column=2)

btn7 = Button(root, text="7", width=7, height=2, command=lambda: btnpress(7))
btn7.grid(row=3, column=0)

btn8 = Button(root, text="8", width=7, height=2, command=lambda: btnpress(8))
btn8.grid(row=3, column=1)

btn9 = Button(root, text="9", width=7, height=2, command=lambda: btnpress(9))
btn9.grid(row=3, column=2)

plus = Button(root, text="+", width=7, height=2, command=lambda: btnpress('+'))
plus.grid(row=1, column=3)

minus = Button(root, text="-", width=7, height=2, command=lambda: btnpress('-'))
minus.grid(row=2, column=3)

multiply = Button(root, text="*", width=7, height=2, command=lambda: btnpress('*'))
multiply.grid(row=3, column=3)

divid = Button(root, text="/", width=7, height=2, command=lambda: btnpress('/'))
divid.grid(row=4, column=1)

equal = Button(root, text="=", width=7, height=2, command=btnequalpress)
equal.grid(row=4, column=2)

clear = Button(root, text="C", width=7, height=2, command=btnclearpress)
clear.grid(row=4, column=3)

root.mainloop()